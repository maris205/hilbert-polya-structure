# Coordinator's AS2 component review

2026-09-07. This is internal mathematical review, not peer review, an
admission or a formal Route A evaluation. The coordinator proposed the
initial conjecture and helped formulate later repairs; this record is
not a nonauthor review of the final assembled classification.

## Actual scope

Read in full:

- [The fixed-coordinate counterexample proof](independent_review/PROOF_PACKAGE.md),
  including its imprimitive-character minimal-level auxiliary lemma.
- [Its exact reconstruction code](independent_review/exact_check.py),
  [execution receipt](independent_review/CHECK_RECEIPT.md), and
  [source audit](independent_review/SOURCE_AUDIT.md).
- [The principal all-exponent proof](oldform_review/PROOF_PACKAGE.md)
  and [review receipt](oldform_review/REVIEW_RECEIPT.md).

The broader primary-source access is recorded in
[AS2_SOURCE_AUDIT.md](AS2_SOURCE_AUDIT.md). In addition, the coordinator
directly checked [DLMF §25.15](https://dlmf.nist.gov/25.15), especially
the Euler product, imprimitive deletion identity and primitive functional
equation. These supply classical analytic facts, not a new theorem.

No accepted numerical check was rerun. The following conclusions come
from reading and checking the actual arguments and code, not from a new
execution or a favorable author summary.

## Counterexample and minimal-level lemma

No unresolved mathematical gap was found in the stated bounded results.
In particular:

1. The twelve cusps at $N=50$ give exactly the complete four-coordinate
   paired quartic sector used in the proof. Its Fourier matrix is fixed.
2. Substitution into the actual Young divisor sum gives the displayed
   oldform matrix and the equal-character, conjugate-pair functional
   equation. No character pair or complex conjugation is silently changed.
3. Comparing constant terms transfers that equation to the original
   scattering matrix in a fixed basis. The parameter-dependent incoming
   matrices are intermediate factors, not claimed fixed similarities.
4. The primitive even Dirichlet functional equation converts the apparent
   zero-times-pole factor at positive integers into a finite, nonzero
   gamma and Euler-product ratio. Both test parameters lie in the
   holomorphic incoming-series half-plane.
5. The constant Gauss and Walsh changes leave a genuine invariant block
   with commutator diagonal entries $\pm384i/221$, multiplied only by a
   common nonzero scalar. The code reconstructs the divisor sum in
   $\mathbb Q(i)$; it does not certify the analytic prerequisites by itself.
6. The minimal-level converse retains the deleted Euler factors before
   applying the primitive functional equation. The coefficient at a
   prime outside the conductor distinguishes a nonreal square character;
   absolute convergence justifies Dirichlet-series uniqueness. This proof
   is restricted to its stated minimal-level paired block.

The original conjecture is therefore refuted. The small counterexample
and auxiliary lemma alone remain insufficient for a paper slot.

## Principal oldforms

No unresolved mathematical gap was found in the all-prime/all-exponent
principal-sector theorem. The independent cusp reduction gives exactly
the coordinator's incoming matrix; the expansion into class-sum series
then proves invariant-subspace applicability rather than assuming it.
The diagonal class-size similarity is independent of the spectral
parameter.

The fixed difference vectors satisfy the asserted generalized eigenvector
identities by finite geometric summation. The even central polynomial
is reciprocal under the specified variable replacement. The odd central
quotient has the same reciprocity after its linear factor is removed;
its apparent quadratic denominator does not exclude a regular parameter,
because the identity holds after clearing denominators. The support and
coordinate-sum arguments give a complete basis in both parity cases,
including exponents zero and one. Repeated eigenvalues and removable
singularities do not invalidate that fixed basis or the continued
commutator identity.

This also justifies the principal tensor corollary at composite levels
and the stated conditional real-sign conjugacy. It does not, by itself,
prove the full cusp-family criterion. The third author's bibliographic
name in the first draft was flagged for correction to Strömbergsson;
this prose correction requires no mathematical rerun.

## Remaining whole-contract gate

The all-level character decomposition, nonreal-square necessity, quartic
phase parity and tensor noncancellation are being assembled in separate
proof documents. The two earlier false analytic guesses remain preserved.
The new parity-sensitive arithmetic lemma is not substituted for those
analytic implications.

Once assembled, the complete theorem requires a reviewer who did not
help derive it, including a substantive-increment assessment after the
classical scattering formulas are deducted. There is still no new target
Euler/root-number statement, autonomous clock or Hilbert–Pólya realization.
