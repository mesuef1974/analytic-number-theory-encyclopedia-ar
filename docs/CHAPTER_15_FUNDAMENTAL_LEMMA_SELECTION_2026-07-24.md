# Chapter 15 — Fundamental Lemma Selection

Date: 2026-07-24

```text
CHAPTER              = 15
VERSION              = 0.19.0-dev
UNIT                 = FUNDAMENTAL-LEMMA-SELECTION
STATUS               = SELECTED-FOR-CHAPTER-ARCHITECTURE
AUTHORING             = BLOCKED
PASS-FOR-AUTHORING   = NO
```

## Decision

The chapter will not attempt a full general proof of the higher-dimensional fundamental lemma. It will use the following layered presentation:

1. Prove internally the elementary Selberg quadratic majorant.
2. Prove or derive internally the finite-dimensional minimization identity in the adopted normalization when feasible.
3. State one general fundamental lemma as a `CITED / COMPOSITE-INPUT` theorem under an explicit dimension hypothesis and a quantitative remainder hypothesis.
4. Present the dimension-one linear sieve separately, with its upper and lower sieve functions, as a specialized cited tool.
5. Treat the beta-sieve as the structural bridge between the general lemma and the linear sieve, not as a synonym for either.

## Adopted variables

```text
P(z)  = product of sieving primes below z
V(z)  = product_{p<z}(1-g(p))
D     = remainder/distribution level
s     = log D / log z
kappa = sieve dimension
```

The chapter will never use `D` for the sifting threshold, and it will never use `kappa` for a distribution exponent.

## General fundamental lemma — chapter role

The selected theorem will have the schematic form

```text
S(A,P,z) = X V(z) times a controlled sieve factor
           + an explicit remainder contribution,
```

under:

- multiplicative local density `g` with `0 <= g(p) < 1`;
- a product-form sieve-dimension condition of dimension `kappa`;
- quantitative control of `r_d` for squarefree `d` up to level `D`;
- an explicit range for `s = log D / log z`.

The exact sieve functions and error term will be copied only after page-level verification in the selected source. Until then no numerical constants, threshold values, or asymptotic error rates are authorized.

## Why this version was selected

- *Opera de Cribro* separates Selberg's sieve, beta-sieve, linear sieve, and the parity principle into distinct chapters, supporting the chapter's layered architecture.
- Diamond--Halberstam--Galway place the fundamental lemma before the special case `kappa=1`, then develop higher-dimensional sieve functions separately. This confirms that the linear sieve is a specialization rather than the definition of the fundamental lemma.
- The chapter needs a usable theorem for applications but does not need to reproduce the full analytic theory of the higher-dimensional sieve functions.

## Linear sieve policy

For `kappa=1`, upper and lower functions `F(s)` and `f(s)` may be introduced as `CITED` tools after the following are verified:

1. normalization of `s`;
2. threshold ranges;
3. differential-difference equations or equivalent defining relations;
4. normalization of the main factor `X V(z)`;
5. remainder norm and level assumptions.

No formula for `F` or `f` is yet authorized in the manuscript.

## Lower-bound policy

A lower bound will not be presented as a sign reversal of the Selberg upper-bound sieve. Any lower-bound theorem must enter through the linear/beta-sieve machinery with its own hypotheses.

## Open verification items

- [ ] Page-level source for the chosen general fundamental lemma.
- [ ] Exact remainder norm and support condition.
- [ ] Exact admissible range in `s`.
- [ ] Page-level source for the dimension-one `F(s),f(s)` normalization.
- [ ] Check whether the chosen application requires only an upper bound, allowing the lower-bound section to remain conceptual.

## Governance

```text
NORMALIZATION-AUDIT      = PASS
FUNDAMENTAL-LEMMA-ROUTE  = SELECTED
EXACT-THEOREM-STATEMENT  = OPEN
LINEAR-SIEVE-FORMULAS    = OPEN
PARITY-AUDIT             = OPEN
APPLICATION-CHOICE       = OPEN
PASS-FOR-AUTHORING       = NO
```
