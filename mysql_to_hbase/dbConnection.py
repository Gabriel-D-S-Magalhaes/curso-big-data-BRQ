import mysql.connector
from mysql.connector import errorcode
import pandas as pd
from dotenv import dotenv_values

config = dotenv_values(".env") 

HOST = config['HOST']
USER = config['USER']
PASS = config['PASS']
DB = config['DB']

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

    df = pd.DataFrame([row for row in cursor], columns=["date", "shares", "symbol", "close", "total"])
    df.to_csv('shares.csv', index=False, sep='|')
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
