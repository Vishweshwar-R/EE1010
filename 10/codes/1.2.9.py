import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if


n = np.arange(0, 13)
u = lambda m: np.heaviside(m, 1)                 # unit step: u(m) = 1 for m >= 0
x = 3 * n * u(n - 1)                             # the multiples of 3: x(n) = 3n u(n-1)
S = np.convolve(x, u(n))[:len(n)]                # S(n) = (x * u)(n), the sum of the first n terms
print("x(1..8) =", x[1:9], " S(8) =", S[8])
assert S[8] == 108 and S[8] == 4 * (2 * 3 + 7 * 3)

plt.figure(figsize=(5.5, 4))
plt.stem(n - 0.1, x, linefmt='b-', markerfmt='bo', basefmt='k-', label='$x(n)$')
plt.stem(n + 0.1, S, linefmt='r-', markerfmt='rs', basefmt='k-', label='$S(n)=(x*u)(n)$')
plt.plot(8, 108, 'g^'); plt.annotate('$S(8)=108$', (8.3, 100))
plt.xlabel('$n$'); plt.legend(); plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/1.2.9.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.9.png"))
#else
#plt.show()
