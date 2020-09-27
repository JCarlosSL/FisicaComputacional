import numpy as np

def npa(x):
    return np.array(x)

def sum(x,y):
    return x+y

def resta(x,y):
    return x-y

def euler(p,v,a,t,h=0.01,myf=sum):  
    vp=[]
    vv=[]
    va=[]

    pt = np.arange(0,t,h)
    for t in pt:
        p = myf(p,v*h)
        v = myf(v,a*h)
        vp.append(p)
        vv.append(v)
        va.append(a)
    return npa(vp),npa(vv),npa(va),npa(pt)

def DrawT_E(plt,x,y):
    plt.subplot(2,3,1)
    plt.plot(x,y)
    plt.xlabel('tiempo')
    plt.ylabel('espacio')
    plt.title('xy-t')
    plt.grid(True)

def DrawT_V(plt,x,y):
    plt.subplot(2,3,2)
    plt.plot(x,y)
    plt.xlabel('tiempo')
    plt.ylabel('velocidad')
    plt.title('t-v')
    plt.grid(True)

def DrawT_A(plt,x,y):
    plt.subplot(2,3,3)
    plt.plot(x,y)
    plt.xlabel('tiempo')
    plt.ylabel('aceleracion')
    plt.title('t-a')
    plt.grid(True)

def DrawE_V(plt,x,y):
    plt.subplot(2,3,4)
    plt.plot(x,y)
    plt.xlabel('espacio')
    plt.ylabel('velocidad')
    plt.title('espacio de faces')
    plt.grid(True)

def DrawX_Y(plt,x,y):
    plt.subplot(2,3,5)
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('x-y')
    plt.grid(True)



