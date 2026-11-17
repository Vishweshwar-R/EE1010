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

def rot(t): return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

# (a) assume side a = 3: B(0,0), C(3,0) and A = B + rot(60 deg)(C - B)
B = np.array([[0], [0]]); C = np.array([[3], [0]])
A = B + rot(np.pi / 3) @ (C - B)
D = B + (C - B) / 3                              # BD = BC/3
AD2 = ((A - D).T @ (A - D))[0, 0]; AB2 = ((A - B).T @ (A - B))[0, 0]
print("(a) 9 AD^2 =", round(9 * AD2, 6), " 7 AB^2 =", round(7 * AB2, 6))
assert np.isclose(9 * AD2, 7 * AB2)

# (b) assume a right angle at B: B(0,0), A(0,3), C(4,0)
B2 = np.array([[0], [0]]); A2 = np.array([[0], [3]]); C2 = np.array([[4], [0]])
dot = ((A2 - B2).T @ (C2 - B2))[0, 0]
AC2 = ((C2 - A2).T @ (C2 - A2))[0, 0]
print("(b) (A-B).(C-B) =", dot, " AC^2 =", AC2, " AB^2 + BC^2 =", 9 + 16)
assert dot == 0 and AC2 == 25

fig, ax = plt.subplots(1, 2, figsize=(8, 3.6))
plt.sca(ax[0])
for U, W in [(A, B), (B, C), (C, A), (A, D)]:
    x = line_gen(U, W); plt.plot(x[0, :], x[1, :], 'b-')
pts = np.block([A, B, C, D]); plt.scatter(pts[0, :], pts[1, :], color='r', s=12)
label_pts(pts, list('ABCD')); plt.title('(a)'); plt.grid(alpha=0.3); ax[0].set_aspect('equal')
plt.sca(ax[1])
for U, W in [(A2, B2), (B2, C2), (C2, A2)]:
    x = line_gen(U, W); plt.plot(x[0, :], x[1, :], 'b-')
pts = np.block([A2, B2, C2]); plt.scatter(pts[0, :], pts[1, :], color='r', s=12)
label_pts(pts, list('ABC')); plt.title('(b)'); plt.grid(alpha=0.3); ax[1].set_aspect('equal')

#If using termux
plt.savefig('figs/1.2.24.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.24.png"))
#else
#plt.show()
