# -*- self=Nonetf-8 -*-

# Form implementation generated from reading ui file 'StartWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from AdminConfig import AdminConfig_UI
from AdminConfig2 import Ui_MainWindow

from UserConfig import UserConfig_UI
from Workfield import Workfield_UI

class Windows:
    def callUserConfig(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UserConfig_UI()
        self.ui.setupUi(self.window)
        self.window.show()
    def callAdminConfig(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def callWorkField(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Workfield_UI()
        self.ui.setupUi(self.window)
        self.window.show()

class StartWindow_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 259)
        self.windows = Windows()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.adminConfigButton = QtWidgets.QPushButton(self.centralwidget)
        self.adminConfigButton.setGeometry(QtCore.QRect(110, 60, 191, 21))
        self.adminConfigButton.setObjectName("adminConfigButton")
        self.adminConfigButton.clicked.connect(lambda: self.windows.callAdminConfig())

        self.userConfigButton = QtWidgets.QPushButton(self.centralwidget)
        self.userConfigButton.setGeometry(QtCore.QRect(110, 130, 141, 20))
        self.userConfigButton.setObjectName("userConfigButton")
        self.userConfigButton.clicked.connect(lambda: self.windows.callUserConfig())

        self.workfieldButton = QtWidgets.QPushButton(self.centralwidget)
        self.workfieldButton.setGeometry(QtCore.QRect(280, 130, 111, 20))
        self.workfieldButton.setObjectName("workfieldButton")
        self.workfieldButton.clicked.connect(lambda: self.windows.callWorkField())

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 51, 21))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 41, 21))
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 22))
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
        self.userConfigButton.setText(_translate("MainWindow", "Open configuration"))
        self.adminConfigButton.setText(_translate("MainWindow", "Open admin configuration"))
        self.workfieldButton.setText(_translate("MainWindow", "Open workfield"))
        self.label.setText(_translate("MainWindow", "Admin:"))
        self.label_2.setText(_translate("MainWindow", "User:"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = StartWindow_UI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())