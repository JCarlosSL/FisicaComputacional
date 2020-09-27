from euler import *
import matplotlib.pyplot as plt

h=0.01
t=100

pa=np.array([0,0])
ve=np.array([2,3])
ac=np.array([0,-10]) #gravedad

# Ejercicio
plt.figure()
vp,vv,va,pt = euler(pa,ve,ac,t,h);

vpp= []
for p in vp:
    if p[1]<-0.05:
        break
    vpp.append(p)
vp=npa(vpp)

plt.plot(vp[:,0],vp[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.grid(True)
plt.show()
