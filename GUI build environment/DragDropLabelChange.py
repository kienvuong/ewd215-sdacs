import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor
from PyQt5.QtCore import Qt, QMimeData, QPointF
from PyQt5 import QtCore, QtGui, QtWidgets


class DragLabel(QLabel):
    #def mousePressEvent(self, event):
        # if event.button() == Qt.LeftButton:
        #     self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not(event.buttons() & Qt.LeftButton):
            return
        else:
            drag = QDrag(self)

            mimedata = QMimeData()
            mimedata.setText(self.text())

            drag.setMimeData(mimedata)

            #creating the dragging effect
            pixmap = QPixmap(self.size()) #label size

            painter = QPainter(pixmap)
            painter.drawPixmap(self.rect(), self.grab())
            painter.end()

            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.exec_(Qt.CopyAction | Qt.MoveAction)

class DropLabel(QLabel):
    def __init__(self, label, parent):
        super().__init__(label, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        # pos = event.pos()
        text = event.mimeData().text()
        self.setText(text)
        # event.acceptProposedAction()

class AppDemo(QGraphicsView):
    def __init__(self):
        super().__init__()

        label_to_drag = DragLabel('Point A', self)

        label_to_drop = DropLabel('Point B', self)
        label_to_drop.move(100, 0)

app = QApplication(sys.argv)

demo = AppDemo()
demo.show()

sys.exit(app.exec_())