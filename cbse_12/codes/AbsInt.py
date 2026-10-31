import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Q14: int_1^5 (|x-1| + |x-2| + |x-4|) dx
from scipy.integrate import quad
f = lambda x: abs(x - 1) + abs(x - 2) + abs(x - 4)
val, _ = quad(f, 1, 5, points=[2, 4])
print("integral =", round(val, 6))
x = np.linspace(1, 5, 400)
plt.figure(figsize=(5.5, 3.5))
plt.plot(x, [f(t) for t in x], "b")
plt.fill_between(x, [f(t) for t in x], alpha=0.2)
plt.xlabel("x"); plt.ylabel("f(x)"); plt.grid(alpha=0.3)
plt.title(f"Area under $|x-1|+|x-2|+|x-4|$ = {val:.0f}")
plt.tight_layout()
#If using termux
plt.savefig('figs/AbsInt.png', dpi=150)
subprocess.run(shlex.split("termux-open figs/AbsInt.png"))
#else
#plt.show()
