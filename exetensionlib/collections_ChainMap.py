import collections

#複雑なDicitionaryを変更するのに便利
#Dictionaruのupdate関数を使うと元のデータに戻せないの

a = {'a': 'a', 'c': 'c', 'num': 0}
b= {'b':'b','c':'cc'}
c={'b':'bbb','c':'ccc'}

#データを変更したときに、変更するかの判定処理などをいれることができる
class DeepChainMap(collections.ChainMap):
    def __setitem__(self, key, value) -> None:
        for mapping in self.maps:
            if type(mapping[key]) is int and mapping[key] < value:
                mapping[key] = value
            return
        self.maps[0][key] = value

m = DeepChainMap(a,b,c)
m['num'] = -1
print(m['num']) #元の Value'num': 0 より値が小さいため判定文ではじかれてもとのまま　当該Keyがなければ新規のデータとして追加する。

#各種データの変更、削除、追加など
# m=collections.ChainMap(a,b,c)
# print(m)       # ChainMap({'a': 'a', 'c': 'c', 'num': 0}, {'b': 'b', 'c': 'cc'}, {'b': 'bbb', 'c': 'ccc'})
# print(m.maps)  # [{'a': 'a', 'c': 'c', 'num': 0}, {'b': 'b', 'c': 'cc'}, {'b': 'bbb', 'c': 'ccc'}]
# m.maps.reverse() 
# print(m.maps)  # [{'b': 'bbb', 'c': 'ccc'}, {'b': 'b', 'c': 'cc'}, {'a': 'a', 'c': 'c', 'num': 0}]
# m.maps.insert(0,{'c':'CCCCC'})
# print(m.maps) # [{'c': 'CCCCC'}, {'b': 'bbb', 'c': 'ccc'}, {'b': 'b', 'c': 'cc'}, {'a': 'a', 'c': 'c', 'num': 0}] 先頭に挿入
# print(m['c']) # CCCCC 'c'のkeyで引っ張れる、一番若い配列のvalueを引っ張り出す
# del m.maps[0]
# print(m.maps) # [{'b': 'bbb', 'c': 'ccc'}, {'b': 'b', 'c': 'cc'}, {'a': 'a', 'c': 'c', 'num': 0}]
# print(m['c']) # ccc
# m['b'] ='BBBB'
# print(m.maps) # [{'b': 'BBBB', 'c': 'ccc'}, {'b': 'b', 'c': 'cc'}, {'a': 'a', 'c': 'c', 'num': 0}]

