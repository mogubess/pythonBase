#タプル内のリストは制御可能

t =([1,2,3],[4,5,6])

t[0][0] = 4
#([4, 2, 3], [4, 5, 6])
print(t)

t2 =(1,2,3)
t3 = (4,5,6)

t4 = t2+t3
print(t4)

#タプルのアンパッキング
num_tuple = (10,20)
print(num_tuple)

x,y,z = t2
print(x,y,z)

#リストのアンパッキング
l = [7,8,9]
a,b,c = l
print(a,b,c)

import copy

a = ('hello','Python','String')  
b = a  
print(a,b)  

#shallw copy
a = ('hello',['Python'],'String')  
b = copy.copy(a)  
b[1].append('Jython')
print(a,b)

#deep copy
a = ('hello',['Python'],'String')  
b = copy.deepcopy(a)  
b[1].append('Jython')
print(a,b)

#タプルをリストに変換
# list /tuple
tuplea = ('python', 'java', 'c#')
lst = list(tuplea)
lst.append('ruby')

print(lst)
print(tuplea)
