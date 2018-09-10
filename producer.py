import json, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform

producer = KafkaProducer(bootstrap_servers=['ip:8081'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    producer.send('alta-piso2-cuarto1', {'time': time.strftime("%X"), 'measurement': 'Distancia',
                  'value': round(uniform(1, 30),1), 'unit': 'Km', 'place': 'piso2/cuarto1'})
                  producer.flush()
                  time.sleep(5)
