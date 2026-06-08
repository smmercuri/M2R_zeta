from sage.all import *
import numpy as np


def gamma_integral_term(s):
    return (s - 1 / 2) * log(s - 1)

def gamma_correction_term(s):
    return -s + 1

def gamma_shifting_factor():
    return (1 / 2) * log(2*pi)

def gamma_bernoulli_term(k, s):
    return bernoulli(2 * k) / (2 * k * (2 * k - 1) * (s - 1) ** (2 * k -1))


def gamma_bernoulli_sum(s, v):
    return sum(gamma_bernoulli_term(k, s) for k in range(1, v + 1))


def log_gamma_euler_maclaurin(s, v):
    return (
        gamma_integral_term(s)
        + gamma_correction_term(s)
        + gamma_shifting_factor()
        + gamma_bernoulli_sum(s, v)
    )

def gamma_euler_maclaurin(s, v):
    return exp(log_gamma_euler_maclaurin(s, v))
