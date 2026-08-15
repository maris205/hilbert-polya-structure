# Paper 34 source lock — SD-C36

## 1. Candidate and question

The candidate is the class of ordinary positive symbolic recognizer compilers
defined below. The question is whether one member can simultaneously own a
literal atom-only primitive ledger, source-visible recognition, a nonnegative
additive logarithmic clock, the original graph-step marker, and a compact or
trace-class whole one-step operator on its natural vertex Hilbert space.

The answer is a scoped negative theorem. The paper does not assert that every
symbolic dynamical system, weighted zeta function, groupoid, signed complex,
matrix cocycle, or quantum statistical system belongs to this class.

## 2. Phase space and recurrence

Let `G=(V,E)` be one cutoff-independent countable loop-allowed directed graph
with no parallel edges. Its
phase space is the one-sided edge shift

```text
X_G^+ = { e_0 e_1 ... : t(e_j)=o(e_{j+1}) for all j }.
```

A primitive orbit is a nonempty directed closed edge word modulo cyclic
rotation that is not a positive temporal power. Reflection is not identified.
The free marker `z` counts one original graph edge.

For the general theorem, the target atoms form a countably infinite set `A`
with a norm `N:A->(1,infinity)` satisfying multiplicative freeness: every
finitely supported integer relation

```text
product_a N(a)^{m_a} = 1
```

has all `m_a=0`. The prime specialization is `A=P`, `N(p)=p`. For the finite
code estimate, enumerate the atoms by nondecreasing norm and assume
`N(a_j)<=j^kappa` eventually. Rational primes permit `kappa=2`.

## 3. Visible code

Fix a finite alphabet `B`, `b=|B|>=2`, and a finite-radius local code. After
higher-block recoding, it is a one-edge label map `lambda:E->B`. The cyclic
label word of `gamma_a` must separate atoms:

```text
Lambda(gamma_a)=Lambda(gamma_c) implies a=c.
```

If this condition is removed, a countable hidden state name or infinite
alphabet can store an arbitrary inventory. Such objects are mandatory
controls, not counterexamples to the finite-visible theorem.

## 4. Roof and whole operator

The source fixes a nonnegative edge roof `tau:E->[0,infinity)` before any
arithmetic evaluation. The total orbit roof is additive. The literal target
requires exactly one primitive orbit `gamma_a` for each atom, no other
primitive orbit, and

```text
T(gamma_a)=sum_{e in gamma_a} tau(e)=log N(a).
```

For real `sigma>0`, the whole positive weighted vertex adjacency acts on
`H=ell^2(V)` by

```text
L_sigma delta_u = sum_{e:u->v} exp(-sigma tau(e)) delta_v.
```

This is a weighted vertex adjacency, not a Ruelle operator on an unstated
Banach space. If it is unbounded, the whole-operator analytic gate fails. If
bounded, compactness and Schatten membership are tested on this same natural
space. An anisotropic space or induced return space is a different object.

## 5. Recognition edges

A recognition edge exposes a local arithmetic computation or certificate. It
is periodically active when it lies on a directed closed walk, transient when
it lies on none, and shared recurrent when its recurrent strongly connected
component serves more than one atom or contains recurrent computation beyond
one atom cycle.

No outdegree-one assumption is imposed. Ordinary graph branching is counted
with ordinary path multiplicity. Boolean existential, idempotent, or quotient
semantics are not silently identified with the scalar trace of `L_sigma`.

## 6. Frozen theorem

The proof must establish all four conclusions.

1. **Recurrent-core rigidity.** Every atom orbit is a simple cycle, distinct
   atom cycles are vertex-disjoint, and each recurrent SCC is exactly one atom
   cycle. For vertex-disjoint cycles in one SCC, the proof may use arbitrary
   mutual directed paths. It must not assume shortest connectors or that both
   connector interiors avoid the cycles.
2. **Exact pruning.** If the whole adjacency is trace class, deleting all
   edges outside the recurrent core preserves every power trace and the entire
   Fredholm determinant.
