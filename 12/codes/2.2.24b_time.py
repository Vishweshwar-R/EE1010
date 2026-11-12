# code by Vishweshwar
# Python is used only for plotting: the timings come from 2.2.24b_time.c
import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

n, t = np.loadtxt('codes/2.2.24b_time.dat', unpack=True)

plt.figure(figsize=(5.5, 4))
plt.loglog(n, t, 'bo-', label='measured time')
plt.loglog(n, t[-1] * (n / n[-1]) ** 3, 'r--', label=r'$\propto n^3$')
plt.xlabel('$n$'); plt.ylabel('time (s)')
plt.legend(); plt.grid(alpha=0.3, which='both')

#If using termux
plt.savefig('figs/2.2.24b_time.png', dpi=200, bbox_inches='tight')
subprocess.run(shlex.split("termux-open figs/2.2.24b_time.png"))
#else
#plt.show()
