from euler import *
import matplotlib.pyplot as plt

def limit(vp):
    vpp=[]
    for p in vp:
        if p[1]<=0 :
            break;
        vpp.append(p)
    return npa(vpp)

h=0.01
t=100

pa=np.array([0,0,0])
ve=np.array([5,2,0])
ac=np.array([0,-10,0]) #gravedad

# Ejercicio
fig = plt.figure()
vp,vv,va,pt = euler(pa,ve,ac,t,h);
ac=np.array([2,-10,0]) #gravedad
vp1,vv1,va1,pt1 = euler(pa,ve,ac,t,h);
ac=np.array([-1,-10,0]) #gravedad
vp2,vv2,va2,pt2 = euler(pa,ve,ac,t,h);
ac=np.array([2,-10,-1]) #gravedad
vp3,vv3,va3,pt3 = euler(pa,ve,ac,t,h);
ac=np.array([pow(100,2)/5,-10,0]) #gravedad
vp4,vv4,va4,pt4 = euler(pa,ve,ac,t,h);

vp1=limit(vp1)
ax = fig.add_subplot(2,2,1,projection='3d')
ax.plot(vp1[:,0],vp1[:,2],vp1[:,1])
ax.scatter3D([vp1[0,0]],[vp1[0,2]],[vp[0,1]],color="red")
ax.scatter3D([vp1[len(vp1)-1,0]],[vp1[len(vp1)-1,2]],[vp[len(vp1)-1,1]],color="red")
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_zlabel('y')
plt.title('a = 2i')
plt.grid(True)

vp2=limit(vp2)
ax = fig.add_subplot(2,2,2,projection='3d')
ax.plot(vp2[:,0],vp2[:,2],vp2[:,1])
ax.scatter3D([vp2[0,0]],[vp2[0,2]],[vp2[0,1]],color="red")
ax.scatter3D([vp2[len(vp2)-1,0]],[vp2[len(vp2)-1,2]],[vp2[len(vp2)-1,1]],color="red")
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_zlabel('y')
plt.title('a = -1i')
plt.grid(True)
 
vp3=limit(vp3)
ax = fig.add_subplot(2,2,3,projection='3d')
ax.plot(vp3[:,0],vp3[:,2],vp3[:,1])
ax.scatter3D([vp3[0,0]],[vp3[0,2]],[vp3[0,1]],color="red")
ax.scatter3D([vp3[len(vp3)-1,0]],[vp3[len(vp3)-1,2]],[vp3[len(vp3)-1,1]],color="red")
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_zlabel('y')
plt.title('a = 2i-k')
plt.grid(True)

vp4=limit(vp4)
ax = fig.add_subplot(2,2,4,projection='3d')
ax.plot(vp4[:,0],vp4[:,2],vp4[:,1])
ax.scatter3D([vp4[0,0]],[vp4[0,2]],[vp4[0,1]],color="red")
ax.scatter3D([vp4[len(vp4)-1,0]],[vp4[len(vp4)-1,2]],[vp4[len(vp4)-1,1]],color="red")
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_zlabel('y')
plt.title('a = t^2/5')
plt.grid(True)

plt.show()
