# ECPP has finite elliptic-group control but no same-object prime-symbolic suspension candidate

**Paper ID:** 072-ecpp-finite-group-lineage-screen  
**Record ID:** ASFS-SCOUT-20260914-49  
**Date / status:** 2026-09-14; EXTERNAL CONTROL / PRE-P0 STOP  
**Route state:** No ASFS Route-A coordinate; Route B NOT INVOKED.

## Why screen ECPP

ECPP is a substantially more geometric arithmetic construction than a generic
prime-labelled map. For each supplied target n_i it chooses elliptic-curve and
point data and verifies an order criterion conditional on a prime q_i. Fixed
elliptic groups have finite cyclic subgroups, so this is an appropriate control
for the temptation to treat local group cycles as the desired primitive closed
orbits.

It does not pass the lineage gate. The construction starts with a target integer
to certify, rather than an action derived from the prior Eratosthenes
prime/composite symbolic observable; its curve and point data are selected for
the target. No sequential Logistic-type deformation or Hénon/conservative lift
is supplied.

## Exact screened chain and ownership

The documented ECPP step has data

\[
(n_i,a_i,b_i,m_i,q_i,P_i),
\]

where the point and group-order conditions show n_i is prime provided q_i is
prime. The next certificate target is q_i. The implementation documentation
states the required range

\[
(n_i^{1/4}+1)^2 < q_i \leq n_i/2,
\]

and sets n_(i+1)=q_i.

| Required owner | Available object | Audit |
| --- | --- | --- |
| arithmetic recognition | certificate verification for a supplied target | internally coherent as a proof protocol |
| local periodic algebra | point operations in one selected finite group | retained only as local control |
| global action | target-dependent chain of changing curves/groups | no fixed self-map |
| closed-orbit/repetition convention | none across the changing chain | ownership FAIL |
| symplectic base, roof, suspension | none specified | NOT SUPPLIED |
| transfer operator/determinant | none on the certificate chain | NOT APPLICABLE |

No group, orbit, roof, or analytic owner from another package is transferred into
this record.

## Two decisive boundaries

First, the full chain is target-driven: choosing n_0 and then curve/order/point
data is a proof search/verification protocol, not an endogenous sieve-symbolic
selection. A finite group cycle after all these inputs are frozen only preserves
that already selected local datum.

Second, the certificate direction is strictly descending. Since q_i <= n_i/2,
the global certificate state cannot return after any positive number of steps.
That conclusion concerns the exact certificate chain, not arbitrary dynamics on
an elliptic curve. Reversing or identifying steps would alter the source object
and require a new frozen card.

| Gate | Result | Reason |
| --- | --- | --- |
| prime-symbolic lineage | scoped FAIL | no action-level sieve/Logistic/Hénon bridge |
| A0 | NOT EVALUATED | no same-object symplectic candidate proposed |
| A1 pre-screen | NOT TESTABLE; certificate chain nonreturning | finite local cycles do not own global chain |
| A2 | NOT EVALUATED | no same-object determinant/trace owner |
| Route B | NOT INVOKED | Route A is not ready |

## Decision

**Portfolio position: stop/fork.** ECPP remains a positive external control for
local arithmetic group structure, not a main ASFS candidate. A later proposal
must first exhibit a fixed, lineage-derived action that itself selects the
arithmetic data and retains nontrivial returns; merely holding one ECPP curve
fixed or attaching an external roof would fail the one-object invariant.

## Evidence index

- FLINT documentation, [ECPP certificate-chain description](https://flintlib.org/doc/ecpp.html)
- [071 Pratt-tree return screen](../071-pratt-tree-return-screen/paper.md)
- [061 Bost--Connes lineage boundary](../061-bost-connes-lineage-boundary/paper.md)
- [069 breadth trilemma frontier](../069-breadth-frontier-cycle-07/paper.md)
