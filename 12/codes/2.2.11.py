import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if


import sympy as sp
from mpl_toolkits.mplot3d import Axes3D  # noqa

x = sp.symbols('x')
A = sp.Matrix([x, 5, -1]); B = sp.Matrix([3, 2, 1]); C = sp.Matrix([4, 5, 5]); D = sp.Matrix([4, 2, -2])
M = sp.Matrix.hstack(B - A, C - A, D - A)         # columns AB, AC, AD
M = sp.Matrix([list(M.row(1)), list(M.row(0)), list(M.row(2))])       # R1 <-> R2
M[0, :] = M[0, :] / M[0, 0]                       # R1 <- R1/(-3)
M[1, :] = sp.expand(M[1, :] - M[1, 0] * M[0, :])  # R2 <- R2 - (3-x) R1
M[2, :] = M[2, :] - M[2, 0] * M[0, :]             # R3 <- R3 - 2 R1
M[2, :] = M[2, :] / M[2, 1]                       # R3 <- R3/6
M[1, :] = sp.expand(M[1, :] - M[1, 1] * M[2, :])  # R2 <- R2 - (4-x) R3
print("last pivot =", sp.simplify(M[1, 2]), " -> zero row iff x =", sp.solve(M[1, 2], x))
assert sp.solve(M[1, 2], x) == [6]

# numerical check: the rank of [AB AC AD] drops to 2 only at x = 6
col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
for xv in (2.0, 6.0, 9.0):
    Av = col(xv, 5, -1); Bv, Cv, Dv = col(3, 2, 1), col(4, 5, 5), col(4, 2, -2)
    print(f"x = {xv}: rank =", LA.matrix_rank(np.block([Bv - Av, Cv - Av, Dv - Av])))
assert LA.matrix_rank(np.block([col(3, 2, 1) - col(6, 5, -1), col(4, 5, 5) - col(6, 5, -1), col(4, 2, -2) - col(6, 5, -1)])) == 2

xs = np.linspace(2, 10, 100)
plt.figure(figsize=(5, 3.6))
plt.plot(xs, (6 - xs) / 2, 'b-'); plt.plot(6, 0, 'ro'); plt.axhline(0, color='k', lw=0.5)
plt.annotate('$x=6$', (6.2, 0.3)); plt.xlabel('$x$'); plt.ylabel('last pivot $(6-x)/2$'); plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/2.2.11.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/2.2.11.png"))
#else
#plt.show()
