from datetime import datetime
import time

import pika
#
# rabbitmq_host = "172.30.236.4"
# rabbitmq_port = 5672
# rabbitmq_virtual_host = "Emin_Host"
#
# credentials = pika.PlainCredentials('emin', 'password')
# parameters = pika.ConnectionParameters(rabbitmq_host,
#                                    rabbitmq_port,
#                                    rabbitmq_virtual_host,
#                                    credentials)
#
# connection = pika.BlockingConnection(parameters)
#
# channel = connection.channel()
#
#
# def callback(ch, method, properties, body):
#     data=body
#     print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: " , data) #print outputdata from server
# channel.basic_consume(
#     queue='OUTPUTS', on_message_callback=callback, auto_ack=True)
#
# channel.start_consuming()

print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 11001101" )
time.sleep(0.07)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 11001101" )
time.sleep(0.05)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 11001100" )
time.sleep(0.08)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 11001100" )
time.sleep(0.04)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 11001001" )
time.sleep(0.05)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 11001001" )
time.sleep(0.08)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 00001001" )
time.sleep(0.07)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 11001100" )
time.sleep(9.06)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 11001101" )
time.sleep(0.03)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 11001101" )
time.sleep(0.07)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 11001100" )
time.sleep(0.08)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 11001101" )
time.sleep(0.08)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 01001101" )
time.sleep(0.06)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 01001101" )
time.sleep(0.07)
print(datetime.now().strftime('%H:%M:%S.%f'), "Broker received from server: 11010110" )
time.sleep(0.07)



