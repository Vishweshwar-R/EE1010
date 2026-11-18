import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if


rng = np.random.default_rng(4)
N = 10**6                                         # number of trials
pA, pB = 3 / 7, 2 / 5
# joint pmf of the indicators (I_A, I_B):  p(a, b) = pA^a (1-pA)^(1-a) pB^b (1-pB)^(1-b)
cases = [(0, 0), (0, 1), (1, 0), (1, 1)]
p_theory = np.array([pA**a * (1 - pA)**(1 - a) * pB**b * (1 - pB)**(1 - b) for a, b in cases])
IA = rng.random(N) < pA; IB = rng.random(N) < pB
p_sim = np.array([np.mean((IA == a) & (IB == b)) for a, b in cases])
print("P(A' and B'): theory", round(p_theory[0], 5), " simulation", round(p_sim[0], 5), " 12/35 =", round(12 / 35, 5))
assert np.allclose(p_theory, p_sim, atol=3e-3) and np.isclose(p_theory[0], 12 / 35)

i = np.arange(4)
plt.figure(figsize=(5.5, 4))
plt.stem(i - 0.07, p_theory, linefmt='b-', markerfmt='bo', basefmt='k-', label='theory')
plt.stem(i + 0.07, p_sim, linefmt='r--', markerfmt='rx', basefmt='k-', label='simulation ($N=10^6$)')
plt.xticks(i, ['(0,0)', '(0,1)', '(1,0)', '(1,1)'])
plt.xlabel('$(I_A, I_B)$'); plt.ylabel('$p(a,b)$'); plt.legend(); plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/2.2.7.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/2.2.7.png"))
#else
#plt.show()
