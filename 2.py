from ultralytics import YOLO

# Загружаем предобученную модель YOLOv8
model = YOLO('best.pt')  # Выберите размер модели: n, s, m, l, x
metrics = model.val()
print(metrics)