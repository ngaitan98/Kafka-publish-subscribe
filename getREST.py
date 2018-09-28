import requests
import json, time

i,j = 5000,0
while i != 0:
    r = requests.get("http://172.24.41.208:8082/nidoo/parqueaderolist")
    print(r.data)
