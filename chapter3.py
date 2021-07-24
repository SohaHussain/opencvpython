# Resizing and Cropping

# in openCV the positive x axis is towards east but positive y axis is towards the south

import cv2

# resizing

img=cv2.imread("resources/lambo.png")
print(img.shape)    # to find size of image (height,width,channel(bgr))
imgres=cv2.resize(img,(300,200))
                 #    (width,height)
cv2.imshow("image",img)
cv2.imshow("resized",imgres)
cv2.waitKey(0)

# cropping

imgcrop=img[0:200,200:500] # [height,width]
cv2.imshow("cropped",imgcrop)
cv2.waitKey(0)