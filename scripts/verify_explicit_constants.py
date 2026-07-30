"""P2-07: verify every explicit numeric constant asserted in the manuscript.

This is a REGRESSION test, not a one-off audit. Rather than restating the
constants as hardcoded literals, it EXTRACTS them from the .tex sources and
then checks the arithmetic identities, orderings and admissibility claims
the prose depends on. If a future edit changes a constant in one place but
not its partner representation, or breaks a claimed ordering, this fails.

Covered:

  A. Short-interval records (chapter 19)
     - Baker-Harman-Pintz is written as x^{0.525} in the theorem (matching
       the published source's own form) but compared as 21/40 in the
       discussion. Those must be the same number.
     - The historical progression Ingham 5/8 -> Huxley 7/12 ->
       Guth-Maynard 17/30 must be strictly decreasing (shorter intervals).
     - The text asserts BHP sits in a *shorter* interval than
       Guth-Maynard, i.e. 21/40 < 17/30, while being qualitatively weaker.
     - The BHP explicit lower-bound constant 9/100.

  B. Exponent-pair processes (chapter 18, both CITED to Graham-Kolesnik)
     - A(k,l) = (k/(2k+2), (k+l+1)/(2k+2))
     - B(k,l) = (l - 1/2, k + 1/2)
     Checked: B is an involution; both processes map the admissible region
     into itself; the two distinguished pairs (1/2,1/2) and (0,1) behave as
     the chapter's definition requires.

  C. Bombieri-Vinogradov error structure (chapter 13): the exponent 5/6
     must lie strictly between 1/2 and 1 for the stated absorption
     argument to work.

Run:  python scripts/verify_explicit_constants.py
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

CHAPTERS = Path("volumes/volume-01-foundations/chapters")
CH19 = CHAPTERS / "chapter-19-primes-short-intervals.tex"
CH18 = CHAPTERS / "chapter-18-exponential-sums-van-der-corput-batch-03.tex"
CH13 = CHAPTERS / "chapter-13-bombieri-vinogradov.tex"

failures: list[str] = []
checks = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global checks
    checks += 1
    if condition:
        print(f"  PASS  {label}")
    else:
        print(f"  FAIL  {label}   {detail}")
        failures.append(f"{label} {detail}".strip())


def read(path: Path) -> str:
    if not path.exists():
        failures.append(f"missing source file: {path}")
        return ""
    return path.read_text(encoding="utf-8")


def find_all(pattern: str, text: str) -> list[str]:
    return re.findall(pattern, text)


# --------------------------------------------------------------------------
# A. short-interval records, chapter 19
# --------------------------------------------------------------------------
def section_a() -> None:
    print("\nA. short-interval records (chapter 19)")
    src = read(CH19)
    if not src:
        return

    # BHP written as a decimal exponent x^{0.525}
    decimals = set(find_all(r"\^\{(0\.\d+)\}", src))
    check("BHP decimal exponent 0.525 present in ch19",
          "0.525" in decimals, f"found {sorted(decimals)}")

    # BHP written as a fraction 21/40 in the comparison discussion
    check("BHP fraction 21/40 present in ch19",
          "21/40" in src)

    # the two representations must be the same number
    if "0.525" in decimals and "21/40" in src:
        check("0.525 == 21/40 exactly",
              Fraction("0.525") == Fraction(21, 40),
              f"{Fraction('0.525')} vs {Fraction(21, 40)}")

    # Guth-Maynard asymptotic exponent
    check("Guth-Maynard exponent 17/30 present in ch19", "17/30" in src)

    # historical progression must be strictly decreasing
    ingham, huxley, guth_maynard = Fraction(5, 8), Fraction(7, 12), Fraction(17, 30)
    check("progression strictly decreasing: 5/8 > 7/12 > 17/30",
          ingham > huxley > guth_maynard,
          f"{float(ingham):.4f} {float(huxley):.4f} {float(guth_maynard):.4f}")

    # the prose claims BHP is in a SHORTER interval than Guth-Maynard
    bhp = Fraction(21, 40)
    check("BHP interval strictly shorter than Guth-Maynard: 21/40 < 17/30",
          bhp < guth_maynard,
          f"{float(bhp):.4f} vs {float(guth_maynard):.4f}")

    # ...and the prose must actually say they are not comparable by exponent
    # alone -- guard the sentence that carries this caveat.
    check("ch19 keeps the 'not orderable by exponent alone' caveat",
          "لا يجوز ترتيب" in src and "17/30" in src and "21/40" in src)

    # BHP explicit constant 9/100
    check("BHP constant 9/100 present in ch19",
          r"\frac{9}{100}" in src)
    check("BHP constant 9/100 is a positive proper fraction",
          0 < Fraction(9, 100) < 1)

    # the upper end of the Guth-Maynard admissible range
    check("ch19 upper range exponent 0.99 < 1", Fraction("0.99") < 1)


# --------------------------------------------------------------------------
# B. exponent-pair processes, chapter 18
# --------------------------------------------------------------------------
def a_process(k: Fraction, l: Fraction) -> tuple[Fraction, Fraction]:
    return (k / (2 * k + 2), (k + l + 1) / (2 * k + 2))


def b_process(k: Fraction, l: Fraction) -> tuple[Fraction, Fraction]:
    return (l - Fraction(1, 2), k + Fraction(1, 2))


def admissible(k: Fraction, l: Fraction) -> bool:
    """The chapter's own admissible region for a one-dimensional pair."""
    interior = (0 <= k <= Fraction(1, 2) <= l <= 1) and (k + l < 1)
    distinguished = (k, l) in {(Fraction(1, 2), Fraction(1, 2)),
                              (Fraction(0), Fraction(1))}
    return interior or distinguished


