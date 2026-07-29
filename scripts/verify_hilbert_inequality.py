"""Numerical verification of the Hilbert-inequality chain used in chapter 58.

Verifies, in order, the PROVED-HERE results of
docs/CHAPTER_58_PROOF_MAP_2026-07-29.md:

  (1) sawtooth Fourier series  sum_{k>=1} sin(2 pi k x)/k = pi(1/2 - x),  0<x<1
  (2) g(x) := sum_{k != 0} e(kx)/k = i pi (1 - 2x),  hence |g| <= pi
  (3) the integral representation (the pivotal step)
          sum_{m != n} z_m conj(z_n)/(n-m) = int_0^1 |f(x)|^2 g(x) dx,
      where f(x) = sum_n z_n e(nx)
  (4) Hilbert's inequality with Schur's sharp constant pi
  (5) the form vanishes identically for real coefficients

Sharpness of the constant pi is NOT checked here -- it needs the operator
norm, see verify_hilbert_sharpness.py. (An earlier version of this script
tried to probe sharpness with real sequences z_n = n^{-1/2}; by (5) those
make the form vanish, so it was measuring zero. Kept out deliberately.)

Run:  python scripts/verify_hilbert_inequality.py
"""

import numpy as np

rng = np.random.default_rng(20260730)
K_TERMS = 200_000
QUAD_NODES = 400_000


def sawtooth_partial(x, terms=K_TERMS):
    k = np.arange(1, terms + 1)
    return np.sum(np.sin(2 * np.pi * np.outer(x, k)) / k, axis=1)


def hilbert_form(z):
    """sum_{m != n} z_m conj(z_n) / (n - m)."""
    idx = np.arange(len(z))
    diff = idx[None, :] - idx[:, None]
    kernel = np.where(diff != 0, 1.0 / np.where(diff == 0, 1, diff), 0.0)
    return np.sum(np.outer(z, np.conj(z)) * kernel)


def integral_side(z, nodes=QUAD_NODES):
    """int_0^1 |f(x)|^2 g(x) dx  with f(x) = sum_n z_n e(nx), g(x) = i pi (1-2x)."""
    x = (np.arange(nodes) + 0.5) / nodes
    f = np.exp(2j * np.pi * np.outer(x, np.arange(len(z)))) @ z
    return np.sum(np.abs(f) ** 2 * (1j * np.pi * (1 - 2 * x))) / nodes


def main():
    xs = np.array([0.05, 0.17, 0.3, 0.5, 0.62, 0.83, 0.95])

    err1 = np.max(np.abs(sawtooth_partial(xs) - np.pi * (0.5 - xs)))
    print(f"(1) sawtooth series      max abs err = {err1:.2e}")

    g_exact = 1j * np.pi * (1 - 2 * xs)
    err2 = np.max(np.abs(2j * sawtooth_partial(xs) - g_exact))
    print(f"(2) g(x) = i.pi.(1-2x)   max abs err = {err2:.2e}"
          f"   |g| <= pi: {bool(np.all(np.abs(g_exact) <= np.pi + 1e-12))}")

    print("(3) integral representation (pivotal step):")
    worst_identity = 0.0
    for n_terms in (2, 4, 5, 9, 12):
        z = rng.normal(size=n_terms) + 1j * rng.normal(size=n_terms)
        err = abs(hilbert_form(z) - integral_side(z))
        worst_identity = max(worst_identity, err)
        print(f"      N={n_terms:3d}  |form - integral| = {err:.2e}")

    print("(4) Hilbert inequality, 400 random complex trials, N in [2,40]:")
    worst_ratio = 0.0
    for _ in range(400):
        n = int(rng.integers(2, 40))
        z = rng.normal(size=n) + 1j * rng.normal(size=n)
        worst_ratio = max(
            worst_ratio, abs(hilbert_form(z)) / (np.pi * np.sum(np.abs(z) ** 2))
        )
    print(f"      max |form| / (pi.sum|z|^2) = {worst_ratio:.6f}  (must be <= 1)")

    print("(5) vanishing for real coefficients (antisymmetric kernel):")
    worst_real = 0.0
    for _ in range(5):
        z = rng.normal(size=int(rng.integers(3, 30)))
        val = abs(hilbert_form(z))
        worst_real = max(worst_real, val)
        print(f"      real z -> |form| = {val:.3e}")

    ok = (err1 < 1e-4 and err2 < 1e-4 and worst_identity < 1e-8
          and worst_ratio <= 1.0 and worst_real < 1e-10)
    print(f"\nVERDICT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
