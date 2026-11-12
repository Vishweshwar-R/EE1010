import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import norm_vec, line_intersect, line_gen, rotmat
from CoordGeo.plotting.funcs import label_pts
from CoordGeo.params import e1

# triangle ABC: BC = 6, AB = 5, angle ABC = 60 deg, with B at the origin
B = np.array([[0], [0]])
C = 6 * e1
A = 5 * rotmat(np.pi / 3) @ e1

# ray BX below BC, with B1..B4 at equal spacing
u = rotmat(-np.pi / 6) @ e1
Bs = [i * 1.5 * u for i in range(1, 5)]
B3, B4 = Bs[2], Bs[3]

# C' : BC meets the line through B3 parallel to B4C
Cp = line_intersect(norm_vec(B, C), B, norm_vec(B4, C), B3)
# A' : BA meets the line through C' parallel to CA
Ap = line_intersect(norm_vec(B, A), B, norm_vec(C, A), Cp)
print("C' =", Cp.ravel().round(4) + 0.0, " A' =", Ap.ravel().round(4) + 0.0)

ratios = [LA.norm(Ap - B) / LA.norm(A - B), LA.norm(Cp - B) / LA.norm(C - B),
          LA.norm(Ap - Cp) / LA.norm(A - C)]
print("side ratios =", np.round(ratios, 4))
assert np.allclose(ratios, 0.75) and np.allclose(Cp, [[4.5], [0]])

plt.figure(figsize=(6, 4.5))
for P, Q, col in [(A, B, 'b-'), (B, C, 'b-'), (C, A, 'b-'), (Ap, B, 'r-'), (B, Cp, 'r-'), (Cp, Ap, 'r-'),
                  (B, B4, 'k:'), (B4, C, 'k:'), (B3, Cp, 'k:')]:
    x = line_gen(P, Q)
    plt.plot(x[0, :], x[1, :], col)
pts = np.block([A, B, C, Ap, Cp] + Bs)
plt.scatter(pts[0, :], pts[1, :], color='k', s=10)
label_pts(pts, ['$A$', '$B$', '$C$', "$A'$", "$C'$", '$B_1$', '$B_2$', '$B_3$', '$B_4$'])
plt.axis('equal'); plt.axis('off')

#If using termux
plt.savefig('figs/1.2.26.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.26.png"))
#else
#plt.show()
