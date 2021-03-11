# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Config.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, QHeaderView, QComboBox, \
    QTableWidgetItem


class StartWindow(object):
    def setupStartWindow(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow")
        MainWindow2.resize(537, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButtonNextStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNextStep.setGeometry(QtCore.QRect(390, 320, 101, 31))
        self.pushButtonNextStep.setObjectName("Next Step")

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "AA"))
        self.pushButtonNextStep.setText(_translate("MainWindow2", "Next Step"))

class ComboBoxTrueFalse(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('font-size: 15px')
        self.addItems(['True', 'False'])
        # self.currentIndexChanged.connect(self.getComboValue)

    def getComboValue(self):
        print(self.currentText())

class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__(1, 3)
        self.setHorizontalHeaderLabels(['Name', 'Bit Position', 'True/False'])
        self.verticalHeader().setDefaultSectionSize(25)
        self.horizontalHeader().setDefaultSectionSize(120)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.combo = ComboBoxTrueFalse(self)
        self.setCellWidget(0, 2, self.combo)

    def _addRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        self.combo = ComboBoxTrueFalse(self)
        self.setCellWidget(rowCount, 2, self.combo)

    def _removeRow(self):
        if self.rowCount() > 0:
            self.removeRow(self.rowCount() - 1)

class ButtonCounter:
    def __init__(self, count):
        self.counter = count

    def plus(self):
        self.counter = self.counter + 1
        print(self.counter)

    def min(self):
        if self.counter > 0:
            self.counter = self.counter - 1
            print(self.counter)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButtonNextStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNextStep.setGeometry(QtCore.QRect(390, 320, 101, 31))
        self.pushButtonNextStep.setObjectName("Next Step")

        self.pushButtonPreviousStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPreviousStep.setGeometry(QtCore.QRect(10, 320, 111, 31))
        self.pushButtonPreviousStep.setObjectName("Previous Step")

        self.pushButtonFinishConfig = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFinishConfig.setGeometry(QtCore.QRect(180, 320, 151, 31))
        self.pushButtonFinishConfig.setObjectName("Finish configuration")

        self.labelStepNumber = QtWidgets.QLabel(self.centralwidget)
        self.labelStepNumber.setGeometry(QtCore.QRect(220, 10, 51, 31))
        self.labelStepNumber.setObjectName("label")

        self.labelChooseType = QtWidgets.QLabel(self.centralwidget)
        self.labelChooseType.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.labelChooseType.setObjectName("label_2")

        self.labelGoToStep = QtWidgets.QLabel(self.centralwidget)
        self.labelGoToStep.setGeometry(QtCore.QRect(10, 270, 81, 21))
        self.labelGoToStep.setObjectName("label_3")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 50, 111, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Set Output")
        self.comboBox.addItem("Condition")
        self.comboBox.addItem("Multiple Condition")

        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(100, 270, 48, 26))
        self.spinBox_2.setObjectName("spinBox_2")

        #TABLEBOX AND CONTENT INSIDE:
        self.tableBox = QtWidgets.QGroupBox(self.centralwidget)
        self.tableBox.setGeometry(QtCore.QRect(10, 70, 520, 185))
        self.tableBox.setObjectName("tableBox")

        # self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        # self.tableWidget.setGeometry(QtCore.QRect(250, 70, 280, 72))
        # self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(0)
        # self.tableWidget.setRowCount(0)

        buttonLayout = QVBoxLayout()
        table = TableWidget()
        #counter of add button:
        buttonCountObject = ButtonCounter(1)

        buttonAdd = QPushButton('Add')
        buttonAdd.clicked.connect(table._addRow)
        buttonAdd.clicked.connect(lambda: buttonCountObject.plus())
        buttonLayout.addWidget(buttonAdd)

        buttonRemove = QPushButton('Remove')
        buttonRemove.clicked.connect(table._removeRow)
        buttonRemove.clicked.connect(lambda: buttonCountObject.min())
        buttonLayout.addWidget(buttonRemove, alignment=Qt.AlignTop)

        self.tableWidgetLayout = QHBoxLayout()
        self.tableBox.setLayout(self.tableWidgetLayout)
        self.tableWidgetLayout.addWidget(table)
        self.tableWidgetLayout.addLayout(buttonLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Configuration"))

        self.pushButtonNextStep.setText(_translate("MainWindow", "Next Step"))
        self.pushButtonPreviousStep.setText(_translate("MainWindow", "Previous Step"))
        self.pushButtonFinishConfig.setText(_translate("MainWindow", "Finish Configuration"))

        self.labelStepNumber.setText(_translate("MainWindow", "Step 1:"))
        self.labelChooseType.setText(_translate("MainWindow", "Choose type:"))
        self.labelGoToStep.setText(_translate("MainWindow", "Go to step:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # MainWindow2 = QtWidgets.QMainWindow()
    # ui = StartWindow()
    # ui.setupStartWindow(MainWindow2)
    # MainWindow2.show()

    sys.exit(app.exec_())


