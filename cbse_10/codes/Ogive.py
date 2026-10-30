import numpy as np
import matplotlib.pyplot as plt

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

plt.figure(figsize=(5.5, 4))
plt.plot(upper, cf, 'b-')
plt.plot(upper, cf, 'ro')
for x, y in zip(upper, cf):
    plt.annotate(f'({x}, {y})', (x, y), textcoords='offset points', xytext=(-30, 6), fontsize=8)
plt.xlabel('Daily income (in Rs.)'); plt.ylabel('Cumulative frequency')
plt.grid(alpha=0.3)
plt.savefig('../figs/Ogive.png', dpi=200, bbox_inches='tight')
