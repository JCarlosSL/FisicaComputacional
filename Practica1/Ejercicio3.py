import matplotlib.pyplot as plt
import numpy as np

h = 0.01
y = -5
vy = 3
ay = 0

pt = np.arange(0,15,h)
py = []
pv = []
pa = []

for t in pt:
    if t>=3 and t<8:
        vy=6
    elif t>=8 and t<10:
        vy=8
    else:
        vy=3
    y = y+vy*h
    vy = vy+ay*h
    py.append(y)
    pv.append(vy)
    pa.append(ay)

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
