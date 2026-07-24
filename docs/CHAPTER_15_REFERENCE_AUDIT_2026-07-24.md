# Chapter 15 Reference Audit — 2026-07-24

## Scope

This audit covers the three externally sourced claims in Chapter 15:

1. the Selberg denominator asymptotic;
2. the fundamental lemma of sieve theory;
3. the parity barrier.

It also records the source status of the finite Selberg minimization proof, although that proof is now written out in the chapter and classified as proved in the manuscript.

## Source inventory added

- Alina Carmen Cojocaru and M. Ram Murty, *An Introduction to Sieve Methods and Their Applications* (Cambridge University Press, 2005).
- Harold G. Diamond, H. Halberstam, and William F. Galway, *A Higher-Dimensional Sieve Method* (Cambridge University Press, 2008).
- Heini Halberstam and Hans-Egon Richert, *Sieve Methods* (Academic Press, 1974).
- John Friedlander and Henryk Iwaniec, *Opera de Cribro* (AMS, 2010).
- John Friedlander and Henryk Iwaniec, “Asymptotic Sieve for Primes” (Annals of Mathematics 148 (1998), 1041–1065; arXiv:math/9811186).
- D. R. Heath-Brown, *Lectures on Sieves* (2002 lecture notes, arXiv:math/0209360).

The entries are stored in `manuscript/chapter-15-bibliography.bib` and loaded from `manuscript/preamble.tex`.

## Build verification

A clean local build after restoring the full governance macro layer completed successfully:

- Biber read `manuscript/chapter-15-bibliography.bib`.
- The final PDF contains 219 pages.
- `build/main.pdf` and `releases/preview.pdf` have equal size and timestamp.
- SHA256 of the final PDF: `95F828F35D7A862DCB094910CB5BEB06850F097A6295C9CEAFBE5DC69309FE5D`.
- Chapter 15 cross-references and citations resolve in the final XeLaTeX pass.
- A final search of `build/main.log` returned no undefined citations, references, or global undefined-reference warning.
- The branch and remote were synchronized at commit `7bbe5c4`, with a clean working tree.
- Historical font, bidi, and overfull-box warnings remain outside the scope of this chapter audit.

Status: `POST-AUTHORING-BUILD-AUDIT = PASS`.

## Text-location verification

### Selberg sieve framework and minimization

- Diamond–Halberstam–Galway, Chapter 2, pp. 13–18: Selberg's sieve method.
- Diamond–Halberstam–Galway, Chapter 5, pp. 43–66: continuation of Selberg's sieve method.
- Cojocaru–Murty, Chapter 7: Selberg's sieve.

Status: `CHAPTER-RANGE-VERIFIED`.

The chapter's finite minimization proof is self-contained after the post-authoring correction. The external sources are supporting references, not substitutes for a missing derivation.

### Fundamental lemma

- Diamond–Halberstam–Galway, Chapter 4, pp. 29–42: “The Fundamental Lemma”.

Status: `TEXT-LOCATION-VERIFIED` at chapter and page-range level.

The manuscript deliberately uses an abstract one-sided formulation and does not claim a specific numerical decay rate for the structural error term.

The manuscript citation is:

```tex
\cite[Chapter~4, pp.~29--42]{DiamondHalberstamGalway2008}
```

### Selberg denominator asymptotic

The manuscript states

\[
G(z,z)=\frac{e^{\gamma\kappa}}{\Gamma(\kappa+1)}V(z)^{-1}\left(1+O_{\kappa,A_1}(1/\log z)\right).
\]

The exact constant and normalization are reproduced in D. R. Heath-Brown, *Lectures on Sieves*, p. 21. The notes explicitly identify the underlying source as Halberstam–Richert, equation (5.3.1). The same passage uses the dimension condition

\[
\sum_{w\le p<z}\frac{\omega(p)\log p}{p}
=
\kappa\log(z/w)+O(1),
\]

which matches the chapter's regularity hypothesis after the identification `g(p)=\omega(p)/p`.

Status: `TEXT-LOCATION-VERIFIED / NORMALIZATION-MATCHED`.

The manuscript citation is:

```tex
\cite[p.~21]{HeathBrown2002LecturesSieves};
\cite[(5.3.1)]{HalberstamRichert1974}
```

### Parity barrier

Friedlander–Iwaniec, *Asymptotic Sieve for Primes*, gives the exact textual match:

- p. 1042: the limitation of the original sieve framework is identified explicitly as the “parity problem” of sieve theory.
- pp. 1044–1045: the authors state that the classical remainder hypothesis alone cannot capture primes, even at level `D(x)=x^{1-\varepsilon}`, and explain that an additional bilinear hypothesis is what resolves the parity problem and permits prime detection.

This matches the chapter's deliberately diagnostic wording: classical local-divisibility and remainder data alone are insufficient to distinguish the prime-parity structure needed for a lower-bound prime-detection result; additional analytic input can breach the barrier.

Status: `TEXT-LOCATION-VERIFIED / CLAIM-MATCHED`.

The manuscript citation should use:

```tex
\cite[pp.~1042, 1044--1045]{FriedlanderIwaniec1998AsymptoticSieve}
```

## Current decision

```text
POST-AUTHORING-BUILD-AUDIT = PASS
REFERENCE-BIBLIOGRAPHY      = PASS
REFERENCE-TEXT-MATCHING     = PASS
SELBERG-DENOMINATOR         = TEXT-LOCATION-VERIFIED / NORMALIZATION-MATCHED
FUNDAMENTAL-LEMMA           = CHAPTER/PAGE-RANGE-VERIFIED
PARITY-BARRIER              = TEXT-LOCATION-VERIFIED / CLAIM-MATCHED
REFERENCE-AUDIT             = PASS
CHAPTER-15                  = AUTHORED-DRAFT
INDEPENDENT-REVIEW          = PENDING
REVIEWED                    = NO
PR-28                       = DRAFT / OPEN / UNMERGED
```

The reference audit is closed. No merge is authorized by this audit.