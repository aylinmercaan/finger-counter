# Parmak Sayma Sistemi (Finger Counter)

OpenCV ve MediaPipe kullanarak canlı kamera görüntüsü üzerinden el parmaklarını tespit edip sayan bir Python projesi.

## Özellikler

- Canlı kamera akışı üzerinden gerçek zamanlı el tespiti
- MediaPipe landmark modeliyle 21 nokta tespiti ve çizimi
- Parmak uçları ile eklem noktaları karşılaştırılarak açık/kapalı parmak tespiti
- Başparmak dahil toplam parmak sayımı
- Ekran üzerinde anlık sayı gösterimi

## Kullanılan Teknolojiler

- Python
- OpenCV
- MediaPipe

## Kullanım

Kamera açıldıktan sonra elinizi kameraya gösterin. Ekranda parmak sayısı anlık olarak güncellenecektir. Çıkmak için `q` tuşuna basabilirsiniz.

## Bilinen Sınırlamalar

Bu proje şu anda temel bir versiyon (v1) durumundadır ve aşağıdaki sınırlamalara sahiptir:

- **Tek el desteği:** Sistem şu an yalnızca tek eli okuyabilmektedir. İki el aynı anda gösterildiğinde tutarlı sonuç alınamayabilir.
- **Avuç içi yönü:** Başparmak sayımı yalnızca avuç içi kameraya dönükken doğru çalışmaktadır. Avuç dışa dönük olduğunda başparmak tespiti hatalı sonuç verebilir.
- **El açısı:** Elin dik ve kameraya düz şekilde tutulduğu varsayılmıştır. Farklı açılarda tutulan ellerde doğruluk düşebilir.

## Gelecek Geliştirmeler

- [ ] İki el desteğinin sağlıklı hale getirilmesi
- [ ] Avuç içi/dışı yönünden bağımsız başparmak tespiti
- [ ] Sol/sağ el için ayrı ayrı parmak sayısı gösterimi
- [ ] Farklı el açılarında doğruluğun artırılması

## Lisans

Bu proje kişisel öğrenme ve portfolyo amaçlı geliştirilmiştir.
