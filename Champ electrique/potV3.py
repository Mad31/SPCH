import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

xmin, ymin, xmax, ymax = -0.2, -0.1, 0.2, 0.1

h = .0005
X = np.arange(xmin, xmax, h)
Y = np.arange(ymin, ymax, h)
X0=[-0.1,0.1]
Y0=[0,0]
Rlim=0.00001

XX,YY = np.meshgrid(X, Y)

R1=np.sqrt((XX+0.1)**2+YY**2)
# R1[R1**2<Rlim] = np.nan 
V1=1/R1

R2=np.sqrt((XX-0.1)**2+YY**2)
# R2[R2**2<Rlim] = np.nan 
V2=-1/R2

V=V1+V2

Ex1 = (XX+0.1)/R1**2
Ex2 = -(XX-0.1)/R2**2

Ey1 = YY/R1**2
Ey2 = -YY/R2**2

Ex=Ex1+Ex2
Ey=Ey1+Ey2

plt.axis('equal')
niveau=np.logspace(1,2, num= 100)
niveau1=-niveau
niveau1.sort()
niveau=np.append(niveau1,niveau)

plt.scatter(XX,YY,s=2,c="black")
plt.scatter(X0,Y0,s=20,c='blue')
C= plt.contourf(XX, YY, V, niveau)
# C= plt.contourf(XX, YY, V, niveau , norm = LogNorm())
plt.colorbar(C)
plt.streamplot(XX,YY,Ex,Ey,density=1, cmap='autumn')
# plt.contour(XX, YY, V, niveau, colors='black', linewidth=.1)
plt.show()

