from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import ui.wordnet as wordnet


class Wordnet_ui(QtGui.QDockWidget, wordnet.Ui_wordnet_dockable):
	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
	def foo(self):
		pass