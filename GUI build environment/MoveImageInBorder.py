import sys

from PyQt5.QtWidgets import QApplication, QGraphicsView, QWidget, QGraphicsEllipseItem, QMainWindow, QGroupBox, QGraphicsScene, QHBoxLayout
from PyQt5.QtCore import Qt, QPointF, QRect
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class MovingObject(QtWidgets.QGraphicsPixmapItem):
    def __init__(self):
        super().__init__(QtGui.QPixmap('bob.png').scaled(64, 64))

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

        #make scene in QGraphicsView
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        #define rectangle which is a border
        self.scene.setSceneRect(0, 0, 500, 500)

        #instantiate object from MovingObject() and set scale of item:
        self.movingObject = MovingObject()

        #add item in scene:
        self.scene.addItem(self.movingObject)

        #set border where item can be moved:
        self.movingObject.setMargins(self.scene.sceneRect())

    #draw border with self.sceneRect()
    def drawBackground(self, painter, rect):
        painter.drawRect(self.sceneRect())

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 500, 800, 800)
        self.setWindowTitle("MainWindow")

        self.graphicView = GraphicView()
        self.setCentralWidget(self.graphicView)


app = QApplication(sys.argv)
GUI = Window()
GUI.show()

sys.exit(app.exec_())

