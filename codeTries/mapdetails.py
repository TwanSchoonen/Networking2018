import matplotlib.patches as patches

clients=[]
cars=[]
blocksize=5

class mapdetails:
	@staticmethod
	def getBlock(x,y):
		# Create a Rectangle patch
		
		rect = patches.Rectangle((x,y),blocksize,blocksize,linewidth=1,edgecolor='black',facecolor='none')
		return(rect)

	@staticmethod
	def getCenter():
		# Get centers location
		center0=(15,29)
		center1=(85,8)
		center2=(36,71)
		center3=(78,78)
		return(center0,center1,center2,center3)

	@staticmethod
	def makeClient(x,y):
		clients.append((x,y))

	@staticmethod
	def getClients():
		return(clients)

	@staticmethod
	def makeCar(x,y):
		cars.append((x,y))

	@staticmethod
	def getCars():
		return(cars)