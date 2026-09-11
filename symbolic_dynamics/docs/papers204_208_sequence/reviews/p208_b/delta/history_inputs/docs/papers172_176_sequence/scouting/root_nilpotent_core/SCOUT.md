# Coordinator negative control — regular-nilpotent invariant-core erosion

**Verdict:** `KILL_DIRECT_ANTI_INVARIANT_OWNER_AND_P109_COLLISION`  
**External state:** `HOLD_EXTERNAL`.

Let `N` be one regular nilpotent Jordan block on `F_q^n` and define

```text
F(U)=U intersect N^(-1)(U)
```

on the full subspace lattice.  Iteration removes vectors whose next Krylov
step leaves the current subspace; the fixed states are exactly the `n+1`
members of the invariant Jordan flag.  A binary exact pilot through `n=6`
finds sharp height `n-1`, with `2^(n-1)` deepest hyperplanes.  The first-step
fibres over successive fixed flag targets are

```text
n-r = 0,1,2,3,4,5,6:  1,1,3,7,31,143,1135.
```

The apparent inverse axis is not fresh.  After quotienting by a fixed flag
target, the condition is precisely

```text
W intersect N^(-1)(W)=0,
```

equivalently `W cap N(W)=0`; these are anti-invariant/splitting subspaces.
Prasad--Ram, *Enumeration of Anti-Invariant Subspaces and Touchard's Formula
for the Entries of the q-Hermite Catalan Matrix* (arXiv:2304.13947), directly
enumerate anti-invariant subspaces for finite linear operators.  Aggarwal--Ram,
*Splitting Subspaces of Linear Operators over Finite Fields* (Finite Fields
and Their Applications 2021, DOI 10.1016/j.ffa.2021.101982), give explicit
cyclic-nilpotent splitting counts.  In addition, P109 already occupies the
regular-nilpotent/full-subspace-lattice clock-and-fibre proof vocabulary.

Accordingly the attractive small sequence is owner confirmation, not a paper
signal.  No theorem contract or reserve is created.  `explore.py` remains only
as a reproducible negative-control pilot.
