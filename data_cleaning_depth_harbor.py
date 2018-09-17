import pandas as pd
import numpy as np
from matplotlib import mlab
from mpl_toolkits.mplot3d.axes3d import *
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy import interpolate
from math import acos, sin , cos, radians



#Data extracten uit raw file.
raw_depth = pd.read_csv('Diepte NWW-CK-HK-OM 10x10.pts', delim_whitespace=True)
#raw_depth = raw_depth[0:20000] #eventuele slicing
depth = np.array(raw_depth.iloc[:,2])
x = np.array(raw_depth.iloc[:,0]) #Decimale coördinaten
y = np.array(raw_depth.iloc[:,1])

x = (x-min(x))
y = (y-min(y))
x= x * (78/max(x)) #1 decimale graden noorderbreedte op 42 NB is ongeveer 78 km
y= y * (78/max(y))

'''
plt.subplot(212) #Mogelijkheid om plaatsen waar data over beschikbaar is te plotten
plt.title('Dieptedata beschikbaar haven van Rotterdam')
plt.plot(x,y)
plt.xlabel('Laterale afstand (km)')
plt.ylabel('Longitudinale afstand (km)')
'''

#Data interpolaten voor plot
xi = np.linspace(np.min(x), np.max(x))
yi = np.linspace(np.min(y), np.max(y))
X, Y = np.meshgrid(xi,yi)
DEPTH = interpolate.griddata((x, y), depth, (X,Y))

#plt.subplot(211) #gebruik als beschikbare data wordt geplot
plt.title('Diepte haven van Rotterdam') #dieptedata plotten
levels = [-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]
plt.contourf(X,Y, DEPTH, levels=levels, cmap='Blues_r')
plt.colorbar()
plt.xlabel('Laterale afstand (km)')
plt.ylabel('Longitudinale afstand (km)')


plt.show()
