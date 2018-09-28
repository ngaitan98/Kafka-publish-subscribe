import requests
import json, time
from random import uniform

i,j = 0,5000
inicios = ['06:00:00','07:00:00','08:00:00','09:00:00','10:00:00', '11:00:00']
fines = ['12:00:00','13:00:00','14:00:00','15:00:00','16:00:00', '17:00:00', '18:00:00', '19:00:00', '20:00:00']
tipos =['Debito', 'Credito', 'Efectivo']
while j != 0:
    r = requests.post("http://172.24.41.208:8082/nidoo/transaccionlist", data={'id': i, 'id_reserva': i, 'costo': round(uniform(12000,34000), 2),'tipo' : tipos[int(round(uniform(0,len(tipos) - 1),0))]})
    if r.status_code != 201:
        i += 1
        print(i)
    j-=1
