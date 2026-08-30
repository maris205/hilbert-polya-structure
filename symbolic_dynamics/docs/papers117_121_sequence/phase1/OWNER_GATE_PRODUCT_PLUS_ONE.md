# Hostile owner gate: product-plus-one coalescence

> **SUPERSEDED OWNER VERDICT (2026-08-30 hostile review).** This initial
> gate missed Disanto--Fuchs--Paningbatan--Rosenberg (2022), who own the same
> random variable under $X_n=R_n+1$, including the split/law, unmarked
> antichains, mean, and second-moment neighborhood.  Its score and residual
> list are historical only.  The current residual is limited to the
> Yule-averaged cardinality-marked transform and the strict pole/radius
> continuation for $r\ge3$.  Andriantiana--Wagner--Wang own the fixed-tree
> marker, while Chang--Fuchs/Rosenberg own the caterpillar probability;
> external status remains HOLD.

**Role:** independent hostile novelty/owner review  
**System:** adjacent merge `(x,y) -> xy+1` from `(1,...,1)`  
**Checked:** 2026-08-30  
**External status:** `HOLD_EXTERNAL`  
**Gate meaning:** a search non-hit is bounded evidence only; it is not a
novelty or priority claim.

## Executive verdict

**Score: 8.5/10. Verdict: PROCEED CONDITIONALLY to a hard proof/owner
gate, but do not freeze a paper number.**

The old `KILL` assessment was based on a first-moment Riccati equation alone.
That assessment is no longer accurate.  The strengthened package has six
coherent exact pieces:

1. a finite distributional recursion from a uniform original-boundary order;
2. a closed triangular differential hierarchy for every raw moment;
3. a closed bivariate OGF for the expected antichain-size polynomial;
4. a strict all-moment radius cascade proved by Riccati linearization,
   Sturm--Euler oscillation, and Pringsheim's theorem;
5. an elementary closed form for the mean, with a rigorously unique dominant
   pole and leading coefficient one; and
6. an exact minimum and its atom for every size.

The score clears the precommitted `7.5` gate because the random-BST
genealogy, deterministic antichain statistic, forest-ideal interpretation, and
generic analytic method are all owned and receive zero credit.  The residual is
the **specific six-part temporal package for this literal merge pair**, not a
new random-tree model or a new theory of antichains.

## Literal reconstruction and exact claims

Start with `n` ordered unit blocks.  At each step choose uniformly one of the
current adjacent boundaries and replace its incident values by `xy+1`.  Let
the terminal value be `X_n`.

Every current boundary is one of the original `n-1` boundaries that has not
yet been deleted.  Hence the deletion sequence is a uniform permutation of
those boundaries.  Its max-Cartesian tree has the usual random binary-search-
tree split law.  If `I_n` is uniform on `{1,...,n-1}`, then

\[
 X_1=1,\qquad X_n\overset d=1+X_{I_n}X'_{n-I_n},
\]

with conditional independence on the right.  Consequently the complete
finite law obeys

\[
 p_n(v)=\frac1{n-1}\sum_{i=1}^{n-1}
 \sum_{1+ab=v}p_i(a)p_{n-i}(b).
\]

### Marked antichain-size transform

For an evaluation tree `T`, let

\[
 P_T(u)=\sum_{C\text{ an antichain of internal nodes}}u^{|C|},
\]

including the empty antichain.  Then `P_leaf(u)=1` and

\[
 P_T(u)=u+P_{T_L}(u)P_{T_R}(u).
\]

Writing `a_n(u)=E P_T(u)` in the random-permutation/Cartesian-tree model and

\[
 A(z,u)=\sum_{n\ge1}a_n(u)z^{n-1},
\]

the uniform root split gives

\[
 \boxed{A_z=A^2+\frac{u}{(1-z)^2},\qquad A(0,u)=1}.
\]

This Riccati equation is elementary but completely solvable.  Put `w=1-z`,

\[
 \Delta=\sqrt{1-4u},\qquad
 \alpha_\pm=\frac{1\pm\Delta}{2},
\]

and

\[
 y(w,u)=\frac{\alpha_+w^{\alpha_+}-
                   \alpha_-w^{\alpha_-}}{\Delta}.
\]

Then `y(1,u)=y_w(1,u)=1`, `y_ww+u w^(-2)y=0`, and hence

