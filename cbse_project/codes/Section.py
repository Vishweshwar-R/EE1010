import numpy as np
import matplotlib.pyplot as plt

# A(2, 3), B(6, -3); P(4, m) divides AB in the ratio k:1
A = np.array([2.0, 3.0])
B = np.array([6.0, -3.0])

# x-coordinate: 4 = (6k + 2)/(k + 1)  ->  k = 1
k = (4.0 - A[0]) / (B[0] - 4.0)
# y-coordinate: m = (k*B_y + A_y)/(k + 1)
m = (k * B[1] + A[1]) / (k + 1)
P = np.array([4.0, m])
print("k =", k, " m =", m)
assert np.isclose(k, 1) and np.isclose(m, 0)

plt.figure(figsize=(5, 4))
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-')
for pt, name, off in [(A, 'A(2, 3)', (-0.2, 0.3)),
                      (B, 'B(6, -3)', (-0.3, -0.7)),
                      (P, 'P(4, 0)', (0.15, 0.3))]:
    plt.plot(*pt, 'ro')
    plt.annotate(name, pt + np.array(off))
plt.axhline(0, color='k', lw=0.5)
plt.axvline(0, color='k', lw=0.5)
plt.xlabel('$x$'); plt.ylabel('$y$')
plt.grid(alpha=0.3); plt.axis('equal')
plt.savefig('../figs/Section.png', dpi=200, bbox_inches='tight')
