import pandas as pd
import numpy as np
from matplotlib import mlab
from mpl_toolkits.mplot3d.axes3d import *
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy import interpolate

#from osg eo import gdal
#from osgeo import gdal_array




#Data extracten uit raw file.
raw_depth = pd.read_csv('Diepte NWW-CK-HK-OM 10x10.pts', delim_whitespace=True)
#raw_depth = raw_depth[0:20000]
depth = raw_depth.iloc[:,2]
x = raw_depth.iloc[:,0] #Decimale coördinaten
y = raw_depth.iloc[:,1]
plt.subplot(212)
plt.plot(x,y)
x = np.array(x)
y = np.array(y)
R = 6731
depth = np.array(depth)



xi = np.linspace(np.min(x), np.max(x))
yi = np.linspace(np.min(y), np.max(y))

X, Y = np.meshgrid(xi,yi)


points = (x,y)
DEPTH = interpolate.griddata((x, y), depth, (X,Y)) #xi, yi)#, method='nearest')#, X, Y)#, xi, yi)
plt.subplot(211)
levels = [-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]
plt.contourf(X,Y, DEPTH, levels=levels)
plt.colorbar()




plt.show()
'''
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X,Y,DEPTH, rstride=1, cstride =1, cmap=cm.jet,linewidth=1,antialiased=True)

plt.show()
plt.close()

import visvis

f = visvis.gca()
m = visvis.grid(xi,yi,DEPTH)
f.daspect = 1,1,10 # z x 10
#draped colors
m = visvis.surf(xi,yi,DEPTH)
m.xolormap=visvis.CM_JET

plt.show()

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

tls.set_credentials_file(username='jaspervlaar', api_key='dgudxbc6IuWrTDe2Svpw')

fig = plt.figure()
ax = fig.gca()
ax.plot(x,y)
plotly_fig = tls.mpl_to_plotly(fig, resize=False, strip_style=False, verbose=False)

plotly_fig.add_trace(dict(type='contour',
                          x=x,
                          y=y,
                          z=depth,
                          ))

plotly_fig.layout.width = 500
plotly_fig.layout.height = 400
py.iplot(plotly_fig)
'''