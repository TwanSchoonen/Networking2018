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

# Get clinets' location
mapdetails.mapdetails.makeClient(13,21)
mapdetails.mapdetails.makeClient(25,20)
mapdetails.mapdetails.makeClient(41,41)

clients=mapdetails.mapdetails.getClients()

# Get cars location
mapdetails.mapdetails.makeCar(centers[0][0],centers[0][1])

cars=mapdetails.mapdetails.getCars()

plt.plot(*zip(*clients), marker='o', color='r', ls='')
plt.plot(*zip(*cars), marker='o', color='b', ls='')

plt.show()

