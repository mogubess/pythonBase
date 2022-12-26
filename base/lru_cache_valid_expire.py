from cache import cache
from datetime import datetime
import time
import requests

@cache(seconds=3)
def add():
  print(f"Expired!!!: {datetime.utcnow().isoformat()}")
  r = requests.get('https://www.google.com/')
  return r


payload = {'key1': 'value1', 'key2': 'value2'}


print(add())

print(add())


print(add())


time.sleep(5)
print(add())


time.sleep(1)
print(add())


time.sleep(3)
print(add())
