import numpy as np
import matplotlib.pyplot as plt

# Q10: (a) int (x-1)/((x-2)(x-3)) dx   (b) int e^x / sqrt(5 - 4e^x - e^2x) dx
import sympy as sp
x = sp.symbols("x")
f = (x - 1) / ((x - 2) * (x - 3))
print("partial fractions:", sp.apart(f))
F1 = -sp.log(sp.Abs(x - 2)) + 2 * sp.log(sp.Abs(x - 3))
import math
dF = lambda t: -1/(t - 2) + 2/(t - 3)
print("check (a): F'(x) - f(x) at x=4,5,-1:", [round(dF(t) - float(f.subs(x, t)), 12) for t in (4, 5, -1)])
g = sp.exp(x) / sp.sqrt(5 - 4 * sp.exp(x) - sp.exp(2 * x))
F2 = sp.asin((sp.exp(x) + 2) / 3)
for v in [-2, -1, -0.5, -0.1]:   # domain: 5 - 4e^x - e^2x > 0  <=>  x < 0
    print("check (b) at x =", v, ":", float((sp.diff(F2, x) - g).subs(x, v)))
