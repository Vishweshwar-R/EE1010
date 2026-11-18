import numpy as np

# (a) boat: 24/(18-x) - 24/(18+x) = 1  ->  x^2 + 48x - 324 = 0
r = np.roots([1, 48, -324])
xa = r[r > 0][0]
print("(a) speed of stream =", xa, "km/h")
assert np.isclose(24 / (18 - xa) - 24 / (18 + xa), 1)

# (b) train: 63/x + 72/(x+6) = 3  ->  x^2 - 39x - 126 = 0
r = np.roots([1, -39, -126])
xb = r[r > 0][0]
print("(b) original speed =", xb, "km/h")
assert np.isclose(63 / xb + 72 / (xb + 6), 3)
