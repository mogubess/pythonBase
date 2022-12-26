# import re
import pytest

@pytest.fixture
def csv_file(tmpdir):
    with open(tmpdir, 'w+') as c:
        yield c

def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os_name')
