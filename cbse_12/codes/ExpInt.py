import numpy as np
import matplotlib.pyplot as plt

# Q11: int e^x (2 + sin 2x)/(2 cos^2 x) dx = e^x tan x + C
import sympy as sp
x = sp.symbols("x")
f = sp.exp(x) * (2 + sp.sin(2 * x)) / (2 * sp.cos(x) ** 2)
print("d/dx(e^x tan x) - integrand =", sp.simplify(sp.diff(sp.exp(x) * sp.tan(x), x) - f))
print("sin2x/(2cos^2x) simplifies to:", sp.simplify(sp.sin(2 * x) / (2 * sp.cos(x) ** 2)))
