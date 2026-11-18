import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if


from math import comb

rng = np.random.default_rng(5)
N = 10**6                                         # number of trials
# L = 1 if the lost card is a spade.  prior pmf: p_L(1) = 1/4, p_L(0) = 3/4
prior = np.array([3 / 4, 1 / 4])
like = np.array([comb(13, 2), comb(12, 2)]) / comb(51, 2)       # P(both drawn are spades | L = l)
post_theory = prior * like / np.sum(prior * like)               # p_{L|A}(l)

# simulation: shuffle the pack, the first card is lost, the next two are drawn
deck = np.array([1] * 13 + [0] * 39)
count = np.zeros(2); total = 0
for _ in range(N // 10):
    d = rng.permutation(deck)
    if d[1] == 1 and d[2] == 1:
        count[d[0]] += 1; total += 1
post_sim = count / total
print("p(L=1 | both spades): theory", round(post_theory[1], 5), " simulation", round(post_sim[1], 5), " 11/50 =", 11 / 50)
assert np.isclose(post_theory[1], 11 / 50) and abs(post_sim[1] - 11 / 50) < 0.01

l = np.arange(2)
plt.figure(figsize=(5, 3.8))
plt.stem(l - 0.07, post_theory, linefmt='b-', markerfmt='bo', basefmt='k-', label='theory')
plt.stem(l + 0.07, post_sim, linefmt='r--', markerfmt='rx', basefmt='k-', label='simulation')
plt.xticks(l, ['not a spade', 'a spade']); plt.ylabel('$p_{L|A}(l)$'); plt.legend(); plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/2.2.18.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/2.2.18.png"))
#else
#plt.show()
