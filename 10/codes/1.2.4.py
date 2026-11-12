# code by Vishweshwar
import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

d = -4
a = 28                                   # first term found in the solution
n = np.arange(-2, 10)
x = (a + (n - 1) * d) * np.heaviside(n - 1, 1)     # x(n) = (a + (n-1)d) u(n-1)

assert x[n == 7][0] == 4                 # seventh term
assert np.all(x[n < 1] == 0)             # the unit step switches the AP on at n = 1

plt.figure(figsize=(5.5, 4))
plt.stem(n, x, basefmt='k-')
plt.plot(7, 4, 'ro')
plt.annotate(r'$x(7)=4$', (7.2, 5))
plt.xlabel('$n$'); plt.ylabel('$x(n)$')
plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/1.2.4.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.4.png"))
#else
#plt.show()
