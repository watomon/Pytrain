# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 00:25:45 2018

@author: watolon
"""

import numpy as np

#  pyplotとかの各種モジュールを同一名空間に一括でimportするための便利モジュール
import matplotlib.pylab as plt 

def relu(x):
    return np.maximum(0, x)

x = np.arange(-6.0, 5.0, 0.1)
plt.plot(x, relu(x))
plt.ylim(-1, 5.5)
plt.show()