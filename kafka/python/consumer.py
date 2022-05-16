import mysql.connector
from mysql.connector import errorcode
from kafka import KafkaConsumer#pip3 install kafka-python
from json import loads

try: 
    # O host poderia ser 'localhost'
    db = mysql.connector.connect(host='172.19.0.2', user='root', password='root', port=3306, database='brq_python')
    cursor = db.cursor()

    # Considerei que a tabela minha_media já está criada no banco brq_python

    consumer = KafkaConsumer(
        'meu-topico-legal',
        bootstrap_servers=['172.19.0.4:29092'],
        value_deserializer = lambda x: loads ( x.decode('utf-8') )
    )

    Σ=0 # Sigma
    count=0
    for msg in consumer:
        print(f"Received: {msg.value}")
        Σ += msg.value
        count += 1
        media = round(Σ/count, 2)
        print(f"Mean: {media}")
        print("="*10)
        cursor.execute(f'INSERT INTO minha_media VALUES ({media})')
        db.commit()# Make sure data is committed to the database
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
    db.close()
    print("Cursor and connection closed.")
