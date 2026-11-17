import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# assume x = 2, y = 3; the cubic t^3 + beta t^2 + alpha t - 1 with roots x, y, z has x y z = 1
x, y = 2.0, 3.0
z = 1 / (x * y)
alpha = x * y + y * z + z * x
beta = -(x + y + z)
M = np.array([[t, t**2, t**3 - 1] for t in (x, y, z)])       # the matrix whose columns are dependent
c = np.array([alpha, beta, 1.0])
print("M c =", np.round(M @ c, 12), " rank(M) =", LA.matrix_rank(M), " xyz =", x * y * z)
assert np.allclose(M @ c, 0) and LA.matrix_rank(M) == 2 and np.isclose(x * y * z, 1)

t = np.linspace(-0.5, 3.5, 400)
plt.figure(figsize=(5.5, 4))
plt.plot(t, t**3 + beta * t**2 + alpha * t - 1, 'b-')
plt.plot([x, y, z], [0, 0, 0], 'ro')
plt.axhline(0, color='k', lw=0.5)
plt.ylim(-5, 8); plt.xlabel('$t$'); plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/2.2.13.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/2.2.13.png"))
#else
#plt.show()
