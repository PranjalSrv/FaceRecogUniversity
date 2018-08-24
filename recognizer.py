import cv2
import numpy as np
import pickle
import time
face_cascade = cv2.CascadeClassifier('HCTrainingImages\\haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('training.yml')
iddict = pickle.load(open('pickle\\iddict.pkl','rb'))
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
start_time = time.asctime(time.localtime(time.time()))

att_stud = {}
init_faculty = {}

while True:

    _, img = cap.read()
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)

    for (x,y,w,h) in faces:
        roi_grey = grey[y:y+h, x:x+w]
        pred_id, config = recognizer.predict(roi_grey)

        
        for regno,[id,desig] in iddict.items():
            if id == pred_id:
                pred_regno = regno
        colour_desig = tuple([255 if desig == 'student' else 0, 255 if desig == 'faculty' else 0,255 if desig == 'admin' else 0])
        cv2.putText(img, str(pred_regno), (x,y), font , 1, colour_desig, 2)
        cv2.putText(img, str(desig), (x,y+h), font , 1, colour_desig, 2)
        #cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.circle(img, (int(x+w/2),int(y+h/2)), int(h/2), (0,255,0), 2)

        if regno not in att_stud and desig == 'student':
            att_stud[regno] = [desig, time.asctime(time.localtime(time.time()))]

        if regno not in init_faculty and desig == 'faculty':
            init_faculty[regno] = [desig, time.asctime(time.localtime(time.time()))]

    cv2.imshow('img', img)
    k = cv2.waitKey(30) &0xFF
    if k==27:
           break

cap.release()
cv2.destroyAllWindows()
end_time = time.asctime(time.localtime(time.time()))

pickle.dump([att_stud, init_faculty, start_time, end_time],open('pickle\\att.pkl','wb'))
