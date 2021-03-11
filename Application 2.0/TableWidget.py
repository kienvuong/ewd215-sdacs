from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, QHeaderView, QComboBox, \
    QAbstractItemView, QMessageBox, QWidget


class TableWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.tableWidget = QTableWidget(0, 3)
        self.tableWidget.setHorizontalHeaderLabels(['Object', 'Bit Position', 'True/False'])
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.type = "Condition"

        self.buttonLayout = QHBoxLayout()

        self.buttonAddRow = QPushButton('Add')
        self.buttonAddRow.clicked.connect(lambda: self._addRow(str(self.type)))
        self.buttonAddRow.setGeometry(0, 0, 50, 50)

        self.buttonRemoveRow = QPushButton('Remove')
        self.buttonRemoveRow.clicked.connect(lambda: self._removeRow())

        # self.buttonReadData = QPushButton('Read Data')
        # self.buttonReadData.clicked.connect(lambda: self.readData())

        self.buttonLayout.addWidget(self.tableWidget)
        self.buttonLayout.addWidget(self.buttonAddRow, alignment=Qt.AlignTop)
        self.buttonLayout.addWidget(self.buttonRemoveRow, alignment=Qt.AlignTop)
        # self.buttonLayout.addWidget(self.buttonReadData, alignment=Qt.AlignTop)

        self.setLayout(self.buttonLayout)

    def readData(self):
        rowCount = self.tableWidget.rowCount()
        columnCount = self.tableWidget.columnCount()
        rowData = ""

        for row in range(rowCount):
            for column in range(columnCount):
                if isinstance(self.tableWidget.cellWidget(row, column), ComboBoxActuators) or \
                        isinstance(self.tableWidget.cellWidget(row, column), ComboBoxSensors) or \
                        isinstance(self.tableWidget.cellWidget(row, column), ComboBoxTrueFalse):
                            rowData = rowData + self.tableWidget.cellWidget(row, column).currentText()
                else:
                    rowData = rowData + self.tableWidget.item(row, column).text()
        print(rowData)

    def _addRow(self, type):
        rowCount = self.tableWidget.rowCount()
        self.type = type
        self.tableWidget.insertRow(rowCount)
        if self.type == "Set Output":
            self.tableWidget.comboBoxActuators = ComboBoxActuators(self.tableWidget)
            self.tableWidget.setCellWidget(rowCount, 0, self.tableWidget.comboBoxActuators)
        else:
            self.tableWidget.comboBoxSensors = ComboBoxSensors(self.tableWidget)
            self.tableWidget.setCellWidget(rowCount, 0, self.tableWidget.comboBoxSensors)

        self.tableWidget.comboBoxTrueFalse = ComboBoxTrueFalse(self.tableWidget)
        self.tableWidget.setCellWidget(rowCount, 2, self.tableWidget.comboBoxTrueFalse)

    def _removeRow(self):
        if self.tableWidget.currentRow() == -1:
            self.tableWidget.removeRow(self.tableWidget.rowCount() - 1)
        else:
            self.tableWidget.removeRow(self.tableWidget.currentRow())

    def removeAllRows(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)

class ComboBoxTrueFalse(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('font-size: 15px')
        self.addItems(['True', 'False'])

    def getComboValue(self):
        print(self.currentText())

class ComboBoxSensors(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('font-size: 15px')
        self.addItems(['Bewegingssensor', 'Metaaldetector', 'Reflectiesensor'])

class ComboBoxActuators(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('font-size: 15px')
        self.addItems(['Loopband', 'Arm', 'Stopper'])
