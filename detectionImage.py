from ultralytics import YOLO
import cv2
import math
import os

def detectImage(img_name, modelName):
    # Fotoğrafı oku
    img = cv2.imread("uploaded_photo/" + img_name)

    model = YOLO("models/" + modelName)  # Kendi verisetiyle eğittiğim YOLO modelini yükleme

    # YOLOv8 kullanarak nesneleri tespit etme
    results = model(img)

    # Modelden tespit edilen sınıfların isimlerini al
    class_names = model.names

    # Farklı sınıflar için farklı renkler
    class_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

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
                class_name = class_names[class_idx]
                label = f'{class_name}: {conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]

                # Etiketin boyutunu hesaplayıp arkaplanı çizme
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1, y1), c2, class_colors[class_idx], -1, cv2.LINE_AA)  # Her sınıf için farklı renk

                # Etiketi yazma
                cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

    # Tespit yapılan fotoğrafı kaydetme
    cv2.imwrite("detected_photo/" + img_name, img)
