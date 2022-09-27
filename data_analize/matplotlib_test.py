from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()

# plt.plot([1,2,3,4],[1,4,9,16]) # [X軸],[Y軸]
# plt.show() 

# plt.plot([1,2,3,4],[1,4,9,16], 'ro') # [X軸],[Y軸] ro=赤点のプロット
# plt.axis([0,6,0,10]) # X=0～6 Y=0～10の範囲で軸を表示する
# plt.show()

#3つのグラフを表示、3引数ごとに（x,y,plotの形状）
# t = np.arange(0,5,0.2)
# plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
# plt.show()
# print(np.random.random(50)) #0.0以上から1未満間で値を作成
# print(np.random.rand(50)) #平均0、分散1（標準偏差1）
# print(np.random.randn(50))
# print(np.random.normal(loc=0,scale=1,size=10))

# x = np.random.rand(50)
# y = np.random.rand(50)

# colors = np.random.rand(50)
# area = np.random.rand(50) * 100

# plt.scatter(x,y,s=area,c=colors,alpha=0.5)
# plt.show()

#棒グラフ
# objects = ('a','b','c','d','e','f')
# y_pos = np.arange(len(objects)) #objectsの数だけの等差配列
# value = [1,2,3,4,5,6]
# # print(type(objects))
# # print(type(y_pos))
# # print(value)

# plt.bar(y_pos, value,alpha=0.5)
# plt.xticks(y_pos,objects)
# plt.ylabel('Usage')
# plt.title('Title')
# plt.show()

# 円グラフ（パイチャート）
# labels = ('Python','C++','Ruby','Java')
# sizes = [10,20,30,40]
# colors = ['red','green','yellow','blue']

# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True)
# plt.axis('equal')
# plt.show()

#Legend(左上にplotのラベル差し込み)
y=[2,4,6,8,10]
y2=[10,11,12,13,14]
x = np.arange(5)

plt.plot(x,y, label='Y')
plt.plot(x,y2,label='Y2')
plt.legend()

plt.show()


