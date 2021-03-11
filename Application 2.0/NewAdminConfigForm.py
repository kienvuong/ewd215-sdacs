# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWidgetTest.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from databaseEWD import Pool
import AdminConfig
import sys

class Windows:
    def showAdminConfig(self, companyData, companyName, stationName):
        self.window = QtWidgets.QMainWindow()
        self.ui = AdminConfig.AdminConfig_UI(companyData, companyName, stationName)
        self.ui.setupUi(self.window)
        self.window.move(100, 130)
        self.window.show()

class CreateNewAdminConfigFile(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(295, 369)

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(110, 60, 160, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItems(Pool().selectAllCompanies())
        self.comboBox.activated.connect(lambda: self.showCompanyInLineEdit((self.comboBox.currentText())))

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 130, 113, 25))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 190, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 250, 113, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 130, 111, 31))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 61, 21))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 121, 31))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.label_4.setObjectName("label_4")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.submitConfig(Form))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def submitConfig(self, Form):
        self.windows = Windows()

        if self.lineEdit.text() != "" and self.lineEdit_2.text() != "" and self.lineEdit_3.text() != "":
            self.companyName = self.lineEdit.text()
            self.companyLocation = self.lineEdit_2.text()
            self.stationName = self.lineEdit_3.text()

            if self.comboBox.currentIndex() == 0:
                id = Pool().insertCompany(self.companyName, self.companyLocation)
                Pool().insertStation(id, self.stationName)
            elif Pool().checkIfCompanyExist(self.companyName, self.companyLocation) == True:
                id = Pool().selectCompanyId(self.companyName, self.companyLocation)
                Pool().insertStation(id, self.stationName)
            self.companyData = self.companyName + ", " + self.stationName
            self.windows.showAdminConfig(self.companyData, self.companyName, self.stationName)
            Form.destroy()
        else:
            print("You must fill in all fields")

    def showCompanyInLineEdit(self, value):
        if value != "Add new Company:":
            a = Pool().selectCompanyAndLocation(value)
            self.lineEdit.setText(a[0])
            self.lineEdit_2.setText(a[1])
        else:
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "New Configuration"))
        self.label.setText(_translate("Form", "Company name"))
        self.label_2.setText(_translate("Form", "Location"))
        self.label_3.setText(_translate("Form", "Name of station"))
        self.comboBox.setItemText(0, _translate("Form", "Add new Company:"))
        self.label_4.setText(_translate("Form", "Find the company or add new one:"))
        self.pushButton.setText(_translate("Form", "Start configuration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = CreateNewAdminConfigFile()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



