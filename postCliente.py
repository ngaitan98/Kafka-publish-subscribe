import requests
import json, time
from random import uniform
i = 1
nombres = ['Juan','Julian','Andres','Nicolas','Manuel','Franciso','Leonel']
apellidos = ['Gaitan', 'Munios', 'Esobar', 'Bello', 'Lugo', 'Naranjo', 'Alvarez']
while i != 0:
    id = i
    nombre = nombres[int(round(uniform(0,len(nombres) - 1),0))] + ' ' +  apellidos[int(round(uniform(0,len(apellidos) - 1),0))]
    documento = str(i*100)
    usuario = '.'.join(nombre.split())+str(i)
    contrasenia = nombre[0:5] + str(123)
    edad = int(round(uniform(18,60),0))
    print(id, nombre, documento, usuario, contrasenia, edad)
    r = requests.post("http://172.24.41.208:8082/nidoo/clientelist", data={'nombre' : 'Nicolas Gaitan', 'documento' : 1018505086, 'usuario' : 'n.gaitan', 'contrasenia': 'Greenday1', 'edad': 20})
    i-=1
    print(r.status_code)
