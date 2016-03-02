import base64
import time
#from urllib2 import urlopen
import urllib2
#import urllib2 as urllib2module
import cv2
import numpy as np
from matplotlib import pyplot
"""
Examples of objects for image frame aquisition from both IP and
physically connected cameras
Requires:
 - opencv (cv2 bindings)
 - numpy
"""
class IpCamera(object):
    def __init__(self, url, user=None, password=None):
        self.url = url
        auth_encoded = base64.encodestring('%s:%s' % (user, password))[:-1]
        print self.url
        self.req = urllib2.Request(self.url)
        self.req.add_header('Authorization', 'Basic %s' % auth_encoded)
    def get_frame(self):
        print "bla"
        response = urllib2.urlopen(self.req)
        print "bla1"
        print response
        cv2.imwrite("/home/strq/thesis/yolo.jpg", response)
        img_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
        print "bla2x"
        frame = cv2.imdecode(img_array, 1)
        print "bla3"
        return frame
class Camera(object):
    def __init__(self, camera=0):
        self.cam = cv2.VideoCapture(camera)
        if not self.cam:
            raise Exception("Camera not accessible")
        self.shape = self.get_frame().shape
    def get_frame(self):
        _, frame = self.cam.read()
        return frame
		
ipcamera = IpCamera("http://192.168.0.100/image")
frame = ipcamera.get_frame()

#print frame
#pyplot.imsave("yolo.jpg", frame)
cv2.imwrite("/home/strq/thesis/yolo.jpg", frame)

cv2.imshow('frame', frame)
video_capture.release()
cv2.destroyAllWindows()
