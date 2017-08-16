from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import models.wordlist_model as wordlist_model
import models.databaseConnection_model as db_model
import models.SocialMedia_model as socialmedia
import psycopg2
import ast
import re

import ui.wordgeography as wordgeography

	# --------------------------------
	# class:     	Wordlist_ui
	# description: 	provide functionality to the wordlist dockable gui element
	# params:     	QtGui.DockWidget, a gui element
	# params:		wordlist.ui_wordlist_dockable, the implmentation of the dockable gui element from qt desginer
	# returns:    	none
	# --------------------------------
class WordGeography_ui(QtGui.QDockWidget, wordgeography.Ui_WordGeography_DockWidget):
	spatialExtent = QtCore.pyqtSignal(str)
	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		self.search_pushButton.clicked.connect(self.search)
		self.loadhtml()
		self.selectedWords=[]

		#self.map_webView.wheelEvent.connect(self.get_extent)
		#self.map_webView.mousePressEvent.connect(self.get_extent)

	def search(self):
		self.frame = self.map_webView.page().mainFrame()

		# js = "L.marker([  49.278811, -122.916560]).addTo(mymap)"\
		# 	".bindPopup(\"<b>Twitter Content</b><br />New Popup\").openPopup();"
		# self.frame.evaluateJavaScript(js)

		#bug, i can't figure out how to delete old markers. might have to delve into marker groups. if i want to segment searches by color, this is where I wold do that
		#js='mymap.clearLayers();'
		#self.frame.evaluateJavaScript(js)

		social_media = self.get_posts()
		print ("creating markers")
		#img=''
		for i in social_media.posts:
			#print(i) 
			# coords = ast.literal_eval(i[1])
			#rendering images....
			#img=''
			# if "http://t.co" in i[0]:
			# 	img= re.search("(?P<url>https?://[^\s]+)", i[0]).group("url")
			# 	print ("img %s" %img)
			# js =  "L.marker([  "+str(coords["coordinates"][1])+", "+str(coords["coordinates"][0])+" ]).addTo(mymap) .bindPopup(\"<b>"+i[2]+"</b><br />"+i[0]+"<img src=\'"+img+"\' /> \").openPopup();"
			#js =  "L.marker([  "+i.lat+", "+i.lon+" ],{icon:red}).addTo(mymap) .bindPopup(\"<b>"+i.username+"</b><br />"+i.text+"<br>at:"+str(i.time)+" \").openPopup();"
			js = "L.marker(["+i.lat+","+i.lon+"]).addTo(mymap).bindPopup(\"<b>"+i.username+"</b><br />"+i.text+"<br>at:"+str(i.time)+" \").openPopup();"
			# #format the social media posting marker
			self.frame.evaluateJavaScript(js)
		#done

		js = "var bounds = L.latLngBounds(markerArray); map.fitBounds(bounds);"
		self.frame.evaluateJavaScript(js)

	def loadhtml(self):
		f=[line.rstrip('\n') for line in open('./data/wordgeography.html')]
		html=''
		for i in f:html+=i 
		#print(html)
		self.map_webView.setHtml(html)

	def get_posts(self):
		
		likeString =''
		for w in self.selectedWords:
			likeString+= str(self.db_connection[1].socialdata)+" LIKE (\'%"+w+"%\') OR "			
		likeString = likeString[:-3]

		if self.boundary_comboBox.currentText() == "Boundary Table":
			#1. create select string
			#2. use select string to get a limit number of posts that are in the area table boundary
			#3. return a list of the social media data 			
			# try:			
			
			spatialBoundary = "ST_Contains(ST_TRANSFORM("+self.db_connection[1].areatable+"."+self.db_connection[1].areageom+",4326),"+self.db_connection[1].socialtable+"."+self.db_connection[1].socialgeom+")"
			#print("spatialBoundary: %s" % spatialBoundary)									
			# sel = "select"
			# where 
			# lim 
			#selectString = "select tweet, handle from van_tweets limit 10"

			# except:
			# 	print ("no connection data yet, try connecting first")

			#selectString = "SELECT "+self.db_connection[1].socialdata+", ST_ASGEOJSON("+self.db_connection[1].socialgeom+"), "+self.db_connection[1].socialusername+" FROM "+self.db_connection[1].socialtable+", "+self.db_connection[1].areatable+" WHERE ("+likeString+") AND "+spatialBoundary+" LIMIT "+str(self.limit_lineEdit.text())		
		else:
			# JSVar = self.frame.evaluateJavaScript('getMapExtent();').toPyObject()
			# # print ("the current mapextent is %s" % str(JSVar))
			# #self.frame.evaluateJavaScript(JSVar)
			# sw_lng= JSVar[QString("_southWest")][QString("lng")]
			# sw_lat= JSVar[QString("_southWest")][QString("lat")]
			# ne_lng= JSVar[QString("_northEast")][QString("lng")]
			# ne_lat= JSVar[QString("_northEast")][QString("lat")]

			# p1 = str(ne_lng)+" "+str(ne_lat)			
			# p2 = str(ne_lng)+" "+str(sw_lat)
			# p3 = str(sw_lng)+" "+str(sw_lat)
			# p4 = str(sw_lng)+" "+str(ne_lat)

			spatialBoundary = self.get_extent()
			# spatialBoundary = " coords && \'POLYGON(("+p1+","+p2+","+p3+","+p4+","+p1+"))\'"
			#spatialBoundary = " coords && \'ST_POLYGON(("+str(sw_lng)+" "+str(sw_lat)+","+str(ne_lng)+" "+str(ne_lat)+"))\'"
			#spatialBoundary = " coords && \'POLYGON(("+JSVar["_southWest"]["lng"]+" "+JSVar["_southWest"]["lat"]+","+JSVar["_northEast"]["lng"]+" "+JSVar["_northEast"]["lat"]+"))\'"
			# spatialBoundary = " coords && \'POLYGON((-123.30 49.10, -122.73 49.10, -122.73 49.3, -123.30 49.3, -123.30 49.10))\'"
			print (spatialBoundary)
			
			#selectString = "SELECT "+self.db_connection[1].socialdata+", ST_ASGEOJSON("+self.db_connection[1].socialgeom+"), "+self.db_connection[1].socialusername+" FROM "+self.db_connection[1].socialtable+" WHERE ("+likeString+") AND "+spatialBoundary+" LIMIT "+str(self.limit_lineEdit.text())
			
		print("starting search for posts")
				
		# cur = self.db_connection[0].cursor()
		# cur.execute(selectString)
		# print("search completed, returning results cursor")
		# return cur

		sm = socialmedia.SocialMedia_posts()
		sm.get_social_from_database(self.db_connection,spatialBoundary,likeString,str(self.limit_lineEdit.text()))
		return sm 

	@QtCore.pyqtSlot()
	def get_extent (self):
		JSVar = self.frame.evaluateJavaScript('getMapExtent();').toPyObject()
		# print ("the current mapextent is %s" % str(JSVar))
		#self.frame.evaluateJavaScript(JSVar)
		sw_lng= JSVar[QString("_southWest")][QString("lng")]
		sw_lat= JSVar[QString("_southWest")][QString("lat")]
		ne_lng= JSVar[QString("_northEast")][QString("lng")]
		ne_lat= JSVar[QString("_northEast")][QString("lat")]

		p1 = str(ne_lng)+" "+str(ne_lat)			
		p2 = str(ne_lng)+" "+str(sw_lat)
		p3 = str(sw_lng)+" "+str(sw_lat)
		p4 = str(sw_lng)+" "+str(ne_lat)

		spatialBoundary = " coords && \'POLYGON(("+p1+","+p2+","+p3+","+p4+","+p1+"))\'"

		self.spatialExtent.emit(spatialBoundary)
		return spatialBoundary


	@QtCore.pyqtSlot(list)
	def on_selectedWords(self,message):
		self.selectedWords = message

		self.raise_()

	@QtCore.pyqtSlot(list)
	def on_connection(self,message):
		self.db_connection = message
		print(self.db_connection[1])
		self.raise_()

	@QtCore.pyqtSlot(tuple)
	def on_samples(self,message):
		self.frame = self.map_webView.page().mainFrame()
		print ("creating markers from samples")
		for i in message[0].posts:
			#create js for maker					
			#js = "L.marker(["+i.lat+","+i.lon+"], {icon: redMarker}).addTo(mymap).bindPopup(\"<b>"+i.username+"</b><br />"+i.text+"<br>at:"+str(i.time)+" \").openPopup();"
			js =  "L.marker([  "+i.lat+", "+i.lon+" ]).addTo(mymap) .bindPopup(\"<b>"+i.username+"</b><br />"+i.text+"<br>at:"+str(i.time)+" \").openPopup();"
			print ("placeing marker")
			#js =  "L.marker([  "+i.lat+", "+i.lon+" ],{icon: redmarker }).addTo(mymap) .bindPopup(\"<b>"+i.username+"</b><br />"+i.text+"<br>at:"+str(i.time)+" \").openPopup();"
			# #format the social media posting marker
			self.frame.evaluateJavaScript(js)


