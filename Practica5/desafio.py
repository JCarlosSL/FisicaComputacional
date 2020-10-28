import matplotlib.pyplot as plt
import numpy as np

def Aceleracion(px):
    ax = -px[0]/(np.power(px[0],2)+np.power(px[1],2))**1.5
    ay = -px[1]/(np.power(px[0],2)+np.power(px[1],2))**1.5
    return np.array([ax,ay])

def Aceleracion3C(px,d):
    ax = -(px[0]+d)/((px[0]+d)**2+px[1]**2)**1.5-(px[0]-d)/((px[0]-d)**2+px[1]**2)**1.5
    ay = -px[1]/((px[0]+d)**2+px[1]**2)**1.5-px[1]/((px[0]-d)**2+px[1]**2)**1.5
    return np.array([ax,ay])

def Euler(px,pv,d,h=0.01):
    pa = Aceleracion(px) #Aceleracion3C(px,d)
    pv = pv + pa*h
    px = px + pv*h
    return (px,pv,pa) 

def getPoint(px1,pv1,pa1,d,r1,h=0.01,t=10):
    vp1 = []

    pt = np.arange(0,t,h)
    for i in pt:
        (px1,pv1,pa1) = Euler(px1,pv1,d,h)
        #if px1[0]>30: break
        if (np.power(px1[0],2)+np.power(px1[1],2))<=r1**2: break
        #if (np.power(px1[0]+d,2)+np.power(px1[1],2))<=r1**2: break
        #if (np.power(px1[0]-d,2)+np.power(px1[1],2))<=r1**2: break
        vp1.append(px1)
    return np.array(vp1)

r1 = 3 # radio planetas
d = 5  # distancia
h = 0.1

pa = np.array([0,0])
px1 = np.array([0,5.0000])
px2 = np.array([0,5.0001])

vx = np.arange(0,0.2,0.05)

axs = plt.subplot()
axs.set_aspect('equal')

cuerpo1 = plt.Circle((px1[0],px1[1]),0.2,color="blue",fill=True)
cuerpo4 = plt.Circle((px2[0],px2[1]),0.2,color="green",fill=True)
#cuerpo2 = plt.Circle((-d,0),r1,color="red",fill=True)
cuerpo3 = plt.Circle((0,0),r1,color="yellow",fill=True)
axs.add_artist(cuerpo1)
axs.add_artist(cuerpo4)
#axs.add_artist(cuerpo2)
axs.add_artist(cuerpo3)

for vxi in vx:
    pv1 = np.array([vxi,0])
    vp1 = getPoint(px1,pv1,pa,d,r1,h,100)
    vp2 = getPoint(px2,pv1,pa,d,r1,h,100)
    plt.plot(vp1[:,0],vp1[:,1],c='blue',linestyle='--')
    plt.plot(vp2[:,0],vp2[:,1],c='green',linestyle='--')


plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.grid(True)
plt.show()
