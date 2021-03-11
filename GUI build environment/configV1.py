# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Config.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class StartWindow(object):
    def setupStartWindow(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow")
        MainWindow2.resize(537, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButtonNextStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNextStep.setGeometry(QtCore.QRect(390, 320, 101, 31))
        self.pushButtonNextStep.setObjectName("Next Step")

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "AA"))

        self.pushButtonNextStep.setText(_translate("MainWindow2", "Next Step"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButtonNextStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNextStep.setGeometry(QtCore.QRect(390, 320, 101, 31))
        self.pushButtonNextStep.setObjectName("Next Step")

        self.pushButtonPreviousStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPreviousStep.setGeometry(QtCore.QRect(10, 320, 111, 31))
        self.pushButtonPreviousStep.setObjectName("Previous Step")

        self.pushButtonFinishConfig = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFinishConfig.setGeometry(QtCore.QRect(180, 320, 151, 31))
        self.pushButtonFinishConfig.setObjectName("Finish configuration")

        self.pushButtonAddOutput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddOutput.setGeometry(QtCore.QRect(10, 90, 89, 25))
        self.pushButtonAddOutput.setObjectName("Add output")

        self.pushButtonCondition = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCondition.setGeometry(QtCore.QRect(10, 90, 89, 25))
        self.pushButtonCondition.setObjectName("Add input condition")

        self.pushButtonMultipleCondition = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMultipleCondition.setGeometry(QtCore.QRect(10, 90, 89, 25))
        self.pushButtonMultipleCondition.setObjectName("Add input multiple condition")

        self.labelStepNumber = QtWidgets.QLabel(self.centralwidget)
        self.labelStepNumber.setGeometry(QtCore.QRect(220, 10, 51, 31))
        self.labelStepNumber.setObjectName("label")

        self.labelChooseType = QtWidgets.QLabel(self.centralwidget)
        self.labelChooseType.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.labelChooseType.setObjectName("label_2")

        self.labelGoToStep = QtWidgets.QLabel(self.centralwidget)
        self.labelGoToStep.setGeometry(QtCore.QRect(10, 270, 81, 21))
        self.labelGoToStep.setObjectName("label_3")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 50, 111, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Set Output")
        self.comboBox.addItem("Condition")
        self.comboBox.addItem("Multiple Condition")

        self.pushButtonMultipleCondition.hide()
        self.pushButtonCondition.hide()
        self.pushButtonAddOutput.show()

        self.comboBox.activated.connect(self.detect)

        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(100, 270, 48, 26))
        self.spinBox_2.setObjectName("spinBox_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def detect(self):
        if self.comboBox.currentIndex() == 0:
            self.pushButtonAddOutput.show()
            self.pushButtonCondition.hide()
            self.pushButtonMultipleCondition.hide()
        elif self.comboBox.currentIndex() == 1:
            self.pushButtonAddOutput.hide()
            self.pushButtonCondition.show()
            self.pushButtonMultipleCondition.hide()
        elif self.comboBox.currentIndex() == 2:
            self.pushButtonAddOutput.hide()
            self.pushButtonCondition.hide()
            self.pushButtonMultipleCondition.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Configuration"))

        self.pushButtonNextStep.setText(_translate("MainWindow", "Next Step"))
        self.pushButtonPreviousStep.setText(_translate("MainWindow", "Previous Step"))
        self.pushButtonFinishConfig.setText(_translate("MainWindow", "Finish Configuration"))

        self.pushButtonAddOutput.setText(_translate("MainWindow", "Add Output"))
        self.pushButtonCondition.setText(_translate("MainWindow", "Add Input"))
        self.pushButtonMultipleCondition.setText(_translate("MainWindow", "Add Input"))

        self.labelStepNumber.setText(_translate("MainWindow", "Step 1:"))
        self.labelChooseType.setText(_translate("MainWindow", "Choose type:"))
        self.labelGoToStep.setText(_translate("MainWindow", "Go to step:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # MainWindow2 = QtWidgets.QMainWindow()
    # ui = StartWindow()
    # ui.setupStartWindow(MainWindow2)
    # MainWindow2.show()

    sys.exit(app.exec_())


