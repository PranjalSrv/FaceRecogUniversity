from PIL import Image
import os
import cv2
import numpy as np
import pickle

recognizer = cv2.face.LBPHFaceRecognizer_create()
im_path = ['UserFaces\\student' , 'UserFaces\\faculty' , 'UserFaces\\admin']
im_path_all = []
for i in im_path:
    for j in os.listdir(i):
        im_path_all.append(i + '\\' + j)


def getImagesId(path):
    imagepaths_1 = []
    for path in im_path_all:
        if len(os.listdir(path))>0:
            imagepaths_1.append([os.path.join(path, imageid) for imageid in os.listdir(path)])


        imagepaths = []
        for sublist in imagepaths_1:
            for item in sublist:
                imagepaths.append(item)
        faces = []
        ids = []
        desig = []
        desig.append(path.split('\\')[1])
        for imagepath in imagepaths:
            faceimg = Image.open(imagepath).convert('L')
            npface = np.array(faceimg,'uint8')
            ID = os.path.split(imagepath)[0].split('\\')[2]
            faces.append(npface)
            ids.append(ID)

    return(faces, ids, desig)

faces,ids,desig = getImagesId(im_path)
index = 0
iddict = {}
train_ID = []
for id in ids:
    if id not in iddict:
        iddict[id]=[index, desig[0]]
        index+=1
for id in ids:
    train_ID.append(iddict.get(id)[0])


pickle.dump(iddict,open('pickle\\iddict.pkl','wb'))

recognizer.train(faces, np.array(train_ID))
recognizer.save('training.yml')
cv2.destroyAllWindows()
