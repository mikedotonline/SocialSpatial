#import json
#from PyQt4 import QtGui
#from datetime import datetime as datetime
import re 
import models.databaseConnection_model as db_model
import psycopg2
import ast

# --------------------------------
# class:     	SocailMedia
# description: 	a data model of a social media posting
# params:     	none
# returns:    	none
# --------------------------------
class SocialMedia(object):
	def __init__(self,_text,_time,_username,_lat,_lon):
		self.text = _text
		self.time = _time
		self.username = _username
		self.link = ''
		self.lat = _lat
		self.lon = _lon
		self.extractLink()
	def extractLink(self):

		if "http://" in self.text:
			self.link= re.search("(?P<url>https?://[^\s]+)", self.text).group("url")
			#print ("img %s" %img)
		else:
			self.link = ''
	

class SocialMedia_posts(object):
	def __init__(self):
		self.posts = []
	
	def get_social_from_database(self,_db_connection,_spatialBoundary,_likeString,_limit):
		_spatialBoundary = "AND "+_spatialBoundary
		selectString = "SELECT "+_db_connection[1].socialdata+", ST_ASGEOJSON("+_db_connection[1].socialgeom+"), "+_db_connection[1].socialusername+","+_db_connection[1].socialtime+" FROM "+_db_connection[1].socialtable+", "+_db_connection[1].areatable+" WHERE ("+_likeString+") "+_spatialBoundary+" LIMIT "+_limit

		cur = _db_connection[0].cursor()
		cur.execute(selectString)

		for i in cur:
			coords = ast.literal_eval(i[1])
			lat = str(coords["coordinates"][1])
			lon = str(coords["coordinates"][0])
			
			user = i[2]
			# print(i[3])
			time = i[3]
			text = i[0]


			sm 	= SocialMedia(text,time,user,lat,lon)
			self.posts.append(sm)







