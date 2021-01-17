import cv2
import os
os.environ['DISPLAY'] = ':0'

print('Welcome to OpenCV!')

## *****************      reading images

# img = cv2.imread("res/sample_image.png")
# cv2.imshow("sample image", img)
# cv2.waitKey(1000)

## *****************     reading video 

# cap = cv2.VideoCapture("res/sample_video.mp4")

# while True:
#     state, img = cap.read()
#     cv2.imshow("sn6-hop", img)

#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

## ****************    reading webcam

# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)

# while True:
#     state, img = cap.read()
#     cv2.imshow("sn6-hop", img)

#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break