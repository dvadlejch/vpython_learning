# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:56:47 2019

@author: Dan
"""

import vpython as vp

# ----- parameters using units: AU, year, sun_mass
G = 4 * vp.pi ** 2
m1 = 1
# m2 = 1/332946
# m3 = 1/332946
m2 = 0.02
m3 = 0.00002

x0 = 1
y0 = 0
vx0 = 0
vy0 = 2 * vp.pi * 1
x01 = -1.5
y01 = 0
vx01 = 0
vy01 = -2 * vp.pi * 0.8
dt = 0.001
# tol = 0.2
# ----- graphic parameters
sun_r = 0.15
earth_r = 0.05
second_planet_r = 0.05
axis_r = 0.01

# ----- objects
sun = vp.sphere(radius=sun_r, pos=vp.vector(0, 0, 0), color=vp.color.yellow)
earth = vp.sphere(radius=earth_r, pos=vp.vector(x0, y0, 0), color=vp.color.blue, make_trail=True)
sec_planet = vp.sphere(radius=second_planet_r, pos=vp.vector(x01, y01, 0), color=vp.color.black, make_trail=True)

xaxis = vp.cylinder(radius=axis_r, pos=vp.vector(-1.5, 0, 0), axis=vp.vector(3, 0, 0), color=vp.color.black)
yaxis = vp.cylinder(radius=axis_r, pos=vp.vector(0, -1.5, 0), axis=vp.vector(0, 3, 0), color=vp.color.black)

# ----- scene settings
# vp.scene.userspin = False
vp.scene.fov = 0.01
vp.scene.background = vp.color.white


##---- calculation

# ---- start button
def start():
    global running
    running = True


start = vp.button(text='start', bind=start)


# ---- stop button


def stop():
    global running
    running = False


stop = vp.button(text='stop', bind=stop)
# ----- restart button
def restart():
    global x, y, vx, vy, x1, y1, vx1, vy1, t
    earth.pos = vp.vector(x0, y0, 0)
    sec_planet.pos = vp.vector(x01, y01, 0)
    x = x0
    y = y0
    vx = vx0
    vy = vy0
    x1 = x01
    y1 = y01
    vx1 = vx01
    vy1 = vy01
    t = 0
    earth.clear_trail()
    sec_planet.clear_trail()


restart = vp.button(text='restart', bind=restart)

vp.scene.append_to_caption('\n\n')
timeReadout = vp.wtext(text='t = 0')


# --- energy
def totalE():
    return 1 / 2 * m2 * (vx ** 2 + vy ** 2) - G * m1 * m2 / (x ** 2 + y ** 2) ** (1 / 2)


x = x0
y = y0
vx = vx0
vy = vy0
x1 = x01
y1 = y01
vx1 = vx01
vy1 = vy01
t = 0

# --- acceleration calcul
x23 = x1 - x  # sec planet acts on earth
y23 = y1 - y
r233 = (x23 ** 2 + y23 ** 2) ** (3 / 2)
ax = -G * m1 / (x0 ** 2 + y0 ** 2) ** (3 / 2) * x0 + G * m3 / r233 * x23
ay = -G * m1 / (x0 ** 2 + y0 ** 2) ** (3 / 2) * y0 + G * m3 / r233 * y23

ax1 = -G * m1 / (x01 ** 2 + y01 ** 2) ** (3 / 2) * x01 - G * m2 / r233 * x23
ay1 = -G * m1 / (x01 ** 2 + y01 ** 2) ** (3 / 2) * y01 - G * m2 / r233 * y23
# dt = tol/vp.sqrt(ax**2+ay**2)
# earth.interval = 1000/dt
# rate0 = 1/dt
running = False
while True:
    #    vp.rate(rate0)
    vp.rate(0.5 / dt)

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
    # -----Euler-Richardson algorithm
    # r3 = (x**2 + y**2)**(3/2)
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

    # ---- The Verlet algorithm
    #    dt = tol/vp.sqrt(ax**2+ay**2)  # adaptive step control
    #    print(dt)
    if running:
        x += vx * dt + 0.5 * ax * dt ** 2
        y += vy * dt + 0.5 * ay * dt ** 2
        x1 += vx1 * dt + 0.5 * ax1 * dt ** 2
        y1 += vy1 * dt + 0.5 * ay1 * dt ** 2

        vx += 0.5 * ax * dt
        vy += 0.5 * ay * dt
        vx1 += 0.5 * ax1 * dt
        vy1 += 0.5 * ay1 * dt

        r3 = (x ** 2 + y ** 2) ** (3 / 2)
        x23 = x1 - x  # sec planet acts on earth
        y23 = y1 - y
        r233 = (x23 ** 2 + y23 ** 2) ** (3 / 2)
        ax = -G * m1 / r3 * x + G * m3 / r233 * x23
        ay = -G * m1 / r3 * y + G * m3 / r233 * y23
        r31 = (x1 ** 2 + y1 ** 2) ** (3 / 2)
        ax1 = -G * m1 / r31 * x1 - G * m2 / r233 * x23
        ay1 = -G * m1 / r31 * y1 - G * m2 / r233 * y23

        vx += 0.5 * ax * dt
        vy += 0.5 * ay * dt
        vx1 += 0.5 * ax1 * dt
        vy1 += 0.5 * ay1 * dt
        t += dt

        timeReadout.text = 't =' + format(t)
        #    print(x)
        # --- move
        earth.pos = vp.vector(x, y, 0)
        sec_planet.pos = vp.vector(x1, y1, 0)
