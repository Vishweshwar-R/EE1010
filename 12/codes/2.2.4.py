import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if


from math import comb

rng = np.random.default_rng(3)
N = 10**6                                         # number of trials

# (a) X = number of diamonds in 4 draws with replacement:  p_X(r) = C(4,r)(1/4)^r (3/4)^(4-r)
r = np.arange(5)
pa_theory = np.array([comb(4, k) * 0.25**k * 0.75**(4 - k) for k in r])
Xa = (rng.random((N, 4)) < 0.25).sum(axis=1)
pa_sim = np.array([np.mean(Xa == k) for k in r])
print("(a) P(X >= 3): theory", round(pa_theory[3:].sum(), 5), " simulation", round(np.mean(Xa >= 3), 5), " 13/256 =", round(13 / 256, 5))

# (b) Z = number of students on time, with P(A) = 2/7, P(B) = 4/7 independent
z = np.arange(3)
pb_theory = np.array([(5 / 7) * (3 / 7), (2 / 7) * (3 / 7) + (5 / 7) * (4 / 7), (2 / 7) * (4 / 7)])
Z = (rng.random(N) < 2 / 7).astype(int) + (rng.random(N) < 4 / 7).astype(int)
pb_sim = np.array([np.mean(Z == k) for k in z])
print("(b) P(Z = 1): theory", round(pb_theory[1], 5), " simulation", round(pb_sim[1], 5), " 26/49 =", round(26 / 49, 5))
assert np.allclose(pa_theory, pa_sim, atol=3e-3) and np.allclose(pb_theory, pb_sim, atol=3e-3)

fig, ax = plt.subplots(1, 2, figsize=(8, 3.6))
for a_, k, th, sm, name, t in [(ax[0], r, pa_theory, pa_sim, '$p_X(r)$', '(a)'), (ax[1], z, pb_theory, pb_sim, '$p_Z(z)$', '(b)')]:
    a_.stem(k - 0.07, th, linefmt='b-', markerfmt='bo', basefmt='k-', label='theory')
    a_.stem(k + 0.07, sm, linefmt='r--', markerfmt='rx', basefmt='k-', label='simulation')
    a_.set_ylabel(name); a_.set_title(t); a_.legend(fontsize=8); a_.grid(alpha=0.3)

#If using termux
plt.savefig('figs/2.2.4.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/2.2.4.png"))
#else
#plt.show()
