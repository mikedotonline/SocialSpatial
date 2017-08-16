from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import models.wordlist_model as wordlist_model
import models.databaseConnection_model as db_model
import models.SocialMedia_model as socialmedia 
#import psycopg2

import ui.postsamples as postsamples

class PostSamples_ui(QtGui.QDockWidget, postsamples.Ui_PostSamples_DockWidget):
	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		self.search_pushButton.clicked.connect(self.search)
		self.addToMap_pushButton.clicked.connect(self.addToMap)

		self.selectedWords = []
		self.mapBoundary='' #once i connect the even handler of mouse wheel and mouse click

	def search (self):
		social_media = self.get_posts()
		print("writing values")
		for i in social_media.posts:
			self.results_listWidget.addItem(QString(i.text))
			print(i.text)



	def addToMap (self):
		pass
		#get the current social media posts
		# create a signal when the add to map button is pressed
		# create a touple of (socialmedia_posts, color)
		# emit object

	def get_posts(self):
		
		likeString =''
		for w in self.selectedWords:
			likeString+= str(self.db_connection[1].socialdata)+" LIKE (\'%"+w+"%\') OR "			
		likeString = likeString[:-3]

		if self.boundary_comboBox.currentText() == "Area Table":	
			
			spatialBoundary = "ST_Contains(ST_TRANSFORM("+self.db_connection[1].areatable+"."+self.db_connection[1].areageom+",4326),"+self.db_connection[1].socialtable+"."+self.db_connection[1].socialgeom+")"									
			#selectString = "SELECT "+self.db_connection[1].socialdata+", ST_ASGEOJSON("+self.db_connection[1].socialgeom+"), "+self.db_connection[1].socialusername+" FROM "+self.db_connection[1].socialtable+", "+self.db_connection[1].areatable+" WHERE ("+likeString+") AND "+spatialBoundary+" LIMIT "+str(self.limit_lineEdit.text())		
		
		#else if the user selects the area boundary of the map extent.
		# currently i need to make my own event handler for the mousePressEvent event in the UI code
		# https://stackoverflow.com/questions/37365036/how-to-detect-if-a-mouse-button-was-pressed-on-a-qwebview
		# https://stackoverflow.com/questions/39559334/pysideqwebviews-mouse-move-and-mouse-press-events-freezing-html-document
		elif self.boundary_comboBox.currentText() == "Word Map Extent":
			pass
			

			# if self.mapBoundary =='':
			# 	spatialBoundary = " coords && \'POLYGON((-123.30 49.10, -122.73 49.10, -122.73 49.3, -123.30 49.3, -123.30 49.10))\'"
			# else:
			# 	spatialBoundary = self.mapBoundary			
			#selectString = "SELECT "+self.db_connection[1].socialdata+", ST_ASGEOJSON("+self.db_connection[1].socialgeom+"), "+self.db_connection[1].socialusername+" FROM "+self.db_connection[1].socialtable+" WHERE ("+likeString+") AND "+spatialBoundary+" LIMIT "+str(self.limit_lineEdit.text())
		else: 
			spatialBoundary = ''
			#selectString = "SELECT "+self.db_connection[1].socialdata+", ST_ASGEOJSON("+self.db_connection[1].socialgeom+"), "+self.db_connection[1].socialusername+" FROM "+self.db_connection[1].socialtable+" WHERE ("+likeString+") LIMIT "+str(self.limit_lineEdit.text())

		print("starting search for posts")
				
		#cur = self.db_connection[0].cursor()
		#cur.execute(selectString)
		print("search completed, returning results cursor")

		sm = socialmedia.SocialMedia_posts()
		sm.get_social_from_database(self.db_connection,spatialBoundary,likeString,str(self.limit_lineEdit.text()))

		#return cur
		return sm 

	@QtCore.pyqtSlot(list)
	def on_selectedWords(self,message):
		self.selectedWords = message

		self.raise_()

	@QtCore.pyqtSlot(list)
	def on_connection(self,message):
		self.db_connection = message
		print(self.db_connection[1])
		self.raise_()

	@QtCore.pyqtSlot(str)
	def on_extent(self,message):
		self.mapBoundary = message