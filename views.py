from PySide.QtCore import *
from PySide.QtGui import *

import sys

import UI
import controller as c

qt_app = QApplication(sys.argv)
class SimpleView():

	def __init__(self):

		self.shotlist = UI.shotlist.ShotList()

		self.populateFilters()
		self.populateTable()

	def refreshFilter(self):
		fA=self.shotlist.ui.artist_search.currentText()
		fS=self.shotlist.ui.status_search.currentText()
		fT=self.shotlist.ui.type_search.currentText()
		self.populateTable(fA,fS,fT)

	def populateFilters(self):
		self.shotlist.ui.status_search.addItem('ALL')
		self.shotlist.ui.type_search.addItem('ALL')
		self.shotlist.ui.artist_search.addItem('ALL')
		c.populate_status(self.shotlist.ui.status_search)
		c.populate_types(self.shotlist.ui.type_search)
		c.populate_artists(self.shotlist.ui.artist_search)
		self.shotlist.ui.artist_search.currentIndexChanged.connect(self.refreshFilter)
		self.shotlist.ui.status_search.currentIndexChanged.connect(self.refreshFilter)
		self.shotlist.ui.type_search.currentIndexChanged.connect(self.refreshFilter)

	def modifiedRow(self):
		print self.shotlist.sender()

	def populateTable(self,filterA= 'ALL',filterS='ALL',filterT='ALL'):
		self.shotlist.ui.shotsQListWidget.clear()
		for a in c.get_shots_simple_row(filterA,filterS,filterT):
			rowWidget=UI.simplerow.SimpleRow()
			rowWidget.ui.label.setText(a.name)
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

			rowWidget.ui.artist_box.currentIndexChanged.connect(self.modifiedRow)
			rowWidget.ui.status_box.currentIndexChanged.connect(self.modifiedRow)
			rowWidget.ui.type_box.currentIndexChanged.connect(self.modifiedRow)
			rowWidget.ui.notes_edit.textChanged.connect(self.modifiedRow)

			listWidgetItem=QListWidgetItem(self.shotlist.ui.shotsQListWidget)
			listWidgetItem.setSizeHint(rowWidget.sizeHint())
			self.shotlist.ui.shotsQListWidget.addItem(listWidgetItem)
			self.shotlist.ui.shotsQListWidget.setItemWidget(listWidgetItem,rowWidget)
			
			

view =SimpleView()
view.shotlist.show()

qt_app.exec_()

