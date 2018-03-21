from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import numpy as np
import mapdetails

# Create figure and axes
fig,ax = plt.subplots(1)

# Make city blocks
for x in range(1,95,7):
	for y in range(1,95,7): 
		# Create a Rectangle patch
		rect = mapdetails.mapdetails.getBlock(x,y)
		# Add the patch to the Axes
		ax.add_patch(rect)

# Color city areas
ax.fill_between((0,50),(50,50),facecolor='green', alpha=0.1)
ax.fill_between((0,50),(50,50),(100,100),facecolor='yellow', alpha=0.1)
ax.fill_between((50,100),(50,50),facecolor='orange', alpha=0.1)
ax.fill_between((50,100),(50,50),(100,100),facecolor='purple', alpha=0.1)

# Mark car centers
centers = mapdetails.mapdetails.getCenter()
ax.fill_between((centers[0][0],centers[0][0]+5),(centers[0][1],centers[0][1]),(centers[0][1]+5,centers[0][1]+5),facecolor='blue')
ax.fill_between((centers[1][0],centers[1][0]+5),(centers[1][1],centers[1][1]),(centers[1][1]+5,centers[1][1]+5),facecolor='blue')
ax.fill_between((centers[2][0],centers[2][0]+5),(centers[2][1],centers[2][1]),(centers[2][1]+5,centers[2][1]+5),facecolor='blue')
ax.fill_between((centers[3][0],centers[3][0]+5),(centers[3][1],centers[3][1]),(centers[3][1]+5,centers[3][1]+5),facecolor='blue')

# Set map boundaries
axes = plt.gca()
axes.set_xlim([0,100])
axes.set_ylim([0,100])

clients=mapdetails.mapdetails.getClients()
cars=mapdetails.mapdetails.getCars()

# Get clinets' location
mapdetails.mapdetails.makeClient(13,21)
mapdetails.mapdetails.makeClient(25,20)
mapdetails.mapdetails.makeClient(41,41)

# Get cars location
mapdetails.mapdetails.makeCar(centers[0][0],centers[0][1])

def draw():
	# Make city blocks
	for x in range(1,95,7):
		for y in range(1,95,7): 
			# Create a Rectangle patch
			rect = mapdetails.mapdetails.getBlock(x,y)
			# Add the patch to the Axes
			ax.add_patch(rect)

	# Color city areas
	ax.fill_between((0,50),(50,50),facecolor='green', alpha=0.1)
	ax.fill_between((0,50),(50,50),(100,100),facecolor='yellow', alpha=0.1)
	ax.fill_between((50,100),(50,50),facecolor='orange', alpha=0.1)
	ax.fill_between((50,100),(50,50),(100,100),facecolor='purple', alpha=0.1)

	# Mark car centers
	centers = mapdetails.mapdetails.getCenter()
	ax.fill_between((centers[0][0],centers[0][0]+5),(centers[0][1],centers[0][1]),(centers[0][1]+5,centers[0][1]+5),facecolor='blue')
	ax.fill_between((centers[1][0],centers[1][0]+5),(centers[1][1],centers[1][1]),(centers[1][1]+5,centers[1][1]+5),facecolor='blue')
	ax.fill_between((centers[2][0],centers[2][0]+5),(centers[2][1],centers[2][1]),(centers[2][1]+5,centers[2][1]+5),facecolor='blue')
	ax.fill_between((centers[3][0],centers[3][0]+5),(centers[3][1],centers[3][1]),(centers[3][1]+5,centers[3][1]+5),facecolor='blue')

	# Set map boundaries
	axes = plt.gca()
	axes.set_xlim([0,100])
	axes.set_ylim([0,100])

	clients=mapdetails.mapdetails.getClients()
	cars=mapdetails.mapdetails.getCars()

def init():
	plt.plot(*zip(*clients), marker='o', color='r', ls='')
	plt.plot(*zip(*cars), marker='o', color='b', ls='')
	return ax,

def changeLocation(arr,index,dest):
	elem=arr[index]
	x=elem[0]
	y=elem[1]
	if x<dest[0]:
		x+=1
	elif x>dest[0]:
		x-=1
	elif y<dest[1]:
		y+=1
	elif y>dest[1]:
		y-=1
	elem=(x,y)
	arr[index]=elem

# animation function.  This is called sequentially
def animate(i):
	ax.clear()
	draw()
	
	#TODO: queue for destination for car after picking up client, getOrder returns client's location and saves destination, send car from list of cars
	if(cars[0]!=clients[0]):
		changeLocation(cars,0,clients[0])
	else:
		clients[0]=(20,60)
	plt.plot(*zip(*clients), marker='o', color='r', ls='')
	plt.plot(*zip(*cars), marker='o', color='b', ls='')
	return ax,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=20, interval=2, blit=True)

plt.show()
