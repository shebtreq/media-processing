import sys
import os
import cv2
import time
import numpy as np

cascPaths = []
cascades = []


count = 0
arrayOfPrevObjects = []

#cascPaths.append( (os.path.dirname(os.path.realpath(__file__))) + "/classifiers/body10/haarcascade_fullbody.xml")
#cascPaths.append( (os.path.dirname(os.path.realpath(__file__))) + "/classifiers/basic-face/face-data.xml")
cascPaths.append( (os.path.dirname(os.path.realpath(__file__))) + "/classifiers/frontalFace10/haarcascade_frontalface_default.xml")
cascPaths.append( (os.path.dirname(os.path.realpath(__file__))) + "/classifiers/HS.xml")

for cascPath in cascPaths:
    cascades.append(cv2.CascadeClassifier(cascPath))
video_capture = cv2.VideoCapture(0)
arrayOfColors = np.random.randint(0,255,(len(cascPaths),3))


while True:

    # Capture frame-by-frame
    ret, frame = video_capture.read()
    width = video_capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    height = video_capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
    #Process frame using data
    if count > 5:
        count = 0
        arrayOfPrevObjects = []
        for index in range(len(cascades)):
            faces = cascades[index].detectMultiScale(
                cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            arrayOfPrevObjects.append(faces)
    else:
        count+=1

    # Draw a rectangle around the objects
    for index in range(len(arrayOfPrevObjects)):
        for (x, y, w, h) in arrayOfPrevObjects[index]:
            cv2.rectangle(frame, (x, y), (x+w, y+h), arrayOfColors[index], 2)
            cv2.line(frame, (int(width/2), int(height/2)), (int(x+w/2), int(y+h/2)), arrayOfColors[index], 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)



# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()