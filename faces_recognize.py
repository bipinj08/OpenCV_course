import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
features = np.load('Features.npy', allow_pickle=True)
labels = np.load('Lables.pny.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_train.yml')

img = cv.imread('Photos/Resources/Faces/val/ben_afflek/3.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Madonna', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
for (x,y,w,h) in faces_rect:
    face_roi = gray[y:y+w, x:x+h]

    label, confidence = face_recognizer.predict(face_roi)
    print(f'Label: {people[label]} with the Confidence: {confidence}')

    cv.putText(img, str(people[label]), (25, 25), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow('Detected Face: ', img)

cv.waitKey(0)