# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Config.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 398)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 320, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButtonPreviousStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPreviousStep.setGeometry(QtCore.QRect(10, 320, 111, 31))
        self.pushButtonPreviousStep.setObjectName("pushButtonPreviousStep")
        self.pushButtonFinishConfig = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFinishConfig.setGeometry(QtCore.QRect(180, 320, 151, 31))
        self.pushButtonFinishConfig.setObjectName("pushButtonFinishConfig")
        self.labelStepNumber = QtWidgets.QLabel(self.centralwidget)
        self.labelStepNumber.setGeometry(QtCore.QRect(220, 10, 51, 31))
        self.labelStepNumber.setObjectName("labelStepNumber")
        self.comboBoxChooseType = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxChooseType.setGeometry(QtCore.QRect(110, 50, 111, 25))
        self.comboBoxChooseType.setObjectName("comboBoxChooseType")
        self.comboBoxChooseType.addItem("")
        self.comboBoxChooseType.addItem("")
        self.comboBoxChooseType.addItem("")
        self.labelChooseType = QtWidgets.QLabel(self.centralwidget)
        self.labelChooseType.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.labelChooseType.setObjectName("labelChooseType")
        self.labelGoToStep = QtWidgets.QLabel(self.centralwidget)
        self.labelGoToStep.setGeometry(QtCore.QRect(10, 270, 81, 21))
        self.labelGoToStep.setObjectName("labelGoToStep")
        self.spinBoxGoToStep = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxGoToStep.setGeometry(QtCore.QRect(100, 270, 48, 26))
        self.spinBoxGoToStep.setObjectName("spinBoxGoToStep")
        self.pushButtonAddOutput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddOutput.setGeometry(QtCore.QRect(10, 80, 89, 25))
        self.pushButtonAddOutput.setObjectName("pushButtonAddOutput")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(240, 70, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        #----------------------------------------------------------------
        buttonLayout = QVBoxLayout()
        button_new = QPushButton('New')
        # button_new.clicked.connect(table._addRow)
        buttonLayout.addWidget(button_new)

        self.tableWidget_layout = QHBoxLayout()
        self.tableWidget_layout.addWidget(self.tableWidget)

        self.tableWidget_layout.addLayout(buttonLayout)

        self.sensorsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.sensorsBox.setGeometry(QtCore.QRect(200, 150, 181, 161))
        self.sensorsBox.setLayout(self.tableWidget_layout)
        self.sensorsBox.setObjectName("sensorsBox")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 544, 22))
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
        self.pushButton.setText(_translate("MainWindow", "Next Step"))
        self.pushButtonPreviousStep.setText(_translate("MainWindow", "Previous Step"))
        self.pushButtonFinishConfig.setText(_translate("MainWindow", "Finish configuration"))
        self.labelStepNumber.setText(_translate("MainWindow", "Step 1:"))
        self.comboBoxChooseType.setItemText(0, _translate("MainWindow", "Set Output"))
        self.comboBoxChooseType.setItemText(1, _translate("MainWindow", "Condition"))
        self.comboBoxChooseType.setItemText(2, _translate("MainWindow", "Multiple Condition"))
        self.labelChooseType.setText(_translate("MainWindow", "Choose type:"))
        self.labelGoToStep.setText(_translate("MainWindow", "Go to step:"))
        self.pushButtonAddOutput.setText(_translate("MainWindow", "Add output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

