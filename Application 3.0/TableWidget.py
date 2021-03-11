from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, QHeaderView, QComboBox, \
    QAbstractItemView, QMessageBox, QWidget, QListWidget, QTableWidgetItem, QLabel
from TreeWidget import TreeWidget

class TableWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.tableWidget = QTableWidget(2, 2)
        self.bool = True
        self.tableWidget.verticalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setAcceptDrops(True)
        self.tableWidget.setDragEnabled(True)

        self.tableWidget.itemChanged.connect(self.detectChangedCell)

        self.tableWidget.setIconSize(QSize(50, 20))
        # self.tableWidget.installEventFilter(self)

        imagelabel = QLabel(self)
        imagelabel.setText("AA")

        imagelabel.setScaledContents(True)
        pixmap = QtGui.QPixmap("img/Knop.png")

        # imagelabel.setPixmap(pixmap)


        self.tableWidget.setCellWidget(1, 1, imagelabel)
        self.tableWidget.cellWidget(1, 1).setGeometry(QtCore.QRect(0,0, 50, 50))

        self.listWidget = QListWidget()

        self.listWidget.setAcceptDrops(True)
        self.listWidget.setFlow(True)
        self.listWidget.setViewMode(QListWidget.IconMode)
        self.listWidget.setIconSize(QSize(60, 60))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

    def eventFilter(self, o, e):
        print(e.type)
        if e.type() == QEvent.DragEnter:  # remember to accept the enter event
            e.acceptProposedAction()
            return True
        if e.type() == QEvent.Drop:
            print("DROP")
            # handle the event
            # ...
            return True
        return False  # remember to return false for other event types

    def dropEvent(self, e):
        print("sjds")
        e.accept()

    def dragEnterEvent(self, e):
        print("DRAAGGED")
        e.accept()


    def detectChangedCell(self, item):
        if self.bool == True:
            self.bool = False
            row = item.row()
            col = item.column()
            print(row, "+", col)

            path = "img/" + self.tableWidget.item(row, col).text() + ".png"
            imagelabel2 = QLabel(self)
            pixmap2 = QtGui.QPixmap(path)


            imagelabel2.setPixmap(pixmap2)


            # self.tableWidget.setItem(row, col, QTableWidgetItem(""))
            item.setText("")
            item.setIcon(QIcon(None))
            self.tableWidget.setCellWidget(row, col, imagelabel2)

            self.bool = True

