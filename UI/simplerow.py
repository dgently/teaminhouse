# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/peter/projects/inhousekeeper/UI/simplerow.ui'
#
# Created: Mon Jul 13 14:53:55 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui




class UI_SimpleRow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(594, 30)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)

        Form.setMinimumSize(QtCore.QSize(0, 30))
        Form.setMaximumSize(QtCore.QSize(16777215, 35))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(3, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.status_box = QtGui.QComboBox(Form)
        self.status_box.setObjectName("status_box")
        self.horizontalLayout_2.addWidget(self.status_box)
        self.type_box = QtGui.QComboBox(Form)
        self.type_box.setObjectName("type_box")
        self.horizontalLayout_2.addWidget(self.type_box)
        self.artist_box = QtGui.QComboBox(Form)
        self.artist_box.setObjectName("artist_box")
        self.horizontalLayout_2.addWidget(self.artist_box)
        self.notes_edit = QtGui.QTextEdit(Form)
        self.notes_edit.setObjectName("notes_edit")
        self.notes_edit.setMaximumSize(3000,30)
        self.horizontalLayout_2.addWidget(self.notes_edit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.type_box, self.status_box)
        Form.setTabOrder(self.status_box, self.notes_edit)

    




    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "SH07_1235", None, QtGui.QApplication.UnicodeUTF8))



class SimpleRow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SimpleRow, self).__init__(parent)
        self.ui = UI_SimpleRow()
        self.ui.setupUi(self)
        self.ui.artist_box.installEventFilter(self)
        self.ui.type_box.installEventFilter(self)
        
        self.ui.status_box.installEventFilter(self)
        



    def eventFilter(self,object,event):
        
        if event.type()== QtCore.QEvent.Type.Wheel:
            return True
        else:
            return QtGui.QWidget.eventFilter(self,object,event)
        
        
 
if __name__ == "__main__":
 app = QtGui.QApplication(sys.argv)
 mySW = SimpleRow()
 mySW.show()
 sys.exit(app.exec_())
