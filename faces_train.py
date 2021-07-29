import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek','Mindy Kaling','Madonna','Elton John','Jerry Seinfield']

dir = r'C:\Users\sohal\OneDrive\Desktop\face recognition\train'

features = [] # image array of faces
labels = [] # whose face does it belong to
haar = cv.CascadeClassifier('haar_face_detection.xml')

# function to loop over every file in every folder in dir and grab the faces in it and add it to our training set

def create_train():
    for person in people:
        
        # looping over every file
        path = os.path.join(dir , person)
        label = people.index(person)
        
        # looping over every image
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            
            # reading an image
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            
            faces_rect = haar.detectMultiScale(gray , scaleFactor = 1.1, minNeighbors = 4)
            
            for (x,y,w,h) in faces_rect:
                # cropping faces
                faces_roi = gray[y:y+h,x:x+w]
                
                features.append(faces_roi)
                labels.append(label)

create_train()
print(f'length of features list : {len(features)}')
print(f'length of labels list : {len(labels)}')

features = np.array(features,dtype='object')
labels = np.array(labels)

# training our recognizer

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

np.save('features.npy',features)
np.save('labels.npy',labels)

# saving trained model
face_recognizer.save('face_trained.yml')