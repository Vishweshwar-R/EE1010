import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Q20: (a) (1+e^2x)dy + (1+y^2)e^x dx = 0, y(0)=1 -> y = e^-x
#      (b) x y' sin(y/x) + x - y sin(y/x) = 0, y(1) = pi/2 -> cos(y/x) = ln x
import sympy as sp
x = sp.symbols("x")
y1 = sp.exp(-x)
print("(a) residual:", sp.simplify((1 + sp.exp(2*x)) * sp.diff(y1, x) + (1 + y1**2) * sp.exp(x)), " y(0) =", y1.subs(x, 0))
xs = np.linspace(0.4, 2.6, 400)
y2 = xs * np.arccos(np.log(xs))
h = 1e-6
t = np.array([0.5, 1.0, 1.5, 2.0])
Y = lambda s: s * np.arccos(np.log(s))
dy = (Y(t + h) - Y(t - h)) / (2*h)
res = t * dy * np.sin(Y(t)/t) + t - Y(t) * np.sin(Y(t)/t)
print("(b) residual:", np.round(res, 6), " y(1) =", Y(1.0), " pi/2 =", np.pi/2)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
xa = np.linspace(-2, 2, 200)
ax[0].plot(xa, np.exp(-xa), "b"); ax[0].plot(0, 1, "ro"); ax[0].set_title(r"(a) $y=e^{-x}$"); ax[0].grid(alpha=0.3)
ax[1].plot(xs, y2, "b"); ax[1].plot(1, np.pi/2, "ro"); ax[1].set_title(r"(b) $\cos(y/x)=\ln x$"); ax[1].grid(alpha=0.3)
plt.tight_layout()
#If using termux
plt.savefig('figs/2.2.20.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/2.2.20.png"))
#else
#plt.show()
