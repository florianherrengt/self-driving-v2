import cv2
import urllib.request
import numpy as np

stream = urllib.request.urlopen('http://192.168.1.131:8000/stream.mjpg')
bytes = bytes()
while True:
    bytes += stream.read(1024)
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    if a != -1 and b != -1:
        jpg = bytes[a:b+2]
        bytes = bytes[b+2:]
        video = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
        video = cv2.adaptiveThreshold(video, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,3)
        cv2.imshow('video', video)
        if cv2.waitKey(1) == 27:
            exit(0)