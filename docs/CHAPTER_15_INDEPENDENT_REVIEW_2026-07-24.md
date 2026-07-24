# Chapter 15 Independent Scientific Review — 2026-07-24

## Scope

This is a new independent review of the corrected 485-line Chapter 15 manuscript after the mathematical correction commit `b9d9f0c` and the exact citation-location commits ending at `292d33c`. The reviewer independently rederived the central Selberg minimization, checked the cited sources, and compared the manuscript with the post-authoring audit, reference audit, and result registry.

## Findings

### 1. Proof correctness

The finite Selberg minimization, including the transformed variables, Möbius inversion, Cauchy--Schwarz step, optimal weights, and the exact remainder multiplicity, is correct.

A blocking gap remains in the sifted-pairs theorem: the proof invokes the Selberg denominator theorem, whose hypothesis is the regularity condition (15.6), but the pair-dimension proposition currently proves only

\[
V_h(z)\asymp_h (\log z)^{-2}.
\]

The converse implication is not established. The manuscript must explicitly verify

\[
\sum_{w\le p<z} g_h(p)\log p
=
2\log(z/w)+O_h(1),
\]

using Mertens' first theorem and the finite set of primes dividing the shift.

Status: `PASS-WITH-ONE-GAP`.

### 2. Hypotheses

Condition (15.6) matches the standard sieve-dimension regularity condition. The fundamental lemma's threshold `s_0(\kappa,A_1)` is acceptable in the abstract formulation, but the chapter does not use the fundamental lemma in the central pair application. This should be stated explicitly.

Status: `PASS / NONBLOCKING-CLARIFICATION`.

### 3. Constants and effectiveness

The constant in the pair bound is effective in principle. The proof uses elementary local densities, Mertens-type estimates, the finite Selberg upper bound, and explicit remainder estimates; it does not use Siegel--Walfisz, exceptional zeros, or an ineffective Siegel constant. The manuscript should record this.

Status: `INCOMPLETE / NONBLOCKING-DOCUMENTATION`.

### 4. Application scope

The chapter correctly avoids claiming twin primes, bounded gaps, or a lower bound for prime pairs. The range `z\le x^{1/4}` is correctly identified as a conservative pedagogical range, and the small-`x` range is handled explicitly.

Status: `PASS`.

### 5. Classification accuracy

The reference audit is now closed as `PASS`, but the chapter text and `docs/RESULTS_REGISTRY_CHAPTER_15.md` still contain stale `OPEN` or `FAIL` states. These files must be synchronized with the final reference-audit document.

Status: `FAIL / BLOCKING-GOVERNANCE-INCONSISTENCY`.

## Decision

```text
PROOF-CORRECTNESS       = PASS-WITH-ONE-GAP
HYPOTHESES              = PASS
CONSTANTS               = INCOMPLETE / NONBLOCKING
APPLICATION-SCOPE       = PASS
CLASSIFICATION-ACCURACY = FAIL
OVERALL                  = CHANGES-REQUIRED
BLOCKING-ITEMS           = 2
  1. Verify condition (15.6) for the pair density g_h before invoking ANT-THM-15-02.
  2. Synchronize REFERENCE-AUDIT status across the chapter and registry.
NONBLOCKING              = Record effectiveness; clarify the fundamental lemma is not used in ANT-THM-15-04; reduce notation ambiguity where practical.
CHAPTER-15               = NOT-YET-REVIEWED
PR-28                    = DRAFT / OPEN / UNMERGED
```

No merge is authorized by this review.
