#!/usr/bin/env python
import pika
import sys
import json

rabbitmq_host = "172.30.236.4"
rabbitmq_port = 5672
rabbitmq_virtual_host = "Emin_Host"

credentials = pika.PlainCredentials('emin', 'password')
parameters = pika.ConnectionParameters(rabbitmq_host,
                                   rabbitmq_port,
                                   rabbitmq_virtual_host,
                                   credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

print(' [*] Waiting for messages from queue OUTPUTS. To exit press CTRL+C')

def callback(ch, method, properties, body):
    data=body
    print(data)
channel.basic_consume(
    queue='OUTPUTS', on_message_callback=callback, auto_ack=True)

channel.start_consuming()