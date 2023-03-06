# MNIST PROBLEM 
import matplotlib.pyplot as plt
from keras.datasets import mnist
import matplotlib.image as mpimg
from keras import models 
from keras import layers
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28, )))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='Adam',
                loss='categorical_crossentropy',
                metrics = ['accuracy'])

# Preprocessing training data
train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32') / 255

# Preprocessing test data
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 225

from keras.utils import to_categorical

train_labels = to_categorical(train_labels)
test_labels  = to_categorical(test_labels)

# Fit the model to its training data
#         Epochs = 5
#         Batch Size = 128
network.fit(train_images, train_labels, epochs=5, batch_size=128)

# Calculate Test loss and Test Accuracy
test_loss, test_acc = network.evaluate(test_images, test_labels)

# Print Test loss and Test Accuracy
print(f"Test Loss: {test_loss}\nTest Accuracy : {test_acc * 100} %")
