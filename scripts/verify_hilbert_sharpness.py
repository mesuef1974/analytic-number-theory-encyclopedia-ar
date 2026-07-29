"""Numerical evidence that pi is the sharp constant in Hilbert's inequality.

This is EVIDENCE, NOT A PROOF. Sharpness (result 8 of
docs/CHAPTER_58_PROOF_MAP_2026-07-29.md) is CITED to Schur (1911) and
Hardy-Littlewood-Polya, Inequalities, 2nd ed., Theorem 294 -- chapter 58
does not prove it. This script only shows the operator norm creeping up
towards pi from below, consistent with sharpness.

Method: the kernel K[m,n] = 1/(n-m) (zero on the diagonal) is real and
antisymmetric, so iK is Hermitian and the supremum of
    |sum_{m != n} z_m conj(z_n)/(n-m)|  /  sum_n |z_n|^2
over z in C^N is exactly the largest |eigenvalue| of iK. Dividing by pi
should approach 1 from below as N grows.

Note the diagonal restriction matters: probing sharpness with REAL
sequences fails, because the form vanishes identically there (antisymmetric
kernel against symmetric weights) -- verified in
verify_hilbert_inequality.py, result (6).

Run:  python scripts/verify_hilbert_sharpness.py
"""

import numpy as np


def hermitian_kernel(size):
    """iK where K[m,n] = 1/(n-m), zero on the diagonal."""
    idx = np.arange(size)
    diff = idx[None, :] - idx[:, None]
    kernel = np.where(diff != 0, 1.0 / np.where(diff == 0, 1, diff), 0.0)
    return 1j * kernel


def main():
    print("operator norm of the Hilbert form, normalised by pi")
    print("(approaches 1 from below; never exceeds it)\n")
    ratios = []
    for size in (10, 50, 200, 1000, 4000):
        norm = np.max(np.abs(np.linalg.eigvalsh(hermitian_kernel(size))))
        ratio = norm / np.pi
        ratios.append(ratio)
        print(f"  N = {size:5d}   ||form|| / pi = {ratio:.6f}")

    monotone = all(b > a for a, b in zip(ratios, ratios[1:]))
    below = all(r <= 1.0 for r in ratios)
    print(f"\nincreasing: {monotone}   all <= 1: {below}")
    print(f"VERDICT: {'CONSISTENT WITH SHARPNESS' if monotone and below else 'UNEXPECTED'}"
          "  (evidence only, not a proof)")
    return 0 if monotone and below else 1


if __name__ == "__main__":
    raise SystemExit(main())
