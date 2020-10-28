import matplotlib.pyplot as plt
import numpy as np
import math
h=0.1
r=3
nlines = 17

punto = [[]for i in range(nlines)]
vPunto = [[]for i in range(nlines)]
aPunto = [[]for i in range(nlines)]
j=0
for j in range(nlines):
	punto[j].append(3)
	punto[j].append(4)
	vPunto[j].append(0)
	vPunto[j].append(0.4)
	aPunto[j].append(0)
	aPunto[j].append(0)

pxPunto=[[]for i in range(nlines)]
pyPunto=[[]for i in range(nlines)]

axs = plt.subplot()
axs.set_aspect('equal')

pt = np.arange(0,400,h)
for it in range(nlines):
	if it>0:
		vPunto[it][0] = vPunto[it-1][0] + 0.37
	for t in pt:
		aPunto[it][0] = -punto[it][0] / pow(pow(punto[it][0],2) + pow(punto[it][1],2),1.5)
		aPunto[it][1] = -punto[it][1] / pow(pow(punto[it][0],2) + pow(punto[it][1],2),1.5)

		vPunto[it][0] = vPunto[it][0] + aPunto[it][0] * h
		vPunto[it][1] = vPunto[it][1] + aPunto[it][1] * h

		punto[it][0] = punto[it][0] + vPunto[it][0] * h
		punto[it][1] = punto[it][1] + vPunto[it][1] * h
		
		pxPunto[it].append(punto[it][0])
		pyPunto[it].append(punto[it][1])

		if(punto[it][0] > 20):
			break

		if(pow(punto[it][0],2) + pow(punto[it][1],2) <= pow(r,2)):
			break
		

cuerpo1 = plt.Circle((0, 0), r, color="lightblue", fill=True)
axs.add_artist(cuerpo1)

for i in range(nlines):
	plt.plot(pxPunto[i],pyPunto[i])

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('X-Y')
plt.grid(True)
plt.show()

