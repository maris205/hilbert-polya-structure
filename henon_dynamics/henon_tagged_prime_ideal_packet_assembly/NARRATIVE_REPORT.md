# Narrative Report

## Research question

HCS-P49 proved that the full multiplier-field norm doubles the inversion
pair and therefore becomes a square.  It left the trace-field half packet
and its principal ideal as the smallest exact arithmetic survivors.  The
next question is whether those local survivors can be put on one ledger
across several primitive H6 orbits without silently identifying inequivalent
prime ideals or residue clocks.

## What is proved

For every finite collection of signed primitive H6 orbit/index pairs, the
prime-ideal factorizations of the half packets define a canonical free
divisor ledger with basis symbols `(orbit, index, trace prime ideal)`.  The
rational norm map is an exact homomorphism from that ledger to the free
divisor group on rational primes.  At residue characteristic not dividing
the cyclotomic index, every supporting multiplier-field residue class has
exact order equal to that index.

This is a source-native finite assembly theorem.  It retains the actual
negative period-three branch and uses no target prime table, zero table, or
fitted weight.

## What is rejected

The norm pushforward is not injective on the exact certificate.  Its domain
has 125 tagged atoms, its image is supported on 95 rational primes, and its
free kernel has rank 30.  Collisions occur across orbits, indices, and prime
ideals.  The rational prime 29 alone supports certified residue orders 7,
14, and 15.  Therefore a bare rational prime is not enough to recover the
intrinsic packet clock.

This is not a claim that no useful scalar statistic exists.  A weighted
pushforward may still be useful.  The proved obstruction is to treating that
pushforward as a lossless, unique identification of the source packets.

## Why the result matters

The project converts the vague phrase “retain the ideals” into an explicit
data type and a theorem.  It also locates exactly where scalarization loses
information.  The next analytic object should therefore be vector-valued at
the source and should postpone rational norm pushforward until after
convergence and pressure weighting have been proved.

## Evidence boundary

The theorem is finite-cutoff and algebraic.  The exact implementation covers
three primitive controls and indices 3--20.  It proves neither an all-orbit
limit nor a prime-distribution theorem.  Existing primitive-divisor results
for Lucas, Lehmer, or fixed-map dynamical sequences do not supply the missing
varying-orbit H6 assembly.
