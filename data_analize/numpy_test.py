from array import array
import numpy as np

#<class 'numpy.ndarray'>を作成する
a = np.array([1,2,3])
print(type(a))
print(a)

#2次元配列の作成
a = np.array([[1,2,3],[4,5,6]])
print(a)

#各次元の要素数の知り方(ndarray.shape)
print(a.shape)

#次元数の知り方(ndarray.ndim)
print(a.ndim)

#次元数の知り方(データ型 int32 etc)
print(a.dtype.name)

#配列の総個数
print(a.size)

##0から30まで5stepの値のndarrayを作成する
a = np.arange(0,30,5)
print(a)

#0から2までの0.3stepでndarrayを作成する
a = np.arange(0,2,0.3)
print(a)

#3x4の0の要素で埋められたndarrayを作成する
a = np.zeros((3,4), dtype=np.int16)
print(a)

#何もないことを示す配列を作成できる
print(np.nan)
print([np.nan]*10)

#0から2までに9つの値を作成したndarrayを作成する
a = np.linspace(0,2,9)
print(a)

#2X3の配列を作成する
a = np.arange(6).reshape(2,3)
print(a)

#2x3x4の配列を作成する
a = np.arange(24).reshape(2,3,4)
print(a)

#出力の省略をどこまでにするかを決める
np.set_printoptions(threshold=1000)

x = np.arange(0,10,2)
y = np.arange(5)
z = np.arange(0,100,20)

#結合
a = np.append(x,y)
print(a)

#並列結合
a = np.vstack([x,y,z])
print(a)

#直列結合
np.hstack([x,y,z])
print(a)

#演算
a = np.array([10,20,30,40,50])
b = np.arange(5)
print('演算')
print(a+b)
print(a-b)
print(b-a)
print(a < 30)
print(a*3)
print(a.sum())
print(a.min())
print(a.max())
#平均
print(a.mean())

print(np.random.random((2,3)))

#縦軸横軸を使った計算
a = np.arange(12).reshape(3,4)
print(a)
print(a.sum(axis=0))
print(a.sum(axis=1))
#縦軸と横軸の入れ替え、3x4から4x3に変換
print(a.T)

#同じ個数なら、配列のリサイズが可能
print(a.resize((2,6)))

# jupyter notebookでなら可能
# import matplotlib.pyplot as plt
# %matplotlib inline
# v = np.random.normal(2,0.5,10000)
# plt.hist(v,bins=50,density=1)
# plt.show()

