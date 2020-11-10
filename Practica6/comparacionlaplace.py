import numpy as np
from matplotlib.colors import Normalize
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.pylab as p
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def meshgrid_of(A):
    x = range(np.shape(A)[0])
    y = range(np.shape(A)[1])
    xx, yy = p.meshgrid(x,y)
    return xx, yy

fig = plt.figure()
def surf(Z, colormap=cm.RdYlGn):
    X, Y = meshgrid_of(Z) 
    C = Z
    scalarMap = cm.ScalarMappable(norm=Normalize(vmin=C.min(), vmax=C.max()), cmap=colormap)
    C_colored = scalarMap.to_rgba(C)

    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z,facecolors=C_colored)
    #fig.colorbar(surf,shrink=0.5,aspect=5)
    return surf,ax

def feval(funcName, *args):
	return eval(funcName)(*args)

def laplace(f1,f2,f3,f4,a,b,h,epsilon):
    # f1 = u(x,0) = u(i,1)-> abajo
    # f2 = u(x,b) = u(i,m) -> arriba
    # f3 = u(0,y) = u(1,j) -> izquierda
    # f4 = u(a,y) = u(n,j) -> derecha
    # a y b son extremos [0,a] [0,b]
    # h tamaño de paso
    # epsilon -> tolerancia

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

    while(rmax > epsilon):
        rmax=0
        for i in range(1,n-1):
            for j in range(1,m-1):
                rij = ((U[i,j+1]+U[i,j-1]+U[i+1,j]+U[i-1,j])/4)-U[i,j]
                U[i,j] = U[i,j]+w*rij
                if rmax <= abs(rij):
                    rmax = abs(rij)
    return U

### Laplace
def GaussJordan(A1,x):
    #Gauss Jordan
    # Ax= b
    # input A1: A
    # input x: b
    m,n=A1.shape
    A=np.zeros(shape=(m,n+1))
    A[:m,:n]=A1
    A[:,m]=x
    
    for i in range(0,m-1):
        for j in range(i+1,m):
            k=(-1)*A[j,i]/A[i,i]
            temprow=A[i,:]*k
            A[j,:]=A[j,:]+temprow
    
    for i in range(m-1,0,-1):
        for j in range(i-1,-1,-1):
            k=(-1)*A[j,i]/A[i,i]
            temprow=A[i,:]*k
            A[j,:]=A[j,:]+temprow
    for i in range(0,m):
        A[i,:]=A[i,:]/A[i,i]
    return A[:,n]

def gausslaplace(f1,f2,f3,f4,a,b,h):
    n = int(np.fix(a/h)+1)  # numero de filas
    m = int(np.fix(b/h)+1)  # numero de columnas

    U=np.zeros((n,m),dtype=float) # matriz de n*m

    x = np.linspace(0,(m-1)*h,m)
    y = np.linspace(0,(n-1)*h,n)
    # Ingreso de datos existentes en la matriz U
    U[0,:] = feval(f3,x)
    U[-1,:] = feval(f4,x)
    U[:,0] = feval(f1,y)
    U[:,-1] = feval(f2,y)

    U[0,0] = (U[0,1]+U[1,0])/2 
    U[0,-1] = (U[0,-2]+U[1,-1])/2 
    U[-1,0] = (U[-2,0]+U[-1,1])/2 
    U[-1,-1] = (U[-2,-1]+U[-1,-2])/2 
    
    #Generación de la matriz de las ecuaciones lineales independientes
    mn = (n-2)*(m-2)
    GJ = np.zeros((mn,mn),dtype=float)
    # La diagonal se define con 4 que son los vecinos cercanos a una variable
    np.fill_diagonal(GJ,4)
    B = np.zeros(mn,dtype=float)
    
    #Obtención automatica de las ecuaciones lineales independientes en una matriz
    # de tamaño mn*mn
    k=0
    m_temp=m-2
    for i in range(1,n-1):
        for j in range(1,m-1):
            if U[i,j+1]==0:
                GJ[k,(i-1)*m_temp+j]=-1
            else:
                B[k]+=U[i,j+1]
            if U[i,j-1]==0:
                GJ[k,(i-1)*m_temp+j-2]=-1
            else:
                B[k]+=U[i,j-1]
            if U[i+1,j]==0:
                GJ[k,(i)*m_temp+j-1]=-1
            else:
                B[k]+=U[i+1,j]
            if U[i-1,j]==0:
                GJ[k,(i-2)*m_temp+j-1]=-1
            else:
                B[k]+=U[i-1,j]
            k+=1
                    
    #LLamamos a Eliminación Gaussian y obtenemos x = el cual son las variables
    x = GaussJordan(GJ,B)
    k=0
    for i in range(1,n-1):
        for j in range(1,m-1):
            U[i,j] = x[k]
            k+=1
    return U

#input a,b,h,epsilon
f1 = lambda y:20 #4.*np.cos(2.*y)  #20u(i,1)       
f2 = lambda y:300 #1.*y            #300U(i,m)         
f3 = lambda x:80 #3.*np.sin(2.*x)  #80U(1,j)
f4 = lambda x:1 # .6*x            #0U(m,j)

UL = laplace('f1','f2','f3','f4',4,4,0.2,0.001)
UG = gausslaplace('f1','f2','f3','f4',4,4,0.2)

EU = abs(UG-UL)

mse = np.square(UG-UL).mean() 

surf(UG,colormap=cm.coolwarm)
surf(UL,colormap=cm.PuBuGn)
#surf(EU)
plt.show()
print("Erro Cuadratico medio: ",mse)
