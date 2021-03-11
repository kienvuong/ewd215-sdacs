# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminConfig3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Step import Step
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButtonRemoveStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemoveStep.setGeometry(QtCore.QRect(250, 550, 101, 31))
        self.pushButtonRemoveStep.setText("Remove Step")
        self.pushButtonRemoveStep.clicked.connect(lambda: self.removeStep())

        self.pushButtonAddStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddStep.setGeometry(QtCore.QRect(350, 550, 101, 31))
        self.pushButtonAddStep.setText("Add Step")
        self.pushButtonAddStep.clicked.connect(lambda: self.addStep())

        self.pushButtonReadData = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReadData.setGeometry(QtCore.QRect(450, 550, 101, 31))
        self.pushButtonReadData.setText("Read Data")
        self.pushButtonReadData.clicked.connect(lambda: self.readData())

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 700, 520))
        self.tabWidget.setObjectName("tabWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def addStep(self):
        self.tabWidget.addTab(Step(), str(self.tabWidget.count()))

    def removeStep(self):
        if self.tabWidget.count() != 1:
            self.tabWidget.removeTab(self.tabWidget.count() - 1)

    def readData(self):
        tabCount = self.tabWidget.count()
        json = {}
        config = {}
        config["byteSize"] = 1
        steps = {}
        for tab in range(tabCount):
            step = {}
            conditions = {}
            conditionsData = self.tabWidget.widget(tab).getConditions()
            step = conditionsData
            step["name"] = "tab_" + str(tab)
            steps[tab] = step
        json["config"] = config
        json["steps"] = steps
        print(json)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

