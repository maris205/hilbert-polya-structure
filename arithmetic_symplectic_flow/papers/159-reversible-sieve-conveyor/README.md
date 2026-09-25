# 159: reversible sieve conveyor

**Candidate ID:** ASFS-20260915-RSC01  
**Date:** 2026-09-15  
**Status:** STOP — COMPLETE REVERSIBLE SOURCE CONVEYOR; NO INTRINSIC CLOSED ORBITS.  
**Portfolio decision:** STOP / FORK.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

This exact two-dimensional symplectic map executes a chronological divisor
scan, reads its output, uncomputes the scan, and proceeds to the next integer.
It retains every real register state and has a specified prime-independent
negative tail, so its evolution is globally reversible rather than a
one-sided computation or an independent fixed-input map for each n.

The full carrier is explicitly conjugate to integer translation times the
identity on R². Its unit-roof suspension is complete and has no closed orbit
at all. This is stronger than a claim about the designated clean-register
trajectory, but is only an explicit new realization of a known monotone-clock
obstruction. It is not a new universal impossibility result.

The finite closed compute–uncompute control does not repair the situation:
its return map is the identity on the entire real register plane, for prime
and composite inputs alike. No centre, calibrated register or selected phase
is removed to disguise that multiplicity.

- [Full definition and proofs](paper.md)
- [Frozen candidate card and disposition](candidate-card.md)
- [Scoped claim ledger](claim-ledger.md)
- [Evidence and verification](evidence/README.md)
- [Previous frontier and source chronology limitation](../156-multi-round-source-trace-frontier/paper.md)

The source arithmetic is operationally positive, while the full-state A1
closed-orbit proposal fails. No determinant, trace, exact prime-log clock or
formal Route advancement is claimed.
