from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import models.wordlist_model as wordlist_model
import models.databaseConnection_model as db_model
import models.SocialMedia_model as socialmedia 
import models.topicmodel_model as TopicModel  

import ui.topicmodel as topicmodel

class TopicModel_ui(QtGui.QDockWidget, topicmodel.Ui_TopicModel_DockWidget):
	
	#signal of the selected words
	#selectedWords = QtCore.pyqtSignal(list)
	
	def __init__(self,parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		


		self.stoplistLoad_pushButton.clicked.connect(self.load_stoplist)
		self.stoplistSave_pushButton.clicked.connect(self.save_stoplist)
		self.runModel_pushButton.clicked.connect(self.run_model)
		self.stopModel_pushButton.clicked.connect(self.stop_model)
		self.loadModel_pushButton.clicked.connect(self.load_model)
		self.saveModel_pushButton.clicked.connect(self.save_model)
		# self.area_comboBox.currentItemChanged.connect(self.set_spatialArea)

	def load_stoplist(self):
		self.stopwords = []	
		# add logic for loading stopwords file
		# f = open('data\stopwords.txt')
		# for w in f.readline().split():
		# 	self.stopwords.append(w)
		# 	self.stopwords_listBox.addItem(QString(w))

	def save_stoplist(self):
		pass
	def run_model(self):
		pass
		# topicModel = TopicModel(self.topics_LineEdit.text(),self.words_LineEdit.text(),self.passes_lineEdit.text(),self.alpha_lineEdit.text(),self.stopwords,self.areaStratify)
		# topics = topicModel.get_topics(db_conn,likeString,spatialBoundary)

		# for t in topics:
		# 	topicModelResults_treeWidget.addItem()
	def stop_model(self):
		pass

	def load_model(self):
		pass

	def save_model(self):
		pass
	def set_spatialArea(self):
		if self.area_comboBox.currentItem() =="Yes":
			self.areaStratify=True
		else:
			self.areaStratify=False