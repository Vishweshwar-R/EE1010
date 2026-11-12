import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#If using termux
import subprocess
import shlex
#end if

# Q1: x = 3 is a root of x^2 - 2kx - 6 = 0, find k
k = sp.symbols('k')
ks = sp.solve(sp.Eq(3**2 - 2*k*3 - 6, 0), k)[0]
print("k =", ks)
assert ks == sp.Rational(1, 2)
kv = float(ks)

f = lambda x, c: x**2 - 2*c*x - 6
roots = np.roots([1, -2*kv, -6])
print("roots of x^2 - 2kx - 6 for this k:", np.sort(roots))
assert np.isclose(f(3, kv), 0)

x = np.linspace(-4, 5, 400)
plt.figure(figsize=(5.5, 4))
plt.plot(x, f(x, kv), 'b', label=r'$k=\frac{1}{2}$')
for c in (-1, 2):                        # other values of k miss the point (3, 0)
    plt.plot(x, f(x, c), '--', alpha=0.5, label=f'$k={c}$')
plt.axhline(0, color='k', lw=0.8)
plt.plot(roots, [0, 0], 'ro')
plt.annotate(r'$x=3$', (3, 0), textcoords='offset points', xytext=(6, 8))
plt.ylim(-12, 12)
plt.xlabel('$x$'); plt.ylabel('$x^2-2kx-6$')
plt.legend(fontsize=8); plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/1.2.1.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.1.png"))
#else
#plt.show()
