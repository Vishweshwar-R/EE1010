import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if


g = lambda x: np.abs(x - 1) + np.abs(x - 2) + np.abs(x - 4)
x4 = np.arange(1, 6)                              # nodes 1, 2, 3, 4, 5 (h = 1)
T4 = np.trapezoid(g(x4), x4)
x = np.linspace(1, 5, 1001); T1000 = np.trapezoid(g(x), x)
print("trapezoidal rule: N = 4 ->", T4, "   N = 1000 ->", round(T1000, 6))
assert T4 == 18 and abs(T1000 - 18) < 1e-9

xx = np.linspace(1, 5, 400)
plt.figure(figsize=(5.5, 3.6))
plt.plot(xx, g(xx), 'b-')
for a, b in zip(x4[:-1], x4[1:]):                 # the four trapezoids
    plt.fill([a, a, b, b], [0, g(a), g(b), 0], alpha=0.2, color='orange', edgecolor='k')
plt.plot(x4, g(x4), 'ro')
plt.xlabel('$x$'); plt.ylabel('$g(x)$'); plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/2.2.9.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/2.2.9.png"))
#else
#plt.show()
