# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:57:05 2019

@author: Dan
"""
from vpython import *

#movingBox = box( pos=vector(0,0,0), size=vector(.1,.1,.1), color=color.green) 
## Move a box across the scene in a straight line:
#while movingBox.pos.x < sqrt(5) and movingBox.pos.y < sqrt(5):
#    rate(10)
#    movingBox.pos.y += 0.01
#    movingBox.pos.x += 0.01

##---- setting up a plot
graph(width=400, height=250, background=color.white, title='time vs position', xtitle='t', ytitle='positon')
xDots = gdots(color=color.green)
yDots = gdots(color=color.magenta)
##----------------------------

movingSphere = sphere( pos=vector(2, 0, 0), radius=0.5, color=color.white, make_trail=True)
theta = 0
r = 2
t = 0
while theta < 5*2*pi:
	rate(50)
	x_sph = r*cos(theta)
	y_sph = r*sin(theta)
	theta += 0.05
	t += 1
	movingSphere.pos = vector(x_sph, y_sph, 0)

	#---- plotting
	xDots.plot(t,x_sph)
	yDots.plot(t,y_sph)

