#Numpyを用いた配列・数値計算

import numpy as np
import matplotlib.pyplot as plt

#配列に整数を格納
x = np.array([1, 3, 5, 7, 9])
y = np.array([0, 2 ,4 ,6 ,8])

#四則演算と表示
print(x/2)
print(x,y)
print(x*y)

xm = np.array([[1, 2],
                [3, 4]])
ym = np.array([[2, 3],
                [4, 5]])

print(xm)          #
print(ym)          #

print(xm.shape)     #
print(xm.dtype)     #データの大きさを表示

#ブロードキャスト
A = np.array([1, 2])
B = np.array([10,10])

print(A*B)
