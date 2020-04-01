from __future__ import absolute_import, division, print_function, unicode_literals
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import numpy as np
import tensorflow as tf

# Setup directories
train_path = "dataset"
train_dir = "dataset/train/"
validation_dir = "dataset/validation"

train_car_dir = os.path.join(train_dir, 'car')
train_person_dir = os.path.join(train_dir, 'person')
train_normal_dir = os.path.join(train_dir, 'normal') 
train_black_dir = os.path.join(train_dir, 'black') 

validation_car_dir = os.path.join(validation_dir, 'car')
validation_person_dir = os.path.join(validation_dir, 'person')
validation_normal_dir = os.path.join(validation_dir, 'normal')
validation_black_dir = os.path.join(validation_dir, 'black')

# Getting total values
total_train = len(os.listdir(train_car_dir)) + len(os.listdir(train_person_dir)) + len(os.listdir(train_normal_dir)) + len(os.listdir(train_black_dir)) 

total_val = len(os.listdir(validation_car_dir)) + len(os.listdir(validation_person_dir)) + len(os.listdir(validation_normal_dir)) + len(os.listdir(validation_black_dir))

# Pre-processing variables
batch_size = 256
epochs = 15
IMG_HEIGHT = 250
IMG_WIDTH = 250

# Data preparation
train_image_generator = ImageDataGenerator(rescale=1./255) 
validation_image_generator = ImageDataGenerator(rescale=1./255)

train_data_gen = train_image_generator.flow_from_directory(
	batch_size=batch_size,
	directory=train_dir,
	shuffle=True,
	target_size=(IMG_HEIGHT, IMG_WIDTH)
)
														      
val_data_gen = validation_image_generator.flow_from_directory(
	batch_size=batch_size,
	directory=validation_dir,
	shuffle=True,
	target_size=(IMG_HEIGHT, IMG_WIDTH)
)

# Create the model
model = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(4)
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
	
# Train the model	
history = model.fit(
    train_data_gen,
    steps_per_epoch=total_train // batch_size,
    epochs=epochs,
    validation_data=val_data_gen,
    validation_steps=total_val // batch_size,
)

# Save the model
model.save('trained_model.h5') 
