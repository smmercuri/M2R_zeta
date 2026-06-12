from gamma_value import gamma_euler_maclaurin, log_gamma_euler_maclaurin
from sage.all import *

if __name__ == "__main__":
    HP = RealField(10000)

    # Gamma(3) = 2! = 2
    print("--- gamma_euler_maclaurin(s=3, N=10) vs Gamma(3) = 2 ---")
    print(HP(2).n(digits=30))
    print(HP(gamma_euler_maclaurin(3, 10, 1)).n(digits=30))
    print(HP(gamma_euler_maclaurin(3, 10, 10)).n(digits=30))
    print(HP(gamma_euler_maclaurin(3, 10, 20)).n(digits=30))
    print(HP(gamma_euler_maclaurin(3, 10, 40)).n(digits=30))

    # Gamma(5) = 4! = 24
    print("\n--- gamma_euler_maclaurin(s=5, N=10) vs Gamma(5) = 24 ---")
    print(HP(24).n(digits=30))
    print(HP(gamma_euler_maclaurin(5, 10, 1)).n(digits=30))
    print(HP(gamma_euler_maclaurin(5, 10, 10)).n(digits=30))
    print(HP(gamma_euler_maclaurin(5, 10, 20)).n(digits=30))
    print(HP(gamma_euler_maclaurin(5, 10, 40)).n(digits=30))

    # log Gamma(1/2) = (1/2)*log(pi)
    print("\n--- log_gamma_euler_maclaurin(s=1/2, N=20) vs log(Gamma(1/2)) = (1/2)*log(pi) ---")
    print(HP(log(pi) / 2).n(digits=30))
    print(HP(log_gamma_euler_maclaurin(QQ(1)/2, 20, 1)).n(digits=30))
    print(HP(log_gamma_euler_maclaurin(QQ(1)/2, 20, 10)).n(digits=30))
    print(HP(log_gamma_euler_maclaurin(QQ(1)/2, 20, 20)).n(digits=30))
    print(HP(log_gamma_euler_maclaurin(QQ(1)/2, 20, 40)).n(digits=30))
