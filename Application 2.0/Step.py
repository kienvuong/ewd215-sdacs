from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton
from TableWidget import TableWidget, ComboBoxSensors, ComboBoxActuators, ComboBoxTrueFalse

class Step(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.stepNr = None
        self.type = 0 #0 = output, 1 = condition, 2 = multiple condition
        self.conditions = None

        self.tableWidget = TableWidget()

        self.labelChooseType = QtWidgets.QLabel(self)
        self.labelChooseType.setGeometry(QtCore.QRect(10, 20, 100, 21))
        self.labelChooseType.setObjectName("type_label")
        self.labelChooseType.setText("Choose type:")

        self.comboBoxChooseType = QtWidgets.QComboBox(self)
        self.comboBoxChooseType.setGeometry(QtCore.QRect(110, 20, 155, 25))
        self.comboBoxChooseType.addItems(['Set Output', 'Condition', 'Multiple Condition'])
        self.comboBoxChooseType.activated.connect(lambda: self.changeType(self.comboBoxChooseType.currentText()))

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 650, 400))
        self.tabWidget.setObjectName("tabWidget")

        self.tabWidget.addTab(self.tableWidget, str(self.tabWidget.count()))

        self.pushButtonAddCondition = QtWidgets.QPushButton(self)
        self.pushButtonAddCondition.setGeometry(QtCore.QRect(300, 20, 100, 25))
        self.pushButtonAddCondition.setText("Add Condition")
        self.pushButtonAddCondition.hide()
        self.pushButtonAddCondition.clicked.connect(lambda: self.addMultipleConditionFor())

        self.pushButtonRemoveCondition = QtWidgets.QPushButton(self)
        self.pushButtonRemoveCondition.setGeometry(QtCore.QRect(400, 20, 140, 25))
        self.pushButtonRemoveCondition.setText("Remove Condition")
        self.pushButtonRemoveCondition.hide()
        self.pushButtonRemoveCondition.clicked.connect(lambda: self.removeMultipleConditionFor())

    def getConditions(self):
        tabCount = self.tabWidget.count()
        rowCount = self.tableWidget.tableWidget.rowCount()
        columnCount = self.tableWidget.tableWidget.columnCount()
        rowData = []
        multipleConditions = {}

        for tab in range(tabCount):
            multipleConditions[tab] = {}
            bits = {}
            for row in range(rowCount):
                # for column in range(columnCount):
                if(self.tabWidget.widget(tab).tableWidget.item(row, 1) != None):
                    bitPos = self.tabWidget.widget(tab).tableWidget.item(row, 1).text()
                else:
                    bitPos = ""
                bitVal = self.tabWidget.widget(tab).tableWidget.cellWidget(row, 2).currentText()
                if(bitVal == "True"):
                    bitVal = 1
                else:
                    bitVal = 0

                bits[bitPos] = bitVal
                if(self.comboBoxChooseType.currentText() == "Set Output"):
                    multipleConditions[tab]['set'] = bits
                else:
                    multipleConditions[tab]['conditions'] = bits
        output = {}
        if(tabCount > 1):
            output["multipleConditions"] = multipleConditions
        else:
            output = multipleConditions[0]
        print(output)
        return output

    def changeType(self, type):
        self.tableWidget.removeAllRows()
        self.tableWidget.type = type
        if type == "Multiple Condition":
            self.pushButtonAddCondition.show()
            self.pushButtonRemoveCondition.show()
        else:
            self.pushButtonAddCondition.hide()
            self.pushButtonRemoveCondition.hide()
            for x in range (self.tabWidget.count()):
                self.removeMultipleConditionFor()

    def addMultipleConditionFor(self):
        self.tabWidget.addTab(TableWidget(), str(self.tabWidget.count()))

    def removeMultipleConditionFor(self):
        if self.tabWidget.count() != 1:
            self.tabWidget.removeTab(self.tabWidget.count() - 1)