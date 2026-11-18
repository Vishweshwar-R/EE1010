import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules

from CoordGeo.line.funcs import dir_vec, line_gen_num, line_dir_pt
from mpl_toolkits.mplot3d import Axes3D  # noqa

col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
# (a) r = (1,1,0) + l(2,-1,1)  and the parallel line r = (2,1,-1) + m(2,-1,1): no cross product needed
a1, a2, b = col(1, 1, 0), col(2, 1, -1), col(2, -1, 1)
w = dir_vec(a1, a2)                              # a2 - a1
p = ((b.T @ w) / (b.T @ b)).item() * b           # projection of w on b
d = LA.norm(w - p)                               # perpendicular component of w
print("(a) distance =", round(d, 6), " sqrt(11/6) =", round(np.sqrt(11 / 6), 6))
assert np.isclose(d, np.sqrt(11 / 6)) and abs((b.T @ (w - p)).item()) < 1e-12
F = a2 - (w - p)                                 # foot on line 1 of the perpendicular from a2
# (b) P(1,3,4) and the plane 2x - y + z + 3 = 0
P, n, c = col(1, 3, 4), col(2, -1, 1), -3
t = (c - (n.T @ P).item()) / (n.T @ n).item()
Q = P + t * n; Pi = P + 2 * t * n
print("(b) Q =", Q.ravel(), " PQ =", round(LA.norm(dir_vec(P, Q)), 6), " image =", Pi.ravel())
assert np.allclose(Q.ravel(), [-1, 4, 3]) and np.allclose(Pi.ravel(), [-3, 5, 2]) and np.isclose(LA.norm(dir_vec(P, Q)), np.sqrt(6))

fig = plt.figure(figsize=(10, 4.5))
ax = fig.add_subplot(121, projection="3d")
ax.plot(*line_dir_pt(b, a1, -1.5, 1.5), "b-", label="line 1")
ax.plot(*line_dir_pt(b, a2, -1.5, 1.5), "g-", label="line 2")
ax.plot(*line_gen_num(a2, F, 5), "r--", label=f"d = {d:.3f}")
ax.legend(fontsize=8); ax.set_title("(a) parallel lines")
ax.view_init(elev=25, azim=72)                   # nearly face-on to the plane of the two lines: true shape of d
ax = fig.add_subplot(122, projection="3d")
# plane 2x - y + z + 3 = 0 drawn as a square patch about Q (equal axes, so the normal PP' looks perpendicular)
nu = n / LA.norm(n)
e1 = col(1, 2, 0) / np.sqrt(5)                   # a unit vector in the plane (n^T e1 = 0)
e2 = np.cross(nu.ravel(), e1.ravel()).reshape(-1, 1)
s_, t_ = np.meshgrid(np.linspace(-4, 4, 10), np.linspace(-4, 4, 10))
X, Y, Z = [Q[i, 0] + s_ * e1[i, 0] + t_ * e2[i, 0] for i in range(3)]
ax.plot_surface(X, Y, Z, alpha=0.25, color="tab:orange", linewidth=0)
ax.plot(*line_gen_num(P, Pi, 10), "b-")
for nm, pt in [("P", P), ("Q", Q), ("P'", Pi)]:
    ax.scatter(*pt.flatten(), color="r", s=40); ax.text(*pt.flatten(), " " + nm)
for k, setter in enumerate((ax.set_xlim, ax.set_ylim, ax.set_zlim)):
    setter(Q[k, 0] - 5, Q[k, 0] + 5)
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=12, azim=38)                   # plane seen obliquely: P, Q, P' lie along the normal
ax.set_title("(b) foot Q and image P'")
for a_ in fig.axes:
    a_.set_xlabel("x"); a_.set_ylabel("y"); a_.set_zlabel("z")
plt.tight_layout()

#If using termux
plt.savefig('figs/2.2.17.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/2.2.17.png"))
#else
#plt.show()
