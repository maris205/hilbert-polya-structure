# Strict-valley absorption — proved boundaries, missing clock

## Claim and status

`PROVABLE AS STATED`: closure; termination and fixed-point characterization;
the explicit staircase lower bound; the complete one-step image criterion;
and a generic target-refinement formula for the chosen rooted convention.

`NOT CURRENTLY JUSTIFIED`: a sharp joint mass/initial-length clock, a
nontrivial recurrence hierarchy beyond generic fixed points, a maximum-fibre
theorem, or a paper-sized independent two-axis residual.

Author disposition: `NO_PROMOTION`. Correct supporting identities are not
admission or mathematical priority claims. Root and scout are contributors.

## Assumptions and notation

Fix $N\ge1$. The finite carrier $\mathcal C_N$ is all ordered tuples of
positive integers with sum $N$. Indices in a tuple of length $k$ are modulo
$k$; thus at $k=1$ both neighbours are the part itself, and at $k=2$ both
are the same other part. Index zero marks one pile.

For a state $x$, let
$$D(x)=\{i:x_i<x_{i-1}\text{ and }x_i<x_{i+1}\}.$$
For each $i\notin D(x)$ retain a pile of mass
$$x_i+\mathbf1_{\{i+1\in D(x)\}}x_{i+1}.$$
If zero survives, begin the resulting tuple there. If zero is deleted,
begin at its surviving predecessor $k-1$. This defines $V(x)$ in the
existing cyclic direction. All tests use the old state simultaneously.
Let $\tau(x)$ be the number of nonfixed updates before fixation.

For an output tuple $y=(y_0,\ldots,y_{m-1})$, an *isolated cyclic one*
means an index with $y_i=1$ and both $y_{i-1},y_{i+1}\ge2$, using the same
small-length conventions.

## Strategy and dependencies

1. Strict minima are nonadjacent, so recipients survive and at most one
   deleted part joins each survivor; positive mass is conserved.
2. Every nonfixed step removes a part, giving only the generic length clock.
3. A single growing accumulator supplies the staircase lower-bound family;
   no upper bound follows from that example.
4. Every output part is one survivor or a survivor followed by a deleted
   minimum. Target ones and twos therefore impose elementary constraints.
5. A canonical one/two-part refinement proves exact image sufficiency.
6. The same unique segmentation gives the generic inverse sum; it is not
   presented as a separate research mechanism.

## Proof

### 1. Closure and termination

At length one $D(x)$ is empty. At every greater length, adjacent indices
cannot both be strict minima: that would require both $x_i<x_{i+1}$ and
$x_{i+1}<x_i$. Thus the predecessor of a deleted pile survives, and each
survivor receives at most its single next neighbour. A global maximum is
not a strict minimum, so at least one survivor remains. The indicated sums
are positive, cover all old masses without overlap, and have total $N$.
The marker's target exists even if index zero is deleted. This proves that
$V$ is a literal autonomous self-map of $\mathcal C_N$.

If $D(x)$ is empty the tuple is unchanged. If $D(x)$ is nonempty its length
strictly decreases. It follows that
$$\tau(x)\le k-1,$$
all recurrent states are fixed, and they are exactly the tuples with no
strict cyclic local minimum. Equal adjacent minima can block deletion:
$(2,1,1)$ is fixed and is not a singleton. These are generic coarsening and
predicate consequences, not a newly obtained time hierarchy.

At length two, equality gives a fixed tuple and inequality deletes exactly
the smaller part, resulting in $(N)$, regardless of which old pile carried
the marker. This agrees with the general definition.

### 2. Root-supplied staircase: lower bound only

For integers $t\ge1$ and $r\ge0$, set
$$w_{t,r}=(2+r,1,2,\ldots,t),\qquad T_j=j(j+1)/2.$$
This has initial length $t+1$ and mass $2+r+T_t$. The case $t=1$ is the
two-part tuple $(2+r,1)$ and takes one update. For $t\ge2$, initially
only the displayed one is a strict minimum. After $j$ updates,
$1\le j<t$, the tuple is
$$V^j(w_{t,r})=(2+r+T_j,j+1,j+2,\ldots,t).$$
For $j<t-1$ the part $j+1$ is strictly below both the accumulator and
the next part $j+2$, since $2+r+T_j>j+1$. Earlier there is no other part;
every later tail part has a smaller preceding tail neighbour. The
accumulator has its smaller right neighbour and cannot be a minimum.
Thus exactly $j+1$ is deleted next and the displayed formula advances.
At $j=t-1$, the two parts are $2+r+T_{t-1}$ and $t$, with the former
strictly larger, so the last step merges to one. Hence
$$\tau(w_{t,r})=t.$$

For example the hand-checked orbit is
$$(2,1,2,3)\mapsto(3,2,3)\mapsto(5,3)\mapsto(8).$$
This attains the elementary $k-1$ bound on that family. It **does not**
prove that $N\ge2+T_t$ is necessary for an arbitrary orbit of depth $t$,
or give the maximum for every joint pair $(N,k)$. No such necessity or
joint sharp formula is claimed. The staircase/coarsening analogy with
P210 is explicitly deducted rather than promoted by its appearance.

### 3. Exact image: no isolated cyclic one

**Theorem.** A target $y\in\mathcal C_N$ lies in $V(\mathcal C_N)$ if
and only if it has no isolated cyclic one.

