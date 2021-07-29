import numpy as np
import cv2 as cv

people = ['Ben Afflek','Mindy Kaling','Madonna','Elton John','Jerry Seinfield']
haar = cv.CascadeClassifier('haar_face_detection.xml')

#features = np.load('features.npy')
#labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\sohal\OneDrive\Desktop\face recognition\val\madonna_\4.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('person',gray)

# detecting 

faces_rect = haar.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    # predicting
    label , confidence = face_recognizer.predict(faces_roi)
    print(f'label : {people[label]} with confidence {confidence}')
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=2)

cv.imshow('detected person',img)
cv.waitKey(0)

               