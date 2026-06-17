from sage.all import *
from zeta_zero import zeros, find_zeros


def prime_power(x, zeros):
    return li(x) - 2 * sum(real_part(Ei(t * log(x))) for t in zeros) - log(2)


def prime(x, zeros):

    n_max = int(log(x) / log(2))
    return sum(
        moebius(n) / n * prime_power(x ** (QQ(1) / n), zeros)
        for n in range(1, n_max + 1)
    )

