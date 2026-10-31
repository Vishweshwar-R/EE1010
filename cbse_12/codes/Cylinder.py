import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import line_gen_num
# Q29: right circular cylinder of greatest curved surface inscribed in a cone has r = R/2
col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
R, H = 1.0, 1.0
csa = lambda r: 2 * np.pi * r * H * (R - r) / R      # h = H(R - r)/R
r = np.linspace(0, R, 400)
print("argmax r =", r[np.argmax(csa(r))], " R/2 =", R / 2)
import sympy as sp
rr, RR, HH = sp.symbols("r R H", positive=True)
S = 2 * sp.pi * rr * HH * (RR - rr) / RR
print("dS/dr = 0 ->", sp.solve(sp.diff(S, rr), rr), " d2S/dr2 =", sp.diff(S, rr, 2))
fig, ax = plt.subplots(1, 2, figsize=(9, 3.8))
ax[0].plot(r, csa(r), "b"); ax[0].axvline(R / 2, color="r", ls="--")
ax[0].set_xlabel("r (R = H = 1)"); ax[0].set_ylabel("curved surface area"); ax[0].grid(alpha=0.3)
ax[0].set_title("CSA is maximum at r = R/2")
Lc, Rc, Ap = col(-R, 0), col(R, 0), col(0, H)
for P_, Q_ in [(Lc, Rc), (Rc, Ap), (Ap, Lc)]:
    L = line_gen_num(P_, Q_, 20); ax[1].plot(L[0, :], L[1, :], "b")
rm = R / 2; hm = H * (R - rm) / R
Cy = np.block([col(-rm, 0), col(rm, 0), col(rm, hm), col(-rm, hm), col(-rm, 0)])
ax[1].plot(Cy[0, :], Cy[1, :], "r"); ax[1].fill(Cy[0, :], Cy[1, :], color="tab:red", alpha=0.2)
ax[1].set_aspect("equal"); ax[1].set_title("cross-section: r = R/2, h = H/2"); ax[1].grid(alpha=0.3)
plt.tight_layout()
#If using termux
plt.savefig('figs/Cylinder.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/Cylinder.png"))
#else
#plt.show()
