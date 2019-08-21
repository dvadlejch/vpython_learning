# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:34:58 2019

@author: Dan
"""

import vpython as vp

#---- parameters
g = 1
L = 1
m = 1

theta0 = 0
omega0 = 0
#---- cartesian transform
x0 = L*vp.sin(theta0)
y0 = -L*vp.cos(theta0)
#E0 = 1/2*m*L**2*omega0**2 + m*g*L*(1-vp.cos(theta0))
dt = 0.01

#---- graphics parameters
bob_r = 0.07
rod_r = 0.01
pivot_r = 0.2

#----- plot
vp.graph(width=400, height=250, background=vp.color.white, title='phase space plot', xtitle='theta', ytitle='omega', align='center', xmin=-vp.pi, xmax=vp.pi)
#thetaDots = vp.gdots(color=vp.color.green)
#EDots = vp.gdots(color=vp.color.red)
phaseDots = vp.gdots(color=vp.color.black)

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

#----- torque function
def torque(theta, omega, t):
    return -g/L*vp.sin(theta) - c_damp*omega + A_drive*vp.sin(f_drive*t)

#---- start/stop button
def start():
    global running, c_damp, A_drive, f_drive
    c_damp = 0
    A_drive = A_drive_slider.value
    f_drive = 2/3
    running = True
    
vp.button(text='start', bind=start)

def stop():
    global running
    running = False

vp.button(text='stop', bind=stop)

#----- clear plot button
def clear_plot():
    phaseDots.delete()

vp.button(text='clear plot', bind=clear_plot)

#------ slider
def adjustA_drive():
    A_drive_sliderReadout.text = format(A_drive_slider.value)

vp.scene.append_to_caption('\n\n')
A_drive_slider = vp.slider(left=10, min=0, max=2, step=.1, value=1, bind=adjustA_drive)
vp.scene.append_to_caption(' A_drive = ')
A_drive_sliderReadout = vp.wtext(text='1')

running = False
while True:
    vp.rate(1/dt)
    
    if running:
        #----integration
        alpha = torque(theta, omega, t)
        omega_mid = omega + alpha*0.5*dt
        theta_mid = theta + omega*0.5*dt
        
        alpha_mid = torque(theta_mid, omega_mid, t)
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
    #    if theta*last_theta < 0:
    #        t_zero_cross_last = t_zero_cross
    #        t_zero_cross = dt/(theta - last_theta)*theta + t - dt
    #        cross_count += 1
    #        if cross_count == 2:
    #            period = 2*(t_zero_cross - t_zero_cross_last)
    #    #---- transform
        x = L*vp.sin(theta)
        y = -L*vp.cos(theta)
        #E = 1/2*m*L**2*omega**2 + m*g*L*(1-vp.cos(theta))
        t += dt
        count +=1
        
        #---- movement
        rod.axis = vp.vector(x,y,0)
        bob.pos = vp.vector(x,y,0)
        
        #---- plot
        if count == 10:
            # throwing theta back to interval -pi to pi
            if theta > vp.pi:
                theta = theta - 2*vp.pi
            if theta < -vp.pi:
                theta = theta + 2*vp.pi
         #   thetaDots.plot(t,theta)
          #  EDots.plot(t,E)
            phaseDots.plot(theta, omega)
            count = 0
    