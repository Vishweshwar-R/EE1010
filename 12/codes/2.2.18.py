import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Q18: (a) d/dv with u = tan^-1((3x-x^3)/(1-3x^2)), v = tan^-1(x/sqrt(1-x^2));  (b) implicit derivative
import sympy as sp
x = sp.symbols("x")
u = sp.atan((3*x - x**3) / (1 - 3*x**2)); v = sp.atan(x / sp.sqrt(1 - x**2))
ratio = sp.diff(u, x) / sp.diff(v, x)
claim = 3 * sp.sqrt(1 - x**2) / (1 + x**2)
for t in [-0.5, -0.2, 0.0, 0.3, 0.5]:
    print("x =", t, ":", float(ratio.subs(x, t)), float(claim.subs(x, t)))
# (b): sqrt(1-x^2) + sqrt(1-y^2) = a(x-y) with a = 2  ->  y = sin(asin x - 2 acot 2)
c = 2 * np.arctan(1 / 2)
y = lambda t: np.sin(np.arcsin(t) - c)
t0, h = 0.3, 1e-6
print("residual of relation:", np.sqrt(1-t0**2) + np.sqrt(1-y(t0)**2) - 2*(t0 - y(t0)))
print("numerical dy/dx:", (y(t0+h) - y(t0-h)) / (2*h), " formula:", np.sqrt(1-y(t0)**2) / np.sqrt(1-t0**2))
xs = np.linspace(-0.57, 0.57, 300)
plt.figure(figsize=(6, 3.5))
plt.plot(xs, 3*np.arctan(xs), label=r"$u=\tan^{-1}\frac{3x-x^3}{1-3x^2}=3\tan^{-1}x$")
plt.plot(xs, np.arcsin(xs), "--", label=r"$v=\tan^{-1}\frac{x}{\sqrt{1-x^2}}=\sin^{-1}x$")
plt.xlabel("x"); plt.grid(alpha=0.3); plt.legend(fontsize=8)
plt.tight_layout()
#If using termux
plt.savefig('figs/2.2.18.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/2.2.18.png"))
#else
#plt.show()
