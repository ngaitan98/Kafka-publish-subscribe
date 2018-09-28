import json, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform

producer = KafkaProducer(bootstrap_servers=['172.24.41.207:8081'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
i = 5000
while i != 0:
    id = i
    nombre = "El parqueadero aleta" + str(id)
    dimensiones = "3x2"
    lon = round(uniform(74047, 74119))/1000
    lat = round(uniform(4615, 4701))/1000
    id_duenio = i%83
    tasaCobro = uniform(70,140)
    direcciones = ['calle 107a #7c-49', 'carrera 22 # 106b-61', 'caerra 1 # 19A - 22', 'carrera 9 # 22 - 63', 'calle 122 # 23 - 45']
    producer.send('Parqueaderos', {'id': id , 'nombre': nombre, 'ciudad': 'Bogota','dimensiones' : dimensiones, 'direccion' : direcciones[int(round(uniform(0, len(direcciones) - 1),0))], 'ocupado' : 0, 'latitud': lat, 'longitud': lon, 'id_duenio': id_duenio, 'tasaCobro' : tasaCobro})
    producer.flush()
    i -= 1

