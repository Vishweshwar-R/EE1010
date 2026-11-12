# code by Vishweshwar
import sys
import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

f = lambda x: x**2 + 100 * x - 300000
df = lambda x: 2 * x + 100

# Newton-Raphson iterates from x0 = 1000
xs = [1000.0]
for _ in range(6):
    xs.append(xs[-1] - f(xs[-1]) / df(xs[-1]))
assert abs(xs[-1] - 500) < 1e-6

x = np.linspace(-700, 1100, 400)
plt.figure(figsize=(5.5, 4.2))
plt.plot(x, f(x), 'b-')
plt.axhline(0, color='k', lw=0.5)
for xn, xn1 in zip(xs[:3], xs[1:4]):          # first three steps, drawn as tangent lines
    P = np.array([[xn], [f(xn)]]); Q = np.array([[xn1], [0.0]]); R = np.array([[xn], [0.0]])
    t = line_gen(P, Q); v = line_gen(R, P)
    plt.plot(t[0, :], t[1, :], 'r-', lw=1)
    plt.plot(v[0, :], v[1, :], 'g:', lw=1)
roots = np.array([[500.0, -600.0], [0.0, 0.0]])
plt.scatter(roots[0, :], roots[1, :], color='k', zorder=3)
label_pts(roots, ['$500$', '$-600$'])
plt.xlabel('$x$'); plt.ylabel('$f(x)$')
plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/1.2.16.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.16.png"))
#else
#plt.show()
