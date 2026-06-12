from sage.all import *
from gamma_value import log_gamma_euler_maclaurin
from zeta_value import zeta_euler_maclaurin
import numpy as np


def theta(t, N, v):
    s = (1 + 2 * i * t) / 4
    log_gamma_approx = log_gamma_euler_maclaurin(s, N, v)
    return imag_part(log_gamma_approx) - t / 2 * log(pi)


def Z(t, N, v):
    return exp(i * theta(t, N, v)) * zeta_euler_maclaurin((1 / 2) + i * t, N, v)


def zero_gap(t, M, C):
    return 2 * pi / (M * log(max(t, C) / (2 * pi)))


def zero_partition(T, M, C):
    step = float(zero_gap(T, M, C))
    n = int(np.ceil(T / step))
    return np.linspace(0, T, n)


def find_zeros(T, M, N, v, C, d):
    zeros = []
    partition = zero_partition(T, M, C)
    Z_values = [Z(t, N, v) for t in partition]
    for i in range(len(partition) - 1):
        if real_part(Z_values[i]) * real_part(Z_values[i + 1]) < 0:
            """Bisection search"""
            t1 = partition[i]
            t2 = partition[i + 1]
            z1 = Z(t1, N, v)
            z2 = Z(t2, N, v)
            for _ in range(d):
                m = (t1 + t2) / 2
                Zm = real_part(Z(m, N, v))
                if real_part(z1) * Zm <= 0:
                    t2 = m
                    z2 = Zm
                else:
                    t1 = m
                    z1 = Zm
            zeros.append((t1, t2))
    return zeros

if __name__ == "__main__":
    K = 3
    T = 50
    M = 4
    N = K * T / 2 * pi
    v = floor(pi * N)
    output = find_zeros(50, 4, 20, 60, 15, 10)
    print(len(output))
    for t in output:
        print(f"1/2 + i{t}")
