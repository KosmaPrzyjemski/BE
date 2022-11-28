#!/usr/bin/env python3
import numpy as np
#import matplotlib.pyplot as plt
from numpy.linalg import norm
import matplotlib.pyplot as plt
from Models import mgi,mdi
from Render import showCurvesX,videoRender, affichage_trajectoire
def trajetCouvre( A, B, C, v1=2, v2=1, amax=2, step=0.1):

    freq=100
    #pour avoir la position, derivé entre t1-t2 t2-t3 .... 
    t1 = v1/amax
    t3 = (v1-v2)/amax
    t5 = v2/amax
    t2 = (norm(A-B) - (t1*v1)/2 - (v1-v2)*t3/2 - v2*t3)/v1
    t4 = (norm(B-C)-t5*v2/2)/v2
    tempCommu = [t1+t2+t3,t4+t5]
    if t2<0 or t4<0 :
        raise NameError("distance trop courte")
    #print( t1, t2, t3, t4, t5 )

    #calcul des fonctions, leurs derives et leurs seconde sur le segment AB
    vectAB= (B-A)/norm(B-A)
    sFoncAB=np.concatenate([
        amax*np.arange(0, t1, step)**2/2,
        amax/2*t1**2+v1*np.arange(0, t2, step),
        amax/2*t1**2+v1*t2+v1*np.arange(0, t3, step)-amax/2*np.arange(0, t3, step)**2
        ])
    dsFoncAB=np.concatenate([
        amax*np.arange(0, t1, step),
        v1*np.ones(int(t2/step)),
        v1-amax*np.arange(0, t3, step)
        ])
    ddsFoncAB=np.concatenate([
        amax*np.ones(int(t1/step)),
        np.zeros(int(t2/step)),
        -amax*np.ones(int(t3/step)),
        ])

    #calcul des fonctions, leurs derives et leurs seconde sur le segment BC
    vectBC= (C-B)/norm(C-B)
    sFoncBC=np.concatenate([
        v2*np.arange(0, t4, step),
        v2*t4+v2*np.arange(0, t5, step)-amax/2*np.arange(0, t5, step)**2
        ])
    dsFoncBC=np.concatenate([
        v2*np.ones(int(t4/step)),
        v2-amax*np.arange(0, t5, step)
        ])
    ddsFoncBC=np.concatenate([
        np.zeros(int(t4/step)),
        -amax*np.ones(int(t5/step))
        ])

    #on concatene les segemens AB et BC
    xList=np.concatenate([
        np.ones((sFoncAB.shape[0],1))@np.atleast_2d(A)+np.atleast_2d(sFoncAB).T@np.atleast_2d(vectAB),
        np.ones((sFoncBC.shape[0],1))@np.atleast_2d(B)+np.atleast_2d(sFoncBC).T@np.atleast_2d(vectBC)
        ])
    dxList=np.concatenate([
        np.atleast_2d(dsFoncAB).T@np.atleast_2d(vectAB),
        np.atleast_2d(dsFoncBC).T@np.atleast_2d(vectBC)
        ])
    ddxList=np.concatenate([
        np.atleast_2d(ddsFoncAB).T@np.atleast_2d(vectAB),
        np.atleast_2d(ddsFoncBC).T@np.atleast_2d(vectBC)
        ])
    affichage_trajectoire(xList,dxList,ddxList,tempCommu, freq**-1)
    showCurvesX(xList, dxList, ddxList,step=freq**-1)
    qList = mgi(xList) 
    dqList = mdi(dxList,qList)
    return qList,dqList
    # return xList,dxList,ddxList,tempCommu

def valideDq(dqList):
   dqButee = 5.0
   print("les valeurs dq max atteingnable par le robot sont de "+str(dqButee)+"rad/s") 
   dqMax = dqList.max(0)
   print ("les valeurs dqMax calculé pour la trajectoire sont "+ str(dqMax))
   dqOk = True
   for dq in dqMax:
       if dq >= dqButee:
           dqOk = False
   return dqOk