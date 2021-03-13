from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QPushButton, QGraphicsView, QListWidget, QListWidgetItem
from PyQt5 import QtWidgets

class ListOfOperators(QListWidget):
    def __init__(self, parent):
        QListWidget.__init__(self, parent)
        self.setGeometry(QRect(15, 425, 200, 150))
        self.setDragEnabled(True)

        l1 = QListWidgetItem("And")
        l2 = QListWidgetItem("Or")
        l3 = QListWidgetItem("Start")

        self.insertItem(1, l1)
        self.insertItem(2, l2)
        self.insertItem(3, l3)