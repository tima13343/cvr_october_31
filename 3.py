from 1 import YOLO

# Предсказание на новом изображении
model = YOLO('yolov8n.pt')
results = model.predict(source="C:\Users\030\PycharmProjects\cvr\image\train", conf=0.5, save=True)
results.show()  # Показываем изображение с предсказанными объектами