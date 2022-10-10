l = [1,2,3,4,5,6,7,8,9,10]
n = ['a','b','c']
x = [l,n]

#2ごと表示
#[1, 4, 7, 10]
print(l[::3]) 

#逆列
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(l[::-1])

#2次元配列
print(x[0])
print(x[0][0])
print(x[1][0])

l[2:5] =['C','D','E']
#[1, 2, 'C', 'D', 'E', 6, 7, 8, 9, 10]
print(l)

#任意の範囲を空にする
l[2:5] =[]
#[1, 2, 6, 7, 8, 9, 10]
print(l)

#全部表示
print(l[:])

#全部から
l[:] = [] 
print(l)

#リストに要素を追加 append/insert
l = [1,2,3,4,5,6,7,8,9,10]
l.append(100)
l.insert(0,200)

print(l)

#要素を取り出して、削除する
pop = l.pop(1)
print(l,pop)

#削除だけ
del l[0]
print(l)

#リスト内の最初にある指定の値を消す
l.remove(9)
print(l)

#リストの結合
l = [3,2,1,4,5,10]
m = [6,7,10,9,8]
l+=m
print(l)

#---------------------------------
#リストのメソッド
#---------------------------------
#検索最初に引き数とマッチしたindexを返す
print(l.index(10))
print(l.index(10,6))#index6から探す
print(l.count(10))

if 5 in l:
    print('exist')

#ソート
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)

#文字列をリストにするときに区切りを指定できる
s = 'My Name is Mike.'
to_split = s.split(' ')
#['My', 'Name', 'is', 'Mike.']
print(to_split)

#文字列のリストを接続する方法
x  = '@'.join(to_split)
print(x)

#y = l.copy() #リストは単なる代入は参照渡しとなるため
y = l[:] #こちらの記述のほうが一般的
y[0] = 20
print(y)
print(l)




# #一番最後
# print(l[-1])
# #最後から2番目
# print(l[-2])

# #最初から2番目まで
# print(l[0:2])
# print(l[:2])

# #3番目から5番目まで
# print(l[2:5])

# #3番目から最後まで
# print(l[2:])

# print(len(l))
# print(type(l))

# print(list('abcdefg'))