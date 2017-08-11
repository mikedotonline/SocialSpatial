# --------------------------------
# class:     GoogleKnowledgeGraph
# description: a class for handling requests to the google knowledge graph
# params:     none
# returns:    none
# --------------------------------
class GoogleKnowledgeGraph(object):
	#set initial params
	def __init__(self,key_file,query,limit,types):
		self.api_key = open(key_file).read()
		self.service_url = 'https://kgsearch.googleapis.com/v1/entities:search'

		self.data = get_response(query,limit,types)

		# if types == 'thing':
			#self.data = get_thing (query,limit)
		# else if types == 'product':
			#self.data = get_products(query, limit)
		# else if types == 'person':
			#self.data = get_person(query,limit)
		#else:
			# throw execption hissyfit
		

	# --------------------------------
	# method:     get_response
	# description:query the google knowledge api and grab some json to play with
	# params:   query, the term that we will search
	#           limit, the number of search results to display
	#           types, the thype of things to reply with: Products, Things, People,etc.
	# returns:  response, the json object back from google
	# --------------------------------
	def get_response(self,query,limit,types):
		self.params= {
		'query':query,
		'limit':limit,
		'indent':True,
		'types':types,
		'key':self.api_key,
		}

		url = self.service_url + '?' + urllib.urlencode(self.params)
		t = datetime.now()
		response = json.loads(urllib.urlopen(url).read())
		logging.info("response completed in: "+str(datetime.now()-t))
		return response 

	def get_products(self):
		pass
		#do get_response with a product type query and form a data object using that 

	def get_thing(self):
		pass
		#do get_response with a thing type query and form a data object based o nthe response

	def get_person(self):
		pass
		#do get response with a thing type query and form a data object based on the response