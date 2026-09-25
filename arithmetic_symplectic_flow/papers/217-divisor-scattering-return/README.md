# 217 — Divisor-port return flow

**Candidate ID:** ANG-20260918-DPR01  
**Status:** STOP — EVERY INTEGER COMPONENT HAS PRIMITIVE RETURNS; PRIME POWERS ARE NEW ORBITS, NOT REPEATS.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

A deterministic cyclic-neighbor walk on all integer divisor-cover graphs
owns a complete suspension with the uniform multiplicative edge metric
tau=abs(log(v/u)). It restores prime-component returns without selecting
prime components. However, every integer component is a nonempty finite
permutation and therefore has primitive returns, including composites.

The component p^k has exactly one primitive of time 2k log p. For k>1
it is not a repeat of the primitive in component p, even though their
time lengths agree. The component pq for distinct primes has two
oriented primitives, each of time 2 log(pq). These exact controls stop
the prime-only dictionary before any geometric lift or analytic work.

The initial divisor-symbolic lineage is explicit; no sequential sieve,
Hénon/symplectic bridge or natural A0 pass is claimed. All components
and the original clock are retained. The broader search remains active.

- [Frozen candidate and appended outcome](candidate-card.md)
- [Complete proof and controls](paper.md)
- [Claim ledger](claim-ledger.md)
- [Evidence and actual checks](evidence/README.md)
