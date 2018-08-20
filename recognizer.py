import cv2
import numpy as np
import pickle

face_cascade = cv2.CascadeClassifier('HCTrainingImages\\haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('training.yml')

cap = cv2.VideoCapture(0)

while True:

    _, img = cap.read()
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)

    for (x,y,w,h) in faces:
        roi_grey = grey[y:y+h, x:x+w]
        font = cv2.FONT_HERSHEY_SIMPLEX
        pred_id, config = recognizer.predict(roi_grey)

        iddict = pickle.load(open('iddict.pkl','rb'))
        for regno,id in iddict.items():
            if id == pred_id:
                pred_regno = regno
            
        cv2.putText(img, str(pred_regno), (x,y), font , 1, (255,0,0), 2)
        #cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.circle(img, (int(x+w/2),int(y+h/2)), int(h/2), (0,255,0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) &0xFF
    if k==27:
           break


cap.release()
cv2.destroyAllWindows()
