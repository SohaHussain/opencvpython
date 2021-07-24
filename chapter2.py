# basic functions

import cv2

# loading image
img = cv2.imread('resources/lena.png')

# now we will convert this image into gray scale

# cvtColor converts our image into different color spaces
# BGR is for blue green red
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# displaying image
cv2.imshow("gray image",imggray)
cv2.waitKey(0)

# now we will blur image

# 7,7 is the kernel size . it has to be odd number
# 0 is our sigmaX
imgblur=cv2.GaussianBlur(imggray,(7,7),0)
cv2.imshow("blur image",imgblur)
cv2.waitKey(0)

# edge detector

# 100 and 100 are threshold values
imgcan=cv2.Canny(img,100,100)
cv2.imshow("edged image",imgcan)
cv2.waitKey(0)