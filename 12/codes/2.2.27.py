import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import dir_vec, line_gen_num, line_dir_pt
# Q27: (a) distance between parallel lines  (b) foot of perpendicular and image in a plane
from mpl_toolkits.mplot3d import Axes3D  # noqa
col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
# (a) r = (1,1,0) + l(2,-1,1)  and  r = (2,1,-1) + m(2,-1,1)
a1, a2, b = col(1, 1, 0), col(2, 1, -1), col(2, -1, 1)
cr = np.cross(dir_vec(a1, a2).T, b.T).flatten()
d = LA.norm(cr) / LA.norm(b)
print("(a) (a2-a1) x b =", cr, " distance =", d, " sqrt(11/6) =", np.sqrt(11 / 6))
lam = (b.T @ dir_vec(a1, a2)).item() / (b.T @ b).item(); F = a1 + lam * b
print("    foot on line 1:", F.T, " |a2 F| =", LA.norm(dir_vec(a2, F)))
# (b) P(1,3,4), plane 2x - y + z + 3 = 0
P, n, c = col(1, 3, 4), col(2, -1, 1), -3
t = (c - (n.T @ P).item()) / (n.T @ n).item()
Q = P + t * n; Pi = P + 2 * t * n
print("(b) Q =", Q.T, " PQ =", LA.norm(dir_vec(P, Q)), " image =", Pi.T)
fig = plt.figure(figsize=(10, 4.5))
ax = fig.add_subplot(121, projection="3d")
ax.plot(*line_dir_pt(b, a1, -1.5, 1.5), "b-", label="line 1")
ax.plot(*line_dir_pt(b, a2, -1.5, 1.5), "g-", label="line 2")
ax.plot(*line_gen_num(a2, F, 5), "r--", label=f"d = {d:.3f}")
ax.legend(fontsize=8); ax.set_title("(a) parallel lines")
ax = fig.add_subplot(122, projection="3d")
g = np.linspace(-6, 4, 10); X, Y = np.meshgrid(g, g)
ax.plot_surface(X, Y, -3 - 2 * X + Y, alpha=0.25, color="tab:orange")
ax.plot(*line_gen_num(P, Pi, 10), "b-")
for nm, p in [("P", P), ("Q", Q), ("P'", Pi)]:
    ax.scatter(*p.flatten(), color="r", s=40); ax.text(*p.flatten(), " " + nm)
ax.set_zlim(-10, 10); ax.set_title("(b) foot Q and image P'")
for a_ in fig.axes:
    a_.set_xlabel("x"); a_.set_ylabel("y"); a_.set_zlabel("z")
plt.tight_layout()
#If using termux
plt.savefig('figs/2.2.27.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/2.2.27.png"))
#else
#plt.show()
