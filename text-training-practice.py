#first neural network practice - from text based data

import numpy as np
from numpy import loadtxt
import tensorflow as tf 
from keras.models import Sequential
from keras.layers import Dense, Input, Flatten, Conv2D, MaxPool2D
from tensorflow.python import keras

from keras.datasets import cifar10
from keras.losses import SparseCategoricalCrossentropy 
#from keras.utils.np_utils import to_categorical 

# a sequential model is a linear pile of layers
model = Sequential([
          Input(shape=(32,32,3,)),
          Conv2D(filters=6, kernel_size=(5,5), padding="same", activation="relu"),
          MaxPool2D(pool_size=(2,2)),
          Conv2D(filters=16, kernel_size=(5,5), padding="same", activation="relu"),
          MaxPool2D(pool_size=(2, 2)),
          Conv2D(filters=120, kernel_size=(5,5), padding="same", activation="relu"),
          Flatten(),
          Dense(units=84, activation="relu"),
          Dense(units=10, activation="softmax"),
      ])
 
print (model.summary())

(trainX, trainY), (testX, testY) = cifar10.load_data()
model.compile(optimizer="adam", loss= SparseCategoricalCrossentropy(), metrics="acc")
 
history = model.fit(x=trainX, y=trainY, batch_size=256, epochs=10, validation_data=(testX, testY))
