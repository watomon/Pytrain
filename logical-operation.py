#Perceptronの実装

#ここでは、簡単なパーセプトロンでANDゲートの実装を行う
#関数ANDで計算し、x1,x2を引数 y1,y2を出力信号、
#w1,w2を重みとし、thetaは閾値である

#関数AND
def AND(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        print(0)
    elif tmp > theta:
        print(1)

#(0,0),(0,1),(1,0),(1,1)でそれぞれ出力値を計算
print("(0,0)")
AND(0,0)
print("(0,1)")
AND(0,1)
print("(1,0)")
AND(1,0)
print("(1,1)")
AND(1,1)

#それ以外の、NANDゲート、ORゲート、NORゲートの実装
