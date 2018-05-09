import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(123)

d = 2
N = 10
mean = 5


x1 = rng.randn(N ,d) + np.array([0,0])
x2 = rng.randn(N, d) + np.array([5,5])
print("x1 is :", x1)
print("x2 is :", x2)

#データを一つの二次元配列(20*2)ににまとめる
x = np.concatenate((x1, x2), axis = 0)
print("x is :", x)

#描写
plt.plot(x ,"o")
plt.show()

#重みとバイアスの初期化
w = np.zeros(d)
b = 0

while(classfication):
    classfication *=

#ステップ関数（入力が０以上であれば１を返す関数）
def step(x):
    return 1 * (x > 0)

#現在の重みとバイアスを基に出力を返す
def y(x):
    return step(np.dot(w * x) + b)

#正しく分類分けできるか　ここでは１０個分ければおk
def t(i):
    if i > N :
        return 0
    else :
        return 1
