# Bounded nonlinear fifth-seat intake

Date: 2026-09-05 UTC. **CLOSED_WITHOUT_PROMOTION / HOLD_EXTERNAL**.
Three fresh literal maps were tested. None supplies an eligible fifth seat.
This is candidate scouting, not a paper or a manuscript review. Three is a
local intake count; the root must deduplicate the batch-wide denominator.

## Dispositions

| Literal | Exact finite boxes | Disposition |
|---|---|---|
| UPR: uniquely represented unordered pair sums in subsets of F_2^d | All subsets for d=1,2,3,4; seeded samples d=5,6,7 | KILL_NO_PARAMETER_SPINE; the apparent fixed-only recurrence is false at d=6 |
| MCR: (x,y) -> (x(1-y),y(1-x)) on F_p^2 | All states for p=2,3,5,7,11,13,17,19 | KILL_QUADRATIC_FAMILY_BUNDLE; exact invariant-fibre quadratic conjugacy |
| CPA: canonical polynomial advection f -> f f' mod(X^p-X) | All canonical coefficient vectors for p=2,3,5 | KILL_NO_ALL_PRIME_CONTRACT; no full temporal theorem or target inverse closed |

CPA is the canonical polynomial advection candidate, also referred to as
CAD in coordination messages; these names denote one literal, not two.
Negative disposition for UPR/CPA means the bounded search did not close
the required theorem, not that useful mathematics is impossible.

## UPR: counterexample and remaining boundary

For S subset F_2^d define T(S) to contain z precisely when exactly one
unordered distinct pair in S has XOR sum z. Integer masks use bit a for
the vector with binary index a; zero is never output.

The d<=4 boxes have only fixed eventual periods. Their fixed counts are
1,2,8,36, consistent with empty plus two-dimensional subspaces minus zero.
That observation was NOT proved for all dimensions, and does not justify
a global recurrence classification.

At d=6, the two distinct masks

```
A=11253440500314867716
B=11533932229067682872
```

each have size17 and satisfy T(A)=B, T(B)=A. A separate ordinary
pair-Counter implementation certifies both equalities in probe_fifth.py.
Thus even the weaker fixed-only recurrence conjecture is false.
The deterministic d=6 stress encounter starts at 3178559749042078984 and
enters this cycle after one step. A d=7 two-cycle also appears; its data
are in CANONICAL.txt. No claim that these are all recurrent types is made.

Closed elementary facts are translation invariance T(S+a)=T(S), the
fixed triangle from any three-point input, and T(S)=empty whenever
|S|>=2^(d-1)+2 (each nonzero-direction matching then has at least two
fully occupied pairs). These facts and small boxes do not give a
full target-resolved inverse or all-d temporal spine.

## MCR: exact decomposition, no separated dynamics

Write d=x-y, which is invariant. In coordinates (d,x), the map is

```
(d,x) -> (d, x(1+d-x)).
```

For odd p, put a=1+d and z=a/2-x. The resulting map is

```
(d,z) -> (d, z^2+(1-d^2)/4).
```

This is an exact bijective coordinate change, not an approximation:
the entire carrier is a disjoint bundle of standard scalar quadratic
functional graphs. For target (u,v), d=u-v, every predecessor is exactly

```
(x,x-d), where x^2-(1+d)x+u=0.
```

For odd p its fibre count is 1+chi((1+d)^2-4u), with chi(0)=0.
Hence the image size is p(p+1)/2, the maximal fibre is two, and
the fixed locus xy=0 has size2p-1. Characteristic2 is checked directly
on four states. These inverse facts are ordinary quadratic algebra;
the proposed two-variable packaging provides no independent temporal
residual. The verifier checks the invariant, conjugacy, and exact inverse
sets in every stated prime box.

## CPA: literal definition matters

A state is the unique polynomial f of degree<p representing a function
F_p->F_p. Different representatives must NOT be differentiated freely:
formal differentiation is not well-defined on the quotient by X^p-X.
The literal differentiates the canonical representative, multiplies by f,
then reduces modulo X^p-X.

