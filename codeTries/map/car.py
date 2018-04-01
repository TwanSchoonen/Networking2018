
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

		self.dest = (-1,-1)
		
		#the place
		self.pos = [randint(0,8), randint(0,6)]
		# between -1 and 1
		self.distance = [0, 0]
		
		self.chooseMovement()
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

	def chooseMovement(self):
		if not self.isAvailable:
			self.gotoLocation()
		else:
			possible_movement = [Car.NORTH, Car.EAST, Car.SOUTH, Car.WEST]
			# top
			if self.pos[1] == 0:
				possible_movement.remove(Car.NORTH)
			# right
			if (self.pos[0] == 8):
				possible_movement.remove(Car.EAST)
			# bottom
			if (self.pos[1] == 6):
				possible_movement.remove(Car.SOUTH)
			# left
			if self.pos[0] == 0:
				possible_movement.remove(Car.WEST)
			self.chooseMovementIn(possible_movement)

	def chooseMovementIn(self, list):
		choice = randint(0, len(list) - 1)
		self.movement = list[choice]
	
				
	def goto(self, data):
		data = data.split(',')
		self.dest = (int(data[0]), int(data[1]))
		print("going to " + str(self.dest))
		self.dest2 = (int(data[2]), int(data[3]))
		self.isAvailable = False
		

	def gotoLocation(self):
		x=self.pos[0]
		y=self.pos[1]
		x1=self.dest[0]
		y1=self.dest[1]
		if x<x1:
			self.movement = Car.EAST
		elif x>x1:
			self.movement = Car.WEST
		elif y<y1:
			self.movement = Car.SOUTH
		elif y>y1:
			self.movement = Car.NORTH
				
	def makeAvailable(self):
		self.isAvailable = True
		self.client.send_message("available")
		self.dest = (-1,-1)
						
	
