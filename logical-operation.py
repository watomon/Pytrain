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
#それ以外の、NANDゲート、ORゲート、NORゲートの実装

#NAND gate
def NAND(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        print(1)
    elif tmp > theta:
        print(0)
#OR gate
def OR(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    tmp = x1 * w1 + x2 * w2
    if tmp >= 0.5:
        print(1)
    elif tmp < 0.5:
        print(0)
#NOR gate
def NOR(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    tmp = x1 * w1 + x2 * w2
    if tmp >= 0.5:
        print(0)
    elif tmp < 0.5:
        print(1)

#(0,0),(0,1),(1,0),(1,1)でそれぞれ出力値を計算
print("AND - GATE")
print("(0,0)")
AND(0,0)
print("(0,1)")
AND(0,1)
print("(1,0)")
AND(1,0)
print("(1,1)")
AND(1,1)

print("NAND - GATE")
print("(0,0)")
NAND(0,0)
print("(0,1)")
NAND(0,1)
print("(1,0)")
NAND(1,0)
print("(1,1)")
NAND(1,1)

print("OR - GATE")
print("(0,0)")
OR(0,0)
print("(0,1)")
OR(0,1)
print("(1,0)")
OR(1,0)
print("(1,1)")
OR(1,1)

print("NOR - GATE")
print("(0,0)")
NOR(0,0)
print("(0,1)")
NOR(0,1)
print("(1,0)")
NOR(1,0)
print("(1,1)")
NOR(1,1)
