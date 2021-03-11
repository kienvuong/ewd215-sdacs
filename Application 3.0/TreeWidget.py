from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, QHeaderView, QComboBox, \
    QAbstractItemView, QMessageBox, QWidget, QListWidget, QTableWidgetItem, QTreeWidget


class TreeWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setAcceptDrops(True)
        self.treeWidget.setColumnCount(2)
