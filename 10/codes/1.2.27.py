import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

A = np.radians(np.linspace(1, 89, 400))
A = A[np.abs(A - np.pi / 4) > 1e-3]       # remove the 0/0 point at 45 deg
lhs = (np.sin(A) - 2 * np.sin(A) ** 3) / (2 * np.cos(A) ** 3 - np.cos(A))
rhs = np.tan(A)
print("max |LHS - RHS| =", np.max(np.abs(lhs - rhs)))
assert np.allclose(lhs, rhs, atol=1e-6)

plt.figure(figsize=(5.5, 4))
plt.plot(np.degrees(A), lhs, 'b-', label='LHS')
plt.plot(np.degrees(A), rhs, 'r--', label=r'$\tan A$')
plt.ylim(-6, 6)
plt.xlabel('$A$ (degrees)'); plt.legend(); plt.grid(alpha=0.3)
#If using termux
plt.savefig('figs/1.2.27.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.27.png"))
#else
#plt.show()
