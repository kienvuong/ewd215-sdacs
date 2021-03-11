# met deze client-server verbinding kan je het volgende:
# 1. lijst van beschikbare functies weergeven
# 2. een functie aanroepen vanuit de client
# 3. argumenten meegeven aan de functies om de functie te kunnen uitvoeren
# 4. de connectie kunnen sluiten vanuit de client

import socket

host = socket.gethostname()
port = 8000

s = socket.socket()
s.connect((host, port))

def PrintFunctie():
    print("Test")

def SendAndReceive(data):
    s.send(data.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    return data

def Client():

    message = input('- type "exit" to disconnect \n'
                    '- type "list" to show all functions \n'
                    '- type a functionname to start the function \n '
                    '--> ')
    # while message != 'exit' :
    while True:
        if message == 'exit':
            s.close()
            break
        # substract function
        elif message == 'substract':
            while True:
                print('Type exit to choose new function')
                input1 = input("Enter first number, floats not allowed:")
                if input == 'exit':
                    s.close()
                    break
                try:
                    int(input1)
                    print('First number is: ' + input1)
                    break;
                except ValueError:
                    print("This is not a number. Please enter a valid number")
            while True:
                print('Type exit to choose new function')
                input2 = input("Enter second number, floats not allowed:")
                if input == 'exit':
                    break
                try:
                    int(input2)
                    print('Second number is: ' + input2)
                    break;
                except ValueError:
                    print("This is not a number. Please enter a valid number")

            data = "substract " + str(input1) + " and " +str(input2)
            answer = SendAndReceive(data)
            print("Antwoord is:  " + answer)
        #add function
        elif message == 'add':
            print('Type exit to choose new function')
            while True:
                input1 = input("Enter first number, floats not allowed:")
                if input1 == 'exit':
                    s.close()
                    break
                try:
                    int(input1)
                    print('First number is: ' + input1)
                    break;
                except ValueError:
                    print("This is not a number. Please enter a valid number")
            while True:
                print('Type exit to choose new function')
                input2 = input("Enter second number, floats not allowed:")
                if input2 == 'exit':
                    break
                try:
                    int(input2)
                    print('Second number is: ' + input2)
                    break;
                except ValueError:
                    print("This is not a number. Please enter a valid number")

            data = "add " + str(input1) + " and " +str(input2)
            answer = SendAndReceive(data)
            print("Antwoord is:  " + answer)
        #list functions
        elif message == 'list':
            s.send(message.encode('utf-8'))
            data = s.recv(1024).decode('utf-8')
            print(data)
        #getRandomBytes
        elif message == 'start':
            s.send(message.encode('utf-8'))
            data = s.recv(1024).decode('utf-8')
            print(data)
        #getRandomBytesRealTime
        elif message == 'realtime':
            while True:
                s.send(message.encode('utf-8'))
                data = s.recv(1024).decode('utf-8')
                print(data)
        else:
            s.send(message.encode('utf-8'))
            data = s.recv(1024).decode('utf-8')
            print('Received from server: ' + data)

        message = input('==> ')

Client()



