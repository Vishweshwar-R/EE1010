import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if


u = lambda m: np.heaviside(m, 1)                 # unit step u(m)
n = np.arange(-1, 7)
x0, D = 2, 4
x = (x0 + (n - 1) * D) * u(n - 1)                # x(n) = (x0 + (n-1)D) u(n-1)
S4 = np.convolve(x[n >= 0], u(n[n >= 0]))[4]     # S(4) = (x * u)(4)
print("x(1..4) =", x[(n >= 1) & (n <= 4)], " S(4) =", S4)
assert S4 == 32
assert np.isclose(x[n == 1][0] * x[n == 4][0] / (x[n == 2][0] * x[n == 3][0]), 7 / 15)

D_ = np.linspace(-6, 6, 200)
f = 15 * (8 - 1.5 * D_) * (8 + 1.5 * D_) - 7 * (8 - 0.5 * D_) * (8 + 0.5 * D_)
fig, ax = plt.subplots(1, 2, figsize=(8, 3.6))
ax[0].stem(n, x, basefmt='k-'); ax[0].set_xlabel('$n$'); ax[0].set_ylabel('$x(n)$'); ax[0].grid(alpha=0.3)
ax[1].plot(D_, f, 'b-'); ax[1].plot([-4, 4], [0, 0], 'ro'); ax[1].axhline(0, color='k', lw=0.5)
ax[1].set_xlabel('$D$'); ax[1].set_ylabel('$f(D)$'); ax[1].grid(alpha=0.3)

#If using termux
plt.savefig('figs/1.2.11.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.11.png"))
#else
#plt.show()
