import numpy as np
import matplotlib.pyplot as plt

# Q16: sin^-1(4/5) + tan^-1(5/12) + cos^-1(63/65) = pi/2
s = np.arcsin(4/5) + np.arctan(5/12) + np.arccos(63/65)
print(s, np.pi / 2, np.isclose(s, np.pi / 2))
print("sin^-1(4/5) = tan^-1(4/3):", np.isclose(np.arcsin(4/5), np.arctan(4/3)))
print("cos^-1(63/65) = tan^-1(16/63):", np.isclose(np.arccos(63/65), np.arctan(16/63)))
print("tan^-1(4/3)+tan^-1(5/12) = tan^-1(63/16):", np.isclose(np.arctan(4/3) + np.arctan(5/12), np.arctan(63/16)))
