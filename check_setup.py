import cv2
import torch
from ultralytics import YOLO
import sys

print("X" * 40)
print(f"Python: {sys.version.split()[0]}")
print(f"OpenCV: {cv2.__version__}")
print(f"Torch: {torch.__version__}")
if torch.cuda.is_available():
    print(f"GPU AKTIF: {torch.cuda.get_device_name(0)}")
else:
    print("GPU BULUNAMADI (CPU Modu)")

print("X" * 40)
print("YOLOv8 Modeli test ediliyor...")
try:
    # yolov8n.pt dosyasini indirip yukleyecek
    model = YOLO("yolov8n.pt")
    print("BASARILI: YOLO modeli yuklendi.")
except Exception as e:
    print(f"HATA: {e}")
print("X" * 40)

