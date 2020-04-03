import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

image = tf.constant([[[[1],[2],[3]],
[[4],[5],[6]],
[[7],[8],[9]]]], dtype=np.float32)
print(image.shape) #shape print (1,3,3,1) => 4 dimension data
plt.imshow(image.numpy().reshape(3,3),cmap='Greys') #numpy image show with reshape 1,3,3,1 to 3,3 and color map grey
plt.show()


# 2 by 2 filter 적용
weight = np.array([[[[1.]],[[1.]]],[[[1.]],[[1.]]]]) # make filter(=mask) "." mean float data

print("weight.shape", weight.shape)#(2,2,1,1) matrix
weight_init = tf.constant_initializer(weight) #initialize with weight matrix

conv2d = keras.layers.Conv2D(filters=1, kernel_size=2, padding='valid', kernel_initializer=weight_init)(image)
#filter count, filter_size, not padded
#option 'same' for zero-padding

print("conv2d.shape", conv2d.shape)
print(conv2d.numpy().reshape(2,2))
plt.imshow(conv2d.numpy().reshape(2,2),cmap='gray')
plt.show()

# 2by 2 filter width padding

weight = np.array([[[[1.]],[[1.]]],[[[1.]],[[1.]]]]) # make filter(=mask) "." mean float data

print("weight.shape", weight.shape)#(2,2,1,1) matrix
weight_init = tf.constant_initializer(weight) #initialize with weight matrix

conv2d = keras.layers.Conv2D(filters=1, kernel_size=2, padding='same', kernel_initializer=weight_init)(image)
#filter count, filter_size, zero-padding

print("conv2d.shape", conv2d.shape)
print(conv2d.numpy().reshape(3,3))
plt.imshow(conv2d.numpy().reshape(3,3),cmap='gray')
plt.show()

# 3 channel filter 적용
weight = np.array([[[[1.,10.,-1.]],[[1.,10.,-1.]]],[[[1.,10.,-1.]],[[1.,10.,-1.]]]]) # make filter(=mask) "." mean float data

print("weight.shape", weight.shape)#(2,2,1,3) matrix, lastone mean channel count
weight_init = tf.constant_initializer(weight) #initialize with weight matrix

conv2d = keras.layers.Conv2D(filters=3, kernel_size=2, padding='same', kernel_initializer=weight_init)(image)
#filter count, filter_size, zero-padding

print("conv2d.shape", conv2d.shape)
feature_maps=np.swapaxes(conv2d,0,3) # 3channel 적용 결과를 출력하기 위해 27개 결과를 9개 단위로 나눔
for i, feature_map in enumerate(feature_maps):
    print(feature_map.reshape(3,3))
    plt.subplot(1,3,i+1)
    plt.imshow(feature_map.reshape(3,3),cmap='gray')
plt.show()