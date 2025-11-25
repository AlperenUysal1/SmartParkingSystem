# Smart Parking System 🅿️

Görüntü işleme teknolojisi kullanarak otopark doluluk durumunu tespit eden ve analiz eden Python tabanlı bir proje.

## 🚀 Özellikler
- **YOLOv8** modelini kullanarak araç tespiti.
- Gerçek zamanlı video işleme.
- Otopark giriş/çıkış takibi ve aktivite günlüğü (`activity_log.txt`).
- Kolay kurulum ve yapılandırma.

## 📂 Proje İçeriği
- `check_setup.py`: Sistem kurulum kontrolü ve ana uygulama dosyası.
- `yolov8n.pt`: Araç tespiti için kullanılan YOLO ağırlık dosyası.
- `requirements.txt`: Gerekli Python kütüphaneleri.
- `activity_log.txt`: Sistem log kayıtları.

## 🛠️ Kurulum

1. Projeyi bilgisayarınıza indirin:
   ```bash
   git clone https://github.com/AlperenUysal1/SmartParkingSystem.git
   cd SmartParkingSystem
   ```

2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. Uygulamayı çalıştırın:
   ```bash
   python check_setup.py
   ```

## 📝 Gereksinimler
- Python 3.x
- Ultralytics (YOLO)
- OpenCV

