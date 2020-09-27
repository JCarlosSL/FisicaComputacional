from euler import *
import matplotlib.pyplot as plt

h=0.05
t=20

a = 10 #gravedad

# Ejercicio
plt.figure()
vp,vv,va,pt = euler(-20,15,a,t,h,resta);
DrawT_E(plt,pt,vp)
DrawT_V(plt,pt,vv)
DrawT_A(plt,pt,va)
DrawE_V(plt,vp,vv)
plt.show()

plt.figure()
vp,vv,va,pt = euler(-20,0,a,t,h,resta);
DrawT_E(plt,pt,vp)
DrawT_V(plt,pt,vv)
DrawT_A(plt,pt,va)
DrawE_V(plt,vp,vv)
plt.show()

plt.figure()
vp,vv,va,pt = euler(20,-15,a,t,h,resta);
DrawT_E(plt,pt,vp)
DrawT_V(plt,pt,vv)
DrawT_A(plt,pt,va)
DrawE_V(plt,vp,vv)
plt.show()
