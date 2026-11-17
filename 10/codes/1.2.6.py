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

# no coordinates are given, so assume P(0,0), Q(6,0), R(2,5)
P = np.array([[0], [0]]); Q = np.array([[6], [0]]); R = np.array([[2], [5]])
k = 1 / 3                                       # AB/PQ
A, B, C = k * P, k * Q, k * R                   # ABC is similar to PQR with ratio k
Omega = np.array([[0, 1], [-1, 0]])

def ar(U, V, W):
    n = Omega @ (V - U)                         # normal vector of UV
    return 0.5 * abs((n.T @ (W - U))[0, 0])

print("ar(PQR) =", ar(P, Q, R), " ar(ABC) =", round(ar(A, B, C), 6), " ratio =", round(ar(A, B, C) / ar(P, Q, R), 6))
assert np.isclose(ar(A, B, C) / ar(P, Q, R), 1 / 9)

plt.figure(figsize=(5, 4))
for V, col in [([P, Q, R], 'b-'), ([A, B, C], 'r-')]:
    for U, W in zip(V, V[1:] + V[:1]):
        x = line_gen(U, W); plt.plot(x[0, :], x[1, :], col)
pts = np.block([P, Q, R, A, B, C])
plt.scatter(pts[0, :], pts[1, :], color='k', s=10)
label_pts(pts, ['$P$', '$Q$', '$R$', '$A$', '$B$', '$C$'])
plt.grid(alpha=0.3); plt.axis('equal')

#If using termux
plt.savefig('figs/1.2.6.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.6.png"))
#else
#plt.show()
