import pygame


class MapView(object):

	black = (0,0,0)
	white = (255,255,255)
	red = (255, 0, 0)
	green = (0, 255, 0)
	blue = (0, 0, 255)
	
	FONTSIZE = 20
	BACKGROUNDCOLOR = white
	
	def __init__(self, model):
		self.model = model

		self.screen = pygame.display.set_mode(model.MAPWIDTH,
											  model.MAPHEIGHT)

		self.font = pygame.font.SysFont('fontawesome5free', FONTSIZE)
		
		
	def drawBack(self):
		self.screen.fill(BACKGROUNDCOLOR)
		
	def drawMain(self):
		for idx in range(len(self.centers)):
			color = Map.centerProps[idx][0]
			pos =  Map.centerProps[idx][1]
			pygame.draw.circle(self.screen, color, pos,
							   Map.CENTERRADIUS)
			self.screen.blit(
				self.font.render(
					self.centers[idx], True, black
				), pos)
		# pygame.draw.circle(self.screen, self.c2_color, self.c2_pos, 50)
		
	# def drawCenter(self, center):
	# 	y_pos = RECTDIST
	# 	while y_pos < self.height:
	# 		x_pos = RECTDIST
	# 		while x_pos < self.width:
	# 			pygame.draw.rect(self.screen, blue, (x_pos, y_pos, RECTSIZE, RECTSIZE))
	# 			x_pos += RECTSIZE + RECTDIST
	# 		y_pos += RECTSIZE + RECTDIST

