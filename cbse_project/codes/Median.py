import numpy as np
import matplotlib.pyplot as plt

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

# less-than ogive: upper limits vs cumulative frequency
xs = np.concatenate(([5], lower + 5))
ys = np.concatenate(([0], cf))
plt.figure(figsize=(5.5, 4))
plt.plot(xs, ys, 'b-o', ms=3)
plt.hlines(N / 2, 5, median, colors='r', linestyles='--')
plt.vlines(median, 0, N / 2, colors='r', linestyles='--')
plt.annotate(f'median = {median:.2f}', (median + 1, 20))
plt.xlabel('Salary (in thousand Rs.)'); plt.ylabel('Cumulative frequency')
plt.grid(alpha=0.3)
plt.savefig('../figs/Median.png', dpi=200, bbox_inches='tight')
