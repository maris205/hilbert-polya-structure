# Theorem package: diagonal-feedback commutator dynamics

## Claim

Let $K=\mathbb F_q$ be any finite field, let $n\geq1$, and let
$M=M_n(K)$.  Write

$$
\Delta(A)=\operatorname{Diag}(a_{11},\ldots,a_{nn}),
\qquad
\Phi(A)=[\Delta(A),A]=\Delta(A)A-A\Delta(A).
$$

For a zero-diagonal target $Y$, let $G_Y$ be the simple graph on $[n]$ with
$\{i,j\}$ an edge precisely when $y_{ij}\ne0$ or $y_{ji}\ne0$.  For a map
$c:[n]\to K$, put $n_\alpha(c)=|c^{-1}(\alpha)|$ and

$$
m(c)=\sum_{\alpha\in K}n_\alpha(c)(n_\alpha(c)-1).
$$

Define the occupation-marked proper-colouring polynomial

$$
\mathcal P_{Y,q}(X;\mathbf z)=
\sum_{\substack{c:[n]\to K\\c\text{ proper for }G_Y}}
 X^{m(c)}\prod_{\alpha\in K}z_\alpha^{n_\alpha(c)}.       \tag{1}
$$

Then:

1. $\Phi^2=0$, so zero is the unique recurrent and fixed state.
2. A matrix $Y$ is in $\operatorname{im}\Phi$ if and only if its diagonal is
   zero and $G_Y$ is $q$-colourable.
3. Every target fibre is exact:

   $$
   |\Phi^{-1}(Y)|=
   \begin{cases}
   \mathcal P_{Y,q}(q;\mathbf1),&
      \operatorname{diag}Y=0\text{ and }\chi(G_Y)\leq q,\\
   0,&\text{otherwise}.
   \end{cases}                                           \tag{2}
   $$

4. The fibre size depends only on the zero/nonzero support graph $G_Y$, not
   on the nonzero field values in $Y$.  Zero is the unique target with the
   largest fibre.
5. If

   $$
   \kappa_{n,q}=\sum_{n_1+\cdots+n_q=n}
   \binom{n}{n_1,\ldots,n_q}
   q^{\sum_{a=1}^q n_a(n_a-1)},                           \tag{3}
   $$

   then the depth layers are

   $$
   |D_0|=1,\qquad |D_1|=\kappa_{n,q}-1,\qquad
   |D_2|=q^{n^2}-\kappa_{n,q}.                            \tag{4}
   $$

6. The image census is

   $$
   |\operatorname{im}\Phi|
   =\sum_{\substack{G\text{ simple on }[n]\\\chi(G)\le q}}
     (q^2-1)^{|E(G)|}.                                   \tag{5}
   $$

7. For every target $Y$ and time $t$,

   $$
   |(\Phi^t)^{-1}(Y)|=
   \begin{cases}
   1,&t=0,\\
   |\Phi^{-1}(Y)|,&t=1,\\
   q^{n^2},&t\ge2\text{ and }Y=0,\\
   0,&t\ge2\text{ and }Y\ne0.
   \end{cases}                                           \tag{6}
   $$

   Its finite-map zeta function is $\zeta_\Phi(z)=(1-z)^{-1}$.  Height two
   is sharp for $n\ge2$; at $n=1$ the height is one.

## Status

`PROVABLE AS STATED / GREEN_OWNER_THIN / HOLD_EXTERNAL`.

The proof below is complete.  The ownership conclusion is deliberately
weaker: the bounded search found no literal owner, which is not a novelty or
freedom-to-operate certificate.

## Assumptions

- The standard ordered basis is part of the state definition; $\Delta$ is
  not similarity invariant.
- The carrier contains every $n\times n$ matrix over the named finite field.
- A `q-colouring` uses the $q$ labelled field elements as colours.
- Graph support forgets directions and nonzero values exactly as defined
  above; no graph-isomorphism quotient is taken.

## Proof Strategy

