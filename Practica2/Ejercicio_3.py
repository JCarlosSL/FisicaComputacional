from euler import *
import matplotlib.pyplot as plt

h=0.01
t=14

a = 10 #gravedad

# Ejercicio
fig = plt.figure()
vp,vv,va,pt = euler(0,15,a,t,h,resta);
ax = fig.add_subplot(1,1,1,projection='3d')
ax.plot(vv,vp,pt)
ax.set_xlabel('v')
ax.set_ylabel('x')
ax.set_zlabel('t')
plt.title('v-x-t')
#ax.legend()
plt.grid(True)
plt.show()

fig = plt.figure()
vp,vv,va,pt = euler(20,0,a,t,h,resta);
ax = fig.add_subplot(1,1,1,projection='3d')
ax.plot(vv,vp,pt)
ax.set_xlabel('v')
ax.set_ylabel('x')
ax.set_zlabel('t')
plt.title('v-x-t')
#ax.legend()
plt.grid(True)
plt.show()


vp,vv,va,pt = euler(0,-15,a,t,h,resta);

fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
ax.plot(vv,vp,pt)
ax.set_xlabel('v')
ax.set_ylabel('x')
ax.set_zlabel('t')
plt.title('v-x-t')
#ax.legend()
plt.grid(True)
plt.show()

