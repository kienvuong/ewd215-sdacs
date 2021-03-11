from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 600, 600)
        self.setWindowTitle("SdACS 1.0")
        self.initUI()

    def initUI(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setText("SdACS")
        self.label.move(275, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Login")
        self.b1.clicked.connect(lambda: self.clicked("AAAA"))

    def clicked(self, text):
        self.label.setText(text)
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()

