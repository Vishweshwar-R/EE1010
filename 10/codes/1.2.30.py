import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# (a) mean = 18  ->  18(40 + f) = 704 + 20f
f = (18 * 40 - 704) / (20 - 18)
print("(a) f =", f)
assert f == 8

# (b) less than type ogive
upper = np.array([100, 120, 140, 160, 180, 200])
freq = np.array([0, 12, 14, 8, 6, 10])
cf = np.cumsum(freq)
print("(b) cumulative frequencies =", cf)
assert list(cf) == [0, 12, 26, 34, 40, 50]

pts = np.block([[upper], [cf]]).astype(float)     # points as columns
plt.figure(figsize=(5.5, 4))
for k in range(pts.shape[1] - 1):
    x = line_gen(pts[:, [k]], pts[:, [k + 1]])
    plt.plot(x[0, :], x[1, :], 'b-')
plt.scatter(pts[0, :], pts[1, :], color='r')
label_pts(pts, [f'$({int(p[0])},{int(p[1])})$' for p in pts.T])
plt.xlabel('Daily income (in Rs.)'); plt.ylabel('Cumulative frequency')
plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/1.2.30.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.30.png"))
#else
#plt.show()
