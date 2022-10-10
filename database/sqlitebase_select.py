import sqlite3

conn = sqlite3.connect('test_sqlite.db')

curs = conn.cursor()

#データのSELECT
try:
    curs.execute(
        'SELECT * FROM persons'
    )
except Exception as e:
    print(e)
else:
    print(curs.fetchall())

conn.close()