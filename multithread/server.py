import socket

host = socket.gethostname()
port = 9008

s = socket.socket()
s.connect((host, port))

print(f"Connecting to server: {host} on port: {port}")

def Client():
    message = input('- type "exit" to disconnect \n'
                    '--> send to client: ')
    while True:
        if message == 'exit':
            s.close()
            break
        else:
            s.send(message.encode('utf-8'))
            data = s.recv(1024).decode('utf-8')
            # print('Received from server: ' + data)
        # message = input('==> send to client: ')

Client()
