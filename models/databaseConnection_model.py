import json

class DatabaseConnection(object):
	def __init__(self):
		self.host=''
		self.port=''
		self.dbname=''
		self.userinfo=''
		self.socialtable=''
		self.socialdata=''
		self.socialgeom=''
		self.socialusername=''
		self.socialtime=''
		self.boundarytable=''
		self.boundarygeom=''
		self.boundarylabel=''		

	# --------------------------------
	# method:     json_load
	# description: load database connection information from a json file and map to the DatabaseConnection model
	# params:     filename, the json file/path
	# returns:    none
	# --------------------------------
	def json_load(self,filename):
		#filename = 'db_defaultinfo.json'#filenamebox.get()
		with open(filename) as infile:
			d = json.load(infile)
		
		self.host=d['host']
		self.port=d['port']
		self.dbname=d['dbname']
		self.userinfo=d['userinfo']
		self.socialtable=d['socialtable']
		self.socialdata=d['socialdata']
		self.socialgeom=d['socialgeom']
		self.socialusername=d['host']
		self.socialtime=d['host']
		self.boundarytable=d['boundarytable']
		self.boundarygeom=d['boundarygeom']
		self.boundarylabel=d['boundaryname']

	
	# --------------------------------
	# method:     json_write
	# description: save database connection information to a json file
	# params:     filename, the json file/path
	# returns:    none
	# --------------------------------
	def json_write(self,filename):
		with open(filename,'w') as outfile:
			json.dump(get_as_dictionary(),outfile,ensure_ascii=False)

	# --------------------------------
	# method:     get_as_dictionary
	# description: return the database connection info as a dictionary
	# params:     none
	# returns:    a dictionary withthe items of a database connection model
	# --------------------------------
	def get_as_dictionary(self):
		return {
			"host":self.host,
			"port":self.port,
			"dbname":self.dbname,
			"userinfo":self.userinfo,
			"socialtable":self.socialtable,
			"socialdata":self.socialdata,
			"socialgeom":self.socialgeom,
			"boundarytable":self.boundarytable,
			"boundarygeom":self.geom,
			"boundaryname":self.boundaryname
			}

