import itertools
from fractions import Fraction

# joint PMF of two independent fair dice: p(i,j) = p_X(i) p_Y(j) = 1/36
pX = {i: Fraction(1, 6) for i in range(1, 7)}
p = {(i, j): pX[i] * pX[j] for i, j in itertools.product(pX, pX)}
assert sum(p.values()) == 1

p1 = sum(v for (i, j), v in p.items() if i == j)        # doublet
p2 = sum(v for (i, j), v in p.items() if i + j == 10)   # sum 10
print("P(doublet) =", p1)
print("P(sum 10)  =", p2)
assert p1 == Fraction(1, 6) and p2 == Fraction(1, 12)
