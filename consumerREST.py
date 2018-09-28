import requests
import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform

consumer = KafkaConsumer('Parqueaderos',
                         bootstrap_servers=['172.24.41.207:8081'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
i = 0
for message in consumer:
  
    r = requests.post("http://172.24.41.208:8082/nidoo/parqueaderolist", data={'id': message.value['id'] , 'nombre': message.value['nombre'], 'ciudad': message.value['ciudad'],'dimensiones' : message.value['dimensiones'], 'direccion' : message.value['direccion'], 'ocupado' : message.value['ocupado'], 'latitud': message.value['latitud'], 'longitud': message.value['longitud'], 'tasaCobro' : message.value['tasaCobro'], 'id_duenio': message.value['id_duenio']})
    if r.status_code != 201:
        i += 1
        print(i)
