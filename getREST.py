import requests
import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform

i = 0
for message in consumer:
    r = requests.get("http://172.24.41.208:8082/nidoo/parqueaderolist")
    if r.status_code != 201:
        i += 1
        print(i)
