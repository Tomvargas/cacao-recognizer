from tkinter import *
from PIL import Image, ImageTk #pip install Pillow
import cv2 #pip install opencv-contrib-python
import sys
import numpy as np
import urllib.request

url = 'http://192.168.100.192/cam-lo.jpg'

def callback():
     imgResponse = urllib.request.urlopen(url)
     imgNp = np.array(bytearray(imgResponse.read()), dtype=np.uint8)
     img = cv2.imdecode(imgNp,-1)
     #cv2.imshow(winName, img)
     im = Image.fromarray(img)
     imgtk = ImageTk.PhotoImage(image=im)
     label.configure(image=imgtk)
          
root = Tk()
root.title("Vision Artificial")


callback()
label = Label(root)
label.grid(row=0)

root.mainloop()