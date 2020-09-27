from euler import *
import matplotlib.pyplot as plt

h=0.01
t=1

pa=np.array([0,0,0])
ve=np.array([5,2,0])
ac=np.array([0,-10,0]) #gravedad

# Ejercicio
fig = plt.figure()
vp,vv,va,pt = euler(pa,ve,ac,t,h);
ac=np.array([2,-10,0]) #gravedad
vp1,vv1,va1,pt1 = euler(vp[len(vp)-1],vv[len(vv)-1],ac,t,h);
ac=np.array([-1,-10,0]) #gravedad
vp2,vv2,va2,pt2 = euler(vp1[len(vp1)-1],vv1[len(vv1)-1],ac,t,h);
ac=np.array([2,-10,0]) #gravedad
vp3,vv3,va3,pt3 = euler(vp2[len(vp2)-1],vv2[len(vv2)-1],ac,t,h);
ac=np.array([pow(5,2)/5,-10,0]) #gravedad
vp4,vv4,va4,pt4 = euler(vp3[len(vp3)-1],vv3[len(vv3)-1],ac,t,h);

ax = fig.add_subplot(1,1,1,projection='3d')

vp=np.concatenate((vp,vp1),axis=0)
vp=np.concatenate((vp,vp2),axis=0)
vp=np.concatenate((vp,vp3),axis=0)
vp=np.concatenate((vp,vp4),axis=0)
ax.plot(vp[:,0],vp[:,2],vp[:,1])
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_zlabel('y')
plt.title('x-y-z')
plt.grid(True)
plt.show()
