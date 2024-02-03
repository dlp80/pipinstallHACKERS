import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

DATADIR = "C:/Users/dlapa/Downloads/archive"
CATEGORIES = ["squat", "push up", "plank", "leg raises", "barbell biceps curl"]

IMG_SIZE = 200

#plt.imshow(new_array, cmap="gray")
#plt.show()



training_data = []

def create_Training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category) #PATH TO IMGS DIR
        
        class_num = CATEGORIES.index(category)

        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass #this passes over any broken images

create_Training_data()

print(len(training_data))

import random
random.shuffle(training_data)

for sample in training_data[:10]:
    print(sample[1])

X=[]
y=[]

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1) #we gotta reshape bc of keras
