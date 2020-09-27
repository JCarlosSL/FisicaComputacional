from euler import *
import matplotlib.pyplot as plt

h=0.01
t=100

pa=np.array([0,3,0])
ve=np.array([2,3,5])
ac=np.array([0,-10,0]) #gravedad

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


maximo = vp[0]
pos=0
c=0
for p in vp:
    if p[1]>maximo[1]:
        maximo=p
        pos=c
    c+=1

print("maximo :",maximo,"tiempo :",pt[pos])
ax.scatter3D(vp[pos][0],vp[pos][2],vp[pos][1],c=vp[pos][1]),'dark'
plt.title('x-y-z')
plt.grid(True)
plt.show()
fig = plt.figure()

alcance = np.sqrt(np.sum((vp[0]-vp[len(vp)-1])**2))
print("alcance :",alcance)
   
