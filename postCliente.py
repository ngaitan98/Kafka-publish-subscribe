import requests
import json, time
from random import uniform
i = 5000
nombres = ['Juan','Julian','Andres','Nicolas','Manuel','Franciso','Leonel']
apellidos = ['Gaitan', 'Muñoz', 'Esobar', 'Bello', 'Lugo', 'Naranjo', 'Alvarez']
while i != 0:
    id = i
    nombre = nombres[int(round(uniform(0,len(nombres) - 1),0))] + apellidos[int(round(uniform(0,len(apellidos) - 1),0))]
    documento = str(i*100)
    usuario = '.'.join(nombre.split())
    contrasenia = nombre[0:5] + str(123)
    edad = int(round(uniform(18,60),0))
    r = requests.post("http://172.24.41.208:8082/nidoo/clientelist", data={'id':id, 'nombre' : nombre, 'documento' : documento, 'usuario' : usuario, 'contrasenia': contrasenia, 'edad': edad})
    i-=1
    print(r.status_code)
