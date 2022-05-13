from kafka import KafkaProducer #pip3 install kafka-python
import json
from time import sleep
import random

producer = KafkaProducer(
    bootstrap_servers=['172.19.0.3:9092'],
    value_serializer = lambda x: str(x).encode('utf-8')
)

try: 
    while (True):
        #content = int(input("> "))
        rand = random.randint(1,999)
        #print(f'Sent: {content}')
        print(f'Sent: {rand}')
        #producer.send('meu-topico-legal', content)
        producer.send('meu-topico-legal', rand)
        sleep(5)
except KeyboardInterrupt:
    print("\nProducer closed.")