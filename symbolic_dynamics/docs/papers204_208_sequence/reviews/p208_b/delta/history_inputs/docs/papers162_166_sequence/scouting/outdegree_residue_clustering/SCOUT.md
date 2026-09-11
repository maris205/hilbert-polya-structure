# DRC3 — outdegree-residue clustering scout

Date: 2026-09-03 UTC  
Exact status: **all requested formulas resolved and independently replayed**  
Value decision: **`KILL_OWNER_THIN_PORTFOLIO_COLLISION`**  
External status: **`HOLD_EXTERNAL / no novelty or priority claim`**

## Outcome first

DRC3 is mathematically clean, and the proposed height statement needs one
important correction: the maximum depth is exactly three only when
`3 does not divide n`; it is exactly two when `3 divides n` (under the
standing `n>=4`).  The exact deepest condition, every one-step fibre, the
full fibre spectrum by target block sizes, the three-stage image tower, and
all four depth counts admit closed finite formulas.

The candidate is nevertheless killed.  Rajendra–Reddy–Madhusudhan directly
own the equivalence-class-to-cliques degree graph construction.  After that
is subtracted, DRC3's temporal axis is a case split on at most three blocks.
Its inverse and census are the same independent-row multinomial calculation.
Internally this is squeezed between P118's stronger one-round quotient plus
part-weighted-fibre architecture, P127's digraph row-residue/fibre lane, and
the permanent equal-cardinality coarsening kill.  The residual is a useful
lemma package, not a new P162–P166 paper.

## Literal system

Fix `n>=4`.  A state is a loopless labelled digraph `G` on `[n]`; opposite
arcs may coexist.  Put

```text
r_v(G) = outdeg_G(v) mod 3.
```

The update `T(G)` contains both arcs `u->v` and `v->u`, for `u!=v`, exactly
when `r_u(G)=r_v(G)`.  Thus `T(G)` is the complete bidirected cluster graph
on the nonempty residue classes

```text
A_r(G)={v:r_v(G)=r},   a_r=|A_r(G)|,   r=0,1,2.
```

There are `2^(n(n-1))` source states.

## Exact quotient and iterate

Write `H_pi` for the complete bidirected cluster graph of a set partition
`pi`.  If the blocks of `pi` have sizes `b_1,...,b_k`, every vertex in block
`i` has outdegree `b_i-1`.  Hence

```text
T(H_pi)=H_(F(pi)),
```

where `F` merges exactly those blocks of `pi` whose sizes are congruent
modulo three.  The first image partition has at most three blocks, so all
later dynamics occurs in this small quotient.

For a partition with at most three blocks:

- pairwise incongruent positive block sizes are fixed;
- two blocks of one residue merge in the next round;
- three equal residues merge to one block;
- a repeated residue `s` and singleton residue `t` first produce block-size
  residues `2s` and `t`.

The last output is nonfixed precisely when `t=2s mod 3`.  With `s!=t`, this
occurs only for `(s,t)=(1,2)` or `(2,1)`.  Consequently `F^2(pi)` is fixed
for every `pi` with at most three blocks.

## Pointwise depth and sharp height

Let `a=(a_0,a_1,a_2)` be the cardinalities of the three outdegree-residue
classes.  Then:

1. `depth(G)=0` iff `G` is a complete bidirected cluster graph whose positive
   block sizes are pairwise incongruent modulo three.
2. If `G` is not fixed, `depth(G)=1` iff the positive entries of `a` are
   pairwise incongruent modulo three.
3. `depth(G)=3` iff every `a_r>0` and

   ```text
   {a_0 mod 3,a_1 mod 3,a_2 mod 3}
   ```

   is `{1,2}`.  Equivalently, the multiset is `{1,1,2}` or `{1,2,2}`.
4. Every remaining state has depth two.

The deepest pattern has total congruent to one or two, never zero.  Conversely
it is realized by

```text
(a_0,a_1,a_2)=(1,1,n-2)  when n=1 mod 3,
(a_0,a_1,a_2)=(2,2,n-4)  when n=2 mod 3.
```

For `n=0 mod 3`, `(1,1,n-2)` gives a depth-two witness.  Every displayed
class-size vector is realizable: outgoing rows are independent, and degrees
`0,1,2` realize the three residues for `n>=4`.  Therefore

```text
max_G depth(G) = 3,  if 3 does not divide n,
                   2,  if 3 divides n.
```

There are no nontrivial recurrent cycles; the stable image is the fixed set.

## Fixed graphs and exact image tower

Let

```text
E_s(z)=sum_(m>=1, m=s mod 3) z^m/m!,   s=0,1,2.
```

Fixed graphs are exactly set partitions with at most one block in each size
residue.  Their labelled EGF and count are

```text
sum_(n>=1) f_n z^n/n! = product_(s=0)^2 (1+E_s(z))-1,

f_n = sum n!/(a_0!a_1!a_2!),
```

where the finite sum is over `a_0+a_1+a_2=n` satisfying
`a_r=0` or `a_r=r+1 mod 3` for each outdegree-residue coordinate `r`.

Let `I_t(n)=|T^t(X_n)|`.  Every set partition with at most three blocks is a
first image.  Put

```text
J_n = (1/2) sum_(1<=p<n) C(n,p)
      1[p congruent to n-p mod 3 and p mod 3 is 1 or 2].
```

Then

```text
I_1(n)=S(n,1)+S(n,2)+S(n,3),
I_2(n)=f_n+J_n,
I_t(n)=f_n  for every t>=3.
```

