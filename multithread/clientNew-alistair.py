import socket
import threading
import time


host = socket.gethostname()
port = 9114 # port where you want to connect to


class CThread(threading.Thread):
    def __init__(self, message, name):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.message = message
        self.name = name

    # Override the run() function of Thread class
    def run(self):
        s = socket.socket()
        s.connect((host, port))
        while True:
            message = self.message
            message = message.encode()
            s.send(message)
            message = s.recv(1024)
            message = message.decode()
            time.sleep(2)
            print('Received from server for', self.name,':', message)


def main():
    # Create an object of Threads
    t1 = CThread('01010101', 'thread1')
    t2 = CThread('11111111', 'thread2')

    # start the threads
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
