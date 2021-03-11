import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QListWidget, QHBoxLayout, QListWidgetItem, QGraphicsView, \
    QGraphicsEllipseItem, QGraphicsScene, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QPointF, QRect
from IOlist import *

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

class Workfield_UI(object):
    def __init__(self):
        self.movingObject = MovingObject()
        self.started = False
        self.buttonStopThread = False
        self.paused = False
        self.programJson = {
            "config": {
                "byteSize": 1,
            },
            "steps": {
                0: {
                    "name": "INIT",
                    "init": True,
                    "next": 1
                },
                1: {
                    "name": "DetectBlock",
                    "conditions": {
                        0: 1 #detect presence of block
                    },
                    "next": 2
                },
                2: {
                    "name": "TurnOnCatterpillar",
                    "set": {
                        0: 1,  # Enable catterpillar
                        3: 1  # Enable stopper
                    },
                    "next": 3
                },
                3: {
                    "name": "DetectColor",
                    "multipleConditions": {
                        "orange:": {
                            "conditions": {
                                1: 0,
                                2: 1
                            },
                            "next": 4
                        },
                        "black:": {
                            "conditions": {
                                1: 0,
                                2: 0
                            },
                            "next": 5
                        },
                        "metal:": {
                            "conditions": {
                                1: 1,
                                2: 1
                            },
                            "next": 6
                        }
                    }
                },
                4: {
                    "name": "TurnOffGates",
                    "set": {
                        1: 0,
                        2: 0
                    },
                    "next": 7
                },
                5: {
                    "name": "TurnBlackGate",
                    "set": {
                        1: 0,
                        2: 1
                    },
                    "next": 7
                },
                6: {
                    "name": "TurnMetalGate",
                    "set": {
                        1: 1,
                        2: 0
                    },
                    "next": 7
                },
                7: {
                    "name": "DetectStorage",
                    "conditions": {
                        2: 1
                    },
                    "next": 8
                },
                8: {
                    "name": "TurnOffMachine",
                    "set": {
                        0: 0,
                        1: 0,
                        2: 0,
                        3: 0
                    },
                    "next": 1
                },
            }
        }
        jsonToString = str(self.programJson)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 674)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #LOGICAL OPERATORS BOX------------------------------------------------------
        self.logicalOperatorsList = QListWidget()

        self.logicalOperatorsList.setViewMode(QListWidget.IconMode)
        self.logicalOperatorsList.setAcceptDrops(False)
        self.logicalOperatorsList.setDragEnabled(True)

        widgetLO1 = QListWidgetItem(QIcon("A.png"), "And")
        widgetLO2 = QListWidgetItem(QIcon("OR.png"), "Or")
        widgetLO3 = QListWidgetItem(QIcon("sorteerband.png"), "Sorteerband")

        self.logicalOperatorsList.addItem(widgetLO1)
        self.logicalOperatorsList.insertItem(2, widgetLO2)

        self.logicalOperatorsBox_layout = QHBoxLayout()
        self.logicalOperatorsBox_layout.addWidget(self.logicalOperatorsList)

        self.logicalOperatorsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.logicalOperatorsBox.setGeometry(QtCore.QRect(0, 0, 181, 201))
        self.logicalOperatorsBox.setLayout(self.logicalOperatorsBox_layout)
        self.logicalOperatorsBox.setObjectName("logicalOperatorsBox")

        #SENSORS BOX------------------------------------------------------
        self.sensorsWidgetList = QListWidget()

        self.sensorsWidgetList.setViewMode(QListWidget.IconMode)
        self.sensorsWidgetList.setAcceptDrops(False)
        self.sensorsWidgetList.setDragEnabled(True)

        widgetSensor1 = QListWidgetItem(QIcon("metaaldetector.png"), "Metaaldetector")
        widgetSensor2 = QListWidgetItem(QIcon("reflectiesensor.png"), "Reflectiesensor")
        widgetSensor3 = QListWidgetItem(QIcon("bewegingssensor.png"), "Bewegingssensor")

        self.sensorsWidgetList.insertItem(1, widgetSensor1)
        self.sensorsWidgetList.insertItem(2, widgetSensor2)

        self.sensorsBox_layout = QHBoxLayout()
        self.sensorsBox_layout.addWidget(self.sensorsWidgetList)

        self.sensorsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.sensorsBox.setGeometry(QtCore.QRect(0, 200, 181, 161))
        self.sensorsBox.setLayout(self.sensorsBox_layout)
        self.sensorsBox.setObjectName("sensorsBox")

        #GRAPHICSVIEW BOX (WORKFIELD)------------------------------------------------------
        self.graphicView = QGraphicsView()
        self.scene = QGraphicsScene()
        self.graphicView.setScene(self.scene)
        self.scene.setSceneRect(0, 0, 670, 550)

        self.graphicViewBox_layout = QHBoxLayout()
        self.graphicViewBox_layout.addWidget(self.graphicView)

        self.graphicViewBox = QtWidgets.QGroupBox(self.centralwidget)
        self.graphicViewBox.setGeometry(QtCore.QRect(200, 0, 700, 600))
        self.graphicViewBox.setLayout(self.graphicViewBox_layout)

        #ADD ITEM TO GRAPHICSVIEW BOX------------------------------------------
        self.scene.addItem(self.movingObject)
        self.movingObject.setMargins(self.scene.sceneRect())

        #DELETE BUTTON---------------------------------------------------------
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(50, 450,100, 25))
        self.deleteButton.setObjectName("Delete_Button")
        self.deleteButton.clicked.connect(self.removeItem)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")

        self.actionSave_as_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_as_2.setObjectName("actionSave_as_2")

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionSave_as_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.label.setText(_translate("MainWindow", "TextLabel"))
        self.logicalOperatorsBox.setTitle(_translate("MainWindow", "Logical Operators"))
        self.sensorsBox.setTitle(_translate("MainWindow", "Sensors"))
        # self.workfieldBox.setTitle(_translate("MainWindow", "Workfield"))
        self.graphicViewBox.setTitle(_translate("MainWindow", "Workfield"))
        self.deleteButton.setText(_translate("MainWindow", "Delete Item"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Open"))
        self.actionSave_as.setText(_translate("MainWindow", "Save"))
        self.actionSave_as_2.setText(_translate("MainWindow", "Save as"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    def removeItem(self):
        itemList = []
        for index in range(self.workfield.count()):
            itemList.append(self.workfield.item(index))
        print(itemList)

        listItems = self.workfield.selectedItems()
        if not listItems: return
        for item in listItems:
            self.workfield.takeItem(self.workfield.row(item))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Workfield_UI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())