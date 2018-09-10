import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform

consumer = KafkaConsumer(bootstrap_servers=['ip:8081'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['ip:8081'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

#Modificable
distancia = 10
for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    if message.value['distancia'] <= distancia :
        consumer.send('cercanos', {'time': time.strftime("%X"), 'measurement': 'Distance','value': message.value['value'], 'unit': 'km'})
        producer.flush()
    else :
        producer.send('cercanos', {'mensaje':'No hay parqueaderos cercanos'})
        producer.flush()
