import matplotlib.pyplot as plt
import numpy as np
h=0.01
#ejercicio 2
#x=7
#vx=-2 #1-3
#ax=0
#ejercicio 3
x=-5
vx=3
ax=0

px=[]
pv=[]
pa=[]
pt = np.arange(0,15,h)

"""for t in pt:
    if t>=3 and t<8:
        vx=6
    elif t>=8 and t<10:
        vx=3
    else:
        vx=-5
    x=x+vx*h
    vx=vx+ax*h
    px.append(x)
    pv.append(vx)
    pa.append(ax)
   """
# ejercicio 4
"""
x=2
vx=4
ax=0

px=[]
pv=[]
pa=[]
pt = np.arange(0,10,h)
for t in pt:
    x=x-vx*h
    vx=vx-ax*h
"""
x=0
vx=0
ax=0
x1=300
px=[]
pv=[]
pa=[]

pt = np.arange(0,2,h)

error=100
while (error!= 0.003):
    for t in pt:
        x=x+vx*h
        vx=vx+ax*h
        px.append(x)
        pv.append(vx)
        pa.append(ax)
    error = np.sqrt(x1-x)
    vx+=error



print(vx,x)

plt.subplot(2,2,1)
plt.plot(pt,px)    
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('x-t')
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(pt,pv)    
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('v-t')
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(pt,pa)    
plt.xlabel('tiempo')
plt.ylabel('aceleracion')
plt.title('a-t')
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(px,pv)    
plt.xlabel('espacio')
plt.ylabel('velocidad')
plt.title('espacio de fases')
plt.grid(True)

plt.show()

