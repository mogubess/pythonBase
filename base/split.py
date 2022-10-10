import re

data = "001002003"

#空文字を取り除ける
list = re.split("(...)",data)[1::2]

print(list)