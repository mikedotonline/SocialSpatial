from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import models.wordlist_model as wordlist_model
import models.databaseConnection_model as db_model
import psycopg2
import ast

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
		self.selectedWords=[]

	def search(self):
		self.frame = self.map_webView.page().mainFrame()

		# js = "L.marker([  49.278811, -122.916560]).addTo(mymap)"\
		# 	".bindPopup(\"<b>Twitter Content</b><br />New Popup\").openPopup();"
		# self.frame.evaluateJavaScript(js)

		socialmedia = self.get_posts()

		for i in socialmedia:
			#print(i) 
			coords = ast.literal_eval(i[1])
			js =  "L.marker([  "+str(coords["coordinates"][1])+", "+str(coords["coordinates"][0])+" ]).addTo(mymap) .bindPopup(\"<b>"+i[2]+"</b><br />"+i[0]+" \").openPopup();"
			# #format the social media posting marker
			self.frame.evaluateJavaScript(js)
		#done

		js = "var bounds = L.latLngBounds(markerArray); map.fitBounds(bounds);"
		self.frame.evaluateJavaScript(js)

	def loadhtml(self):
		f=[line.rstrip('\n') for line in open('./data/wordgeography.html')]
		html=''
		for i in f:html+=i 
		print(html)
		self.map_webView.setHtml(html)

	def get_posts(self):
		if self.boundary_comboBox.currentText() == "Boundary Table":
			pass
			#1. create select string
			#2. use select string to get a limit number of posts that are in the area table boundary
			#3. return a list of the social media data 
			
			# try:
			likeString =''
			for w in self.selectedWords:
				likeString+= str(self.db_connection[1].socialdata)+" LIKE (\'%"+w+"%\') OR "			
			likeString = likeString[:-3]
			print(likeString)

			selectString = "SELECT "+self.db_connection[1].socialdata+", ST_ASGEOJSON("+self.db_connection[1].socialgeom+"), "+self.db_connection[1].socialusername+" FROM "+self.db_connection[1].socialtable+" WHERE "+likeString+" LIMIT "+str(self.limit_lineEdit.text())
			
			# sel = "select"
			# where 
			# lim 
			#selectString = "select tweet, handle from van_tweets limit 10"
			cur = self.db_connection[0].cursor()
			cur.execute(selectString)

			return cur

			# except:
			# 	print ("no connection data yet, try connecting first")
		else:
			pass

	@QtCore.pyqtSlot(list)
	def on_selectedWords(self,message):
		self.selectedWords = message

		self.raise_()

	@QtCore.pyqtSlot(list)
	def on_connection(self,message):
		self.db_connection = message
		print(self.db_connection[1])
		self.raise_()