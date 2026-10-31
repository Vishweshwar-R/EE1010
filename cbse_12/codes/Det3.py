import numpy as np
import matplotlib.pyplot as plt

# Q15: determinant |x x^2 x^3-1; y y^2 y^3-1; z z^2 z^3-1| = (xyz - 1)(y-x)(z-x)(z-y)
import sympy as sp
x, y, z = sp.symbols("x y z")
D = sp.Matrix([[v, v**2, v**3 - 1] for v in (x, y, z)]).det()
print(sp.factor(D))
print("equal to (xyz-1)(y-x)(z-x)(z-y):", sp.simplify(D - (x*y*z - 1)*(y - x)*(z - x)*(z - y)) == 0)
