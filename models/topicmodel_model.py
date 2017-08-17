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
	def __init__(self,_topics,_topicwords,_passes,_alpha,_update,_stopwords):		
		
		#params
		self.num_topics = _topics 			#int
		self.num_topicwords = _topicwords 	#int
		self.num_passes = _passes 			#int
		self.num_alpha = _alpha 			#float
		self.num_update = _update			#int
		self.stopwords=_stopwords 			#list
		
		self.socialmedia=None 				#SocialMedia_Posts[SocialMedia]
		self.topics = None 					#dictionary
		self.area_topics = None

	def get_topics (self, db_conn, _likeString, _spatialBoundary):

		self.social_media = Socialmedia(db_conn,_spatialBoundary,_likestring,limit=0)
		print("data recieved, starting gensim operations")
		model = self.do_gensim()

		topics = self.format_topics(model.show_topics(num_topics=self.num_topics,num_words=self.num_topicwords,log=False,formatted=False))

		return topics
	
	def format_topics(_model):
		#incomming model in forms of list[list[tuple()]] model[topic(word,prob)]
		topic_model={}
		topic_model["Name"] = "Test Topic Model"
		i=0
		for topics in _model:
			#for each topic in the Gensim Model topics
			topics["Topic Number "] = str(i)
			for topic in topics:
				topic_d = {}
				j=0
				for topic_word in topic:
					d_fromTuple = {}
					d_fromTuple["word"+str(j)] = topic_word[0] #look up the syntax of the gensim.model return function
					d_fromTuple["probability"]=topic_word[1]
					j+=1
				topic_d["Word "+str(i)]=d_fromTuple
			i+=1			
			#this space is where we set the Topic Number			
			topics["Topics Words"] = topic_d
		topic_model["Topics"] = topics

		return topic_model




	def do_gensim():
		logging.info("Starting GENSIM code")
		documents=[]
		logging.info("INCOMMING TWEET CORPUS SIZE: "+str(len(social_data.posts)))
		for tweet in social_data.posts:
			#tweet = str(curr.fetchone()[0])
			documents.append(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(gt)"," ",tweet.text.split()).lower()))
		
		logging.info("CORPUS SIZE AFTER REGEX: "+str(len(documents)))
		

		#stoplist work
		s = ""
		for w in self.stopwords:
			s+=w+" "
		stoplist = set(s.split())
		#logging.info("s:\n\t"+s)
		#logging.info("stopwords"+str([i for i in self.builder.get_object('TopicStopwords_Listbox').get(0,tk.END)]))
		#logging.info(stoplist)
		
		#tokenize
		texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]		
		logging.info("CORPUS SIZE AFTER STOPLIST: "+str(len(texts)))	

		#singles reduction
		all_tokens = sum(texts, [])
		logging.info("beginning tokenization")
		tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
		logging.info("words tokenized, starting single mentioned word reduction")
		texts = [[word for word in text if word not in tokens_once] for text in texts]
		logging.info("words mentioned only once removed")
		#remove nulls
		texts = filter(None,texts)
		logging.info("CORPUS SIZE AFTER EMPTY ROWS REMOVED: "+str(len(texts)))			
		dictionary = corpora.Dictionary(texts)
		
		#create corpus, tfidf, set up model
		corpus = [dictionary.doc2bow(text) for text in texts]
		tfidf = models.TfidfModel(corpus) #step 1. --initialize(train) a model
		corpus_tfidf = tfidf[corpus] # Apply TFIDF transform to entire corpus
		logging.info("starting LDA model")

		#run model
		
		model = models.ldamodel.LdaModel(corpus_tfidf, id2word=dictionary, alpha=self.num_alpha, num_topics=self.num_topics, update_every=self.num_update, passes=self.num_passes)

		return model


class Area_TopicModel(object):
	def __init__(self, topicData)
		self.area

