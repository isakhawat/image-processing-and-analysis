# -*- coding: utf-8 -*-
"""CNN Basic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1roSllVZq6hIGlXnpMy-HzSKeoadf_vO3

#What Is a Convolutional Neural Network?

it uses two operations called ‘convolution’ and pooling’ to reduce an image into its essential features, and uses those features to understand and classify the image.

### The basic building blocks of CNN are:

**Convolution layer**━ a “filter”, sometimes called a “kernel”, is passed over the image, viewing a few pixels at a time (for example, 3X3 or 5X5).

**Activation layer** ━ the convolution layer generates a matrix that is much smaller in size than the original image. This matrix is run through an activation layer, which introduces non-linearity to allow the network to train itself via backpropagation. The **activation function is typically ReLu.**

**Pooling layer** ━ “pooling” is the process of further downsampling and reducing the size of the matrix. 

**"পুলিং" ম্যাট্রিক্সের আকার আরও কমিয়ে নেওয়ার প্রক্রিয়া।**

**Fully connected layer** ━ a traditional multilayer perceptron structure. Its input is a one-dimensional vector representing the output of the previous layers.

# Build a CNN in Keras in Only 11 Lines

### 1.Defining the model

**Sequential() function :** It add layers on one by one.
"""

model = Sequential()

"""**Keras Conv2D function :** to create a 2-dimensional convolutional layer . with kernel size (filter) of 5X5 pixels and a stride of 1 in x and y directions. 

The Conv2D command automatically creates the activation function for you━here we use ReLu activation.
"""

model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
                 activation='relu',
                 input_shape=input_shape))

"""Then use the **MaxPooling2D function** to add a 2D max pooling layer, with pooling filter sized 2X2 and stride of 2 in x and y directions."""

model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

"""Add **one more convolution and pooling layers** ━this time the convolution has 64 filters:"""

model.add(Conv2D(64, (5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

"""**Finally**, flatten the output and define the** fully connected layers** that generate probabilities for the ten prediction labels (0.9, the possible values of every written digit):"""

model.add(Flatten())
model.add(Dense(1000, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

"""###2.Compile and training the CNN
 **model.compile()** command. 
 
*** Select cross entropy 
 
 *** loss function, 
 
*** Adam optimizer with learning rate 0.01, 
 
*** accuracy as your metric to evaluate performance.
"""

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01),
              metrics=['accuracy'])

"""Now train it using **model.fit()**, passing the training and testing dataset, and specifying your batch size and number of epochs for training."""

model.fit(x_train, y_train,
          batch_size=128,
          epochs=10,
          verbose=1,
          validation_data=(x_test, y_test),
          callbacks=[history])

"""###3.Evaluating performance
The results look like this:

3328/60000 [>.............................] - ETA: 87s - loss: 0.2180 - acc: 0.9336
3456/60000 [>.............................] - ETA: 87s - loss: 0.2158 - acc: 0.9349
...
Use the evaluate() function to evaluate the performance of the model, using accuracy as we defined previously:
"""

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

"""#Advanced CNN in TensorFlow

# CNN: How to Build One in Keras

CNNs are **primarily used** for **computer vision**, powering tasks like **image classification**, **face recognition**, identifying and classifying everyday objects, and image processing in robots and autonomous vehicles. They are also used for **video analysis and classification**, **semantic parsing**, automatic caption generation, search query retrieval, **sentence classification**, and more.

**How CNNs Works**

A CNN operates in three stages. The first is a convolution, in which the image is “scanned” a few pixels at a time, and a feature map is created with probabilities that each feature belongs to the required class (in a simple classification example). The second stage is pooling (also called downsampling), which reduces the dimensionality of each feature while maintaining its most important information. The pooling stage creates a “summary” of the most important features in the image.

Most CNNs use “max pooling”, in which the highest value is taken from each pixel area scanned by the CNN, as illustrated below.

**1.Load the MNIST dataset**
nd split into train and test sets, with X_train and X_test containing the training and testing images, and y_train and y_test containing the “ground truth” of the digits represented in the images. In the MNIST data set 60,000 images are used for training and 10,000 for testing/validation (learn more about neural network bias and variance in our neural network guide).
"""

# Load the MNIST dataset
from keras.datasets import mnist

# split into train set with X_train and y_train  
# and test sets X_test  and y_test
(X_train, y_train), (X_test, y_test) = mnist.load_data()

"""**2. View** 

**plt.imshow:** view one of the images  

**.shape function :** using the size

understand what the dataset looks like. Try this on several images. As you will see, all the MNIST images are uniformly 28 x 28 pixels in size and contain handwritten digits.
"""

import matplotlib.pyplot as plt
plt.imshow(X_train[0])
X_train[0].shape

"""**3. Reshape**

**Two set of image:**, X_train and X_test, 

to the shape expected by the CNN model. The Keras reshape function takes **four arguments**: 

**number of training images:** 60000

 **pixel size :** 28*28
 
** Image depth :** —use 1 to indicate a grayscale image.
"""

X_train = X_train.reshape(60000,28,28,1)
X_test = X_test.reshape(10000,28,28,1)