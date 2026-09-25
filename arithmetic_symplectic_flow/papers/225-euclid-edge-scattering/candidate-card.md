# Candidate card — Euclid edge scattering

**Candidate ID:** ASFS-20260918-EES01  
**Paper ID:** 225-euclid-edge-scattering  
**Version:** 1; frozen 2026-09-18 before the mathematical audit.  
**Initial status:** FROZEN HYPOTHESIS — FULL PERIODIC LEDGER AND NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## 1. Integer-word graph and exact port convention

Let W be all nonempty finite ordered words w=(a_1,...,a_k) with integer
entries a_i>=2. Include every such word, with no product cutoff, prime table,
or prime-only restriction. Form a simple undirected graph G on W. Distinct
words are adjacent precisely when one local move below, in either direction,
changes one word into the other:

1. Split/merge: replace an entry ab by the consecutive entries (a,b),
   where a,b>=2, or reverse this replacement.
2. Left Euclid shear: replace consecutive entries (a,b) by (a+b,b).
3. Right Euclid shear: replace consecutive entries (a,b) by (a,a+b).

An inverse subtraction is allowed only when all resulting entries are >=2.
Coincident generator edges are collapsed into one simple edge. There are no
ordinary self-loops in G. Write N(w) for its complete neighbor set and
I={w:N(w) is empty}. This definition of I, not a supplied prime predicate,
selects the terminal vertices.

For each nonempty N(w), use shortlex order (word length first, then ordinary
lexicographic integer order) and let c_w be its cyclic successor, including
wraparound. The nonterminal state set is

    E = {(u,v): v in N(u)}.

Adjoin exactly one stationary port l_w for each w in I. The full discrete
symbol set is X=E disjoint-union {l_w:w in I}. Freeze

    sigma(u,v) = (v,c_v(u)),       sigma(l_w)=l_w.

This is an explicit generalized port completion: reversal exchanges (u,v)
and (v,u), but fixes l_w. A stationary port is NOT an ordinary undirected
self-loop with two distinct darts. A two-dart loop is a different control
and must retain both states; neither orientation nor multiplicity may be
silently quotiented. The topology of W, E, X is discrete.

## 2. Full geometric owner and clock

Freeze the countable disjoint union

    M = disjoint-union over x in X of R^2_x,
    omega on every component = dq wedge dp.

Every real point in every component is retained. With

    B(q,p) = (q+p+1,p+1),
    A(q,p) = (2q+p,q+p),

the proposed smooth map is

    F(e,q,p) = (sigma(e),B(q,p))         for e in E,
    F(l_w,q,p) = (l_w,A(q,p))           for w in I.

The fixed parameters are exactly the displayed matrices, unit drift and
shortlex order. Symplecticity, bijectivity and the full periodic set are
proof obligations. The measure is componentwise Lebesgue symplectic area;
no finite invariant probability is supplied.

The roof is exactly tau=1 on the whole M. Define the suspension by

    M_1 = (M x [0,1])/((z,1) equivalent to (F(z),0)),

with translation flow. This is an odd-dimensional mapping torus, not a
claimed Hamiltonian flow. A logarithmic roof, scale quotient, or label-dependent
clock is NOT part of version 1. Non-Zeno and completeness must be checked
from the proposed global inverse and unit roof.

## 3. Arithmetic lineage and ownership obligations

The proposed lineage is prime/composite factor-witness exclusion -> finite
factorization-word admissibility -> reversible Euclid deformation ->
positive-dimensional conservative port lift. A singleton is tested by its
available factorization moves, not by a stored primality bit. Euclid moves
may change the product of a word, so the graph is not defined as a union of
fixed-product factorization graphs. Whether this actually generates prime
packets rather than merely placing terminal components remains an explicit
naturalness question.

The finite-dimensional conservative arrow is a new componentwise symplectic
construction; no conjugacy to the prior Logistic or Hénon map, no faithful
chronological sieve semiconjugacy, and no natural Markov partition is assumed.
The component projection M->X is the proposed symbolic factor of this exact
F. Its entire geometric fibre must be audited, not only selected centres.

