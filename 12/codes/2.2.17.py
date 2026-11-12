import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import dir_vec
# Q17: A(x,5,-1), B(3,2,1), C(4,5,5), D(4,2,-2) coplanar
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D  # noqa
x = sp.symbols("x")
A = sp.Matrix([x, 5, -1]); B = sp.Matrix([3, 2, 1]); C = sp.Matrix([4, 5, 5]); D = sp.Matrix([4, 2, -2])
stp = sp.Matrix.hstack(B - A, C - A, D - A).det()
print("[AB AC AD] =", sp.expand(stp), "-> x =", sp.solve(stp, x))
col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
Av, Bv, Cv, Dv = col(6, 5, -1), col(3, 2, 1), col(4, 5, 5), col(4, 2, -2)
print("det[AB AC AD] at x=6:", round(LA.det(np.block([dir_vec(Av, Bv), dir_vec(Av, Cv), dir_vec(Av, Dv)])), 9))
print("det[AB AC AD] at x=2:", round(LA.det(np.block([dir_vec(col(2, 5, -1), Bv), dir_vec(col(2, 5, -1), Cv), dir_vec(col(2, 5, -1), Dv)])), 9), "(not zero)")
n = np.cross(dir_vec(Bv, Cv).T, dir_vec(Bv, Dv).T).flatten()
g = np.linspace(2, 7, 8); X, Y = np.meshgrid(g, g)
fig = plt.figure(figsize=(5.5, 4.5)); ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Bv[2, 0] - (n[0]*(X - Bv[0, 0]) + n[1]*(Y - Bv[1, 0])) / n[2], alpha=0.25, color="tab:green")
for name, p in zip("ABCD", [Av, Bv, Cv, Dv]):
    ax.scatter(*p.flatten(), color="r", s=40); ax.text(*p.flatten(), f" {name}", fontsize=10)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z"); ax.set_title("Coplanar for x = 6")
plt.tight_layout()
#If using termux
plt.savefig('figs/2.2.17.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/2.2.17.png"))
#else
#plt.show()
