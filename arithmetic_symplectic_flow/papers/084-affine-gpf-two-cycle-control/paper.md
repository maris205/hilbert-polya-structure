# An affine greatest-prime-factor recurrence has a complete prime-only two-cycle

**Paper ID:** 084-affine-gpf-two-cycle-control  
**Record ID:** ASFS-SCOUT-20260914-57  
**Date / status:** 2026-09-14; OWNER-LEVEL A0+A1 POSITIVE CONTROL  
**Route state:** No formal ASFS Route-A coordinate; Route B NOT INVOKED.

## Abstract

This paper freezes the one-dimensional arithmetic map

\[
H(n)=\operatorname{gpf}(n+1),\qquad n\ge1.
\]

It is a direct autonomous prime-factor deformation and has an exact global
periodic-orbit classification: the only periodic orbit is the oriented prime
two-cycle (2\to3\to2).  The proof uses no finite cutoff or prime table.
Thus this discrete map supplies a same-object A0/A1 control with a primitive
orbit and repetitions.  It does not supply a symplectic phase space, a Hénon
owner, a roofed flow, or a Route result.

## 1. Candidate identity and same-object ledger

| Item | Frozen owner | Status |
| --- | --- | --- |
| Carrier | (\mathbb N_{>0}) | discrete |
| Arithmetic mechanism | (n\mapsto\operatorname{gpf}(n+1)) | internal to same (H) |
| Lineage arrow | prime/composite observable -> autonomous recurrence deformation | direct control; no later-arrow owner |
| Primitive orbit / repetitions | (gamma=(2,3)), and its oriented traversals (gamma^r) | exact |
| Symplectic map, roof, suspension | none | NOT SUPPLIED |
| Transfer operator / zeta | none | NOT SUPPLIED |

The map's output is a prime, so its arithmetical content is not a detached
label attached to a separate symbolic system.  Conversely, it is not made
symplectic by that fact: it is noninjective, since (H(1)=H(2)=2).

## 2. Exact periodic classification

For every (n\), (H(n)) is prime.  Hence every periodic point must be prime.
For an odd prime (p\), (p+1) is even and composite.  Its largest prime
factor is at most half of it, so

\[
H(p)=\operatorname{gpf}(p+1)\le \frac{p+1}{2}<p.
\]

The only exceptional prime is (2), and direct evaluation gives

\[
H(2)=\operatorname{gpf}(3)=3,\qquad
H(3)=\operatorname{gpf}(4)=2.
\]

Thus an orbit entering an odd prime other than (3) strictly decreases until
it reaches (3), while (2) and (3) form the unique cycle.  A periodic
orbit cannot contain a strict decrease, proving

\[
\operatorname{Per}(H)=\{2,3\}
\]

as one oriented primitive period-two orbit.  Its (r)-fold traversal has
period (2r) before primitive reduction, which is the full repetition
convention for this exact discrete object.

## 3. Controls and limits

- **No finite experiment.** The classification is the displayed descent
  argument, so no bounded orbit enumeration is used as an infinite claim.
- **No direct logarithmic readout.** No roof or (log p) value is defined.
  Adding one would create a distinct object requiring a fresh card and the
  prohibition against a pointwise prime-label clock still applies.
- **No geometry transfer.** The map is noninjective and its carrier is
  discrete.  The componentwise symplectic obstruction in 080 is relevant as a
  warning, but no universal lifting no-go theorem is asserted here.
- **No cross-family transfer.** This two-cycle does not enlarge the distinct
  second-order GPF-Fibonacci packet in 078.

## 4. Gate assessment and decision

| Gate | Evidence for this exact object | Status |
| --- | --- | --- |
| A0 | fixed endogenous prime-factor rule, directly acting on its recurrence state | owner-level positive control |
| A1 | complete primitive 2-cycle and (r)-traversal convention | owner-level positive control |
| A2 | no roof, flow, operator, or target/divisor evidence | NOT EVALUATED |
| Route B | no Route-A readiness | NOT INVOKED |

**Portfolio position: stop and fork.**  The object reaches an exact
owner-level A0+A1 control but cannot be admitted as classical ASFS.  Future
search should favor an invertible or intrinsically reversible realization of a
comparable prime-factor return law, rather than attaching geometry to this map.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [078 GPF-Fibonacci control](../078-gpf-fibonacci-a0-a1-control/paper.md)
- [080 componentwise-lift boundary](../080-gpf-symplectic-fibre-lift-obstruction/paper.md)
