#command to convert .ui to .py =  pyuic5 -x filename.ui -o filename.py
import socket
import json
import threading
import random
import modules.Pi
import pika



def main():
    host = socket.gethostname()
    port = 9119

    #bind socket first
    s = socket.socket()
    s.bind((host, port))
    print("socket binded to port", port)

    #put socket in listening mode
    s.listen(5)
    print ("socket is listening")

    while True:
        c, addr = s.accept()
        t = SThread(c)
        t.start()

class Process:
    def __init__(self, data):
        self.data = data

    def GetRandomByte(self):
        value = '01'
        randomByte = ''.join(random.choice(value) for i in range(8))
        return randomByte

    def processing(self):
        if self.data == "01010101":
            self.data = self.GetRandomByte()
        elif self.data == "11111111":
            self.data = self.data + "b"
        elif self.data == "11110000":
            self.data = self.data
        return self.data

    def GetByteThread1(self):
        value = '01'
        randomByte = ''.join(random.choice(value) for i in range(8))
        return randomByte

    def GetByteThread2(self):
        value = '01'
        randomByte = ''.join(random.choice(value) for i in range(8))
        return randomByte


class SThread(threading.Thread):
    def __init__(self, c):
        threading.Thread.__init__(self)
        self.c = c

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
            data = body
            print(data)

            data = str(data)
            outputdata = data.encode()
            self.c.send(outputdata)

        channel.basic_consume(
            queue='OUTPUTS', on_message_callback=callback, auto_ack=True)

        channel.start_consuming()
        # while True:
        #     inputdata = self.c.recv(1024)
        #
        #     inputdata = str("AA")
        #     data = str(data)
        #     outputdata = data.encode()
        #     self.c.send(outputdata)


        # while True:
        #     inputdata = self.c.recv(1024)
        #     inputdata = inputdata.decode()
        #     inputdata, id = inputdata.split("+")
        #     if id == "thread1":
        #         print("received from thread 1  =  " + inputdata)                #Inputdata printen
        #         process = Process(inputdata)                                    #processing simulatie
        #         outputdata = process.GetByteThread1()                            #outputdata printen
        #     else:
        #         print("received from thread 2  =  " + inputdata)  # Inputdata printen
        #         process = Process(inputdata)  # processing simulatie
        #         outputdata = process.GetByteThread2()  # outputdata printen
        #
        #         pi = modules.Pi(outputdata)
        #         outputdata = pi.sendToPi()
        #         inputdata = pi.receiveFromPi()
        #
        #
        #     outputdata = str("AA")
        #     outputdata = outputdata.encode()
        #     self.c.send("AAA")

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

if __name__ == '__main__':
    main()
