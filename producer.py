import json, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform

producer = KafkaProducer(bootstrap_servers=['172.24.41.207:8081'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    id = round(uniform(1, 20000),1)
    nombre = "El parqueadero aleta" + str(id)
    ciudad = "Bogotá"
    dimensiones = "3x2"
    lat = round(uniform(74047, 74119),1)/1000
    lon = round(uniform(4615, 4701),1)/1000
    id_duenio = round(uniform(1, 20000),1)
    producer.send('Parqueaderos', {'id': id , 'nombre': nombre, 'dimesiones' : dimensiones, 'direccion' : 'Calle 107a #6c-53', 'ocupado' : 0, 'latitud': lat, 'longitud': lon, 'id_duenio': id_duenio})
    producer.flush()
    time.sleep(5)
