# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QWidget, QApplication, QListWidget, QHBoxLayout, QListWidgetItem
# from PyQt5.QtGui import QIcon
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.myListWidget1 = QListWidget()
#         self.myListWidget2 = QListWidget()
#         self.myListWidget3 = QListWidget()
#
#         self.myListWidget1.setViewMode(QListWidget.IconMode)
#
#         self.myListWidget1.setAcceptDrops(False)
#         self.myListWidget1.setDragEnabled(True)
#
#         self.myListWidget2.setAcceptDrops(True)
#         self.myListWidget2.setDragEnabled(True)
#
#         self.myListWidget3.setAcceptDrops(True)
#         self.myListWidget3.setDragEnabled(True)
#
#         self.setGeometry(300, 350, 500, 300)
#
#         self.hboxlayout = QHBoxLayout()
#         self.hboxlayout.addWidget(self.myListWidget1)
#         self.hboxlayout.addWidget(self.myListWidget2)
#         self.hboxlayout.addWidget(self.myListWidget3)
#
#
#         l1 = QListWidgetItem(QIcon("motor.png"), "Motor")
#         l2 = QListWidgetItem(QIcon("lamp.png"), "Lamp")
#         l3 = QListWidgetItem(QIcon("sorteerband.png"), "Sorteerband")
#         l4 = QListWidgetItem(QIcon("stopper.png"), "Metaaldetector")
#
#         self.myListWidget1.insertItem(1, l1)
#         self.myListWidget1.insertItem(2, l2)
#         self.myListWidget1.insertItem(3, l3)
#         # self.myListWidget1.insertItem(4, l4)
#
#         QListWidgetItem(QIcon("metaaldetector.png"), "Metaaldetector", self.myListWidget1)
#         QListWidgetItem(QIcon("reflectiesensor.png"), "Reflectiesensor", self.myListWidget2)
#
#
#         self.setWindowTitle("Tutorial")
#         self.setLayout(self.hboxlayout)
#
#         self.show()
#
# app = QApplication(sys.argv)
# window = Window()
# sys.exit(app.exec())

#!/usr/bin/python

#--------------------------------------------------------------------------------------------------------

# import sys
#
# from PyQt5.QtWidgets import QApplication, QGraphicsView, QWidget, QGraphicsEllipseItem, QMainWindow, QGroupBox, QGraphicsScene, QHBoxLayout
# from PyQt5.QtCore import Qt, QPointF, QRect


# class MovingObject(QGraphicsEllipseItem):
#     def __init__(self, x, y, r):
#         #de meegegeven waardes gebruiken om beginpositie en grootte ellips te bepalen
#         super().__init__(0, 0, r, r)
#         self.setPos(x, y)
#         self.setBrush(Qt.red)
#         # self.setAcceptHoverEvents(False)
#
#     ## mouse hover event
#     # def hoverEnterEvent(self, event):
#     #     app.instance().setOverrideCursor(Qt.OpenHandCursor)
#     #
#     # def hoverLeaveEvent(self, event):
#     #     app.instance().restoreOverrideCursor()
#
#     ## mouse click event
#
#     ##mousePressEvent checkt of er wel of niet wordt geklikt
#     def mousePressEvent(self, event):
#         pass
#
#     ##mouseMoveEvent is om de item te kunnen draggen
#     def mouseMoveEvent(self, event):
#         orig_cursor_position = event.lastScenePos()
#         updated_cursor_position = event.scenePos()
#
#         orig_position = self.scenePos()
#
#         updated_cursor_x = updated_cursor_position.x() - orig_cursor_position.x() + orig_position.x()
#         updated_cursor_y = updated_cursor_position.y() - orig_cursor_position.y() + orig_position.y()
#         self.setPos(QPointF(updated_cursor_x, updated_cursor_y))
#
#     # def mouseReleaseEvent(self, event):
#     #     print('x: {0}, y: {1}'.format(self.pos().x(), self.pos().y()))
#
#
# class GraphicView(QGraphicsView):
#     def __init__(self):
#         super().__init__()
#
#         self.scene = QGraphicsScene()
#         self.setScene(self.scene)
#         self.setSceneRect(0, 0, 60, 60)
#         #waardes x, y, r waarvan x en y beginpositie van ellips is en r is straal van ellips
#         self.scene.addItem(MovingObject(0, 0, 40))
#
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(800, 500, 400, 400)
#         self.setWindowTitle("MainWindow")
#
#         #make Box
#         # self.move_Box_Layout = QHBoxLayout()
#         #
#         # self.move_Box = QGroupBox()
#         # self.move_Box.setGeometry(QRect(0, 0, 181, 201))
#         # self.move_Box.setLayout(self.move_Box_Layout)
#         # self.move_Box.setObjectName("logicalOperatorsBox")
#
#         #set GraphicView in Window
#         self.graphicView = GraphicView()
#         self.setCentralWidget(self.graphicView)
#
#
#
#
# app = QApplication(sys.argv)
#
# GUI = Window()
# GUI.show()
#
# sys.exit(app.exec_())
#--------------------------------------------------------------------------------------------------------
import sys

from PyQt5.QtWidgets import QApplication, QGraphicsView, QWidget, QGraphicsEllipseItem, QMainWindow, QGroupBox, QGraphicsScene, QHBoxLayout
from PyQt5.QtCore import Qt, QPointF, QRect

class MovingObject(QGraphicsEllipseItem):
    def __init__(self, x, y, r):
        super().__init__(0, 0, r, r)
        self.setPos(x, y)
        self.setBrush(Qt.red)
        self.setFlag(self.ItemIsMovable, True)
        self.setFlag(self.ItemSendsGeometryChanges, True)
        self.margins = None

    def setMargins(self, margins):
        self.margins = margins

    def itemChange(self, change, value):
        if change == self.ItemPositionChange and self.margins:
            newRect = self.boundingRect().translated(value)
            if newRect.x() < self.margins.x():
                # beyond left margin, reset
                value.setX(self.margins.x())
            elif newRect.right() > self.margins.right():
                # beyond right margin
                value.setX(self.margins.right() - newRect.width())
            if newRect.y() < self.margins.y():
                # beyond top margin
                value.setY(self.margins.y())
            elif newRect.bottom() > self.margins.bottom():
                # beyond bottom margin
                value.setY(self.margins.bottom() - newRect.height())
        return super().itemChange(change, value)


class GraphicView(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.scene.setSceneRect(0, 0, 200, 100)

        self.movingObject = MovingObject(0, 0, 40)
        self.scene.addItem(self.movingObject)
        self.movingObject.setMargins(self.scene.sceneRect())

    def drawBackground(self, painter, rect):
        painter.drawRect(self.sceneRect())

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 500, 400, 400)
        self.setWindowTitle("MainWindow")

        #make Box
        # self.move_Box_Layout = QHBoxLayout()
        #
        # self.move_Box = QGroupBox()
        # self.move_Box.setGeometry(QRect(0, 0, 181, 201))
        # self.move_Box.setLayout(self.move_Box_Layout)
        # self.move_Box.setObjectName("logicalOperatorsBox")

        #set GraphicView in Window
        self.graphicView = GraphicView()
        self.setCentralWidget(self.graphicView)


app = QApplication(sys.argv)

GUI = Window()
GUI.show()

sys.exit(app.exec_())
#-----------------------------------------------------------------------------------------------------
