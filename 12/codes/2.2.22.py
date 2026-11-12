import numpy as np
import sympy as sp

# Q22: int cos2x cos4x cos6x dx using the Laplace transform
x, s = sp.symbols("x s", positive=True)
f = sp.cos(2*x) * sp.cos(4*x) * sp.cos(6*x)
F = sp.laplace_transform(sp.expand_trig(f).rewrite(sp.cos), x, s, noconds=True)
F = sp.simplify(F)
G = F / s                                   # transform of the integral from 0 to x
g = sp.inverse_laplace_transform(G, s, x)
g = sp.simplify(g.subs(sp.Heaviside(x), 1))
ans = (x + sp.sin(12*x)/12 + sp.sin(8*x)/8 + sp.sin(4*x)/4) / 4
print("F(s) =", F)
print("Laplace result - answer =", sp.simplify(g - ans))
print("check d/dx(answer) - f at points:",
      [round(float((sp.diff(ans, x) - f).subs(x, t)), 12) for t in (0.1, 0.7, 1.9)])
