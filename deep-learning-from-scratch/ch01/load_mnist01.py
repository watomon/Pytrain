#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 00:10:00 2018

@author: bitman
"""

import sys, os
sys.path.append(os.pardir) 
from dataset.mnist import load_mnist

#pardir : 親ディレクトリのこと

#最初の呼び出しに少し時間かかる
（数分ほど）
(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False)
"""

load_mnist関数について解説

(訓練画像,　訓練ラベル), (テスト画像 ,テストラベル)　という形で、読み込んだMNISTデータを返してくれる
normalize ：　0.0~1.0の間に正規化するかどうか　
falseにすれば、元の入力画像のピクセルは、0~255になる

flatten　：　入力画像を１次元配列にするかどうか
Trueにすると、７８４個の要素からなる　１次元配列になる

"""

    
    

#それぞれのデータの形状を出力
print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

#(60000, 784) 
#(60000,)
#(10000, 784)
#(10000,)