\[
 \boxed{A(z,u)=\frac{y_w(w,u)}{y(w,u)}}.
\]

The expression is taken as a formal power series near `u=0`, or with
consistent principal branches in an analytic neighborhood.  At `u=1/4` the
apparent `Delta=0` singularity is removable, with

\[
 y(w,1/4)=w^{1/2}\left(1+\frac12\log w\right).
\]

Thus `[z^(n-1)u^k]A` is the exact expected number of `k`-element antichains
for every `n,k`; `u=1` recovers the product-plus-one mean.  This is a genuine
marked theorem, but its present derivation is still the same random-BST
root-split route and does **not** by itself satisfy the independent-route
gate.

For `m_{r,n}=E X_n^r` and
`F_r(z)=sum_{n>=1}m_{r,n}z^(n-1)`, direct binomial expansion gives

\[
 (n-1)m_{r,n}=\sum_{i=1}^{n-1}\sum_{k=0}^r
 {r\choose k}m_{k,i}m_{k,n-i},
\]

and therefore

\[
 \boxed{F_r'(z)=\sum_{k=0}^r{r\choose k}F_k(z)^2,
 \quad F_r(0)=1},\qquad F_0(z)=\frac1{1-z}.
\]

This is an exact all-moment hierarchy, but not a claimed elementary closed
form for every `r`: at level `r` it is a Riccati equation forced by lower
levels.  It nevertheless yields the following all-order theorem.

### Strict all-moment radius cascade

Define `rho_0=1`.  For `r>=1`, separate the new unknown in the hierarchy:

\[
 F_r'=F_r^2+G_r,\qquad
 G_r=\sum_{k=0}^{r-1}{r\choose k}F_k^2.
\]

Let `F_r=-u_r'/u_r`, where

\[
 u_r''+G_r u_r=0,\qquad u_r(0)=1,\quad u_r'(0)=-1.
\]

Inductively, let `rho_r` be the first positive zero of `u_r`.  Then

\[
 \boxed{1=\rho_0>\rho_1>\rho_2>\cdots>0},
\]

`rho_r` is the radius of convergence of `F_r`, and `F_r` has a simple
unit-residue pole there:

\[
 F_r(z)=\frac1{\rho_r-z}+O(1).
\]

Here is the point at which a careless proof would be incomplete.  Assume the
claim through `r-1`.  Since all earlier radii are larger,
`G_r` is analytic in `|z|<rho_(r-1)`.  On the positive axis, the inductive
unit pole gives, with `s=rho_(r-1)-x`,

\[
 G_r(x)=\frac{r}{s^2}+O(s^{-1}).
\]

Choose `c` with `1/4<c<r`.  Near the endpoint,
`G_r(x)>=c/s^2`.  The comparison Euler equation

\[
 y_{ss}+\frac{c}{s^2}y=0
\]

has oscillatory solutions
`sqrt(s) cos((sqrt(4c-1)/2)log(s)+phi)` and hence infinitely many zeros
accumulating at `s=0`.  Sturm comparison forces every nonzero solution
`u_r` to have zeros before `rho_(r-1)`, so its first positive zero satisfies
`0<rho_r<rho_(r-1)`.  Since `G_r` is analytic at `rho_r`, uniqueness for the
linear ODE excludes a double zero; the logarithmic derivative therefore has
the displayed unit-residue simple pole.

It remains to identify this first positive pole with the complex radius.
The coefficients of `F_r` are the nonnegative moments `m_(r,n)`.  If its
radius `R` were smaller than `rho_r`, Pringsheim's theorem would force a
singularity at the positive point `R`; but `G_r` is analytic there and `u_r`
has no positive zero before `rho_r`, so `-u_r'/u_r` is analytic near `R`, a
contradiction.  Thus `R=rho_r`.  In particular,

\[
 \boxed{\limsup_{n\to\infty}(\mathbb E X_n^r)^{1/n}=\rho_r^{-1}}.
\]

No uniqueness of the dominant complex singularity, and hence no full
coefficient asymptotic, is asserted for `r>=2`.  For `r=1`, the explicit
solution below supplies uniqueness and the complete asymptotic.

For `M=F_1`,

\[
 M'=M^2+(1-z)^{-2},\qquad M(0)=1.
\]

With `w=1-z`, `alpha=sqrt(3)/2`, the logarithmic-derivative solution is

