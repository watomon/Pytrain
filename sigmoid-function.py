# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 23:50:02 2018

@author: watomon
"""
import numpy as np

#  pyplotとかの各種モジュールを同一名空間に一括でimportするための便利モジュール
import matplotlib.pylab as plt 

def sigmoid(x):
    return 1 /(1+np.exp(-x))

x = np.arange(-5.0, 5.0 ,0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) #y軸の範囲を指定する
plt.show()

