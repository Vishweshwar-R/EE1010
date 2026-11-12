import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import line_gen_num
# Q19: (a) R = {(a,b): |a-b| even} on {1..7} is an equivalence relation; (b) f(x) = (4x+3)/(6x-4)
import sympy as sp
S = range(1, 8)
R = {(a, b) for a in S for b in S if abs(a - b) % 2 == 0}
refl = all((a, a) in R for a in S)
symm = all((b, a) in R for (a, b) in R)
trans = all((a, c) in R for (a, b) in R for (b2, c) in R if b == b2)
print("reflexive:", refl, " symmetric:", symm, " transitive:", trans)
x, y = sp.symbols("x y")
f = (4*x + 3) / (6*x - 4)
print("f(f(x)) =", sp.simplify(f.subs(x, f)), "  => f is its own inverse")
print("solve y = f(x) for x:", sp.solve(sp.Eq(y, f), x))
fig, ax = plt.subplots(1, 2, figsize=(9, 3.8))
M = np.array([[1 if (a, b) in R else 0 for b in S] for a in S])
ax[0].imshow(M, cmap="Blues"); ax[0].set_xticks(range(7)); ax[0].set_xticklabels(S)
ax[0].set_yticks(range(7)); ax[0].set_yticklabels(S); ax[0].set_title("(a) relation matrix of R")
xs1 = np.linspace(-3, 2/3 - 0.02, 300); xs2 = np.linspace(2/3 + 0.02, 4, 300)
fx = lambda t: (4*t + 3) / (6*t - 4)
ax[1].plot(xs1, fx(xs1), "b"); ax[1].plot(xs2, fx(xs2), "b")
D = line_gen_num(np.array([[-3.], [-3.]]), np.array([[4.], [4.]]), 20)
ax[1].plot(D[0, :], D[1, :], "r--", label="y = x")
ax[1].set_ylim(-3, 4); ax[1].set_xlim(-3, 4); ax[1].grid(alpha=0.3); ax[1].legend()
ax[1].set_title("(b) graph of f is symmetric about y = x")
plt.tight_layout()
#If using termux
plt.savefig('figs/2.2.19.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/2.2.19.png"))
#else
#plt.show()
