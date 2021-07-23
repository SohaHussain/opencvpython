# chapter 1: read images , videos and webcam
import cv2

#img = cv2.imread("resources/lena.png")  # function to read images // in brackets add path of image
#cv2.imshow("output", img)  # function to display image . 1st argument is name of window and second is image

# the image will appear for just a few milliseconds
# to delay display time
#cv2.waitKey(0)   # 0 is for infinite time

# importing video
cap = cv2.VideoCapture("resources/test_video.mp4")   # function to import video

# since video is just a sequence of images so we will need a while loop to go through each frame one by one
while True:
    success,img = cap.read()  # this will save our image in variable img and then it will tell us if it was done
                              # successfully or not. success variable is a boolean
    cv2.imshow("video",img)   # to display
    if cv2.waitKey(1) & 0xFF==ord('q'): # going to add delay and wait for the keyboard q press to break out of the loop
        break






