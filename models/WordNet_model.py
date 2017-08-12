import nltk
from nltk.corpus import wordnet as wn #use NLTK for access to wordNet
from itertools import chain
# --------------------------------
#class WordNet
#description: this class finds all semantic equivalent terms
#parameter: the search term
# --------------------------------
class WordNet:
	def __init__ (self,word):
		self.word = word
		self.hyponyms = self.get_hyponyms()
		self.synonyms = self.get_synonyms()
		self.hypernyms = self.get_hypernyms()
			
	# --------------------------------
	#method get_hyponyms
	#description: creates a list of all the semantic children 
	#returns: a list of hyponyms
	# --------------------------------
	def get_hyponyms(self):
		li=[]
		for i,j in enumerate(wn.synsets(self.word)):
			li.append(list(chain(*[l.lemma_names() for l in j.hyponyms()])))
		return list(set([item for sublist in li for item in sublist])) #this line flattens the lits of lists and removes duplicates.... so pythonic it hurts (to read)

	# --------------------------------
	#method get_synonyms
	#description: creates a list of all the term synonyms
	#returns: a list of synonyms
	# --------------------------------
	def get_synonyms(self):
		li=[]
		for i,j, in enumerate(wn.synsets(self.word)):
			for k in j.lemma_names():
				li.append(k)
				li = list(set(li))
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
		return list(set([item for sublist in li for item in sublist]))
