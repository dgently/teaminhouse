# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/peter/projects/inhousekeeper/UI/simplerow.ui'
#
# Created: Fri Jul 17 08:24:29 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(594, 30)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 30))
        Form.setMaximumSize(QtCore.QSize(16777215, 36))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(3, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.shot_label = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shot_label.sizePolicy().hasHeightForWidth())
        self.shot_label.setSizePolicy(sizePolicy)
        self.shot_label.setMinimumSize(QtCore.QSize(90, 0))
        self.shot_label.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.shot_label.setFont(font)
        self.shot_label.setObjectName("shot_label")
        self.horizontalLayout_2.addWidget(self.shot_label)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.version_label = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.version_label.sizePolicy().hasHeightForWidth())
        self.version_label.setSizePolicy(sizePolicy)
        self.version_label.setMinimumSize(QtCore.QSize(30, 0))
        self.version_label.setObjectName("version_label")
        self.horizontalLayout_2.addWidget(self.version_label)
        self.status_box = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_box.sizePolicy().hasHeightForWidth())
        self.status_box.setSizePolicy(sizePolicy)
        self.status_box.setMinimumSize(QtCore.QSize(100, 0))
        self.status_box.setMaximumSize(QtCore.QSize(120, 16777215))
        self.status_box.setObjectName("status_box")
        self.horizontalLayout_2.addWidget(self.status_box)
        self.type_box = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_box.sizePolicy().hasHeightForWidth())
        self.type_box.setSizePolicy(sizePolicy)
        self.type_box.setMinimumSize(QtCore.QSize(75, 0))
        self.type_box.setMaximumSize(QtCore.QSize(120, 16777215))
        self.type_box.setObjectName("type_box")
        self.horizontalLayout_2.addWidget(self.type_box)
        self.artist_box = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.artist_box.sizePolicy().hasHeightForWidth())
        self.artist_box.setSizePolicy(sizePolicy)
        self.artist_box.setMinimumSize(QtCore.QSize(75, 0))
        self.artist_box.setObjectName("artist_box")
        self.horizontalLayout_2.addWidget(self.artist_box)
        self.notes_edit = QtGui.QTextEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.notes_edit.sizePolicy().hasHeightForWidth())
        self.notes_edit.setSizePolicy(sizePolicy)
        self.notes_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.notes_edit.setAcceptDrops(False)
        self.notes_edit.setReadOnly(True)
        self.notes_edit.setObjectName("notes_edit")
        self.horizontalLayout_2.addWidget(self.notes_edit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.type_box, self.status_box)
        Form.setTabOrder(self.status_box, self.notes_edit)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_label.setText(QtGui.QApplication.translate("Form", "SH075_1235", None, QtGui.QApplication.UnicodeUTF8))
        self.version_label.setText(QtGui.QApplication.translate("Form", "v001", None, QtGui.QApplication.UnicodeUTF8))

