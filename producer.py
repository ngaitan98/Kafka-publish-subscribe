import json, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform

producer = KafkaProducer(bootstrap_servers=['ip_kafka_server:kafka_port'], 
						 value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
	producer.send('alta-piso2-cuarto1', {'time': time.strftime("%X"), 'measurement': 'temperature', 
					'value': round(uniform(20, 25),1), 'unit': 'C', 'place': 'piso2/cuarto1'})
	producer.send('baja-piso2-cuarto2', {'time': time.strftime("%X"), 'measurement': 'temperature', 
					'value': round(uniform(20, 25),1), 'unit': 'C', 'place': 'piso2/cuarto2'})
	producer.flush()
	time.sleep(5)