import requests
import json, time

i,j = 5000,0
while i != 0:
    r = requests.get("http://172.24.41.208:8082/nidoo/parqueaderolist")
    if r.status_code != 200:
        i += 1
        print(i)
    else:
        print(r.request.data)
    i-=1
