import cv2
import numpy as np
import os
os.environ['DISPLAY'] = ':0'

faceCascade = cv2.CascadeClassifier("res/haarcascade_frontalface_default.xml")

img = cv2.imread("res/faces.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
        
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)
    cv2.imshow('Faces',img)
    cv2.waitKey(10000)

# cap = cv2.VideoCapture(0)
# cap.set(3,1200)
# cap.set(4,800)
# cap.set(10,100)

# while True:
#     state, img = cap.read()
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)

#     cv2.imshow('Faces',img)
#     cv2.waitKey(1)
#     # if cv2.waitKey(1) & 0xFF ==ord('q'):
#     #     break