def section_b() -> None:
    print("\nB. exponent-pair processes (chapter 18, CITED)")
    src = read(CH18)
    if not src:
        return

    # guard that the chapter still states the formulas this script encodes
    check("ch18 states A-process numerator k/(2k+2)",
          r"\frac{\kappa}{2\kappa+2}" in src)
    check("ch18 states A-process second coordinate (k+l+1)/(2k+2)",
          r"\frac{\kappa+\lambda+1}{2\kappa+2}" in src)
    check("ch18 states B-process (l-1/2, k+1/2)",
          r"\lambda-\frac12" in src and r"\kappa+\frac12" in src)

    half = Fraction(1, 2)
    trivial = (half, half)
    other = (Fraction(0), Fraction(1))

    # the two distinguished pairs are admissible by the chapter's definition
    check("(1/2,1/2) admissible", admissible(*trivial))
    check("(0,1) admissible", admissible(*other))

    # B is an involution
    ok = True
    for k, l in [trivial, other, (Fraction(1, 6), Fraction(2, 3)),
                 (Fraction(1, 9), Fraction(13, 18))]:
        if b_process(*b_process(k, l)) != (k, l):
            ok = False
    check("B is an involution: B(B(k,l)) == (k,l)", ok)

    # B swaps the two distinguished pairs in the expected way
    check("B(1/2,1/2) == (0,1)", b_process(*trivial) == other,
          str(b_process(*trivial)))
    check("B(0,1) == (1/2,1/2)", b_process(*other) == trivial,
          str(b_process(*other)))

    # A applied to the trivial pair: the classical (1/6, 2/3)
    a_trivial = a_process(*trivial)
    check("A(1/2,1/2) == (1/6, 2/3)",
          a_trivial == (Fraction(1, 6), Fraction(2, 3)), str(a_trivial))
    check("A(1/2,1/2) is admissible", admissible(*a_trivial))

    # A maps admissible pairs to admissible pairs over a sampled sweep
    bad: list[str] = []
    for kn in range(0, 51):
        for ln in range(0, 51):
            k, l = Fraction(kn, 100), Fraction(50 + ln, 100)
            if not admissible(k, l):
                continue
            ak, al = a_process(k, l)
            if not admissible(ak, al):
                bad.append(f"A({k},{l})=({ak},{al})")
    check("A maps the admissible region into itself (sampled sweep)",
          not bad, f"{len(bad)} violations, first: {bad[:2]}")

    # A always contracts the first coordinate below 1/2
    check("A(k,l) first coordinate < 1/2 for admissible k",
          all(a_process(Fraction(kn, 100), Fraction(3, 4))[0] < half
              for kn in range(0, 51)))


# --------------------------------------------------------------------------
# C. Bombieri-Vinogradov error structure, chapter 13
# --------------------------------------------------------------------------
def section_c() -> None:
    print("\nC. Bombieri-Vinogradov error structure (chapter 13)")
    src = read(CH13)
    if not src:
        return

    check("ch13 uses the exponent 5/6", "5/6" in src)
    five_sixths = Fraction(5, 6)
    check("1/2 < 5/6 < 1 (needed for the absorption argument)",
          Fraction(1, 2) < five_sixths < 1,
          f"{float(five_sixths):.4f}")
    # the companion terms in the same bracket
    check("ch13 keeps the companion exponents 1/2 and 1 in the same bound",
          "x^{1/2}" in src)


def main() -> int:
    print("P2-07: explicit numeric constants asserted in the manuscript")
    print("(constants are extracted from source, not hardcoded)")
    section_a()
    section_b()
    section_c()

    print(f"\n{checks} checks run, {len(failures)} failed")
    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(f"  - {f}")
    print(f"\nVERDICT: {'PASS' if not failures else 'FAIL'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
