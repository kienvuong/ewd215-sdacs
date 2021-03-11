from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QLabel, QGraphicsView, QPushButton

from GraphicsView import GraphicsView
from ListOfActuators import ListOfActuators
from ListOfSensors import ListOfSensors
from ListOfOperators import ListOfOperators

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = GraphicsView(self.centralwidget)
        self.graphicsViewTitle = QLabel(self.centralwidget)
        self.graphicsViewTitle.setText("Workfield")
        self.graphicsViewTitle.setGeometry(QRect(250, 6, 70, 20))

        self.listOfActuators = ListOfActuators(self.centralwidget)
        self.listOfActuatorsTitle = QLabel(self.centralwidget)
        self.listOfActuatorsTitle.setText("Actuators")
        self.listOfActuatorsTitle.setGeometry(QRect(15, 6, 70, 20))

        self.listOfSensors = ListOfSensors(self.centralwidget)
        self.listOfSensorsTitle = QLabel(self.centralwidget)
        self.listOfSensorsTitle.setText("Sensors")
        self.listOfSensorsTitle.setGeometry(QRect(15, 206, 70, 20))

        self.listOfOperators = ListOfOperators(self.centralwidget)
        self.listOfOperatorsTitle = QLabel(self.centralwidget)
        self.listOfOperatorsTitle.setText("Logic Ports")
        self.listOfOperatorsTitle.setGeometry(QRect(15, 406, 80, 20))

        self.deleteItemButton = QPushButton(self.centralwidget)
        self.deleteItemButton.setText("Delete Item")
        self.deleteItemButton.setGeometry(QRect(15, 606, 90, 25))
        self.deleteItemButton.clicked.connect(lambda: self.graphicsView.graphicsScene.removeItemInList())

        self.printDataButton = QPushButton(self.centralwidget)
        self.printDataButton.setText("Print Data")
        self.printDataButton.setGeometry(QRect(115, 606, 90, 25))
        self.printDataButton.clicked.connect(lambda: self.graphicsView.printData())

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
