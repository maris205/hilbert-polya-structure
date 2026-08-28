# Hostile review — P85

**Verdict: GO** for the theorem-bearing internal paper after the corrections
listed below.  The standing prohibition on public posting or priority claims
in `README.md` is unchanged.

Audit date: 2026-08-28 UTC.

## Formula-by-formula audit

- For `x in X_r`, coordinate `kp-r+t` belongs to `A_t`, so every displayed
  block lies in `B=A_0 x ... x A_(p-1)` and the blocks partition all integer
  coordinates.
- The conjugacy alignment is exact.  Before the wrap,
  `(Phi_(r+1)(Tx))_(k,t)=x_(kp-r+t)=(Phi_r(x))_(k,t)`; at `r=p-1`,
  `(Phi_0(Tx))_(k,t)=x_(kp+t+1)=(Phi_(p-1)(x))_(k+1,t)`.  This matches the
  declared left-shift direction in the cyclic suspension.
- The displayed `p` is the intrinsic graph period, not merely a presentation
  length: disjoint phase alphabets force every closed walk length to be a
  multiple of `p`, and a length-`p` closed walk exists.  Thus the
  classification by `(p,Q)` has the required minimal-period qualifier built
  in without an extra minimality assumption.
- The fixed-point count, zeta, and entropy follow from the suspension:
  `T^(pk)` is the full `Q`-shift's `k`th power on each of `p` components and
  nonmultiples of `p` change phase.
- For the block-cyclic adjacency matrix, the direct sum of phasewise
  sum-zero spaces has dimension `sum(q_j)-p` and is annihilated.  On the
  phase-indicator space, the matrix is a weighted cyclic shift with `p`th
  power `Q I` and a cyclic vector.  Hence its characteristic polynomial is
  exactly `lambda^(sum(q_j)-p)*(lambda^p-Q)`.

## Corrections applied

1. Added both coordinate identities to the block-conjugacy proof, fixing the
   alignment and shift direction explicitly.
2. Replaced the informal eigenvector paragraph by a proposition and complete
   invariant-subspace proof of the characteristic polynomial, including the
   zero multiplicity.
3. Added direct control assertions for alphabet alignment, non-wrap
   alignment, and wrap alignment over positive and negative block indices.
4. Restored one missing backslash before `\qquad` in the size display.

## Reproducibility and release checks

- Deterministic control: **PASS — 5,242 exact assertions across 340
  schedules**.
- The control covers all schedules of lengths `1<=p<=4` with phase sizes
  `1..4`, direct traces, exact characteristic polynomials where matrix size
  permits, same-class ledgers, factorization-collapse witnesses, and a
  separate block-alignment grid for `1<=p<=6` and block indices `-3..3`.
- Four-stage build (`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`): all exits
  zero.
- Final PDF: **4 A4 pages, 310,975 bytes**.
- Log scan: no undefined references/citations, LaTeX errors, overfull or
  underfull boxes, fatal errors, or rerun requests.
- Fonts: **24/24 embedded, subsetted, and Unicode-mapped**.
- Visual inspection: all four pages clean; no clipping, collision, or stray
  `qquad` text.

## Surviving scope boundaries

The theorem assumes nonempty, pairwise-disjoint phase alphabets, includes
all clock phases, uses unconstrained complete transitions from one phase to
the next, and takes `Q>=2`.  It does not classify constrained rectangular
transition schedules or a nonautonomous system before the clock extension.
General nonautonomous entropy/zeta theory and finite-type determinant theory
remain cited background; no priority claim is made.
