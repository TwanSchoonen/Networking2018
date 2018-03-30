import pygame
import constants

from mapmodel import MapModel

class MapView(object):

	FONTSIZE = 20
	BACKGROUNDCOLOR = constants.white
	
	def __init__(self, model):
		self.model = model
		self.screen = pygame.display.set_mode((constants.MAPWIDTH,
											   constants.MAPHEIGHT))
		self.font = pygame.font.SysFont('fontawesome5free',
										MapView.FONTSIZE)

	def draw(self):
		self.drawBack()

		if self.model.center == -1:
			self.drawMain()
		else:
			self.drawCenter()
		
	def drawBack(self):
		self.screen.fill(MapView.BACKGROUNDCOLOR)
		
	def drawMain(self):
		for idx in range(len(self.model.centers)):
			color = constants.CENTERPROPS[idx][0]
			pos = constants.CENTERPROPS[idx][1]
			pygame.draw.circle(self.screen, color, pos,
							   constants.CENTERRADIUS)
		# 	self.screen.blit(
		# 		self.font.render(
		# 			self.centers[idx], True, black
		# 		), pos)
		# pygame.draw.circle(self.screen, self.c2_color, self.c2_pos, 50)
		
	def drawCenter(self):
		y_pos = constants.RECTDIST
		while y_pos < constants.MAPHEIGHT:
			x_pos = constants.RECTDIST
			while x_pos < constants.MAPWIDTH:
				pygame.draw.rect(self.screen, constants.blue,
								 (x_pos, y_pos, constants.RECTSIZE,
								  constants.RECTSIZE))
				x_pos += constants.RECTSIZE + constants.RECTDIST
			y_pos += constants.RECTSIZE + constants.RECTDIST

		cars = self.model.cars[self.model.center]

		for car in cars:
			pygame.draw.circle(self.screen, constants.black, car.getMapPos(),
							   int(constants.RECTDIST / 2))
