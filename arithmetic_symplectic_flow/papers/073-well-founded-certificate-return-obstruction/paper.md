# Well-founded arithmetic certification cannot itself supply a primitive-return ledger

**Paper ID:** 073-well-founded-certificate-return-obstruction  
**Record ID:** ASFS-METHOD-20260914-10  
**Date / status:** 2026-09-14; METHOD THEOREM / PRE-P0 STOP RULE  
**Route state:** No ASFS Route-A coordinate; Route B NOT INVOKED.

## Purpose

The breadth search has encountered two structurally different prime-certificate
objects: Pratt's factor tree and ECPP's elliptic-curve certificate chain. Both
retain genuine arithmetic content, and ECPP additionally has finite local group
cycles. Neither directly provides the required recurrent same-object carrier.
This record states the exact common condition, so future certification variants
can be stopped or admitted before prolonged A0/A1 work.

## The complete-state descent theorem

Let X be the set of *complete* arithmetic states: a state contains every target,
certificate, witness, curve, module, or other datum whose update is being claimed
as the endogenous arithmetic mechanism. Let R be a directed transition relation
on X. Suppose there is a map

\[
\rho:X\longrightarrow W
\]

to a well-founded strict order W such that

\[
x\mathrel{R}y \quad\Longrightarrow\quad \rho(y)<\rho(x).
\]

**Theorem.** The relation R has no directed cycle of positive length.

**Proof.** A cycle x_0 R x_1 R ... R x_(r-1) R x_0 would give
rho(x_0) > rho(x_1) > ... > rho(x_(r-1)) > rho(x_0), impossible in a
strict order. ∎

The point of recording the *complete* state is essential. If one omits the
progressing target or certificate data, one may display a periodic local
operation while no longer owning the asserted arithmetic transition. Such a
projection is a different object and cannot supply its predecessor's A1 credit.

## Applications and controls

| Screened object | Rank | Why the theorem applies | What remains only local |
| --- | --- | --- | --- |
| 071 Pratt certificate | prime node label p | each required child q of p - 1 satisfies q < p | no self-map/fibre cycle is supplied |
| 072 ECPP chain | target n_i | documented next target q_i <= n_i/2 | point operations after curve/group data are fixed |

This is not the same rule as the advancing-frontier and deletion-only rules in
018 or 063. Its rank decreases rather than increases, and it therefore applies
to certification/reduction trees. It also does not assert that a reversible
extension cannot exist: a proposed extension must freeze its own state, action,
lineage link, and full orbit ledger as a new candidate.

## A0--A2 boundary

| Coordinate | Result |
| --- | --- |
| lineage | method derived from prime-recursive controls; it does not establish the required full prior-work deformation |
| A0 | NOT EVALUATED — no symplectic candidate is defined |
| A1 | screening obstruction only for a complete state satisfying the descent hypothesis |
| A2 | NOT EVALUATED — no same-object zeta/determinant is provided |
| Route B | NOT INVOKED |

## Decision

**Portfolio position: fork.** Stop screening certificate chains whose exact
global transition is strictly ranked. The next search should target a genuinely
non-well-founded, autonomous prime-symbolic mechanism with nontrivial return,
not a local cycle over externally frozen certificate data.

## Evidence index

- [071 Pratt-tree return screen](../071-pratt-tree-return-screen/paper.md)
- [072 ECPP finite-group lineage screen](../072-ecpp-finite-group-lineage-screen/paper.md)
- [018 monotone sieve-clock obstruction](../018-monotone-sieve-clock-obstruction/paper.md)
- [063 monotone-elimination periodic-rigidity rule](../063-monotone-elimination-periodic-rigidity/paper.md)
