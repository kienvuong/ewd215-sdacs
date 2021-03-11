#!/usr/bin/env python
import pika
import sys
import json
import time
from datetime import datetime
rabbitmq_host = "172.30.236.4" #ubuntu server ip
rabbitmq_port = 5672 
rabbitmq_virtual_host = "Emin_Host"

credentials = pika.PlainCredentials('emin', 'password')
parameters = pika.ConnectionParameters(rabbitmq_host,
                                rabbitmq_port,
                                rabbitmq_virtual_host,
                                credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

data = "010101001"
data = 0
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'info'
while True:
    data = data + 1
    message = json.dumps(data)
    print(datetime.now())
    channel.basic_publish(exchange='TCR_EXCHANGE',
                    routing_key='OUTPUTS',
                    body=message,
                    properties=pika.BasicProperties(delivery_mode =2,))

    print(" [x] Sent to queue 2 %r:%r" % (routing_key,message))

    time.sleep(1)
connection.close()