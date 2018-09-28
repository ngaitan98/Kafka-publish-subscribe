import json, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform

producer = KafkaProducer(bootstrap_servers=['172.24.41.207:8081'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
nombres = ['Juan','Julian','Andres','Nicolas','Manuel','Franciso','Leonel']
apellidos = ['Gaitan', 'Munios', 'Esobar', 'Bello', 'Lugo', 'Naranjo', 'Alvarez']
i = 1
while i != 0:
    id = i
    nombre = nombres[int(round(uniform(0,len(nombres) - 1),0))] + ' ' +  apellidos[int(round(uniform(0,len(apellidos) - 1),0))]
    documento = str(i*100)
    usuario = '.'.join(nombre.split())+str(i)
    contrasenia = nombre[0:5] + str(123)
    edad = int(round(uniform(18,60),0))
    producer.send('Parqueaderos', {'id': '1', 'nombre' : 'Nicolas Gaitan', 'documento' : 1018505086, 'usuario' : 'n.gaitan', 'contrasenia': 'Greenday1', 'tipo': 'tipo'})
    producer.flush()
    i -= 1

