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
N = 10
N_in_line = ceil( vp.sqrt(N) )

x = []
y = []
vx = []
vy = []
ax = []
ay = []
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
    ball.append(vp.sphere(pos=vp.vector(x[i],y[i],0), radius=0.5, color=vp.color.blue))