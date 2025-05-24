# -*- coding: utf-8 -*-
"""
Created on Sat May 24 00:36:47 2025

@author: esram
"""

import torch
import cv2

# YOLOv5s modelini yükle
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Kedi ve köpek sınıf isimleri
hedef_siniflar = ['cat', 'dog']

# Kamera başlat
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Modeli çalıştır
    results = model(frame)

    # Tespit sonuçlarını al
    for *box, conf, cls in results.xyxy[0]:
        etiket = model.names[int(cls)]
        if etiket in hedef_siniflar:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{etiket} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    # Ekrana göster
    cv2.imshow("Kedi ve Köpek Tanıma", frame)

    # ESC tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
