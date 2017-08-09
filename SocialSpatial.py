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

class SocialSpatialApp(QtGui.QMainWindow, ui.mainwindow.Ui_MainWindow):
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
		self.db = db_model.DatabaseConnection()		
		
		#create signals for text changes in the form items
		self.conn_host_lineEdit.textChanged.connect(self.set_host) #connect the contents of con_host to the data model
		self.conn_port_lineEdit.textChanged.connect(self.set_port)
		self.conn_userfilename_lineEdit.textChanged.connect(self.set_userfilename)
		self.conn_dbname_lineEdit.textChanged.connect(self.set_dbname)

		self.social_table_lineEdit.textChanged.connect(self.set_socialtable)
		self.social_data_lineEdit.textChanged.connect(self.set_socialdata)
		self.social_time_lineEdit.textChanged.connect(self.set_socialtime)
		self.social_user_lineEdit.textChanged.connect(self.set_socialuser)
		self.social_geom_lineEdit.textChanged.connect(self.set_socialgeom)

		self.area_table_lineEdit.textChanged.connect(self.set_areatable)
		self.area_label_lineEdit.textChanged.connect(self.set_arealabel)
		self.area_geom_lineEdit.textChanged.connect(self.set_areageom)

	#methods for signals. i bet this could have all been done inline with lambda functions.
	# self.conn_host_lineEdit.connect(lambda s:self.db.socialtable=s) 
	def set_host(self,host):self.db.host = str(host)
	def set_port(self,port):self.db.port = str(port)
	def set_userfilename(self,userinfo):self.db.userinfo = str(userinfo)
	def set_dbname(self,dbname):self.db.dbname = str(dbname)

	def set_socialtable(self,s): self.db.socialtable = str(s)
	def set_socialdata(self,s): self.db.socialdata = str(s)
	def set_socialtime(self,s): self.db.socialtime = str(s)
	def set_socialuser(self,s): self.db.socialusername = str(s)
	def set_socialgeom(self,s): self.db.socialgeom = str(s)

	def set_areatable(self,a):self.db.areatable = str(a)
	def set_arealabel(self,a):self.db.arealabel = str(a)
	def set_areageom(self,a):self.db.areageom = str(a)


	def load_config(self):
		print 'load btn pressed'		
		self.db.json_load(self.config_filename_lineEdit.text())

		self.conn_host_lineEdit.setText(self.db.host)
		self.conn_port_lineEdit.setText(self.db.port)
		self.conn_userfilename_lineEdit.setText(self.db.userinfo)
		self.conn_dbname_lineEdit.setText(self.db.dbname)

		self.social_table_lineEdit.setText(self.db.socialtable)
		self.social_data_lineEdit.setText(self.db.socialdata)
		self.social_time_lineEdit.setText(self.db.socialtime)
		self.social_user_lineEdit.setText(self.db.socialusername)
		self.social_geom_lineEdit.setText(self.db.socialgeom)

		self.area_table_lineEdit.setText(self.db.areatable)
		self.area_label_lineEdit.setText(self.db.arealabel)
		self.area_geom_lineEdit.setText(self.db.areageom)



	def save_config(self):
		print 'save btn pressed'
		print 'self.db.host: '+self.db.host #testing
		self.db.json_write(self.config_filename_lineEdit.text())


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
	form = SocialSpatialApp()
	form.show()    
	
	app.exec_()


if __name__ == '__main__':
	main()