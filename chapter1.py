#chapter 1: read images , videos and webcam
import cv2

img = cv2.imread("resources/lena.png")  # function to read images // in brackets add path of image
cv2.imshow("output", img)  # function to display image . 1st argument is name of window and second is image
# the image will appear for just a few milliseconds
# to delay display time
cv2.waitKey(0) # 0 is for infinite time





