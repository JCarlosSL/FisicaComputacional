import numpy as np
import random
import matplotlib.pyplot as plt

m = 10000
veces = 50
ax = -np.sqrt(2)
bx = np.sqrt(2)
ay = -np.sqrt(3)
by = np.sqrt(3)
az = -2
bz = 2

sa = 0
saa = 0

for k in range(0,veces):
    n = 0
    px,py,pz = [], [], []
    for i in range(0,m):
        r =  random.random()
        x = ax + (bx-ax)*r
        r = random.random()
        y = ay + (by-ay)*r
        r = random.random()
        z = az + (bz-az)*r

        if (x**2)/2 + (y**2)/3+ (z**2)/4 <=1:
            n+=1
            px.append(x)
            py.append(y)
            pz.append(z)

    area = n*(by-ay)*(bx-ax)/m * (bz-az)
    sa+=area
    saa+=area**2

prom = sa/veces #promedio
desv = np.sqrt(veces*saa-sa**2)/veces #desviación
fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
ax.plot(px,py,pz,'.')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('area montecarlo')
plt.axis([-3,3,-4,4])
#plt.text(0.5,3.5,str(prom))
#ax.text(1.5,3.5,'+-')
#ax.text(2,3.5,str(desv))

plt.show()

