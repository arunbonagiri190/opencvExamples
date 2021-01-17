import cv2
import numpy as np
import os
os.environ['DISPLAY'] = ':0'

img = np.zeros((512, 512,3), np.uint8)

cv2.line(img, (20,300), (480, 300), (255,0,0), 2)
cv2.rectangle(img, (40,100),(460,250), (255,255,0), 1)
cv2.circle(img, (250,70), 30, (0,0,255), 1)
cv2.putText(img, " OpenCV ", (100, 200), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 3)

cv2.imshow("Numpy Image", img)
cv2.waitKey(0)