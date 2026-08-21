# Stage-2 theorem contract: complete cyclic blocks with transient phase allocation

## Proof-status vocabulary

Only the following status labels are used.

- `PROVABLE AS STATED`: a complete proof is included in `PROOF_PACKAGE.md`.
- `PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION`: the displayed extra
  hypothesis is part of the theorem, not an informal proviso.
- `NOT CURRENTLY JUSTIFIED`: excluded from the proved package.

No numerical check upgrades a proof status.

## Frozen object and notation

Fix integers `d>=2`, `p>=1`, and positive integers
`a=(a_0,...,a_{p-1})`.  Let `V_0,...,V_{p-1}` be disjoint phase alphabets
with `|V_j|=a_j`.  The complete cyclic incidence block `C(a)` has all and
only the edges

```text
V_j -> V_(j+1 mod p),
```

and every such bipartite phase-to-phase edge is present.  Labels are placed
on the rooted ordered `d`-ary tree.  Put

```text
c_j = log(a_j),
Delta_n = union of levels 0,...,n,
|Delta_n| = (d^(n+1)-1)/(d-1).
```

The metric is

```text
D(x,y) = exp(-sup{|Delta_n| : x and y agree on Delta_n}).
```

All logarithms are natural.  Indices on phase vectors are in `Z/pZ`.  Define

```text
H_j(c) = (d-1)/(d^p-1)
         * sum_(t=0)^(p-1) d^(p-1-t) c_(j-t).

bar(c) = (1/p) * sum_j c_j.
```

For a weak composition `m=(m_0,...,m_{p-1})` of `d`, define

```text
b_k(m) = (1/d) * sum_s m_s c_(s+k),
D_1(m;c) = min_j H_j(b(m))
         = min_j (1/d) * sum_s m_s H_(s+j)(c).
```

The one-level feeder matrix adds one state `r`, puts edges from `r` to every
state of every `V_j`, and puts no edge from the core back to `r` and no edge
`r->r`.

For `L>=1`, the canonical `L`-level feeder adds states
`r_0,...,r_(L-1)` with the only transient edges

```text
r_0 -> r_1 -> ... -> r_(L-1) -> union_j V_j,
```

where each displayed edge to a single transient state forces all `d`
children to carry that state, and the last state sees every core label.  At
level `L` there are `N=d^L` independently phase-allocated core roots.  For a
weak composition `m` of `N`, put

```text
D_L(m;c) = min_j (1/d^L) * sum_s m_s H_(s+j)(c),
D_L^*(c) = max_(m_s>=0, sum m_s=d^L) D_L(m;c).
```

## Normalized claims

### C0. Exact cylinder-dimension lemma

`PROVABLE AS STATED`.

For every frozen phase stratum in this package, if `P_n` is its number of
depth-`n` cylinders and the compatible uniform conditional measure gives
each such cylinder mass `P_n^(-1)`, then

```text
dim_H = liminf_(n->infinity) log(P_n)/|Delta_n|.
```

This is only asserted for the explicitly equiprobable complete-block
strata.

### C1. Complete cyclic block formula

`PROVABLE AS STATED`.

For every `d>=2`, `p>=1`, and every positive integer vector `a`,

```text
dim_H T_C(a) = min_(j in Z/pZ) H_j(c).
```

For a root phase `h`, the exact prefix count is

```text
P_(n,h) = product_(ell=0)^n a_(h+ell)^(d^ell),
```

and along `n congruent r mod p` its normalized logarithm tends to
`H_(h+r)(c)`.

The elementary block calculation also gives
`rho(C(a))=(product_j a_j)^(1/p)`, so `bar(c)=log rho(C(a))`; no external
spectral equality theorem is used.

Boundary cases are included: `p=1`; some or all `a_j=1`; and zero dimension.
Vectors with an entry `a_j=0` are outside the contract.

### C2. Exact one-level transient optimization

`PROVABLE AS STATED`.

For a fixed ordered phase assignment of the `d` children with composition
`m`, the root-`r` stratum has dimension `D_1(m;c)`.  Hence the full one-level
Markov hom tree-shift satisfies

```text
dim_H T_M = max_(m_s>=0, sum m_s=d) D_1(m;c).
```

The maximum already dominates every core-root stratum, because a
composition concentrated in one phase recovers `min_j H_j(c)`.

More generally, if a declared feeder permits a nonempty finite set `F` of
phase compositions and no others, its feeder-root dimension is exactly
`max_(m in F) D_1(m;c)`.  This variant does not license incomplete cyclic
core blocks or return edges.

### C3. Saturation criterion

`PROVABLE AS STATED`.

For any weak composition `m` of `d`,

```text
D_1(m;c) <= bar(c).
```

