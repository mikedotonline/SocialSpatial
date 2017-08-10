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
	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		self.wordlistload_pushButton.clicked.connect(self.load_wordlist)
		self.wordlistsave_pushButton.clicked.connect(self.save_wordlist)
		self.AddNew_pushButton.clicked.connect(self.add_word)
		self.removewords_pushButton.clicked.connect(self.remove_words)
		self.wl = wordlist_model.Wordlist()	

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
		row=0
		for key in self.wl.words.keys():
			print 'new row:'+key
			newitem = QTableWidgetItem(key)
			self.wordlist_tableWidget.setItem(row,0,newitem)
			col=1
			for v in self.wl.words[key]:
				print "\t adding value: "+v
				newitem = QTableWidgetItem(v)
				self.wordlist_tableWidget.setItem(row,col,newitem)
				col+=1
			row+=1
		print 'table rows:'+str(self.wordlist_tableWidget.rowCount())

	def save_wordlist(self):
		pass

	# --------------------------------
	# method:     	add_word
	# description: 	use the word and tags (comma seperated) in the new word form to add a new word to the wordlist
	# params:     	none
	# returns:    	none
	# to_do: 		sync with the self.wl data model
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

	# --------------------------------
	# method:     	remove_word
	# description: 	delete selected word (and associated tags) from the wordlist
	# params:     	none
	# returns:    	none
	# to_do: sync 	with the self.wl data model
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
			#print "removing"+str(i)
			self.wordlist_tableWidget.removeRow(i)


