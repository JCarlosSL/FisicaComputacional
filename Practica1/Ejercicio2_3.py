import matplotlib.pyplot as plt
import numpy as np

h = 0.01
x = 3
y = -4
vx = 4
vy = -3
ax = -3
ay = 5

pt = np.arange(0,10,h)
p = []
pv = []
pa = []

for t in pt:
    x = x+vx*h
    y = y+vy*h
    vx = vx+ax*h
    vy = vy+ay*h
    p.append([x,y])
    pv.append([vx,vy])
    pa.append([ax,ay])

plt.subplot(2,3,1)
plt.plot(pt,p)
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('xy-t')
plt.grid(True)

plt.subplot(2,3,2)
plt.plot(pt,pv)
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('v-t')
plt.grid(True)

plt.subplot(2,3,3)
plt.plot(pt,pa)
plt.xlabel('tiempo')
plt.ylabel('aceleracion')
plt.title('a-t')
plt.grid(True)

plt.subplot(2,3,4)
plt.plot(p,pv)
plt.xlabel('espacio')
plt.ylabel('velocidad')
plt.title('espacio de fases')
plt.grid(True)

p=np.array(p)
plt.subplot(2,3,5)
plt.plot(p[:,0],p[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.grid(True)
plt.show()

