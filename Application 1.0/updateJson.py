#!/usr/bin/env python
import pika
import sys
import json


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

data = {
    "config": {
        "byteSize": 1,
        "speed": 0 #Integer in seconds (0 = fastest)
    },
    "steps": {
        0: {
            "name": "INIT",
            "init": True,
            "next": 1
        },
        1: {
            "name": "DetectBlock",
            "conditions": {
                0: 1
            },
            "next": 2
        },
        2: {
            "name": "TurnOnCatterpillar",
            "set": {
                0: 1, #Enable catterpillar
                3: 1  #Enable stopper
            },
            "errors": {
                3: [1, "Error: Storage is full", 1] #Value, Message, Goto step
            },
            "next": 3
        },
        3: {
            "name": "DetectColor",
            "sleep": 1,
            "multipleConditions": {
                "orange:": {    #OR
                    "conditions": { #AND
                        1: 0,
                        2: 1
                    },
                    "next": 5
                },
                "black:": {     #OR
                    "conditions": { #AND
                        1: 0,
                        2: 0
                    },
                    "next": 5
                },
                "metal:": {     #OR
                    "conditions": { #AND
                        1: 1,
                        2: 1
                    },
                    "next": 6
                }
            }
        },
        4: {
            "name": "TurnOffGates",
            "set": {
                1: 0,
                2: 0,
                3: 0
            },
            "next": 7
        },
        5: {
            "name": "TurnBlackGate",
            "set": {
                1: 0,
                2: 1,
                3: 0
            },
            "next": 7
        },
        6: {
            "name": "TurnMetalGate",
            "set": {
                1: 1,
                2: 0,
                3: 0
            },
            "next": 7
        },
        7: {
            "name": "DetectStorage",
            "conditions": {
                3: 1
            },
            "next": 8
        },
        8: {
            "name": "TurnOffMachine",
            "set": {
                0: 0,
                1: 0,
                2: 0,
                3: 0
            },
            "next": 1
        },
    }
}



message = json.dumps(data)
channel.basic_publish(exchange='TCR_EXCHANGE',
                routing_key='OUTPUTS',
                body=message,
                properties=pika.BasicProperties(delivery_mode =2,))
print(message)

def callback(ch, method, properties, body):
    data=body
    print(data)
channel.basic_consume(
    queue='OUTPUTS', on_message_callback=callback, auto_ack=True)

channel.start_consuming()

connection.close()