3. **Finite-code clock obstruction.** Infinitely many atoms satisfy
   `ell(a)>=log N(a)/(2 kappa log b)`. For primes,
   `ell(p)>=log p/(4 log b)` on an infinite subsequence. Total roof `log p`
   then makes the whole adjacency either unbounded or bounded and noncompact,
   hence outside every finite Schatten class.
4. **Free-marker obstruction.** First return changes the raw factor
   `1-z^{ell(a)}N(a)^{-s}` to `1-zN(a)^{-s}`. Equality after `z=1` gives no
   same-marker credit. Equality as a free-marker germ forces every
   `ell(a)=1`, which conflicts with finite visible separation for infinitely
   many atoms.

## 7. Preregistered hypothesis repair

The exact prototype deliberately tested a stronger connector normal form:
lexicographically shortest mutual connectors whose interiors both avoid the
two cycles. Finite enumeration found counterexamples to that normal form. The
formal theorem never uses it. It uses only mutual reachability in one SCC and
arbitrary attachment paths; the failed strict proxy and the repaired witness
must both remain in the canonical artifact ledger.

## 8. Source and evaluator firewall

The candidate source may enumerate neutral graphs, paths, codes, roofs,
formal weights, and determinants. It may not contain or invoke primality,
factorization, square/Fibonacci membership, a random support table, a target
coefficient, target zero, file-loaded label, or network oracle.

The independent evaluator assigns all arithmetic/control labels only after the
neutral source artifacts are fixed. It must independently reconstruct SCCs,
primitive roots, determinant factors, prefix decoding, clock inequalities,
marker comparisons, and all decisive counts.

## 9. Mandatory controls

- one-way connectors and transient branches;
- cyclic rotations of one primitive orbit;
- private disjoint cycles and countable one-symbol atom loops;
- signed scalar and matrix-valued cancellation toys;
- zero, negative, nonlocal, and hidden/infinite-alphabet roofs or codes;
- prime, square, Fibonacci, modular, hash-selected, matched-cardinality, all,
  empty, and arbitrary inventory controls;
- random strongly connected graphs with frozen deterministic seeds.

Finite enumeration is implementation evidence. Infinite rigidity,
noncompactness, and marker conclusions require independent proofs.

## 10. Allowed and forbidden repairs

Allowed inputs are cutoff-independent symbolic source rules, source-fixed
positive roofs, exact formal calculations, frozen deterministic controls, and
post-source evaluator labels.

Forbidden repairs include a prime or accepted-support table; a terminal
support projector; target values placed directly in hidden states, symbols,
roofs, or loops without source derivation; inducing presented as the original
clock; orthogonal compression presented as an induced quotient; a
cutoff-dependent alphabet; target-zero data; coefficient fitting; and Route B.

## 11. Route lock

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

The result is a negative closure theorem. No xi completion, functional
equation, critical-line divisor, Weil compression, target-zero fit, or RH
implication is claimed.

## 12. Research provenance

- Mathematical package SHA-256:
  `2b9dc8106d3feaea7ed1c4bd377ec98e05baa25ca83bd370ec2fb9eee14952a7`.
- Literature audit SHA-256:
  `e67ab00a518def77c4bdc6ac157736f7f0c4fd7d6e1ee9b92e3f608700a013cc`.
- Canonical experiment hashes are intentionally not embedded in this source
  lock. They are recorded in `EXPERIMENT_REPORT.md`, `results/SHA256SUMS.txt`,
  `results/integrity_audit.json`, and the strict Route-A card after execution.
  This keeps the pre-execution research lock acyclic: `research_lock.json`
  hashes this file, while the downstream result ledger hashes
  `research_lock.json`.
- Two-stage Git provenance is intentionally pending until the first artifact
  commit; the Route card contains the paired pending fields and seal note.

## 13. Paper 35 boundary

Only after this theorem is frozen may an `ax+b`/Bost--Connes-type symbolic
coding be tested as a benchmark. It must name which hypothesis above it leaves,
classify its full connected primitive ledger before weights, derive any
cancellation from the source, own the same uninduced operator and marker, and
pass arbitrary-inventory and generic-action controls. It may not inherit
symbolic or Fredholm credit from a Hamiltonian partition function alone.
