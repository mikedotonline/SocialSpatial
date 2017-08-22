from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import json

import models.wordlist_model as wordlist_model
import models.databaseConnection_model as db_model
import models.SocialMedia_model as socialmedia 
import models.topicmodel_model as TopicModel  

from pprint import pprint as pp

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

		for w in d['stopwords']:
			self.stoplist_listWidget.addItem(QString(w))

		return d['stopwords'] #list


	def save_stoplist(_filename,d):
		pass		

	def run_model(self):
		#pass
		likeString =''
		for w in self.selectedWords:
			likeString+= str(self.db_connection[1].socialdata)+" LIKE (\'%"+w+"%\') OR "			
		likeString = likeString[:-3]
		
		spatialBoundary = "ST_Contains(ST_TRANSFORM("+self.db_connection[1].areatable+"."+self.db_connection[1].areageom+",4326),"+self.db_connection[1].socialtable+"."+self.db_connection[1].socialgeom+")"

		topicModel = TopicModel.TopicModel(self.topics_lineEdit.text(),self.words_lineEdit.text(),self.passes_lineEdit.text(),self.alpha_lineEdit.text(),self.update_lineEdit.text(),self.stopwords)
		topics = topicModel.get_topics(self.db_connection,likeString,spatialBoundary)
		#print(topics)
		self.add_tree_items(topics)

	def add_tree_items(self, _topics):		
		#set number of columns
		self.topicModelResults_treeWidget.setColumnCount(len(_topics["topics"].keys()))
		
		#set names for columns
		labels = ["topic"]
		for i in range(0,len(_topics['topics'].keys())): 
			labels.append("Word "+str(i)+" (Prob)")
		self.topicModelResults_treeWidget.setHeaderLabels(labels)

		# pp(_topics)

		root = QTreeWidgetItem(self.topicModelResults_treeWidget, [_topics["name"]])

		#ugly, and not as flexible, but works
		# for i in range(0,len(_topics['topics'])):
		# 	topic_level = QTreeWidgetItem(root, ['Topic'+str(i)])
		# 	for j in range(len(_topics['topics']['topic'+str(i)])):
		# 		words_and_probs = []
		# 		words_and_probs.append(_topics['topics']['topic'+str(i)]["Topic Word"+str(j)]["word"]+":"+_topics['topics']['topic'+str(i)]["Topic Word"+str(j)]["prob"][:-7])
		# 		print(words_and_probs)
		# 		word_level = QTreeWidgetItem(topic_level,words_and_probs)
		
		# a more pythonic, flexible method that requires less information about the data structure
		for topic in sorted(_topics["topics"]):			
			words_and_probs = []
			for word in _topics["topics"][topic].keys(): 
				
				words_and_probs.append(_topics["topics"][topic][word]["word"]+" ("+_topics["topics"][topic][word]["prob"][:-9]+")")
			# word_level = QTreeWidgetItem(topic_level,words_and_probs)
			topic_level = QTreeWidgetItem(root,[topic]+words_and_probs)
		self.topicModelResults_treeWidget.setColumnWidth(0,100)




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
		#print(self.db_connection[1])
		self.raise_()