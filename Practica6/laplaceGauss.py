import numpy as np
from matplotlib.colors import Normalize
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.pylab as p


def feval(funcName, *args):
    return eval(funcName)(*args)
        
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
    plt.show()
    return surf

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

def gausslaplace(f1,f2,f3,f4,a,b,h,epsilon):
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
    surf(U)
    print(U)




f1 = lambda y:20 #4.*np.cos(2.*y)  #20u(i,1)       
f2 = lambda y:300 #4.*np.cos(2.*y)  #20u(i,1)       
f3 = lambda x:80 #4.*np.cos(2.*y)  #20u(i,1)       
f4 = lambda x:1#4.*np.cos(2.*y)  #20u(i,1)       

gausslaplace('f1','f2','f3','f4',5,6,1,0.01)
