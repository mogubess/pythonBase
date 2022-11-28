import functools

#python2のmemoizeと同じ考え キャッシュしておいた関数の結果を同じ引数のときに即座に返す

global_value  = 5

@functools.lru_cache(maxsize=5)
def long_func():
    r = 0
    for i in range(10000000):
        r+=global_value*1
    return r

# for i in range(10):

global_value  = 20

print(long_func())

global_value  = 30

print(long_func())

print(long_func())

print(long_func.cache_info())
#long_func.cache_clear() #cacheのクリア

# print('next run')
# for i in reversed(range(10)):
#     print(long_func())

# print(long_func.cache_info())

