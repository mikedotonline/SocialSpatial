import resources.shpUtils as shpUtils # for shapefile reading, requires dbfUtils.py
# import resources.shp_wordle_prettier  as s
import models.poly_model as poly 

import logging #intelligent logging....
logging.basicConfig(level=logging.debug) # optional argument filename='example.log'

class Shapefile(object):
	'''Class Shapefile
	Data Object to capture records from the shpUtils package
	'''
	def __init__(self,filename):
		self.filename = filename # the filename and location of the shapefile
		self.records = [] #list of easch poly in the shapefile
		self.minX = 9999
		self.maxX =-9999
		self.minY= 9999
		self.maxY= -9999

		shpRecords = shpUtils.loadShapefile(self.filename) 

		for i in range(0,len(shpRecords)):
			x=[]
			y=[]
			for j in range(0,len(shpRecords[i]['shp_data']['parts'][0]['points'])):
				tempx = float(shpRecords[i]['shp_data']['parts'][0]['points'][j]['x'])
				tempy = float(shpRecords[i]['shp_data']['parts'][0]['points'][j]['y'])
				x.append(tempx)
				y.append(tempy)

			name = shpRecords[i]['dbf_data']['NAME']
			#logging.info("reading name:"+name)
			#name = 'test'
			self.records.append(poly.Poly(x,y,name))

		# Calculates the spatial extents. ideally this information is calculated in the above for loop, but i'm lazy and this is fast.
		for p in self.records:										# for each poly
			tX = min(p.coords[...,0])									# find the min value of X
			tY = min(p.coords[...,1])									# find the min value of Y
			if tX<self.minX: self.minX=tX 								# if the current poly's min x is smaller than recorded minX, set min to current
			if tY<self.minY: self.minY=tY 								# if the current poly's min y is smaller than recorded miny, set min to current
			tX = max(p.coords[...,0])									# find the max value of X
			tY = max(p.coords[...,1])									# find the max value of Y
			if tX>self.maxX: self.maxX=tX 								# if the current poly's max x is smaller than recorded maxX, set min to current
			if tY>self.maxY: self.maxY=tY 
	
	def getExtents(self):
		tMinX=9999
		tMinY=9999
		tMaxX=-9999
		tMaxY=-9999
		# Calculates the spatial extents. ideally this information is calculated in the above for loop, but i'm lazy and this is fast.
		for p in self.records:										# for each poly
			tX = min(p.coords[...,0])									# find the min value of X
			tY = min(p.coords[...,1])									# find the min value of Y
			if tX<tMinX: tMinX=tX 								# if the current poly's min x is smaller than recorded minX, set min to current
			if tY<tMinY: tMinY=tY 								# if the current poly's min y is smaller than recorded miny, set min to current
			tX = max(p.coords[...,0])									# find the max value of X
			tY = max(p.coords[...,1])									# find the max value of Y
			if tX>tMaxX: tMaxX=tX 								# if the current poly's max x is smaller than recorded maxX, set min to current
			if tY>tMaxY: tMaxY=tY 
		return ((tMinX,tMinY),(tMaxX,tMaxY))		

	def shp_shift(self,xSize,ySize):
		''' shp_shift
		desc: 
			changes all of the x and y coordinates of the shapefile and places them within a specified coordainte range from 0-max
		params:
			x: the max x value to scale to 
			y: the max y value to scale to 
		returns:
			nothing: could easily be modified to return a copy of the shapefile instead.
			this may be very important when it comes to automatically computing a geoTiff from the output...
		'''
		# battleplan
		# 1. determine shift forward
		# 2. determine shift back
		# 3. determine scale factor
		# 4. loop each polygon
			# 4.1 shift the poly forward
			# 4.2 shift the poly back
		# 5. optional (return shifted poly)

		#amount to shift forwards is self.minX,self.minY

		for p in self.records:
			#1. shift poly forward by the minX and minY
			p.coords[...,0]+=abs(self.minX)
			p.coords[...,1]+=abs(self.minY)

		#see changes
		ext = self.getExtents()
		logging.debug("step1 poly shift extents"+str(ext))

		for p in self.records:
			#2. shift polygon back to origin
			p.coords[...,0]-=ext[0][0]
			p.coords[...,1]-=ext[0][1]

		#see changes
		ext = self.getExtents()
		logging.debug("step2 poly shift extents"+str(ext))

		for p in self.records:
			#3. stretch over new range of values
			p.coords[...,0]=(p.coords[...,0].astype(float)/ext[1][0])*xSize
			p.coords[...,1]=(p.coords[...,1].astype(float)/ext[1][1])*ySize

		#see changes
		ext = self.getExtents()
		logging.debug("step2 poly shift extents"+str(ext))