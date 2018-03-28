'''
Object handler for contructing objects in the city and give updates on cars and clients locations
Junctions locations (both x and y coords) for adding clients location and destination [7x-1:7x+1]
'''

import matplotlib.patches as patches

clients=[]
cars=[]
centers=[]
blocksize=5

class objecthandler:
	@staticmethod
	def getBlock(x,y):
		# Create a Rectangle patch
		rect = patches.Rectangle((x,y),blocksize,blocksize,linewidth=1,edgecolor='black',facecolor='none')
		return(rect)

	@staticmethod
	def getCenter():
		return(centers)

	@staticmethod
	def makeClient(pos,numberOfPassengers,dest):
		isPicked=False
		newClient=[pos,numberOfPassengers,dest,isPicked]
		clients.append(newClient)
		
	@staticmethod
	def removeClient(index):
		clients[index][0]=(-1,-1)

	@staticmethod
	def getClients():
		clientsLocations=[]
		for i in range(0,len(clients)):
			clientsLocations.append(clients[i][0])
		return(clientsLocations)

	@staticmethod
	def makeCar(center):
		pos=centers[center]
		isAvailable=True
		dest=pos
		clientIndex=-1
		newCar=[pos,isAvailable,dest,clientIndex]
		cars.append(newCar)
		

	@staticmethod
	def getCars():
		carsLocations=[]
		for i in range(0,len(cars)):
			carsLocations.append(cars[i][0])
		return(carsLocations)
		
	@staticmethod
	def changeLocation(pos,dest):
		x=pos[0]
		y=pos[1]
		if x<dest[0]:
			x+=1
		elif x>dest[0]:
			x-=1
		elif y<dest[1]:
			y+=1
		elif y>dest[1]:
			y-=1
		pos=(x,y)
		return(pos)
		
	@staticmethod
	def findNearestCar(cars,indexes,client):
		mindist=(cars[indexes[0]][0][0]-client[0])**2+(cars[indexes[0]][0][1]-client[1])**2
		mincar=indexes[0]
		for i in indexes[1:]:
			tempdist = (cars[indexes[i]][0][0]-client[0])**2+(cars[indexes[i]][0][1]-client[1])**2
			if(tempdist<mindist):
				mindist=tempdist
				mincar=indexes[i]
		return(mincar)
	
	@staticmethod
	def handleClient(clients):
		for i in range(0,len(clients)):
			if(not clients[i][3]):
				return i
		return -1
	
	@staticmethod
	def findAvailableCars():
		available=[]
		for i in range(0,len(cars)):
			if(cars[i][1]):
				available.append(i)
		return(available)

	@staticmethod
	def getNearestCenter(location):
		if(location[0]<50):
			if(location[1]<50):
				return(centers[0])
			else:
				return(centers[2])
		else:
			if(location[1]<50):
				return(centers[1])
		return(centers[3])

	@staticmethod
	def updateObjects():
		#TODO: handle cars to center connection
		nextClient=objecthandler.handleClient(clients)
		if(nextClient!=-1):
			available=objecthandler.findAvailableCars()
			if(available!=[]):
				mincar = objecthandler.findNearestCar(cars,available,clients[nextClient][0])
				cars[mincar][1]=False
				clients[nextClient][3]=True
				cars[mincar][3]=nextClient
				cars[mincar][2]=clients[nextClient][0]
		for i in range(0,len(cars)):
			cars[i][0]=objecthandler.changeLocation(cars[i][0],cars[i][2])
			if(not cars[i][1] and cars[i][0]==cars[i][2]):
				if(cars[i][0]==clients[cars[i][3]][2]):
					cars[i][1]=True
					cars[i][2]=objecthandler.getNearestCenter(cars[i][0])
					cars[i][3]=objecthandler.getNearestCenter(cars[i][0])
				else:
					cars[i][2]=clients[cars[i][3]][2]
					objecthandler.removeClient(cars[i][3])
		return(objecthandler.getClients(),objecthandler.getCars())
		
	@staticmethod
	def init():
		# Get centers location
		centers.append([15,29])
		centers.append([85,8])
		centers.append([36,71])
		centers.append([78,78])
		
		# Get clinets' location
		objecthandler.makeClient((1,1),1,(10,100))
		objecthandler.makeClient((13,21),1,(20,20))
		objecthandler.makeClient((25,20),1,(5,15))
		objecthandler.makeClient((41,41),1,(13,21))

		# Get cars location
		objecthandler.makeCar(0)
		objecthandler.makeCar(1)
		
		
