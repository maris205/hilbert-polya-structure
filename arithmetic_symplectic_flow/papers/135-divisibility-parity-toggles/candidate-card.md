# Scope card — ASFS-SCOUT-20260914-98

**Version:** 1, 2026-09-14; frozen before audit.  
**Initial status:** PRE-P0 HYPOTHESIS — OPEN.

Let P=N_{>=2} ordered by divisibility, J(P) all downsets with the inherited
product topology in {0,1}^P. Define rank(n) as the maximum number of ELEMENTS
of a strict divisibility chain in P ending at n (a one-element chain has rank
1). This convention is clarified before the mathematical audit, and differs
by one from edge-count rank. No prime list is a defining input.

Toggle t_n changes membership of n exactly if the changed set is still a
downset, and otherwise does nothing. Let T_odd and T_even toggle
simultaneously all vertices of odd or even rank, respectively. The new action
is F=T_even composed with T_odd. Each eligibility test in a half-step uses
that half-step's input downset. Well-definedness and involutivity are OPEN
before audit; do not import finite-poset theorems without proof.

| Field | Frozen specification |
| --- | --- |
| Lineage | prime/composite divisibility admissibility -> state-dependent local toggles -> two-color autonomous coupled update |
| New object | J(P), product topology, and exactly F; not rowmotion R from 132 |
| Arithmetic mechanism | intrinsic minimal-element/source support and rank changes; proposed prime interpretation OPEN |
| Diagnostic seed | empty downset; no output bound or prime data |
| Periodic convention | full states with least positive F-period, cyclic phase quotient |
| Controls | half-step inverses; infinite upper-neighbor continuity; rank-initial ideals; finite-poset comparison |
| Roof / flow / analytic owner | NOT SUPPLIED |
| Classical geometry | NOT APPLICABLE at symbolic screen |
| Budget / stop | well-definedness, arithmetic seed, inverse/topology, first decisive return obstruction; no full orbit classification after failure |
| Route | A0/A1/A2 UNASSIGNED; Route B NOT INVOKED |

Any topology change, bounded poset, different toggle order or selected recurrent
core requires a new card.

## Audit outcome — same version-1 object

**Status:** `PRE-P0 STOP — PRODUCT-TOPOLOGY DISCONTINUITY; EMPTY-SEED RANK ESCAPE`  
**Portfolio position:** `fork`.

The [paper](paper.md) proves both half-steps are well-defined involutions and
the full action is bijective. Its coordinate at 2 gives an exact failure of
continuity under downarrow(2q_j) -> {2}; the inverse has an analogous
coordinate-4 failure. The first half-step of the empty state is the prime
support, whereas complete F-steps produce I_{2t}={rank<=2t}, an infinite
nonreturning source orbit. The full ideal is a fixed point; other periodic
states remain unclassified. No topology, carrier, schedule, roof, or owner
has been replaced.

A0/A1/A2 remain `UNASSIGNED`; formal Route coordinates `NOT EVALUATED`;
Route B `NOT INVOKED`. See the [claim ledger](claim-ledger.md) and
[evidence record](evidence/README.md).
