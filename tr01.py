#matplotlibを用いたグラフ描写

import numpy as np
import matplotlib.pyplot as plt

#データの作成
x = np.arange(0, 6, 0.1)  #0から6まで0.1刻みで生成
y = np.sin(x)

#グラフの描写
plt.plot(x, y)
plt.show()

#2018/04/13 テスト変更
