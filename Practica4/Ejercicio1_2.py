import matplotlib.pyplot as plt
import numpy as np

def getplot(plt,row,col,pos,x,y,labelx,labely,_title):
    plt.subplot(row,col,pos)
    plt.plot(x,y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(_title)
    plt.grid(True)

def Aceleracion(k,m,x):
    return -(k/m)*x

def EElastic(k,x):
    return (1/2)*k*pow(x,2)

def ECinetic(m,v):
    return (1/2)*m*pow(v,2)

def ETotal(u,k):
    return u+k


def PuntoMedio(pv,pa,px,t,h,k,m):
    vx = []
    vU = []
    vK = []
    vT = []
                    
    f0=0
    c=0
    w=0
    pt = np.arange(0,t,h)
    pa = Aceleracion(k,m,px)-c*pv/m+f0*np.cos(w*t)/m
    pv = pv + pa*h/2
    for s in pt:
        pa = Aceleracion(k,m,px)-c*pv/m+f0*np.cos(w*t)/m
        pv = pv + pa*h
        px = px + pv*h

        U = EElastic(k,px)
        K = ECinetic(m,pv)
        vU.append(U)
        vK.append(K)
        vT.append(U+K)

        vx.append(px)

    return (np.array(vU),np.array(vK),
            np.array(vT),np.array(vx))


k=0.1 #N/m
m = 0.2 #kg
h=0.01

x = np.array([2]) #m
v_x = np.array([0])
a_x = np.array([0])

vU,vK,vT,vx = PuntoMedio(v_x,a_x,x,20,h,k,m)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(vx,vU)
ax.plot(vx,vK)
ax.plot(vx,vT)
plt.title("U-K-T-x")
plt.grid()
plt.show()

#getplot(plt,2,2,1,vt,vx,'tiempo','espacio','x-t')
#getplot(plt,2,2,2,vt,vv,'tiempo','velocidad','v-t')
#getplot(plt,2,2,3,vt,va,'tiempo','aceleracion','a-t')
#getplot(plt,2,2,4,vx,vv,'espacio','velocidad','v-x')
#plt.show()


