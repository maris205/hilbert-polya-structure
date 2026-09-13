# Initial Proposal: A Quartic Period-Three Separator

## Problem Anchor

Cantat--Dujardin exhibit a normalized quartic Jacobian-minus-one Henon family
whose period-one and period-two multiplier traces are constant. Their general
finite-cutoff theorem is non-effective. The target problem is to determine the
first trace period that separates conjugacy on the complete normalized
quartic fixed-trace-zero fiber.

## Initial Approach

1. Prove that every monic-centered quartic with fixed trace multiset \(0^4\)
   has
   \[
   p(x)=(x^2-L)^2.
   \]
2. Compute the formal exact-period-three second trace moment:
   \[
   S_2^{(3)}(L)=-1296000-1572864L^3.
   \]
3. Prove normalized conjugacy is classified by \(L^3\).
4. Conclude that period three is the minimal separator on this fiber because
   periods one and two are constant.

## Initial Strength

The proposal gave a sharp, falsifiable, exact answer on the direct 2026
obstruction. It was intrinsic: \(L^3\) is the normalized conjugacy coordinate
and is recovered from the formal periodic derivative trace, not inserted as a
label or target weight.

## Initial Weakness

The quartic calculation alone was judged too small for the Batch-04
standalone-paper gate. The family and low-period blindness were already in
Cantat--Dujardin, while global-residue and formal-period tools were mature.
Without a broader mechanism, the result risked reading as one exact
elimination identity.

## Required Refinement

Preserve the quartic theorem as the dominant contribution, but add only the
smallest degree-uniform mechanism that explains it:

- a formal all-\(m\) period-three residue law on
  \(f_{m,a}=(y+(x^m-a)^2,x)\);
- an exact quotient coordinate \(a^{2m-1}\);
- a transparent finite certificate for the slope \(D_m\);
- an explicit nonclaim that universal \(D_m\ne0\) is open.

No unrelated height, prime, zero, unstable-spectrum, or global-rigidity route
is permitted as a paper-size patch.
