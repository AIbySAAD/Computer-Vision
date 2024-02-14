import numpy as np
import cv2

# variables
drawing=False # True when key is pressed otherwise false
ix=-1
iy=-1

# Function
def draw(Event,x,y,flags,params):
  global drawing,ix,iy
  if Event==cv2.EVENT_LBUTTONDOWN:
    drawing =True
    ix,iy=x,y
  elif Event==cv2.EVENT_MOUSEMOVE:
    if drawing ==True:
      cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
  elif Event==cv2.EVENT_LBUTTONUP:
    drawing=False
    cv2.rectangle(img,(ix,iy),(x,y),(0,0,100),-1)
# Showing the image

img=np.zeros((512,512,3))
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw)
while True:
  cv2.imshow('my_drawing',img)
  if cv2.waitKey(1) & 0xFF==27:
    break
cv2.destroyAllWindows()