for i in range(10):
    # 0 - 9
    print(i)
for i in range(2,10):
    # 2 - 9
    print(i)

for i in range(2,10,3):
    # 2,5,8
    print(i)

for _ in range(10):
    #10回まわす
    print('hello')

list = ['a','b','c']
list2 = ['aa','bb','cc']
list3 = ['d','e','f']

for i,w in enumerate(list):
    print(i,w)

for q,w,e in zip(list,list2,list3):
    print(q,w,e)
