'''
Object handler for contructing objects in the city and give updates on cars and clients locations
Junctions locations (both x and y coords) for adding clients location and destination [7x-1:7x+1]
'''

import matplotlib.patches as patches
import socketcar

clients=[]
cars=[]
centers=[]
blocksize=5

class objecthandler(object):
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
	
	
	def makeCar(self,center):
		pos=(centers[center][0],centers[center][1])
		newCar=socketcar.socketcar(pos)
		cars.append(newCar)
		
	@staticmethod
	def getCars():
		carsLocations=[]
		for car in cars:
			carsLocations.append(car.pos)
		return(carsLocations)
		
	@staticmethod
	def findNearestCar(cars,indexes,client):
		mindist=99999
		for car in cars:
			carpos = car.pos
			tempdist = (carpos[0]-client[0])**2+(carpos[1]-client[1])**2
			if(tempdist<mindist):
				mindist=tempdist
				mincar=car
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
		for car in cars:
			if(car.isAvailable):
				available.append(car)
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
				mincar = objecthandler.findNearestCar(available,available,clients[nextClient][0])
				socketcar.socketcar.setNewDest(mincar,False,nextClient,clients[nextClient][0],clients[nextClient][2])
				clients[nextClient][3]=True
		for car in cars:
			socketcar.socketcar.changeLocation(car)
			
			if(not car.isAvailable and car.pos==car.dest):
				if(car.pos==car.clientdest):
					nearestCenter=objecthandler.getNearestCenter(car.pos)
					socketcar.socketcar.setNewDest(car,True,-1,nearestCenter,nearestCenter)
				else:
					car.dest=car.clientdest
					objecthandler.removeClient(car.clientIndex)
					
		
		return(objecthandler.getClients(),objecthandler.getCars())
		

		
	def init(self):
		# Get centers location
		centers.append([15,29])
		centers.append([85,8])
		centers.append([36,71])
		centers.append([78,78])
		
		# Get clinets' location
		objecthandler.makeClient((1,1),1,(8,77))
		objecthandler.makeClient((13,21),1,(20,20))
		objecthandler.makeClient((25,20),1,(7,15))
		objecthandler.makeClient((41,41),1,(13,21))

		# Get cars location
		objecthandler().makeCar(0)
		objecthandler().makeCar(1)
		
		
