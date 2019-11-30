import matplotlib.pyplot as plt
import numpy as np

xmin, ymin, xmax, ymax = -0.5, -0.5, 0.5, 0.5

h = .02
X = np.arange(xmin, xmax, h)
Y = np.arange(ymin, ymax, h)
X0=[0]
Y0=[0]
Rlim = 0.002

XX,YY = np.meshgrid(X, Y)

R=np.sqrt(XX**2+YY**2)
R[R**2<Rlim] = np.nan 
Ex=XX/R**2
Ey=YY/R**2

plt.axis('equal')

plt.scatter(XX,YY,s=2,c="black")
plt.scatter(X0,Y0,s=20,c='blue')
plt.quiver(XX,YY,Ex,Ey,color='blue', width=0.002, scale = 500)
plt.show()
