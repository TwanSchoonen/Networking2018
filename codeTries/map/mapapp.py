#!/usr/bin/env python
import pygame
from pygame.locals import *
from mapmodel import MapModel
from mapview import MapView
from mapcontrol import MapControl

class MapApp(object):
	
	def __init__(self):	
		pygame.init()
		pygame.display.set_caption('Map with cars')
		self.model = MapModel()
		self.view = MapView(self.model)
		self.control = MapControl(self.model)

		#test -----
		# self.model.addCenter(["test", "1", "localhost", "1111"])
		# self.model.addClient(["test", "1", "2", "4", "4"])
		# self.model.cars[0][0].goto("1,2,4,4")


	def start_loop(self):
		clock = pygame.time.Clock()
		crashed = False

		while not crashed:

			#handle input
			crashed = self.control.checkEvents()

			self.model.update()
			
			#draw screen
			self.view.draw()

			#update
			pygame.display.update()
			clock.tick(60)
			
			# mousepres = pygame.mouse.get_pressed()

			# Left mouse buttom
		# if mousepres[0]:
		# 	pygame.mouse.get_pos()

		# 	if in_circle(mouse, map.c1_pos, 50):
		# 		state = 2
		# 		center = 1
		# 		map.c1_color = (0,0,0)

		# 	if in_circle(mouse, map.c2_pos, 50):
		# 		state = 2
		# 		center = 2
		# 		map.c2_color = (0,0,0)

		# if state == 1:
		# elif state == 2:
		# 	map.drawCenter(center)
		
		# pygame.draw.circle(screen, red, (x,y), 50)
		
		# pygame.draw.rect(screen, red, (10,10,50,50))


def main():
	app = MapApp()
	app.start_loop()
	pygame.quit()
	quit()

if __name__== "__main__":
	main()
  
