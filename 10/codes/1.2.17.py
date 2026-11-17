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

Omega = np.array([[0, 1], [-1, 0]])
def rot(t): return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
def ar(U, V, W):
    n = Omega @ (V - U)                          # normal vector of UV
    return 0.5 * abs((n.T @ (W - U))[0, 0])

# (a) no side is given, so assume a square of side a = 2
A = np.array([[0], [0]]); B = np.array([[2], [0]]); C = np.array([[2], [2]]); D = np.array([[0], [2]])
E = B + rot(-np.pi / 3) @ (C - B)                # equilateral triangle on the side BC
F = A + rot(np.pi / 3) @ (C - A)                 # equilateral triangle on the diagonal AC
r = ar(B, C, E) / ar(A, C, F)
print("ar(BCE) =", round(ar(B, C, E), 6), " ar(ACF) =", round(ar(A, C, F), 6), " ratio =", round(r, 6))
assert np.isclose(r, 0.5)

# (b) assume PQR with P(0,0), Q(4,0), R(1,3); ABC = k PQR is similar to it
P = np.array([[0], [0]]); Q = np.array([[4], [0]]); R = np.array([[1], [3]])
f = lambda k: k**2 * ar(P, Q, R) - ar(P, Q, R)   # ar(ABC) - ar(PQR) with ar(ABC) = k^2 ar(PQR)
k = 3.0
for _ in range(8):                               # Newton-Raphson on f(k) = 0
    k = k - f(k) / (2 * k * ar(P, Q, R))
print("k =", round(k, 9), " |AB|/|PQ| =", round(LA.norm(k * (Q - P)) / LA.norm(Q - P), 6))
assert np.isclose(k, 1)

fig, ax = plt.subplots(1, 2, figsize=(8, 3.6))
plt.sca(ax[0])
for V in ([A, B, C, D], [B, C, E], [A, C, F]):
    for U, W in zip(V, V[1:] + V[:1]):
        x = line_gen(U, W); plt.plot(x[0, :], x[1, :], 'b-')
pts = np.block([A, B, C, D, E, F]); plt.scatter(pts[0, :], pts[1, :], color='r', s=12)
label_pts(pts, list('ABCDEF')); plt.title('(a)'); plt.grid(alpha=0.3); ax[0].set_aspect('equal')
plt.sca(ax[1])
for U, W in zip([P, Q, R], [Q, R, P]):
    x = line_gen(U, W); plt.plot(x[0, :], x[1, :], 'b-')
pts = np.block([P, Q, R]); plt.scatter(pts[0, :], pts[1, :], color='r', s=12)
label_pts(pts, ['$P=A$', '$Q=B$', '$R=C$']); plt.title('(b) $k=1$'); plt.grid(alpha=0.3); ax[1].set_aspect('equal')

#If using termux
plt.savefig('figs/1.2.17.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.17.png"))
#else
#plt.show()
