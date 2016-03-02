import sys
import os
import cv2
import time
import numpy as np

cascPaths = []
cascades = []
scaleFactor = 0.3
scaleMulti = 1/scaleFactor

count = 0
arrayOfPrevObjects = []

cascPaths.append( (os.path.dirname(os.path.realpath(__file__))) + "/classifiers/frontalFace10/haarcascade_frontalface_default.xml")
cascPaths.append( (os.path.dirname(os.path.realpath(__file__))) + "/classifiers/HS.xml")

for cascPath in cascPaths:
    cascades.append(cv2.CascadeClassifier(cascPath))
video_capture = cv2.VideoCapture(0)
arrayOfColors = np.random.randint(0,255,(len(cascPaths),3))

windowName = "Detect Faces"
cv2.startWindowThread()
cv2.namedWindow(windowName)

while True:

    # Capture frame-by-frame
    ret, frame = video_capture.read()
    width = video_capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    height = video_capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
    smallframe = cv2.resize(frame, None, None, scaleFactor, scaleFactor)


    #Process frame using data
    if count > 5:
        count = 0
        arrayOfPrevObjects = []
        for index in range(len(cascades)):
            detections = cascades[index].detectMultiScale(
                cv2.cvtColor(smallframe, cv2.COLOR_BGR2GRAY),
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            arrayOfPrevObjects.append(detections)
    else:
        count+=1

    # Draw a rectangle around the objects
    for index in range(len(arrayOfPrevObjects)):
        for (x, y, w, h) in arrayOfPrevObjects[index]:
            x, y, w, h = int(x*scaleMulti), int(y*scaleMulti), int(w*scaleMulti), int(h*scaleMulti)
            cv2.rectangle(frame, (x, y), (x+w, y+h), arrayOfColors[index], 2)
            cv2.line(frame, (int(width/2), int(height/2)), (int(x+w/2), int(y+h/2)), arrayOfColors[index], 2)

    # Display the resulting frame
    cv2.imshow(windowName, frame)


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
