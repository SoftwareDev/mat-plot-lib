import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d, ortho3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(6, 2)

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

ax3 = fig.add_subplot(gs[0, 1], projection='orthogonal')
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

ax6 = fig.add_subplot(gs[1, 1], projection='orthogonal')
X, Y, Z = ortho3d.get_test_data(0.05)
ax6.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

ax4.set_xlabel('X Label')
ax4.set_ylabel('Y Label')
ax4.set_zlabel('Z Label')

ax6.set_xlabel('X Label')
ax6.set_ylabel('Y Label')
ax6.set_zlabel('Z Label')


#SURFACE
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

ax7 = fig.add_subplot(gs[2, 0], projection='3d')
ax7.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

ax9 = fig.add_subplot(gs[2, 1], projection='orthogonal')
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

ax11 = fig.add_subplot(gs[3, 1], projection='orthogonal')
ax11.plot_trisurf(x, y, z, cmap=mpl.cm.jet, linewidth=0.2)

# CONTOUR

X, Y, Z = axes3d.get_test_data(0.05) 

ax12 = fig.add_subplot(gs[4, 0],projection='3d')
ax12.contourf(X, Y, Z, cmap=mpl.cm.coolwarm)


ax14 = fig.add_subplot(gs[4, 1],projection='orthogonal')
ax14.contourf(X, Y, Z, cmap=mpl.cm.coolwarm)

# SCATTER PLOTS
def randrange(n, vmin, vmax):
    return (vmax-vmin)*np.random.rand(n) + vmin
n = 100

ax15 = fig.add_subplot(gs[5, 0],projection='3d')
for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zl, zh)
    ax15.scatter(xs, ys, zs, c=c, marker=m)

    
ax17 = fig.add_subplot(gs[5, 1],projection='orthogonal')
for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zl, zh)
    ax17.scatter(xs, ys, zs, c=c, marker=m)

    
plt.tight_layout()
plt.show()
