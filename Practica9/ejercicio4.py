import numpy as np
import random
import matplotlib.pyplot as plt

m = 10000
veces = 50
ax = -0.5
bx = 4
ay = -1
by = 3

sa = 0
saa = 0

for k in range(0,veces):
    n = 0
    px,py = [],[]
    for i in range(0,m):
        r =  random.random()
        x = ax + (bx-ax)*r
        r = random.random()
        y = ay + (by-ay)*r

        if (y**2)<=(2*x+1) and y>=x-1:
            n+=1
            px.append(x)
            py.append(y)

    area = n*(by-ay)*(bx-ax)/m
    sa+=area
    saa+=area**2

prom = sa/veces #promedio
desv = np.sqrt(veces*saa-sa**2)/veces #desviación
plt.plot(px,py,'.')
plt.title('area montecarlo')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-3,3,-4,4])
plt.text(0.5,3.5,str(prom))
plt.text(1.5,3.5,'+-')
plt.text(2,3.5,str(desv))

plt.show()

