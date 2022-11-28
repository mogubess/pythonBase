#Pythonで、モックに差し替えたメソッドが呼ばれた回数や呼ばれた時の引数を検証する
#https://thinkami.hatenablog.com/entry/2017/03/18/063454

#メソッドが呼ばれた回数を検証
#メソッドが呼ばれた時の引数を検証
#メソッドが呼ばれた回数と引数を同時に検証
#メソッドが呼ばれていないことを検証

#fixture

#parametarise

from unittest.mock import patch 

class Test(object):
    a = 100

    def aa(self,x,y):
        print(x * y)



with patch.object(Test,'a',200) as dummy:
    print("Test",Test.a)
    print("dummy",dummy)



