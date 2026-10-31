import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Q6: (a) P(at least 3 diamonds in 4 draws with replacement), (b) P(exactly one on time)
from fractions import Fraction as F
from math import comb
p = F(1, 4)
pk = [comb(4, k) * p**k * (1 - p)**(4 - k) for k in range(5)]
print("P(X>=3) =", pk[3] + pk[4])
rng = np.random.default_rng(1)
draws = rng.random((10**6, 4)) < 0.25
print("simulation:", np.mean(draws.sum(axis=1) >= 3), " 13/256 =", 13 / 256)
pa, pb = F(2, 7), F(4, 7)
print("P(only one) =", pa * (1 - pb) + (1 - pa) * pb)
plt.figure(figsize=(5, 3.2))
plt.bar(range(5), [float(v) for v in pk], color=["tab:blue"] * 3 + ["tab:red"] * 2)
plt.xlabel("number of diamonds in 4 draws"); plt.ylabel("probability")
plt.title("Binomial(4, 1/4); red bars: at least 3")
plt.tight_layout()
#If using termux
plt.savefig('figs/Cards.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/Cards.png"))
#else
#plt.show()
