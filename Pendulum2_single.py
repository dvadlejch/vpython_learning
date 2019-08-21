# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 22:00:26 2019

@author: Dan
"""

import vpython as vp

#---- parameters
g = 9.81
L = 1
m = 1
theta0 = 3
omega0 = 0
#---- cartesian transform
x0 = L*vp.sin(theta0)
y0 = -L*vp.cos(theta0)
E0 = 1/2*m*L**2*omega0**2 + m*g*L*(1-vp.cos(theta0))
dt = 0.01

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
t_zero_cross = 0
cross_count = 0
while t < 10:
    vp.rate(1/dt)
    
    #----integration
    alpha = - g/L * vp.sin(theta)
    omega_mid = omega + alpha*0.5*dt
    theta_mid = theta + omega*0.5*dt
    
    alpha_mid = - g/L * vp.sin(theta_mid)
    omega += alpha_mid*dt
    last_theta = theta
    theta += omega_mid*dt
    
    #----integration
#    alpha = -g/L * vp.sin(theta)
#    omega += alpha*dt
#    
#    last_theta = theta
#    theta += omega*dt
    
    #----- finding of period
    if theta*last_theta < 0:
        t_zero_cross_last = t_zero_cross
        t_zero_cross = dt/(theta - last_theta)*theta + t - dt
        cross_count += 1
        if cross_count == 2:
            period = 2*(t_zero_cross - t_zero_cross_last)
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

print('\n theta0 = ',theta0, '  period = ', period)