import numpy as np
import cv2

detector_cascade = cv2.CascadeClassifier("cascade/cascade.xml")

img = cv2.imread("train/tenis.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

boot = detector_cascade.detectMultiScale(gray,1.01, 7)
for(x,y,w,h) in boot:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,00,2))

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()