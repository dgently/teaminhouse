# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/peter/projects/inhousekeeper/UI/shotlist.ui'
#
# Created: Wed Jul 15 19:39:06 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
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
        self.refresh_button = QtGui.QToolButton(Form)
        self.refresh_button.setObjectName("refresh_button")
        self.horizontalLayout.addWidget(self.refresh_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.shotsQListWidget = QtGui.QListWidget(Form)
        self.shotsQListWidget.setAlternatingRowColors(True)
        self.shotsQListWidget.setViewMode(QtGui.QListView.ListMode)
        self.shotsQListWidget.setObjectName("shotsQListWidget")
        self.verticalLayout.addWidget(self.shotsQListWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "IHkeeper", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_button.setText(QtGui.QApplication.translate("Form", "R", None, QtGui.QApplication.UnicodeUTF8))

