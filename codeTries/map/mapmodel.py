import math

class MapModel(object):

	MAPWIDTH = 800
	MAPHEIGHT = 600
	
	black = (0,0,0)
	white = (255,255,255)
	red = (255, 0, 0)
	green = (0, 255, 0)
	blue = (0, 0, 255)
	
	CENTERPROPS = [
			(blue, (int(MAPWIDTH * 0.25), int(MAPHEIGHT * 0.5))),
			(red, (int(MAPWIDTH * 0.75), int(MAPHEIGHT * 0.5))),
		]

	CENTERRADIUS = 50
	RECTSIZE = 50
	RECTDIST = 10

	
	def __init__(self):

		# what center is shown, -1 is no center
		self.center = -1
		self.centers = []

	def addCenter(self, name):
		print("adding: %s" % name)
		self.centers.append(name)

	def inACenter(self, click):
		for idx in range(len(self.centers)):
			if MapModel.inCircle(click, MapModel.CENTERPROPS[idx][1]):
				print("switching to center " + str(idx) )
				self.center = idx

	@staticmethod
	def inCircle(click, point):
		return ((math.pow((click[0] - point[0]), 2)) +
				math.pow((click[1] - point[1]), 2) <
				pow(MapModel.CENTERRADIUS, 2))
