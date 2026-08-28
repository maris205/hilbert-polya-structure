# Hostile review — P82

Audit date: 2026-08-28 UTC

Reviewer disposition: **GO for internal short-note freeze; external HOLD**

## Bottom line

The theorem package survives adversarial proof and control checks.  The
if-and-only-if local boundary rule, the cyclic trace formula, the rank-two
characteristic polynomial, the closed count, and the explicitly spatial zeta
function are correct, including the delicate ring-size-one endpoint.  I found
no mathematical release blocker.

The contribution should remain framed as a short exact-enumeration note.  Once
the local matrix is displayed, the entropy and determinant-zeta consequences
are standard SFT machinery; the residual content is the derivation of that
matrix for this particular two-layer network and the resulting all-size count.
No broader novelty claim is supportable from this package.

## Proof audit

1. **Layer order and locality — PASS.**  After the aligned gate on
   `(a_j,b_j,c_j)`, the shifted gate restores exactly
   `(b_j,c_j,a_{j+1})`.  These shifted triples partition the ring, so the
   local pair predicate is necessary and sufficient globally.  For `m=1`,
   the shifted triple is `(b_0,c_0,a_0)` with three distinct sites, and the
   same proof still applies.
2. **Transfer matrix — PASS.**  Reverse evaluation of all 64 ordered block
   pairs reproduces the displayed rows: `000,100,001` allow every successor;
   `010` requires next first bit zero; `011,111` require it one; `110,101`
   have no successor.
3. **Trace count — PASS.**  Labelled cyclic block words of length `m` are
   counted by `tr(M^m)` without quotienting by spatial rotation, exactly as
   required for fixed binary ring configurations.
4. **Spectrum — PASS.**  The row space is spanned by the even- and odd-column
   indicator rows, so `rank(M)=2`.  Nullity gives at least six zero roots;
   `tr(M)=5` and `tr(M^2)=19` force the remaining roots to have sum five and
   product three.  Hence
   `det(lambda I-M)=lambda^6(lambda^2-5lambda+3)`.
5. **Entropy and zeta — PASS.**  The largest root is positive and strictly
   dominates the other root.  Standard finite-type-shift identities give the
   stated block entropy and `det(I-zM)^{-1}`.  The manuscript consistently
   distinguishes this spatial shift zeta from temporal iteration of `T_m`.
6. **Reversibility/conservation — PASS.**  Both disjoint gate layers are
   involutions; `(B_m A_m)^{-1}=A_m B_m`, conjugation by `A_m` reverses the
   map, and each gate preserves Hamming weight.

## Independent controls

- The package control was rerun verbatim: **299,592 states** and
  **1,878,811 assertions**, ending in PASS with the recorded cycle census.
- A separate tuple-based implementation, not importing the package script,
  exhaustively checked the literal map against the SFT predicate for
  `m=1,...,5`; it returned fixed counts `5,19,80,343,1475`.
- An independent symbolic characteristic-polynomial calculation reproduced
  `lambda^6(lambda^2-5lambda+3)`.

## Ownership and terminology audit

The cited ownership chain is materially appropriate:

- Fredkin--Toffoli own conservative logic and the Fredkin conditional
  interchange primitive (DOI `10.1007/BF01857727`).
- Toffoli--Margolus and Kari own the alternating/overlapping reversible block
  architecture; Kari's abstract explicitly concerns a two-layer Margolus
  neighborhood with overlapping partitions (DOI `10.3233/FI-1999-381208`).
- Morita owns the survey-level embedding of Fredkin gates in simple reversible
  cellular automata (DOI `10.1080/17445760.2022.2052871`).
- Singh--Vasseur--Gopalakrishnan own the distinct three-layer, four-site
  Fredkin staircase and its transport/integrability analysis
  (DOI `10.1103/PhysRevLett.130.046001`).

One terminology issue was corrected during this audit.  Fredkin and Toffoli's
1982 table is control-on-zero, whereas the present map is control-on-one.
The abstract, introduction, comparison paragraph, and definition now state
the actual convention, and the definition explicitly assigns the original
control-on-zero table to its source.

Bounded searches for the exact phrases and invariant package (`shifted
Fredkin` fixed points, staggered Fredkin frozen states, Fredkin transfer
matrix, and the polynomial `1-5z+3z^2`) found no direct owner of this exact
two-layer frozen-set calculation as of the audit date.  This is only a narrow
collision check, not evidence of absolute priority; the manuscript's external
HOLD and no-priority language must remain.

## Release audit after correction

- Four-stage `pdflatex / bibtex / pdflatex / pdflatex`: PASS.
- PDF: **6 A4 pages**, **336,857 bytes**.
- Undefined references/citations: **0/0**.
- LaTeX warnings and overfull/underfull boxes: **0**.
- Fonts: **24/24 embedded, subsetted, and Unicode-mapped**.
- Visual inspection of the two changed pages found no clipping or collision.
- SHA-256: `19e0eb0ec255fe04f18f94eda26c538350ebc50b025afc1033b54fb376c82b25`.

## Residual risks

- The exact-model novelty search is bounded, not systematic across every
  reversible-circuit proceedings venue.  Do not remove external HOLD without
  a dedicated database search.
- `M` contains two zero rows.  This causes no error in periodic counts or
  entropy, but readers should understand that the eight-symbol presentation
  is not claimed to be irreducible or minimal.
- The finite temporal period table is descriptive only.  It must not be used
  to claim unbounded periods, temporal zeta rationality, or integrability.
