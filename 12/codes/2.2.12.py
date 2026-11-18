import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules

from CoordGeo.line.funcs import line_norm, line_isect
from CoordGeo.conics.funcs import circ_gen, parab_gen
from CoordGeo.plotting.funcs import label_pts

# (a) a = 1: the region x^2 + y^2 <= 16, y^2 <= 6x, integrated along y with the trapezoidal rule
y = np.linspace(-2 * np.sqrt(3), 2 * np.sqrt(3), 100001)
ha = np.sqrt(16 - y**2) - parab_gen(y, 6)
area_a = np.trapezoid(ha, y)
print("(a) trapezoidal area =", round(area_a, 6), " exact =", round(4 / 3 * (4 * np.pi + np.sqrt(3)), 6))
assert abs(area_a - 4 / 3 * (4 * np.pi + np.sqrt(3))) < 1e-4

# (b) vertices as intersections of the three lines n^T x = c
col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
n1, c1 = col(4, -1), -5; n2, c2 = col(1, 1), 5; n3, c3 = col(1, -4), -5
A = line_isect(n1, c1, n3, c3); B = line_isect(n1, c1, n2, c2); C = line_isect(n2, c2, n3, c3)
L1 = lambda t: 4 * t + 5; L2 = lambda t: 5 - t; L3 = lambda t: (t + 5) / 4
x1 = np.array([-1.0, 0.0]); x2 = np.array([0.0, 3.0])             # the corners are the nodes
area_b = np.trapezoid(L1(x1) - L3(x1), x1) + np.trapezoid(L2(x2) - L3(x2), x2)
print("(b) trapezoidal area =", area_b, " vertices:", A.ravel(), B.ravel(), C.ravel())
assert np.isclose(area_b, 7.5)

fig, ax = plt.subplots(1, 2, figsize=(9, 4))
plt.sca(ax[0])
yy = np.linspace(-4, 4, 400)
Cc = circ_gen(col(0, 0), 4)
plt.fill_betweenx(y, parab_gen(y, 6), np.sqrt(16 - y**2), alpha=0.3, color='orange')
plt.plot(Cc[0, :], Cc[1, :], 'b-', label='$x^2+y^2=16$'); plt.plot(parab_gen(yy, 6), yy, 'g-', label='$y^2=6x$')
plt.legend(fontsize=8); plt.grid(alpha=0.3); plt.axis('equal'); plt.title('(a)')
plt.sca(ax[1])
for (n, c, lab) in [(n1, c1, '$4x-y+5=0$'), (n2, c2, '$x+y-5=0$'), (n3, c3, '$x-4y+5=0$')]:
    L = line_norm(n, c, -14, 14); plt.plot(L[0, :], L[1, :], label=lab)
T = np.block([A, B, C]); plt.fill(T[0, :], T[1, :], alpha=0.3, color='orange'); plt.scatter(T[0, :], T[1, :], color='k')
label_pts(T, ['$A$', '$B$', '$C$']); plt.xlim(-3, 5); plt.ylim(-0.5, 7); plt.legend(fontsize=8); plt.grid(alpha=0.3); plt.title('(b)')

#If using termux
plt.savefig('figs/2.2.15.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/2.2.15.png"))
#else
#plt.show()
