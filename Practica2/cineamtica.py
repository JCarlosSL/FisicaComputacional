import matplotlib.pyplot as plt
import numpy as np


def funciony(vx,vy,ax,g,pp):
    px=[]
    py=[]
    print(px)
    for x in pp:
        print("a")
        y=(vy/ax)*(-vx+np.sqrt(pow(x,2)+2*ax*x))+(g/pow(ax,2))*(pow(-vx+np.sqrt(pow(vx,2)+2*ax*x),2))
        px.append(x)
        py.append(y)
    return np.array(px),np.array(py)

vx=4
vy=10
ax=2
g=-10
px=np.arange(0,1000,0.5)

vx,vy = funciony(vx,vy,ax,g,px)

print(vx,vy)
plt.figure()
plt.plot(vx,vy)
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.grid(True)

plt.show()


