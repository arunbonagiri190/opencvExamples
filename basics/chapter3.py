import cv2
import os
os.environ['DISPLAY'] = ':0'





img = cv2.imread('res/sample_image.png')
print("Orginal ", img.shape)

imgResize = cv2.resize(img, (600, 300))
print("Resized ", imgResize.shape)

imgCrop = img[300:390, 0:100]
print("Cropped ", imgCrop.shape)

cv2.imshow("Orginal Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCrop)

cv2.waitKey(20000)
