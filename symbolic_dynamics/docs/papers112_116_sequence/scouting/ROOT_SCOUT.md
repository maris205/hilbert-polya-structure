# Root scout for P112--P116

**Historical provenance:** this is a Stage-1 scouting record.  Paper-local
consolidated hostile reviews and final QA control the post-review claims,
owner subtraction, and release boundary.

## Decision summary

The root lane contributes one theorem-ready recommendation and records nine
deliberate non-selections.  It is intended to diversify, not displace, the
three specialist scouting lanes.

| ID | System | earliest exact signal | intake decision |
|---|---|---|---|
| R1 | bounded Cartier operator on `F_(p^a)[x]_{≤n}` | coefficient indices are divided by `p`, while the constant core follows inverse Frobenius | **GO candidate / HOLD external** |
| R2 | rooted-forest parallel leaf peeling | height is the exact clock; endpoint-indexed assembly and an elementary `(m,s)` local-fibre formula survive owner subtraction | **conditional GO / P105 firewall / HOLD external** |
| R3 | `b`-fold run contraction on bounded words | every run length evolves as `ceil(r/b^t)` | reserve-thin: exact but coordinatewise after run coding |
| R4 | parallel Glaisher carry on integer partitions | `b`-free towers conserve mass and terminate at base-`b` digits | kill historical: Glaisher splitting was already rejected before P102--P106 freeze |
| R5 | graph squaring | Bell fixed core and logarithmic diameter depth | kill/direct-background reserve: graph powers own the mechanism |
| R6 | repeated-squaring transitive closure of relations | path lengths double at every step | kill direct: standard parallel transitive closure |
| R7 | iid uniform-hyperplane intersection | dimension is an exact pure-death chain | reserve collision: direct random-matrix rank laws and P109 subspace proximity |
| R8 | truncated-ring Frobenius `f -> f^p mod x^n` | exponents multiply until nilpotent absorption | kill same-family: weaker dual of R1 and arithmetic absorber proximity |
| R9 | ordinary derivative on bounded polynomials | `D^p=0` and depth is controlled by exponent residues | kill thin/direct: a generic nilpotent linear operator after monomial coding |
| R10 | binary-tree center peeling | exact radius clock and path deepest shell | reserve only behind R2; same pruning engine |

## R1: bounded Cartier dynamics

Let `q=p^a` and

```text
X_(q,n) = {sum_(j=0)^n c_j x^j : c_j in F_q}.
```

With `c^(1/p)` denoting inverse Frobenius, define

```text
C(sum c_j x^j) = sum c_(pj)^(1/p) x^j.
```

The coefficient-selection identity closes every iterate:

```text
C^t(f) = sum_(p^t j ≤ n) c_(p^t j)^(p^(-t)) x^j.
```

Consequences visible before any asymptotic fitting are:

- `Im(C^t)` has `q^(floor(n/p^t)+1)` elements and every nonempty
  `t`-step fibre has size `q^(n-floor(n/p^t))`;
- the periodic core consists exactly of the constants, on which the update
  is inverse Frobenius;
- `#Fix(C^m)=p^gcd(a,m)`, so exact core-cycle counts follow by divisor
  Möbius inversion;
- if `tau(f)` is first entry into the constant core, then

  ```text
  tau(f)=0                                      for constant f,
  tau(f)=1+max{v_p(j): j>0 and c_j != 0}       otherwise,
  # {f: tau(f) ≤ t} = q^(n+1-floor(n/p^t));
  ```

- along `n_L=floor(alpha p^L)`, `1≤alpha<p`, the reverse depth defect has
  the exact lattice limit

  ```text
  P(L+1-tau ≥ k) -> q^(-floor(alpha p^(k-1))),  k≥1;
  ```

- the fixed sequence first reveals `p`, reaches `q` first at time `a`, and
  the phase size then recovers `n`; hence the temporal signature recovers
  `(p,a,n)`.

Writing `j=u p^v` with `p` not dividing `u`, the explicit coordinates
`d_(u,v)=sigma^(-v)(c_(u p^v))` have an explicit inverse and conjugate the map
as `Psi C Psi^(-1)=sigma^(-1) x N`, where `N` is the product of finite chain
shifts.  Every inverse-Frobenius cycle of length `d` therefore supports one
weak component of size `d q^n`, with identical attached nilpotent in-trees,
per-root entry layers, and indegree type.

