import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=5)

while True:
    success,img = cap.read()
    hands,img = detector.findHands(img)
    cv2.imshow("Image",img)
    cv2.waitkey(1)