from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QPushButton, QGraphicsView, QListWidget, QListWidgetItem
from PyQt5 import QtWidgets

class ListOfSensors(QListWidget):
    def __init__(self, parent):
        QListWidget.__init__(self, parent)
        self.setGeometry(QRect(15, 225, 200, 150))
        self.setDragEnabled(True)

        self.insertItem(1, QListWidgetItem("Knop"))