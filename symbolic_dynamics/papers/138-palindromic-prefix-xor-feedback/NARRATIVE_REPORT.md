# Narrative report — P138

## Research question

What happens when a word is not replaced by one selected palindrome statistic,
but by the synchronous XOR of all of its palindromic-prefix decisions?

## Mechanism

The first coordinate always flips.  Quotienting by global complement therefore
removes a phase variable and exposes the real mechanism: one application forces
the first three normalized coordinates to zero, and each later application
extends any zero prefix by at least one place.  This is a deterministic
synchronizing amplifier rather than a generic Boolean-network argument.

## Main progression

1. Complement invariance of palindrome tests gives an exact quotient map.
2. The quotient has the unique attractor `0^n`; the phase lift is the strict
   two-cycle `0^n <-> 1^n`.
3. The amplifier gives the upper clock `n-2`.  The periodic source with ones
   at positions `3 mod 4` enters a chain of alternating tails, showing that
   every unit of the bound is necessary.
4. Inverting one step is unexpectedly local after conditioning on the already
   chosen source prefix.  A nonpalindromic middle forces the next bit; a
   palindromic middle either branches twice or rejects the target.  The target
   first bit fixes the phase, so the quotient decoder is already the original
   fibre count.

## Evidence discipline

The paper-local program exhausts complete functional graphs through length 18,
all targets for the decoder through length 15, and the sharp closed family
through length 64.  These checks test the proofs but are not used to infer
unbounded results.  Observed image and maximum-fibre sequences are reported as
control data only.

## Credit boundary and status

Palindrome recognition, palindromic trees, static palindromic generation, and
prefix-palindrome encodings are fully credited background.  The admissible
claim is only the repeated full-vector XOR feedback and its exact temporal and
inverse theorems.  External release remains `HOLD_EXTERNAL`.
