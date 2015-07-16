from PySide.QtCore import *
from PySide.QtGui import *

import sys

import UI
import controller as c




class SimpleRow(QWidget):
    def __init__(self, parent=None):
        super(SimpleRow, self).__init__(parent)
        self.ui = UI.simplerow.Ui_Form()
        self.ui.setupUi(self)
        self.ui.artist_box.installEventFilter(self)
        self.ui.type_box.installEventFilter(self)
        self.ui.status_box.installEventFilter(self)
        



    def eventFilter(self,object,event):
        
        if event.type()== QEvent.Type.Wheel:
            return True
        else:
            return QWidget.eventFilter(self,object,event)




class SimpleShotList(QWidget):
	def __init__(self, parent=None):
		super(SimpleShotList, self).__init__(parent)
		self.ui = UI.shotlist.Ui_Form()
		self.ui.setupUi(self)

		self.populateFilters()
		self.populateTable()
		self.ui.refresh_button.clicked.connect(self.refreshFilter)

	def refreshFilter(self):
		fA=self.ui.artist_search.currentText()
		fS=self.ui.status_search.currentText()
		fT=self.ui.type_search.currentText()
		self.populateTable(fA,fS,fT)

	def populateFilters(self):
		self.ui.status_search.addItem('ALL')
		self.ui.type_search.addItem('ALL')
		self.ui.artist_search.addItem('ALL')
		c.populate_status(self.ui.status_search)
		c.populate_types(self.ui.type_search)
		c.populate_artists(self.ui.artist_search)
		self.ui.artist_search.currentIndexChanged.connect(self.refreshFilter)
		self.ui.status_search.currentIndexChanged.connect(self.refreshFilter)
		self.ui.type_search.currentIndexChanged.connect(self.refreshFilter)

	def modifiedRow(self):
		field=self.sender().objectName()
		shot=self.sender().parent().ui.shot_label.text()
		value = self.sender().currentText()

		c.update_shot_attribute(shot,field,value)

	def populateTable(self,filterA= 'ALL',filterS='ALL',filterT='ALL'):
		self.ui.shotsQListWidget.clear()
		for a in c.get_shots_simple_row(filterA,filterS,filterT):
			rowWidget=SimpleRow()
			rowWidget.ui.shot_label.setText(a.name)
			c.populate_artists(rowWidget.ui.artist_box)
			c.populate_status(rowWidget.ui.status_box)
			c.populate_types(rowWidget.ui.type_box)
			
			index=rowWidget.ui.artist_box.findText(a.currentArtist.first)
			rowWidget.ui.artist_box.setCurrentIndex(index)

			index=rowWidget.ui.status_box.findText(a.status.status)
			rowWidget.ui.status_box.setCurrentIndex(index)

			index=rowWidget.ui.type_box.findText(a.shotType.shotType)
			rowWidget.ui.type_box.setCurrentIndex(index)
			
			rowWidget.ui.notes_edit.setText(c.get_current_submission_note(a))

			rowWidget.ui.version_label.setText(c.get_current_submission_version(a))

			rowWidget.ui.artist_box.currentIndexChanged.connect(self.modifiedRow)
			rowWidget.ui.status_box.currentIndexChanged.connect(self.modifiedRow)
			rowWidget.ui.type_box.currentIndexChanged.connect(self.modifiedRow)
			

			listWidgetItem=QListWidgetItem(self.ui.shotsQListWidget)
			listWidgetItem.setSizeHint(rowWidget.sizeHint())
			self.ui.shotsQListWidget.addItem(listWidgetItem)
			self.ui.shotsQListWidget.setItemWidget(listWidgetItem,rowWidget)
			

			
if __name__ == '__main__':
	qt_app = QApplication(sys.argv)
	view =SimpleShotList()
	view.show()

	qt_app.exec_()
else:
	from nukescripts import panels

	panels.registerWidgetAsPanel('inhousekeeper.views.SimpleShotList','inHouseKeeper','uk.co.thefoundry.inHouseWindow')