The diagonal of a commutator with a diagonal matrix vanishes immediately,
which proves the two-step clock.  For the inverse direction, freeze the input
diagonal $d=(d_1,\ldots,d_n)$.  Every off-diagonal equation becomes the
independent scalar equation

$$
y_{ij}=(d_i-d_j)a_{ij}.                                  \tag{7}
$$

Nonzero target entries force unequal diagonal colours and then determine the
input entry uniquely.  Equal colours are allowed only across support
nonedges and make that input entry free.  This is exactly the weighted
proper-colouring sum (1).

## Dependency Map

1. Entrywise commutator multiplication gives (7) and zero output diagonal.
2. Zero output diagonal gives $\Phi^2=0$.
3. Solvability of (7) gives the support-colouring image criterion.
4. Counting the free equal-colour ordered entries gives (1)--(2).
5. The empty support gives the kernel formula (3) and depth layers (4).
6. Grouping reachable targets by support graph gives (5).
7. Square-zero dynamics gives (6), the component description, and zeta.

## Proof

### Step 1: entrywise form and square-zero clock

Put $d_i=a_{ii}$.  Direct multiplication by a diagonal matrix gives

$$
(\Phi(A))_{ij}=(d_i-d_j)a_{ij}.                           \tag{8}
$$

In particular every diagonal entry of $\Phi(A)$ is zero.  Hence
$\Delta(\Phi(A))=0$, and therefore

$$
\Phi^2(A)=[0,\Phi(A)]=0                                  \tag{9}
$$

for every $A$.  If $A$ is fixed, then $A=\Phi(A)=\Phi^2(A)=0$, so zero is
the unique fixed and recurrent state.

### Step 2: image criterion

Suppose $\Phi(A)=Y$.  Equation (8) first forces $y_{ii}=0$.  If
$y_{ij}\ne0$, it also forces $d_i\ne d_j$.  Consequently the diagonal map
$i\mapsto d_i$ is a proper $K$-colouring of $G_Y$.

Conversely, assume $Y$ has zero diagonal and choose a proper colouring
$c:[n]\to K$ of $G_Y$.  Set $a_{ii}=c(i)$.  When $c(i)\ne c(j)$, equation
(8) has the unique solution

$$
a_{ij}=y_{ij}/(c(i)-c(j)).                                \tag{10}
$$

When $c(i)=c(j)$, properness implies $y_{ij}=0$, and any value of $a_{ij}$
solves (8).  This constructs a preimage and proves statement 2.

### Step 3: every-target marked fibre

Fix a proper colouring $c$.  There is one forced input entry for every
ordered pair $(i,j)$ with $c(i)\ne c(j)$.  For every ordered pair with equal
colours, the target entries in both directions vanish and $a_{ij}$ is an
arbitrary field element.  The number of these ordered pairs is

$$
m(c)=\sum_{\alpha\in K}n_\alpha(c)(n_\alpha(c)-1).
$$

The input diagonal was already fixed by $c$, so this colouring contributes
exactly $q^{m(c)}$ preimages.  Distinct colourings give disjoint preimage
sets because they prescribe different input diagonals.  Summation proves
(1)--(2), including the full occupation marking.

The same calculation shows that nonzero target values never enter the
count: only their support forces colour inequalities.  Thus equal support
graphs have equal fibres.

### Step 4: the unique maximal fibre and kernel

For $Y=0$, the support graph is empty and every one of the $q^n$ colourings
appears in (1).  If $Y\ne0$ is reachable, then $G_Y$ has an edge, so at
least one colouring is excluded by properness.  Every summand is positive
at $X=q$, hence

$$
|\Phi^{-1}(Y)|<|\Phi^{-1}(0)|.
$$

Unreachable targets have empty fibres.  Zero is therefore the unique fibre
maximizer.

Grouping all colourings of the empty graph by their occupation vector
$(n_1,\ldots,n_q)$ gives exactly (3).  Thus
$\kappa_{n,q}=|\ker\Phi|$.  Every nonzero kernel state has depth one and
every state outside the kernel has depth two by (9), proving (4).

### Step 5: image census

