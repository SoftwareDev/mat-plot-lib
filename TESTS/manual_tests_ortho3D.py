import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(5, 3)

mpl.rcParams['legend.fontsize'] = 10

# PARAMETRIC CURVE
fig = plt.figure()
ax = fig.add_subplot(gs[0, 0], projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='parametric curve perspective projection')
ax.legend()

ax2 = fig.add_subplot(gs[0, 1], projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax2.plot(x, y, z, label='parametric curve perspective top view')
ax2.view_init(90, 90)
ax2.legend()

ax3 = fig.add_subplot(gs[0, 2], projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax3.plot(x, y, z, label='parametric curve orthogonal projection')
ax3.legend()

# WIREFRAME
ax4 = fig.add_subplot(gs[1, 0], projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax4.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

ax5 = fig.add_subplot(gs[1, 1], projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax5.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
ax5.view_init(90, 90)

ax6 = fig.add_subplot(gs[1, 2], projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax6.plot_wireframe(X, Y, Z, rstride=10, cstride=10)


#SURFACE
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

ax7 = fig.add_subplot(gs[2, 0], projection='3d')
ax7.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

ax8 = fig.add_subplot(gs[2, 1], projection='3d')
ax8.view_init(90, 90)
ax8.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

ax9 = fig.add_subplot(gs[2, 2], projection='3d')
ax9.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

#TRI SURFACE

n_angles = 36
n_radii = 8
# An array of radii
# Does not include radius r=0, this is to eliminate duplicate points
radii = np.linspace(0.125, 1.0, n_radii)
# An array of angles
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
# Repeat all angles for each radius
angles = np.repeat(angles[...,np.newaxis], n_radii, axis=1)
# Convert polar (radii, angles) coords to cartesian (x, y) coords
# (0, 0) is added here. There are no duplicate points in the (x, y) plane
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())
# Pringle surface
z = np.sin(-x*y)

ax9 = fig.add_subplot(gs[3, 0], projection='3d')
ax9.plot_trisurf(x, y, z, cmap=mpl.cm.jet, linewidth=0.2)

ax10 = fig.add_subplot(gs[3, 1], projection='3d')
ax10.plot_trisurf(x, y, z, cmap=mpl.cm.jet, linewidth=0.2)
ax10.view_init(90, 90)

ax11 = fig.add_subplot(gs[3, 2], projection='3d')
ax11.plot_trisurf(x, y, z, cmap=mpl.cm.jet, linewidth=0.2)

# CONTOUR

X, Y, Z = axes3d.get_test_data(0.05) 

ax12 = fig.add_subplot(gs[4, 0],projection='3d')
ax12.contourf(X, Y, Z, cmap=mpl.cm.coolwarm)

ax13 = fig.add_subplot(gs[4, 1],projection='3d')
ax13.contourf(X, Y, Z, cmap=mpl.cm.coolwarm)
ax13.view_init(90, 90)

ax14 = fig.add_subplot(gs[4, 2],projection='3d')
ax14.contourf(X, Y, Z, cmap=mpl.cm.coolwarm)

plt.tight_layout()
plt.show()