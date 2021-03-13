from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QRect, Qt, QDataStream
from PyQt5.QtWidgets import QWidget, QPushButton, QGraphicsView, QLabel, QGraphicsScene, QGraphicsLineItem
from secretstorage import item
import substring

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
        byteArray = event.mimeData().data('application/x-qabstractitemmodeldatalist')
        itemIndex = QDataStream(byteArray).readInt32()
        itemName = event.source().item(itemIndex).text()
        source = event.source()
        x = event.scenePos().x()
        y = event.scenePos().y()
        self.addItemInList(itemName, x, y, source)

    def addItemInList(self, itemName, x, y, source):
        item = PixmapItem(itemName, x, y)

        self.addItem(item)
        # for tuple in self.itemList:
        #     for tupleElement in tuple:
                # if tupleElement == "Start":
                #     print("Start block already exist")
                # else:
                #     self.addItem(item)

        source = substring.substringByChar(str(source), startChar="<", endChar=".")
        if source == "<ListOfSensors.":
            source = "sensor"
        elif source == "<ListOfActuators.":
            source = "actuator"
        else:
            source = "operator"

        t = (itemName, source, item)
        name = t[0]
        item.setName(name)
        self.itemList.append(t)
        print(self.itemList)


    def removeItemInList(self):
        self.loopCount = 0
        for selectedItem in self.selectedItems():
            if isinstance(selectedItem, Edge):
                selectedItem.delete()
            for listItem in self.itemList:
                for tupleItem in listItem:
                    if selectedItem == tupleItem:
                        del self.itemList[self.loopCount]
                self.loopCount += 1
            self.removeItem(selectedItem)



















