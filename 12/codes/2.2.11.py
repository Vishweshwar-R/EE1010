import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if


from mpl_toolkits.mplot3d import Axes3D  # noqa

col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
n1, n2, P0 = col(1, 2, 3), col(3, 3, 1), col(-1, 3, 2)

# the required normal n satisfies n1^T n = 0 and n2^T n = 0:  Gauss elimination on [n1^T; n2^T]
M = np.block([n1, n2]).T
M[1] = M[1] - M[1, 0] / M[0, 0] * M[0]           # R2 <- R2 - 3 R1
print("after elimination:\n", M)
z = 3.0                                          # free variable
y = -M[1, 2] * z / M[1, 1]
x = -(M[0, 1] * y + M[0, 2] * z) / M[0, 0]
n = col(x, y, z)
d = (n.T @ P0).item()
print("n =", n.T, f" -> {n[0,0]:.0f}x + {n[1,0]:.0f}y + {n[2,0]:.0f}z = {d:.0f}   i.e.  7x - 8y + 3z + 25 = 0")
assert np.allclose(n.ravel(), [7, -8, 3]) and abs((n.T @ n1).item()) < 1e-12 and abs((n.T @ n2).item()) < 1e-12

g = np.linspace(-6, 6, 12)
X, Y = np.meshgrid(g, g)
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, (5 - X - 2 * Y) / 3, alpha=0.25, color="tab:blue")
ax.plot_surface(X, Y, -3 * X - 3 * Y, alpha=0.25, color="tab:green")
ax.plot_surface(X, Y, (d - n[0, 0] * X - n[1, 0] * Y) / n[2, 0], alpha=0.35, color="tab:red")
ax.scatter(*P0.flatten(), color="k", s=40)
ax.set_zlim(-15, 15); ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
plt.tight_layout()

#If using termux
plt.savefig('figs/2.2.11.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/2.2.11.png"))
#else
#plt.show()
