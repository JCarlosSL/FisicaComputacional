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

def surf(Z, colormap=cm.coolwarm):
    X, Y = meshgrid_of(Z) 
    C = Z

    fig = plt.figure()
    scalarMap = cm.ScalarMappable(norm=Normalize(vmin=C.min(), vmax=C.max()), cmap=colormap)
    C_colored = scalarMap.to_rgba(C)

    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, facecolors=C_colored)
    cset = ax.contour(X, Y, Z, zdir='z',offset=-1, cmap=cm.coolwarm)
    #cset = ax.contourf(X, Y, Z, zdir='x',cmap=cm.coolwarm)
    #cset = ax.contour(X, Y, Z, zdir='y', cmap=cm.coolwarm)
    """ax.set_xlabel('X')
    ax.set_xlim(-40, 40)"""
    #fig.colorbar(surf,shrink=0.5,aspect=5)
    #plt.show()
    return surf

def feval(funcName, *args):
	return eval(funcName)(*args)

def Onda(f,g,a,b,v,h,k):
    # f es la condición inicial de la poición
    # g es la condición inicial de la velocidad
    # v es la velocidad de propagación de la onda
    # a es la longitud de la cuerda
    # b es el tiempo que necesita para evaluar la onda
    # h es el tamaño de paso para el espacio
    # k es el tamaño de paso para el tiempo
    n = int(a/h+1)
    m = int(b/k+1)

    # r es el calculo para la condición de estabilidad
    r = v*k/h
    r1 = r**2
    r2 = r**2/2

    s1 = 1-r**2
    s2 = 2*(1-r**2)

    #U es la matriz donde se almacena la solucion numerica
    U = np.zeros((n,m))
    #y = np.linspace(0,(n-1)*h,n)
    # calculo de las primeras dos filas
    for i in range(1,n-1):
        U[i,0]=feval(f,h*(i-1))
        U[i,1]=s1*feval(f,h*(i-1))+k*feval(g,h*(i-1))+r2*(
                feval(f,h*i)+feval(f,h*(i-2)))

    # calculo a partir de la 3ra fila
    count=0
    for j in range(1,m-1):
        for i in range(1,n-1):
            U[i,j+1] = s2*U[i,j]+r1*(U[i-1,j]+U[i+1,j])-U[i,j-1]
        #surf(np.transpose(U))
        #plt.savefig('data/fig'+str(count)+'.png')
        count+=1
        #plt.show()
    surf(np.transpose(U))
    plt.savefig('data/fig'+str(count)+'.png')

    #plt.show()
    #gift
    """images=[]
    for i in range(count):
        images.append(imageio.imread('data/fig'+str(i)+'.png'))
    imageio.mimsave('movie.gif',images,duration=0.8)"""

f = lambda x: x**2-x+np.sin(2*np.pi*x) 
g = lambda x: 0

"""Ejericici 1"""
#Onda('f','g',1,1,2,0.05,0.01)
#Onda('f','g',1,1,2,0.02,0.03)
#Onda('f','g',1,1,2,0.1,0.01)
#Onda('f','g',1,1,2,0.05,0.05)


"""Ejercicio 2"""
#r<=1
r = 0.9
h = 0.05
k = 0.01
v = r*h/k
#Onda('f','g',1,1,v,h,k)

r = 0.3
v = r*h/k
Onda('f','g',1,1,v,h,k)

