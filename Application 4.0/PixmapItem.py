from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QWidget, QPushButton, QGraphicsView, QLabel, QGraphicsScene, QGraphicsPixmapItem, \
    QGraphicsItem, QGraphicsLineItem


class PixmapItem(QGraphicsPixmapItem):
    def __init__(self, itemName, x, y):
        QGraphicsPixmapItem.__init__(self)
        self.end_ports = []
        self.setPixmap(QPixmap("img/"+ itemName +".png").scaled(64, 64))
        self.setFlag(self.ItemIsMovable, True)
        self.setFlag(self.ItemIsSelectable, True)
        self.setPos(x - 32, y - 32)
        self.create_end_ports()

    def create_end_ports(self):
        up = TerminalItem(QtCore.QLineF(QtCore.QPointF(29, 0), QtCore.QPointF(35, 0)), self)
        right = TerminalItem(QtCore.QLineF(QtCore.QPointF(64, 29), QtCore.QPointF(64, 35)), self)
        down = TerminalItem(QtCore.QLineF(QtCore.QPointF(29, 64), QtCore.QPointF(35, 64)), self)
        left = TerminalItem(QtCore.QLineF(QtCore.QPointF(0, 29), QtCore.QPointF(0, 35)), self)

        self.end_ports.append(up)
        self.end_ports.append(right)
        self.end_ports.append(down)
        self.end_ports.append(left)

class TerminalItem(QGraphicsLineItem):
    def __init__(self, line, parent=None):
        super().__init__(line, parent)
        self.setAcceptHoverEvents(True)
        self.setPen(QtGui.QPen(QtGui.QColor(QtCore.Qt.transparent), 4))
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)

    def deleteEdge(self, edge):
        self.edges.remove(edge)

    def mousePressEvent(self, event):
        event.accept()

    def mouseMoveEvent(self, event):
        event.accept()

    def end(self):
        return self.mapToScene(self.line().p1())

    def hoverEnterEvent(self, event):
        self.setPen(QtGui.QPen(QtGui.QColor(QtCore.Qt.darkYellow), 4))

    def hoverLeaveEvent(self, event):
        self.setPen(QtGui.QPen(QtGui.QColor(QtCore.Qt.transparent), 7))

class Edge(QGraphicsLineItem):
    def __init__(self, source, dest, parent=None):
        super().__init__(parent)
        self.setFlag(self.ItemIsSelectable, True)

        self.source = source
        self.dest = dest
        self.source.addEdge(self)
        self.dest.addEdge(self)
        self.setPen(QtGui.QPen(QtCore.Qt.blue, 1.75))
        self.adjust()

    def adjust(self):
        self.prepareGeometryChange()
        self.setLine(QtCore.QLineF(self.dest.end(), self.source.end()))

    def delete(self):
        self.source.deleteEdge(self)
        self.dest.deleteEdge(self)






