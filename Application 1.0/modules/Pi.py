import random

class Pi:
    def __init__(self, data):
        self.data = data

    def sendToPi(self):
        # print("Pi received from server = " + self.data)
        return self.data

    def GetRandomByte(self):
        value = '01'
        randomByte = ''.join(random.choice(value) for i in range(8))
        return randomByte

    def receiveFromPi(self):
        self.data = self.GetRandomByte()
        return self.data