import socket


class socketcar(object):
	def __init__(self,pos):
		isAvailable=True
		clientIndex=-1
		dest=pos
		clientdest=pos
		
		self.isAvailable=isAvailable
		self.clientIndex=clientIndex
		self.pos=pos
		self.dest=dest
		self.clientdest=clientdest


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
