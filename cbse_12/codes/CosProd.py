import numpy as np
import matplotlib.pyplot as plt

# Q22: int cos2x cos4x cos6x dx
import sympy as sp
x = sp.symbols("x")
f = sp.cos(2*x) * sp.cos(4*x) * sp.cos(6*x)
F = (x + sp.sin(12*x)/12 + sp.sin(8*x)/8 + sp.sin(4*x)/4) / 4
print("residual:", sp.simplify(sp.diff(F, x) - f))
print("numeric:", [round(float((sp.diff(F, x) - f).subs(x, t)), 12) for t in (0.1, 0.7, 1.9)])
