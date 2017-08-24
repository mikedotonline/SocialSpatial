from gensim import corpora, models
import re
import time

#import psycopg2	social media gathering is done by the social media data model
import models.databaseConnection_model as DB_model
import models.SocialMedia_model as Socialmedia 


import logging #get some logging going to make it easier to debug
logging.basicConfig(level=logging.INFO) #optional argument, filename="tk_freebase-explorer.log" and filemode='w'
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

class TopicModel(object):
	def __init__(self,_topics,_topicwords,_passes,_alpha,_update,_stopwords):		
		
		#params
		self.num_topics = int(_topics) 			#int
		self.num_topicwords = int(_topicwords) 	#int
		self.num_passes = int(_passes) 			#int
		self.num_alpha = float(_alpha) 			#float
		self.num_update = int(_update)			#int
		self.stopwords=_stopwords 			#list
		
		self.social_data=None 				#SocialMedia_Posts[SocialMedia]
		self.topics = None 					#dictionary
		self.area_topics = None

	def get_topics (self, db_conn, _likeString, _spatialBoundary,_name):
		self.social_data = Socialmedia.SocialMedia_posts()
		lim="100"
		self.social_data.get_social_from_database(db_conn,_spatialBoundary,_likeString,lim)
		print("%s tweets recieved, starting gensim operations" % len(self.social_data.posts))
		model = self.do_gensim()

		topics = self.format_topics(model.show_topics(num_topics=self.num_topics,num_words=self.num_topicwords,log=False,formatted=False),_name)

		return topics
	
	def format_topics(self,_model,_name):
	    model = {"name":_name}
	    topics = {}
	    t=0
	    for i in _model:
	        #print ("topic") 
	        #print i #touple (#,topic
	        dT = {}
	        r=0
	        for j in i[1]: #the topic in each tuple
	            d = {"word":str(j[0]),"prob":str(j[1])}

	            dT["Topic Word"+str(r)] = d
	            r+=1
	        topics["topic"+str(t)]=dT
	        t+=1
	    model["topics"]=topics

	    return model


	def do_gensim(self):
		logging.info("Starting GENSIM code")
		documents=[]
		logging.info("INCOMMING TWEET CORPUS SIZE: "+str(len(self.social_data.posts)))
		for tweet in self.social_data.posts:
			#tweet = str(curr.fetchone()[0])
			#print("doc:%s" %tweet.text)
			documents.append(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(gt)"," ",tweet.text).split()).lower())
		
		logging.info("CORPUS SIZE AFTER REGEX: "+str(len(documents)))
		

		#stoplist work
		s = ""
		for w in self.stopwords:
			s+=w+" "
		stoplist = set(s.split())
		#print("stoplist %s" % str(stoplist))
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

