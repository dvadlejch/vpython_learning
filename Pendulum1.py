# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:42:18 2019

@author: Dan
"""

import vpython as vp

#---- parameters
g = 1
L = 1
m = 1
theta0 = 3.1
omega0 = 0
#---- cartesian transform
x0 = L*vp.sin(theta0)
y0 = -L*vp.cos(theta0)
E0 = 1/2*m*L**2*omega0**2 + m*g*L*(1-vp.cos(theta0))
dt = 0.2

#---- graphics parameters
bob_r = 0.07
rod_r = 0.01
pivot_r = 0.2

#----- plot
vp.graph(width=400, height=250, background=vp.color.white, title='time vs position', xtitle='t', ytitle='angle', align='center')
thetaDots = vp.gdots(color=vp.color.green)
EDots = vp.gdots(color=vp.color.red)

#----- initial objects
pivot = vp.cylinder(radius=pivot_r, pos=vp.vector(0,0,-0.15), axis=vp.vector(0,0,0.3), color=vp.color.cyan)
rod = vp.cylinder(radius=rod_r, pos=vp.vector(0,0,0), axis=vp.vector(x0,y0,0), color=vp.color.cyan)
bob = vp.sphere(radius=bob_r, pos=vp.vector(x0,y0,0), color=vp.color.blue)


theta = theta0
omega = omega0
t = 0
count = 0
while t < 50:
    vp.rate(1/dt)
    
    #----integration
#    alpha = - g/L * vp.sin(theta)
#    omega_mid = omega + alpha*0.5*dt
#    theta_mid = theta + omega*0.5*dt
#    
#    alpha_mid = - g/L * vp.sin(theta_mid)
#    omega += alpha_mid*dt
#    theta += omega_mid*dt
    
    #----integration
    alpha = -g/L * vp.sin(theta)
    omega += alpha*dt
    theta += omega*dt
    
    #---- transform
    x = L*vp.sin(theta)
    y = -L*vp.cos(theta)
    E = 1/2*m*L**2*omega**2 + m*g*L*(1-vp.cos(theta))
    t += dt
    count +=1
    
    #---- movement
    rod.axis = vp.vector(x,y,0)
    bob.pos = vp.vector(x,y,0)
    
    #---- plot
    if count == 10:
        thetaDots.plot(t,theta)
        EDots.plot(t,E)
        count = 0
    