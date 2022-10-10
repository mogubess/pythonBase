import io
import requests
import zipfile

#ファイルを一時的にダウンロードして、中身を確認して、ソフト終了とともに、消すことができる。
# SJISファイルのときは結構手続きが必要
url =('https://pypi.tuna.tsinghua.edu.cn/packages/82/cb/906d051fdf1c8b7703d288d3cc44ff32746090378f7f8539c8476a21ce9a/setuptools-0.6b1.zip#sha256=24197f28b1e09f669a5d68eb9ff95f317ec9217f580c34fa73a4d7e6c03f81cc')

f = io.BytesIO()
#f = io.StringIO() #違いの確認を

r = requests.get(url)
f.write(r.content)

with zipfile.ZipFile(f) as z:
    with z.open('setuptools-0.6b1/PKG-INFO') as r:
        print(r.read().decode())


