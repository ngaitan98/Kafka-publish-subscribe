import requests
import json, time

i,j = 5000,0
while i != 0:
    r = requests.get("http://34.219.60.225:8000/nidoo/clientelist")
    if r.status_code != 200:
        i += 1
        print(i)
    else:
        print(r.request.data)
    i-=1
