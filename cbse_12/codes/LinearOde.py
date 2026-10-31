import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Q8: (y + 3x^2) dx/dy = x  <=>  dy/dx - y/x = 3x
import sympy as sp
x = sp.symbols("x", positive=True)
y = sp.Function("y")
sol = sp.dsolve(sp.Eq(y(x).diff(x) - y(x) / x, 3 * x), y(x))
print(sol)
C = 1.5
yy = lambda x, c: 3 * x**2 + c * x
res = sp.simplify(sp.diff(3 * x**2 + sp.Symbol("C") * x, x) - (3 * x**2 + sp.Symbol("C") * x) / x - 3 * x)
print("residual:", res)
xs = np.linspace(0.05, 2, 200)
plt.figure(figsize=(6, 3.8))
for c in [-3, -1.5, 0, 1.5, 3]:
    plt.plot(xs, yy(xs, c), label=f"C={c}")
plt.ylim(-3, 15); plt.xlabel("x"); plt.ylabel("y"); plt.grid(alpha=0.3); plt.legend(fontsize=7)
plt.title(r"Solutions $y=3x^2+Cx$")
plt.tight_layout()
#If using termux
plt.savefig('figs/LinearOde.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/LinearOde.png"))
#else
#plt.show()
