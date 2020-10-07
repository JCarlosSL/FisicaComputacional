import matplotlib.pyplot as plt
import numpy as np

def velocidad(vx,vy):
    return np.sqrt(pow(vx,2)+pow(vy,2))

def K(C,A,p,m):
    return (1/2) * ((C*A*p)/m)

def Euler(px,pv,pa,v,h=0.01):
    v=velocidad(pv[0],pv[1])
    pa = np.array([-k*v*pv[0],-10-k*v*pv[1]])
    px = px + pv*h
    pv = pv + pa*h
    return (px,pv,pa,v) 

def getPoint(px,pv,pa,v,h=0.01,t=10):
    vp = []
    vv = []
    va = []

    pt = np.arange(0,t,h)
    for i in pt:
        (px,pv,pa,v) = Euler(px,pv,pa,v,h)
        if(px[1]<=0): break
        vp.append(px)
        vv.append(pv)
        va.append(pa)
    return (np.array(vp),np.array(vv),
            np.array(va),np.array(pt))

r = 0.5 # m
m = 1/pow(10,8) # kg
h = 0.1
v = 14 # m/s
C = 0.8 #coeficiente de arrastre
p = 1000 # kg/m^3

#ac = r*v
vx,vy = np.cos(0)*v,np.sin(0)*v #angle de 60
pa = np.array([0,-10])
px = np.array([0,1.6])
pv = np.array([vx,vy])

# para poder ver los dos casos   comenta k=0 y descomenta el otro
#k=0
A = np.pi*(r**2)
k=K(C,A,p,m)

(vp,vv,va,pt) = getPoint(px,pv,pa,v,0.01,20)

#plt.subplot(2,3,5)
#print(vp)
plt.plot(vp[:,0],vp[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.grid(True)
plt.show()
