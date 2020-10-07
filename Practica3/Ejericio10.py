import matplotlib.pyplot as plt
import numpy as np

def velocidad(vx,vy):
    return np.sqrt(pow(vx,2)+pow(vy,2))

def K(C,A,p,m):
    return (1/2) * ((C*A*p)/m)

def Euler(px,pv,pa,v,h=0.01):
    pa = np.array([-k*v*pv[0],-10-k*v*pv[1]])
    px = px + pv*h
    pv = pv + pa*h
    v=velocidad(pv[0],pv[1])
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

r = 0.0367 # m
m = 0.145 # kg
h = 0.1
v = 50 # m/s
C = 0.5 #coeficiente de arrastre
p = 1.2 # kg/m^3

x,y =0,0 
vx,vy = np.cos(np.pi/3)*v,np.sin(np.pi/3)*v #angle de 60
pa = np.array([0,0])
px = np.array([x,y])
pv = np.array([vx,vy])

# para poder ver los dos casos   comenta k=0 y descomenta el otro
#k=0
A=np.pi*(r**2)
k=K(C,A,p,m)

(vp,vv,va,pt) = getPoint(px,pv,pa,v,0.0001,10)

#plt.subplot(2,3,5)
#print(vp)
plt.plot(vp[:,0],vp[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.grid(True)
plt.show()