\[
 \boxed{M(z)=\frac1w\left[\frac12-\alpha
 \tan\!\left(\alpha\log w-\frac\pi6\right)\right]}.
\]

Equivalently `M=-u'/u`, where

\[
 u(z)=\frac2{\sqrt3}w^{1/2}
 \cos\!\left(\alpha\log w-\frac\pi6\right).
\]

The dominant-pole assertion survives hostile checking.  In `|z|<1`, `w` is
in the right half-plane and the principal logarithm is analytic.  Since every
complex zero of cosine is real, a zero of `u` there forces `log w` real and
thus `w>0`.  All such zeros are

\[
 w_k=\exp\!\left(\frac2{\sqrt3}
 \left(\frac{2\pi}3+k\pi\right)\right),\qquad k\in\mathbb Z.
\]

The nearest singularity is the simple zero with `k=-1`, namely

\[
 \rho=1-\exp\!\left(-\frac{2\pi}{3\sqrt3}\right).
\]

For `k<=-2`, `0<w_k<w_{-1}`, hence the corresponding positive `z_k` is
strictly larger than `rho`.  For `k>=0`, `w_k>e^2>2`, so
`|1-w_k|>1>rho`; the logarithmic branch point is at `z=1`.  Thus `rho` is the
unique dominant singularity.  A simple-zero logarithmic derivative gives

\[
 M(z)=\frac1{\rho-z}+O(1),\qquad
 \boxed{\mathbb E X_n\sim\rho^{-n}}.
\]

The leading coefficient is exactly one in this indexing, not merely a
positive unspecified constant.

Finally, `xy+1>=x+y` for positive integers, with equality exactly when
`x=1` or `y=1`.  Induction therefore gives `X_n>=n`, and equality forces an
endpoint split at every internal node, i.e. a planar comb.  The favourable
boundary orders satisfy `c_2=1`, `c_n=2c_{n-1}`, whereas there are `(n-1)!`
orders in total.  Hence

\[
 \boxed{\min\operatorname{supp}X_n=n,\qquad
 \Pr(X_n=n)=\frac{2^{n-2}}{(n-1)!}\quad(n\ge2)}.
\]

## Exact-control result

The independent stochastic pilot compared the literal adjacent process with
all original-boundary permutations through `n=9`, the literal law with raw
moments `r=0,...,6` through `n=12`, the differential hierarchy through
`r=6,n=60`, the marked-antichain ODE coefficientwise through `n=60` (and by
direct boundary-permutation enumeration through `n=9`), and the linear Euler
equation with the Riccati coefficients.  It reports

```text
stoch_phase2b_product_plus_one: PASS
assertions=1694
states=8113
bst_equivalence=uniform original-boundary order checked_n<=9
moment_hierarchy=M_r'=sum_{k=0}^r binom(r,k) M_k^2 checked_r<=6,n<=60
marked_antichains=A_z=A^2+u/(1-z)^2 checked_n<=60,permutations_n<=9
minimum_atom=P(X_n=n)=2^(n-2)/(n-1)! checked_n<=12
```

The separately written root verifier also passes.  Agreement of two programs
is control evidence; the arguments above, not the programs, establish the
all-parameter statements.

## Owner subtraction

