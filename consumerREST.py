import requests
import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform

consumer = KafkaConsumer('Parqueaderos',
                         bootstrap_servers=['172.24.41.207:8081'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
        r = requests.post("http://172.24.41.208:8082/measurements/", data={'id': message.value['measurement'], 'value': message.value['value'], 'unit': message.value['unit'], 'place': 22})
        print (r.status_code, r.reason)
