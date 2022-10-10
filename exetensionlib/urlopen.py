import json
import pprint
from urllib.request import urlopen

# with urlopen('http://pypi.python.org/pypi/Twisted/json') as url:
#     http_info = url.info()
#     raw_data = url.read().decode(http_info.get_content_charset())
# project_info = json.loads(raw_data)
# print(project_info)

# import urllib

#403エラーがでるので、以下URLで対応を検討
#https://rainbow-engine.com/python-http-err403/

response = urlopen('http://pypi.python.org/pypi/twisted/json')
print('url:', response.geturl())
# print('code:', response.getcode())
# print('Content-Type:', response.info()['Content-Type'])
# content = response.read()
# print(content)
# response.close()