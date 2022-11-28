from functools import lru_cache
from datetime import datetime, timedelta
from threading import Lock

def cache(seconds: int):
    print(f"wrapper0")
    def wrapper(f):
        func = lru_cache(maxsize=1, typed=False)(f)
        func.ttl = seconds
        func.expire = datetime.utcnow() + timedelta(seconds=func.ttl)
        print(func)
        def inner(*args, **kwargs):
            with Lock():
                print(f"wrapper2")
                if datetime.utcnow() > func.expire:
                    print(f"wrapper4")
                    func.cache_clear()
                    func.expire = datetime.utcnow() + timedelta(seconds=func.ttl)
                return func(*args, **kwargs)

        print(f"wrapper3")
        return inner

    return wrapper
