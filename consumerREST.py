import requests
import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform

consumer = KafkaConsumer('promedio',
						 bootstrap_servers=['ip_kafka_server:kafka_port'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

    r = requests.post("http://ip_RESTservice:service_port/measurements/", data={'measurement': message.value['measurement'], 'value': message.value['value'], 'unit': message.value['unit'], 'place': message.value['place'], 'time': message.value['time']})
    print (r.status_code, r.reason)
