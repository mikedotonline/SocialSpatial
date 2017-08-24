import numpy as np
class Poly(object):
	''' Class Poly
	Data object that creates a polygon as a 2D numpy array
	'''
	def __init__(self, x,y,name): #need to implement the polygon name attribute.
		''' constructor
		Desc: the method takes the two lists and creates a 2xn dimensional array
		i.e. [ [2,4]
			   [5,6]]
		Param: x - a list of x values for a polygon
		Param: y - a list of y values for the same polygon

		Public variable: coords - the polygon coordinates
		Public Varibale: name   - the name of the polygon from the attribute table
		'''
		self.x = x #x coords as list
		self.y = y #y coords as list
		self.name = name # name of the polygon from shapefile
		self.coords = np.array([]).reshape(0,2)
		
		#read coordinates into numpy array
		for i in range(0,len(self.x)):
			self.coords = np.vstack([self.coords,[self.x[i],self.y[i]]])

		# logging.info(self.coords)

	def poly_shift(self, xSize, ySize):
		''' Method: poly_shift
			Desc:	returns an array of the polygon, but with the coordinates 
					translated into the space of the output surface
			Params:	xSize - the coord range to translate to, from 0-xSize
					ySize - the coord range to translate to, from 0-ySize
			Return:	a 2D numpy array of adjusted coordinates
		'''
		#strategy. 
		# 1. apply shift for polygon using absolute value of min, regardless of positive of negative
		# 2. apply shift back to origin reagrless of weather it is there or not
		# 3. stretch over new size

		#1. shift polygon over 
		self.coords[...,0]+=abs(self.coords[...,0].min())
		self.coords[...,1]+=abs(self.coords[...,1].min())

		#2. shift polygon back to origin
		self.coords[...,0]-=self.coords[...,0].min()
		self.coords[...,1]-=self.coords[...,1].min()

		#3. stretch over new range of values
		self.coords[...,0]=(self.coords[...,0].astype(float)/self.coords[...,0].ptp())*xSize
		self.coords[...,1]=(self.coords[...,1].astype(float)/self.coords[...,1].ptp())*ySize

		#4. return augmented array
		return self.coords 