import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import dir_vec, line_gen_num
# Q9: collinearity of (2,-1,3), (3,-5,1), (-1,11,9); Lagrange identity
from mpl_toolkits.mplot3d import Axes3D  # noqa
col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
A, B, C = col(2, -1, 3), col(3, -5, 1), col(-1, 11, 9)
AB, BC = dir_vec(A, B), dir_vec(B, C)
print("AB =", AB.T, " BC =", BC.T, " BC/AB =", (BC / AB).T)
print("rank[AB BC] =", LA.matrix_rank(np.block([AB, BC])), "(1 => collinear)")
a, b = col(1, 2, 3), col(-2, 0, 5)
axb = np.cross(a.flatten(), b.flatten())
lhs = float(axb @ axb)
rhs = (a.T @ a).item() * (b.T @ b).item() - (a.T @ b).item() ** 2
print("Lagrange identity:", lhs, rhs)
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection="3d")
ax.plot(*line_gen_num(A, B, 20), "b-"); ax.plot(*line_gen_num(B, C, 20), "b-")
for name, p in zip("ABC", (A, B, C)):
    ax.scatter(*p.flatten(), color="r", s=40)
    ax.text(*p.flatten(), f" {name}{tuple(int(v) for v in p.flatten())}", fontsize=8)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
plt.tight_layout()
#If using termux
plt.savefig('figs/2.2.9.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/2.2.9.png"))
#else
#plt.show()
