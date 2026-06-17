import os
from zeta_zero import find_zeros

ZEROS_FILE = os.path.join(os.path.dirname(__file__), "zetazeros")

T = 200
M = 4
N = 40
v = 120
C = 15
D = 10


def load_known_zeros(path, T):
    """Return sorted list of known zero imaginary parts up to T."""
    zeros = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            _, imag = line.split()
            t = float(imag)
            if t <= T:
                zeros.append(t)
    return sorted(zeros)


def zero_in_interval(zero, intervals):
    return any(t1 <= zero <= t2 for t1, t2 in intervals)


def run_test(T, d):
    known = load_known_zeros(ZEROS_FILE, T)
    intervals = find_zeros(T, M, N, v, C, d)
    count_ok = len(intervals) == len(known)
    all_found = all(zero_in_interval(z, intervals) for z in known)
    return known, intervals, count_ok, all_found


def test_all_zeros_found(T=T, d=D):
    known, intervals, count_ok, all_found = run_test(T, d)

    print(f"find_zeros returned {len(intervals)} interval(s) (expected {len(known)} up to T={T})")
    for idx, (t1, t2) in enumerate(intervals, 1):
        print(f"  Interval {idx:2d}: ({t1:.6f}, {t2:.6f})")

    print()
    print("Per-zero check:")
    for idx, z in enumerate(known, 1):
        found = zero_in_interval(z, intervals)
        status = "PASS" if found else "FAIL"
        print(f"  Zero {idx:2d} (t = {z:.6f}): {status}")

    print()
    if count_ok and all_found:
        print(f"OVERALL: PASS — all {len(known)} zeros found and each lies in an interval.")
    else:
        if not count_ok:
            print(f"OVERALL: FAIL — expected {len(known)} intervals, got {len(intervals)}.")
        if not all_found:
            print("OVERALL: FAIL — one or more known zeros not contained in any interval.")


def test_increasing_d(T=T):
    """Run with increasing bisection depth until the test fails."""
    print("=" * 60)
    print(f"Increasing bisection depth d until test fails (T={T})")
    print("=" * 60)
    for d in range(1, 60):
        known, intervals, count_ok, all_found = run_test(T, d)
        status = "PASS" if (count_ok and all_found) else "FAIL"
        print(f"  d = {d:2d}: {len(intervals)} interval(s), all zeros found = {all_found}  [{status}]")
        if not (count_ok and all_found):
            print(f"  Test first failed at d = {d}.")
            break
    else:
        print("  Test passed for all d values tested (d = 1 to 59).")


if __name__ == "__main__":
    print("=" * 60)
    print(f"Testing find_zeros(T={T}, M={M}, N={N}, v={v}, C={C}, d={D})")
    print("=" * 60)
    test_all_zeros_found()
    print()
    test_increasing_d()
