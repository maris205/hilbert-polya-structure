# Focused theorem/owner audit — general dihedral normalizer dynamics

**Audit date:** 2026-09-02 UTC  
**Handle:** `GDN`  
**External status:** `HOLD_EXTERNAL`  
**Decision:** `PASS_OWNER_THIN` (freeze-eligible, with all structural group
theory credited to its owners)

This is an internal theorem contract and falsification record.  It is not a
novelty, priority, authorship, or release claim.

## Outcome first

For every integer `n>=3`, let

```text
G_n = D_(2n) = <r,s | r^n=s^2=1, srs=r^(-1)>
```

and let `N_n` send each subgroup `H<=G_n` to its normalizer in `G_n`.
Writing `n=2^a m` with `m` odd, the complete functional graph of `N_n` is a
forest of `sigma(m)` fixed-root binary trees of height `a`, with all rotation
subgroups feeding the distinguished root `G_n` in one step.  More precisely:

1. every cyclic rotation subgroup has depth one;
2. a dihedral subgroup with step `d` has depth exactly `v_2(d)`;
3. every image and every target fibre of `N_n^t` has a closed formula for all
   `t>=1`;
4. the unlabelled functional graph is classified exactly by
   `(v_2(n), sigma(odd(n)), tau(n))`; and
5. the map therefore cannot recover the ambient group order.  In particular,
   `D_66` and `D_70` have isomorphic subgroup-normalizer dynamics, and the
   collision persists after multiplying both polygon parameters by any common
   power of two.

The structural subgroup list and the one-step halving formula are owner-heavy
and receive zero contribution credit.  The admissible residual is the
all-parameter dynamical synthesis: full rooted-forest decomposition, all-time
target fibres, exact functional-graph classification, and arithmetic
non-identifiability pairs.

The independent literal replay covers 44 values of `n`, constructs every
subgroup as an element set, recomputes every normalizer by conjugating every
subgroup element by every ambient group element, and then checks the temporal,
image, fibre, and collision formulas.  It records **29,590 exact assertions**.

## 1. Literal carrier and complete coordinate system

For every divisor `d|n`, put

```text
R_d     = <r^d>,
H_(d,j) = <r^d, r^j s>,             0<=j<d.
```

The complete subgroup carrier is

```text
{R_d:d|n} disjoint_union {H_(d,j):d|n,0<=j<d}.
```

Hence it has

```text
tau(n)+sigma(n)
```

states.  The classification itself is classical and is not counted as new.
The verifier does not assume that the displayed sets are distinct: it builds
them as literal subsets of `Z/nZ semidirect C_2`, checks their expected count,
and checks that no two keys produce the same subset.

## 2. One-step normalizer formula

Every `R_d` is normal, so

```text
N_n(R_d)=G_n=H_(1,0).                                      (2.1)
```

For the reflection-containing subgroup, conjugation by a rotation gives

```text
r^u (r^j s) r^(-u) = r^(j+2u)s.
```

Thus `r^u` normalizes `H_(d,j)` exactly when `d|2u`.  Reflections give the
same congruence coset.  Therefore

```text
N_n(H_(d,j))
  = H_(d/gcd(d,2), j mod (d/gcd(d,2))).                    (2.2)
```

Equivalently, odd-step dihedral subgroups are self-normalizing and every even
step is halved.  Formula (2.2) is a direct structural calculation, and a close
infinite-dihedral owner explicitly records the same odd/even normalizer
phenomenon.  It is therefore zero-credit background here.

## 3. Rooted-forest and temporal theorem

Write `n=2^a m`, `m` odd.  Resolve a dihedral step as `d=2^k e`, where
`e|m`.  Iterating (2.2) gives

```text
N_n^t(H_(2^k e,j))
  = H_(2^(max(k-t,0)) e,
        j mod (2^(max(k-t,0)) e)).                         (3.1)
```

Consequently

```text
depth(R_d)=1,
depth(H_(d,j))=v_2(d).                                     (3.2)
```

There are `sigma(m)` fixed points, namely all `H_(e,j)` with odd `e|m`.
For `1<=k<=a`, exactly `2^k sigma(m)` dihedral states have depth `k`.
Adding the `tau(n)` rotation subgroups at depth one yields the complete depth
polynomial

```text
D_n(z)
 = sigma(m) + tau(n) z
   + sigma(m) sum_(k=1)^a 2^k z^k.                         (3.3)
```

In particular the sharp clock is `max(1,a)`.  If `a>=2`, the deepest states
are exactly the `2^a sigma(m)` subgroups whose step has full two-adic
valuation `a`.  All cycles are fixed points, so the fixed-iterate count is

```text
#Fix(N_n^t)=sigma(m),               t>=1.                  (3.4)
```

The associated zeta expression `(1-z)^(-sigma(m))` is generic finite-map
bookkeeping and receives zero credit.

## 4. Every image and every target fibre for all time

For `t>=1`, the surviving image levels are

```text
k=0,1,...,max(a-t,0).
```

Each level `k` contains `2^k sigma(m)` dihedral subgroups.  Therefore

```text
|im(N_n^t)|
 = sigma(m) [2^(max(a-t,0)+1)-1].                          (4.1)
```

