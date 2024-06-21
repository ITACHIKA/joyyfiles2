import kafka
import json
import numpy as np

server=['192.168.134.128:9092','192.168.134.129:9092']

producer=kafka.KafkaProducer(bootstrap_servers=server,value_serializer=lambda s:json.dumps(s).encode('utf-8'))

for i in range (10):
    data={"message":str(np.random.random()*100)}
    producer.send("assign_topic",value=data,partition=1)

producer.close()