**Necessity.** Each output comes from a surviving source value $a_i$,
possibly followed by one deleted value $b_i>0$. Write $b_i=0$ if nothing
was deleted after that survivor. Then $y_i=a_i+b_i$, and $b_i>0$ implies
$$b_i<a_i\quad\text{and}\quad b_i<a_{i+1}.$$
If $y_i=1$, positivity forces $a_i=1,b_i=0$. The preceding deleted value
$b_{i-1}$ cannot be positive, since it would need $b_{i-1}<a_i=1$.
Thus the source neighbour immediately to its left is the unchanged value
$a_{i-1}=y_{i-1}$. If $y_{i+1}\ge2$, then $a_{i+1}\ge2$: an
unmerged value has that size, while a merged value has
$a_{i+1}>b_{i+1}\ge1$. Therefore, if both target neighbours are at least
two, the source one would be a strict minimum, contradicting its survival.

**Sufficiency.** Given a target with no isolated cyclic one, choose
$$b_i=\begin{cases}1,&y_i\ge3\text{ and }y_{i+1}\ge2,\\
0,&\text{otherwise},\end{cases}\qquad a_i=y_i-b_i.$$
Expand it cyclically to $a_0$, then $b_0$ if positive, then $a_1$, then
$b_1$ if positive, and so on; place the source marker on $a_0$.
Every inserted one has preceding survivor at least two and following
survivor at least two, so it is a strict minimum. We check that no survivor
is a strict minimum, exhausting the four possible cases:

- If $b_i=1$, survivor $a_i\ge2$ has its smaller inserted one to the right.
- If $y_i\ge3$ and $b_i=0$, then $y_{i+1}=1$; its right neighbour is
  the unchanged one and is smaller.
- If $y_i=2$, then $b_i=0$. Its left source neighbour is at most two:
  it is an inserted one when $y_{i-1}\ge3$ (the next target is two),
  an unchanged two when $y_{i-1}=2$, or an unchanged one otherwise.
- If $y_i=1$, at least one of its two target neighbours is also one.
  Such target ones remain adjacent unchanged source ones on that side,
  so the strict-minimum condition fails.

Exactly the inserted ones are deleted, recovering $y_i=a_i+b_i$ for
each survivor in the prescribed order and with the marker on its first
survivor. The argument includes target length one: $(1)$ and $(2)$ are
their own preimages; $y_0\ge3$ is the image of $(y_0-1,1)$.
It includes target length two with the repeated-neighbour convention.
This proves necessity, sufficiency and the explicit right section. ∎

The source root was kept on a survivor solely to provide a right section;
it is not a restriction on the carrier. Sources with a deleted marked pile
remain part of the full inverse below. This elementary local target test
is all-size mathematics, but does not supply the missing temporal axis.

### 4. Generic full-target refinement sum

For each target part choose
$$0\le b_i\le\left\lfloor\frac{y_i-1}{2}\right\rfloor,
\qquad a_i=y_i-b_i.$$
For cyclic indices put
$$\ell_i=\begin{cases}b_{i-1},&b_{i-1}>0,\\a_{i-1},&b_{i-1}=0.
\end{cases}$$
Call the choices feasible when, for every $i$,
$$b_i>0\ \Longrightarrow\ b_i<a_{i+1},$$
and
$$b_i=0\ \Longrightarrow\ \neg(a_i<\ell_i\text{ and }a_i<a_{i+1}).$$
The range of $b_i$ already ensures $b_i<a_i$ when it is positive.
The first test makes each inserted child a strict minimum; the second
prevents a singleton survivor from firing. A survivor with $b_i>0$ cannot
fire because its right child is smaller. Thus precisely these predicates
make the one/two-part segmentation valid, and
$$|V^{-1}(y)|=\sum_{\text{feasible }(b_0,\ldots,b_{m-1})}
\left(1+\mathbf1_{\{b_0>0\}}\right).$$

To justify the root multiplier and absence of overcounting, start each
segmented source either at $a_0$, or, if $b_0>0$, at $b_0$ and continue
cyclically through the remaining segments and finally $a_0$. The first
marker survives and the second is deleted into its preceding $a_0$, so
both yield exactly the rooted target $y$. Conversely the actual deleted
set of a source is determined by the source; the survivor producing target
index zero is the marked source pile if it survives or its predecessor
otherwise. Following its survivors in cyclic order uniquely recovers every
$a_i,b_i$ and the root branch. Hence distinct counted data give distinct
rooted tuples. This also rules out overcounting from repeated target values.

For $m=1$ the formula reads $1+2\lfloor(N-1)/2\rfloor$, accounting for
the fixed singleton and all unequal ordered two-part sources. No source of
length at least three can reach one in one step, since nonadjacent minima
cannot remove all but one of those sites. This is ordinary local refinement
bookkeeping; no independent maximum-fibre or coupled extremal mechanism is
claimed.

## Corrections and missing obligations

The weaker preliminary image criterion was false; see the unmodified
FAILED_IMAGE_CLAIM_01.md. The corrected no-isolated-one criterion and its
canonical split are distinct statements, both traceable here.

The missing obligation is not closure, the definition of the marker, or a
finite counterexample check. It is an all-state sharp joint temporal theorem
with research value after P210/old coarsening subtraction, together with an
independent inverse/extremal residual stronger than local refinement
bookkeeping. Neither is established by the present deductions. No pilot,
numerical proof, independent review or paper admission is asserted.
