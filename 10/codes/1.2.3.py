import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules

from CoordGeo.line.funcs import line_norm
from CoordGeo.plotting.funcs import label_pts

# x + y = 30,  x - y = 14
A = np.array([[1.0, 1.0], [1.0, -1.0]]); b = np.array([[30.0], [14.0]])
Ab = np.block([A, b])
Ab[1] = Ab[1] - Ab[1, 0] / Ab[0, 0] * Ab[0]     # R2 <- R2 - R1
y = Ab[1, 2] / Ab[1, 1]
x = (Ab[0, 2] - Ab[0, 1] * y) / Ab[0, 0]
print("x =", x, " y =", y)
assert np.allclose([x, y], LA.solve(A, b).ravel()) and (x, y) == (22, 8)

plt.figure(figsize=(5, 4))
for (n, c, lab) in [(np.array([[1], [1]]), 30, '$x+y=30$'), (np.array([[1], [-1]]), 14, '$x-y=14$')]:
    L = line_norm(n, c, -30, 30); plt.plot(L[0, :], L[1, :], label=lab)
S = np.array([[x], [y]])
plt.scatter(S[0, :], S[1, :], color='r', zorder=3)
label_pts(S, ['$(22,8)$'])
plt.xlim(0, 40); plt.ylim(-5, 35); plt.legend(); plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/1.2.3.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.3.png"))
#else
#plt.show()
