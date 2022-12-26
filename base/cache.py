from functools import lru_cache
from datetime import datetime, timedelta
from threading import Lock

def cache(seconds: int):
    def wrapper(f):
        func = lru_cache(maxsize=1, typed=False)(f)
        func.ttl = seconds
        func.expire = datetime.utcnow() + timedelta(seconds=func.ttl)
        print("wrapper:",f)
        def inner(*args, **kwargs):
            with Lock():
                if datetime.utcnow() > func.expire:
                    func.cache_clear()
                    func.expire = datetime.utcnow() + timedelta(seconds=func.ttl)
                return func(*args, **kwargs)

        return inner

    return wrapper
