# Derivation package — Paper 34 / SD-C36

## 1. Target and status

The target is not a new arithmetic zeta construction. It is a classification
of how a positive symbolic recognizer can, or cannot, become recurrent while
retaining a literal atom ledger, the original graph clock, and ordinary
Fredholm ownership.

```text
derivation_status: coherent after strict scoping
positive_candidate_status: rejected
target_zero_data: forbidden and unused
route_b: locked
```

## 2. Frozen input

Let `G=(V,E)` be a countable loop-allowed directed graph with no parallel
edges, `lambda:E->B` a finite
visible alphabet, and `tau:E->[0,infinity)` a source-fixed roof. Let `A` be a
countable atom set with multiplicatively free norms `N(a)>1`. The literal
ledger asserts that the primitive directed orbits are exactly
`{gamma_a:a in A}` and

```text
T(gamma_a)=sum_{e in gamma_a} tau(e)=log N(a).
```

For real `sigma>0`, the whole vertex adjacency is

```text
L_sigma delta_u = sum_{e:u->v} exp(-sigma tau(e)) delta_v.
```

The free variable `z` counts one original graph edge.

## 3. Derivation map

```text
literal atomic primitive ledger
        |
        +-- shared vertex or shared recurrent SCC
        |       -> concatenate closed words inside one SCC
        |       -> take the unique primitive word root
        |       -> multiplicative-freeness contradiction
        |       -> recurrent SCCs are private simple atom cycles
        |
        +-- recognition edges outside those SCCs
        |       -> no closed walk contains them
        |       -> every diagonal power coefficient is unchanged
        |       -> all power traces and Fredholm determinant prune exactly
        |
        +-- finite visible orbit separation
        |       -> at most sum_{r<=L} b^r visible words of length <=L
        |       -> infinitely many ell(a) >= log N(a)/(2 kappa log b)
        |       -> one edge per private cycle has bounded roof
        |       -> weak-null basis vectors have images bounded away from zero
        |       -> whole adjacency is noncompact whenever bounded
        |
        +-- first return on one vertex per cycle
                -> diagonal weight N(a)^(-s)
                -> raw factor 1-z^{ell(a)}N(a)^(-s)
                -> induced factor 1-zN(a)^(-s)
                -> equality only after forgetting the raw clock at z=1
```

## 4. Word-root step

Every nonempty finite word `W` has a unique primitive root `w` and an integer
`m>=1` such that `W=w^m`. The words `W` and `w` have exactly the same edge
support. This support fact removes the overstrong connector normal form from
the preregistration: mutual reachability in one SCC suffices. Shortest paths
and connector interiors avoiding both cycles are unnecessary.

If distinct atom cycles meet at a vertex, rotate them to based words `x,y`.
Writing `xy=w^m` and using the literal ledger gives

```text
N(a) N(c) = N(d)^m,
```

which violates multiplicative freeness. If a cycle repeats a vertex, split it
into two closed subwords and obtain the same contradiction. If two disjoint
atom cycles lie in one SCC, arbitrary mutual paths yield a closed word whose
primitive root contains edges from both cycles, contradicting pairwise
disjointness.

## 5. Trace and determinant step

After recurrent rigidity, every closed walk lies on one private atom cycle.
Let `C_sigma` retain only the cycle edges. If `L_sigma` is trace class, then
the diagonal conditional expectation applied after the cycle-successor
permutation proves `C_sigma` is trace class. For every `r>=1`, based closed
walk enumeration gives

```text
Tr L_sigma^r = Tr C_sigma^r.
```

The trace logarithm gives equality near `z=0`; entireness in `z` extends it:

```text
det(I-zL_sigma)
  = det(I-zC_sigma)
  = product_a (1-z^{ell(a)} N(a)^(-sigma)).
```

The computation outside the recurrent core is therefore not merely small; it
is absent from every connected trace coefficient.

## 6. Coding and compactness step

Write the atoms as `a_1,a_2,...` in nondecreasing norm and assume
`N(a_j)<=j^kappa` eventually. If the cyclic visible labels separate atoms,
then among the first `J` atoms the maximum cycle length `M_J` satisfies

```text
J < sum_{r=1}^{M_J} b^r,
```

so record lengths obey `M_J>=log J/(2 log b)` eventually. On an infinite
record subsequence,

```text
ell(a)>=log N(a)/(2 kappa log b).
```

Some edge on each such cycle has roof at most `2 kappa log b`, hence weight at
least `b^{-2 kappa sigma}`. The source vertices lie on distinct cycles, so
their standard basis vectors form a weakly-null orthonormal sequence whose
images do not converge to zero. A bounded `L_sigma` is not compact and belongs
to no finite Schatten class.

For rational primes, the elementary eventual estimate `p_j<=j^2` permits
`kappa=2` and the stated constant `1/(4 log b)`.

## 7. Marker step

First return multiplies the edge weights around `gamma_a` and gives
`N(a)^(-s)`. On its induced diagonal space, the operator is trace class when
`sum_a N(a)^(-Re(s))` converges. Its determinant is honest for that induced
object, but one induced step equals `ell(a)` original steps. Therefore

```text
raw:      1-z^{ell(a)}N(a)^(-s),
induced:  1-zN(a)^(-s).
```

Comparing the coefficient of `z` in an absolutely convergent positive germ
shows that a raw determinant equal to the induced atom product forces
`ell(a)=1` for every atom. A finite alphabet has only finitely many one-letter
cyclic words, so infinite visible atom separation fails.

## 8. Sharp boundaries

- A one-way connector is transient and does not create a mixed orbit.
- Private cycles can realize any supplied countable inventory.
- An infinite visible alphabet evades the coding bound.
- Signed or matrix coefficients may cancel mixed trace contributions even
  though the primitive words still exist.
- Boolean, idempotent, or existential acceptance is not ordinary scalar path
  summation.
- An anisotropic operator space, nonlocal action, groupoid trace, or quantum
  partition function is a different ownership problem.

These are theorem boundaries, not omitted positive results.

## 9. Route consequence

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

The formal countable atom diagonal can receive conditional Euler-product
credit under a weaker A1 convention, but it is an arbitrary inventory and
does not alter the route decision.
