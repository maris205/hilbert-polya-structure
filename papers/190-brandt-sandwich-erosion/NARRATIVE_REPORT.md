# Narrative report — P190 Round 0

## Problem

Let `B_n={0} union [n]^2` be the aperiodic Brandt semigroup.  On a cyclic word
of length `m`, update every coordinate by `x_i <- x_i x_(i+1) x_i`.  The goal
is to resolve all iterates, transients, fixed points, every labelled one-step
fibre, and the image without hiding behind generic finite-map arguments.

## Mechanism

For a nonzero matrix unit `u`, the local sandwich `u v u` equals `u` exactly
when `v=u*`; otherwise it is zero.  Values therefore never change colour:
they persist while a forward run of inverse-compatible edges remains and are
then erased.  The inverse side is different.  An output letter defines a
zero-one transition matrix on adjacent source letters.  A nonzero output pins
one source edge, so an arbitrary target fibre factors into powers of the
zero-output matrix across cyclic zero gaps.

## Theorem-level progress

- `T^t(x)_i` equals `x_i` exactly when the next `t` compatibility edges are
  good; otherwise it is zero.
- Fixed-state counts are `1+n` for odd `m` and `1+n^2` for even `m`.
- Every nonfixed point has tail one plus its longest cyclic good run.  For
  `n>=2` the sharp maximum is `m` for odd `m` and `m-1` for even `m`; for
  `n=1` it is `max(0,m-1)`.
- Every target fibre is `tr(prod_i M_(y_i))` and, when the target has nonzero
  anchors, an explicit product of entries of powers of `A=M_0`.
- The all-zero fibre is governed by `s_0=2`, `s_1=n^2`,
  `s_m=n^2 s_(m-1)+s_(m-2)` plus the exact `+1/-1` multiplicities.
- The target image is characterized solely by zero-gap lengths, and all
  target fibres sum to `(n^2+1)^m`.

## Subtraction and status

Brandt multiplication and identities, fixed-element sandwich variants,
semigroup-induced cellular automata, and de Bruijn predecessor matrices are
background and receive zero contribution credit.  The generic erosion motif
also receives zero credit.  The retained package is the conjunction of the
parity-sensitive temporal classification and the explicit every-target
inverse factorization for this literal map.

The owner search is bounded.  No novelty, priority, completeness, or freedom-
to-operate claim is made.  The manuscript remains `OWNER_AMBER /
HOLD_EXTERNAL`.

