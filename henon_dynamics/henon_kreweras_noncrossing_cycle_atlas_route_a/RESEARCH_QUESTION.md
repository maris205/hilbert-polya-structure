# Research question

**Can one freeze the ordinary Kreweras complement as a finite clock and close
its entire all-iterate cycle/Koopman ledger with auditable evidence while
keeping the Route-A arithmetic firewall explicit?**

The answer delivered by C209 is yes at the source-theorem level: the type-A
order-2n CSP supplies every fixed count, and finite permutation identities then
supply exact periods, cycles, zeta factors, determinant, spectrum, rank
duality, and reflection reversal.  The answer is deliberately negative for
arithmetic promotion: Catalan labels and rotations do not provide an intrinsic
rational-prime clock or a target divisor.

## Frozen assumptions

* n ranges over all positive integers; computational formula rows stop at n=24.
* Vertices are 0,...,n-1, and K uses p_pi^(-1)c with c(i)=i+1 mod n.
* The actual action order is 1,2,2n for n=1,2,>=3; CSP bookkeeping uses the
  abstract order G_n=1,2n,2n,... .
* No data from target zeros/primes, local arithmetic, Euler products, root
  numbers, or Route B are admitted.

## Falsifiers

The package is considered failed if direct enumeration disagrees with the
fixed formula; K^2 disagrees with the declared rotation; Mobius populations
are negative/nonintegral or do not sum to Catalan; a q-Catalan root remainder
disagrees; a reflection fails the dihedral relation; or a repaired-hash/stale-
hash mutation is accepted.