| owned layer | primary owner / direct neighbour | required subtraction |
|---|---|---|
| counting rooted subtrees | Frank Ruskey, [*Listing and Counting Subtrees of a Tree*](https://doi.org/10.1137/0210011), SIAM J. Comput. 10 (1981) | deterministic subtree enumeration and the recursive tree parameter receive zero credit |
| forest ideals | Koda--Ruskey, [*A Gray Code for the Ideals of a Forest Poset*](https://doi.org/10.1006/jagm.1993.1044), J. Algorithms 15 (1993) | ideals/antichains of a forest and their generation receive zero credit |
| average antichains on random tree classes | Klazar, [*Twelve Countings with Rooted Plane Trees*](https://doi.org/10.1006/eujc.1995.0095), Eur. J. Combin. 18 (1997) | average antichain enumeration on rooted plane trees and its generating-function treatment receive zero credit |
| random forest ideals | Janson, [*Ideals in a Forest, One-Way Infinite Binary Trees and the Contraction Method*](https://doi.org/10.1007/978-3-0348-8211-8_24) (2002) | random-tree/forest ideal statistics and contraction-method limits receive zero credit; his finite model is the uniform/Catalan tree model, not this random-permutation BST law |
| random-BST analytic framework | Flajolet--Gourdon--Martinez, [*Patterns in Random Binary Search Trees*](https://doi.org/10.1002/%28SICI%291098-2418%28199710%2911%3A3%3C223%3A%3AAID-RSA2%3E3.0.CO%3B2-2), RSA 11 (1997) | uniform root splitting, Cartesian/BST equivalence, bivariate analytic models, Riccati-to-linear reduction, and singularity analysis receive zero credit |
| BST moment differential equations | Martinez--Panholzer--Prodinger, [*On the Number of Descendants and Ascendants in Random Search Trees*](https://doi.org/10.37236/1358), EJC 5 (1998) | all-moment generating-function/differential-equation analysis for classical BST parameters receives zero method credit; their parameter is not the antichain count |

The full binary evaluation tree has `n-1` internal nodes.  Its value satisfies
`A(leaf)=1`, `A(T)=1+A(T_L)A(T_R)`, which counts antichains of internal nodes
including the empty antichain: either take the root, or exclude it and choose
independently below.  Equivalently it is a standard rooted-subtree/forest-
ideal statistic.  This identification is subtraction, not a novelty bridge.

Exact-phrase, recurrence, sequence, random-BST, Cartesian-tree, antichain,
rooted-subtree, pruning, forest-ideal, and 2025--2026 searches did not locate a
source giving the displayed random-permutation-BST marked-antichain transform,
tangent formula, constant `rho`, strict moment-radius cascade, all-moment
hierarchy, or minimum atom as one result.  The integer
weighted totals

```text
1, 2, 6, 26, 148, 1048, 8896, 88144, 999152, 12755904, ...
```

also produced no OEIS hit in the checked window.  These are bounded no-hits,
not evidence that all equivalent vocabularies or unpublished sources have
been exhausted.

## Residual, proof routes, and strongest objection

After subtraction, the defensible residual is narrow:

- the literal adjacent process and its finite law recursion are presentation;
- the antichain/BST identification is classical structure;
- the residual mathematical content is the **closed marked-antichain
  transform, specialized all-moment Riccati hierarchy, strict unit-pole radius
  cascade, elementary tangent evaluation, exact first-moment dominant pole
  with leading constant one, and comb atom as a coherent parameter package**.

Two routes are plausible but are not yet equally mature:

1. **Temporal/analytic route:** uniform boundary deletion, independent root
   splits, moment hierarchy, Riccati--Euler linearization, Sturm comparison,
   Pringsheim radius identification, and first-moment zero analysis.
2. **Combinatorial route:** boundary permutations as heap labelings of
   Cartesian trees, then count pairs `(heap labeling, forest ideal)` directly;
   comb labelings give the minimum atom.  To qualify as materially distinct,
   this route must recover the mean coefficients or their OGF without simply
   restating the conditional split recurrence.

**Strongest reviewer objection.**  “Once `X_n` is recognized as the number of
forest ideals of a standard random BST, every displayed identity--including
the marked transform--is a short exercise in the classical root-split
recurrence; the paper changes neither the tree model nor the statistic, and
the higher-moment equations are not explicitly solved beyond their radii.”

That objection is serious.  The exact tangent solution, isolated
transcendental growth constant with unit leading factor, closed marked
transform, and strict all-moment radius cascade clear the hard-proof intake
gate, but not an external novelty statement.

## Actionable gate

Proceed only if the next stage does all of the following:

1. completes a direct heap-labeling/ideal enumeration route that is not the
   root-split proof in different notation;
2. searches the citation neighborhoods of Ruskey, Klazar, Janson, and the BST
   analytic literature for this exact parameter;
3. states the residual at the pair-specific package level and gives all
   classical objects zero credit; and
4. keeps the higher-moment claim at the proved level (strict radii, unit
   positive poles, and exact `limsup`) unless a uniqueness theorem justifies
   full coefficient asymptotics; and
5. gives a direct combinatorial coefficient interpretation of the proved
   marked transform, rather than counting the transform itself as a second
   route.

Kill immediately on a direct random-BST antichain/ideal source containing the
tangent OGF or equivalent constant.  Also kill if Route 2 collapses to the
same root-split recurrence and no additional theorem appears.  External
release, novelty, and priority remain on hold.
