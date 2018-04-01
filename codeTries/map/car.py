
import constants

from random import randint
from carclient import CarClient

class Car(object):

	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3

	def __init__(self, address, port):

		# client takes car of center input
		self.client = CarClient(address, port, self)
		# if the car is pickingup a client
		self.isAvailable = True
		
		#the place
		self.pos = [randint(0,8), randint(0,6)]
		# between -1 and 1
		self.distance = [0, 0]
		
		self.chooseRandomMovement()
		# self.clientdest=clientdest
	
	def update(self):
		self.updateDistance()
		self.move()

	def updateDistance(self):
		#choose random movement at the corners
		if self.distance[0] >= 1:
			self.updatePos(0, 1)

		if self.distance[0] <= -1:
			self.updatePos(0, -1)

		if self.distance[1] >= 1:
			self.updatePos(1, 1)

		if self.distance[1] <= -1:
			self.updatePos(1, -1)
			
	def updatePos(self,idx, amount):
		self.pos[idx] = self.pos[idx] + amount
		self.distance[idx] = 0
		self.chooseMovement()

	def move(self):
		# move north
		if self.movement == Car.NORTH:
			self.distance[1] = self.distance[1] - constants.CARSPEED

		# move east
		elif self.movement == Car.EAST:
			self.distance[0] = self.distance[0] + constants.CARSPEED

		# move south
		elif self.movement == Car.SOUTH:
			self.distance[1] = self.distance[1] + constants.CARSPEED

		# move west
		elif self.movement == Car.WEST:
			self.distance[0] = self.distance[0] - constants.CARSPEED

	def chooseRandomMovement(self):
		# # in left uppper corner
		# if self.pos[0] == 0 and self.pos[1] == 0:
		# 	chooseMovementIn([Car.EAST, Car.SOUTH])
		# on top
		if self.pos[1] == 0:
			self.chooseMovementIn([Car.EAST, Car.SOUTH, Car.WEST])
		# right
		elif (self.pos[0] == 8):
			self.chooseMovementIn([Car.NORTH, Car.SOUTH, Car.WEST])
		# # bottom
		elif (self.pos[1] == 6):
			self.chooseMovementIn([Car.NORTH, Car.EAST, Car.WEST])
		# left
		elif self.pos[0] == 0:
			self.chooseMovementIn([Car.NORTH, Car.EAST, Car.SOUTH])
		# elif (self.getMapPos()[0] >= constants.MAPWIDTH and
		# self.getMapPos()[0] >= constants.MAPWIDTH):
		# 	pass
		# elif self.getMapPos()[0] >= constants.MAPWID:
		else:
			self.chooseMovementIn([Car.NORTH, Car.EAST, Car.SOUTH, Car.WEST])

	def chooseMovementIn(self, list):
		choice = randint(0, len(list) - 1)
		self.movement = list[choice]
	
				
	def goto(self, data):
		data = data.split(',')
		self.dest1 = (data[0], data[1])
		print("going to " + str(self.clientLocation))
		self.dest2 = (data[2], data[1])
		self.isAvailable = False
		

	def changeLocation(self):
		if(self.pos!=self.dest):
			x=self.pos[0]
			y=self.pos[1]
			x1=self.dest[0]
			y1=self.dest[1]
			if x<x1:
				x+=1
			elif x>x1:
				x-=1
			elif y<y1:
				y+=1
			elif y>y1:
				y-=1
				self.pos=(x,y)
		return(self.pos)
	
	def setNewDest(self,isAvailable,clientIndex,dest,clientdest):
		self.isAvailable = isAvailable
		self.dest = dest
		self.clientdest=clientdest
		self.clientIndex=clientIndex