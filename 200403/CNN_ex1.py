import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

mnist= keras.datasets.mnist
class_names = ['0','1','2','3','4','5','6','7','8','9']
# 전처리만 수행하므로 classname이 사용되진 않았다

#data load
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.astype(np.float32)/255 #0~1사이 값으로 scaling
test_images = test_images.astype(np.float32)/255

img = train_images[0] 
plt.imshow(img,cmap='gray')
plt.show()

# convolution layer
img=img.reshape(-1,28,28,1) 
# data를 4차원으로 변환, 원본 28*28pixel image
# reshape에 -1을 주게 되면 뒤의 값을 기준으로 해당 값을 자동 설정해준다
# 지금의 경우 28*28, 1 channel image 한개를 사용하므로 -1은 자동으로 1로 변환이 된다
img = tf.convert_to_tensor(img) 
# tensor로 변환

weight_init=keras.initializers.RandomNormal(stddev=0.01)
# filter로 활용할 난수 tensor
# 정규 분포를 따르고, 난수의 평균 mean(default=0), 표준편차 stddev(default=0.05) 설정 가능
conv2d = keras.layers.Conv2D(filters = 5, kernel_size=3, strides=2, padding='same',kernel_initializer=weight_init)(img)
# stride를 2(=(2,2))로 설정했기 때문에, 두 칸씩 이동, convolution을 할 것이다
# 결과의 크기 역시 절반으로 감소할 것이다
print(conv2d.shape)
# (1,14,14,5)로 예상되는 결과 출력
feature_maps=np.swapaxes(conv2d,0,3)
for i,feature_map in enumerate(feature_maps):
    plt.subplot(1,5,i+1), plt.imshow(feature_map.reshape(14,14),cmap='gray')
    # 감소한 크기 기준으로 출력
plt.show()

# pooling layer
pool = keras.layers.MaxPool2D(pool_size=(2,2),strides=2,padding='same')(conv2d)
# 마찬가지로 stride를 2로 설정해 주었기 때문에 크기가 반으로 감소될 것이다
print(pool.shape)
# (1,7,7,5)로 예상되는 결과 출력
# 채널의 감소는 발생하지 않는 것을 확인 가능

feature_maps = np.swapaxes(pool,0,3)
for i,feature_map in enumerate(feature_maps):
    plt.subplot(1,5,i+1), plt.imshow(feature_map.reshape(7,7),cmap='gray')
    # 감소한 크기 기준으로 출력
plt.show()

# 이후 Fully Connected(Dense) Layer로 연결하고 softmax를 통과하여 결과 도출
