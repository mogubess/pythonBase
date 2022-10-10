dd = dict([('a',10),('b',20)])

#{'a': 10, 'b': 20}
print(dd)

dd['xx'] = 30

print(dd)
print(dd.keys())
print(dd.values())

#for loop
for key,value in dd.items():
    print(key,value)

ff = {'x':10,'y':20,'a':30 }

#ddをffで上書き
#{'a': 30, 'b': 20, 'xx': 30, 'x': 10, 'y': 20}
dd.update(ff)
print(dd)

#keyの検索
print('a' in dd)
print('d' in dd)
#valueの検索
print(20 in dd.values())
print(500 in dd.values())

#辞書のコピー
gg = dd.copy()
dd['a'] = 210
print(gg)
print(dd)

#setdefault　keyが存在しないときだけ追加する手法、ないキーの追加はしない

dd.setdefault('a',330) #追加されない
dd.setdefault('c',330) #追加される
print(dd)