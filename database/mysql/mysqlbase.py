import mysql.connector


### 1 CREATE DATABASE
# conn = mysql.connector.connect(host='127.0.0.1',user='root',password='mogusql0797')
# cursor = conn.cursor()
# cursor.execute('CREATE DATABASE test_mysql_database')
# cursor.close()
# conn.close()

### 2CREATE TABLE
# conn = mysql.connector.connect(host='127.0.0.1',user='root',password='mogusql0797',database='test_mysql_database')
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE persons(id int NOT NULL AUTO_INCREMENT,name varchar(14) NOT NULL,PRIMARY KEY(id))')
# cursor.close()
# conn.close()

### 3 INSERT DATA
conn = mysql.connector.connect(host='127.0.0.1',user='root',password='mogusql0797',database='test_mysql_database')
cursor = conn.cursor()
cursor.execute('INSERT INTO persons(name) values("Mikes")')
conn.commit()

### 4 SELECT
cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)

cursor.close()
conn.close()

# UPDATE
#cursor.execute('UPDATE prsons set name = "Michel" WHERE name = "Mike"')
# DELETE
# cursor.execute('DELETE FROM prsons WHERE name = "Mike"')
