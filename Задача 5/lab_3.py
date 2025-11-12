import math as m
import numpy as np
import matplotlib.pyplot as plt




P_in=[]
t=[]
Pi_ndBm=[0,3,6,9,12,15,18,21]
Pout=[0.2,0.5,1.03,2.1,4.21,8.4,16.6,32]
Vout=[1.72,1.22,0.85,0.58,0.394,0.26,0.169,0.104]
for i in range(len(Pi_ndBm)):
    P_in.append(m.pow(10,Pi_ndBm[i]/10))
    t.append(Vout[i]*Vout[i]/50*1000)

print(P_in)
print(t)