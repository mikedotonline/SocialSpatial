import json
from PyQt4 import QtGui


class Wordlist(object):
	def __init__(self):
		self.words = {}




	# --------------------------------
	# method:     json_load
	# description: load wordlist information from a json file and map to the wordlist model
	# params:     filename, the json file/path
	# returns:    none
	# --------------------------------
	def json_load(self,filename):
		#filename = 'db_defaultinfo.json'#filenamebox.get()
		with open(filename) as infile:
			d = json.load(infile)

		# to do: for each member var, convert the dictionary item
		self.words=d

	# --------------------------------
	# method:     json_write
	# description: save wordlist information to a json file
	# params:     filename, the json file/path
	# returns:    none
	# --------------------------------
	def json_write(self,filename):
		with open(filename,'w') as outfile:
			json.dump(self.get_as_dictionary(),outfile,ensure_ascii=False)
			with open(filename,'w') as outfile:
				json.dump(self.words,outfile,ensure_ascii=False)

	def len_tags(self):
		longest=0
		for key in self.words.keys():
			if len(self.words[key]) > longest:
					longest=len(self.words[key])	
					print 'longest'+str(longest)				
		return longest