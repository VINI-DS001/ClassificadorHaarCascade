import numpy as np
import cv2

flower_cascade = cv2.CascadeClassifier("cascade.xml")

img = cv2.imread("test/Image_503.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

flower = flower_cascade.detectMultiScale(gray,1.01, 7)
for(x,y,w,h) in flower:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,00,2))

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()