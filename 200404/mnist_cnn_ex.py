import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. set hyper parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100

# checkpoint 저장 dir 및 파일명 지정
cur_dir = os.getcwd()
ckpt_dir_name = 'checkpoints'
model_dir_name = 'mnist_cnn_seq'

checkpoint_dir = os.path.join(cur_dir, ckpt_dir_name, model_dir_name)
os.makedirs(checkpoint_dir, exist_ok=True)

checkpoint_prefix = os.path.join(checkpoint_dir, model_dir_name)

# 2. make a data pipelining
mnist = keras.datasets.mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
#(60000, 28, 28) (60000,)       (10000,28,28) (10000,)
train_images = train_images.astype(np.float32)/255.
#scaling
test_images = test_images.astype(np.float32)/255.
train_images = np.expand_dims(train_images, axis=-1)
# 3차원 데이터를 4차원으로 확장. axis=-1은 마지막 차원을 의미
test_images = np.expand_dims(test_images, axis=-1)

train_labels = to_categorical(train_labels, 10)
# One-hot encoding
# 각 단어 집합을 벡터화 하여 해당 단어는 1, 나머지는 0으로 처리
# 단어에 고유 인덱스를 부여하여 벡터로 다루는 방법
test_labels = to_categorical(test_labels, 10)

train_dataset = tf.data.Dataset.from_tensor_slices((train_images,
                                                    train_labels)).shuffle(buffer_size=100000).batch(batch_size)
test_dataset = tf.data.Dataset.from_tensor_slices((test_images,
                                                   test_labels)).batch(batch_size)
# data slice 및 공급
# 테스트 데이터는 셔플이 불필요하므로 셔플과정 생략

# 3. build a neural network model - sequential API
# sequential api 사용
# model.add를 사용, 각 레이어를 순차적으로 추가하여 네트워크를 구성


def crate_model():
    model = keras.Sequential()
    model.add(keras.layers.Conv2D(filters=32, kernel_size=3, activation=tf.nn.relu,
                                  padding='same', input_shape=(28, 28, 1)))
    # input shape는 필수 작성사항은 아니지만, 디버그 등에 활용하기 위해 처음엔 적어주는 것이 좋다
    model.add(keras.layers.MaxPool2D(padding='same'))
    model.add(keras.layers.Conv2D(filters=64, kernel_size=3, activation=tf.nn.relu,
                                  padding='same'))
    model.add(keras.layers.MaxPool2D(padding='same'))
    model.add(keras.layers.Conv2D(filters=128, kernel_size=3, activation=tf.nn.relu,
                                  padding='same'))
    model.add(keras.layers.MaxPool2D(padding='same'))
    model.add(keras.layers.Flatten())
    # Feature map을 벡터로 분해?변환?
    model.add(keras.layers.Dense(256, activation=tf.nn.relu))
    # Dense layer를 사용
    model.add(keras.layers.Dropout(0.4))
    # Dense layer의 convolution layer에 비해 파라미터가 매우 많기 때문에 dropout 적용
    # 이 데이터의 경우 마지막 conv layer의 파라미터는 73856, 첫 Dense layer는 524544개가 발생
    model.add(keras.layers.Dense(10))
    return model


# model 출력 (설계 검증용)
model = crate_model()
model.summary()

# loss function 구현


def loss_fn(model, images, labels):
    logits = model(images, training=True)
    # training=True를 training이 필요한 과정임을 명시
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
        logits=logits, labels=labels))
    return loss

# gradient 계산


def grad(model, images, labels):
    with tf.GradientTape() as tape:
        loss = loss_fn(model, images, labels)
    return tape.gradient(loss, model.variables)


# 6. Select an Optimizer(여기선 아담 사용)
optimizer = tf.optimizers.Adam(learning_rate=learning_rate)

# 7. Define a Metric for Models's Performance


def evaluate(model, images, labels):
    logits = model(images, training=False)
    # Accuracy 계산엔 training이 불필요하므로 False로 명시
    correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))
    # training된 데이터와 정답과의 비교
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    # 그 평균을 계산
    return accuracy


# 8. Make a Checkpoint for Saving
checkpoint = tf.train.Checkpoint(cnn=model)

# 9. Train and Validate a Neural Network Model
for epoch in range(training_epochs):
    avg_loss = 0.
    avg_train_acc = 0.
    avg_test_acc = 0.
    train_step = 0
    test_step = 0

    for images, labels in train_dataset:
        # batch size만큼 가져온다
        grads = grad(model, images, labels)
        optimizer.apply_gradients(zip(grads, model.variables))
        # apply_gradients를 통해 weight 업데이트
        loss = loss_fn(model, images, labels)
        acc = evaluate(model, images, labels)
        avg_loss = avg_loss+loss
        avg_train_acc = avg_train_acc+acc
        train_step += 1
    avg_loss = avg_loss/train_step
    avg_train_acc = avg_train_acc/train_step

    # epoch 마다 validation 진행
    for images, labels in test_dataset:
        acc = evaluate(model, images, labels)
        avg_test_acc = avg_test_acc+acc
        train_step += 1
    avg_test_acc = avg_test_acc/test_step

    print('Epoch:', '{}'.format(epoch+1), 'loss =', '{:.8f}'.format(avg_loss),
          'train accuracy = ', '{:.4f}'.format(avg_train_acc),
          'test accuracy = ', '{:.4f}'.format(avg_test_acc))

    checkpoint.save(file_prefix=checkpoint_prefix)
