# met deze client-server verbinding kan je het volgende:
# 1. lijst van beschikbare functies weergeven
# 2. een functie aanroepen vanuit de client
# 3. argumenten meegeven aan de functies om de functie te kunnen uitvoeren
# 4. de connectie kunnen sluiten vanuit de client

import socket
import string
import random
from time import sleep


class Functions:

    def AddFunction(self, x, y):
        return x + y

    def SubstractFunction(self, x, y):
        return x - y

    def PrintAAA(self):
        return "AAAAAAAA"

    def GetRandomByte(self):
        value = '01'
        randomByte = ''.join(random.choice(value) for i in range(8))
        return randomByte


def Enc(message):
    return message.encode('utf-8')


def Dec(message):
    return message.decode('utf-8')


def Server():
    host = socket.gethostname()  # naam van de machine
    port = 8000  # tussen > 1024 en <65535

    instance = Functions()

    s = socket.socket()

    s.bind((host, port))
    s.listen(1)

    c, addr = s.accept()
    print("Connection from: " + str(addr))

    while True:
        data = Dec(c.recv(1024))
        if not data:
            break
        print('From online user: ' + data)
        if data.split()[0] == 'add':
            x = int(data.split()[1])
            y = int(data.split()[3])
            answer = instance.AddFunction(x, y)
            c.send(Enc(str(answer)))
        elif data.split()[0] == 'substract':
            x = int(data.split()[1])
            y = int(data.split()[3])
            answer = instance.SubstractFunction(x, y)
            c.send(Enc(str(answer)))
        elif data == 'list':
            functionString = ""
            for x in dir(Functions):
                if x.startswith('__') == False:
                    functionString = functionString + x + "\n"
            c.send(Enc(functionString))
        elif data == 'start':
            randomByte = instance.GetRandomByte()
            c.send(Enc(str(randomByte)))
        elif data == 'realtime':
            randomByte = instance.GetRandomByte()
            sleep(2)
            c.send(Enc(str(randomByte)))
        else:
            data = data.upper()
            c.send(data.encode('utf-8'))
    c.close()


Server()
