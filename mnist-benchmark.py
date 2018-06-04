from sklearn import datasets
import numpy as np
import tensorflow as tf



mnist = datasets.fetch_mldata('MNIST original', data_home='.')

n = len(mnist.data)
N = 10000
indices = np.random.permutation(range(n))[:N] #ランダムにN枚を選択する:{indices:indexの複数形,permutation:順序を並び替える}
X = mnist.data[indices]
y = mnist.target[indices]
Y = np.eye(10)[y.astype(int)]
# .eye(n)[a] : aの数字を元に、n*nの単位行列を生成している。 1 of K表現

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.8)
#データ全体の7割りをXの訓練データ、３割をXの評価データ、正解データ(ラベル)の７割をY_train、3割をY_testにしている。
#わかりやすい例　＝＞　http://docs.pyq.jp/python/machine_learning/tips/train_test_split.html


#Kerasを用いて多層パーセプトロンを実装
#入力層の次元を７８４、隠れ層の次元を２００とする

'''
モデル設定
'''
n_in = len(X[0]) # 入力層：784こ
n_hidden = 200  #隠れ層：200
n_out = len(Y[0]) # 10 -> 数字の種類

model = Sequential()
model.add(Dense(n_hidden, input_dim=n_in))
model.add(Activation('sigmoid'))

model.add(Dense(n_out))
model.add(Activation('softmax'))
