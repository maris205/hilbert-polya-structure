# HCS-C63 theorem package

Status: **PREFREEZE_IMPLEMENTED / PAPER_COMPILED / NOT_RELEASED**.

## Conditional theorem

For the 16 ambient-conjugacy subgroup types `S1,...,S16` extracted from C62,
let `M` be the integer matrix whose rows are the 25 values of the permutation
characters of `G/S_i` on the 25 conjugacy classes of `G=W(E_6)`.  The target is
\[
 \operatorname{rank}_{\mathbb Q}M=13,
 \qquad \dim_{\mathbb Q}\ker M=3,
\]
with the three displayed vectors in `RESEARCH_QUESTION.md` as a basis.

Writing `r=Y15-Y16` for the original C61 Gassmann difference and `q` for the
C62 exterior-square plus-minus difference, the target also records
\[
 q=-(z_2),\qquad q_{\mathrm{sym}}=q+r,
\]
under the fixed plus-minus convention.  The headline relation is the
support-restricted primitive four-term vector `-q`; `z_1=Y10-Y9` is retained
only as an inherited C60 collision control.

## Gates

* G0: source-rebind C61 and byte-bind the C62 atlas/dictionary inputs.
* G1: reconstruct all 25 ambient conjugacy classes deterministically.
* G2: compute the complete 25-by-16 fixed-coset character matrix.
* G3: independently verify rank, nullity, basis vectors, and C62 relation
  placement, including C61 `H_+`/`H_-` character equality.
* G4: hostile schema/matrix mutations, deterministic replay, paper audit.
* G5: compile the manuscript and close the scoped manifest.

The arithmetic/local gate is intentionally outside scope.  The literal
`NO_BAD_EULER_OR_ROOT_NUMBER` remains mandatory.
