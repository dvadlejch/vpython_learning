# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 22:26:11 2019

@author: Dan
"""

import vpython as vp

#---- parameters
g = 1
L = 1
m = 1
c_damp = 0.5
A_drive = 0.5
f_drive = 2/3
theta0 = 0
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
#thetaDots = vp.gdots(color=vp.color.blue)
#thetaDots2 = vp.gdots(color=vp.color.red)
#EDots = vp.gdots(color=vp.color.red)
theta_difDots = vp.gdots(color=vp.color.black)

#----- initial objects
pivot = vp.cylinder(radius=pivot_r, pos=vp.vector(0,0,-0.15), axis=vp.vector(0,0,0.3), color=vp.color.cyan)
rod = vp.cylinder(radius=rod_r, pos=vp.vector(0,0,-0.1), axis=vp.vector(x0,y0,0), color=vp.color.cyan)
bob = vp.sphere(radius=bob_r, pos=vp.vector(x0,y0,-0.1), color=vp.color.blue)

rod2 = vp.cylinder(radius=rod_r, pos=vp.vector(0,0,0.1), axis=vp.vector(x0,y0,0), color=vp.color.cyan)
bob2 = vp.sphere(radius=bob_r, pos=vp.vector(x0,y0,0.1), color=vp.color.red)


theta = theta0
omega = omega0
theta2 = theta0 + 0.005
omega2 = omega0

t = 0
count = 0
#t_zero_cross = 0
#cross_count = 0

#----- torque function
def torque(theta, omega, t):
    return -g/L*vp.sin(theta) - c_damp*omega + A_drive*vp.sin(f_drive*t)

while t < 100:
    vp.rate(1/dt)
    
    #----integration
    alpha = torque(theta, omega, t)
    omega_mid = omega + alpha*0.5*dt
    theta_mid = theta + omega*0.5*dt
    
    alpha_mid = torque(theta_mid, omega_mid, t)
    omega += alpha_mid*dt
#    last_theta = theta
    theta += omega_mid*dt
    
    alpha2 = torque(theta2, omega2, t)
    omega_mid2 = omega2 + alpha2*0.5*dt
    theta_mid2 = theta2 + omega2*0.5*dt
    
    alpha_mid2 = torque(theta_mid2, omega_mid2, t)
    omega2 += alpha_mid2*dt
#    last_theta = theta
    theta2 += omega_mid2*dt
    #----integration
#    alpha = -g/L * vp.sin(theta)
#    omega += alpha*dt
#    
#    last_theta = theta
#    theta += omega*dt
    
    #----- finding of period
#    if theta*last_theta < 0:
#        t_zero_cross_last = t_zero_cross
#        t_zero_cross = dt/(theta - last_theta)*theta + t - dt
#        cross_count += 1
#        if cross_count == 2:
#            period = 2*(t_zero_cross - t_zero_cross_last)
    #---- transform
    x = L*vp.sin(theta)
    y = -L*vp.cos(theta)
#    E = 1/2*m*L**2*omega**2 + m*g*L*(1-vp.cos(theta))
    
    x2 = L*vp.sin(theta2)
    y2 = -L*vp.cos(theta2)
#    E2 = 1/2*m*L**2*omega2**2 + m*g*L*(1-vp.cos(theta2))
    t += dt
    count +=1
    
    #---- movement
    rod.axis = vp.vector(x,y,0)
    bob.pos = vp.vector(x,y,-0.1)
    rod2.axis = vp.vector(x2,y2,0)
    bob2.pos = vp.vector(x2,y2,0.1)
    
    #---- plot
    if count == 10:
        #thetaDots.plot(t,theta)
        #thetaDots2.plot(t,theta2)
#        EDots.plot(t,E)
        theta_difDots.plot(t, vp.log(abs(theta2-theta)))
        count = 0

#print('\n theta0 = ',theta0, '  period = ', period)