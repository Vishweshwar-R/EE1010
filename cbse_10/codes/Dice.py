import itertools
from fractions import Fraction

# all 36 outcomes of two dice
S = list(itertools.product(range(1, 7), repeat=2))
doublet = [s for s in S if s[0] == s[1]]
sum10 = [s for s in S if sum(s) == 10]

p1 = Fraction(len(doublet), len(S))
p2 = Fraction(len(sum10), len(S))
print("n(S) =", len(S))
print("P(doublet) =", p1)
print("P(sum 10)  =", p2)
assert p1 == Fraction(1, 6) and p2 == Fraction(1, 12)
