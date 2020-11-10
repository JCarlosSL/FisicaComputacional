import numpy as np
from matplotlib.colors import Normalize
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.pylab as p
import imageio


def meshgrid_of(A):
    x = range(np.shape(A)[1])
    y = range(np.shape(A)[0])
    xx, yy = p.meshgrid(x,y)
    return xx, yy

def surf(Z, colormap=cm.RdYlGn):
    X, Y = meshgrid_of(Z) 
    C = Z

    fig = plt.figure()
    scalarMap = cm.ScalarMappable(norm=Normalize(vmin=C.min(), vmax=C.max()), cmap=colormap)
    C_colored = scalarMap.to_rgba(C)

    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z,facecolors=C_colored)
    #fig.colorbar(surf,shrink=0.5,aspect=5)
    #plt.show()
    return surf

def feval(funcName, *args):
	return eval(funcName)(*args)

def laplaceElipse(f1,a,b,h,epsilon):
    n = int(np.fix(a/h)+1)
    m = int(np.fix(b/h)+1)
    U = np.ones((n,m))
    # frontera
    vx = np.linspace(0,(m-1)*h,m)
    vy = np.linspace(0,(n-1)*h,n)
    i=0
    for x in vy:
        j=0
        for y in vx:
            U[i,j]=feval(f1,x,y)
            j+=1
        i+=1
    surf(U)

    w = 4/(2+np.sqrt(4-np.power(np.cos(np.pi/(n-1))+np.cos(np.pi/(m-1)),2)));
    rmax = 1
    while(rmax > epsilon):
        rmax=0
        for i in range(1,n-1):
            for j in range(1,m-1):
                rij = ((U[i,j+1]+U[i,j-1]+U[i+1,j]+U[i-1,j])/4)-U[i,j]
                U[i,j] = U[i,j]+w*rij
                if rmax <= abs(rij):
                    rmax = abs(rij)
    surf(U)
    plt.show()

#input a,b,h,epsilon
f1 = lambda x,y:(x-y)**2 #4.*np.cos(2.*y)  #20u(i,1)       


laplaceElipse('f1',2,4,0.2,0.01)
