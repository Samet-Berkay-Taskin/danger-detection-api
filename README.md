# YoloV8 ile Nesne Tespiti Api'si

Bu proje, backend ve frontend olmak üzere iki aşamadan oluşmaktadır. Bu repository, projenin backend kısmını içermektedir. Ancak projeyi tamamlayabilmek için frontend kısmını da kurmanız gerekmektedir. Frontend kodlarına [BU LİNKTEN](https://github.com/Samet-Berkay-Taskin/danger-detection-react-app)
 ulaşabilir ve projeyi tamamlayabilirsiniz.

Projede, YOLOv8 modeli kullanılarak geliştirilmiş bir nesne tespit uygulaması bulunmaktadır. Bu uygulama, belirli nesneleri tanıyan dört farklı model içermektedir. Backend kısmı, Flask API kullanılarak Python ile geliştirilmiştir. Bu backend, kullanıcının yüklediği videoları ve fotoğrafları işleyebilir ve seçilen modelle nesne tespiti yapabilir. Ayrıca, YouTube'dan video linki alıp, videoyu indirip ve bu videodaki nesneleri de tespit edebilir.

Frontend kısmı ise React ile geliştirilmiştir. Kullanıcılar, web arayüzü üzerinden videoları ve fotoğrafları yükleyebilir, YouTube'dan video linki verebilir ve tespit sonuçlarını görüntüleyebilir veya indirebilirler. Ayrıca, hangi modelin kullanılacağını seçme seçeneği bulunmaktadır.

Bu proje, nesne tespiti alanında geniş bir kullanım alanına sahiptir ve kullanıcıların çeşitli ihtiyaçlarını karşılamak için esnek bir yapıya sahiptir. Özel veri setleriyle eğitilmiş modellerle özelleştirilmiş tespitler yapılabilir veya genel amaçlı bir model tercih edilebilir.


## Modeller
### 1. Silah Tespiti Modeli
Özel bir silah veri seti ile eğitilmiştir ve görüntülerde silah tespiti yapar.   [Bu linkten Tabanca Modeli Eğitimi Reposuna gidebilirsiniz](https://github.com/Samet-Berkay-Taskin/YOLOv8-Training-with-custom-data-Pistol-Detection-)

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

Flask API'yi çalıştırdıktan sonra, frontend tarafını kurup (React uygulaması) aşağıdaki işlemleri yapabilirsiniz:

1. **Video ve Fotoğraf Yükleme:** Kullanıcılar video ve fotoğraf yükleyerek nesne tespiti yapabilirler.
2. **YouTube Video Tespiti:** Kullanıcılar YouTube video linki sağlayarak videoyu indirip analiz ettirebilirler.
3. **Model Seçimi:** Kullanıcılar, tespit yapmak istedikleri modeli seçebilirler (silah, yangın, kedi ve köpek, varsayılan YoloV8 modeli).
4. **Sonuçları Görüntüleme ve İndirme:** Tespit yapılmış video ve fotoğrafları görüntüleyebilir ve indirebilirler.



