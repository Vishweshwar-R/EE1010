import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import ang_vec, line_dir_pt
# Q2: angle between a line and a plane; point where a line meets the yz-plane
from mpl_toolkits.mplot3d import Axes3D  # noqa
col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
# (a) line r = (2,-1,3) + t(3,-1,2), plane x+y+z = 3
a, b, n = col(2, -1, 3), col(3, -1, 2), col(1, 1, 1)
phi = np.arccos((b.T @ n).item() / (LA.norm(b) * LA.norm(n)))   # angle between direction and normal (same as ang_vec(b, n))
theta = np.pi / 2 - phi                # angle between line and plane
print("sin(theta) =", np.sin(theta), " 4/sqrt(42) =", 4 / np.sqrt(42))
print("theta      =", np.degrees(theta), "deg")
# (b) (x+2)/1 = (y-5)/3 = (z+1)/5 meets x = 0
p0, d = col(-2, 5, -1), col(1, 3, 5)
lam = (0 - p0[0, 0]) / d[0, 0]
P = p0 + lam * d
print("lambda =", lam, " point =", P.T)

fig = plt.figure(figsize=(10, 4.5))
ax = fig.add_subplot(121, projection="3d")
g = np.linspace(-3, 6, 12)
X, Y = np.meshgrid(g, g)
ax.plot_surface(X, Y, 3 - X - Y, alpha=0.3, color="tab:green")
L = line_dir_pt(b, a, -1.5, 1.5)
ax.plot(*L, "b-")
ax.set_title("(a) line and plane $x+y+z=3$")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax = fig.add_subplot(122, projection="3d")
Yg, Zg = np.meshgrid(np.linspace(0, 14, 8), np.linspace(-3, 12, 8))
ax.plot_surface(0 * Yg, Yg, Zg, alpha=0.3, color="tab:orange")
L = line_dir_pt(d, p0, -1, 3)
ax.plot(*L, "b-")
ax.scatter(*P.flatten(), color="r", s=40)
ax.text(*P.flatten(), " (0, 11, 9)")
ax.set_title("(b) line meets yz-plane")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
plt.tight_layout()
#If using termux
plt.savefig('figs/LinePlane.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/LinePlane.png"))
#else
#plt.show()
