# C165 two-round paper improvement log

## Round 0

The initial internal draft recorded the counterpropagating site permutation
and the fixed-count formula.  It did not yet expose a configuration-level
conjugacy or operator owner.

## Round 1: theorem completion

- Added the reversed-odd pairing and proved exact conjugacy to a four-letter
  length-`m` cyclic rotation.
- Promoted fixed counts to the complete exact-period, primitive-cycle, and
  finite-zeta law for every `m>=1`.
- Added the deliberately coarse but uniform short-period bound and treated
  `m=1` and `m=2` explicitly.

## Round 2: reversibility and hostile scope audit

- Added the reflection reversor, finite same-clock Koopman determinant, and
  antiunitary time reversal.
- Recorded the rejected Rule-90 continuation and prevented a failed broad
  claim from being reframed as Margolus evidence.
- Stated that the conjugate necklace dynamics is not claimed to be chaotic or
  interacting and made no uniform self-adjoint Hilbert--Polya claim.
- Closed independent checker, SymPy, byte replay, repaired-hash mutation,
  deterministic bilingual build, declarations, and manifest requirements.

These are two rounds of internal theorem and artifact review.  They are not
external peer review and do not claim a reviewer-independent error process.

## Post-round hostile audit repair

- Replaced a blanket non-self-adjoint sentence by the exact family boundary:
  `U_T` is self-adjoint for `m=1,2` and non-self-adjoint for every `m>=3`.
  The period theorem supplies the required `m`-cycle witness.
