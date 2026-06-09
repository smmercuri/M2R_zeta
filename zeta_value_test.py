from zeta_value import zeta_euler_maclaurin
from sage.all import *

if __name__ == "__main__":
    HP = RealField(10000)

    print(HP(pi**2 / 6).n(digits=30))
    print(HP(zeta_euler_maclaurin(2, 10, 1)).n(digits=30))
    print(HP(zeta_euler_maclaurin(2, 10, 10)).n(digits=30))
    print(HP(zeta_euler_maclaurin(2, 10, 20)).n(digits=30))
    print(HP(zeta_euler_maclaurin(2, 10, 40)).n(digits=30))
    print(HP(zeta_euler_maclaurin(2, 10, 80)).n(digits=30))
    print(HP(zeta_euler_maclaurin(2, 10, 85)).n(digits=30))
    print(HP(zeta_euler_maclaurin(2, 10, 86)).n(digits=30))
    print(HP(zeta_euler_maclaurin(2, 10, 88)).n(digits=30))
    print(HP(zeta_euler_maclaurin(2, 10, 90)).n(digits=30))
