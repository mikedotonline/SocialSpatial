from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import ui.googleknowledgegraph as googleknowledgegraph
import models.GoogleKnowledgeGraph_model as GoogleKnowledgeGraph_model 


class GoogleKnowledgeGraph_ui(QtGui.QDockWidget, googleknowledgegraph.Ui_GoogleKnowledgGraph_dockable):
	
	procStart = QtCore.pyqtSignal(list)
	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		self.search_pushButton.clicked.connect(self.search)
		self.addtolist_pushButton.clicked.connect(self.addToList)

		self.set_types()


	# --------------------------------
	# method:     	search
	# description: 	search google for graph items 
	# params:     	none
	# returns:    	none
	# --------------------------------
	def search(self):
		#remove old contents
		self.results_listWidget.clear()

		#get parameters from form
		self.type = str(self.types_comboBox.currentText())
		self.limit = self.entries_lineEdit.text()
		self.query = self.searchterm_lineEdit.text()
		self.key_file = './data/k.key' #hardcoded because its not something that changes.

		#perform the search
		self.gkg = GoogleKnowledgeGraph_model.GoogleKnowledgeGraph(self.key_file,self.query,self.limit,self.type)

		#check to see if the search produced results.
		if len(self.gkg.items) == 0:
			self.results_listWidget.addItem(QString("nothing found: try again"))
		else:
			for i in self.gkg.items:self.results_listWidget.addItem(QString(i))

	# --------------------------------
	# method:     	addToList
	# description: 	get all of the currently selected items, and send them off to the main window as a slot
	# property:		procStart, the list data to add to the wordlist
	# params:     	none
	# returns:    	none
	# --------------------------------	
	@QtCore.pyqtSlot()
	def addToList(self):
		sel = []
		for i in self.results_listWidget.selectedItems():sel.append(i.text())

		self.procStart.emit(sel)

	# --------------------------------
	# method:     	set_types
	# description: 	using validated 'types' listed on schema.org and checked against google, populate the combolox
	# params:     	none
	# returns:    	none
	# --------------------------------
	def set_types(self):		
		lines = [line.rstrip('\n') for line in open('./data/validtypes.txt')] #constant.
		self.types_comboBox.addItems(lines)

