import matplotlib.pyplot as plt
import numpy as np

def pointinit(angle,r):
    x = np.cos(angle)*r
    y = np.sin(angle)*r
    return x,y

def pointvelo(angle):
    x = -4*np.cos(angle)
    y = 4 * np.cos(angle)
    return x,y

def AceleCentri(pa,px,r):
    return -pa/r*px

def Euler(px,pv,pa,r,h=0.01):
    pa = AceleCentri(2,px,r);
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
        a=np.sqrt(np.power(pa[0],2)+np.power(pa[1],2))
        print(pa,"Fuerza",m*a)
        vp.append(px)
        vv.append(pv)
        va.append(pa)
    return (np.array(vp),np.array(vv),
            np.array(va),np.array(pt))

a = 2 # m/s
r = 8 # m
m = 5 # kg
h = 0.1
v = 4 # m/s

x,y = pointinit(np.pi/4,r)
vx,vy = pointvelo(np.pi/4)
pa = np.array([0,0])
px = np.array([x,y])
pv = np.array([vx,vy])

(vp,vv,va,pt) = getPoint(px,pv,pa,r,0.001,10)

#plt.subplot(2,3,5)
#print(vp)
plt.scatter(vp[0,0],vp[0,1],marker='o')
plt.plot(vp[:,0],vp[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.grid(True)
plt.show()
