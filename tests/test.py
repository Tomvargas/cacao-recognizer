from tkinter import *
from PIL import Image, ImageTk #pip install Pillow
import cv2 #pip install opencv-contrib-python
import numpy as np
import urllib.request
import sys

url = 'http://192.168.100.192/cam-lo.jpg'

winName = 'CAM'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)
scale_percent = 80

while(1):
    imgResponse = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResponse.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp,-1)
    cv2.imshow(winName, img)

    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break

cv2.destroyAllWindows()


