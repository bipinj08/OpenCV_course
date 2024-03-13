import cv2 as cv

img = cv.imread('Photos/group.png')
cv.imshow('children', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

'''
* minNeighbours gives number of neighbours rectangle should have to called face.
* Changing the minNeighbours value will give you sensivity of detecting the face.
* lower value increases the sensivity whereas higher value decreases the sensivity 
'''

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Face Detection', img)

cv.waitKey(0)