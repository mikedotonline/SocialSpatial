from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import json

# import models.wordlist_model as wordlist_model
# import models.databaseConnection_model as db_model
# import models.SocialMedia_model as socialmedia 
import models.topicmodel_model as TopicModel  
import models.shapefile_model as shapefile 

from pprint import pprint as pp


import resources.shpUtils as shpUtils
import resources.shp_wordle_prettier as wordle 
import cairo # for creating a raster surface
import numpy as np #for handling multi-dimensional arrays

import ui.cartogram as cartogram

class Cartogram_ui(QtGui.QDockWidget, cartogram.Ui_Cartogram_dock):
	
	#signal of the selected words
	#selectedWords = QtCore.pyqtSignal(list)
	
	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		# a basic way to set the value of the progressbar.
		self.progressBar.setValue(0)

		self.run_pushButton.clicked.connect(self.run)

		pixmap = QPixmap('data\cartogram_example.jpg')
		self.preview_label.setPixmap(pixmap)

	def run(self):
		s = shapefile.Shapefile('data\\van_nhoods\\van_nhoods.shp')
		# Dummy list of wrods for debugging

		#real words from postgres database
		tableName = 'geoLDA_van_complete'
		t = wordle.TopicWords(tableName)
		words = t.words

		#words = prepare_words(topcis)

		cloud = wordle.Shp_WordCloud(words,s)
		cloud.show()


	def prepare_words(self, _topicModel):
		pass
		# augment the topic model data into a list of words that the wordle can sue

	@QtCore.pyqtSlot(dict)
	def on_areatopics(self,message):
		self.areatopics = message
