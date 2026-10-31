import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Q21: y = (sin x)^x + sin^-1(sqrt(1-x^2)),  0 < x < 1
import sympy as sp
x = sp.symbols("x")
y = sp.sin(x)**x + sp.asin(sp.sqrt(1 - x**2))
dy = sp.diff(y, x)
claim = sp.sin(x)**x * (x * sp.cot(x) + sp.log(sp.sin(x))) - 1 / sp.sqrt(1 - x**2)
for t in [0.2, 0.5, 0.8]:
    print("x =", t, float(dy.subs(x, t)), float(claim.subs(x, t)))
xs = np.linspace(0.02, 0.98, 300)
fy = sp.lambdify(x, y, "numpy"); fd = sp.lambdify(x, claim, "numpy")
plt.figure(figsize=(6, 3.5))
plt.plot(xs, fy(xs), label="y"); plt.plot(xs, fd(xs), "--", label="dy/dx")
plt.xlabel("x"); plt.grid(alpha=0.3); plt.legend()
plt.tight_layout()
#If using termux
plt.savefig('figs/LogDiff.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/LogDiff.png"))
#else
#plt.show()
