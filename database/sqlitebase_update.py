import sqlite3

conn = sqlite3.connect('test_sqlite.db')

curs = conn.cursor()

#データのSELECT
try:
    curs.execute(
        'UPDATE persons set name = "Michel" WHERE name = "Mike"'
    )
    conn.commit()
except Exception as e:
    print(e)

conn.close()