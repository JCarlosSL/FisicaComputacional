from euler import *
import matplotlib.pyplot as plt

h=0.01
t=100

pa=np.array([10,10,10])
ve=np.array([2,0,0])
ac=np.array([-2,-10,4]) #gravedad

# Ejercicio
fig = plt.figure()
vp,vv,va,pt = euler(pa,ve,ac,t,h);

vpp=[]
for p in vp:
    if p[1]<0:
        break
    vpp.append(p)
vp=npa(vpp)

ax = fig.add_subplot(1,1,1,projection='3d')

ax.plot(vp[:,0],vp[:,2],vp[:,1])
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_zlabel('y')
plt.title('x-y-z')
plt.grid(True)
plt.show()
