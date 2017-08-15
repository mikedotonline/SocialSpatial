from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import models.wordlist_model as wordlist_model
import ui.wordlist as wordlist

	# --------------------------------
	# class:     	Wordlist_ui
	# description: 	provide functionality to the wordlist dockable gui element
	# params:     	QtGui.DockWidget, a gui element
	# params:		wordlist.ui_wordlist_dockable, the implmentation of the dockable gui element from qt desginer
	# returns:    	none
	# --------------------------------
class Wordlist_ui(QtGui.QDockWidget, wordlist.Ui_wordlist_dockable):
	
	#signal of the selected words
	selectedWords = QtCore.pyqtSignal(list)
	
	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		


		self.wordlistload_pushButton.clicked.connect(self.load_wordlist)
		self.wordlistsave_pushButton.clicked.connect(self.save_wordlist)
		self.AddNew_pushButton.clicked.connect(self.add_word)
		self.removewords_pushButton.clicked.connect(self.remove_words)
		self.wl = wordlist_model.Wordlist()	

		self.wordlist_tableWidget.itemSelectionChanged.connect(self.send_list)

	# --------------------------------
	# method:     	load_wordlist
	# description: 	get the contents of the wordlist dictionary and print it into the QTableWidget
	# params:     	none
	# returns:    	none
	# --------------------------------
	def load_wordlist(self):
		self.wordlist_tableWidget.setRowCount(0)
		self.wordlist_tableWidget.setColumnCount(0)


		self.wl.json_load(self.wordlistfile_lineEdit.text())
		self.wordlist_tableWidget.setRowCount(len(self.wl.words))
		self.wordlist_tableWidget.setColumnCount(self.wl.len_tags()+1) #we add one because the word itself needs a column

		#set the column headers
		hdrs = QStringList()
		hdrs.append(QString("Word"))
		for i in range(1,self.wl.len_tags()+1):
			hdrs.append(QString("tag"+str(i)))

		self.wordlist_tableWidget.setHorizontalHeaderLabels(hdrs)

		row=0
		for key in self.wl.words.keys():
			# print 'new row:'+key
			newitem = QTableWidgetItem(key)
			self.wordlist_tableWidget.setItem(row,0,newitem)
			col=1
			for v in self.wl.words[key]:
				#print "\t adding value: "+v
				newitem = QTableWidgetItem(v)
				self.wordlist_tableWidget.setItem(row,col,newitem)
				col+=1
			row+=1
		print 'table rows:'+str(self.wordlist_tableWidget.rowCount())

	# --------------------------------
	# method:     	save_wordlist
	# description: 	saves the current wordlist to a json file
	# params:     	none
	# returns:    	none
	# --------------------------------
	def save_wordlist(self):
		self.wl.json_write(self.wordlistfile_lineEdit.text())

	# --------------------------------
	# method:     	add_word
	# description: 	use the word and tags (comma seperated) in the new word form to add a new word to the wordlist
	# params:     	none
	# returns:    	none
	# --------------------------------
	def add_word(self):
		self.wordlist_tableWidget.setRowCount(self.wordlist_tableWidget.rowCount()+1)
		newitem = QTableWidgetItem(self.NewWord_lineEdit.text())
		self.wordlist_tableWidget.setItem(self.wordlist_tableWidget.rowCount()-1,0,newitem)
		tags = self.NewTags_lineEdit.text().split(",")
		col=1
		if len(tags) > self.wordlist_tableWidget.columnCount()-1:
				self.wordlist_tableWidget.setColumnCount(len(tags)+1)
		for t in tags:			
			newitem = QTableWidgetItem(t)			
			self.wordlist_tableWidget.setItem(self.wordlist_tableWidget.rowCount()-1,col,newitem)
			col+=1
		print 'table rows:'+str(self.wordlist_tableWidget.rowCount())

		#add the word to the wl data model
		l = []
		for t in tags:
			l.append(str(t))
		self.wl.words[str(self.NewWord_lineEdit.text())]=l
		#print self.wl.words

	# --------------------------------
	# method:     	remove_word
	# description: 	delete selected word (and associated tags) from the wordlist
	# params:     	none
	# returns:    	none
	# --------------------------------
	def remove_words(self):
		l=[]
		for i in self.wordlist_tableWidget.selectedIndexes():
			#print i.row()
			l.append(i.row())
		l=list(set(l))
		l.sort()
		
		#remove in reverse order to preserve the table indexes
		for i in l[::-1]:			
			#print "popping: "+str(self.wordlist_tableWidget.item(i,0).text())
			self.wl.words.pop(str(self.wordlist_tableWidget.item(i,0).text()))		# update the worldlist data model
			self.wordlist_tableWidget.removeRow(i)
		#print self.wl.words

	@QtCore.pyqtSlot(list)
	def on_procStart(self, message):
		print(message)
		self.add_word(message)


		self.raise_()

	#add_words overload for adding in 
	def add_word(self,in_list):
		for i in in_list:
			self.wordlist_tableWidget.setRowCount(self.wordlist_tableWidget.rowCount()+1)
			newitem = QTableWidgetItem(i)
			self.wordlist_tableWidget.setItem(self.wordlist_tableWidget.rowCount()-1,0,newitem)
			self.wl.words[str(i)]=['']
	
	@QtCore.pyqtSlot()
	def send_list(self):
		row=[]
		for i in self.wordlist_tableWidget.selectedIndexes():
			row.append(i.row())
		row=list(set(row))
		wrds=[]
		for i in row:
			wrds.append(str(self.wordlist_tableWidget.item(i,0).text()))
		#print wrds 
		self.selectedWords.emit(wrds)