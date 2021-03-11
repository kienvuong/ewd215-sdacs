from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout, QListWidgetItem, QListView, QPushButton, \
    QLabel, QLayout, QComboBox, QVBoxLayout, QTreeWidget, QGridLayout
from PyQt5.QtGui import QIcon
from TableWidget import TableWidget

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 650)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.myListWidget1 = QListWidget(self.centralwidget)
        self.myListWidget1.setGeometry(QtCore.QRect(30, 50, 100, 31))
        self.myListWidget1.setViewMode(QListWidget.IconMode)
        self.myListWidget1.setIconSize(QSize(50, 50))

        self.myListWidget2 = QListWidget(self.centralwidget)
        self.myListWidget2.setGeometry(QtCore.QRect(30, 50, 100, 31))
        self.myListWidget2.setViewMode(QListWidget.IconMode)
        self.myListWidget2.setIconSize(QSize(100, 100))

        self.myListWidget1.setDragEnabled(True)
        self.myListWidget1.setAcceptDrops(True)
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(False)
        self.myListWidget2.itemChanged.connect(lambda: self.limitDrops())

        self.tableWidget = TableWidget()

        funList = QListWidget(self.centralwidget)
        funList.setIconSize(QSize(50,50))
        funList.setFlow(True)
        # Create widget
        itemN = QListWidgetItem()
        widget = QWidget()
        widgetComboBox = QComboBox()
        widgetComboBox.setGeometry(QtCore.QRect(30, 50, 10, 11))
        widgetLayout = QVBoxLayout()
        widgetLayout.addWidget(widgetComboBox)

        # widgetLayout.setSizeConstraint(QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)
        # itemN.setSizeHint(widget.sizeHint())
        itemN.setSizeHint(QSize(100, 70))

        self.pushButtonDebug = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDebug.setText("Debug")
        self.pushButtonDebug.clicked.connect(lambda: self.getAmountItems())

        self.pushButtonDelete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDelete.setText("Delete")
        self.pushButtonDelete.clicked.connect(lambda: self.deleteItem())

        self.myLayout = QHBoxLayout()
        # self.myLayout.addWidget(self.myListWidget1)
        # self.myLayout.addWidget(self.myListWidget2)
        self.myLayout.addWidget(funList)

        self.myLayout.addWidget(self.tableWidget)
        self.myLayout.addWidget(self.pushButtonDebug)
        self.myLayout.addWidget(self.pushButtonDelete)

        l1 = QListWidgetItem(QIcon('img/Lamp.png'), "Lamp")
        l2 = QListWidgetItem(QIcon('img/Loopband.png'), "Loopband")
        l3 = QListWidgetItem(QIcon('img/Knop.png'), "Knop")
        l4 = QListWidgetItem(QIcon('img/Loopband.png'), "Loopband")

        self.myListWidget1.insertItem(1, l1)
        self.myListWidget1.insertItem(2, l2)
        # self.myListWidget1.insertItem(3, l3)


        funList.insertItem(1, l2)
        funList.insertItem(2, l3)

        # Add widget to QListWidget funList
        # funList.addItem(itemN)
        funList.addItem(itemN)
        funList.setItemWidget(itemN, widget)
        funList.insertItem(3, l4)
        funList.setAcceptDrops(True)
        funList.setViewMode(QListWidget.IconMode)

        self.centralwidget.setLayout(self.myLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def limitDrops(self):
        if self.myListWidget2.count() >= 2:
            self.myListWidget2.setAcceptDrops(False)

    def deleteItem(self):
        self.myListWidget2.takeItem(self.myListWidget2.count() - 1)

    def getAmountItems(self):
        print(self.myListWidget2.count())

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


