import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# make sample matrix
image = tf.constant([[[[4],[3]],[[2],[1]]]], dtype=np.float32)

# 2 by 2 matrix에 maxpool 적용 
pool = keras.layers.MaxPool2D(pool_size=(2,2),strides=1,padding='valid')(image)
print(pool.shape)
# (1,1,1,1)로 pooling을 통해 matirx 크기 감소 확인
print(pool.numpy())
# 결과 [[[[4.]]]] 출력으로 maxpool 적용 확인

# 2 by 2 결과 얻기 -> matrix에 zero-padding을 통해 진행
pool = keras.layers.MaxPool2D(pool_size=(2,2),strides=1,padding='same')(image)
# zero padding을 통해 matrix 감소를 막는다

print(pool.shape)
# (1,2,2,1)로 matrix 크기 동일함을 확인 가능
print(pool.numpy())
# 2 by 2의 형태의 matrix로 출력 확인
