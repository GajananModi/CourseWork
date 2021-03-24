# -*- coding: utf-8 -*-
"""FINAL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/193ubyDMV5ahU85AF-gZZHw2UHr517idM
"""

import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import OneHotEncoder

import numpy as np
import pandas as pd
import cv2

!pip install keras-tuner

training_data = pd.read_csv('/content/drive/My Drive/train.csv')
image_path = "/content/drive/My Drive/ntrain/"
test_path = "/content/drive/My Drive/ntest/"
test_data = pd.read_csv('/content/drive/My Drive/test.csv')

label = np.array(training_data['emotion'])
label= label.reshape(-1,1)
label.shape


encode = OneHotEncoder()
label = encode.fit_transform(label).toarray()
print(label.shape)

width = 128
height = 128
dim = (width, height)

faceImages=[] 
for i in training_data['image_file']:
    idb = image_path + i + ".jpg"
    print(idb)
    img = cv2.imread(idb,0)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    faceImages.append(resized)

jpg_try=[]
for i in test_data['image_file']:
    idb = test_path + i + ".jpg"
    print(idb)
    img = cv2.imread(idb,0)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    jpg_try.append(resized)



images_array = faceImages.copy()



x_train = np.array(faceImages)

x_train = x_train.reshape(len(x_train),128, 128,1)

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.layers import SpatialDropout2D
from keras import regularizers
from keras.layers.normalization import BatchNormalization
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import Adam
from keras.layers import Conv2D , BatchNormalization
from keras.layers import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
from keras import layers
from keras.layers import Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D
from keras.layers import AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D
from keras.models import Model
from keras.initializers import glorot_uniform

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape = (128,128,1)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.25))
model.add(Dense(5, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adamax', metrics=['accuracy'])

print(model.summary())



opt = Adam(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer='adamax', metrics=['accuracy'])
model.fit(x_train, label, epochs=100, batch_size=64)

x_test = np.array(jpg_try) 
x_test = x_test.reshape(len(x_test),128, 128,1)

op = model.predict(x_test)
ans=[]
for i in range(len(op)):
    ans.append(np.argmax(op[i]))

np.savetxt("/content/drive/My Drive/submission1.csv", ans,fmt="%d",header ="emotion",comments='', delimiter=",")