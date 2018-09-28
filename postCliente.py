import requests
import json, time
from random import uniform
consumer = KafkaConsumer('Parqueaderos',
                         bootstrap_servers=['172.24.41.207:8081'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
i = 0
for message in consumer:
    r = requests.post("http://172.24.41.208:8082/nidoo/parqueaderolist", data={'id': message.value['id'] , 'nombre': message.value['nombre'], 'documento': message.value['documento'],'usuario' : message.value['usuario'], 'contrasenia' : message.value['contrasenia'], 'edad' : message.value['edad']})
    if r.status_code != 201:
        i += 1
        print(i)