This includes the stabilized value `sigma(m)` once `t>=a`.

The target-resolved formula is as follows.  Rotation subgroups have empty
fibres for every positive time.  For `H_(2^k e,j)` with `k>=1`,

```text
|(N_n^t)^(-1)(H_(2^k e,j))|
 = 2^t,       k+t<=a,
   0,         k+t>a.                                      (4.2)
```

The `2^t` sources are the congruence lifts of `j` from modulus `2^k e` to
modulus `2^(k+t)e`.  For a fixed root `H_(e,j)`, all levels at most `t`
have already entered, giving

```text
|(N_n^t)^(-1)(H_(e,j))|
 = 2^(min(t,a)+1)-1
   + tau(n) [e=1 and j=0].                                 (4.3)
```

The final term in (4.3) is the complete rotation-subgroup family, which feeds
only the distinguished root `G_n=H_(1,0)`.  Equations (4.1)--(4.3) partition
all `tau(n)+sigma(n)` sources at every audited time; the verifier checks them
target by target, including targets outside the image.

## 5. Exact functional-graph classification

Define the arithmetic signature

```text
S(n)=(a, sigma(m), tau(n)),      n=2^a m, m odd.            (5.1)
```

### Sufficiency

For each odd divisor `e|m` and residue `j mod e`, the root `H_(e,j)` carries
one full binary inverse tree of height `a`.  At level `k`, its nodes are
indexed by the `2^k` lifts of `j mod e`.  Match roots arbitrarily while
matching the distinguished root to the distinguished root, preserve the
binary lift index at every level, and match the `tau(n)` rotation leaves
arbitrarily.  Equal signatures therefore give an explicit graph conjugacy.

The verifier constructs this bijection rather than comparing summary counts,
and checks the commuting square at every state for

```text
(33,35), (66,70), (132,140), (264,280).
```

### Necessity

The functional graph itself recovers all three coordinates.

- The number of fixed vertices is `sigma(m)`.
- If the maximum tail is at least two, it equals `a`.  When the maximum tail
  is one, `a=0` is distinguished from `a=1` because nondistinguished fixed
  roots have no incoming transient children in the former case and two in
  the latter.  The excluded small parameters `n=1,2` are exactly the cases in
  which that comparison degenerates.
- Once `a` and `sigma(m)` are known, the total number of vertices recovers the
  last coordinate without any comparison between distinct roots:

  ```text
  tau(n)=|Sub(G_n)|-sigma(m)(2^(a+1)-1).                   (5.2a)
  ```

  The subtracted term is the total number of dihedral vertices in the
  `sigma(m)` full binary trees.  This also covers the one-root case `m=1`,
  where an argument phrased as "excess indegree over other roots" would be
  invalid because no other root exists.

Thus, for all `n,q>=3`,

```text
(Sub(G_n),N_n) is graph-conjugate to (Sub(G_q),N_q)
iff S(n)=S(q).                                               (5.2)
```

This is an inverse theorem with a sharp negative side: the graph recovers the
signature but not the group order.

## 6. Arithmetic collision family

The smallest clean collision used here is

```text
tau(33)=tau(35)=4,
sigma(33)=(1+3)(1+11)=48=(1+5)(1+7)=sigma(35).
```

Therefore for every `a>=0`,

```text
(Sub(D_(2*(2^a*33))),N) ~= (Sub(D_(2*(2^a*35))),N),        (6.1)
```

although the ambient groups have different orders and cannot be isomorphic.
The collision is not inferred from equal state counts: Section 5 supplies an
explicit conjugacy and proves its completeness.

## 7. Separation and contribution boundary

### Earlier internal `DNT` reserve

The P142--P146 scout contained an unnumbered, unpublished reserve restricted
to `m=1` (dihedral 2-groups).  That slice had one fixed root and only one-step
fibres.  It was not selected into P142--P146.  The current theorem is not a
second count of that reserve: its paper-sized residual is created by the odd
core and consists of

1. `sigma(m)` distinct rooted components;
2. all-time target fibres (4.2)--(4.3);
3. the if-and-only-if graph signature (5.2); and
4. nonisomorphic ambient groups with conjugate dynamics (6.1).

### Occupied papers

The nearest numbered systems are P119 (fixed-regular Engel dynamics) and P135
(derived-centralizer orbit partitions).  `GDN` uses neither a group word nor
a centralizer-derived partition.  Its state is an actual subgroup, its update
is normalizer inflation, and its proof is a divisor-indexed congruence forest.
All generic subgroup classification, normalizer-tower language, divisor sums,
and zeta bookkeeping remain zero credit.

### External owner risk

The subgroup classification and odd/even normalizer step are explicitly
owner-heavy.  A bounded search did not locate the conjunction (3.3),
(4.1)--(4.3), (5.2), and (6.1); that non-hit is not novelty evidence.  A
source stating the full functional-graph classification or an equivalent
all-time fibre theorem would kill or materially narrow this contract.

## 8. Reproduction

```bash
python3 docs/papers152_156_sequence/scouting/gdn/verify.py
```

The replay is deterministic, integer-only, and dependency-free.  Enumeration
is falsification pressure; the all-parameter results above rest on the written
deductions from (2.1)--(2.2).
