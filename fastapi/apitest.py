# https://jsonplaceholder.typicode.com/

import requests

# url = 'https://jsonplaceholder.typicode.com/posts'

# params = {
#     'id': 3
# }


# res = requests.get(url,params)

# print("result {}".format(res.status_code))

# data1 = res.json()

# print("result {}".format(data1))

# 楽天トラベル

URL = 'https://app.rakuten.co.jp/services/api/Travel/KeywordHotelSearch/20170426'
APP_ID = '1040720284694989256'
params = {
    'applicationId': APP_ID,
    'keyword': '沖縄'
}

res = requests.get(URL,params)

print(res.status_code)

hotels = res.json()['hotels']

hotelBasicInfo = hotels[0]['hotel'][0]['hotelBasicInfo']

print(hotelBasicInfo['hotelName'])


