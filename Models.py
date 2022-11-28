#!/usr/bin/env python3
from math import sin,cos,pi,atan2,acos
import numpy as np
from numpy.linalg import norm,pinv
#from Render import videoRender

l=10;m=20;n=10
def mgi(xList):
    qList = np.zeros(xList.shape)

    for i in range(xList.shape[0]):
        [x,y,z]= xList[i,:]
        
        q1=atan2(y,x)
        q3=-acos( (x**2+y**2+(z-l)**2-m**2-n**2)/(2*m*n))
        c2=((m+n*cos(q3))*norm([x,y])+n*sin(q3)*(z-l)) / ((m+n*cos(q3))**2 + (n*sin(q3))**2)
        s2=((m+n*cos(q3))*(z-l)-n*sin(q3)*norm([x,y])) / ((m+n*cos(q3))**2 + (n*sin(q3))**2)
        q2=atan2(s2,c2)

        qList[i,:]=[q1,q2,q3]
    return qList

def mdi( dxList, qList):
    
    dqList = np.zeros(dxList.shape)

    for i in range(dxList.shape[0]):
        
        [q1, q2, q3] = qList[i,:]
        jq= np.array([
                [ -n*sin(q1)*cos(q2+q3), -cos(q1)*(m*sin(q2)+n*sin(q2+q3)),                                        -cos(q1)*n*sin(q2+q3) ],
                [  n*cos(q1)*cos(q2+q3),  sin(q1)*(m*sin(q2)+n*sin(q2+q3)),                                        -sin(q1)*n*sin(q2+q3) ],
                [  0                   ,  (m*cos(q2)+n*cos(q2+q3))*sin(q1)**2+(m*cos(q2)+n*cos(q2+q3))*cos(q1)**2,  n*cos(q2+q3) ]])

        dqList[i,:]=pinv(jq) @ dxList[i,:]
   
    return dqList
