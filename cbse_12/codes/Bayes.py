import numpy as np
import matplotlib.pyplot as plt
# Q28: a card is lost; two cards drawn from the remaining 51 are both spades. P(lost card is a spade)?
from fractions import Fraction as F
p_lost_spade = F(1, 4)
like_spade = F(12, 51) * F(11, 50)        # 12 spades left in 51 cards
like_other = F(13, 51) * F(12, 50)        # 13 spades left in 51 cards
post = p_lost_spade * like_spade / (p_lost_spade * like_spade + (1 - p_lost_spade) * like_other)
print("exact posterior =", post)
rng = np.random.default_rng(0)
N = 4_000_000                             # cards 0..12 are spades
lost = rng.integers(0, 52, N)
d1 = rng.integers(0, 51, N); d1 += d1 >= lost
d2 = rng.integers(0, 50, N)
lo, hi = np.minimum(lost, d1), np.maximum(lost, d1)
d2 += d2 >= lo; d2 += d2 >= hi
ok = (d1 < 13) & (d2 < 13)
print("simulation      =", np.mean(lost[ok] < 13), " 11/50 =", 11 / 50)
