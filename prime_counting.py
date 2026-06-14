from sage.all import *
import matplotlib.pyplot as plt
from zeta_zero import zeros
from primes import prime
import numpy as np
import re


def load_zeros_from_file(filepath):
    intervals = []
    with open(filepath) as f:
        lines = f.readlines()
    for line in lines[1:]:
        m = re.search(r'np\.float64\(([^)]+)\),\s*np\.float64\(([^)]+)\)', line)
        if m:
            intervals.append((float(m.group(1)), float(m.group(2))))
    return intervals


output = zeros(load_zeros_from_file("out/zeta_zero200.txt"))

x_vals = list(np.linspace(30, 50, 100))
y_vals = [prime(RR(n), output) for n in x_vals]

plt.plot(x_vals, y_vals, label="π(x)")
plt.xlabel("x")
plt.ylabel("Number of primes up to x")
plt.title("Prime counting function")
plt.legend()
plt.grid(True)
plt.savefig("out/Prime_counting_function.png", dpi=150)
plt.show()
