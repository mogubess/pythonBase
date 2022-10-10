import collections


Point = collections.namedtuple('Point','x,y')
p = Point(10,y=20)
#値を取り出すことはできるが、編集することはできない
print(p.x)
print(p.y)

p1 = Point._make([100,200]) #xとｙに代入できる
print(p1)
print(p1._asdict())
print(type(p1._asdict())) #class dict

p1._replace(x=500)
print(p1) #これはreplaceされていない
p2 = p1._replace(x=500) #p1の値を置き換えて新たに生成するときに使う
print(p2)

#クラスに継承して使う方法
class SumPoint(collections.namedtuple('Point', ['x','y'])):
    @property
    def total(self):
        return self.x + self.y

p3 = SumPoint(2,3)
print(p3.x, p3.y, p3.total)
print(p3)

