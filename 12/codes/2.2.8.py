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

# the three planes n_i^T x = d_i meet in one point Q; each is drawn as an equal square patch about M
N = np.block([n1, n2, n]).T
dv = np.array([5.0, 0.0, d])
Q = LA.solve(N, dv).reshape(-1, 1)
M = (Q + P0) / 2

def patch(nv, dd, half=3.5, num=12):
    u0 = nv / LA.norm(nv)
    a = np.array([[1.0], [0.0], [0.0]]) if abs(u0[0, 0]) < 0.9 else np.array([[0.0], [1.0], [0.0]])
    e1 = a - (a.T @ u0).item() * u0; e1 = e1 / LA.norm(e1)
    e2 = np.cross(u0.ravel(), e1.ravel()).reshape(-1, 1)
    c = M - ((nv.T @ M).item() - dd) / (nv.T @ nv).item() * nv   # projection of M on the plane
    s_, t_ = np.meshgrid(np.linspace(-half, half, num), np.linspace(-half, half, num))
    return [c[i, 0] + s_ * e1[i, 0] + t_ * e2[i, 0] for i in range(3)]

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection="3d")
for nv, dd, colr in [(n1, 5.0, "tab:blue"), (n2, 0.0, "tab:green"), (n, d, "tab:red")]:
    ax.plot_surface(*patch(nv, dd), alpha=0.35, color=colr, linewidth=0)
ax.scatter(*P0.flatten(), color="k", s=40)
ax.text(*(P0.flatten() + 0.3), "$P_0(-1,3,2)$", fontsize=9)
for k in range(3):
    lo, hi = M[k, 0] - 5, M[k, 0] + 5
    (ax.set_xlim, ax.set_ylim, ax.set_zlim)[k](lo, hi)
ax.set_box_aspect((1, 1, 1))
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.view_init(elev=22, azim=-58)       # chosen view: shows all three planes and P0 without overlap
plt.tight_layout()

#If using termux
plt.savefig('figs/2.2.8.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/2.2.8.png"))
#else
#plt.show()
