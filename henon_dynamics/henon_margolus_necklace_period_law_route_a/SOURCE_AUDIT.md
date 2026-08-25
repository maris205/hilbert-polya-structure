# C165 source audit

## Frozen source

- Candidate: `HCS-C165`.
- Repository source commit: `4342893ce5e2516924181744bfacc01c12e4959d`.
- Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.
- Phase space: binary configurations on the labelled ring
  `Z/(2m)Z`, for every `m>=1`.
- First half-step `A`: swap `(0,1),(2,3),...`.
- Second half-step `B`: swap
  `(1,2),(3,4),...,(2m-1,0)`.
- One source clock tick is the complete composition `T=B after A`.  Neither
  half-step is silently counted as a full tick.
- Normalization: labelled configurations first, exact least full-tick
  periods second, geometric cycles only after division by the period.
- Determinant convention: the finite Artin--Mazur zeta and the ordinary
  determinant of the same-clock finite Koopman permutation.

## Recorded model pivot

The initial continuation proposed another broad composite-clock Rule-90
closed law.  It was rejected before paper construction: the general
trace-zero subgroup count has no uniform elementary reduction, and three
preceding rounds already occupy that lineage.  C165 changes dynamical
subtype to a reversible two-phase Margolus partitioned cellular automaton.
The rejection is not described as a result of the replacement model.

## Source ownership and proof boundary

The local swap schedule alone determines the site permutation, the
four-letter pairing, every fixed-point count, the exact-period inversion,
the reflection reversor, and the Koopman matrix.  The theorem applies to
every `m>=1`; the replay through `m=16` and direct enumeration through `m=8`
are regression sentinels only.

The exact conjugacy makes the full-tick map a cyclic rotation of an
`m`-letter word over the alphabet `{0,1}^2`.  Consequently this package does
not call the model chaotic or interacting.  Its natural finite Koopman lift
is self-adjoint at the exact boundaries `m=1,2` and non-self-adjoint for
`m>=3`; no uniform self-adjoint Hilbert--Polya realization is claimed.

## Forbidden inputs and claims

No target zero table, target prime table, target divisor, target functional
equation, target counting law, arithmetic local datum, Euler factor, root
number, automorphy object, or Route-B input is read or frozen.  Source gcds,
divisors, and Moebius inversion are finite-clock bookkeeping only.

`route_b_invocation_allowed=false` remains frozen.
