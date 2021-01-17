import cv2
import numpy as np
import os
os.environ['DISPLAY'] = ':0'

# paths
cocoNamesPath = '../res/coco.names' 
configPath = '../res/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = '../res/frozen_inference_graph.pb'

# loading labels
classLabels = []
with open(cocoNamesPath, 'rt') as cocoFile:
    classLabels = cocoFile.read().rstrip('\n').split('\n')

# building model
model = cv2.dnn_DetectionModel(weightsPath, configPath)
model.setInputSize(340, 340)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

#img = cv2.imread("../res/faces.png")
cap = cv2.VideoCapture(0)

while True:

    success, img = cap.read()
    classIds, confdns, bbox = model.detect(img, confThreshold=0.6)
    
    #print("classIds: ", len(classIds), " box: ",len(bbox))

    if len(classIds) > 0:
        # print("labels", classIds)
        for classId, confd, box in zip(classIds.flatten(), confdns.flatten(), bbox):
            if classId <81:
                cv2.rectangle(img, box, (0, 255, 0), 2)
                cv2.putText(img, classLabels[classId-1].upper(), (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX
                            ,1, (0,0,255), 2)

    cv2.imshow("Output", img)
    cv2.waitKey(1)