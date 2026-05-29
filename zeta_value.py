from sage.all import *
import numpy as np

def bernoulli_number(n):
    return bernoulli(n)

def partial_zeta(s, N):
    return sum(n ** (-s) for n in range(1, N))

def integral_term(s, N):
    return N ** (1 - s) / (s - 1)

def correction_term(s, N):
    return QQ(1) / (2 * N ** s)

def bernoulli_term(k, N, s):
    m = 2 * k - 1
    B2k = bernoulli_number(2 * k)
    factorial_2k = factorial(2 * k)
    poch = rising_factorial(s, m)
    deriv_at_N = -poch * N ** (-(s + m))
    return (B2k / factorial_2k) * deriv_at_N

def bernoulli_sum(N, s, v):
    return sum(bernoulli_term(k, N, s) for k in range(1, v))

def zeta_euler_maclaurin(s, N, v):
    return (
        partial_zeta(s, N)
        + integral_term(s, N)
        + correction_term(s, N)
        + bernoulli_sum(N, s, v)
    )
