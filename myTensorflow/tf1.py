import tensorflow as tf
import os
import pickle
import numpy as np

CIFAR_DIR = "F:\pydata\cifar-10-batches-py"
print(os.listdir(CIFAR_DIR))


def load_data(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f, encoding='bytes')
        return data[b'data'], data[b'labels']


x = tf.compat.v1.placeholder(tf.float32, [None, 3071])
y = tf.compat.v1.placeholder(tf.int64, [None])

w = tf.get_variable('w', [x.get_shape()[-1], 1], initializer=tf.random_normal_initializer(0, 1))
b = tf.get_variable('b', [1], initializer=tf.constant_initializer(0.0))

y_ = tf.matmul(x, w) + b
p_y_1 = tf.nn.sigmoid(y_)
