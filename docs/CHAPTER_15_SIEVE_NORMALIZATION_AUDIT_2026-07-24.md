# Chapter 15 — Sieve Normalization Audit

Date: 2026-07-24

```text
CHAPTER              = 15
VERSION              = 0.19.0-dev
AUDIT                = SIEVE-NORMALIZATION
STATUS               = PASS-FOR-NOTATION
AUTHORING             = BLOCKED
PASS-FOR-AUTHORING   = NO
```

## Adopted notation

Let `A` be a finite sequence (with multiplicity allowed), let `P` be a set of primes, and define

```text
P(z) = product_{p<z, p in P} p,
S(A,P,z) = sum_{a in A, gcd(a,P(z))=1} 1.
```

For squarefree `d | P(z)`, write

```text
A_d = {a in A : d | a},
|A_d| = X g(d) + r_d,
```

where `g` is multiplicative and `0 <= g(p) < 1` for the sieving primes.

The local Euler product is

```text
V(z) = product_{p<z, p in P} (1-g(p)).
```

For Selberg's quadratic minimization define

```text
h(p) = g(p)/(1-g(p))
```

and extend `h` multiplicatively to squarefree integers. The symbol `G` is reserved for the minimization sum built from `h`; it is not used for the local Euler product.

A working one-parameter notation is

```text
G(z) = sum_{d<z, d|P(z)} mu(d)^2 h(d),
```

with the explicit warning that some references use a two-parameter sum `G(D,z)` or truncate at a Selberg level different from the sifting limit. The final theorem statement must state the truncation explicitly.

## Distribution level and sieve parameter

The remainder level is denoted by `D`. The dimensionless sieve parameter is

```text
s = log D / log z.
```

`D` is not the same object as the sifting threshold `z`, and the sieve dimension is not determined by `D` alone.

## Sieve dimension

The chapter will use a product-form dimension hypothesis rather than an informal prime-sum slogan. The working form is that, for `2 <= w < z`,

```text
product_{w<=p<z} (1-g(p))^{-1}
  <= C (log z / log w)^kappa
```

with a fixed dimension `kappa >= 0` and a controlled constant `C`. Equivalent prime-sum formulations may be quoted only after their hypotheses and error terms are stated.

## Separation of tools

1. Selberg upper-bound sieve: quadratic positivity plus minimization.
2. Fundamental lemma: comparison of the sifted count with `X V(z)` under a quantitative remainder level and dimension hypothesis.
3. Linear/beta sieve: separate upper and lower functions depending on `s`.
4. Parity barrier: a limitation of classical divisor-data sieves, not a universal impossibility theorem for every argument containing sieve weights.

## Source hierarchy

- Primary structural reference: Friedlander--Iwaniec, *Opera de Cribro*, especially the chapters on sieve terminology, Selberg's sieve, beta-sieve, linear sieve, and the parity principle.
- Fundamental-lemma cross-check: Diamond--Halberstam--Galway, *A Higher-Dimensional Sieve Method*, Part I.
- Pedagogical cross-check: Greaves, *Sieves in Number Theory*.
- Weighted sieve reference: Richert, “Selberg's sieve with weights”, *Mathematika* 16 (1969), 1--22.
- Modern parity cross-check: D. H. J. Polymath, “Variants of the Selberg sieve, and bounded intervals containing many primes”, including its published erratum.

## Governance decision

```text
NOTATION-NORMALIZATION = CLOSED
FUNDAMENTAL-LEMMA      = OPEN
PARITY-AUDIT           = OPEN
APPLICATION-CHOICE     = OPEN
PASS-FOR-AUTHORING     = NO
```

No theorem identifiers are reserved by this audit.