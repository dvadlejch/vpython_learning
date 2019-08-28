## molecular dynamics simulation

import vpython as vp
from math import ceil
# ---- scene parameters
width = 20
vp.scene.width = width*40
vp.scene.height = width*40
vp.scene.center = vp.vector(width/2, width/2, 0)
vp.scene.range = width/2
vp.scene.fov = 0.01
vp.scene.autoscale = False

# ----- simulation params
N = 5
N_in_line = ceil( vp.sqrt(N) )
wall_stiffness = 0

step_per_frame = 10
dt = 0.02
t = 0


x = []
y = []
vx = []
vy = []
ax = []
ay = []
#ax_w = []  # wall acceleration
#ay_w = []
ball = []

j = 0
i_prime = 0
for i in range(N):

    x_pos = i_prime*width/2 /N_in_line
    y_pos = j*width/2 /N_in_line
    i_prime += 1

    if i%N_in_line == (N_in_line-1):
        j += 1
        i_prime = 0


    x.append(width/4 + x_pos)
    y.append(width/4 + y_pos)
    vx.append(0)
    vy.append(0)
    ax.append(0)
    ay.append(0)
#    ax_w.append(0)
#    ay_w.append(0)
    ball.append(vp.sphere(pos=vp.vector(x[i],y[i],0), radius=0.5, color=vp.color.blue))

#----- calculation functions
def singleStep():
#---- the Verlet algorithm
    global t
    for i in range(N):
        x[i] += vx[i] * dt  +  0.5 * ax[i] * dt ** 2
        y[i] += vy[i] * dt  +  0.5 * ax[i] * dt ** 2
        vx[i] += ax[i] * 0.5 * dt
        vy[i] += ay[i] * 0.5 * dt
        computeAccel() # updating accelerations
        vx[i] += ax[i] * 0.5 * dt
        vy[i] += ay[i] * 0.5 * dt
        t += dt
    pass

def computeAccel():
    for i in range(N):
        #----- walls

        # vertical
        if x[i] < 0.5:
            ax[i] = wall_stiffness * (0.5 - x[i])
        elif x[i] > (width-0.5):
            ax[i] = wall_stiffness * (width - 0.5 - x[i])
        else:
            ax[i] = 0

        # horizontal
        if y[i] < 0.5:
            ay[i] = wall_stiffness * (0.5 - y[i])
        elif y[i] > (width - 0.5):
            ay[i] = wall_stiffness * (width - 0.5 - y[i])
        else:
            ay[i] = 0

    # particle - particle interaction, Lenard-Jones
    for i in range(N):
        for j in range(i):
            r_ij_2 = (x[j] - x[i])**2 + (y[j] - y[i])**2
            force_factor = 24*(2/(r_ij_2**3) - 1)/(r_ij_2**4)
            ax[j] += force_factor*(x[j] - x[i])
            ay[j] += force_factor * (y[j] - y[i])
            ax[i] += -ax[j]
            ay[i] += -ay[j]


    pass

# total energy calcul
def totalE():
    E = 0
    for i in range(N):
        E += 0.5*(vx[i]**2 + vy[i]**2)
    return E

# momentum calcul
def totalMom():
    px = 0
    py = 0
    for i in range(N):
        px += vx[i]
        py += vy[i]
    return px, py

#----- main simulation loop

while True:
    vp.rate(1000)

#---- calculating next position
    for i in range(step_per_frame):
        singleStep()

    # E = totalE()
    # print(E)
   # px, py = totalMom()
   # print(px, py)

#---- moving with balls
    for i in range(N):
        ball[i].pos = vp.vector(x[i], y[i], 0)
