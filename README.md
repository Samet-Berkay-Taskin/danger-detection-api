# YoloV8 ile Nesne Tespiti Api'si

Bu proje, YoloV8 modelini kullanarak özel veri setleriyle eğitilmiş dört farklı nesne tespit modeli içermektedir. Bu modeller şunlardır:
1. Silah tespiti
2. Yangın tespiti
3. Kedi ve köpek tespiti
4. YoloV8'in varsayılan modeli (Ultralytics tarafından eğitilmiş)

Proje, Python'da Flask API kullanarak bu modelleri servis eden bir backend ve bu backend'i kullanarak video ve fotoğraflarda nesne tespiti yapan bir React frontend içerir. Kullanıcılar video ve fotoğraflar üzerinde tespit yapabilir, hatta YouTube linki vererek videoyu indirip analiz ettirebilir. Kullanıcılar ayrıca hangi modeli kullanmak istediklerini seçebilirler.

## Modeller
### 1. Silah Tespiti Modeli
Özel bir silah veri seti ile eğitilmiştir ve görüntülerde silah tespiti yapar.

### 2. Yangın Tespiti Modeli
Özel bir alev ve yangın veri seti ile eğitilmiştir ve yangın tespiti yapar.

### 3. Kedi ve Köpek Tespiti Modeli
Özel bir kedi ve köpek veri seti ile eğitilmiştir ve kedi ve köpek tespiti yapar.

### 4. Varsayılan YoloV8 Modeli
Ultralytics tarafından eğitilmiş olan varsayılan YoloV8 modelidir ve genel nesne tespiti yapar.

## Kurulum

Projenin Python backend kısmını çalıştırmak için aşağıdaki adımları izleyin.

### 1. Depoyu Klonlayın

```bash
git clone https://github.com/Samet-Berkay-Taskin/danger-detection-api.git
```

### 2. Gereksinimleri Yükleyin
```bash
pip install -r requirements.txt
```

### 3.Flask API'yi (Backend) Çalıştırın
```bash
python main.py
```

## Kullanım

Flask API'yi çalıştırdıktan sonra, frontend tarafı (React uygulaması) aracılığıyla aşağıdaki işlemleri yapabilirsiniz:

1. **Video ve Fotoğraf Yükleme:** Kullanıcılar video ve fotoğraf yükleyerek nesne tespiti yapabilirler.
2. **YouTube Video Tespiti:** Kullanıcılar YouTube video linki sağlayarak videoyu indirip analiz ettirebilirler.
3. **Model Seçimi:** Kullanıcılar, tespit yapmak istedikleri modeli seçebilirler (silah, yangın, kedi ve köpek, varsayılan YoloV8 modeli).
4. **Sonuçları Görüntüleme ve İndirme:** Tespit yapılmış video ve fotoğrafları görüntüleyebilir ve indirebilirler.


