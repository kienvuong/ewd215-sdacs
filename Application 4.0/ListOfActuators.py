from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QPushButton, QGraphicsView, QListWidget, QListWidgetItem
from PyQt5 import QtWidgets

class ListOfActuators(QListWidget):
    def __init__(self, parent):
        QListWidget.__init__(self, parent)
        self.setGeometry(QRect(15, 25, 200, 150))
        self.setDragEnabled(True)

        l1 = QListWidgetItem("Loopband")
        l2 = QListWidgetItem("Lamp")

        self.insertItem(1, l1)
        self.insertItem(2, l2)

