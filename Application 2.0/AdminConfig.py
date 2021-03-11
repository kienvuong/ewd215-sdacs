# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Config.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, QHeaderView, QComboBox, QAbstractItemView, QMessageBox

import NewAdminConfig
import sys

class ShowWindow():
    def startWindow(self):
        self.ui1 = AdminConfig_UI("", "", "")
        self.ui1.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

class SubWindows():
    def showNewAdminConfigFile(self):
        self.ui = NewAdminConfig.MyWidget()
        self.ui.show()

class ComboBoxTrueFalse(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('font-size: 15px')
        self.addItems(['True', 'False'])

    def getComboValue(self):
        print(self.currentText())

class ComboBoxSensors(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('font-size: 15px')
        self.addItems(['Bewegingssensor', 'Metaaldetector', 'Reflectiesensor'])

class ComboBoxActuators(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('font-size: 15px')
        self.addItems(['Loopband', 'Arm', 'Stopper'])

class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__(0, 3)
        self.setHorizontalHeaderLabels(['Object', 'Bit Position', 'True/False'])
        self.verticalHeader().setDefaultSectionSize(25)
        self.horizontalHeader().setDefaultSectionSize(120)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

    def _addRow(self, type):
        rowCount = self.rowCount()
        self.type = type
        self.insertRow(rowCount)
        if self.type == "Set Output":
            self.comboBoxActuators = ComboBoxActuators(self)
            self.setCellWidget(rowCount, 0, self.comboBoxActuators)
        else:
            self.comboBoxSensors = ComboBoxSensors(self)
            self.setCellWidget(rowCount, 0, self.comboBoxSensors)

        self.comboBoxTrueFalse = ComboBoxTrueFalse(self)
        self.setCellWidget(rowCount, 2, self.comboBoxTrueFalse)

    def _removeRow(self):
        if self.currentRow() == -1:
            self.removeRow(self.rowCount() - 1)
        else:
            self.removeRow(self.currentRow())

    def removeAllRows(self):
        self.setRowCount(0)
        self.setColumnCount(3)

class ButtonCounter:
    def __init__(self):
        self.counter = 0

    def plus(self):
        self.counter = self.counter + 1
        print(self.counter)

    def min(self):
        if self.counter > 0:
            self.counter = self.counter - 1
            print(self.counter)

    def getCounter(self):
        return self.counter

class AddChooseTypeAndMC:
    def __init__(self):
        self.tabStep2 = QtWidgets.QWidget()
        self.tabWidgetMultipleConditionsS2 = QtWidgets.QTabWidget(self.tabStep2)
        self.tabWidgetMultipleConditionsS2.setGeometry(QtCore.QRect(20, 70, 530, 330))

        self.labelChooseTypeS2 = QtWidgets.QLabel(self.tabStep2)
        self.labelChooseTypeS2.setGeometry(QtCore.QRect(10, 20, 100, 21))
        self.labelChooseTypeS2.setObjectName("label_2")
        self.labelChooseTypeS2.setText("Choose type:")

        self.comboBoxChooseTypeS2 = QtWidgets.QComboBox(self.tabStep2)
        self.comboBoxChooseTypeS2.setGeometry(QtCore.QRect(110, 20, 155, 25))
        self.comboBoxChooseTypeS2.addItems(['Set Output', 'Condition', 'Multiple Condition'])
        self.comboBoxChooseTypeS2.activated.connect(lambda: self.showAddRemoveCButtonS2(self.comboBoxChooseTypeS2.currentText()))
        self.comboBoxChooseTypeS2.activated.connect(lambda: self.warning_eraseS2())

        self.pushButtonAddConditionS2 = QtWidgets.QPushButton(self.tabStep2)
        self.pushButtonAddConditionS2.setGeometry(QtCore.QRect(300, 20, 100, 25))
        self.pushButtonAddConditionS2.setText("Add Condition")
        self.pushButtonAddConditionS2.hide()
        self.pushButtonAddConditionS2.clicked.connect(lambda: self.addMultipleConditionForS2())
        self.pushButtonAddConditionS2.clicked.connect(lambda: print("wrs"))

        self.pushButtonRemoveConditionS2 = QtWidgets.QPushButton(self.tabStep2)
        self.pushButtonRemoveConditionS2.setGeometry(QtCore.QRect(400, 20, 140, 25))
        self.pushButtonRemoveConditionS2.setText("Remove Condition")
        self.pushButtonRemoveConditionS2.hide()
        self.pushButtonRemoveConditionS2.clicked.connect(lambda: self.removeMultipleConditionForS2())

        self.tableS2C2 = TableWidget()

    def addMultipleConditionForS2(self):
        self.tableS2C2 = TableWidget()

        self.tabS2C2 = QtWidgets.QWidget()

        self.tabWidgetMultipleConditionsS2.addTab(self.tabS2C2, str(self.tabWidgetMultipleConditionsS2.count()))

        self.buttonCounterS2C2 = ButtonCounter()
        self.buttonLayoutS2C2 = QVBoxLayout()
        self.tableWidgetLayoutS2C2 = QHBoxLayout()

        self.buttonAddRowS2C2 = QPushButton('Add')
        self.buttonAddRowS2C2.clicked.connect(self.tableS2C2._addRow)
        self.buttonAddRowS2C2.clicked.connect(lambda: self.buttonCounterS2C2.min())
        self.buttonLayoutS2C2.addWidget(self.buttonAddRowS2C2)

        self.buttonRemoveRowS2C2 = QPushButton('Remove')
        self.buttonRemoveRowS2C2.clicked.connect(self.tableS2C2._removeRow)
        self.buttonRemoveRowS2C2.clicked.connect(lambda: self.buttonCounterS2C2.min())
        self.buttonLayoutS2C2.addWidget(self.buttonRemoveRowS2C2, alignment=Qt.AlignTop)

        self.labelGoToStepS2C2 = QtWidgets.QLabel(self.tabS2C2)
        self.labelGoToStepS2C2.setObjectName("label_3")
        self.labelGoToStepS2C2.setText("Go to step:")
        self.buttonLayoutS2C2.addWidget(self.labelGoToStepS2C2, alignment=Qt.AlignBottom)

        self.spinBoxS2C1 = QtWidgets.QSpinBox()
        self.spinBoxS2C1.setObjectName("spinBox_3")
        self.buttonLayoutS2C2.addWidget(self.spinBoxS2C1)

        self.layoutBoxS2C1 = QtWidgets.QGroupBox(self.tabS2C2)
        self.layoutBoxS2C1.setGeometry(QtCore.QRect(0, 0, 520, 280))

        self.layoutBoxS2C1.setLayout(self.tableWidgetLayoutS2C2)
        self.tableWidgetLayoutS2C2.addWidget(self.tableS2C2)
        self.tableWidgetLayoutS2C2.addLayout(self.buttonLayoutS2C2)
        self.tabWidgetMultipleConditionsS2.addTab(self.tabS2C2, str(self.tabWidgetMultipleConditionsS2.count()))

    def warning_eraseS2(self):
        if self.tableS2C2.rowCount() != 0 or self.tabWidgetMultipleConditionsS2.count() != 1:
            warningErasePopUp = QMessageBox()
            warningErasePopUp.setWindowTitle("Warning")
            warningErasePopUp.setText("Are you sure?")
            warningErasePopUp.setInformativeText("All objects of this step will be deleted")
            warningErasePopUp.setIcon(QMessageBox.Warning)
            warningErasePopUp.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            self.result = warningErasePopUp.exec_()
            if self.result == QMessageBox.Yes:
                self.tableS2C2.removeAllRows()
                for x in range(self.tabWidgetMultipleConditionsS2.count()):
                    self.removeMultipleConditionForS2()

    def removeMultipleConditionForS2(self):
        if self.tabWidgetMultipleConditionsS2.count() != 1:
            self.tabWidgetMultipleConditionsS2.removeTab(self.tabWidgetMultipleConditionsS2.count() - 1)

    def showAddRemoveCButtonS2(self, type):
        if type == "Multiple Condition":
            self.pushButtonAddConditionS2.show()
            self.pushButtonRemoveConditionS2.show()
        else:
            self.pushButtonAddConditionS2.hide()
            self.pushButtonRemoveConditionS2.hide()

class AdminConfig_UI(object):
    def __init__(self, companyData, companyName, stationName):
        self.companyName = companyName
        self.stationName = stationName
        self.companyData = companyData
        self.checkVar()

    def checkVar(self):
        if self.stationName and self.companyName:
            print("Company name: " + self.stationName + ", Station name: " + self.companyName)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #DEFINING BUTTONS--------------------------------------------------------------------
        self.pushButtonNextStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNextStep.setGeometry(QtCore.QRect(390, 620, 101, 31))
        self.pushButtonNextStep.setObjectName("Next Step")

        self.pushButtonPreviousStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPreviousStep.setGeometry(QtCore.QRect(10, 620, 111, 31))
        self.pushButtonPreviousStep.setObjectName("Previous Step")

        self.pushButtonFinishConfig = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFinishConfig.setGeometry(QtCore.QRect(180, 620, 151, 31))
        self.pushButtonFinishConfig.setObjectName("Finish configuration")

        self.pushButtonAddCondition = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddCondition.setGeometry(QtCore.QRect(300, 50, 100, 25))
        self.pushButtonAddCondition.setObjectName("Add Condition")
        self.pushButtonAddCondition.hide()
        self.pushButtonAddCondition.clicked.connect(lambda: self.addCondition())

        self.pushButtonRemoveCondition = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemoveCondition.setGeometry(QtCore.QRect(400, 50, 140, 25))
        self.pushButtonRemoveCondition.setObjectName("Remove Condition")
        self.pushButtonRemoveCondition.hide()
        self.pushButtonRemoveCondition.clicked.connect(lambda: self.removeMultipleConditionForS1())

        self.pushButtonAddStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddStep.setGeometry(QtCore.QRect(390, 570, 101, 31))
        self.pushButtonAddStep.setObjectName("Add Step")
        self.pushButtonAddStep.clicked.connect(lambda: self.addStep())

        self.pushButtonRemoveStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemoveStep.setGeometry(QtCore.QRect(10, 570, 111, 31))
        self.pushButtonRemoveStep.setObjectName("Remove Step")
        self.pushButtonRemoveStep.clicked.connect(lambda: self.removeStep())

        #DEFINING LABELS--------------------------------------------------------------------
        self.labelCompanyName= QtWidgets.QLabel(self.centralwidget)
        self.labelCompanyName.setGeometry(QtCore.QRect(400, 1, 200, 31))
        self.labelCompanyName.setObjectName("label")

        self.labelStationName = QtWidgets.QLabel(self.centralwidget)
        self.labelStationName.setGeometry(QtCore.QRect(400, 20, 200, 31))
        self.labelStationName.setObjectName("label")

        self.labelStepNumber = QtWidgets.QLabel(self.centralwidget)
        self.labelStepNumber.setGeometry(QtCore.QRect(10, 60, 100, 31))
        self.labelStepNumber.setObjectName("label")

        #DEFINING TABWIDGET FOR STEPS--------------------------------------------------------------------
        self.tabWidgetSteps = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetSteps.setGeometry(QtCore.QRect(10, 100, 630, 450))
        self.tabWidgetSteps.setObjectName("tabWidgetChild")

        #DEFINING FIRST STEP AS FIRST TAB AND ADD TO TABWIDGET--------------------------------------------------------------------
        self.tabStep1 = QtWidgets.QWidget()
        self.tabStep1.setObjectName("tabStep1")
        self.tabWidgetSteps.addTab(self.tabStep1, "1")

        self.outerLayoutBoxS1 = QtWidgets.QGroupBox(self.tabStep1)
        self.outerLayoutBoxS1.setGeometry(QtCore.QRect(0, 0, 620, 410))
        self.outerLayoutBoxS1.setObjectName("outerLayoutBoxS1")

        self.chooseTypeLayoutS1 = QHBoxLayout()
        self.chooseTypeLayoutS1.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        #DEFINING AND ADD CHOOESETYPE COMBOBOX, LABEL, BUTTONS TO TABSTEP1 ----------------------------------
        self.labelChooseTypeS1 = QtWidgets.QLabel(self.tabStep1)
        self.labelChooseTypeS1.setGeometry(QtCore.QRect(0, 0, 100, 21))
        self.labelChooseTypeS1.setObjectName("label_2")
        self.chooseTypeLayoutS1.addWidget(self.labelChooseTypeS1)

        self.comboBoxChooseTypeS1 = QtWidgets.QComboBox()
        self.comboBoxChooseTypeS1.setGeometry(QtCore.QRect(0, 0, 10, 25))
        self.comboBoxChooseTypeS1.addItems(['Set Output', 'Condition', 'Multiple Condition'])
        self.comboBoxChooseTypeS1.activated.connect(lambda: self.warning_erase())
        self.comboBoxChooseTypeS1.activated.connect(lambda: self.showAddRemoveCButtonS1(self.comboBoxChooseTypeS1.currentText()))
        self.chooseTypeLayoutS1.addWidget(self.comboBoxChooseTypeS1)

        self.pushButtonAddConditionS1 = QtWidgets.QPushButton(self.tabStep1)
        self.pushButtonAddConditionS1.setGeometry(QtCore.QRect(300, 20, 100, 25))
        self.pushButtonAddConditionS1.setObjectName("Add Condition")
        self.pushButtonAddConditionS1.hide()
        self.pushButtonAddConditionS1.clicked.connect(lambda: self.addMultipleConditionForS1())
        self.chooseTypeLayoutS1.addWidget(self.pushButtonAddConditionS1)

        self.pushButtonRemoveConditionS1 = QtWidgets.QPushButton(self.tabStep1)
        self.pushButtonRemoveConditionS1.setGeometry(QtCore.QRect(400, 20, 140, 25))
        self.pushButtonRemoveConditionS1.setObjectName("Remove Condition")
        self.pushButtonRemoveConditionS1.hide()
        self.pushButtonRemoveConditionS1.clicked.connect(lambda: self.removeMultipleConditionForS1())
        self.chooseTypeLayoutS1.addWidget(self.pushButtonRemoveConditionS1)
        
        self.outerLayoutBoxS1.setLayout(self.chooseTypeLayoutS1)

        #DEFINING TABWIDGETMULTIPLECONDITIONS FOR MULTIPLE CONDITIONS IN STEP 1--------------------------------------------------------------------
        self.tabWidgetMultipleConditionsS1 = QtWidgets.QTabWidget(self.tabStep1)
        self.tabWidgetMultipleConditionsS1.setGeometry(QtCore.QRect(20, 70, 530, 330))
        self.tabWidgetMultipleConditionsS1.setObjectName("tabWidgetMultipleConditionsS1")

        #DEFINING FIRST CONDITION AND ADD TO TABWIDGETMULTIPLECONDITIONSS1--------------------------------------------------------------------
        self.tabS1C1 = QtWidgets.QWidget()
        self.tabS1C1.setObjectName("tabS1C1")
        self.tabWidgetMultipleConditionsS1.addTab(self.tabS1C1, "1")

        #DEFINING LAYOUTBOX FOR TABLE AND BUTTONS. LAYOUTBOX IS INSIDE A MULTIPLE CONDITION TAB--------------------------------------------------------------------
        self.layoutBoxS1C1 = QtWidgets.QGroupBox(self.tabS1C1)
        self.layoutBoxS1C1.setGeometry(QtCore.QRect(0, 0, 520, 280))
        self.layoutBoxS1C1.setObjectName("layoutBox")

        #DEFINING SPINBOX AND LABEL FOR GO TO NEXT STEP
        self.labelGoToStepS1C1 = QtWidgets.QLabel()
        self.labelGoToStepS1C1.setObjectName("label_2")

        self.spinBoxS1C1 = QtWidgets.QSpinBox()
        self.spinBoxS1C1.setObjectName("spinBox_2")

        #DEFINING TABLE OBJECT WHICH IS THE TABLE--------------------------------------------------------------------
        self.tableS1C1 = TableWidget()

        #DEFINING ADD AND REMOVE BUTTONS AND LAYOUT---------------------------------------------------------
        self.buttonLayoutS1C1 = QVBoxLayout()
        self.buttonCounterS1C1 = ButtonCounter()

        self.buttonAddRowS1C1 = QPushButton('Add')
        self.buttonAddRowS1C1.clicked.connect(lambda: self.tableS1C1._addRow(self.comboBoxChooseTypeS1.currentText()))
        self.buttonAddRowS1C1.clicked.connect(lambda: self.buttonCounterS1C1.plus())
        self.buttonLayoutS1C1.addWidget(self.buttonAddRowS1C1)

        self.buttonRemoveRowS1C1 = QPushButton('Remove')
        self.buttonRemoveRowS1C1.clicked.connect(self.tableS1C1._removeRow)
        self.buttonRemoveRowS1C1.clicked.connect(lambda: self.buttonCounterS1C1.min())
        self.buttonLayoutS1C1.addWidget(self.buttonRemoveRowS1C1, alignment=Qt.AlignTop)

        self.buttonLayoutS1C1.addWidget(self.labelGoToStepS1C1, alignment=Qt.AlignBottom)
        self.buttonLayoutS1C1.addWidget(self.spinBoxS1C1)

        #LAYOUT FOR THE BUTTONS AND TABLE---------------------------------------------------------
        self.tableWidgetLayoutS1C1 = QHBoxLayout()
        self.layoutBoxS1C1.setLayout(self.tableWidgetLayoutS1C1)
        self.tableWidgetLayoutS1C1.addWidget(self.tableS1C1)
        self.tableWidgetLayoutS1C1.addLayout(self.buttonLayoutS1C1)

        MainWindow.setCentralWidget(self.centralwidget)

        #MAKING MENU BAR----------------------------------------------------------------
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)

        # ----------------------------------------------------------------------
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        # ----------------------------------------------------------------------
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        subWindows = SubWindows()
        self.actionNew.triggered.connect(lambda: subWindows.showNewAdminConfigFile())
        self.actionNew.triggered.connect(lambda: MainWindow.close())

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")

        self.actionSave_as_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_as_2.setObjectName("actionSave_as_2")

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        #----------------------------------------------------------------------
        self.menubar.addAction(self.menuFile.menuAction())

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionSave_as_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showAddRemoveCButtonS1(self, type):
        if type == "Multiple Condition":
            self.pushButtonAddConditionS1.show()
            self.pushButtonRemoveConditionS1.show()
        else:
            self.pushButtonAddConditionS1.hide()
            self.pushButtonRemoveConditionS1.hide()

    def addMultipleConditionForS1(self):
        self.tabS1C2 = QtWidgets.QWidget()
        self.tableS1C2 = TableWidget()

        self.buttonLayoutS1C2 = QVBoxLayout()
        self.buttonCounterS1C2 = ButtonCounter()
        self.tableWidgetLayoutS1C2 = QHBoxLayout()

        self.buttonAddRowS1C2 = QPushButton('Add')
        self.buttonAddRowS1C2.clicked.connect(self.tableS1C2._addRow)

        self.buttonAddRowS1C2.clicked.connect(lambda: self.buttonCounterS1C2.min())
        self.buttonLayoutS1C2.addWidget(self.buttonAddRowS1C2)

        self.buttonRemoveRowS1C2 = QPushButton('Remove')
        self.buttonRemoveRowS1C2.clicked.connect(self.tableS1C2._removeRow)
        self.buttonRemoveRowS1C2.clicked.connect(lambda: self.buttonCounterS1C2.min())
        self.buttonLayoutS1C2.addWidget(self.buttonRemoveRowS1C2, alignment=Qt.AlignTop)

        self.labelGoToStepS1C2 = QtWidgets.QLabel(self.tabS1C2)
        self.labelGoToStepS1C2.setObjectName("label_2")
        self.labelGoToStepS1C2.setText("Go to step:")
        self.buttonLayoutS1C2.addWidget(self.labelGoToStepS1C2, alignment=Qt.AlignBottom)

        self.spinBoxS1C2 = QtWidgets.QSpinBox()
        self.spinBoxS1C2.setObjectName("spinBox_3")
        self.buttonLayoutS1C2.addWidget(self.spinBoxS1C2)

        self.layoutBoxS1C2 = QtWidgets.QGroupBox(self.tabS1C2)
        self.layoutBoxS1C2.setGeometry(QtCore.QRect(0, 0, 520, 280))

        self.layoutBoxS1C2.setLayout(self.tableWidgetLayoutS1C2)
        self.tableWidgetLayoutS1C2.addWidget(self.tableS1C2)
        self.tableWidgetLayoutS1C2.addLayout(self.buttonLayoutS1C2)
        self.tabWidgetMultipleConditionsS1.addTab(self.tabS1C2, str(self.tabWidgetMultipleConditionsS1.count() + 1))

    def removeMultipleConditionForS1(self):
        if self.tabWidgetMultipleConditionsS1.count() != 1:
            self.tabWidgetMultipleConditionsS1.removeTab(self.tabWidgetMultipleConditionsS1.count() - 1)

    def addStep(self):
        #DEFINING OBJECT TO ADD CHOOSETYPE AND MULTIPLE CONDITION IN STEP 2------------------------------------------------------------
        self.addChooseTypeAndMC = AddChooseTypeAndMC()

        #DEFINING THE FIRST SUBTAB OF EVERY STEP (PUTTING TAB IN TABWIDGET)-----------------
        self.addChooseTypeAndMC.tabS2C1 = QtWidgets.QWidget()
        self.addChooseTypeAndMC.tabWidgetMultipleConditionsS2.addTab(self.addChooseTypeAndMC.tabS2C1, "1")

        #DEFINING ALL CONTENT FOR THE FIRST SUBTAB--------------------------------------------
        self.addChooseTypeAndMC.tableS2C1 = TableWidget()

        self.buttonCounterS2C1 = ButtonCounter()
        self.buttonLayoutS2C1 = QVBoxLayout()
        self.tableWidgetLayoutS2C1 = QHBoxLayout()

        self.buttonAddRowS2C1 = QPushButton('Add')
        self.buttonAddRowS2C1.clicked.connect(self.addChooseTypeAndMC.tableS2C1._addRow)
        self.buttonAddRowS2C1.clicked.connect(lambda: self.buttonCounterS2C1.min())
        self.buttonLayoutS2C1.addWidget(self.buttonAddRowS2C1)

        self.buttonRemoveRowS2C1 = QPushButton('Remove')
        self.buttonRemoveRowS2C1.clicked.connect(self.addChooseTypeAndMC.tableS2C1._removeRow)
        self.buttonRemoveRowS2C1.clicked.connect(lambda: self.buttonCounterS2C1.min())
        self.buttonLayoutS2C1.addWidget(self.buttonRemoveRowS2C1, alignment=Qt.AlignTop)

        self.labelGoToStepS2C1 = QtWidgets.QLabel(self.addChooseTypeAndMC.tabS2C1)
        self.labelGoToStepS2C1.setObjectName("label_3")
        self.labelGoToStepS2C1.setText("Go to step:")
        self.buttonLayoutS2C1.addWidget(self.labelGoToStepS2C1, alignment=Qt.AlignBottom)

        self.spinBoxS2C1 = QtWidgets.QSpinBox()
        self.spinBoxS2C1.setObjectName("spinBox_3")
        self.buttonLayoutS2C1.addWidget(self.spinBoxS2C1)

        self.layoutBoxS2C1 = QtWidgets.QGroupBox(self.addChooseTypeAndMC.tabS2C1)
        self.layoutBoxS2C1.setGeometry(QtCore.QRect(0, 0, 520, 280))

        self.layoutBoxS2C1.setLayout(self.tableWidgetLayoutS2C1)
        self.tableWidgetLayoutS2C1.addWidget(self.addChooseTypeAndMC.tableS2C1)
        self.tableWidgetLayoutS2C1.addLayout(self.buttonLayoutS2C1)

        # self.addChooseTypeAndMC.comboBoxChooseTypeS2.activated.connect(lambda: warning_eraseS2())

        #ADDING SUBTAB (A CONDITION) TO THE SUBTABWIDGET
        self.addChooseTypeAndMC.tabWidgetMultipleConditionsS2.addTab(self.addChooseTypeAndMC.tabS2C1, str(self.addChooseTypeAndMC.tabWidgetMultipleConditionsS2.count()))

        #ADDING A TAB (A STEP) TO MAIN TABWIDGET
        self.tabWidgetSteps.addTab(self.addChooseTypeAndMC.tabStep2, str(self.tabWidgetSteps.count() + 1))

        self.addChooseTypeAndMC.comboBoxChooseTypeS2.activated.connect(lambda: warning_eraseS2())

        def warning_eraseS2():
            if self.addChooseTypeAndMC.tableS2C1.rowCount() != 0 or self.addChooseTypeAndMC.tabWidgetMultipleConditionsS2.count() != 1:
                warningErasePopUp = QMessageBox()
                warningErasePopUp.setWindowTitle("Warning")
                warningErasePopUp.setText("Are you sure?")
                warningErasePopUp.setInformativeText("All objects of this step will be deleted")
                warningErasePopUp.setIcon(QMessageBox.Warning)
                warningErasePopUp.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                self.result = warningErasePopUp.exec_()
                if self.result == QMessageBox.Yes:
                    print("everything deleted")
                    self.addChooseTypeAndMC.tableS2C1.removeAllRows()
                    for x in range(self.addChooseTypeAndMC.tabWidgetMultipleConditionsS2.count()):
                        # self.removeMultipleConditionForS2()
                        print("AA")
    def removeStep(self):
        if self.tabWidgetSteps.count() != 1:
            self.tabWidgetSteps.removeTab(self.tabWidgetSteps.count() - 1)

    def warning_erase(self):
        if self.tableS1C1.rowCount() != 0 or self.tabWidgetMultipleConditionsS1.count() != 1:
            warningErasePopUp = QMessageBox()
            warningErasePopUp.setWindowTitle("Warning")
            warningErasePopUp.setText("Are you sure?")
            warningErasePopUp.setInformativeText("All objects of this step will be deleted")
            warningErasePopUp.setIcon(QMessageBox.Warning)
            warningErasePopUp.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            self.result = warningErasePopUp.exec_()
            if self.result == QMessageBox.Yes:
                print("everything deleted")
                self.tableS1C1.removeAllRows()
                for x in range(self.tabWidgetMultipleConditionsS1.count()):
                    self.removeMultipleConditionForS1()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Configuration"))

        self.pushButtonNextStep.setText(_translate("MainWindow", "Next Step"))
        self.pushButtonPreviousStep.setText(_translate("MainWindow", "Previous Step"))
        self.pushButtonFinishConfig.setText(_translate("MainWindow", "Finish Configuration"))
        self.pushButtonRemoveCondition.setText(_translate("MainWindow","Remove Condition"))
        self.pushButtonAddCondition.setText(_translate("MainWindow","Add Condition"))
        self.pushButtonRemoveConditionS1.setText(_translate("MainWindow", "Remove Condition"))
        self.pushButtonAddConditionS1.setText(_translate("MainWindow", "Add Condition"))
        self.pushButtonAddStep.setText(_translate("MainWindow", "Add Step"))
        self.pushButtonRemoveStep.setText(_translate("MainWindow", "Remove Step"))

        self.labelCompanyName.setText(_translate("MainWindow", "Company name: " + self.companyName))
        self.labelStationName.setText(_translate("MainWindow", "Station name: "+ self.stationName))
        self.labelStepNumber.setText(_translate("MainWindow", "Stepnumber:"))
        self.labelChooseTypeS1.setText(_translate("MainWindow", "Choose type:"))
        self.labelGoToStepS1C1.setText(_translate("MainWindow", "Go to step:"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Open"))
        self.actionSave_as.setText(_translate("MainWindow", "Save"))
        self.actionSave_as_2.setText(_translate("MainWindow", "Save as"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()


    ShowWindow().startWindow()


