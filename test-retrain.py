import os
import numpy as np
from keras.preprocessing import image
from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.models import Sequential
from keras.layers import Dense, GlobalAveragePooling2D

# Load the InceptionV3 model without the final classification layer
base_model = InceptionV3(weights='imagenet', include_top=False)

# Build a custom model on top of the InceptionV3 base model
model = Sequential()
model.add(base_model)
model.add(GlobalAveragePooling2D())
model.add(Dense(1024, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # Binary classification, so output layer has 1 neuron with sigmoid activation

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Directory path containing images
image_folder_path = 'C:/Users/dlapa/Downloads/archive/archive/squat'

# Get all image files in the folder
image_files = [f for f in os.listdir(image_folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Process each image in the folder
for image_file in image_files:
    # Load and preprocess the image
    img_path = os.path.join(image_folder_path, image_file)
    img = image.load_img(img_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = preprocess_input(np.expand_dims(img_array, axis=0))

    # Make predictions
    predictions = model.predict(img_array)

    # Interpret the predictions
    result = "Squat" if predictions[0][0] >= 0.5 else "Not a Squat"
    confidence = predictions[0][0] if result == "Squat" else 1 - predictions[0][0]
    
    # Print the classification
    print(f'{image_file}: {result} (Confidence: {confidence:.2f})')

