import kafka,json

consumer=kafka.KafkaConsumer(bootstrap_servers=['192.168.134.128:9092'],auto_offset_reset='latest',consumer_timeout_ms=1000000,value_deserializer=lambda m: json.loads(m.decode('ascii')),client_id="add")
consumer.assign([kafka.TopicPartition("assign_topic",0)])
for msg in consumer:
    print(msg)