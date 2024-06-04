from ultralytics import YOLO
import cv2
import math


def detectVideo(videoName, modelName):
    cap = cv2.VideoCapture("uploaded_videos/" + videoName)

    # Kameradan alınacak görüntünün genişlik ve yüksekliğini alma cap.get(3) genişlik cap.get(4) yükseklik
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Video dosyasını oluşturma ve ayarlarını belirleme
    out = cv2.VideoWriter('detected_videos/' + videoName, cv2.VideoWriter_fourcc(*'mp4v'), 10,
                          (frame_width, frame_height))

    model = YOLO("models/" + modelName)  # Kendi verisetiyle eğittiğim YOLO modelini yükleme

    class_names = model.names  # Modelden sınıf isimlerini al

    class_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]  # Farklı sınıflar için renkler

    while cap.isOpened():  # Video dosyası açık olduğu sürece
        success, img = cap.read()  # Kameradan bir kare okuma

        if not success:
            break  # Eğer kare okunamazsa, döngüyü sonlandır

        # YOLOv8 kullanarak kareleri tespit etme
        results = model(img, stream=True, conf=0.6)

        # Tespit sonuçlarını kontrol etme
        for r in results:
            # Her bir tespit sonucunda sınırlayıcı kutuları alırız
            boxes = r.boxes
            # Her bir sınırlayıcı kutu için işlemleri yapma
            for box in boxes:
                # tespit etiketinin koordinatlarını alıp dikdörtgen çizme
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                class_idx = int(box.cls[0])

                # Sınıf indeksi class_colors listesinin indeks aralığında ise
                if class_idx < len(class_colors):
                    cv2.rectangle(img, (x1, y1), (x2, y2), class_colors[class_idx], 3)  # Her sınıf için farklı renk

                    # Güven değerini alıp yazdırma
                    conf = math.ceil((box.conf[0] * 100)) / 100
                    label = f'{class_names[class_idx]}: {conf}'  # Sınıf ismini ve güven değerini etikete ekle
                    t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]

                    # Etiketin boyutunu hesaplayıp arkaplanı çizme
                    c2 = x1 + t_size[0], y1 - t_size[1] - 3
                    cv2.rectangle(img, (x1, y1), c2, class_colors[class_idx], -1, cv2.LINE_AA)  # Her sınıf için farklı renk

                    # Etiketi yazma
                    cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

        # Görüntüyü video dosyasına yazma
        out.write(img)

    # Video yazma nesnesini serbest bırakma
    out.release()
    cap.release()  # Video( kamera)  kaynağını serbest bırak

    cv2.destroyAllWindows()  # Tüm açık pencereleri kapat
