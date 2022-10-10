#PosgreSQLの話
#使うライブラリはpsycopg2 aiohttp Server との組み合わせでよく使われる。
# Qiita https://qiita.com/hoto17296/items/fcefdb308d95c01606c7
#そもそも DB-API に規定されている仕様は同期的な API のため)
#https://peps.python.org/pep-0249/

#import asyncpg #posgresql

import sqlite3

conn = sqlite3.connect('test_sqlite.db')

#テーブル作成
curs = conn.cursor()
try:
    curs.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
    conn.commit()
except Exception as e:
    print(e) # table persons already exists
# Error 

#作成されたかをターミナルに移動して、確認する
# sqlite3 .\test_sqlite.db 
# sqlite> .tables
# persons  << personsのTABLEを確認した

#データの格納
curs.execute(
    'INSERT INTO persons(name) values("Mike")'
)



conn.close()