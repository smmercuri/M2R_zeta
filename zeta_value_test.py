from zeta_value import zeta_euler_maclaurin
from sage.all import *

if __name__ == "__main__":
    print(float(pi**2 / 6))
    print(zeta_euler_maclaurin(2, 10, 1))
    print(zeta_euler_maclaurin(2, 10, 10))
    print(zeta_euler_maclaurin(2, 10, 20))
    print(zeta_euler_maclaurin(2, 10, 40))
    print(zeta_euler_maclaurin(2, 10, 80))
    print(zeta_euler_maclaurin(2, 10, 85))
    print(zeta_euler_maclaurin(2, 10, 86))
    print(zeta_euler_maclaurin(2, 10, 88))
    print(zeta_euler_maclaurin(2, 10, 90))
