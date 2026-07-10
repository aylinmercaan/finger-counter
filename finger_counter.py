import cv2
import time
import mediapipe as mp
from mediapipe.tasks.python import vision

cap = cv2.VideoCapture(0)

options = vision.HandLandmarkerOptions(
    base_options = mp.tasks.BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=vision.RunningMode.VIDEO
)

detector = vision.HandLandmarker.create_from_options(options)

HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),
    (0,17)
]

pTime = 0
cTime = 0

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    h, w, c = frame.shape
    
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGB)
    frame_timestamp_ms = int(time.time()*1000)
    
    results = detector.detect_for_video(mp_image, frame_timestamp_ms)

    count = 0

    if results.hand_landmarks:
        for idx, handLms in enumerate(results.hand_landmarks):
            points = [(int(lm.x*w), int(lm.y*h)) for lm in handLms]

            hand_label = results.handedness[idx][0].category_name
            
            for start, end in HAND_CONNECTIONS:
                cv2.line(frame, points[start], points[end], (0,0,0), 2)

            tip_ids = [8, 12, 16, 20]
            ref_ids = [6, 10, 14, 18]
            for tip_id, ref_id in zip(tip_ids, ref_ids):
                tip_x, tip_y = points[tip_id]
                ref_x, ref_y = points[ref_id]
                
                if tip_y < ref_y:
                    count += 1

            thumb_tip_x, _ = points[4]
            thumb_ref_x,_ = points[2]


            if hand_label == 'Right':
                if thumb_tip_x > thumb_ref_x:
                    count += 1
            else:
                if thumb_tip_x < thumb_ref_x:
                    count += 1

        cv2.putText(frame, "Hand: "+ hand_label ,(10,145), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 5)

                
    cv2.putText(frame, "Finger Count: "+ str(count) ,(10,110), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 5)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(frame, "FPS: "+ str(int(fps)),(10,75), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 5)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) &0xFF == ord("q"):
        break

detector.close()
cap.release()
