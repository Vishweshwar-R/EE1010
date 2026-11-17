import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

rng = np.random.default_rng(1)
N = 10**6                                        # number of trials
X = rng.integers(1, 7, N); Y = rng.integers(1, 7, N)
S = X + Y

s = np.arange(2, 13)
p_theory = (6 - np.abs(s - 7)) / 36              # p_S = p_X * p_Y (convolution)
p_sim = np.array([np.mean(S == k) for k in s])
print("P(doublet): theory", round(1 / 6, 4), " simulation", round(np.mean(X == Y), 4))
print("P(sum 10) : theory", round(p_theory[s == 10][0], 4), " simulation", round(p_sim[s == 10][0], 4))
assert np.allclose(p_theory, p_sim, atol=3e-3) and abs(np.mean(X == Y) - 1 / 6) < 3e-3

plt.figure(figsize=(5.5, 4))
plt.stem(s - 0.1, p_theory, linefmt='b-', markerfmt='bo', basefmt='k-', label='theory $p_S(s)$')
plt.stem(s + 0.1, p_sim, linefmt='r--', markerfmt='rx', basefmt='k-', label=f'simulation ($N=10^6$)')
plt.xlabel('$s$'); plt.ylabel('$p_S(s)$'); plt.legend(); plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/1.2.11.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.11.png"))
#else
#plt.show()
