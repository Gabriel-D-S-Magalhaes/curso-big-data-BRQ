import mysql.connector
from mysql.connector import errorcode

HOST = '<host_here>'
USER = '<user_here>'
PASS = '<password_here>'
DB = 'stockfgv'

try:
    cnx = mysql.connector.connect(
        host=HOST, user=USER, password=PASS, port=3306, database=DB)
    cursor = cnx.cursor()

    query = ("select s.date_ as 'date', "
             "p.shares, "
             "p.symbol, "
             "s.close, "
             "ROUND(s.close * p.shares, 2) total "
             "from stockfgv.stocks s "
             "INNER JOIN stockfgv.portfolio p "
             "ON p.symbol = s.symbol "
             "WHERE s.date_ = '2020-06-12';")
    cursor.execute(query)

    for (date, shares, symbol, close, total) in cursor:
        print(f"{date}\t|\t{shares}\t|\t{symbol}\t|\t{close}\t|\t{total}")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
except KeyboardInterrupt:
    print("\nConsumer closed.")
finally:
    print("Closing cursor and connection...")
    cursor.close()
    cnx.close()
    print("Cursor and connection closed.")
