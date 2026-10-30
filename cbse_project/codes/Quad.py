import numpy as np
import matplotlib.pyplot as plt

def shoelace(V):
    x, y = V[:, 0], V[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))

# (a) parallelogram ABCD with a = b = 1
Pa = np.array([[-2, 1], [1, 0], [4, 1], [1, 2]], dtype=float)
A, B, C, D = Pa
assert np.allclose((A + C) / 2, (B + D) / 2)       # diagonals bisect each other
sides = [np.linalg.norm(Pa[(i + 1) % 4] - Pa[i]) for i in range(4)]
print("sides =", [round(float(x), 4) for x in sides])
assert np.allclose(sides, np.sqrt(10))

# (b) quadrilateral ABCD
Pb = np.array([[-5, 7], [-4, -5], [-1, -6], [4, 5]], dtype=float)
area = shoelace(Pb)
print("area =", area)
assert np.isclose(area, 72)

fig, ax = plt.subplots(1, 2, figsize=(8, 3.6))
for a, V, title in [(ax[0], Pa, '(a)'), (ax[1], Pb, '(b)')]:
    a.fill(V[:, 0], V[:, 1], alpha=0.25)
    a.plot(*np.vstack([V, V[0]]).T, 'b-')
    for p, n in zip(V, 'ABCD'):
        a.plot(*p, 'ro'); a.annotate(n, p + 0.2)
    a.set_title(title); a.grid(alpha=0.3); a.set_aspect('equal')
plt.savefig('../figs/Quad.png', dpi=200, bbox_inches='tight')
