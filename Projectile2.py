# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:53:45 2019

@author: Dan
"""

from vpython import *

#----initial parameters
x0 = 0
y0 = 1
#v0 = 50
#theta = 45
#theta = theta/180*pi
#vx0 = v0*cos(theta)
#vy0 = v0*sin(theta)
drag_coef = 0.001
g = 9.81
dt = 0.005
ball_r = 1
ground_thickness = .05


#---- creating a button
def launch():
    print('Launching the projectile!!')
    
    #----initial parameters 
    global running, x0, y0, v0, theta, vx0, vy0, drag_coef, x, y, vx, vy, t
    x0 = 0
    y0 = 1
    v0 = speedSlider.value
    theta = angleSlider.value
    theta = theta/180*pi
    vx0 = v0*cos(theta)
    vy0 = v0*sin(theta)
    drag_coef = dragSlider.value
    x = x0
    y = y0
    vx = vx0
    vy = vy0
    t = 0


    running = True

button(text='Launch', bind=launch)

#---- restart button
def restart_button():
    ball.pos.x = x0
    ball.pos.y = y0
    ball.clear_trail()

button(text='Restart', bind=restart_button)

#------ angle slider
def adjustAngle():
    angleSliderReadout.text = format(angleSlider.value) + 'degrees'
    
scene.append_to_caption('\n\n')
angleSlider = slider(left=10, min=0, max=90, step=1, value=45, bind=adjustAngle)
scene.append_to_caption(' angle = ')
angleSliderReadout = wtext(text="45 degrees")

#------ initial speed slider
def adjustSpeed():
    speedSliderReadout.text = format(speedSlider.value) + 'm/s'
    
scene.append_to_caption('\n\n')
speedSlider = slider(left=10, min=0, max=50, step=1, value=25, bind=adjustSpeed)
scene.append_to_caption(' speed = ')
speedSliderReadout = wtext(text='25 m/s')

#------ drag constant slider
def adjustDrag():
    dragSliderReadout.text = format(dragSlider.value) + '1/m'
    
scene.append_to_caption('\n\n')
dragSlider = slider(left=10, min=0, max=1, step=0.005, value=0, bind=adjustDrag)
scene.append_to_caption(' drag coefficient = ')
dragSliderReadout = wtext(text='0 1/m')

##----scene settings
scene.center = vector(75, 20, 0)
scene.width = 600

#------ initial objects
ball = sphere( pos=vector(x0,y0,0), radius=ball_r, color=color.cyan, make_trail=True, interval=0.01/dt)
#ball = sphere( pos=vector(x0,y0,0), radius=ball_r, color=color.cyan)
ground = box(pos = vector(0,0,0), size=vector(300,ground_thickness,300), color=color.white)
#----------------------

#---- initial conditions
#x = x0
#y = y0
#vx = vx0
#vy = vy0
t = 0

h_max = 0
#---forever loop
running = False
while True:
    rate(1/dt)

    if running:
        ##---integrating
        # acceleration at the start of the interval
        ax_drag = -drag_coef*sqrt(vx**2+vy**2)*vx
        ay_drag = -drag_coef*sqrt(vx**2+vy**2)*vy
        ax = ax_drag
        ay = -g + ay_drag
        # position and velocity in the middle of the interval
        x_mid = x + vx*0.5*dt
        vx_mid = vx + ax*0.5*dt
        y_mid = y + vy*0.5*dt
        vy_mid = vy + ay*0.5*dt
        # acceleration in the middle of the interval
        ax_drag_mid = -drag_coef*sqrt(vx_mid**2+vy_mid**2)*vx_mid
        ay_drag_mid = -drag_coef*sqrt(vx_mid**2+vy_mid**2)*vy_mid
        ax_mid = ax_drag_mid
        ay_mid = -g + ay_drag_mid
        # position and velocity at the end of the interval
        x += vx_mid*dt
        vx += ax_mid*dt
        y += vy_mid*dt
        vy += ay_mid*dt
        t += dt
        #---- searching for h_max
        if h_max < y:
            h_max = y
            
        #----moving
        ball.pos.x = x
        ball.pos.y = y

        if ball.pos.y <= (ball_r+ground_thickness):
            running = False
            print('The landing time = {:.2f}'.format(t), 'landing distance = {:.2f}'.format(x), 'and projectile maximum height = {:.2f}'.format(h_max))

    