The affine stratum f=a+bX obeys (a,b)->(ab,b^2), an ordinary powering
cocycle. On the full carrier, p=5 already has period4 and maximum tail6,
where p=2,3 have only period1. This is finite evidence, not a disproof of
an all-prime theorem. No adequate full-carrier clock, complete recurrence
classification, or target-resolved inverse was established in the bounded
intake. Therefore it is not promoted.

## Intake exclusions: zero new tested rows

- Subset doubling is exact P97, not a fresh candidate.
- Tangent/secant threshold variations sit beside the archived XSD exact
  two-secant geometry transform, killed without an all-parameter spine:
  docs/papers162_166_sequence/scouting/open_fresh_p166_round6/IDEA_LEDGER.md
  and OWNER_SEARCH_LOG.md. No threshold variant is promoted.
- Fibre-size feedback is archived same-size coagulation:
  docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md (near line624),
  docs/papers112_116_sequence/scouting/COMBINATORIAL_SCOUT.md (C5),
  docs/papers187_191_sequence/phase1/HISTORICAL_COLLISION_AUDIT.md (C04PME).
- Cofactor/diagonal feedback was withheld against the occupied determinant
  and adjugate surface: docs/papers187_191_sequence/scouting/algebra_lane/
  CANDIDATES.md (A08) and KILL_LEDGER.md, including P175.
- Archived NL14/BSP, T(x,y)=(xy,x(1-y)), is not silently renamed as MCR:
  docs/papers162_166_sequence/scouting/replacement_nonlinear_algebra/SCOUT.md.
- Polynomial derivative-gcd has an older PDG owner record:
  docs/papers152_156_sequence/scouting/algebraic/SCOUT.md and
  OWNER_SEARCH_LOG.md. CPA is a different literal but is still unclosed.
- Matrix powers/Frobenius linearization, AA^T A, mutual conjugation, cyclic
  code shortening, Frattini/centralizer maps, and canonical closures were
  excluded at intake under the parent task's binding kill list.

## Bounded primary-source search

Queries executed included:
"uniquely represented" sums elementary abelian 2 group;
"unique representation" "sumset" iteration;
finite fields quadratic polynomial functional graphs x squared c;
"polynomial" "f f'" "finite fields" dynamics;
Sidon sets elementary abelian 2 groups uniquely represented sums arxiv;
"f f'" "mod" "polynomial" dynamics finite.

Primary metadata/abstract pages were actually opened on 2026-09-05:
- Konyagin, Luca, Mans, Mathieson, Sha and Shparlinski, *Functional Graphs
  of Polynomials over Finite Fields*, arXiv1307.2718v3 (2015):
  https://arxiv.org/abs/1307.2718v3 .
  It studies polynomial functional graphs, with explicit quadratic focus.
  This is quadratic-family background, not a claim that it introduces MCR.
- Nagy, *Thin Sidon sets and the nonlinearity of vectorial Boolean
  functions*, arXiv2212.05887v2 (2022):
  https://arxiv.org/abs/2212.05887v2 .
  Its abstract identifies a survey of Sidon sets in elementary abelian
  2-groups. This is additive-representation background, not an exact UPR
  iteration owner.

Only these metadata/abstract read scopes are claimed; no full-text theorem
transfer is inferred from them. No exact CPA owner was located in the
bounded queries. Search misses establish neither novelty nor priority.
The MCR kill rests on the displayed exact algebraic conjugacy, not on a
search miss or an unsupported bibliographic ownership assertion.

## Evidence and next action

The probe contains census, targeted algebra checks, seeded stress, and a
separate UPR counterexample implementation. Exact boxes, samples, and
deductions remain separately labelled. No assertion total is invented.
Two fresh matching runs are recorded in REPLAY_RECEIPT.md.
The parent requested transition to the independently authored period-
feedback Stage1 gate; this closed intake does not fill that candidate's seat.

