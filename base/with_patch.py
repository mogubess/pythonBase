from unittest.mock import patch 

class Test(object):
    a = 100



with patch.object(Test,'a',200) as dummy:
    print(Test.a)
    print(dummy)
