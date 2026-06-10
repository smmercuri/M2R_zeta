from sage.all import *
import matplotlib.pyplot as plt
from zeta_value import zeta_euler_maclaurin

HP = RealField(1000)

true_value_rat = QQ(1) / 6
true_value = HP(pi) ** 2 * HP(true_value_rat)
s = 2

for N in [4, 6, 9, 13, 19, 26]:
    v_range = range(1, 8 * N)
    errors = [
        float(abs(HP(QQ(zeta_euler_maclaurin(s, N, v))) - true_value)) for v in v_range
    ]
    plt.plot(v_range, errors, marker=".", markersize=5, label=f"N={N}")

plt.yscale("log")
plt.xlabel("v")
plt.ylabel("absolute error |EM approx - pi^2/6|")
plt.title("Euler-Maclaurin approximation of zeta(2)")
plt.legend()
plt.grid(True)
plt.savefig("euler_maclaurin_divergence.png", dpi=150)
plt.show()

with open("euler_maclaurin_tables.txt", "w") as f:
    for N in [4, 6, 9, 13, 19, 26]:
        v_range = range(1, 8 * N)
        f.write(f"N = {N}\n")
        f.write(f"{'v':>6}  {'absolute error':>20}\n")
        f.write("-" * 30 + "\n")
        for v in v_range:
            err = float(abs(HP(QQ(zeta_euler_maclaurin(s, N, v))) - true_value))
            f.write(f"{v:>6}  {err:>20.6e}\n")
        f.write("\n")
