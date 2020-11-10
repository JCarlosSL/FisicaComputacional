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

def laplace(f1,f2,f3,f4,a,b,h,epsilon):
    n = int(np.fix(a/h)+1)
    m = int(np.fix(b/h)+1)

    pp = ((a*(feval(f1,0)+feval(f2,0))+ b*(feval(f3,0)+feval(f4,0)))/(2*a+2*b))
    U = pp*np.ones((n,m))*.9

    # frontera
    x = np.linspace(0,(m-1)*h,m)
    y = np.linspace(0,(n-1)*h,n)
    U[0,:] = feval(f3,x)
    U[-1,:] = feval(f4,x)
    U[:,0] = feval(f1,y)
    U[:,-1] = feval(f2,y)
    
    U[0,0] = (U[0,1]+U[1,0])/2
    U[0,-1] = (U[0,-2]+U[1,-1])/2
    U[-1,0] = (U[-2,0]+U[-1,1])/2
    U[-1,-1] = (U[-2,-1]+U[-1,-2])/2
   
    #omega
    w = 4/(2+np.sqrt(4-np.power(np.cos(np.pi/(n-1))+np.cos(np.pi/(m-1)),2)));
    rmax = 1
    f=0
    while(rmax > epsilon):
        rmax=0
        for i in range(1,n-1):
            for j in range(1,m-1):
                rij = ((U[i,j+1]+U[i,j-1]+U[i+1,j]+U[i-1,j])/4)-U[i,j]
                U[i,j] = U[i,j]+w*rij
                if rmax <= abs(rij):
                    rmax = abs(rij)
        surf(U)
        plt.savefig('data/fig'+str(f)+'.png')
        f+=1

    #gift
    images=[]
    print(f)
    for f in range(f):
        images.append(imageio.imread('data/fig'+str(f)+'.png'))
    imageio.mimsave('movie.gif',images,duration=0.8)
#input a,b,h,epsilon
f1 = lambda y:20 #4.*np.cos(2.*y)  #20u(i,1)       
f2 = lambda y:300 #1.*y            #300U(i,m)         
f3 = lambda x:80 #3.*np.sin(2.*x)  #80U(1,j)
f4 = lambda x:0 # .6*x            #0U(m,j)


laplace('f1','f2','f3','f4',7,6,0.2,0.001)
