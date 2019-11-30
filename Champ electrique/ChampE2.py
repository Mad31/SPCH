import matplotlib.pyplot as plt
import numpy as np

xmin, ymin, xmax, ymax = -2, -2, 2, 2

h = 0.1
X = np.arange(xmin, xmax, h)
Y = np.arange(ymin, ymax, h)
X0=[-1,1]
Y0=[0,0]
Rlim = 0.01

XX,YY = np.meshgrid(X, Y)

R1=np.sqrt((XX+1)**2+YY**2)
R1[R1**2<Rlim] = np.nan 

R2=np.sqrt((XX-1)**2+YY**2)
R2[R2**2<Rlim] = np.nan 

Ex1 = 10*(XX+1)/R1**2
Ex2 = -10*(XX-1)/R2**2

Ey1 = 10*YY/R1**2
Ey2 = -10*YY/R2**2

Ex=Ex1+Ex2
Ey=Ey1+Ey2

plt.axis('equal')

# plt.scatter(XX,YY,s=2,c="black")
plt.scatter(X0,Y0,s=20,c='blue')
# plt.quiver(XX,YY,Ex,Ey,width=0.002, scale = 900)
plt.streamplot(XX,YY,Ex,Ey,density=[0.5, 1], cmap='autumn')
plt.show()

