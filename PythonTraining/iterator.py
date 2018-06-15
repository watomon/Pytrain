import itertools

season = ['Spring', 'Summer','Fall','Winter']
index = [0,1,2,3]

#chainメソッドでシーケンスの結合を行う
it = itertools.chain(index, season);
print("データの型",type(it))
print("chainメソッドの場合")
for i in it:
    print(i)
print("\n")


#zip_longestメソッドで要素同士を結合する
it = itertools.zip_longest(index, season)
print("データの型",type(it))
print("zip_longestメソッドの場合")
for i in it:
    print(i)
print("\n")


#isliceメソッドで0~10未満までの整数要素を２つおきに抽出
it = itertools.islice(itertools.count(),0, 10, 2)
print("データの型",type(it))
print("isliceメソッドの場合")
for i in it:
    print(i)
print("\n")

#イテレータを複製することができるメソッド
it = itertools.islice(itertools.count(), 3)
it1, it2 = itertools.tee(it)
print("データの型",type(it1))
print("teeメソッドの場合")

for i in it1:
    print('it1:' + str(i))
for i in it2:
    print('it2:' + str(i))
print("\n")

#自分でクラスを作成して、イテレータの実装を行う
class Iter:
    def __init__(self, objs):
        self.objs = objs
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.objs):
            raise StopIteration
        value = self.objs[self.index]
        index = self.index
        self.index += 2
        return index, value
print("\n")
print("自作のクラスでイテレータを実装")
print("nextメソッドはイテレータを２個進める")
iter = Iter(['Spring', 'Summer', 'Fall', 'Winter'])

for i in iter:
    print(i)






"""
class MyIterator(object):
    def __init__(self, *numbers):
        self._numbers = numbers
        self._i = 0;
    #next()はselfが実装してるのでそのままselfを返す
    def __iter__(self):
        return self
    def next(self):
        if self._i == len(self._numbers):
            raise StopIteration()
        value = sekf._numbers[self._i]
        self._i +=1
        return value


my_iterator = MyIterator(10, 20, 30)
for num in my_iterator:
    print('hello %d' % num)



season = ['Spring', 'Summer', 'Fall', 'Winter']
iter_season = iter(season)
print(type(iter_season))

next(iter_season)

#イテレーターでは、next文がなくても、
#自動で次のイテレーターに進むようになっている
print(next(iter_season))

for i in iter_season:
    print(i)
"""
