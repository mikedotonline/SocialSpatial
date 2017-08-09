from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import models.databaseConnection_model as db_model
import ui.wordlist as wordlist

class Wordlist_ui(QtGui.QDockWidget, wordlist.Ui_wordlist_dockable):
	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
	def foo(self):
		pass