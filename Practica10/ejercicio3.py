import numpy as np
import matplotlib.pyplot as plt

def feval(funcName, *args):
	return eval(funcName)(*args)

f = lambda t,x,v,m,b,c,d,f0,w: (b*x-c*x**3)/m -d/m*v +f0*np.cos(w*t)

n = 0
m = 1
 
c = 1
b = 1
d = 0.01

t = 0.0
x = 1
v = -1
tfin = 1000

pt = []
pv = []
px = []
pt.append(t)
pv.append(v)
px.append(x)
h=0.1
f0=1
w=0.1

while(t<tfin):
    n = n+1
    a = feval('f',t,x,v,m,b,c,d,f0,w)
    k1 = h*a
    a = feval('f',t+0.5*h,x+h*0.5*v,v+0.5*k1,m,b,c,d,f0,w)
    k2 = h*a
    a=feval('f',t+0.5*h,x+0.5*h*(v+0.5*k1),v+0.5*k2,m,b,c,d,f0,w)
    k3 = h*a
    a = feval('f',t+h,x+h*v+h*k2*0.5,v+k3,m,b,c,d,f0,w)
    k4 = h*a
    x = x+h*v+h*(k1+k2+k3)/6
    v = v+(k1+2*k2+2*k3+k4)/6
    t=t+h
    px.append(x)
    pv.append(v)

plt.subplot(111)
plt.plot(px,pv,'-')
plt.xlabel('x(m)')
plt.ylabel('v(m/s)')
plt.title('x-v')
plt.grid(True)

plt.show()
