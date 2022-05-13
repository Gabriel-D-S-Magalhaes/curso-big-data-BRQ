import mysql.connector

# host = endereço IP do container que roda o MySQL (e.g. 172.17.0.3) ou o nome do container (e.g. mysql)
db = mysql.connector.connect(host='mydb', user='root', password='root', port=3306)

my_cursor=db.cursor()

my_cursor.execute('DROP DATABASE IF EXISTS brq')
my_cursor.execute('CREATE DATABASE IF NOT EXISTS brq_python CHARACTER SET UTF8 COLLATE utf8_bin') 
my_cursor.execute('USE brq_python')
my_cursor.execute('CREATE TABLE IF NOT EXISTS feras_brq(nome varchar(255), email varchar(255))')
my_cursor.execute('INSERT INTO feras_brq VALUES ("Gabriel dos Santos Magalhães", "gabrielmagalhaes@brq.com")')

db.commit()
db.close()
