from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QPushButton, QGraphicsView, QLabel, QGraphicsLineItem
from GraphicsScene import GraphicsScene
from PixmapItem import TerminalItem, Edge, PixmapItem


class GraphicsView(QGraphicsView):
    def __init__(self, parent):
        QGraphicsView.__init__(self, parent)
        self.setGeometry(QRect(250, 25, 530, 600))
        self.setAcceptDrops(True)

        self.graphicsScene = GraphicsScene(self)
        self.setScene(self.graphicsScene)
        self.setRenderHints(QtGui.QPainter.Antialiasing)
        self.line_item = QGraphicsLineItem()
        self.line_item.setPen(QtGui.QPen(QtGui.QColor("green"), 4))
        self.scene().addItem(self.line_item)
        self.line_item.hide()
        self.itemList = []

        self.start_item = None
        self.end_item = None

    def mousePressEvent(self, event):
        items = self.items(event.pos())
        for x in items:
            if isinstance(x, PixmapItem):
                for item in items:
                    if isinstance(item, TerminalItem):
                        item.setPen(QtGui.QPen(QtCore.Qt.yellow, 4))
                        self.line_item.show()
                        sp = item.end()
                        line = QtCore.QLineF(sp, sp)
                        self.line_item.setLine(line)
                        self.start_item = item
                        break
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        for item in self.items():
            if isinstance(item, TerminalItem):
                for x in item.edges:
                    x.adjust()
        if self.line_item.isVisible():
            l = self.line_item.line()
            l.setP2(self.mapToScene(event.pos()))
            self.line_item.setLine(l)
            for item in self.items():
                if (
                        isinstance(item, TerminalItem)
                        and item is not self.start_item
                ):
                    item.setPen(QtGui.QPen(QtCore.Qt.transparent, 4))

            for item in self.items():
                if isinstance(item, TerminalItem):
                    item.setPen(QtGui.QPen(QtCore.Qt.black, 4))
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.line_item.isVisible():
            self.line_item.hide()
            for item in self.items():
                if isinstance(item, TerminalItem) and item:
                    item.setPen(QtGui.QPen(QtCore.Qt.transparent, 4))
            self.end_item = None
            for item in self.items(event.pos()):
                if isinstance(item, TerminalItem):
                    if item != self.start_item:
                        self.end_item = item
                    break
            if self.end_item is not None:
                edge = Edge(self.start_item, self.end_item)
                self.scene().addItem(edge)
                self.start_item = None
        super().mouseReleaseEvent(event)

    def printData(self):
        self.itemList = []
        for item in self.items():
            if isinstance(item, PixmapItem):
                self.itemList.append(item)
        print(self.itemList)




