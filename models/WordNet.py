# --------------------------------
#class WordNet
#description: this class finds all semantic equivalent terms
#parameter: the search term
# --------------------------------
class WordNet:
	def __init__ (self,word):
		self.word = word
		#searchString = self.word+".n.01" #use first definition
		#self.term = wn.synset(searchString) #make a synset of the term

		#for debugging, write out a lists of everything that is going on
		# for i,j, in enumerate(wn.synsets(word)):
		# 	logging.info("word",i,j.name())
		# 	logging.info("Synonyms:"+", ".join(j.lemma_names()))
		# 	logging.info("Hypernyms:"+" ,".join(list(chain(*[l.lemma_names() for l in j.hypernyms()]))))
		# 	logging.info("Hyponyms:"+" ,".join(list(chain(*[l.lemma_names() for l in j.hyponyms()]))))


	
	# --------------------------------
	#method get_hyponyms
	#description: creates a list of all the semantic children 
	#returns: a list of hyponyms
	# --------------------------------
	def get_hyponyms(self):
	# 	hyponyms = set()
	# 	for hyponym in synset.hyponyms():
	# 		hyponyms |= set(self.get_hyponyms(hyponym))
	# 	return hyponyms | set(synset.hyponyms())
		li=[]
		for i,j in enumerate(wn.synsets(self.word)):
			li.append(list(chain(*[l.lemma_names() for l in j.hyponyms()])))
		return li

	# --------------------------------
	#method get_synonyms
	#description: creates a list of all the term synonyms
	#returns: a list of synonyms
	# --------------------------------
	def get_synonyms(self):
		li=[]
		for i,j, in enumerate(wn.synsets(self.word)):
			li.append(j.lemma_names())
		return li 


	# --------------------------------
	#method get_hypernyms
	#description: creates a list of all the semantic parents 
	#returns: a list of hypernyms
	# --------------------------------	
	def get_hypernyms(self):
		li=[]
		for i,j in enumerate(wn.synsets(self.word)):
			li.append(list(chain(*[l.lemma_names() for l in j.hypernyms()])))
		return li
