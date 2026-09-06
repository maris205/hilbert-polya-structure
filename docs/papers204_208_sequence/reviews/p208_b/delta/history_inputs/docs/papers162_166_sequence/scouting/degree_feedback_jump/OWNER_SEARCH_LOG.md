# DFJ bounded owner and internal-collision audit

Date: 2026-09-03  
Status: **KILL / HOLD_EXTERNAL / no novelty claim**

## Search scope

The bounded search used literal and mechanism variants of:

- indegree-dependent pointer jump on a functional digraph;
- `f^(1+indegree)` endofunction iteration;
- powers and square roots in finite full transformation semigroups;
- functional graphs of permutation and group power maps;
- square-root fibres by permutation cycle type;
- 2025--2026 endofunction and transformation-semigroup dynamics.

No inspected record stated the exact literal DFJ rule.  This non-hit has no
positive novelty or priority weight because the candidate's strongest
invariant classes reduce exactly to directly owned power/root problems.

## Primary owner subtraction

### Power maps on symmetric groups

Matt Larson, [*Power maps in finite groups*](https://arxiv.org/abs/1707.06696),
studies the functional graphs and cycle counts of `x -> x^a`, explicitly
including symmetric groups.  DFJ restricted to permutations is precisely the
case `a=2`; its uniformly leaf-decorated classes realize every fixed exponent
`a>=2`.  All preperiod/period statements obtained from multiplicative orders
receive zero credit.

### Permutation-root fibres

Leaños, Moreno, and Rivera-Martínez,
[*On the number of mth roots of permutations*](https://arxiv.org/abs/1005.1531),
give explicit expressions and generating functions for the number of roots
of a permutation of arbitrary cycle type, while recording earlier solution
and classification results.  DFJ's entire fibre over every permutation target
is exactly the `m=2` specialization.

### Full-transformation roots and powers

Peter M. Higgins,
[*A Method for Constructing Square Roots in Finite Full Transformation
Semigroups*](https://doi.org/10.4153/CMB-1986-053-2), constructs all square
roots of an arbitrary element of the full transformation semigroup using its
directed functional graph.  This directly owns the wider carrier/root
neighbourhood, even though a general DFJ predecessor is not a semigroup
square root.

Zeng, Cheng, Yang, and Shao,
[*Power graphs of full transformation semigroups*](https://doi.org/10.2298/FIL2508725Z),
characterize connected components of the power graph of the full
transformation semigroup.  This is direct current evidence that the generic
power structure of this carrier is active, not unoccupied background.

Pointer jumping is broad algorithmic vocabulary and is not used as a direct
owner claim.  The exact owner subtraction rests on the displayed conjugacies,
not on shared terminology.

## Internal collision audit

- **Prior `FSQ` scout:** the P162--P166 cross-class lane already exact-tested
  `f -> f^2` on the full transformation semigroup, derived its height/order
  phase portrait, and permanently killed it as generic power-map theory.
  DFJ contains this map exactly on the whole permutation slice and contains
  all fixed power maps on uniform-leaf lifts.
- **P105:** P105's identity indegree is already the involution sequence
  `1,2,4,10,26,76,232,...`.  DFJ reproduces the same result literally because
  `T(f)=id` forces `f` to be a permutation and then says `f^2=id`.
- **P114:** owns sharp rooted-forest height dynamics, bounded-depth labelled
  EGFs, and local fibres.  DFJ's fixed height-two species lies in this occupied
  rooted-functional-digraph enumerative neighbourhood, while lacking P114's
  global clock and target fibres.
- **P115:** owns complete functional components, attached rooted trees,
  local indegrees, image/fibre data, and cycle counts after a structural
  conjugacy.  Generic component classification or attached-tree machinery
  cannot be counted as a new DFJ axis.
- **Other P162--P166 adaptive/endofunction scouts:** endofunction conjugations,
  rank summaries, and fixed-action lanes were already killed when their
  dynamics reduced to a relabelling or fixed semigroup action.  DFJ is
  nonlinear off its invariant slices, but the only closed temporal spine is
  again an action already removed by that firewall.

## Residue after subtraction

The exact literal residue is the fixed-point criterion and its residue-class
EGF.  It is mathematically clean, but it is one static theorem.  The target
fibres that admit a closed formula are precisely the owned permutation-root
fibres; non-permutation fibres depend on finer rooted attachment shape, and
the exhaustive phase portraits do not suggest a sharp global clock or cycle
census.

**Decision: KILL_POWER_MAP_CORE_AND_NO_SECOND_AXIS.**  Preserve only as a
negative control under `HOLD_EXTERNAL`; do not assign a paper number or make
a novelty claim.
