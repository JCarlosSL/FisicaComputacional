import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np

def Aceleracion3C(px,d):
    ax = -(px[0]+d)/((px[0]+d)**2+px[1]**2)**1.5-(px[0]-d)/((px[0]-d)**2+px[1]**2)**1.5
    ay = -px[1]/((px[0]+d)**2+px[1]**2)**1.5-px[1]/((px[0]-d)**2+px[1]**2)**1.5
    return np.array([ax,ay])

def Euler(px,pv,d,h=0.01):
    pa = Aceleracion3C(px,d)
    pv = pv + pa*h
    px = px + pv*h
    return (px,pv,pa) 

def getPoint(px1,pv1,pa1,d,r1,h=0.01,t=10):
    vp1 = []

    pt = np.arange(0,t,h)
    for i in pt:
        (px1,pv1,pa1) = Euler(px1,pv1,d,h)
        #if px1[0]>35: break
        if (np.power(px1[0]+d,2)+np.power(px1[1],2))<=r1**2: break
        if (np.power(px1[0]-d,2)+np.power(px1[1],2))<=r1**2: break
        vp1.append(px1)
    return np.array(vp1)

r1 = 30 # radio planetas
d = 60  # distancia
h = 1

pa = np.array([0,0])
px1 = np.array([40,50])

vx = np.arange(320,330,4)

axs = plt.subplot()
axs.set_aspect('equal')

images= []
color_1 = (11,123,112)
color_2 = (12,32,112)
color_3 = (123,23,111)
color_4 = (123,122,122)

#cuerpo1 = plt.Circle((px1[0],px1[1]),0.4,color="blue",fill=True)
#cuerpo2 = plt.Circle((-d,0),r1,color="red",fill=True)
#cuerpo3 = plt.Circle((d,0),r1,color="yellow",fill=True)
#axs.add_artist(cuerpo1)
#axs.add_artist(cuerpo2)
#axs.add_artist(cuerpo3)
i=0
while(i<2):
    i+=1
    vp1=[]
    for vxi in vx:
        pv1 = np.array([vxi,50])
        vp1 = getPoint(px1,pv1,pa,d,r1,h,400)
        #print(vp)
        plt.plot(vp1[:,0],vp1[:,1],c='blue',linestyle='--')
    
    for p in vp1:
        im = Image.new('RGB',(100,100),color_1)
        draw = ImageDraw.Draw(im)
        draw.ellipse((d, 0, 30, 30), fill = 'green', outline ='blue')
        draw.ellipse((d+d, 0, 30, 30), fill = 'yellow', outline ='blue')
        draw.point((p[0],p[1]),fill=color_1)
        draw.point((p[0],p[1]),fill=color_2)
        images.append(im)
                        
images[0].save('desafio.png',save_all=True,append_images=images[1:],
        optimize=False,duration=20,loop=0)


plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.grid(True)
plt.show()
