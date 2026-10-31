import numpy as np
import matplotlib.pyplot as plt
# Q24: (a) inverse by elementary row operations, (b) the linear system
import sympy as sp
A = sp.Matrix([[3, 0, -1], [2, 3, 0], [0, 4, 1]])
M = A.row_join(sp.eye(3))
ops = [("R1 -> R1 - R2", lambda M: M.row_op(0, lambda v, j: v - M[1, j])),
       ("R2 -> R2 - 2R1", lambda M: M.row_op(1, lambda v, j: v - 2*M[0, j])),
       ("R2 -> R2 - 2R3", lambda M: M.row_op(1, lambda v, j: v - 2*M[2, j])),
       ("R1 -> R1 + 3R2", lambda M: M.row_op(0, lambda v, j: v + 3*M[1, j])),
       ("R3 -> R3 - 4R2", lambda M: M.row_op(2, lambda v, j: v - 4*M[1, j])),
       ("R1 -> R1 + R3", lambda M: M.row_op(0, lambda v, j: v + M[2, j]))]
for name, op in ops:
    op(M); print(name, "\n", M)
print("inverse =", M[:, 3:], "\n matches A.inv():", M[:, 3:] == A.inv())
An = np.array(A.tolist(), dtype=float)
print("numpy check A @ A^-1 = I:", np.allclose(An @ np.array(M[:, 3:].tolist(), dtype=float), np.eye(3)))
# (b) system as printed: row-reduce the augmented matrix [A | b]
B = sp.Matrix([[2, 3, 10], [4, -6, 5], [6, 9, -20]]); rhs = sp.Matrix([4, 1, 2])
Ab = B.row_join(rhs)
Ab.row_op(1, lambda v, j: v - 2*Ab[0, j])      # R2 -> R2 - 2R1
Ab.row_op(2, lambda v, j: v - 3*Ab[0, j])      # R3 -> R3 - 3R1
print("[A|b] after R2-2R1, R3-3R1 =", Ab.tolist())
print("|A| from the triangular form =", Ab[0, 0]*Ab[1, 1]*Ab[2, 2], " |A| =", B.det())
z = Ab[2, 3]/Ab[2, 2]; y = (Ab[1, 3] - Ab[1, 2]*z)/Ab[1, 1]; x = (Ab[0, 3] - Ab[0, 1]*y - Ab[0, 2]*z)/Ab[0, 0]
print("x, y, z =", x, y, z, " check A^-1 b =", (B.inv()*rhs).T)
assert (x, y, z) == (sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 5)) and B.det() == 1200
