import tensorflow as tf
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random

train = []
test = []
x_train = []
y_train = []
x_test = []
y_test = []
#totshape = 0
for i in range(1,101):
    imgpath1 = "UserFaces\\student\\17BCE0038\\" + str(i) + ".jpg"
    imgpath2 = "UserFaces\\faculty\\17BCE2113\\" + str(i) + ".jpg"
    img1 = Image.open(imgpath1)
    npimg1 = np.array(img1,'uint8')
    #totshape+=npimg.shape[0]
    #ARYAMAN CHANGE1 : Changing shape of images from 164X164 to 28X28
    npimg1 = np.resize(npimg1,(28,28))
    npimg1 = tf.keras.utils.normalize(npimg1, axis = 1)

    img2 = Image.open(imgpath2)
    npimg2 = np.array(img2,'uint8')
    #totshape+=npimg.shape[0]
    npimg2 = np.resize(npimg2,(28,28))
    npimg2 = tf.keras.utils.normalize(npimg2, axis = 1)    
    if i<80:
        train.append([npimg1,0])
        train.append([npimg2,1])
    else:
        test.append([npimg1,0])
        test.append([npimg2,1])

random.shuffle(train)
random.shuffle(test)

for feat, labels in train:
    x_train.append(feat)
    y_train.append(labels)

for feat, labels in train:
    x_test.append(feat)
    y_test.append(labels)



x_train = np.array(x_train).reshape(-1 ,784)
y_train = np.array(y_train, 'uint8')

x_test = np.array(x_test).reshape(-1, 784)
y_test = np.array(y_test, 'uint8')
print(x_test.shape)
print(x_test[0].shape)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(784, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(2, activation = tf.nn.softmax))

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
model.fit(x_train, y_train, epochs = 20)
print('asasasasasasasasasasasasasasasas')

pred = model.evaluate(x_test, y_test)
print('Loss = ',str(pred[0]))
print('Test accuracy = ', str(pred[1]))

pred = model.predict(x_test[0])
