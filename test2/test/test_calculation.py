import pytest
import os
# test_calculation.py

is_Release=True

from ..src.calculation import (
    addition, subtraction, division, Cal
)

class TestCall(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.test_file_name = 'test.txt'

    @classmethod
    def teardown_class(cls):
        print('end')

    def setup_method(self,method):
        print(f'method={method.__name__} setup')

    def teardown_method(self,method):
        print(f'method={method.__name__} teardown')

    def test_save(self, tmpdir):
        cal = Cal()
        cal.save(tmpdir, self.test_file_name)
        print(tmpdir)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    def test_add(self,request,csv_file):
        print(f'csv_file {csv_file}')
        # csv_file.write('csv_file')

        os_name = request.config.getoption('--os-name')
        print(f'method=ada start os {os_name}')
        cal = Cal()
        assert cal.add_num_and_double(2, 3) == 10

    def test_raise(self):
        cal = Cal()
        with pytest.raises(ValueError):
            cal.add_num_and_double('1','1')

@pytest.mark.skip(reason='skip!')
def test_add():
    assert addition(2, 3) == 5

# @pytest.mark.skipif(is_Release==True,reason='skip!')
def test_sub():
    assert subtraction(9, 3) == 6

def test_divide_ok():
    assert division(8,4) == 2
