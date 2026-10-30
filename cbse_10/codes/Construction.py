import numpy as np
import matplotlib.pyplot as plt

# triangle ABC: BC = 6, AB = 5, angle ABC = 60 deg
B = np.array([0.0, 0.0])
C = np.array([6.0, 0.0])
A = 5 * np.array([np.cos(np.pi / 3), np.sin(np.pi / 3)])

# ray BX below BC, with B1..B4 at equal spacing
u = np.array([np.cos(-np.pi / 6), np.sin(-np.pi / 6)])
Bs = [B + i * 1.5 * u for i in range(1, 5)]
B3, B4 = Bs[2], Bs[3]

# C' = point on BC with B3C' parallel to B4C
t = -B3[1] / (C - B4)[1]
Cp = B3 + t * (C - B4)
Ap = B + 0.75 * (A - B)            # C'A' parallel to CA
print("C' =", Cp, " A' =", Ap)
assert np.allclose(Cp, [4.5, 0])
ratios = [np.linalg.norm(Ap - B) / np.linalg.norm(A - B),
          np.linalg.norm(Cp - B) / np.linalg.norm(C - B),
          np.linalg.norm(Ap - Cp) / np.linalg.norm(A - C)]
print("side ratios =", [round(float(r), 4) for r in ratios])
assert np.allclose(ratios, 0.75)

plt.figure(figsize=(6, 4.5))
plt.fill(*np.array([A, B, C]).T, alpha=0.15, color='b')
plt.plot(*np.array([A, B, C, A]).T, 'b-')
plt.plot(*np.array([Ap, B, Cp, Ap]).T, 'r-')
plt.plot(*np.array([B, B4]).T, 'k:')
plt.plot(*np.array([B4, C]).T, 'k:')
plt.plot(*np.array([B3, Cp]).T, 'k:')
for P, n, off in [(A, 'A', (0, 0.15)), (B, 'B', (-0.3, 0.1)), (C, 'C', (0.1, 0.1)),
                  (Ap, "A'", (-0.4, 0.1)), (Cp, "C'", (0, 0.2))]:
    plt.plot(*P, 'ko', ms=3); plt.annotate(n, P + np.array(off))
for i, P in enumerate(Bs, 1):
    plt.plot(*P, 'k.'); plt.annotate(f'$B_{i}$', P + np.array([0.1, -0.35]))
plt.axis('equal'); plt.axis('off')
plt.savefig('../figs/Construction.png', dpi=200, bbox_inches='tight')
