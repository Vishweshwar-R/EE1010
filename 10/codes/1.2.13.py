import numpy as np
from sympy import factorint

p, q = 404, 96
primes = [2, 3, 101]
e = np.array([factorint(p).get(r, 0) for r in primes])      # exponent vector of 404
f = np.array([factorint(q).get(r, 0) for r in primes])      # exponent vector of 96
hcf = int(np.prod([r**k for r, k in zip(primes, np.minimum(e, f))]))
lcm = int(np.prod([r**k for r, k in zip(primes, np.maximum(e, f))]))
print("e =", e, " f =", f, " HCF =", hcf, " LCM =", lcm)
assert hcf == 4 and lcm == 9696 and hcf * lcm == p * q
