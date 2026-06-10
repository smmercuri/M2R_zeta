from sage.all import *
import numpy as np


def partial_zeta(s, N):
    return sum(QQ(n) ** (-s) for n in range(1, N))


def zeta_integral_term(s, N):
    return QQ(N) ** (1 - s) / (s - 1)


def zeta_correction_term(s, N):
    return QQ(1) / (2 * N**s)


def zeta_bernoulli_term_diff(k, N, s):
    x = var("x")
    deriv = diff(x ** (-s), x, 2 * k - 1)(x=N)
    return -bernoulli(2 * k) / factorial(2 * k) * deriv


def zeta_bernoulli_sum(N, s, v):
    return sum(zeta_bernoulli_term_diff(k, N, s) for k in range(1, v + 1))


def zeta_euler_maclaurin(s, N, v):
    return (
        partial_zeta(s, N)
        + zeta_integral_term(s, N)
        + zeta_correction_term(s, N)
        + zeta_bernoulli_sum(N, s, v)
    )
