import random
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

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'info'
while True:
    value = '01'
    byte = ''.join(random.choice(value) for i in range(8))
    data = byte
    message = json.dumps(data)
    print(datetime.now().strftime('%H:%M:%S.%f'), " , inputdata from broker and ready to send to server: ", data)
    channel.basic_publish(exchange='TCR_EXCHANGE',
                    routing_key='OUTPUTS',
                    body=message,
                    properties=pika.BasicProperties(delivery_mode =2,))

    time.sleep(1)
connection.close()
#
# print(datetime.now(), "10010110")
# time.sleep(0.1)
# print(datetime.now(), "10100110")
# time.sleep(0.1)
# print(datetime.now(), "00010110")
# time.sleep(0.1)
# print(datetime.now(), "01110011")
# time.sleep(0.1)
# print(datetime.now(), "10101110")
# time.sleep(0.1)
# print(datetime.now(), "10000100")
# time.sleep(0.1)
# print(datetime.now(), "00011101")
# time.sleep(0.1)
# print(datetime.now(), "11110010")
# time.sleep(0.1)
# print(datetime.now(), "10101011")
# time.sleep(0.1)
# print(datetime.now(), "11001011")
# time.sleep(0.1)
# print(datetime.now(), "11010101")
# time.sleep(0.1)
# print(datetime.now(), "11110010")
# time.sleep(0.1)
# print(datetime.now(), "00001101")


print(datetime.now().strftime('%H:%M:%S.%f'), ", inputdata from broker and ready to send to server: 10010110")
time.sleep(5)
print(datetime.now().strftime('%H:%M:%S.%f'), ", inputdata from broker and ready to send to server: 00010110")
time.sleep(5)
print(datetime.now().strftime('%H:%M:%S.%f'), ", inputdata from broker and ready to send to server: 01110011")
time.sleep(5)
print(datetime.now().strftime('%H:%M:%S.%f'), ", inputdata from broker and ready to send to server: 10101110")
time.sleep(5)
print(datetime.now().strftime('%H:%M:%S.%f'), ", inputdata from broker and ready to send to server: 10010110")
time.sleep(5)
print(datetime.now().strftime('%H:%M:%S.%f'), ", inputdata from broker and ready to send to server: 11110010")
time.sleep(5)
print(datetime.now().strftime('%H:%M:%S.%f'), ", inputdata from broker and ready to send to server: 00010111")
time.sleep(5)
print(datetime.now().strftime('%H:%M:%S.%f'), ", inputdata from broker and ready to send to server: 10010111")
time.sleep(5)
print(datetime.now().strftime('%H:%M:%S.%f'), ", inputdata from broker and ready to send to server: 01101100")
time.sleep(5)
print(datetime.now().strftime('%H:%M:%S.%f'), ", inputdata from broker and ready to send to server: 10010110")
time.sleep(5)
print(datetime.now().strftime('%H:%M:%S.%f'), ", inputdata from broker and ready to send to server: 11001101")
time.sleep(5)
print(datetime.now().strftime('%H:%M:%S.%f'), ", inputdata from broker and ready to send to server: 10110010")

