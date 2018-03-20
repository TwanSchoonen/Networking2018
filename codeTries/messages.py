class messages:
	@staticmethod
	def dequeueOrder():
		location=(1,2)
		numberOfPassengers=3
		destination=(7,7)
		return(location,numberOfPassengers,destination)
	
	@staticmethod
	def orderToCar(order):
		return(order[0],order[1],order[2])
		
