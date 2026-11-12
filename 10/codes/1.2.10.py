import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import norm_vec, line_intersect, line_gen
from CoordGeo.plotting.funcs import label_pts
from CoordGeo.params import e1

# A(2, 3), B(6, -3); P(4, m) lies on AB and has x = 4
A = np.array([[2], [3]])
B = np.array([[6], [-3]])

n = norm_vec(A, B)                     # normal vector of AB
P = line_intersect(n, A, e1, 4 * e1)   # AB meets the line x = 4 at P
m = P[1, 0]

# P = (kB + A)/(k + 1)  ->  k = (P_x - A_x)/(B_x - P_x)
k = (P[0, 0] - A[0, 0]) / (B[0, 0] - P[0, 0])
print("P =", P.ravel().round(6) + 0.0, " k =", round(float(k), 6), " m =", round(float(m), 6) + 0.0)
assert np.isclose(k, 1) and np.isclose(m, 0)
assert np.allclose(P, (k * B + A) / (k + 1))

x_AB = line_gen(A, B)
plt.figure(figsize=(5, 4))
plt.plot(x_AB[0, :], x_AB[1, :], 'b-')
pts = np.block([A, B, P])
plt.scatter(pts[0, :], pts[1, :], color='r')
label_pts(pts, ['$A(2,3)$', '$B(6,-3)$', '$P(4,0)$'])
plt.axhline(0, color='k', lw=0.5); plt.axvline(0, color='k', lw=0.5)
plt.xlabel('$x$'); plt.ylabel('$y$')
plt.grid(alpha=0.3); plt.axis('equal')

#If using termux
plt.savefig('figs/1.2.10.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.10.png"))
#else
#plt.show()
