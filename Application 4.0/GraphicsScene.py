from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QRect, Qt, QDataStream
from PyQt5.QtWidgets import QWidget, QPushButton, QGraphicsView, QLabel, QGraphicsScene, QGraphicsLineItem
from secretstorage import item

from PixmapItem import PixmapItem, Edge


class GraphicsScene(QGraphicsScene):
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.setSceneRect(0, 0, 530, 600)
        self.itemList = []
        self.itemIndex = 0

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        print("DROPPED")
        byteArray = event.mimeData().data('application/x-qabstractitemmodeldatalist')
        itemIndex = QDataStream(byteArray).readInt32()
        itemName = event.source().item(itemIndex).text()
        x = event.scenePos().x()
        y = event.scenePos().y()
        self.addItemInList(itemName, x, y)

    def addItemInList(self, itemName, x, y):
        self.addItem(PixmapItem(itemName, x, y))
        print(PixmapItem(itemName, x, y).sceneBoundingRect())

    def removeItemInList(self):
        for x in self.selectedItems():
            if isinstance(x, Edge):
                x.delete()
            self.removeItem(x)





















