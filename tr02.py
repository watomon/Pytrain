#クラスの宣言とインスタンスの生成

import numpy as np
import matplotlib.pyplot as plt

# making class
class Android:
    def __init__(self, name):   #コンストラクタ
        self.name=name
        print(self.name + "というアンドロイドを生成しました")

    def hello(self):            #自己紹介メソッド
        print("Hello , I'm " + self.name)

    def goodbye(self):
        print("Goodbye")


m = Android("yajyu1919")
m.hello()
m.goodbye()
