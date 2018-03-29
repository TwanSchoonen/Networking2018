import pygame

from mapmodel import MapModel

class MapView(object):

	FONTSIZE = 20
	BACKGROUNDCOLOR = MapModel.white
	
	def __init__(self, model):
		self.model = model
		self.screen = pygame.display.set_mode((MapModel.MAPWIDTH,
											   MapModel.MAPHEIGHT))
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
			color = MapModel.CENTERPROPS[idx][0]
			pos = MapModel.CENTERPROPS[idx][1]
			pygame.draw.circle(self.screen, color, pos,
							   MapModel.CENTERRADIUS)
		# 	self.screen.blit(
		# 		self.font.render(
		# 			self.centers[idx], True, black
		# 		), pos)
		# pygame.draw.circle(self.screen, self.c2_color, self.c2_pos, 50)
		
	def drawCenter(self):
		y_pos = MapModel.RECTDIST
		while y_pos < MapModel.MAPHEIGHT:
			x_pos = MapModel.RECTDIST
			while x_pos < MapModel.MAPWIDTH:
				pygame.draw.rect(self.screen, MapModel.blue,
								 (x_pos, y_pos, MapModel.RECTSIZE,
								  MapModel.RECTSIZE))
				x_pos += MapModel.RECTSIZE + MapModel.RECTDIST
			y_pos += MapModel.RECTSIZE + MapModel.RECTDIST

