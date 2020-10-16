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

def ETotal(u,v):
    return u+v


def PuntoMedio(pv,pa,px,t,h,k,m):
    vx = []
    vv = []
    va = []
                    
    f0=0.01
    c=0.05
    w=0.3
    pt = np.arange(0,t,h)
    pa = Aceleracion(k,m,px)-c*pv/m+f0*np.cos(w*t)/m
    pv = pv + pa*h/2
    for s in pt:
        pa = Aceleracion(k,m,px)-c*pv/m+f0*np.cos(w*t)/m
        pv = pv + pa*h
        px = px + pv*h
        
        vx.append(px)
        vv.append(pv)
        va.append(pa)

    return (np.array(vx),np.array(vv),
            np.array(va),np.array(pt))


k=0.1 #N/m
m = 0.2 #kg
h=0.1

x = np.array([-1]) #m
v_x = np.array([1])
a_x = np.array([0])

vx,vv,va,vt = PuntoMedio(v_x,a_x,x,20,h,k,m)


"""
fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
ax.plot(vv,vx,vt)
ax.set_xlabel('v')
ax.set_ylabel('x')
ax.set_zlabel('t')
plt.title('v-x-t')
plt.grid(True)
plt.show()
"""
getplot(plt,2,2,1,vt,vx,'tiempo','espacio','x-t')
getplot(plt,2,2,2,vt,vv,'tiempo','velocidad','v-t')
getplot(plt,2,2,3,vt,va,'tiempo','aceleracion','a-t')
getplot(plt,2,2,4,vx,vv,'espacio','velocidad','v-x')
plt.show()

