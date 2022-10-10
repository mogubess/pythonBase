#位置引数、キーワード引数、デフォルト引き数

def menu(a=4,b=5,c=6):
    print(a,b,c)

#1 2 3
menu(a=1,b=2,c=3)

#4 5 6
menu()


#位置引数のタプル化(*args)
def say_somothing(*args):
    print(args)
    for arg in args:
        print(arg)

def say_somothing2(word, *args):
    print(word,args)
    for arg in args:
        print(arg)

#('Hi', 'Mike', 'Nancy')
# Hi
# Mike
# Nancy
say_somothing('Hi','Mike','Nancy')

#これはほとんど使わない
# t = {'Mike', 'Hi'}
# say_somothing2('Hi',*t)

#Hi ('Mike', 'Nancy')
#Mike
#Nancy
say_somothing2('Hi','Mike','Nancy')


#キーワード引き数の辞書化
def menu(**kwargs):
    print(kwargs)
    for k , v in kwargs.items():
        print(k,v)

#{'a': '1', 'b': '2', 'c': '3'}
# a 1
# b 2
# c 3
menu(a='1',b='2',c='3')

dd = {
    'x':5,
    'y':6,
    'z':7,
}

#辞書をアンパックして引き数に渡す
# {'x': 5, 'y': 6, 'z': 7}
# x 5
# y 6
# z 7
menu(**dd)

def menu2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

# bannna
# ('apple', 'orange')
# {'entree': 'beef', 'drink': 'water'}
menu2('bannna','apple','orange',entree='beef',drink='water')
