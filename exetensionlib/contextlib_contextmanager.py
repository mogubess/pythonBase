import contextlib

#デコレータをシンプルに記述する方法

@contextlib.contextmanager
def tag(name):
    print(f'<{name}>')
    yield
    print(f'<{name}>')

# withの場合
with tag('h2'):
    print('test')
#-- output
# <h2>
# test
# <h2>
#--

with tag('h2'):
    print('test')
    with tag('h5'):
        print('test2')
#-- output
# <h2>
# test
# <h5>
# test2
# <h5>
# <h2>
#--
with tag('h2'):
    print('test')
with tag('h5'):
    print('test2')
#-- output
# <h2>
# test
# <h2>
# <h5>
# test2
#--


# 関数につけた場合
# @tag('h2')
# def f(content):
#     print(content)

# f('test')

#以下のような、ややこしくなるデコレータを解決することができる方法

# def tag(name):
#     def _tag(f):
#         def _wrapper(content):
#             print(f'<{name}>')
#             r = f(content)
#             print(f'<{name}>')
#             return r
#         return _wrapper
#     return _tag

# # @tag('h2')
# # def f(content):
# #     print(content)

# def f(content):
#     print(content)

# f = tag('h2')(f)

# f('test')