Permitted inputs are integers, addition, multiplication, division tests, word
order and the fixed geometric constants. Prime tables, Riemann-zero data,
von Mangoldt weights and per-prime tuning are prohibited. Terminal stationary
ports and the choice to apply A there instead of B are declared engineering
choices; their arithmetic necessity is not assumed.

## 4. Periodic and analytic contract

Primitivity means least positive period under F; cyclic phases are identified
only along that orbit. A suspension primitive is the corresponding oriented
flow circle; repetitions traverse that same circle r times. Distinct ports,
word labels, or geometric periodic points are not identified merely because
their periods agree. The audit must classify all real periodic points and
report monodromy and any extra multiplicity.

The only analytic proposal is the ordinary unweighted full primitive product

    Z(s) = product over primitive gamma of (1-exp(-s T_gamma))^(-1)

if its full repetition logarithm has a convergence domain. No weights,
regularization, operator, function space or Fredholm determinant are supplied.
Operator/trace owners remain OPEN; Hamiltonian/contact/quantum owners are
DEFERRED. No analytic object from another candidate may be substituted.

## 5. Precommitted discriminators and stop conditions

1. Prove or refute local finiteness and the exact inverse of sigma; audit
   ordinary versus stationary-loop multiplicity explicitly.
2. Check global invertibility and symplecticity of F on the full manifold.
3. Test nonterminal momentum drift and all powers of A, not just fixed points.
4. Test prime singletons, composite singletons and nonsingleton words;
   classify the full closed-orbit ledger before any analytic claim.
5. Compare arbitrary local cyclic orders, deleting the terminal completion,
   ordinary two-dart completion, all-B geometry, and a nonarithmetic graph
   with prescribed isolated vertices. These are distinct controls, not edits
   to version 1 or transferable candidate credit.
6. Inspect the actual unit clock and full unweighted repetition series. Stop
   deep development if natural A0 or useful same-object arithmetic time is
   missing; an engineered prime-only packet set alone is not a pass.

An undefined port ordering, loop convention or inverse causes a scoped P0
stop. A changed graph, completion, drift, hyperbolic map, carrier, roof or
analytic weight requires a fresh ID. Work here is exact proof plus lightweight
document verification; no GPU job, parameter sweep or numerical census is
part of this card. No descendant author is assigned by this subtask.

## Related frozen controls

- [136 factorization path owner](../136-factorization-nonbacktracking-flow/candidate-card.md)
- [217 divisor-port return owner](../217-divisor-scattering-return/candidate-card.md)
- [145 convex witness Hénon owner](../145-convex-witness-henon-sieve/candidate-card.md)
- [Prior-work lineage](../../docs/prior_work/README.md)

These links document differences and ancestry only. No theorem, gate score,
source lock or authorization is inherited.

## Appended outcome — version-1 inputs unchanged

**Status:** STOP — ENGINEERED PRIME FIXED PACKETS; UNIT CLOCK COLLAPSE.

The [paper](paper.md) proves local finiteness, exact port bijectivity and a
global two-dimensional symplectic owner. Its full periodic set is exactly
one hyperbolic fixed origin per prime singleton: B's momentum grows by 1
at every nonterminal step, while A has no nonzero periodic real point.
The same unit suspension has primitive lengths 1 and repeat lengths r.
Its full ordinary unweighted repetition logarithm has no absolute-convergence
half-plane because infinitely many primitives have length 1.

The arithmetic terminal criterion is derived, but the stationary-port
completion and A-versus-B geometric choice are engineered. Ordinary two-dart
loops give two prime packets; arbitrary isolated-state graphs admit the
same selection construction. Natural A0 is therefore NOT ESTABLISHED;
prime-log clock relevance fails for this frozen roof. Retain the exact
geometric result as a control and stop / fork. Formal Route coordinates
remain UNASSIGNED; Route B NOT INVOKED.
