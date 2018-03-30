import math
import constants

from car import Car

class MapModel(object):

	def __init__(self):

		# what center is shown, -1 is no center
		self.center = -1
		self.centers = []
		self.cars = []

	def update(self):
		if self.center != -1:
			# only update if city is shown
			for car in self.cars[self.center]:
				car.update()


	def addCenter(self, centerData):
		print(centerData)
		print("adding: %s" % centerData[0])
		self.centers.append(centerData[0])
		list = []
		for idx in range(int(centerData[1])):
			list.append(Car(centerData[2], int(centerData[3])))
		self.cars.append(list)
		
		
	def inACenter(self, click):
		for idx in range(len(self.centers)):
			if MapModel.inCircle(click, constants.CENTERPROPS[idx][1]):
				print("switching to center " + str(idx) )
				self.center = idx

	@staticmethod
	def inCircle(click, point):
		return ((math.pow((click[0] - point[0]), 2)) +
				math.pow((click[1] - point[1]), 2) <
				pow(constants.CENTERRADIUS, 2))
