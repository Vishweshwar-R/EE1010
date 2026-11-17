import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules

from CoordGeo.line.funcs import line_gen
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.plotting.funcs import label_pts

def rot(t): return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

# no data is given, so assume O(0,0), radius r = 3 and an external point P(5,3)
O = np.array([[0], [0]]); r = 3.0; P = np.array([[5], [3]])
d = LA.norm(P - O)
u = (P - O) / d
# the angle phi between OP and OA satisfies cos(phi) = r/d: Newton-Raphson on cos(phi) - r/d = 0
phi = 1.0
for _ in range(10):
    phi = phi + (np.cos(phi) - r / d) / np.sin(phi)
A = O + r * rot(phi) @ u                         # points of contact
B = O + r * rot(-phi) @ u
print("phi =", round(phi, 6), " PA =", round(LA.norm(P - A), 6), " PB =", round(LA.norm(P - B), 6),
      " sqrt(|OP|^2 - r^2) =", round(np.sqrt(d**2 - r**2), 6))
assert np.isclose((A - O).T @ (P - A), 0) and np.isclose(LA.norm(P - A), LA.norm(P - B))

C = circ_gen(O, r)
plt.figure(figsize=(5, 4.5))
plt.plot(C[0, :], C[1, :], 'b-')
for U, W in [(P, A), (P, B), (O, A), (O, B), (O, P)]:
    x = line_gen(U, W); plt.plot(x[0, :], x[1, :], 'r-' if (U is P) else 'g--')
pts = np.block([O, P, A, B]); plt.scatter(pts[0, :], pts[1, :], color='k', s=12)
label_pts(pts, ['$O$', '$P$', '$A$', '$B$'])
plt.grid(alpha=0.3); plt.axis('equal')

#If using termux
plt.savefig('figs/1.2.18.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.18.png"))
#else
#plt.show()
