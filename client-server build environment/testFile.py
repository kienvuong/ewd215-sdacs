import threading
import random
import socket
import json
#-----------------------------------------------------------------------------
# Random byte genereren
def GetRandomByte():
    value = '01'
    randomByte = ''.join(random.choice(value) for i in range(8))
    return randomByte

print(GetRandomByte())

#----------------------------------------------------------------------------
#Threads aanmaken en runnen
def printAAA():
    print("AAA")
def printBBB():
    print("BBB")

my_thread = threading.Thread(target=printAAA)
my_thread2 = threading.Thread(target=printBBB)

my_thread.daemon = True

my_thread.start()
my_thread2.start()

#-----------------------------------------------------------------------------
#Wat zit opgeslagen in s.accept()

# host = socket.gethostname()
# port = 9000
#
# # bind socket first
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((host, port))
# print("socket binded to port", port)
#
# # put socket in listening mode
# s.listen(5)
# print("socket is listening")
#
# c, addr = s.accept()
# print ('Got connection from', addr)

#-------------------------------------------------------------------------------
jsonArray = '{"name": "Bob", "languages": ["English", "French"]}'
data = json.loads(jsonArray)
print(data)
#-----------------------------------------------------------------------------
#play with JSON

programJson = {
    "config": {
        "byteSize": 1,
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
            "next": 3
        },
        3: {
            "name": "DetectColor",
            "multipleConditions": {
                "orange:": {
                    "conditions": {
                        1: 0,
                        2: 1
                    },
                    "next": 4
                },
                "black:": {
                    "conditions": {
                        1: 0,
                        2: 0
                    },
                    "next": 5
                },
                "metal:": {
                    "conditions": {
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
                2: 0
            },
            "next": 7
        },
        5: {
            "name": "TurnBlackGate",
            "set": {
                1: 0,
                2: 1
            },
            "next": 7
        },
        6: {
            "name": "TurnMetalGate",
            "set": {
                1: 1,
                2: 0
            },
            "next": 7
        },
        7: {
            "name": "DetectStorage",
            "conditions": {
                2: 1
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
toString = str(programJson)
print(toString)

#============================================================================
import threading
import time


class MyThread (threading.Thread):

    def __init__(self, speed):
        self._speed_cache = 0
        self.speed = speed
        self.lock = threading.RLock()
        super(MyThread, self).__init__()

    def set_speed(self, speed):  # you can use a proper setter if you want
        with self.lock:
            self.speed = speed

    def run(self):
        while True:
            with self.lock:
                if self.speed == 0:
                    print("Speed dropped to 0, exiting...")
                    break
                # just so we don't continually print the speed, print only on change
                if self.speed != self._speed_cache:
                    print("Current speed: {}".format(self.speed))
                    self._speed_cache = self.speed
            time.sleep(0.1)  # let it breathe


current_speed = 3  # initial speed

blink_thread = MyThread(current_speed)
blink_thread.start()

while current_speed != 0:  # main loop until 0 speed is selected
    time.sleep(0.1)  # wait a little for an update
    current_speed = int(input("Enter 0 to Exit or 1/2/3 to continue\n"))  # add validation?
    blink_thread.set_speed(current_speed)