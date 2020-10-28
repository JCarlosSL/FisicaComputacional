import matplotlib.pyplot as plt
import numpy as np

def Aceleracion(px,r):
    ax = -px[0]/(np.power(px[0],2)+np.power(px[1],2))**1.5
    ay = -px[1]/(np.power(px[0],2)+np.power(px[1],2))**1.5
    return np.array([ax,ay])

def Euler(px,pv,pa,r,h=0.01):
    pa = Aceleracion(px,r);
    px = px + pv*h
    pv = pv + pa*h
    return (px,pv,pa) 

def getPoint(px,pv,pa,r,h=0.01,t=10):
    vp = []
    vv = []
    va = []

    pt = np.arange(0,t,h)
    for i in pt:
        (px,pv,pa) = Euler(px,pv,pa,r,h)
        #if px[0]>30: break
        if (np.power(px[0],2)+np.power(px[1],2))<=r**2: break
        vp.append(px)
        vv.append(pv)
        va.append(pa)
    return (np.array(vp),np.array(vv),
            np.array(va),np.array(pt))

#GM=1 por comodidad
                 
r = 20 # m
h = 0.1

pa = np.array([2,0])
px = np.array([20,40])

vx = np.arange(0.5,0.6,0.5)

axs = plt.subplot()
axs.set_aspect('equal')

cuerpo = plt.Circle((0,0),r,color="green",fill=True)
particula = plt.Circle((30,70),1,color="blue",fill=True)
axs.add_artist(cuerpo)
axs.add_artist(particula)

for vxi in vx:
    pv = np.array([vxi,0.3])
    (vp,vv,va,pt) = getPoint(px,pv,pa,r,h,400)
    print(vp)
    plt.plot(vp[:,0],vp[:,1],c='blue',linestyle='--')


plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.grid(True)
plt.show()
