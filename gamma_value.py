from sage.all import *
import numpy as np


def partial_log_gamma(s, N):
    return -sum(log(s - 1 + i) for i in range(1, N))

def gamma_integral_term(s, N):
    return (s + N - QQ(3)/2) * log(s + N - 2)

def gamma_correction_term(s, N):
    return -(s + N - 2)

def gamma_shifting_factor():
    return (1 / 2) * log(2*pi)


def gamma_bernoulli_term(k, N, s):
    return bernoulli(2 * k) / (2 * k * (2 * k - 1) * (s + N - 2) ** (2 * k - 1))


def gamma_bernoulli_sum(N, s, v):
    return sum(gamma_bernoulli_term(k, N, s) for k in range(1, v + 1))


def log_gamma_euler_maclaurin(s, N, v):
    return (
        partial_log_gamma(s, N)
        + gamma_integral_term(s, N)
        + gamma_correction_term(s, N)
        + gamma_shifting_factor()
        + gamma_bernoulli_sum(N, s, v)
    )

def gamma_euler_maclaurin(s, N, v):
    return exp(log_gamma_euler_maclaurin(s, N, v))
