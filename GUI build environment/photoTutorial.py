# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'photoTutorial.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 371, 461))
        self.photo.setText("")
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 10, 371, 451))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.spaghetti = QtWidgets.QPushButton(self.centralwidget)
        self.spaghetti.setGeometry(QtCore.QRect(90, 490, 89, 25))
        self.spaghetti.setObjectName("spaghetti")

        self.bob = QtWidgets.QPushButton(self.centralwidget)
        self.bob.setGeometry(QtCore.QRect(510, 490, 89, 25))
        self.bob.setObjectName("bob")


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

        self.bob.clicked.connect(self.show_bob)
        self.spaghetti.clicked.connect(self.show_spaghetti)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.spaghetti.setText(_translate("MainWindow", "Spaghetti"))
        self.bob.setText(_translate("MainWindow", "Bob"))

    def show_bob(self):
        self.label.setPixmap(QtGui.QPixmap("bob.png"))
        self.photo.clear()

    def show_spaghetti(self):
        self.photo.setPixmap(QtGui.QPixmap("img/spaghetti.jpeg"))
        self.label.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

