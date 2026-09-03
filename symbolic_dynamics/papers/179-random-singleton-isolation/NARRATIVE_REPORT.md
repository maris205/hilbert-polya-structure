# Narrative report — P179

## Problem

Start from an arbitrary labelled set partition of `[n]`.  At every epoch,
sample one label uniformly and isolate it as a singleton.  The question is
not merely when the chain absorbs, but whether the complete spectrum,
all-time source-to-target kernel, and inverse geometry can all be written in
closed form while retaining the initial block sizes.

## Mechanism

The isolation maps commute and are idempotent, so an entire history is
determined by its set of observed labels.  Inside an old block, the unseen
labels remain together; a residual of size zero or one is indistinguishable
from complete dissolution.  This turns the temporal problem into an exact
support problem and the spectral problem into simultaneous diagonalization.

## Theorem-level progress

- Complete spectrum: eigenvalue `s/n` has multiplicity
  `binom(n,s) D^*_(n-s)`, with the impossible `n-1` layer removed and the
  absorbing eigenvalue `1` simple.
- Arbitrary-source absorption CDF:
  `n^(-t) sum_m e_m(b_1,...,b_k)(n-m)! S(t,n-m)`.
- Every labelled target probability is a disjoint finite sum over explicit
  admissible missing sets.
- Every target has both a distinct-predecessor count
  `0` or `1+s(b-s)+binom(s,2)` and a labelled action-pair count `sb`.
- `n=1`, `t=0`, and the absent `n-1` singleton stratum are handled explicitly.

## Limits and status

The marked-element split, partition lattice, associated Bell numbers, coupon
support enumeration, and semigroup spectral technology are all background.
P169's deterministic block-number-preserving successor transfer and P110's
cyclic shift--join coarsening are internal carrier neighbours, not this
support-only isolation chain.  The retained contribution is the theorem
conjunction for this literal chain.
Owner status is amber and external release remains forbidden.
