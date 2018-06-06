import numpy as np
import tensorflow as tf

X = np.array([0, 0],[0, 1],[1, 0],[1, 1])
Y = np.array([0], [1], [1], [0])

#placeholderは数値をを格納する為のもの（ここでは定数（入力と正解データ））
x = tf.placeholder(tf.float32, shape=[None, 2])
t = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.truncated_normal([2,3]))
b = tf.Variable(tf.zeros([2]))
h = tf.m.sigmoid(tf.matmal(x, W) + b)
