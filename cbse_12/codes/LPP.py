import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import line_norm, line_dir_pt, line_isect
from CoordGeo.plotting.funcs import label_pts
from CoordGeo.params import omat, e1, e2
# Q26: maximise Z = 100x + 120y  s.t. 5x + 8y <= 200, 10x + 8y <= 240, x, y >= 0
from scipy.optimize import linprog
col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
n1, c1 = col(5, 8), 200
n2, c2 = col(10, 8), 240
O = col(0, 0)
P1 = line_isect(e2, 0, n2, c2)         # y = 0 meets 10x + 8y = 240
P2 = line_isect(n1, c1, n2, c2)        # the two constraints meet
P3 = line_isect(e1, 0, n1, c1)         # x = 0 meets 5x + 8y = 200
V = np.block([O, P1, P2, P3])
Z = lambda p: 100 * p[0, 0] + 120 * p[1, 0]
for name, p in zip(["O", "P1", "P2", "P3"], [O, P1, P2, P3]):
    print(name, p.T, " Z =", Z(p))
res = linprog([-100, -120], A_ub=[[5, 8], [10, 8]], b_ub=[200, 240], bounds=[(0, None)] * 2)
print("linprog:", res.x, " max Z =", -res.fun)
plt.figure(figsize=(6, 5))
for n, c, lab in [(n1, c1, "5x+8y=200"), (n2, c2, "10x+8y=240")]:
    L = line_norm(n, col(c)[0, 0], -40, 40); plt.plot(L[0, :], L[1, :], label=lab)
plt.fill(V[0, :], V[1, :], color="tab:green", alpha=0.3, label="feasible region")
L = line_dir_pt(omat @ col(100, 120), col(32, 0), -0.3, 0.3)
plt.plot(L[0, :], L[1, :], "k--", lw=1, label="Z = 3200")
plt.scatter(V[0, :], V[1, :], color="r", zorder=3)
label_pts(V, ["O", "(24,0)", "(8,20)", "(0,25)"])
plt.xlim(-3, 45); plt.ylim(-3, 32); plt.xlabel("x (type A)"); plt.ylabel("y (type B)")
plt.grid(alpha=0.3); plt.legend(fontsize=8)
plt.tight_layout()
#If using termux
plt.savefig('figs/LPP.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/LPP.png"))
#else
#plt.show()
