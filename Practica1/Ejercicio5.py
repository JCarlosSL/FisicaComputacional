import matplotlib.pyplot as plt
import numpy as np

h = 0.01
y = 0
vy = 0
ay = 0

pt = np.arange(0,2,h)

error = 300
while(error > 0):

    py = []
    pv = []
    pa = []
    for t in pt:
        y = y+vy*h
        vy = vy+ay*h
        py.append(y)
        pv.append(vy)
        pa.append(ay)
    error = np.sqrt(pow(300-y,2)/2)
    vy += 1
    y=0
    
plt.subplot(2,2,1)
plt.plot(pt,py)
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('y-t')
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
plt.plot(py,pv)
plt.xlabel('espacio')
plt.ylabel('velocidad')
plt.title('espacio de fases')
plt.grid(True)

plt.show()
