# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/peter/projects/inhousekeeper/UI/shotlist.ui'
#
# Created: Mon Jul 13 15:02:29 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class UI_ShotList(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.status_search = QtGui.QComboBox(Form)
        self.status_search.setObjectName("status_search")
        self.horizontalLayout.addWidget(self.status_search)
        self.type_search = QtGui.QComboBox(Form)
        self.type_search.setObjectName("type_search")
        self.horizontalLayout.addWidget(self.type_search)
        self.artist_search = QtGui.QComboBox(Form)
        self.artist_search.setObjectName("artist_search")
        self.horizontalLayout.addWidget(self.artist_search)
        self.verticalLayout.addLayout(self.horizontalLayout)
        #self.listView = QtGui.QListView(Form)
        #self.listView.setObjectName("listView")
        #self.verticalLayout.addWidget(self.listView)

        self.shotsQListWidget = QtGui.QListWidget(Form)
        self.verticalLayout.addWidget(self.shotsQListWidget)
        




        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "IHkeeper", None, QtGui.QApplication.UnicodeUTF8))




class ShotList(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ShotList, self).__init__(parent)
        self.ui = UI_ShotList()
        self.ui.setupUi(self)
 
if __name__ == "__main__":
 app = QtGui.QApplication(sys.argv)
 mySW = ShotList()
 mySW.show()
 sys.exit(app.exec_())