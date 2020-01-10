# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:51:30 2020

@author: gpinnell
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage as ndimage
import matplotlib.tri as mtri
from stl import mesh
 
imageFile = 'parrotID.png'
mat = imread(imageFile)
mat = mat[:,:,0] # get the first channel
rows, cols = mat.shape
xv, yv = np.meshgrid(range(cols), range(rows)[::-1])
 
blurred = ndimage.gaussian_filter(mat, sigma=(5, 5), order=0)
fig = plt.figure(figsize=(6,6))
 
ax = fig.add_subplot(221)
ax.imshow(mat, cmap='gray')
 
ax = fig.add_subplot(222, projection='3d')
ax.elev= 75
rawplot = ax.plot_surface(xv, yv, mat)
 
ax = fig.add_subplot(223)
ax.imshow(blurred, cmap='gray')
 
"""
ax = fig.add_subplot(224, projection='3d')
ax.elev= 75
blurplot = ax.plot_surface(xv, yv, blurred)
plt.show()
"""
#everything past this is unknown to function

# u, v are parameterisation variables
u = (np.linspace(0, 2.0 * np.pi, endpoint=True, num=50) * np.ones((10, 1))).flatten()
v = np.repeat(np.linspace(-0.5, 0.5, endpoint=True, num=10), repeats=50).flatten()

# Triangulate parameter space to determine the triangles
tri = mtri.Triangulation(u, v)

#try converting the plot to a triplot
ax = fig.add_subplot(225, projection='3d')
ax.elev= 75
triplot = ax.plot_trisurf(xv, yv, blurred, triangles=tri.triangles, cmap=plt.cm.Spectral)
plt.show()
