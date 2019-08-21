# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:55:33 2019

@author: Dan
"""

from vpython import *

print('Hello, GlowScript-VPython!')
box( pos=vector(1,0,0), size=vector(.5,.3,.2), color=vector(.7, .1, .7) )
box( pos=vector(-.5, -1, 0), size=vector(0.2, .3, .5), color=color.blue )
box( pos=vector(0, 1, 1), size=vector(0.3, .1, .5), color=color.green )

sphere( radius=0.25, pos=vector(-1,0,0), color=color.cyan )
sphere( radius=0.1, pos=vector(.5, -1, -1), color=color.magenta )

cylinder( radius=0.1, axis=vector(0,1.5,0), pos=vector(0,0,0), color=color.cyan )

#----axes------
xaxis = cylinder( radius=.01, axis=vector(10,0,0), pos=vector(-5,0,0), color=vector(1,.85,.85) ) # x-axis
yaxis = cylinder( radius=xaxis.radius, axis=vector(0,10,0), pos=vector(0,-5,0), color=xaxis.color ) # y-axis
zaxis = cylinder( radius=xaxis.radius, axis=vector(0,0,10), pos=vector(0,0,-5), color=xaxis.color ) # z-axis

#-----dumbbell------------
bar = cylinder( radius=0.1, axis=vector(1,0,0), pos=vector(-.5,-3,0), color=color.cyan )
sph1 = sphere( radius=bar.radius*3, pos=bar.pos, color=bar.color )
sph2 = sphere( radius=bar.radius*3, pos=bar.pos + bar.axis, color=bar.color )

scene.background = vector(0.82, 0.92, 1)
scene.range = 5


#-----table----------
tablex = 4
tabley = -2
tablez = -1
tableLength = 3.5
tableWidth = 2
tableHeight = 1.5
legRadius = 0.05*tableWidth
tableColor = color.green

tableTop = box( pos=vector(tablex,tabley,tablez), size=vector(tableLength,tableWidth, 0.1*tableHeight), color=tableColor)
tableLeg_1 = cylinder( radius=legRadius, axis=vector(0,0,tableHeight), pos=vector(tablex+0.4*tableLength, tabley+0.4*tableWidth, tablez), color=tableColor)
tableLeg_2 = cylinder( radius=tableLeg_1.radius, axis=tableLeg_1.axis, pos=vector(tablex-0.4*tableLength, tabley+0.4*tableWidth, tablez), color=tableLeg_1.color)
tableLeg_3 = cylinder( radius=tableLeg_1.radius, axis=tableLeg_1.axis, pos=vector(tablex+0.4*tableLength, tabley-0.4*tableWidth, tablez), color=tableLeg_1.color)
tableLeg_4 = cylinder( radius=tableLeg_1.radius, axis=tableLeg_1.axis, pos=vector(tablex-0.4*tableLength, tabley-0.4*tableWidth, tablez), color=tableLeg_1.color)