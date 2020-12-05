import numpy as np
import random
import matplotlib.pyplot as plt

m = 10000
veces = 50
"""
ax = -1
bx = 1
ay = 0
by = 1
"""
"""
ax = 0
bx = 1
ay = 0
by = 1
"""

ax = 0
bx = 4
ay = -1
by = 3
az = 0
bz = 0
sa = 0
saa = 0

for k in range(0,veces):
    n = 0
    px = []
    py = []
    for i in range(0,m):
        r =  random.random()
        x = ax + (bx-ax)*r
        r = random.random()
        y = ay + (by-ay)*r
        r = random.random()
        z = az + (bz-az)*r

        if y**2<=2*x+1 and x-y-1<=0:#y<=np.sqrt(x) and y>=x**2: #y<= np.exp(-x**2): #(x**2/4+y**2/9)<1:
            n+=1
            px.append(x)
            py.append(y)
            pz.append(z)
    area = n*(by-ay)*(bx-ax)/m
    sa+=area
    saa+=area**2

prom = sa/veces
desv = np.sqrt(veces*saa-sa**2)/veces
promedio = str(prom)
desviacion = str(desv)
plt.plot(px,py,'.')
plt.title('area montecarlo')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-3,3,-4,4])
plt.text(0.5,3.5,promedio)
plt.text(1.5,3.5,'+-')
plt.text(2,3.5,desviacion)

plt.show()

