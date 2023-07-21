# -*- coding: utf-8 -*-
"""nti_ml_CNN_cifar10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17PCbnEaY1v1jh3kiDCVsVsfTl3nJjFq7
"""

from tensorflow.keras import optimizers, datasets, layers
import tensorflow as tf
import matplotlib.pyplot as plt

((train_x, train_y),(test_x, test_y)) = datasets.cifar10.load_data()

train_x.shape

train_x[0]

train_x=train_x.astype('float32')/255

test_x=test_x.astype('float32')/255

train_y[0]

train_y = tf.keras.utils.to_categorical(train_y)
test_y = tf.keras.utils.to_categorical(test_y)

train_y[0]

train_x.shape

import tensorflow as tf

from tensorflow.keras import activations

model1 = tf.keras.Sequential()
model1.add(layers.Conv2D(filters= 32,kernel_size= 5, strides= 1, padding= 'same',activation= tf.nn.relu, input_shape= (32,32,3)))

model1.add(layers.MaxPool2D(pool_size=(2,2), strides= (2,2), padding= 'valid'))

model1.add(layers.Conv2D(filters= 64,kernel_size= 3, strides= (1,1), padding= 'same',activation= tf.nn.relu))
model1.add(layers.MaxPool2D(pool_size=(2,2), strides= (2,2), padding= 'valid'))

model1.add(layers.Dropout(0.25))
model1.add(layers.Flatten())

model1.add(layers.Dense(units= 128, activation= tf.nn.relu))

model1.add(layers.Dropout(0.5))

model1.add(layers.Dense(units= 10, activation= tf.nn.softmax))

train_x.shape

train_x= train_x.reshape(-1,32,32,3)
test_x= test_x.reshape(-1,32,32,3)
model1.compile(optimizer= 'adam', loss= 'categorical_crossentropy', metrics= ['accuracy'])
history=model1.fit(x= train_x, y= train_y, epochs= 10, batch_size= 128)

print(tf.__version__)

score=model1.evaluate(test_x,test_y , batch_size=None, verbose=1,
               sample_weight=None, steps=None, callbacks=None, max_queue_size=10)

print("the accuracy of the model:",score[1]*100,"%")
print("the loss of the model:",score[0])

from  ann_visualizer.visualize import ann_viz
ann_viz(model1, title="neural network",filename='test.gv')

import matplotlib.pyplot as plt

loss = history.history['loss']

# Plot the loss
loss = history.history['loss']
plt.plot(loss, 'g', label='Training loss')
plt.title('Training loss')
plt.xlabel('Epoch')
plt.ylabel('loss')
plt.legend()
plt.show()

accuracy = history.history['accuracy']

# Plot the accuracy
plt.plot(accuracy, 'g', label='Training Accuracy')
plt.title('Training Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim(0.6, 1)
plt.legend()
plt.show()