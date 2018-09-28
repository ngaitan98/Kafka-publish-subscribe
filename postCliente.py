import requests
import json, time
from random import uniform
from kafka import KafkaConsumer

consumer = KafkaConsumer('Parqueaderos',
                         bootstrap_servers=['172.24.41.207:8081'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
i = 0
for message in consumer:
    print(message.value)
    r = requests.post("http://172.24.41.208:8082/nidoo/dueniolist", data={'id': message.value['id'] , 'nombre': message.value['nombre'], 'documento': message.value['documento'],'usuario' : message.value['usuario'], 'contrasena' : message.value['contrasena'], 'edad' : message.value['edad']})
    if r.status_code != 201:
        i += 1
        print(i)