Equality holds if and only if the circular convolution is constant:

```text
sum_s m_s c_(s+k) is independent of k.
```

Because `a_s` are positive integers, this is equivalently the exact integer
condition

```text
product_s a_(s+k)^(m_s) is independent of k.
```

### C4. Divisibility and Fourier support

`PROVABLE AS STATED` with the hypotheses written below.

- Universally, `p|d` is sufficient for saturation: take `m_s=d/p`.
- Define

  ```text
  hat(c)(q) = sum_(j=0)^(p-1) c_j exp(-2*pi*i*q*j/p).
  ```

  If `hat(c)(q) != 0` for every `q=1,...,p-1`, then a saturating integer
  composition exists if and only if `p|d`; every saturating composition is
  uniform.
- Without this full nonzero Fourier-support hypothesis, necessity is false.
  The mandatory exact counterexample is

  ```text
  p=4, d=2, a=(2,3,2,3), m=(1,1,0,0).
  ```

  Every shifted product is `6`, so saturation holds although `4` does not
  divide `2`.

### C5. Closed formulas for `p=2`

`PROVABLE AS STATED`.

Let

```text
mu = (c_0+c_1)/2,
Delta = |c_1-c_0|.
```

Then

```text
component = mu - (d-1) Delta / (2(d+1)).
```

For a composition `(k,d-k)`,

```text
D_1((k,d-k);c)
  = mu - (d-1)|2k-d| Delta / (2d(d+1)).
```

Consequently,

```text
max feeder = mu                                      if d is even,
             mu - (d-1)Delta/(2d(d+1))              if d is odd.
```

If `Delta>0`, the feeder strictly beats the component for every `d>=2` and
saturates exactly for even `d`.  If `Delta=0`, every composition saturates;
this equality boundary is explicit and is not folded into the parity iff.

### C6. `L`-level denominator and convergence

`PROVABLE AS STATED` for the canonical unrestricted feeder frozen above.

For a fixed phase assignment of the `d^L` level-`L` core roots, its
dimension is exactly `D_L(m;c)`, with denominator `d^L`.  The full Markov hom
tree-shift with the transient chain has dimension `D_L^*(c)`.  Moreover,

```text
D_L(m;c)=bar(c)
iff sum_s m_s c_(s+k) is independent of k.
```

Thus `p|d^L` is sufficient, and it is necessary for the existence of a
saturating level-`L` composition only under the full nonzero Fourier-support
hypothesis in C4.  Without that hypothesis the constant-convolution test,
not divisibility, is the exact statement.  Separately from exact saturation,
the optimized dimensions obey

```text
D_L^*(c) <= bar(c),
D_(L+1)^*(c) >= D_L^*(c),
0 <= bar(c)-D_L^*(c) <= p * max_j H_j(c) / d^L,
lim_(L->infinity) D_L^*(c) = bar(c).
```

If `p|d^L`, the uniform composition gives exact equality already at level
`L`; no converse is asserted without C4's hypothesis.  The convergence
statement for a restricted composition family
requires, and is only claimed under, an explicit balanced-access condition.

### C7. Four-state strict max-SCC counterexample

`PROVABLE AS STATED`.

For `d=2`, state order `(r,a,b1,b2)`, and adjacency

```text
0 1 1 1
0 0 1 1
0 1 0 0
0 1 0 0
```

the only cyclic essential SCC is the complete block with phase sizes
`a=(1,2)`.  Its Hausdorff dimension is `log(2)/3`, while the transient-root
stratum with one child in each phase has dimension `log(2)/2`.  By C2 and
C5 the full shift has dimension `log(2)/2`.  Thus the arbitrary formula
“Hausdorff dimension equals the maximum cyclic-SCC dimension” is false.

## Explicit nonclaims

| Proposed strengthening | Status | Reason |
|---|---|---|
| An SCC-max formula for arbitrary reducible matrices | `NOT CURRENTLY JUSTIFIED` | C7 disproves it. |
| A formula for feeders with return edges | `NOT CURRENTLY JUSTIFIED` | The finite-union transient decomposition fails. |
| The same formula for incomplete cyclic blocks | `NOT CURRENTLY JUSTIFIED` | Equal cylinder counts and phase-only state reduction fail. |
| `p|d` is necessary without a Fourier hypothesis | `NOT CURRENTLY JUSTIFIED` | The required `p=4,d=2` control disproves it. |
| A general non-transient strengthening | `NOT CURRENTLY JUSTIFIED` | No independent matching upper bound is supplied. |
| Any BLW primitive or equality specialization | `NOT CURRENTLY JUSTIFIED` for use here | The proof deliberately imports neither version-sensitive clause. |

The proof package stops at these boundaries.
