import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules

from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

A = np.array([[0.0], [100.0]]); B = np.array([[0.0], [0.0]])
# the line of sight with depression angle t meets the ground y = 0: Gauss elimination on (lambda, x)
def ground(t):
    M = np.array([[np.sin(t), 0.0], [np.cos(t), -1.0]]); rhs = np.array([[100.0], [0.0]])
    return LA.solve(M, rhs)[1, 0]
x1, x2 = ground(np.pi / 4), ground(np.pi / 6)
C = np.array([[x1], [0.0]]); D = np.array([[x2], [0.0]])
print("BC =", round(x1, 4), " BD =", round(x2, 4), " CD =", round(x2 - x1, 4))
assert np.isclose(x2 - x1, 100 * (np.sqrt(3) - 1))

plt.figure(figsize=(6, 3.6))
for U, W, st in [(A, B, 'k-'), (A, C, 'r-'), (A, D, 'b-'), (B, D, 'k-')]:
    x = line_gen(U, W); plt.plot(x[0, :], x[1, :], st)
pts = np.block([A, B, C, D]); plt.scatter(pts[0, :], pts[1, :], color='k', s=12)
label_pts(pts, ['$A$', '$B$', '$C$', '$D$'])
plt.grid(alpha=0.3); plt.axis('equal')

#If using termux
plt.savefig('figs/1.2.12.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.12.png"))
#else
#plt.show()
