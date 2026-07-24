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
- John Friedlander and Henryk Iwaniec, “Asymptotic Sieve for Primes” (1998 preprint).
- D. R. Heath-Brown, *Lectures on Sieves* (2002 lecture notes, arXiv:math/0209360).

The entries are stored in `manuscript/chapter-15-bibliography.bib` and loaded from `manuscript/preamble.tex`.

## Build verification

A clean local build after restoring the full governance macro layer completed successfully:

- Biber read `manuscript/chapter-15-bibliography.bib`.
- The final PDF contains 218 pages.
- Chapter 15 cross-references and citations resolve in the final XeLaTeX pass.
- A final search of `build/main.log` returned no undefined citations, references, or global undefined-reference warning.
- The branch and remote were synchronized at commit `6fbfabf`, with a clean working tree before the denominator-location update.
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

The manuscript deliberately uses an abstract one-sided formulation and does not claim a specific numerical decay rate for the structural error term. Matching a precise theorem number and normalization remains open.

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

The manuscript citation should be updated to:

```tex
\cite[p.~21]{HeathBrown2002LecturesSieves};
\cite[(5.3.1)]{HalberstamRichert1974}
```

This item no longer blocks the reference audit.

### Parity barrier

Iwaniec–Kowalski Chapter 6 is a standard chapter-level reference for elementary sieve limitations. Friedlander–Iwaniec's asymptotic sieve paper explicitly describes the classical parity problem and the additional axiom used to break it in their setting.

Status: `CONCEPT-VERIFIED / EXACT-BOOK-LOCATION-OPEN`.

The manuscript's wording must remain diagnostic rather than absolute: classical local-divisibility sieve data alone do not distinguish prime parity patterns sufficiently to yield the desired lower bounds.

The supporting conceptual citation includes `FriedlanderIwaniec1998AsymptoticSieve`, but this does not close the exact book-location requirement.

## Current decision

```text
POST-AUTHORING-BUILD-AUDIT = PASS
REFERENCE-BIBLIOGRAPHY      = PASS
REFERENCE-TEXT-MATCHING     = PARTIAL
SELBERG-DENOMINATOR         = TEXT-LOCATION-VERIFIED / NORMALIZATION-MATCHED
FUNDAMENTAL-LEMMA           = CHAPTER/PAGE-RANGE-VERIFIED
PARITY-BARRIER              = CONCEPT-VERIFIED / EXACT-LOCATION-OPEN
REFERENCE-AUDIT             = OPEN
CHAPTER-15                  = AUTHORED-DRAFT
REVIEWED                    = NO
PR-28                       = DRAFT / OPEN / UNMERGED
```

No merge is authorized by this audit.
