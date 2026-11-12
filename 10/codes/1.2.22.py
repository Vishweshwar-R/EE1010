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

f = np.array([49, 133, 63, 15, 6, 7, 4, 2, 1])
lower = np.arange(5, 50, 5)                 # class lower limits 5, 10, ..., 45
cf = np.cumsum(f)
N = cf[-1]

# median class: first class with cf >= N/2
i = np.argmax(cf >= N / 2)
l, h = lower[i], 5
cf_prev = cf[i - 1] if i > 0 else 0
median = l + (N / 2 - cf_prev) / f[i] * h
print("N =", int(N), " median class =", (int(l), int(l + h)), " median =", round(float(median), 2))
assert np.isclose(median, 13.42, atol=0.005)

# less than type ogive: points (upper class limit, cumulative frequency) as columns
pts = np.block([[np.concatenate(([5], lower + 5))],
                [np.concatenate(([0], cf))]]).astype(float)
plt.figure(figsize=(5.5, 4))
for k in range(pts.shape[1] - 1):
    x = line_gen(pts[:, [k]], pts[:, [k + 1]])
    plt.plot(x[0, :], x[1, :], 'b-')
plt.scatter(pts[0, :], pts[1, :], color='b', s=10)

M = np.array([[median], [N / 2]])           # point of the ogive at N/2
Y = np.array([[5.0], [N / 2]])
X = np.array([[median], [0.0]])
for P, Q in [(Y, M), (M, X)]:
    x = line_gen(P, Q)
    plt.plot(x[0, :], x[1, :], 'r--')
label_pts(X, [f'median = {median:.2f}'])
plt.xlabel('Salary (in thousand Rs.)'); plt.ylabel('Cumulative frequency')
plt.grid(alpha=0.3)

#If using termux
plt.savefig('figs/1.2.22.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.22.png"))
#else
#plt.show()
