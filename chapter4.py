# shapes and texts

import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)   # 0 is for black

# to color image
#img[:]=255,0,0

# to add lines

#       (image,(starting point),(ending point),(color),thickness[optional])
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

# to add rectangle

cv2.rectangle(img,(0,0),(200,300),(0,255,255),2)
#cv2.rectangle(img,(0,0),(200,300),(0,255,255),cv2.FILLED)  # to fill rectangle

# to add circle

#         (image,(center),radius,(color),thickness)
cv2.circle(img,(400,20),30,(255,255,0),5)

# adding text to images

       #   (image,text,origin to start at,font,scale,color,thickness
cv2.putText(img," soha ",(300,300),cv2.FONT_HERSHEY_COMPLEX,1,(0,245,255),2)
cv2.imshow("image",img)
cv2.waitKey(0)