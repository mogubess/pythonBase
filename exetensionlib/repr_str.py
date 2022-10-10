import datetime

#reprはPythonObjectで全部表示する

d=datetime.datetime.now()

# 2022-09-29 17:59:38.793846
print(d)
# 2022-09-29 17:59:38.793846
print(str(d))
# datetime.datetime(2022, 9, 29, 17, 59, 38, 793846)
print(repr(d))

# 'test' test1 test2
print('{!r} {} {!s}'.format('test', 'test1', 'test2'))

class Point(object):
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return 'Point<object>'
    def __str__(self) -> str:
        return 'Point ({} {})'.format(self.x,self.y)

p=Point(10,200)
# Point<object>
print('{0!r}'.format(p))
# Point (10 200)
print('{0}'.format(p))
# Point (10 200)
print('{0!s}'.format(p))
