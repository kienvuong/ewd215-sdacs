import NewAdminConfigForm
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class MyWidget(QtWidgets.QWidget, NewAdminConfigForm.CreateNewAdminConfigFile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def closeEvent(self, event):
        event.accept()
        NewAdminConfigForm.Windows().showAdminConfig("", "", "")
        self.close()




