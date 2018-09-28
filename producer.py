import json, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform

producer = KafkaProducer(bootstrap_servers=['172.24.41.207:8081'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
nombres = ['Juan','Julian','Andres','Nicolas','Manuel','Franciso','Leonel']
apellidos = ['Gaitan', 'Munios', 'Esobar', 'Bello', 'Lugo', 'Naranjo', 'Alvarez']
i = 5000
while i != 1:
    id = i
    nombre = nombres[int(round(uniform(0,len(nombres) - 1),0))] + ' ' +  apellidos[int(round(uniform(0,len(apellidos) - 1),0))]
    documento = str(i*100)
    usuario = str('.'.join(nombre.split())+str(i))
    edad = int(round(uniform(18,60),0))
    contrasenia = str(nombre[0:5] + str(123))+str(edad%43)+str(usuario[0:2])
    producer.send('Parqueaderos', {'id': i, 'nombre' : nombre, 'documento' : documento, 'usuario' : usuario, 'contrasena': contrasenia, 'edad': edad})
    producer.flush()
    i -= 1

