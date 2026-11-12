import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Q4: d/dx cos^-1(sin 2x)
f = lambda x: np.arccos(np.sin(2 * x))
x0 = np.linspace(-np.pi / 4 + 0.01, np.pi / 4 - 0.01, 9)
h = 1e-6
print("numerical derivative:", np.round((f(x0 + h) - f(x0 - h)) / (2 * h), 5))
x = np.linspace(-np.pi / 2, np.pi / 2, 2000)
plt.figure(figsize=(6, 3.5))
plt.plot(x, f(x), "b", label=r"$\cos^{-1}(\sin 2x)$")
xs = np.linspace(-np.pi / 4, np.pi / 4, 50)
plt.plot(xs, np.pi / 2 - 2 * xs, "r--", label=r"$\pi/2-2x$")
plt.axvspan(-np.pi / 4, np.pi / 4, color="gray", alpha=0.15)
plt.xlabel("x"); plt.grid(alpha=0.3); plt.legend()
plt.tight_layout()
#If using termux
plt.savefig('figs/2.2.4.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/2.2.4.png"))
#else
#plt.show()
