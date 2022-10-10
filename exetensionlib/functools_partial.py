import functools

#クロージャーを簡潔に書く方法
def f(x,y):
    return x+y

def task(f):
    print('stat')
    print(f())

# def outer(x,y):
#     def inner():
#         return x +y
#     return inner

# f = outer(10,20)
p=functools.partial(f,10,20)
task(p)

# task(lamda x,y:x+y)
