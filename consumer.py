import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform
import gpxpy.geo

consumer = KafkaConsumer(bootstrap_servers=['172.24.41.207:8081'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe(pattern='Parqueaderos')

producer = KafkaProducer(bootstrap_servers=['172.24.41.207:8081'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
lat = round(uniform(74047, 74119),1)/1000
lon = round(uniform(4615, 4701),1)/1000
dist = 2
for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    print(gpxpy.geo.haversine_distance(lat, lon, message.value['latitud'], message.value['longitud']))


