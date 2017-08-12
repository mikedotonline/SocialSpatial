from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import models.wordlist_model as wordlist_model

import ui.wordgeography as wordgeography

	# --------------------------------
	# class:     	Wordlist_ui
	# description: 	provide functionality to the wordlist dockable gui element
	# params:     	QtGui.DockWidget, a gui element
	# params:		wordlist.ui_wordlist_dockable, the implmentation of the dockable gui element from qt desginer
	# returns:    	none
	# --------------------------------
class WordGeography_ui(QtGui.QDockWidget, wordgeography.Ui_WordGeography_DockWidget):
	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		self.search_pushButton.clicked.connect(self.search)
		self.loadhtml()

	def search(self):
		pass

	def loadhtml(self):
		f=[line.rstrip('\n') for line in open('./data/wordgeography.html')]
		html=''
		for i in f:html+=i 
		print(html)
		self.map_webView.setHtml(html)

		