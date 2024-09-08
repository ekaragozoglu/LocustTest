# Arama Yük Testi

Bu proje, Locust kullanarak bir web sitesindeki arama özelliğini yük testi yapmayı amaçlamaktadır. Proje, ürün arama taleplerinin performansını değerlendirmek için tasarlanmıştır.

## Açıklama

Proje, belirli anahtar kelimelerle arama yaparak n11.com üzerindeki arama fonksiyonunu test eder. Her arama isteği sonucunda elde edilen yanıtı değerlendirir ve sonuçları ekrana yazdırır.

## Kurulum

Projeyi kullanmak için aşağıdaki adımları takip edebilirsiniz:

**Depoyu Klonlayın:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   
Proje Dizini İçine Girin:
cd path/to/LocustTest

Gerekli Python Paketlerini Yükleyin:
pip install -r requirements.txt

## Kullanım

Locust testi çalıştırmak için aşağıdaki komutu kullanabilirsiniz:
locust -f locustfile.py
