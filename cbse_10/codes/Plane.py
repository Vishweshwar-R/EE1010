import numpy as np

# 1500/x - 1500/(x+100) = 1/2  ->  x^2 + 100x - 300000 = 0
roots = np.roots([1, 100, -300000])
print("roots =", roots)
x = roots[roots > 0][0]
print("usual speed =", x, "km/h")
assert np.isclose(1500 / x - 1500 / (x + 100), 0.5)
