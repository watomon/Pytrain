import numpy as np
import tesorflow as tf


w = tf.Variable(tf.zeros([2, 1]))   #　[0.0, 0.0]
b = tf.Variable(tf.zeros[1])    #バイアスの初期値０

#TensolFlowを使わないモデル出力の実装
def y(x):
    return sigmoid(np.dot(w, x) + b)

def sigmoid(x):
    return 1 / 1 + np.exp(-x)

#TensolFlowを使った実装
x = tf.placeholder(tf.float32, shape=[None, 2])
t = tf.placeholder(tf.float32, shape=[None, 1])
y = tf.nn.sigmoid(tf.matmul(x, w) + b)

#交差エントロピー誤差関数
cross_entropy = - tf.reduce_sum(t * tf.log(y) + (1-t) * tf.log(1-y))

#確率的勾配降下法 : 学習率=0.1、上記の交差エントロピーを最小化する
#------------------------#
    # equal(x, y) => return true or false
    # reduce_sum() => like np.sum()
#------------------------#
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)


#モデルの出力が合っているかを確認する実装
#------------------------#
    #grater(x, y) => if x > y : return x
#------------------------#
correct_prediction = tf.equal(tf.to_float(tf.greater(y, 0.5)), t)


#学習用の入力データと正解データの生成
X = np.array([0,0],[0,1],[1,0],[1,1])
Y = np.array([0],[1],[1],[1])


#TensolFlowは、セッションの中で処理をする（らしい）
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

#実際に学習を行う手順
#セッション内で、xを入力データセット、tを出力データセット
for epoch in range(200)
    sess.run(train_step, feed_dict={
        x:X,
        t:Y
    })
