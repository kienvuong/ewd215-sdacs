from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import StartWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = StartWindow.StartWindow_UI()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())

