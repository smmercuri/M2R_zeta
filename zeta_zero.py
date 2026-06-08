from sage.all import *
from gamma_value import log_gamma_euler_maclaurin
from zeta_value import zeta_euler_maclaurin
import numpy as np


def partial_log_gamma(s, N):
    return -sum(log(s - 1 + i) for i in range(1, N + 1))


def theta(t, N, v):
    s = (1 + 2 * i * t) / 4
    log_gamma_approx = log_gamma_euler_maclaurin(s + N, v) + partial_log_gamma(s, N)
    return imag_part(log_gamma_approx) - t / 2 * log(pi)


def Z(t, N, v):
    return exp(i * theta(t, N, v)) * zeta_euler_maclaurin(QQ(1, 2) + i * t, N, v)


def zero_gap(t, M):
    return 2 * pi / (M * log(t / (2 * pi)))


def zero_partition(T, M):
    step = float(zero_gap(T, M))
    n = int(np.ceil(T / step))
    return np.linspace(0, T, n, endpoint=False)


def find_zeros(T, M, N, v):
    zeros = []
    partition = zero_partition(T, M)
    Z_values = [Z(t, N, v) for t in partition]
    for i in range(len(partition) - 1):
        if real_part(Z_values[i]) * real_part(Z_values[i + 1]) < 0:
            zeros.append((partition[i], partition[i + 1]))
    return zeros
