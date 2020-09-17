import matplotlib.pyplot as plt
import numpy as np

h = 0.01
x = -3
y = -4
z = -5
vx = 2
vy = 4
vz = 0
ax = 0
ay = 0
az = 0

pt = np.arange(0,5,h)
p = []
pv = []
pa = []

for t in pt:
    x = x-vx*h
    y = y-vy*h
    z = z-vz*h
    vx = vx-ax*h
    vy = vy-ay*h
    vz = vz-az*h
    p.append([x,y,z])
    pv.append([vx,vy,vz])
    pa.append([ax,ay,az])

fig = plt.figure()

ax = fig.add_subplot(2,3,1)
ax.plot(pt,p)
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('xyz-t')
plt.grid(True)

ax = fig.add_subplot(2,3,2)
ax.plot(pt,pv)
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('v-t')
plt.grid(True)

ax = fig.add_subplot(2,3,3)
ax.plot(pt,pa)
plt.xlabel('tiempo')
plt.ylabel('aceleracion')
plt.title('a-t')
plt.grid(True)

ax = fig.add_subplot(2,3,4)
ax.plot(p,pv)
plt.xlabel('espacio')
plt.ylabel('velocidad')
plt.title('espacio de fases')
plt.grid(True)

p=np.array(p)
plt.subplot(2,3,5)
ax = fig.add_subplot(2,3,5,projection='3d')
ax.plot(p[:,0],p[:,1],p[:,2])
plt.title('x-y-z')
ax.legend()
plt.grid(True)
plt.show()

