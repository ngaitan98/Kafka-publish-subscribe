import requests

import json, time

from random import uniform

i,j = 0,5000

Nombres=['Nicolás','Juan','Manuel','Andrés','Francisco','Leonel','Eldete','Bellosapo','Elchiconavi', 'Elchicogym']
           
Apellidos = ['Bello', 'Gaitán', 'Lugo', 'Escobar', 'Alvarez', 'Puentes', 'Muñoz', 'Espinosa','Elquiebracucas', 'Mashu']
                        
while j != 0:
    r = requests.post("http://34.219.60.225:8000/nidoo/clientelist", data={'nombre':Nombres[int(round(uniform(0,len(Nombres) - 1),0))] + Apellidos[int(round(uniform(0,len(Apellidos) - 1),0))] ,'Documento' :  str(j*1000000), 'Usuario': 'userName'+str(j), 'Contrasena': 'contra'+str(j), 'edad': j%73})
    if r.status_code != 201:
        i += 1
        print(i)
    print(r)
    j-=1
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
