#Importing the libraries
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential        #cnn model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as k
from keras import optimizers

img_width, img_height = 224,224
train_data_dir = 'dataset/training_set'
validation_data_dir = 'dataset/test_set'
nb_train_samples = 253
nb_test_samples = 72
epochs = 10
batch_size = 16

if k.image_data_format() == 'channels_first':
    input_shape = (3,img_width,img_height)
else:
    input_shape = (img_width,img_height,3)

#Stage1:
model = Sequential()
model.add(Conv2D(32,(3,3), input_shape = input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

#Stage2:
model.add(Conv2D(32, (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

#Stage3:
model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

#print(model.summary())

#Classification Stage
model.add(Flatten())
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(4))                 
model.add(Activation('softmax'))

#Building the network
model.compile(loss = 'categorical_crossentropy',
            optimizer = optimizers.SGD(lr=0.01),
            metrics = ['accuracy'])

train_datagen = ImageDataGenerator(
    rescale = 1. / 255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1. /255)

#Loading the dataset
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size = (img_width,img_height),
    batch_size = batch_size,
    class_mode = 'categorical'
)

test_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size = (img_width,img_height),
    batch_size = batch_size,
    class_mode = 'categorical'
)

classifier = model.fit(
    train_generator,
    steps_per_epoch = nb_train_samples // batch_size,
    epochs = epochs,
    validation_data = test_generator,
    validation_steps = nb_test_samples // batch_size  
)

#saving the model
import h5py
model.save('Trained_model.h5')

#Plotting the performance of model
print(classifier.history.keys())

import matplotlib.pyplot as plt
plt.plot(classifier.history['accuracy'])
plt.plot(classifier.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(classifier.history['loss'])
plt.plot(classifier.history['val_loss'])
plt.title('Model Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
