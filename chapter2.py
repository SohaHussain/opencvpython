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