import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d, ortho3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from itertools import combinations, product

gs = gridspec.GridSpec(1, 2)
fig = plt.figure()

ax = fig.add_subplot(gs[0, 0], projection='3d')
ax.set_aspect("equal")
# Draw a cube with ortho
r = [-1, 1]
for s, e in combinations(np.array(list(product(r,r,r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax.plot3D(*zip(s,e), color="b") 
ax.view_init(0, 0)

ax = fig.add_subplot(gs[0, 1], projection='orthogonal')
ax.set_aspect("equal")
# Draw a cube with ortho
r = [-1, 1]
for s, e in combinations(np.array(list(product(r,r,r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax.plot3D(*zip(s,e), color="b")
ax.view_init(0, 0)

plt.tight_layout()
plt.show()

