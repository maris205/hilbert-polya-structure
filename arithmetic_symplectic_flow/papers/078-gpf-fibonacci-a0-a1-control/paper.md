<!-- PSR01 CORRECTION NOTICE START -->
> **2026-09-19 superseding correction — ASFS-SCOUT-20260914-53.**
> Current status: **CORRECTED FULL LEDGER — PRIME FIXED POINTS PLUS ONE FOUR-CYCLE**.
> The frozen all-positive map has one fixed point (p,p) per prime, plus the displayed four-cycle. The old arbitrary-positive-seed/unique-cycle claims below are WITHDRAWN. The internal arithmetic rule and noninjectivity result remain; no new geometry or Route credit follows.
> See the [complete correction and proof](../266-prime-source-return-rescreen/paper.md).
> Full carrier, action, roof and same-object identity are preserved;
> formal coordinates UNASSIGNED, Route B NOT INVOKED.
>
> **Historical text retained below; superseded claims must not be used.**
<!-- PSR01 CORRECTION NOTICE END -->

# GPF-Fibonacci supplies one fixed endogenous prime map with a complete prime-only periodic ledger

**Paper ID:** 078-gpf-fibonacci-a0-a1-control  
**Record ID:** ASFS-SCOUT-20260914-53  
**Date / status:** 2026-09-14; OWNER-LEVEL A0+A1 POSITIVE CONTROL / PRE-P0 STOP  
**Route state:** No classical ASFS Route-A coordinate; Route B NOT INVOKED.

## Frozen object

For x,y in N_{>0}, set

\[
G(x,y)=(y,\operatorname{gpf}(x+y)),
\]

where gpf(m) is the greatest prime factor of the integer m >= 2. The second
coordinate is therefore prime after one update. This is a single autonomous
map, not a prime-indexed family.

Back and Caragiu prove that every GPF-Fibonacci sequence, for arbitrary positive
initial values, ultimately enters the unique cycle

\[
7,3,5,2.
\]

In ordered-pair state form its cycle is

\[
(7,3)\mapsto(3,5)\mapsto(5,2)\mapsto(2,7)\mapsto(7,3).
\]

The displayed arrows follow directly from
gpf(10)=5, gpf(8)=2, gpf(7)=7, and gpf(9)=3. They have least period four:
the ordered pairs are distinct. Since every state is eventually captured by this
cycle, no other periodic orbit can exist.

## Same-object A0+A1 control

The arithmetic source and orbit ledger belong to the same exact map G.

| Required feature | Status |
| --- | --- |
| endogenous arithmetic mechanism | established: gpf is evaluated by G at every update |
| prime-symbolic lineage | direct prime-factor observable -> autonomous sequential deformation |
| fixed action | established: G |
| complete periodic ledger | established: one prime-only primitive 4-cycle |
| repetition convention | established: r-fold repetition has iterate length 4r |
| prime-log clock / prime-power rule | absent |
| Hénon/conservative/symplectic owner | absent |
| roof, suspension, determinant | absent |

This is an owner-level positive control, not a formal Route-A pass. The
prior-work Hénon bridge is still missing, and neither the unit iterate count four
nor its repetitions may be relabelled as log p or prime-power data.

## Geometric type boundary

The exact state space is a discrete countable set. The map is also noninjective:

\[
G(1,1)=(1,\operatorname{gpf}(2))=(1,2)
\quad\text{and}\quad
G(3,1)=(1,\operatorname{gpf}(4))=(1,2).
\]

It is therefore not a diffeomorphism of a positive-dimensional smooth manifold
and does not possess an automatic cotangent lift or area-preserving Hénon
realization. A reversible completion or geometric embedding would be a new
object. It must retain the full unique-cycle theorem and internal gpf rule; a
generic reversible simulation would not earn that ownership.

| Gate | Result | Reason |
| --- | --- | --- |
| owner-level A0 | positive control | endogenous greatest-prime-factor rule |
| owner-level A1 | positive control | unique actual prime-only 4-cycle and repetitions |
| classical P0 geometry | STOP | discrete noninjective map; no Hénon/symplectic owner |
| A2 | NOT EVALUATED | no same-object roof/determinant |
| Route B | NOT INVOKED | no classical Route-A-ready candidate |

## Decision

**Portfolio position: advance as the leading source control; fork for geometry.**
078 clears the strongest currently available same-object arithmetic/return test,
but no classical geometry is inherited. Any follow-up must freeze a separately
defined natural carrier or lift and prove it preserves both the exact gpf update
and the complete prime-only orbit ledger before it is called an ASFS candidate.

## Evidence index

- Back and Caragiu, [*The Greatest Prime Factor and Recurrent Sequences*](https://fq.math.ca/Papers1/48-4/Back_Caragiu.pdf)
- Caragiu, Vicol, Zaki, [*On Conway's subprime function, a covering of N and an unexpected appearance of the golden ratio*](https://fq.math.ca/Papers1/55-4/CaragiuVicolZaki03162017.pdf)
- [077 subprime-Fibonacci full-ledger control](../077-subprime-fibonacci-a0-a1-control/paper.md)
- [011 reversible sieve simulation control](../011-reversible-sieve-simulation-control/paper.md)
- [076 direct-lineage breadth frontier](../076-breadth-frontier-cycle-08/paper.md)
