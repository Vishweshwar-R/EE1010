import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Q3: differential equation of the family y = -A cos 3x + B sin 3x
import sympy as sp
x, A, B = sp.symbols("x A B")
y = -A * sp.cos(3 * x) + B * sp.sin(3 * x)
print("y'' + 9y =", sp.simplify(sp.diff(y, x, 2) + 9 * y))     # 0
xs = np.linspace(0, 2 * np.pi, 400)
plt.figure(figsize=(6, 3.5))
for Av, Bv in [(1, 0), (0, 1), (1, 1), (-2, 1), (0.5, -1.5)]:
    plt.plot(xs, -Av * np.cos(3 * xs) + Bv * np.sin(3 * xs), label=f"A={Av}, B={Bv}")
plt.xlabel("x"); plt.ylabel("y"); plt.grid(alpha=0.3); plt.legend(fontsize=7)
plt.title("Members of the family, all satisfying $y''+9y=0$")
plt.tight_layout()
#If using termux
plt.savefig('figs/OdeFamily.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/OdeFamily.png"))
#else
#plt.show()
