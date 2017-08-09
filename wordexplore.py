from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import ui.mainwindow
import ui.dbconn as dbconn
import ui.wordnet as wordnet
import ui.wordlist as wordlist
import models.databaseConnection_model as db_model
import models.GoogleKnowledgeGraph
import models.WordNet

class WordExploreApp(QtGui.QMainWindow, ui.mainwindow.Ui_MainWindow):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		self.dbconn_dock = DBconn_ui()
		self.addDockWidget(Qt.LeftDockWidgetArea,self.dbconn_dock)

		self.wordnet_dock = Wordnet_ui()
		self.addDockWidget(Qt.RightDockWidgetArea,self.wordnet_dock)
		self.wordnet_dock.hide()

		self.wordlist_dock = Wordlist_ui()
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


class DBconn_ui(QtGui.QDockWidget, dbconn.Ui_dbconn_dockable):
	def __init__(self,parent=None):
		super(self.__class__,self).__init__(parent)
		self.setupUi(self)

		self.config_LoadFile_pushButton.clicked.connect(self.load_config)
		self.config_saveFile_pushButton.clicked.connect(self.save_config)


	def load_config(self):
		print 'load btn pressed'
		db = db_model.DatabaseConnection()
		db.json_load(self.config_filename_lineEdit.text())

		self.conn_host_lineEdit.setText(db.host)
		self.conn_port_lineEdit.setText(db.port)
		self.conn_userfilename_lineEdit.setText(db.userinfo)
		self.conn_dbname_lineEdit.setText(db.dbname)

		self.social_table_lineEdit.setText(db.socialtable)
		self.social_data_lineEdit.setText(db.socialdata)
		self.social_time_lineEdit.setText(db.socialtime)
		self.social_user_lineEdit.setText(db.socialusername)
		self.social_geom_lineEdit.setText(db.socialgeom)

		self.area_table_lineEdit.setText(db.boundarytable)
		self.area_label_lineEdit.setText(db.boundarylabel)
		self.area_geom_lineEdit.setText(db.boundarygeom)



	def save_config(self):
		print 'save btn pressed'

class Wordnet_ui(QtGui.QDockWidget, wordnet.Ui_wordnet_dockable):
	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
	def foo(self):
		pass

class Wordlist_ui(QtGui.QDockWidget, wordlist.Ui_wordlist_dockable):
	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
	def foo(self):
		pass


def main():
	app = QtGui.QApplication(sys.argv)
	form = WordExploreApp()
	form.show()    
	
	app.exec_()


if __name__ == '__main__':
	main()