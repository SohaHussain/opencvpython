# warp perspective

# warp perspective of an image to get its bird eye view

import cv2
import numpy as np

img=cv2.imread("resources/cards.jpg")

width,height = 250,350
# 4 points of a particular card in image
# to get these points open image in paint
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])

# defining these points
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# transformation matrix requires for perspective
matrix=cv2.getPerspectiveTransform(pts1,pts2)

imgout=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("image",img)
cv2.imshow("output",imgout)
cv2.waitKey(0)

