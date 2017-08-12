from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import ui.wordnet as wordnet
import models.WordNet_model as Wordnet_model 


class Wordnet_ui(QtGui.QDockWidget, wordnet.Ui_wordnet_dockable):
	
	procStart = QtCore.pyqtSignal(list)

	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		self.search_pushButton.clicked.connect(self.search)
		self.addtolist_pushButton.clicked.connect(self.addToList)
		
		

	def search(self):
		
		#clear current contents
		self.synonyms_listWidget.clear()
		self.hyponyms_listWidget.clear()
		self.hypernyms_listWidget.clear()

		self.wn = Wordnet_model.WordNet(str(self.search_lineEdit.text()))

		for i in self.wn.synonyms:self.synonyms_listWidget.addItem(QString(i))
		for i in self.wn.hypernyms:self.hypernyms_listWidget.addItem(QString(i))
		for i in self.wn.hyponyms:self.hyponyms_listWidget.addItem(QString(i))

	@QtCore.pyqtSlot()
	def addToList(self):
		sel = []
		for i in self.synonyms_listWidget.selectedItems():	sel.append(i.text())
		for i in self.hypernyms_listWidget.selectedItems():	sel.append(i.text())
		for i in self.hyponyms_listWidget.selectedItems(): sel.append(i.text())
		#print sel
		self.procStart.emit(sel)

		#now, how do I transfer the items from this class to the next....
		# https://stackoverflow.com/questions/14090353/sending-messages-between-two-widgets-using-signals-and-slots
		