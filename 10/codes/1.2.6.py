import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

rng = np.random.default_rng(2)
N = 10**6                                        # number of trials
X = rng.integers(2, 100, N)                      # uniform on {2, ..., 99}

k = np.arange(2, 100)
r = np.arange(8)
p_theory = np.array([np.sum(k % 8 == i) for i in r]) / 98     # pmf of R = X mod 8
p_sim = np.array([np.mean(X % 8 == i) for i in r])
print("P(8 | X): theory", round(12 / 98, 4), " simulation", round(p_sim[0], 4))
print("P(8 does not divide X): theory", round(43 / 49, 4), " simulation", round(1 - p_sim[0], 4))
assert np.allclose(p_theory, p_sim, atol=3e-3) and p_theory[0] == 12 / 98

plt.figure(figsize=(5.5, 4))
plt.stem(r - 0.1, p_theory, linefmt='b-', markerfmt='bo', basefmt='k-', label='theory $p_R(r)$')
plt.stem(r + 0.1, p_sim, linefmt='r--', markerfmt='rx', basefmt='k-', label='simulation ($N=10^6$)')
plt.xlabel('r = X mod 8'); plt.ylabel('$p_R(r)$'); plt.legend(); plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/1.2.6.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.6.png"))
#else
#plt.show()
