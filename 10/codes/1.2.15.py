import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom CoordGeo modules
from CoordGeo.line.funcs import dir_vec, line_gen
from CoordGeo.plotting.funcs import label_pts

def area_tri(P, Q, R):
    # area = (1/2)|det[Q - P, R - P]|
    return 0.5 * abs(LA.det(np.block([dir_vec(P, Q), dir_vec(P, R)])))

# (a) parallelogram ABCD: A + C = B + D with B = (a, 0), C = (4, b)
A = np.array([[-2], [1]]); D = np.array([[1], [2]])
a = A[0, 0] + 4 - D[0, 0]            # x: -2 + 4 = a + 1
b = D[1, 0] - A[1, 0]                # y: 1 + b = 0 + 2
B = np.array([[a], [0]]); C = np.array([[4], [b]])
print("a =", a, " b =", b)
assert (a, b) == (1, 1)
sides = [LA.norm(dir_vec(P, Q)) for P, Q in [(A, B), (B, C), (C, D), (D, A)]]
print("sides =", np.round(sides, 4))
assert np.allclose(sides, np.sqrt(10))

# (b) quadrilateral ABCD: area = ar(ABC) + ar(ADC)
A2 = np.array([[-5], [7]]); B2 = np.array([[-4], [-5]])
C2 = np.array([[-1], [-6]]); D2 = np.array([[4], [5]])
area = area_tri(A2, B2, C2) + area_tri(A2, D2, C2)
print("area =", round(float(area), 6))
assert np.isclose(area, 72)

fig, ax = plt.subplots(1, 2, figsize=(8, 3.6))
for axis, V, title in [(ax[0], [A, B, C, D], '(a)'), (ax[1], [A2, B2, C2, D2], '(b)')]:
    plt.sca(axis)
    for P, Q in zip(V, V[1:] + V[:1]):
        x = line_gen(P, Q)
        plt.plot(x[0, :], x[1, :], 'b-')
    pts = np.block(V)
    plt.scatter(pts[0, :], pts[1, :], color='r')
    label_pts(pts, list('ABCD'))
    plt.title(title); plt.grid(alpha=0.3); axis.set_aspect('equal')

#If using termux
plt.savefig('figs/1.2.15.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/1.2.15.png"))
#else
#plt.show()
