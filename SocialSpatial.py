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
#import models.GoogleKnowledgeGraph
#import models.WordNet
import viewmodels.DBConn as dbconn
import viewmodels.wordnet as wordnet
import viewmodels.wordlist as wordlist
import viewmodels.googleknowledgegraph as googleknowledgegraph
import viewmodels.wordgeography as wordgeography
import viewmodels.postsamples as postsamples


class SocialSpatialApp(QtGui.QMainWindow, ui.mainwindow.Ui_MainWindow):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		
		#database connection dock
		self.dbconn_dock = dbconn.DBConn_ui()
		self.addDockWidget(Qt.LeftDockWidgetArea,self.dbconn_dock)
		self.dbconn_dock.visibilityChanged.connect(self.showhide_dbconn)

		#wordlist dock
		self.wordlist_dock = wordlist.Wordlist_ui()
		self.addDockWidget(Qt.RightDockWidgetArea,self.wordlist_dock)
		self.wordlist_dock.visibilityChanged.connect(self.showhide_wordlist)

		#wordnet dock tool
		self.wordnet_dock = wordnet.Wordnet_ui()
		self.addDockWidget(Qt.RightDockWidgetArea,self.wordnet_dock)
		self.wordnet_dock.hide()
		self.wordnet_dock.visibilityChanged.connect(self.showhide_wordnet)
		
		#googleknowedgegraph dock tool
		self.googleknowledgegraph_dock = googleknowledgegraph.GoogleKnowledgeGraph_ui()
		self.addDockWidget(Qt.RightDockWidgetArea,self.googleknowledgegraph_dock)
		self.googleknowledgegraph_dock.hide()
		self.googleknowledgegraph_dock.visibilityChanged.connect(self.showhide_googleknowledgegraph)

		#wordgeography dock tool
		self.wordgeography_dock = wordgeography.WordGeography_ui(self.wordlist_dock)
		self.addDockWidget(Qt.RightDockWidgetArea,self.wordgeography_dock)
		self.wordgeography_dock.hide()
		self.wordgeography_dock.visibilityChanged.connect(self.showhide_wordgeography)

		#post samples dock tool
		self.postsamples_dock = postsamples.PostSamples_ui(self.wordlist_dock)
		self.addDockWidget(Qt.RightDockWidgetArea,self.postsamples_dock)
		self.postsamples_dock.hide()
		self.postsamples_dock.visibilityChanged.connect(self.showhide_postsamples)

		#menu item control
		self.actionDatabase_Connection.activated.connect(self.showhide_dbconn)
		self.actionWordnet.activated.connect(self.showhide_wordnet)
		self.actionGoogle_Knowledge_Graph.activated.connect(self.showhide_googleknowledgegraph)
		self.actionWord_List.activated.connect(self.showhide_wordlist)
		self.actionWord_Map.activated.connect(self.showhide_wordgeography)
		self.actionPost_Samples.activated.connect(self.showhide_postsamples)
		
		#set initial visibility or each dock item
		self.dbconn_visible = False
		self.wordlist_visible = False
		self.wordnet_visible = False
		self.googleknowledgegraph_visible = False
		self.wordgeography_visible = False
		self.postsamples_visible = False

		#create the signal connection
		self.wordnet_dock.procStart.connect(self.wordlist_dock.on_procStart)
		self.googleknowledgegraph_dock.procStart.connect(self.wordlist_dock.on_procStart)
		self.wordlist_dock.selectedWords.connect(self.wordgeography_dock.on_selectedWords)
		self.dbconn_dock.connection.connect(self.wordgeography_dock.on_connection)
		self.wordlist_dock.selectedWords.connect(self.postsamples_dock.on_selectedWords)
		self.dbconn_dock.connection.connect(self.postsamples_dock.on_connection)
		self.wordgeography_dock.spatialExtent.connect(self.postsamples_dock.on_extent)
	def showhide_dbconn(self):
		if self.dbconn_visible==True:
			self.dbconn_dock.hide()
			self.dbconn_visible=False
		else:
			self.dbconn_dock.show()
			self.dbconn_visible=True
	
	@QtCore.pyqtSlot()
	def showhide_wordlist(self):
		if self.wordlist_visible==True:
			self.wordlist_dock.hide()
			self.wordlist_visible=False
		else:
			self.wordlist_dock.show()
			self.wordlist_visible=True
			self.wordlist.raise_()
			self.googleknowledgegraph.raise_()

	
	def showhide_wordnet(self):
		if self.wordnet_visible==True:
			self.wordnet_dock.hide()
			self.wordnet_visible=False
		else:
			self.wordnet_dock.show()
			self.wordnet_visible=True

	def showhide_googleknowledgegraph(self):
		if self.googleknowledgegraph_visible==True:
			self.googleknowledgegraph_dock.hide()
			self.googleknowledgegraph_visible=False
		else:
			self.googleknowledgegraph_dock.show()
			self.googleknowledgegraph_visible=True

	@QtCore.pyqtSlot()
	def showhide_wordgeography(self):
		if self.wordgeography_visible==True:
			self.wordgeography_dock.hide()
			self.wordgeography_visible=False
		else:
			self.wordgeography_dock.show()
			self.wordgeography_visible=True
			self.wordgeography_dock.raise_()

	def showhide_postsamples(self):
		if self.postsamples_visible==True:
			self.postsamples_dock.hide()
			self.postsamples_visible=False
		else:
			self.postsamples_dock.show()
			self.postsamples_visible=True
			self.postsamples_dock.raise_()				


def main():
	app = QtGui.QApplication(sys.argv)
	form = SocialSpatialApp()
	form.show()    
	
	app.exec_()


if __name__ == '__main__':
	main()