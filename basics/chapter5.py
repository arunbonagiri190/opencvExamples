import cv2
import numpy as np
import os
os.environ['DISPLAY'] = ':0'

img = cv2.imread("res/sample_image_2.png")
width, height = 94, 146
pts1 = np.float32([[30,68], [124,47], [65,214], [155,190]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
outImage = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Orginal Image", img)
cv2.imshow("Wrap Image", outImage)
cv2.waitKey(1000*20)