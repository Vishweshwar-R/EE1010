import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Q23: f(x) = sin 2x + cos 2x on [0, pi] is strictly decreasing on (pi/8, 5pi/8)
x = np.linspace(0, np.pi, 1000)
f = np.sin(2*x) + np.cos(2*x); df = 2*np.cos(2*x) - 2*np.sin(2*x)
dec = x[df < 0]
print("f' < 0 on [", dec.min(), ",", dec.max(), "]   pi/8 =", np.pi/8, " 5pi/8 =", 5*np.pi/8)
plt.figure(figsize=(6.5, 3.8))
plt.plot(x, f, "b", label="f(x)"); plt.plot(x, df, "g--", label="f'(x)")
plt.axvspan(np.pi/8, 5*np.pi/8, color="red", alpha=0.12, label="strictly decreasing")
plt.axhline(0, color="k", lw=0.6)
plt.xticks([0, np.pi/8, np.pi/2, 5*np.pi/8, np.pi], ["0", r"$\pi/8$", r"$\pi/2$", r"$5\pi/8$", r"$\pi$"])
plt.grid(alpha=0.3); plt.legend(fontsize=8)
plt.tight_layout()
#If using termux
plt.savefig('figs/Decreasing.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/Decreasing.png"))
#else
#plt.show()