Indeed the only nonfixed members of the second image have two block sizes
congruent to the same nonzero residue.  Such a target is obtained by splitting
one block into two sizes of residue one (when the target residue is two) or
two sizes of residue two (when it is one).  The `n>=4` boundary excludes the
only too-small obstruction.

## Every first-image target and fibre spectrum

For `r=0,1,2`, let

```text
c_r(n)=sum_(0<=j<n, j=r mod 3) C(n-1,j)
      =[2^(n-1)+2 cos(((n-1)-2r)pi/3)]/3.
```

Fix a target cluster graph with blocks `B_1,...,B_k`, sizes
`b_i=|B_i|`.  Its fibre is zero for `k>3`.  For `k<=3`,

```text
Phi_n(b_1,...,b_k)
  = sum_(sigma:[k]->{0,1,2} injective)
      product_(i=1)^k c_(sigma(i))(n)^(b_i).                 (1)
```

Proof: each target block must be one full source outdegree-residue class, so
the blocks receive distinct residues.  A vertex assigned residue `r` has
exactly `c_r(n)` possible outgoing rows.  Rows have disjoint arc coordinates
and hence multiply.  All `c_r(n)>0`, so every target with at most three blocks
is supported.

For every `n`, exactly two `c_r` values coincide.  Write their common value
as `A` and the exceptional value as `B`.  Formula (1) becomes

```text
k=1:  2 A^n+B^n;
k=2:  2[A^n+B^p A^q+B^q A^p],                 p+q=n;
k=3:  2 sum_i B^(b_i) A^(n-b_i).
```

This is the complete typewise fibre spectrum.  A block-size partition
`lambda=(b_1>=...>=b_k)` occurs for exactly

```text
n! / [product_i b_i! product_s m_s(lambda)!]
```

labelled targets; numerically equal fibre values are aggregated by summing
these multiplicities.  The mass identity is

```text
sum_(targets with <=3 blocks) Phi_n(target)=2^(n(n-1)).
```

## Exact depth census

For `a_0+a_1+a_2=n`, define

```text
M_n(a)=n!/(a_0!a_1!a_2!) product_(r=0)^2 c_r(n)^(a_r).
```

Let `Q` be the set of vectors whose positive entries have pairwise distinct
residues modulo three, and let `R` be the set of positive vectors whose entry
residues use both one and two and no zero.  Then the exact shell counts are

```text
D_0(n)=f_n,
D_1(n)=sum_(a in Q) M_n(a)-f_n,
D_3(n)=sum_(a in R) M_n(a),
D_2(n)=2^(n(n-1))-D_0(n)-D_1(n)-D_3(n).
```

Equivalently, the depth CDF is

```text
C_0=f_n,
C_1=sum_(a in Q) M_n(a),
C_2=2^(n(n-1))-D_3,
C_3=2^(n(n-1)).
```

The deepest shell also has the coefficient form

```text
D_3(n)=n![z^n]
 sum_(s in {1,2}^3, s nonconstant)
 product_(r=0)^2 E_(s_r)(c_r(n)z).
```

This is an exact deepest-shell enumerator, although the `c_r(n)` dependence
means it is a coefficient formula rather than one fixed EGF in `n`.

## Boundary values and falsification evidence

Literal exhaustive digraph enumeration gives

| `n` | states | first image | fixed | `(D0,D1,D2,D3)` |
|---:|---:|---:|---:|---:|
| 4 | 4,096 | 14 | 5 | `(5,1445,918,1728)` |
| 5 | 1,048,576 | 41 | 11 | `(11,274515,391550,382500)` |

The first divisible boundary is

```text
n=6: c=(11,10,11), images=(122,82,82),
     depth=(82,720370922,353370820,0).
```

The independent verifier:

- exhausts every loopless labelled digraph for `n=4,5`;
- compares every first-image target fibre with (1);
- enumerates every labelled partition with at most three blocks through
  `n=10` and checks both image levels and every partition depth;
- checks roots-of-unity and two-value fibre formulas for all target shapes
  through `n=18`;
- checks fixed counts, image counts, exact shell/CDF formulas, deepest-shell
  congruence, and source-mass identities; and
- executes **2,154,318 assertions**.

Two fresh replays matched `CANONICAL.txt` byte for byte.  Frozen hashes are

```text
CANONICAL.txt   d4799d77926cf92f4c0a94619ef96191f28dffbbbe579b921c7cf8274bc16260
verify_scout.py ce7dc135e3df888eff6cd7d7a7a6811f1af957e8d10945833d69847384f4149d
```

## Hostile value decision and claim ceiling

The theorem package is correct; no mathematical counterexample remains.
The failure is value and ownership:

1. the first-step construction is a direct modular/directed specialization
   of the published degree-equivalence graph template;
2. the entire temporal theorem after the collapse is a finite case analysis
   on at most three block sizes;
3. fibres and all depth counts use the same row-independence/multinomial
   engine, so the census is not an independent second mechanism; and
4. P118, P127, P110, and the EQC permanent kill already occupy the relevant
   quotient, row-residue, and block-coarsening proof architecture.

**Final decision: `KILL_OWNER_THIN_PORTFOLIO_COLLISION`.**  The formulas above
are the maximum safe archival claim ceiling for DRC3, with the degree-
equivalence construction, roots-of-unity filter, and generic labelled
enumeration explicitly zero-credit.  Do not draft a paper, reserve a slot,
contact owners, post, submit, or circulate externally.
