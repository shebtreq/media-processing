import cv2
import sys
import os
import time

cascPath = (os.path.dirname(os.path.realpath(__file__))) + "basicFace/face-data.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

count = 0
prevFaces = []

while True:
	# Exit program when q pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Capture frame-by-frame
    ret, frame = video_capture.read()
    #time.sleep(0.05)
    if count > 5:
    	count = 0
    	#Process frame using facial data
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        prevFaces = faces;

    else:
        count+=1
    # Draw a rectangle around the faces
    for (x, y, w, h) in prevFaces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display the resulting frame
    cv2.imshow('Video', frame)





# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
