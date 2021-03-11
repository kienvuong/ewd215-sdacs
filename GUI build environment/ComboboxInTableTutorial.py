# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QComboBox, QVBoxLayout
#
#
# class comboCompanies(QComboBox):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.setStyleSheet('font-size: 25px')
#         self.addItems(['Microsoft', 'Facebook', 'Apple', 'Google'])
#         self.currentIndexChanged.connect(self.getComboValue)
#
#     def getComboValue(self):
#         print(self.currentText())
#         # return self.currentText()
#
#
# class TableWidget(QTableWidget):
#     def __init__(self):
#         super().__init__(1, 5)
#
#         self.setHorizontalHeaderLabels(list('ABCDE'))
#         self.setColumnWidth(4, 200)
#         self.verticalHeader().setDefaultSectionSize(50)
#         self.horizontalHeader().setDefaultSectionSize(250)
#
#         combo = comboCompanies(self)
#         self.setCellWidget(0, 4, combo)
#
#
# class AppDemo(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(1600, 600)
#
#         mainLayout = QVBoxLayout()
#         table = TableWidget()
#         mainLayout.addWidget(table)
#
#         self.setLayout(mainLayout)
#
#
# app = QApplication(sys.argv)
# demo = AppDemo()
# demo.show()
# app.exit(app.exec_())

#-------------------------------------------------------
import sys
from PyQt5 import QtWidgets, QtCore

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,500)
        self.setWindowTitle('PyQt Tuts')
        self.table()


    def table(self):

        comboBox = QtWidgets.QComboBox()

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setGeometry(QtCore.QRect(220, 100, 411, 392))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)
        self.tableWidget.show()

        attr = ['one', 'two', 'three', 'four', 'five']
        i = 0
        for j in attr:
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(j))
            comboBox = QtWidgets.QComboBox()
            self.tableWidget.setCellWidget(i, 1, comboBox)
            i += 1


def run():
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())

run()
