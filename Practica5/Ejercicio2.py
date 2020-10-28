import matplotlib.pyplot as plt
import numpy as np
import math

def Aceleracion(px):
    ax = -px[0]/np.power(np.power(px[0],2)+np.power(px[1],2),1.5)
    ay = -px[1]/np.power(np.power(px[0],2)+np.power(px[1],2),1.5)
    return np.array([ax,ay])

def Euler(px,pv,h=0.01):
    pa = Aceleracion(px);
    px = px + pv*h
    pv = pv + pa*h
    return (px,pv,pa) 

def getPoint(px,pv,pa,r,h=0.01,t=10):
    vp = []
    vv = []
    va = []

    pt = np.arange(0,t,h)
    for i in pt:
        (px,pv,pa) = Euler(px,pv,h)
        vp.append(px)
        #vv.append(pv)
        #va.append(pa)
        if px[0]>20: break
        if (pow(px[0],2)+pow(px[1],2))<=pow(r,2): break
    return (np.array(vp),np.array(vv),
            np.array(va),np.array(pt))

r = 2 # m
h = 0.1

pa = np.array([0,0])
px = np.array([3,4])

vx = np.arange(0,0.55,0.05)

axs = plt.subplot()
axs.set_aspect('equal')

cuerpo = plt.Circle((0,0),r,color="green",fill=True) #fill =0
particula = plt.Circle((3,4),0.2,color="blue",fill=True) #fill =0
axs.add_artist(cuerpo)
axs.add_artist(cuerpo)

for vxi in vx:
    pv = np.array([vxi,0.1])
    (vp,vv,va,pt) = getPoint(px,pv,pa,r,h,400)
    print(pa)
    plt.plot(vp[:,0],vp[:,1],c='blue',linestyle='--')


plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.grid(True)
plt.show()
