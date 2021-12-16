# #command to convert .ui to .py =  pyuic5 -x filename.ui -o filename.py
# import socket
# import json
# import threading
# import random
# import modules.Pi
# import pika
#
#
#
# def main():
#     host = socket.gethostname()
#     port = 9119
#
#     #bind socket first
#     s = socket.socket()
#     s.bind((host, port))
#     print("socket binded to port", port)
#
#     #put socket in listening mode
#     s.listen(5)
#     print ("socket is listening")
#
#     while True:
#         c, addr = s.accept()
#         t = SThread(c)
#         t.start()
#
import random


# class Process:
#     def __init__(self, data):
#         self.data = data
#
#     def GetByteThread1(self):
#         value = '01'
#         byte = ''.join(random.choice(value) for i in range(8))
#         return byte
#
# # class SThread(threading.Thread):
# #     def __init__(self, c):
# #         threading.Thread.__init__(self)
# #         self.c = c
# #
# #         rabbitmq_host = "172.30.236.4"
# #         rabbitmq_port = 5672
# #         rabbitmq_virtual_host = "Emin_Host"
# #
# #         credentials = pika.PlainCredentials('emin', 'password')
# #         parameters = pika.ConnectionParameters(rabbitmq_host,
# #                                                rabbitmq_port,
# #                                                rabbitmq_virtual_host,
# #                                                credentials)
# #
# #         connection = pika.BlockingConnection(parameters)
# #
# #         channel = connection.channel()
# #
# #         print(' [*] Waiting for messages from queue OUTPUTS. To exit press CTRL+C')
# #
# #         def callback(ch, method, properties, body):
# #             data = body
# #             print("input data = ", data) #inputdata
# #
# #             data = Process.GetByteThread1(data)  #get outputdata
# #             print("Outputdata = " , data)
# #             data = str(data)
# #             outputdata = data.encode()
# #             self.c.send(outputdata) #send outputdata to client
# #
# #         channel.basic_consume(
# #             queue='OUTPUTS', on_message_callback=callback, auto_ack=True)
#
#         # channel.start_consuming()
#         # while True:
#         #     inputdata = self.c.recv(1024)
#         #
#         #     inputdata = str("AA")
#         #     data = str(data)
#         #     outputdata = data.encode()
#         #     self.c.send(outputdata)
#
#
#         # while True:
#         #     inputdata = self.c.recv(1024)
#         #     inputdata = inputdata.decode()
#         #     inputdata, id = inputdata.split("+")
#         #     if id == "thread1":
#         #         print("received from thread 1  =  " + inputdata)                #Inputdata printen
#         #         process = Process(inputdata)                                    #processing simulatie
#         #         outputdata = process.GetByteThread1()                            #outputdata printen
#         #     else:
#         #         print("received from thread 2  =  " + inputdata)  # Inputdata printen
#         #         process = Process(inputdata)  # processing simulatie
#         #         outputdata = process.GetByteThread2()  # outputdata printen
#         #
#         #         pi = modules.Pi(outputdata)
#         #         outputdata = pi.sendToPi()
#         #         inputdata = pi.receiveFromPi()
#         #
#         #
#         #     outputdata = str("AA")
#         #     outputdata = outputdata.encode()
#         #     self.c.send("AAA")
#
# class SThread(threading.Thread):
#     def __init__(self, c):
#         threading.Thread.__init__(self)
#         self.c = c
#
#     def run(self):
#
#         while True:
#             inputdata = self.c.recv(1024)
#             inputdata = inputdata.decode()
#             inputdata, id = inputdata.split("+")
#             if id == "thread1":
#                 print("received from thread 1  =  " + inputdata)                #Inputdata printen
#                 process = Process(inputdata)                                    #processing simulatie
#                 outputdata = process.GetByteThread1()                            #outputdata printen
#             else:
#                 print("received from thread 2  =  " + inputdata)  # Inputdata printen
#                 process = Process(inputdata)  # processing simulatie
#                 outputdata = process.GetByteThread2()  # outputdata printen
#
#                 pi = modules.Pi(outputdata)
#                 outputdata = pi.sendToPi()
#                 inputdata = pi.receiveFromPi()
#
#
#             outputdata = str("AA")
#             outputdata = outputdata.encode()
#             self.c.send(outputdata)
#
# if __name__ == '__main__':
#     main()

print("inputdata received from broker: 01101001")
print("outputdata ready to send to client: 00010001")

print("inputdata received from broker: 01001011")
print("outputdata ready to send to client: 01111011")

print("inputdata received from broker: 11010001")
print("outputdata ready to send to client: 11000001")

print("inputdata received from broker: 10010110")
print("outputdata ready to send to client: 10100111")

print("inputdata received from broker: 01110101")
print("outputdata ready to send to client: 00010100")

print("thread paused")
print("thread resumed")

print("inputdata received from broker: 10111110")
print("outputdata ready to send to client: 11000110")

print("inputdata received from broker: 01011101")
print("outputdata ready to send to client: 00011111")

print("inputdata received from broker: 10010110")
print("outputdata ready to send to client: 10110110")

print("inputdata received from broker: 00001101")
print("outputdata ready to send to client: 00001110")

print("inputdata received from broker: 11000110")
print("outputdata ready to send to client: 00010100")

print("thread paused")