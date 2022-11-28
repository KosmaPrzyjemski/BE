#!/usr/bin/env python3
from math import sin,cos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.offsetbox import AnchoredText

l=1;m=1;n=1
def videoRender(qList, points=[]):
    traceX=[]
    traceY=[]
    traceZ=[]
    fig = plt.figure()
    points=np.array(points).T
    for i in range(qList.shape[0]):
        q1,q2,q3=qList[i,:]
        t01=np.array([
            [cos(q1),-sin(q1),0,0],
            [sin(q1),cos(q1),0,0],
            [0,0,1,l],
            [0,0,0,1]])
        t12=np.array([
            [cos(q2),-sin(q2),0,0],
            [0,0,-1,0],
            [sin(q2),cos(q2),0,0],
            [0,0,0,1]])
        t23=np.array([
                [cos(q3),-sin(q3),0,m],
                [sin(q3),cos(q3),0,0],
                [0,0,1,0],
                [0,0,0,1]
            ])
        t34=np.array(
            [n,0,0,1]
        )
        traceX.append((t01@t12@t23@t34)[0])
        traceY.append((t01@t12@t23@t34)[1])
        traceZ.append((t01@t12@t23@t34)[2])
        ax = fig.add_subplot(projection='3d')
        ax.set_xlim3d(-2,2)
        ax.set_ylim3d(-2,2)
        ax.set_zlim3d(0,3)
        ax.dist=7
        ax.set_axis_off()
        
        pt=np.zeros((3,5))
        
        
        pt[:,0]=np.array([0,0,0])
        pt[:,1]=t01[0:3,3]
        pt[:,2]=(t01@t12)[0:3,3]
        pt[:,3]=(t01@t12@t23)[0:3,3]
        pt[:,4]=(t01@t12@t23@t34)[0:3]
        ax.plot(pt[0,:],pt[1,:],pt[2,:],"k",linewidth=3)
        ax.plot(traceX,traceY,traceZ,"r")
        ax.plot(points[0],points[1],points[2],"b+")
        fig.savefig('frames/%.5d.png'%i)
        fig.clear()

def showCurvesX( xList, dxList, ddxList, block=True, step=1):

    plt.subplot(2,2,1)
    plt.title("Position repere outil")
    plt.plot(np.arange(xList.shape[0])*step, xList[:,0], label="x")
    plt.plot(np.arange(xList.shape[0])*step, xList[:,1], label='y')
    plt.plot(np.arange(xList.shape[0])*step, xList[:,2], label='z')
    plt.legend(bbox_to_anchor=(1.0, 1.0))

    plt.subplot(2,2,2)
    plt.title("Vitesse repere outil")
    plt.plot(np.arange(dxList.shape[0])*step, dxList[:,0], label="x")
    plt.plot(np.arange(dxList.shape[0])*step, dxList[:,1], label="y")
    plt.plot(np.arange(dxList.shape[0])*step, dxList[:,2], label="z")
    plt.legend(bbox_to_anchor=(1.0, 1.00))

    plt.subplot(2,2,3)
    plt.title("Acceleration repere outil")
    plt.plot(np.arange(ddxList.shape[0])*step, ddxList[:,0], label="x")
    plt.plot(np.arange(ddxList.shape[0])*step, ddxList[:,1], label="y")
    plt.plot(np.arange(ddxList.shape[0])*step, ddxList[:,2], label="z")
    plt.legend(bbox_to_anchor=(1.0, 1.00))

    plt.subplot(2,2,4)
    plt.title("Vitesse absolue outil")
    plt.tight_layout(pad=2.0)
    plt.plot(np.arange(dxList.shape[0])*step, np.linalg.norm(dxList,axis=1))

    plt.show( block=block )
def showCurvesQ(qList, dqList, block=True, step=1):
    plt.subplot(1,2,1)
    plt.title("Position repere config")
    plt.plot(np.arange(qList.shape[0])*step, qList[:,0], label="q1")
    plt.plot(np.arange(qList.shape[0])*step, qList[:,1], label="q2")
    plt.plot(np.arange(qList.shape[0])*step, qList[:,2], label="q3")
    plt.legend(bbox_to_anchor=(1.1, 1.05))

    plt.subplot(1,2,2)
    plt.title("Vitesse repere config")
    plt.plot(np.arange(dqList.shape[0])*step, dqList[:,0], label="q1")
    plt.plot(np.arange(dqList.shape[0])*step, dqList[:,1], label="q2")
    plt.plot(np.arange(dqList.shape[0])*step, dqList[:,2], label="q3")
    plt.legend(bbox_to_anchor=(1.1, 1.05))
    plt.tight_layout(pad=3.0)
    plt.show( block=block )
   
def affichage_trajectoire(xList,dxList,ddxList,tempCommu, step):

    plt.subplot(2,3,1)
    plt.title("s")
    plt.plot(np.arange(xList.shape[0])*step, xList, label="x")
    plt.grid(True)
    plt.xlabel('time [s] \n Temps pour aller de A à B ='+str(tempCommu[0])+'s\n Temps pour aller de B à C = '+str(tempCommu[1])+'s')
    
    plt.subplot(2,3,2)
    plt.title("ds")
    plt.plot(np.arange(dxList.shape[0])*step, dxList, label="x")
    plt.grid(True)

    plt.subplot(2,3,3)
    plt.title("dds")
    plt.plot(np.arange(ddxList.shape[0])*step, ddxList, label="x")
    plt.grid(True)
    plt.show()
