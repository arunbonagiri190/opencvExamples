import numpy as np
import cv2
import os
os.environ['DISPLAY'] = ':0'

kernel = np.ones((5,5), np.uint8)

img = cv2.imread("res/sample_image.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=3)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow('Orginal Image', img)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dialated Image', imgDialation)
cv2.imshow('Eroded Image', imgEroded)

cv2.waitKey(0)