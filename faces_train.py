import os
import cv2 as cv
import numpy as np

people = []

for i in os.listdir(r"C:\Users\User\Desktop\Data Science\Computer Vision\OpenCV_beginners_project\Photos\Resources\Faces\train"):
    people.append(i)

print(people)

DIR = (r"C:\Users\User\Desktop\Data Science\Computer Vision\OpenCV_beginners_project\Photos\Resources\Faces\train")

haar_cascade = cv.CascadeClassifier('haar_face.xml')
features = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()
print('Training done------------------------------')
features = np.array(features, dtype='object')
labels = np.array(labels)
# print(len(f'The leangth of features is {len(features)}'))
# print(len(f'The leangth of features is {len(labels)}'))

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on features and labels list
face_recog = face_recognizer.train(features, labels)
face_recognizer.save("face_train.yml")
np.save('Features.npy', features)
np.save('Lables.pny', labels)
