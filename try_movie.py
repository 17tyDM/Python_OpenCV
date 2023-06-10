import cv2
import sys

cap = cv2.VideoCapture('./sample.mp4')

if not cap.isOpened():
    sys.exit()

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

cv2.destroyWindow('frame')