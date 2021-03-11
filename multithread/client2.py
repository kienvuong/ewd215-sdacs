#met multithread kunnen er meerdere clients verbinden met de server
#elke client krijgt een poort toegewezen
#voor elke client die wil verbinden met de server, wordt er een thread aangemaakt

import socket
import threading

def Enc(message):
    return message.encode('utf-8')

def Dec(message):
    return message.decode('utf-8')

host = socket.gethostname()
port = 9008

counter = 0

s = socket.socket()
try:
    s.bind((host, port))
    s.listen(1)
except Exception as e:
    raise SystemExit('connection not succesful')

def connection_new_client(client, connection):
    ip = connection[0]
    port = connection[1]
    print(f"Connection succesful from IP: {ip} and port : {port}")
    while True:
        data = Dec(client.recv(1024))
        if not data:
            print('No message from client or exit, connection will be broken now')
            s.close()
            break
        print('Message from a server: ' + data)
        client.sendall(Enc(data.upper()))
        break
    client.close()

while True:
    try:
        client, ip = s.accept()
        threading._start_new_thread(connection_new_client, (client, ip))
    except Exception as e:
        print(f"starting a thread not succesfully:  {e}")
    # if counter == 0:
    #     s.shutdown()
