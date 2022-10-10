import functools

#python2のmemoizeと同じ考え キャッシュしておいた関数の結果を同じ引数のときに即座に返す

@functools.lru_cache(maxsize=5)
def long_func(n):
    r = 0
    for i in range(10000000):
        r+=n*1
    return r

for i in range(10):
    print(long_func(i))

print(long_func.cache_info())
#long_func.cache_clear() #cacheのクリア

print('next run')
for i in reversed(range(10)):
    print(long_func(i))

print(long_func.cache_info())

