from euler import *
import matplotlib.pyplot as plt

h=0.1
t=10

a = -10 #gravedad

# Ejercicio
vp,vv,va,pt = euler(-30,-30,a,t,h);

DrawT_E(plt,pt,vp)
DrawT_V(plt,pt,vv)
DrawT_A(plt,pt,va)
DrawE_V(plt,vp,vv)
plt.show()

vp,vv,va,pt = euler(0,0,a,t,h);
DrawT_E(plt,pt,vp)
DrawT_V(plt,pt,vv)
DrawT_A(plt,pt,va)
DrawE_V(plt,vp,vv)
plt.show()

vp,vv,va,pt = euler(30,30,a,t,h);
DrawT_E(plt,pt,vp)
DrawT_V(plt,pt,vv)
DrawT_A(plt,pt,va)
DrawE_V(plt,vp,vv)
plt.show()