Fix a simple graph $G$ on $[n]$.  A zero-diagonal matrix has support graph
exactly $G$ precisely when, for each edge $\{i,j\}$, the ordered pair
$(y_{ij},y_{ji})$ is anything except $(0,0)$, while a nonedge forces both
entries to zero.  Hence exactly $(q^2-1)^{|E(G)|}$ matrices have support
$G$.  Step 2 retains exactly the $q$-colourable support graphs, proving (5).

### Step 6: complete functional graph and all times

Equation (9) places $\operatorname{im}\Phi$ inside $\ker\Phi$.  Zero is the
root.  Each nonzero image state is a depth-one child with the number of
depth-two leaves prescribed by (2).  A nonzero kernel state outside the
image is a depth-one leaf.  There are no other vertices or edges.

Equation (6) follows immediately: at time one use (2), while every state is
at zero by time two.  The unique periodic orbit is the fixed point zero, so
$\zeta_\Phi(z)=(1-z)^{-1}$.

For $n\ge2$, take $d_1\ne d_2$ and an input with $a_{12}=1$; equation (8)
gives a nonzero first image, proving sharp height two.  At $n=1$, every input
maps directly to zero and the height is one.  This proves all claims.
$\square$

## Boundary Cases and Falsifiers

- `n=1`: carrier size $q$, kernel size $q$, image size one, height one.
- `n=2`: the exact controls give kernel sizes `10` at $q=2$ and `33` at
  $q=3$, with image sizes $4$ and $9$.
- A target with a nonzero diagonal is never reachable.
- At $q=2$, a target whose support graph contains an odd cycle is never
  reachable.  In particular, the two-colour image condition is not merely
  a zero-diagonal condition.
- Replacing $\Delta(A)$ by a fixed diagonal matrix destroys the feedback
  fibres; replacing it by an arbitrary diagonal statistic need not make the
  second iterate zero.  These are different systems, not parameter cases.

## Open Risks

- The temporal axis is deliberately shallow; the candidate is viable only
  because the image and every-target inverse axis are uniform in both $n$
  and $q$ and retain the occupation marking.
- Additive commutator varieties and Potts/chromatic sums are mature.  Those
  ingredients receive zero credit; only their exact conjunction through the
  state-derived diagonal feedback remains under review.
- A source stating this literal self-map, or the support-only weighted fibre
  formula, is a kill switch.

## Exact hostile controls

The shared standard-library verifier exhausts

\[
(n,q)=(2,2),(2,3),(3,2),(3,3),(4,2).
\]

For every literal source it checks (\Phi^2(A)=0).  For every target it
compares the observed fibre with (2), then refines the comparison by the full
labelled diagonal occupation vector
((n_0,\ldots,n_{q-1})).  It independently enumerates every simple support
graph and verifies (5), every depth layer, and the unique maximal zero fibre.
Representative exact values are

| ((n,q)) | carrier | image | (\kappa_{n,q}) | nonzero fibre values |
|---:|---:|---:|---:|---|
| (2,2) | 16 | 4 | 10 | 2 |
| (2,3) | 81 | 9 | 33 | 6 |
| (3,2) | 512 | 37 | 152 | 8, 16 |
| (3,3) | 19,683 | 729 | 2,355 | 6, 60, 114 |
| (4,2) | 65,536 | 829 | 8,800 | 32, 64, 128, 160, 320 |

The complete eighteen-system canonical run makes **517,353 assertions** and
has edge digest
`ba346c933983b076b55a3560b603017a1f43cdc1f510aea12392eea624dd2098`.
Enumeration is counterexample pressure; the proof above is independent.

## Final internal recommendation

P119's fixed group commutator theorem, general commutator-map fibres, and
generic Potts/chromatic sums are explicitly zero credit.  Their proof engines
do not yield the state-feedback support criterion or its nonuniform marked
fibres.  After that subtraction, M01 is the sole survivor of this lane:

`SURVIVE_INTERNAL / GREEN_OWNER_THIN / HOLD_EXTERNAL`.

No paper number, posting permission, novelty claim, or priority claim follows
from this recommendation.
