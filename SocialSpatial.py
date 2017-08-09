from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import ui.mainwindow
#import ui.dbconn as dbconn
#import ui.wordnet as wordnet
#import ui.wordlist as wordlist
#import models.databaseConnection_model as db_model
import models.GoogleKnowledgeGraph
#import models.WordNet
import viewmodels.DBConn as dbconn
import viewmodels.wordnet as wordnet
import viewmodels.wordlist as wordlist


class SocialSpatialApp(QtGui.QMainWindow, ui.mainwindow.Ui_MainWindow):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		self.dbconn_dock = dbconn.DBConn_ui()
		self.addDockWidget(Qt.LeftDockWidgetArea,self.dbconn_dock)

		self.wordnet_dock = wordnet.Wordnet_ui()
		self.addDockWidget(Qt.RightDockWidgetArea,self.wordnet_dock)
		self.wordnet_dock.hide()

		self.wordlist_dock = wordlist.Wordlist_ui()
		self.addDockWidget(Qt.RightDockWidgetArea,self.wordlist_dock)

		self.actionDatabase_Connection.activated.connect(self.showhide_dbconn)
		self.actionWordnet.activated.connect(self.showhide_wordnet)
		self.actionWord_List.activated.connect(self.showhide_wordlist)
		self.dbconn_visible = True
		self.wordlist_visible = True
		self.wordnet_visible=False

	def showhide_dbconn(self):
		if self.dbconn_visible==True:
			self.dbconn_dock.hide()
			self.dbconn_visible=False
		else:
			self.dbconn_dock.show()
			self.dbconn_visible=True
	
	def showhide_wordlist(self):
		if self.wordlist_visible==True:
			self.wordlist_dock.hide()
			self.wordlist_visible=False
		else:
			self.wordlist_dock.show()
			self.wordlist_visible=True

	def showhide_wordnet(self):
		if self.wordnet_visible==True:
			self.wordnet_dock.hide()
			self.wordnet_visible=False
		else:
			self.wordnet_dock.show()
			self.wordnet_visible=True


def main():
	app = QtGui.QApplication(sys.argv)
	form = SocialSpatialApp()
	form.show()    
	
	app.exec_()


if __name__ == '__main__':
	main()