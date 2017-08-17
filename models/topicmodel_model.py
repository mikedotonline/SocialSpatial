from gensim import corpora, models
import re
import time

import psycopg2
import models.databaseConnection_model as DB_model
import models.SocialMedia_model as Socialmedia 


import logging #get some logging going to make it easier to debug
logging.basicConfig(level=logging.INFO) #optional argument, filename="tk_freebase-explorer.log" and filemode='w'
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

class TopicModel(object):
	def __init__(self,_topics,_topicwords,_passes,_alpha,_update,_stopwords,_areaStratify):		
		
		#params
		self.num_topics = _topics 			#int
		self.num_topicwords = _topicwords 	#int
		self.num_passes = _passes 			#int
		self.num_alpha = _alpha 			#float
		self.stopwords=_stopwords 			#list
		self.areaStratify = _area 			#boolean
		
		self.socialmedia=None 				#SocialMedia_Posts[SocialMedia]
		self.topics = [] 					#list [topic]
	
	def get_topics (self, db_conn, _likeString, _spatialBoundary):

		social_data = Socialmedia(db_conn,_spatialBoundary,_likestring,limit=0)

		return topics





# class Topic(object):
# 	def __init__(self, topicData)
# 		self.topic = list(tuple)

