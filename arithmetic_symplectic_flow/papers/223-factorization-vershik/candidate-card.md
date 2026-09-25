# Frozen candidate card — ANG-20260918-FVP01

**Paper ID:** 223-factorization-vershik  
**Candidate ID:** ANG-20260918-FVP01  
**Date:** 2026-09-18  
**Version:** 1; frozen before the gate audit.  
**Initial status:** PRE-P0 SCREEN — CANONICAL VERSHIK SUCCESSOR NOT A BIJECTION  
**Formal Route coordinates:** UNASSIGNED; **Route B:** NOT INVOKED.

## Frozen carrier and proposed action

Let \(\mathcal P\) denote the primes as *derived* atoms.  For positive
rationals, write \(x<_{D}y\) when \(y/x\in\mathbb N\) and \(y/x\ge2\).  A strict cover
\(x\prec_{\rm cov}y\) is an interval with no \(z\) satisfying
\(x<_{D}z<_{D}y\).  The cover ratio is then a prime, by the elementary
factorization test; no prime table is supplied as input.

The factorization graph has vertex set \(\mathbb Q_{>0}\) and ordered edges

\[
  x\longrightarrow xp\qquad(p\in\mathcal P),
\]

where the outgoing edges at a fixed \(x\) are ordered by the ordinary
integer order of \(p\) (equivalently by the child endpoint \(xp\)).  Freeze the
normalized two-sided path carrier

\[
 X_{\rm FVP}=\{x=(x_j)_{j\in\mathbb Z}:x_0=1,\;
 x_j\prec_{\rm cov}x_{j+1}\text{ for all }j\}.
\]

Write \(p_j(x)=x_{j+1}/x_j\).  Thus \(p(x)\in\mathcal P^{\mathbb Z}\), with
the product topology on the discrete prime alphabet.  The proposed
Bratteli–Vershik-style action \(V\) is the lexicographic successor with
carry: scan a designated carry ray from index \(0\) toward negative indices,
increment the first non-maximal outgoing edge in the ordinary order, and
reset all earlier edges on the ray to the minimal edge \(2\).  If no such
edge exists, the endpoint convention must be stated; no endpoint or wrap is
silently added.  The intended scale cocycle is

\[
 \kappa(x)=p_0(x)=x_1,\qquad
 G(x,r)=(Vx,r/\kappa(x))\quad (r>0),
\]

with the prospective multiplicative time observable \(\log\kappa\).  This
scale quotient is only a declared downstream owner; it is not asserted to be
a flow until \(V\) is a homeomorphism.

| Field | Frozen scope |
| --- | --- |
| Carrier/type | Two-sided divisor-cover factorization paths; nonclassical ANG path/action candidate |
| Lineage arrow | Prime/composite divisor observable → cover-prime symbolic edges → factorization paths → proposed lexicographic/carry return |
| Arithmetic input | Positive rational divisibility and ordinary integer order only; no supplied prime list, prime times, von Mangoldt data, or zeros |
| Action | The exact successor/carry rule above; a global endpoint/wrap is OPEN, not implicit |
| Primitive packets | All actual periodic \(V\)-orbits, modulo cyclic phase, if \(V\) exists; no selected constant-word sector |
| Clock / cocycle | \(\kappa=p_0\), with a prospective multiplicative scale quotient; actual roof and repetitions OPEN until \(V\) exists |
| Operator / trace / determinant | NOT SUPPLIED; only a future same-object owner could be considered |
| Classical symplectic fields | NOT APPLICABLE; no finite-dimensional map or suspension is claimed |
| Controls | Unbounded outgoing order; minimal-edge preimage; finite-prime truncation; two-sided carry-ray ambiguity; mixed factorization paths |
| Stop/fork rule | If the canonical successor is non-surjective, stop before P0. Adding a maximal symbol, wrap, finite cutoff, or one-sided boundary is a new candidate ID |
| Route state | Owner-level T0–T3 not entered; formal Route-A coordinates unassigned; Route B not invoked |

## Precommitted discriminators

1. Prove the cover-ratio/prime correspondence from the divisor order, rather
   than importing a prime alphabet.
2. Check whether the ordinary-order edge set has a maximal element needed by a
   carry.  If not, test the no-carry increment and its image.
3. Check both \(V\) and \(V^{-1}\) on the full two-sided path carrier, not on a
   finite selected word set.
4. Keep a mixed path (for example alternating \(2,3\)) and the all-\(2\)
   path in the carrier; no periodic-sector restriction is allowed.
5. Only if a bijective action survives, classify primitive paths, scale return
   times and the same-object quotient. Otherwise record the early stop.

Changing the endpoint convention, adding a largest prime, taking a finite
alphabet, or replacing the successor by the shift changes the frozen action.
Those repairs cannot inherit this card's source or gate evidence. In
particular, the unit-roof full shift in
[148](../148-saturated-divisibility-chain-shift/paper.md) and the ordered
scale carrier in [163](../163-ordered-cover-scale-suspension/paper.md) are
separate objects; no result from either is transferred here.

## Correction receipt — 2026-09-18

The initial audit wording incorrectly treated the absence of a maximal prime
as if the stated scan for the **first non-maximal** digit were undefined.
It is not: every digit is non-maximal, so the scan stops immediately at
index \(0\).  Under the frozen rule the actual map is the everywhere-defined
next-prime update at \(p_0\), with all other coordinates unchanged.  The
decisive obstruction is therefore non-surjectivity (the states with
\(p_0=2\) have no preimage), not undefinedness.  The candidate definition is
unchanged; this receipt corrects only the gate reasoning.  In particular, the
“no such edge” endpoint branch is unreachable for the frozen ordinary order.
