import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import dir_vec, line_gen_num, line_isect
from CoordGeo.conics.funcs import circ_gen, parab_gen
from CoordGeo.plotting.funcs import label_pts
# Q25: (a) area of {x^2+y^2 <= 16a^2, y^2 <= 6ax}  (a = 1);  (b) triangle bounded by three lines
import sympy as sp
from scipy.integrate import quad
col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
a = sp.symbols("a", positive=True); x = sp.symbols("x", positive=True)
I1 = sp.integrate(sp.sqrt(6*a*x), (x, 0, 2*a))
I2 = sp.integrate(sp.sqrt(16*a**2 - x**2), (x, 2*a, 4*a))
area_a = sp.simplify(2*(I1 + I2))
print("(a) area =", area_a, " = (4a^2/3)(4pi + sqrt3):", sp.simplify(area_a - sp.Rational(4, 3)*a**2*(4*sp.pi + sp.sqrt(3))) == 0)
num, _ = quad(lambda t: 2*(np.sqrt(6*t) + 0), 0, 2)
num = 2*(quad(lambda t: np.sqrt(6*t), 0, 2)[0] + quad(lambda t: np.sqrt(16 - t**2), 2, 4)[0])
print("    numeric (a=1):", num, " formula:", 4/3*(4*np.pi + np.sqrt(3)))
# (b) vertices from line_isect:  n.x = c
n1, c1 = col(4, -1), -5      # 4x - y + 5 = 0
n2, c2 = col(1, 1), 5        # x + y - 5 = 0
n3, c3 = col(1, -4), -5      # x - 4y + 5 = 0
A_ = line_isect(n1, c1, n3, c3); B_ = line_isect(n1, c1, n2, c2); C_ = line_isect(n2, c2, n3, c3)
print("(b) vertices:", A_.T, B_.T, C_.T)
area_b = 0.5 * abs(LA.det(np.block([dir_vec(A_, B_), dir_vec(A_, C_)])))
f_up = lambda t: (4*t + 5) if t < 0 else (5 - t)
f_lo = lambda t: (t + 5) / 4
int_b = quad(lambda t: f_up(t) - f_lo(t), -1, 0)[0] + quad(lambda t: f_up(t) - f_lo(t), 0, 3)[0]
print("    area by determinant:", area_b, " by integration:", int_b)

fig, ax = plt.subplots(1, 2, figsize=(10, 4.2))
O = col(0, 0)
Cc = circ_gen(O, 4); ax[0].plot(Cc[0, :], Cc[1, :], "b")
yy = np.linspace(-4, 4, 400); ax[0].plot(parab_gen(yy, 6), yy, "r")
xx = np.linspace(2, 4, 100)
ax[0].fill_between(xx, -np.sqrt(16 - xx**2), np.sqrt(16 - xx**2), color="tab:blue", alpha=0.25)
xx = np.linspace(0, 2, 100)
ax[0].fill_between(xx, -np.sqrt(6*xx), np.sqrt(6*xx), color="tab:blue", alpha=0.25)
ax[0].set_aspect("equal"); ax[0].grid(alpha=0.3); ax[0].set_xlim(-5, 5)
ax[0].set_title(r"(a) $x^2+y^2\leq 16$, $y^2\leq 6x$  ($a=1$)")
V = np.block([A_, B_, C_])
for P, Q in [(A_, B_), (B_, C_), (C_, A_)]:
    L = line_gen_num(P, Q, 20); ax[1].plot(L[0, :], L[1, :], "b")
ax[1].fill(V[0, :], V[1, :], color="tab:blue", alpha=0.25)
ax[1].scatter(V[0, :], V[1, :], color="r", zorder=3); label_pts(V, ["A(-1,1)", "B(0,5)", "C(3,2)"])
ax[1].grid(alpha=0.3); ax[1].set_title("(b) triangle ABC, area = 7.5")
plt.tight_layout()
#If using termux
plt.savefig('figs/Area.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/Area.png"))
#else
#plt.show()
