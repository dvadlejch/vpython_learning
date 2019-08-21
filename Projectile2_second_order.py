# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:20:47 2019

@author: Dan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:26:46 2019

@author: Dan
"""
from vpython import *

#---- initial parameters
y0 = 10
vy0 = 0
g = -9.81
ay = g
drag_coef = .1
dt = 0.2
ball_r = 0.1
ground_thickness = .05
#----------------

##---- setting up a plot
graph(width=400, height=250, background=color.white, title='time vs position', xtitle='t', ytitle='positon', align='center')
yDots = gdots(color=color.green)
yDots.plot(0,y0)

#----scene settings
scene.center = vector(0, y0/2, 0)
scene.width = 600

#------ initial objects
ball = sphere( pos=vector(0,y0,0), radius=ball_r, color=color.cyan, make_trail=True, interval=0.1/dt)
ground = box(pos = vector(0,0,0), size=vector(20,ground_thickness,20), color=color.white)
#----------------------

#-------- moving ball
y = y0
vy = vy0
t = 0

try:
	a_air = -vy0/abs(vy0)*drag_coef*vy0**2
except:
	a_air = 0
    
while ball.pos.y > (ball_r+ground_thickness):
	rate(1/dt)
	#---calculating next pos and vel
	y_mid = y + vy*0.5*dt
	vy_mid = vy + (ay+a_air)*0.5*dt
	
    #-----calculation of the drag acceleration
	try:
		a_air_mid = -vy_mid/abs(vy_mid)*drag_coef*vy_mid**2
	except:
		a_air_mid = 0
	#---calculating next pos and vel
	y += vy_mid*dt
	vy += (ay+a_air_mid)*dt
	a_air = -vy/abs(vy)*drag_coef*vy**2
	#---moving
	ball.pos.y = y
	t += dt
	
	#----plotting
	yDots.plot(t,y)
	
print('Ball lands at t =', t, 'seconds with velocity =', vy, 'm/s')

#y_prev = y - (vy-g*dt)*dt
#v_prev = vy - g*dt
#t_prev = t - dt
#dy = v_prev*dt
#dv = g*dt
#bound = ball_r+ground_thickness
#t_imp = dt/dy * (y_prev - bound) + t_prev
#v_imp = dv/dy * (y_prev - bound) + v_prev
#print('Ball lands at t =', t_imp, 'seconds with velocity =', v_imp, 'm/s')