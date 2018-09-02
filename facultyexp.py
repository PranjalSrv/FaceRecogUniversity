
import pickle
import cv2


all_att = pickle.load(open('pickle\\all_att.pkl', 'rb'))

def unlock(authregno):

    cap = cv2.VideoCapture(0)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('training.yml')
    iddict = pickle.load(open('pickle\\iddict.pkl','rb'))
    face_cascade = cv2.CascadeClassifier('HCTrainingImages\\haarcascade_frontalface_default.xml')
    font = cv2.FONT_HERSHEY_SIMPLEX

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
                    pred_desig = desig
                    if pred_regno == authregno:
                        cv2.putText(img, str(pred_regno + ': Authenticated'), (x,y), font , 1, (0,255,0), 2)
                        return True
        
        cv2.imshow('img', img)
        k = cv2.waitKey(30) &0xFF
        if k==27:
            break


def explore(regno):
    print("Exploring")


##k = 0  ##d
##l = 30  ##d
##allfac = []
##
##for att in list(all_att):
##    if k%2 == 0:  ##d
##        c = l+k  ##d
##    att[1] = {str(c):['faculty',1234]}   ##d
##    print(att[1])                        ##d
##    allfac.append(list(att[1].keys())[0])
##    k+=1  ##d


#allfac = list(set(allfac))

choice = input("Enter Registration No.: ")
allowed = unlock(choice)
if allowed == True:
    print("Unlocked")
    explore(choice)
            