The two routes are complementary, not logically independent end to end.  The
first follows coefficient-index forests and inverse Frobenius orbits and
establishes the iterate and product conjugacy.  The second computes semilinear ranks,
kernel sizes, and subfield fixed counts, then uses divisor inversion.  The
finite control implements actual fields `F_2,F_3,F_4,F_8,F_9,F_16`, rather
than treating `q` as a label permutation.

The direct Cartier/Bridy operator literature owns coefficient extraction on
power series and the Frobenius algebra, and Jeong is a close Cartier-family
owner.  Elspas, Wang, Hernandez Toledo, Panario--Reis, and Reis own generic
finite-linear state diagrams, cyclic--nilpotent decomposition, components,
and attached-tree machinery; these receive zero credit.  The residual
candidate is only the exact bounded Cartier specialization: coefficient and
iterate/image/fibre formulas, the explicit index-chain product conjugacy and
component formulas, all core-entry shells, Frobenius core zeta, lattice depth
limit, and parameter recovery.  No absolute novelty claim is made.

## R2: rooted-forest leaf peeling

On the union of rooted forests carried by all subsets of `[n]`, delete every
non-root leaf simultaneously and keep roots immortal.  The pointwise depth is
the maximum root distance, and the endpoint is the edgeless forest on the
original root set.  If a fixed endpoint has `r>0` roots, its complete basin is

```text
B_(n,r) = sum_(k=0)^(n-r) binom(n-r,k) r(r+k)^(k-1),
```

with the `k=0` term interpreted as `1`; the empty endpoint has basin one.
The empty target (`m=0`) has exactly one predecessor, namely itself.  For a
nonempty target forest `G` with `m>0` present vertices and `s` non-root leaves,
the exact one-step fibre within ambient `[n]` is

```text
sum_(j=0)^s (-1)^j binom(s,j) (m-j+1)^(n-m).
```

Writing `A_0(x)=1` and `A_h(x)=exp(x A_(h-1)(x))`, the number of basin
states of depth at most `h` is the explicit finite EGF coefficient sum of
`A_h(x)^r`.  The fixed count is `2^n`; for `n>=2`, the sharp maximum depth is
`n-1` and exactly `n!` states attain it; they are the rooted Hamilton paths.
At `n=0` there is one depth-zero empty state, and at `n=1` there are two
depth-zero states.  Metric peeling and labelled-species/Prüfer enumeration
give complementary derivations.  Miller--Reif RAKE, Kovchegov--Zaliapin
height pruning, Addario-Berry et al. leaf stripping, Chaiken all-minors,
Riordan and Renyi--Szekeres height enumeration, Cayley counts, the nested EGF,
absorption, zeta conversion, generic inclusion--exclusion, and Hamilton
extremality are all zero-credit background.  The residual internal scope is
only the endpoint-indexed finite-map assembly and elementary `(m,s)` fibre
calculation, with no priority inference.  Because
P105 also deletes combinatorial material, the manuscript must state the
object/update/enumeration firewall explicitly.

The script `code/root_forest_peeling_spike.py` exhausts every state through
`n=6` and checks **431,084 exact assertions; PASS**.  In the `n=6` lane it
checks all `26,830` forests, all local fibres, all endpoint/depth cells, and
the `720=6!` deepest states.

## Exact Cartier proof spike

- Script: `code/root_cartier_spike.py`
- Literal lanes: `F_2` through degree `7`, `F_3` through degree `5`,
  `F_4` through degree `5`, `F_8` through degree `4`, `F_9` through degree
  `3`, and `F_16` through degree `2`.
- Result: **507,007 exact assertions; PASS**.
- Independent checks: direct finite-field orbit iteration, closed coefficient
  formula, depth CDF, every iterate-image fibre, core cycles, and every
  fixed count through two Frobenius periods.

## Freeze advice

Use R1 only if the final five do not already contain two finite-field linear
systems.  Its early signal and complete theorem contract are strong; its
external owner gate remains open.  R2 is now a theorem-complete conditional
GO and is preferable to adding a second random-matrix paper; its P105
firewall remains mandatory.  R3 is only a backup.
