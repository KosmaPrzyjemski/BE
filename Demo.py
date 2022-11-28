#!/usr/bin/env python3

import numpy as np

from Trajectoire import trajetCouvre
from Models import mgi,mdi
from Render import showCurvesQ,videoRender, affichage_trajectoire
import matplotlib.pyplot as plt

A = np.array((10,0, 0))
B = np.array((0,10, 0))
C = np.array((0, 18, 0))

freq=100

qList,dqList = trajetCouvre( A, B, C, v1=2, v2=1, step=freq**-1 )
showCurvesQ( qList, dqList, step=freq**-1 )
#print( len(xList), len(dxList), len(ddxList))
#qList = mgi( xList )
#dqList = mdi( dxList, qList )
#print(len(qList), len(dqList))

#videoRender( qList, points=[A,B,C] )



#affichage_trajectoire(xList,dxList,ddxList,tempCommu, freq**-1)
