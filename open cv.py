import cv2
from pprint import pprint
cap = cv2.VideoCapture(0)
#VideoCapture - захват камерой
while True:
    #ret - получилось ли достать кадр
    #frame - сам кадр
    ret, frame = cap.read()
    print(ret)
    for el in frame:
        for i in el:
            print(i, end='')
        print()

    cv2.imshow('camera', frame)
    # ожидать нажатия клавиши 1 мс
    cv2.waitKey(1)
    break
