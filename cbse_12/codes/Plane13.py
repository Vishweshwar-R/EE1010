import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if
# Q13: plane through (-1,3,2) perpendicular to x+2y+3z=5 and 3x+3y+z=0
from mpl_toolkits.mplot3d import Axes3D  # noqa
col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
n1, n2, P0 = col(1, 2, 3), col(3, 3, 1), col(-1, 3, 2)
n = np.cross(n1.T, n2.T).T                      # normal of required plane
d = (n.T @ P0).item()
print("normal =", n.T, f" -> {n[0,0]:.0f}x + {n[1,0]:.0f}y + {n[2,0]:.0f}z = {d:.0f}  i.e.  7x - 8y + 3z + 25 = 0")
print("n.n1 =", (n.T @ n1).item(), " n.n2 =", (n.T @ n2).item())
g = np.linspace(-6, 6, 12)
X, Y = np.meshgrid(g, g)
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, (5 - X - 2 * Y) / 3, alpha=0.25, color="tab:blue")
ax.plot_surface(X, Y, -3 * X - 3 * Y, alpha=0.25, color="tab:green")
ax.plot_surface(X, Y, (d - n[0, 0] * X - n[1, 0] * Y) / n[2, 0], alpha=0.35, color="tab:red")
ax.scatter(*P0.flatten(), color="k", s=40)
ax.set_zlim(-15, 15)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.set_title("Red plane is perpendicular to both blue and green")
plt.tight_layout()
#If using termux
plt.savefig('figs/Plane13.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/Plane13.png"))
#else
#plt.show()
