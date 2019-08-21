# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:38:12 2019

@author: Dan
"""

import vpython as vp

#----- parameters using units: AU, year, sun_mass
G = 4*vp.pi**2 
m1 = 1
m2 = 1/332946

x0 = 0.58
y0 = 0
vx0 = 0
vy0 = 2*vp.pi*1.84317
#dt = 0.01
tol = 0.2
#----- graphic parameters
sun_r = 0.15
earth_r = 0.05
axis_r = 0.01

#----- objects
sun = vp.sphere(radius=sun_r, pos=vp.vector(0,0,0), color=vp.color.yellow)
earth = vp.sphere(radius=earth_r, pos=vp.vector(x0,y0,0), color=vp.color.blue, make_trail=True, interval=10)

xaxis = vp.cylinder(radius=axis_r, pos=vp.vector(-1.5,0,0), axis=vp.vector(3,0,0), color=vp.color.black)
yaxis = vp.cylinder(radius=axis_r, pos=vp.vector(0,-1.5,0), axis=vp.vector(0,3,0), color=vp.color.black)

#----- scene settings
#vp.scene.userspin = False
vp.scene.fov = 0.01
vp.scene.background = vp.color.white



##---- calculation

#--- energy
def totalE():
    return 1/2*m2*(vx**2+vy**2) - G*m1*m2/(x**2 + y**2)**(1/2)

x = x0
y = y0
vx = vx0
vy = vy0
t = 0

ax = -G*m1/(x0**2 + y0**2)**(3/2) * x0
ay = -G*m1/(x0**2 + y0**2)**(3/2) * y0
dt = tol/vp.sqrt(ax**2+ay**2)
earth.interval = 1000/dt
rate0 = 1/dt
while t < 76:
#    vp.rate(rate0)
    vp.rate(20)
    
#    r3 = (x**2 + y**2)**(3/2)
    
#    #---Euler algorithm
  #  r3 = (x**2 + y**2)**(3/2)
#    ax = -G*m1/r3 * x
#    ay = -G*m1/r3 * y
#    
#    print('E before = ',totalE())
##    print(ax)
##    print(ay)
#    
#    vx += ax*dt
#    vy += ay*dt
#    x += vx*dt
#    y += vy*dt
#    t += dt
#    
#    print('E after = ',totalE())
#    #---------------------------
#    print('E before = ',totalE())
    #-----Euler-Richardson algorithm
    #r3 = (x**2 + y**2)**(3/2)
#    ax = -G*m1/r3 * x
#    ay = -G*m1/r3 * y
#    
#    vx_mid = vx + ax*0.5*dt
#    vy_mid = vy + ay*0.5*dt
#    x_mid = x + vx_mid*0.5*dt
#    y_mid = y + vy_mid*0.5*dt
#    
#    ax_mid = -G*m1/r3 * x_mid
#    ay_mid = -G*m1/r3 * y_mid
#    
#    vx += ax_mid*dt
#    vy += ay_mid*dt
#    x += vx_mid*dt
#    y += vy_mid*dt
#    t += dt
    
    #---- The Verlet algorithm
    dt = tol/vp.sqrt(ax**2+ay**2)  # adaptive step control
#    print(dt)
    
    x += vx*dt + 0.5*ax*dt**2
    y += vy*dt + 0.5*ay*dt**2
    
    vx += 0.5*ax*dt
    vy += 0.5*ay*dt
    
    r3 = (x**2 + y**2)**(3/2)
    ax = -G*m1/r3 * x
    ay = -G*m1/r3 * y
    
    vx += 0.5*ax*dt
    vy += 0.5*ay*dt
    t += dt
#    print(x)
    #--- move
    earth.pos = vp.vector(x,y,0)

#sun.delete()
#earth.clear_trail()
#earth.delete()
