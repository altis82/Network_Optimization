#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:11:14 2019

@author: Chuan Pham
"""

import numpy as np
import matplotlib.pyplot as plt
N=3 #number of users
#channel gain matrix H
H=np.random.rand(N,N)
#print(H)
#require level
Gamma=[0.1,0.2,0.3]
#SIR level
SIR=[0.1,0.2,0.3]
#power available of users
P=np.ones(N)*0.5
#noise power at each receiver
N=np.ones(N)*0.01
SIR=[H[0,0]*P[0]/(H[2,0]*P[2]+H[1,0]*P[1]+N[0]),H[1,0]*P[1]/(H[2,0]*P[2]+H[0,0]*P[0]+N[1]),H[2,0]*P[2]/(H[1,0]*P[1]+H[0,0]*P[0]+N[2])]
print(SIR)
list_SIR=[]

Err=np.zeros((40,3))
list_SIR.append(SIR)
iter=0
#while np.max(Err)>0.000001:
for iter in range(40):
    P=(Gamma*1/np.array(SIR))*P
    SIR=[H[0,0]*P[0]/(H[2,0]*P[2]+H[1,0]*P[1]+N[0]),H[1,0]*P[1]/(H[2,0]*P[2]+H[0,0]*P[0]+N[1]),H[2,0]*P[2]/(H[1,0]*P[1]+H[0,0]*P[0]+N[2])]
    #print("\n",SIR)
    list_SIR.append(SIR)
    Err[iter,:]=np.abs(np.array(Gamma)-np.array(SIR))
    #print(Err)
    #iter+=1
    
#print(Err)
print(Err[:,0])
plt.plot((Err[:,0]))
plt.plot((Err[:,1]))
plt.plot((Err[:,2]))

plt.show()