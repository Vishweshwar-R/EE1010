import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Q14: int_1^5 (|x-1| + |x-2| + |x-4|) dx
from scipy.integrate import quad
f = lambda x: abs(x - 1) + abs(x - 2) + abs(x - 4)
val, _ = quad(f, 1, 5, points=[2, 4])
print("integral =", round(val, 6))

# Laplace route: f = 7 - 3x + 2*sum (x-a)u(x-a);  g = L^-1{F/s}
import sympy as sp
s_, t_ = sp.symbols("s t", positive=True)
F = 7/s_ - 3/s_**2 + 2*(sp.exp(-s_) + sp.exp(-2*s_) + sp.exp(-4*s_))/s_**2
g = sp.inverse_laplace_transform(F/s_, s_, t_)
lap = sp.nsimplify(g.subs(t_, 5) - g.subs(t_, 1))
print("Laplace result g(5)-g(1) =", lap, " quad =", round(val, 6))
assert abs(float(lap) - val) < 1e-9
x = np.linspace(1, 5, 400)
plt.figure(figsize=(5.5, 3.5))
plt.plot(x, [f(t) for t in x], "b")
plt.fill_between(x, [f(t) for t in x], alpha=0.2)
plt.xlabel("x"); plt.ylabel("f(x)"); plt.grid(alpha=0.3)
plt.title(f"Area under $|x-1|+|x-2|+|x-4|$ = {val:.0f}")
plt.tight_layout()
#If using termux
plt.savefig('figs/2.2.14.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/2.2.14.png"))
#else
#plt.show()
