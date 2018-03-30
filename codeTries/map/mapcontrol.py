import pygame

from mapserver import MapServer

class MapControl(object):

	def __init__(self, model):
		self.model = model

		self.startServer()

	def startServer(self):
		MapServer('0.0.0.0', 1234, self).start_server()

	def serverEvent(self, data):
		print(data)
		stringData = data.decode('utf-8').split(', ')
		self.model.addCenter(stringData)
		
	def checkEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True

			if event.type == pygame.MOUSEBUTTONUP:
				print(pygame.mouse.get_pos())
				self.model.inACenter(pygame.mouse.get_pos())
				
		return False
