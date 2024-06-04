# YoloV8 ile Nesne Tespiti Projesi

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
git clone https://github.com/kullanici-adi/proje-adi.git
cd proje-adi
```

### 2. Gereksinimleri Yükleyin
```bash
pip install -r requirements.txt
```


