# P170 paper plan

**Working title:** Endpoint Histories in a Random-Permutation Fixed-Point
Sieve  
**Format:** anonymous short theory note, `amsart` 10pt  
**Lifecycle:** `ROUND0 AUTHOR FREEZE / HOLD_EXTERNAL`

## Claim spine

The literal state is a labelled subset of `[n]`.  An independent uniform
permutation is sampled at every epoch, and the state is intersected with its
fixed-point set.  The note has two deliberately unequal axes.

1. **Self-contained unmarked axis (zero contribution credit):** pathwise
   common-fixed identity, exact every-endpoint inclusion--exclusion kernel,
   support exception, Boolean-zeta eigenbasis, absorption CDF/survival/PGF
   and first two moments, including separate `n=1,2,3` boundaries.
2. **Retained marked axis:** weight each complete history by the total number
   of cycles in its sampled permutations.  Give the exact endpoint
   polynomial, prove its sharp least and greatest degrees for every supported
   endpoint (including `d=1`), and derive the exact endpoint-conditioned mean
   total cycle count.

The theorem ceiling is the endpoint-resolved conjunction.  It does not claim
the individual ingredients—common fixed points, prescribed fixed labels,
Boolean semilattice spectra, inclusion--exclusion, absorption algebra, or
ordinary cycle polynomials.

## Section architecture

- **1. Literal process and theorem package.** Define the update without an
  implicit convention; state one complete theorem and the ownership ceiling.
- **2. Unmarked histories, spectrum, and absorption.** Prove the kernel,
  support, containment diagonalization, transforms, and the mandatory `n=3`
  repair.
- **3. Cycle-marked endpoint histories.** Derive the polynomial, prove both
  sharp degree bounds by explicit histories, and differentiate for the
  conditional expectation.
- **4. Claim boundary and exact pressure.** State all zero-credit ingredients,
  the bounded nature of the owner search, and the role of the verifier.

No figure is planned: the only nontrivial dependency is algebraic, and the
formulas plus the parity-split witness construction are more precise than a
diagram.

## Proof obligations

- `t=0` must give the Kronecker delta, not only a positive-time formula.
- The only positive-time missing containment edge is a full source and an
  `(n-1)`-point target.
- The eigenvalue collision `lambda_(n-1)=lambda_n` must be stated.
- The two-scale absorption expansion starts at `n>=4`; `n=3` is exact and
  separate because ranks two and three collide.
- Marked coefficients are nonnegative by literal enumeration, not by an
  unproved assertion about an alternating sum.
- The maximum marked degree must treat `d=0`, even `d`, odd `d>=3`, and
  `d=1` separately.
- The conditional expectation is stated only for supported endpoints, so its
  denominator is positive.

## Evidence and release rule

The author verifier must be independent of the hostile gate, use exact
integers/rationals, replay byte-identically at least twice, and check every
theorem boundary.  The LaTeX source must compile twice in fresh directories
containing only `main.tex` and `references.bib`, and both PDFs must match the
canonical PDF byte for byte.  External release remains on hold regardless of
internal mathematical status.
