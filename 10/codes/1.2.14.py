import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# p(x) = 2x^4 - 9x^3 + 5x^2 + 3x - 1
coeffs = [2, -9, 5, 3, -1]
zeros = np.sort(np.roots(coeffs))
print("zeros =", zeros)
expected = np.sort([2 + np.sqrt(3), 2 - np.sqrt(3), 1, -0.5])
assert np.allclose(zeros, expected)

x = np.linspace(-1.2, 3.8, 400)
plt.figure(figsize=(5.5, 4))
plt.plot(x, np.polyval(coeffs, x), 'b-')
plt.plot(zeros, np.zeros_like(zeros), 'ro')
plt.axhline(0, color='k', lw=0.5)
plt.ylim(-10, 15)
plt.xlabel('$x$'); plt.ylabel('$p(x)$')
plt.grid(alpha=0.3)
#If using termux
plt.savefig('figs/1.2.14.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.14.png"))
#else
#plt.show()
