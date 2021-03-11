#command to convert .ui to .py =  pyuic5 -x AdminConfig3.ui -o AdminConfig3.py
import socket
import threading
import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from IOlist import *
from datetime import datetime

host = socket.gethostname()
port = 9119 # port where you want to connect to

class CThread(threading.Thread):
    def __init__(self, message, name, buttonStopThread):
        threading.Thread.__init__(self)
        self.message = message
        self.name = name
        self.buttonStopThread = buttonStopThread
        self.lock = threading.RLock()
        self.paused = False
        self.lockForPause = threading.Condition(threading.Lock())

    def set_stop(self, buttonStopThread):
        self.lock.acquire()
        self.buttonStopThread = buttonStopThread
        print("stopThread == True, dus thread gaat stoppen")
        self.lock.release()

    def pause(self):
        self.paused = True
        self.lockForPause.acquire()

    def resume(self):
        self.paused = False
        self.lockForPause.notify()
        self.lockForPause.release()

    def run(self):
        s = socket.socket()
        s.connect((host, port))
        while True:
            with self.lockForPause:
                while self.paused:
                    self.lockForPause.wait()
                if self.buttonStopThread:
                    print("thread stopped")
                    break
                if not self.buttonStopThread:
                    # self.message = str(self.message) + "+" + str(self.name)
                    self.message = "A"
                    s.send(self.message.encode())
                    self.message = s.recv(1024)
                    self.message = self.message.decode()
                    time.sleep(1)
                    if self.buttonStopThread == False:
                        print("received from broker: " + self.message + str(datetime.now()))
                        ui.label1.setText(self.message)
                        # if self.name == "thread1":
                        #     ui.label1.setText(self.message)
                        #     print('Received from server for', self.name, ':', self.message)
                        # else:
                        #     ui.label2.setText(self.message)
                        #     print('Received from server for', self.name, ':', self.message)

class Ui_MainWindow(object):
    def __init__(self):
        self.started = False
        self.buttonStopThread = False
        self.paused = False
        self.started2 = False
        self.buttonStopThread2 = False
        self.paused2 = False
        self.programJson = {
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
                        0: 1,  # Enable catterpillar
                        3: 1  # Enable stopper
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
        jsonToString = str(self.programJson)

    def createNewFile(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_IOlist()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 674)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(310, 210, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(490, 210, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        #--------------------------------------------------------------------
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 350, 100, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.startThread1)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 350, 100, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.stopThread1)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 400, 110, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.pauseThread1)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(335, 400, 117, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.resumeThread1)
        #--------------------------------------------------------------------
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 450, 100, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.startThread2)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 450, 100, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.stopThread2)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 500, 110, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.pauseThread2)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(335, 500, 117, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.resumeThread2)
        #----------------------------------------------------------
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 181, 201))
        self.groupBox.setObjectName("groupBox")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 200, 181, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(self.createNewFile)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")

        self.actionSave_as_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_as_2.setObjectName("actionSave_as_2")

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionSave_as_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.label.setText(_translate("MainWindow", "TextLabel"))
        #self.label2.setText(_translate("MainWindow", "TextLabel"))
        #-------------------------------------------------------------------
        self.pushButton.setText(_translate("MainWindow", "Start Thread 1"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop Thread 1"))
        self.pushButton_3.setText(_translate("MainWindow", "Pause Thread 1"))
        self.pushButton_4.setText(_translate("MainWindow", "Resume Thread 1"))
        #---------------------------------------------------------------------
        self.pushButton_5.setText(_translate("MainWindow", "Start Thread 2"))
        self.pushButton_6.setText(_translate("MainWindow", "Stop Thread 2"))
        self.pushButton_7.setText(_translate("MainWindow", "Pause Thread 2"))
        self.pushButton_8.setText(_translate("MainWindow", "Resume Thread 2"))
        #-----------------------------------------------------------------------
        self.groupBox.setTitle(_translate("MainWindow", "Logical Operators"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Sensors"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Open"))
        self.actionSave_as.setText(_translate("MainWindow", "Save"))
        self.actionSave_as_2.setText(_translate("MainWindow", "Save as"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    def startThread1(self):
        if not self.started:
            self.buttonStopThread = False
            self.t1 = CThread('01010101', 'thread1', self.buttonStopThread)
            self.t1.start()
            self.started = True
            print("thread just started and is active")
        else:
            print("thread already started")

    def pauseThread1(self):
        try:
            if not self.paused and self.t1.isAlive():
                try:
                    self.t1.pause()
                    self.paused = True
                    print("Thread paused")
                except:
                    print("Pause not possible")
            else:
                print("Thread already paused")
        except:
            print("No thread to pause")

    def resumeThread1(self):
        try:
            if self.paused and self.t1.isAlive():
                try:
                    self.t1.resume()
                    self.paused = False
                    print('Thread resumed')
                except:
                    print("Resume not possible")
            else:
                print("Nothing to resume")
        except:
            print("No thread to resume")

    def stopThread1(self):
        try:
            self.buttonStopThread = True
            self.t1.set_stop(self.buttonStopThread)
            # self.t1.join()
            self.started = False
            del(self.t1)
        except:
            print("No thread found")
    #-------------------------------------------------------------
    def startThread2(self):
        if not self.started2:
            self.buttonStopThread2 = False
            self.t2 = CThread('01010101', 'thread2', self.buttonStopThread2)
            self.t2.start()
            self.started2 = True
            print("thread just started and is active")
        else:
            print("thread already started")

    def pauseThread2(self):
        try:
            if not self.paused2 and self.t2.isAlive():
                try:
                    self.t2.pause()
                    self.paused2 = True
                    print("Thread paused")
                except:
                    print("Pause not possible")
            else:
                print("Thread already paused")
        except:
            print("No thread to pause")

    def resumeThread2(self):
        try:
            if self.paused2 and self.t2.isAlive():
                try:
                    self.t2.resume()
                    self.paused2 = False
                    print('Thread resumed')
                except:
                    print("Resume not possible")
            else:
                print("Nothing to resume")
        except:
            print("No thread to resume")

    def stopThread2(self):
        try:
            self.buttonStopThread2 = True
            self.t2.set_stop(self.buttonStopThread2)
            # self.t1.join()
            self.started2 = False
            del(self.t2)
        except:
            print("No thread found")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())



