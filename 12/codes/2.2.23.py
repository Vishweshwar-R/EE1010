import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules

import cvxpy as cp
from CoordGeo.line.funcs import line_norm, line_isect
from CoordGeo.plotting.funcs import label_pts
from CoordGeo.params import e1, e2

# maximise Z = 100x + 120y  s.t.  5x + 8y <= 200,  10x + 8y <= 240,  x, y >= 0
c = np.array([100, 120]); A = np.array([[5, 8], [10, 8]]); b = np.array([200, 240])
x = cp.Variable(2)
prob = cp.Problem(cp.Maximize(c @ x), [A @ x <= b, x >= 0])
prob.solve()
print("CVXPY: x* =", np.round(x.value, 6), " max Z =", round(prob.value, 6))
assert np.allclose(x.value, [8, 20], atol=1e-5) and abs(prob.value - 3200) < 1e-3

# corner points of the feasible region from the constraint lines (for the figure)
col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
n1, c1 = col(5, 8), 200; n2, c2 = col(10, 8), 240
V = np.block([col(0, 0), line_isect(e2, 0, n2, c2), line_isect(n1, c1, n2, c2), line_isect(e1, 0, n1, c1)])
for P in V.T:
    print((round(float(P[0]), 3), round(float(P[1]), 3)), " Z =", round(float(c @ P), 3))

plt.figure(figsize=(6, 5))
for (n, cc, lab) in [(n1, c1, '$5x+8y=200$'), (n2, c2, '$10x+8y=240$')]:
    L = line_norm(n, cc, -60, 40); plt.plot(L[0, :], L[1, :], label=lab)
plt.fill(V[0, :], V[1, :], alpha=0.3, color='tab:green', label='feasible region')
L = line_norm(col(100, 120), 3200, -60, 40); plt.plot(L[0, :], L[1, :], 'k--', lw=1, label='$Z=3200$')
plt.scatter(V[0, :], V[1, :], color='r', zorder=3)
label_pts(V, ['$O$', '$(24,0)$', '$(8,20)$', '$(0,25)$'])
plt.xlim(-3, 45); plt.ylim(-3, 32); plt.xlabel('$x$ (type A)'); plt.ylabel('$y$ (type B)')
plt.grid(alpha=0.3); plt.legend(fontsize=8)

#If using termux
plt.savefig('figs/2.2.23.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/2.2.23.png"))
#else
#plt.show()
