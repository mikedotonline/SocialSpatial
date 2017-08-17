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
		
		self.stopwords = self.load_stoplist('data\\stoplist.json')

		self.stoplistLoad_pushButton.clicked.connect(self.load_stoplist)
		self.stoplistSave_pushButton.clicked.connect(self.save_stoplist)
		self.runModel_pushButton.clicked.connect(self.run_model)
		self.stopModel_pushButton.clicked.connect(self.stop_model)
		self.loadModel_pushButton.clicked.connect(self.load_model)
		self.saveModel_pushButton.clicked.connect(self.save_model)
		# self.area_comboBox.currentItemChanged.connect(self.set_spatialArea)

		self.topicmodel = None
		self.db_connection = None
		self.selectedWords = None

	def load_stoplist(self,_filename):
		filename = _filename
		with open(filename) as infile:
			d = json.load(infile)
		return d['stopwords'] #list

	def save_stoplist(_filename,d):
		pass		

	def run_model(self):
		#pass
		topicModel = TopicModel(self.topics_LineEdit.text(),self.words_LineEdit.text(),self.passes_lineEdit.text(),self.alpha_lineEdit.text(),self.stopwords,self.areaStratify)
		topics = topicModel.get_topics(db_conn,likeString,spatialBoundary)
		print(topics)

		# for t in topics:
		# 	topicModelResults_treeWidget.addItem()
	def stop_model(self):
		pass

	def load_model(self):
		pass

	def save_model(self):
		filename = str(self.topicModelFile_lineEdit.text())		
		with open(filename,'w') as outfile:
			json.dump(self.topicmodel,outfile,ensure_ascii=False)

	def set_spatialArea(self):
		if self.area_comboBox.currentItem() =="Yes":
			self.areaStratify=True
		else:
			self.areaStratify=False

	@QtCore.pyqtSlot(list)
	def on_selectedWords(self,message):
		self.selectedWords = message

		self.raise_()

	@QtCore.pyqtSlot(list)
	def on_connection(self,message):
		self.db_connection = message
		print(self.db_connection[1])
		self.raise_()