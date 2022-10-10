import functools

def d(f):
    @functools.wraps(f)
    def w():
        """ Wrapper docstring"""
        print('decorator')
        return f()
    return w

@d
def example():
    """ Example docstring"""
    print('example')

#デコレータのDocStringを表示しないようにするための対応
help(example)