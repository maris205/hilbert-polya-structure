# Negative proof package

## Claim

This package certifies three elementary exclusions inside two screened
entrances. The controls below are stated solely to identify occupied proof
mechanisms, not to instantiate fresh candidate literals.

1. Simultaneous subspace balancing is idempotent; its fixed triples are
   precisely the triples with all pairwise intersections equal.
2. Odd-incidence extraction followed by its dual is a linear incidence
   operator determined by the standard projective-plane incidence identity.
3. Taking all tangent lines of a unital and then all dual tangents returns
   the original unital. This is a restricted reconstruction statement, not
   a theorem for arbitrary subsets of a projective plane.

## Status

**PROVABLE AS STATED** for Claims 1–3.

A new two-axis paper or an arbitrary-subset nonlinear tangent-dynamics
theorem is **NOT CURRENTLY JUSTIFIED** by these claims.

## Assumptions and notation

For Claim 1, let $V=\mathbb F_q^d$, where $q$ is a prime power and $d\ge0$.
All coordinates are subspaces of $V$; $+$ denotes subspace sum. Write
$$
B(U,V_1,W)=
\bigl(U+(V_1\cap W),\ V_1+(U\cap W),\ W+(U\cap V_1)\bigr).
$$
The symbol $V_1$ is a coordinate, not the ambient vector space $V$.

For Claim 2, fix any finite projective plane of order $q\ge2$ that exists.
Its point and line sets are $\mathcal P$ and $\mathcal L$, each of size
$v=q^2+q+1$. Each point lies on $q+1$ lines; two distinct points lie on
exactly one common line. Let $A$ be the line-by-point incidence matrix,
$I$ the $v$-by-$v$ identity, $J$ the all-ones matrix and $\mathbf1$ the
all-ones column. Subsets are represented by their $\mathbb F_2$ indicators.

For Claim 3, fix a projective plane $\Pi$ of order $r^2$, with $r\ge2$.
Assume that a unital $U$ exists: $|U|=r^3+1$, and every line meets $U$
in either one or $r+1$ points. A tangent meets $U$ once; a secant meets
it $r+1$ times. Let $\tau_\Pi(U)$ be the set of all tangent lines,
regarded as points of the dual plane $\Pi^*$.

## Proof strategy

Use direct subspace decompositions, the two projective-plane intersection
counts, and a partition of the unital by lines through one point. No
finite computation or unproved generalization is a dependency.

## Dependency map

1. Claim 1 depends on equality of all three pairwise intersections after
   one balancing step. The original lattice source independently owns
   the same update and modular one-step closure result.
2. Claim 2 depends only on the diagonal and off-diagonal entries of
   $A^\mathsf T A$. The odd-secant source identifies the static extraction
   operation; the displayed matrix calculation is this desk's deduction.
3. Claim 3 depends on the tangent count through points inside and outside
   $U$. The primary unital paper explicitly records those counts and
   dual-unital construction; the proof below rederives the needed facts.

## Proof

### Step 1 — simultaneous subspace balancing

Put
$$
K=(U\cap V_1)+(U\cap W)+(V_1\cap W)
$$
and write $B(U,V_1,W)=(U',V_1',W')$.
Every summand defining $K$ lies in both $U'$ and $V_1'$.
For the reverse inclusion, take
$$
x=u+b=v+a,\qquad
u\in U,\quad v\in V_1,\quad b\in V_1\cap W,\quad a\in U\cap W.
$$
Then $u-a=v-b$ belongs to $U\cap V_1$, so
$$
x=(u-a)+a+b\in K.
$$
This proves $U'\cap V_1'=K$. The same already-proved identity is invariant
under permutations of the three coordinate names: applying the
transpositions exchanging $V_1$ with $W$, and $U$ with $W$, gives
$U'\cap W'=K$ and $V_1'\cap W'=K$.

Consequently every additional summand in the second balancing step is $K$,
already contained in each transformed coordinate. Thus $B^2=B$.

A fixed triple satisfies $V_1\cap W\subseteq U$,
$U\cap W\subseteq V_1$ and $U\cap V_1\subseteq W$.
Each pairwise intersection then equals $U\cap V_1\cap W$.
Conversely, equality of all pairwise intersections gives the three
inclusions and hence a fixed triple. This proves Claim 1.
The argument includes $d=0$, when there is only one triple.

This is exactly the first adjustment polynomial in
[Grätzer–Wehrung, §2](https://arxiv.org/pdf/math/0501430),
with meet $=\cap$ and join $=+$; Lemmas 2.3 and 2.7 already give one-step
closure on modular lattices. The finite-vector-space proof is not a
new temporal theorem. It does not prove a novel evaluated fibre formula.

### Step 2 — odd-incidence extraction

The diagonal entry $(A^\mathsf T A)_{p,p}$ counts the $q+1$ lines through
$p$. For distinct points $p,p'$, the corresponding entry counts their
unique common line. Therefore, over the integers,
$$
A^\mathsf T A=qI+J.
$$
For a point-subset indicator $x$, the vector $Ax$ over $\mathbb F_2$
selects exactly the lines meeting that subset oddly. Applying the dual
odd-incidence extraction gives
$$
A^\mathsf T Ax=(q\bmod2)x+
\left(\sum_{p\in\mathcal P}x_p\bmod2\right)\mathbf1.
$$
This proves Claim 2 on every existing plane under the stated hypotheses,
without a polarity identification or any restriction to Desarguesian
planes. It is a linear-map calculation, and is excluded by the current
matrix-power rule. No nonlinear residual follows from renaming the
coordinates as points and lines.

[Ball–Csajbók, introduction](https://arxiv.org/pdf/1711.10876)
defines odd secants. That paper is not being cited as the author of
this two-pass dynamical calculation or of its inverse fibres.

### Step 3 — tangent duality on unitals

For $p\in U$, the $r^3$ other unital points are partitioned by lines through
$p$. Each secant accounts for $r$ of them and each tangent for zero.
Thus there are $r^2$ secants and, out of $r^2+1$ incident lines, one tangent.

For $p\notin U$, let $s$ and $t$ count its secants and tangents.
Every line is one of these two types and the lines partition $U$, so
$$
s+t=r^2+1,\qquad (r+1)s+t=r^3+1.
$$
Subtracting gives $s=r^2-r$ and hence $t=r+1$.

Every tangent contains exactly one unital point, and each unital point
has exactly one tangent. Hence $|\tau_\Pi(U)|=r^3+1$.
A line of $\Pi^*$ corresponding to $p\in\mathcal P$ meets $\tau_\Pi(U)$
in one point if $p\in U$, and in $r+1$ points if $p\notin U$.
Thus $\tau_\Pi(U)$ is a unital in $\Pi^*$ and its tangent lines, under
the canonical double-dual identification, correspond exactly to $U$:
$$
\tau_{\Pi^*}\bigl(\tau_\Pi(U)\bigr)=U.
$$
This proves Claim 3. Tangent extraction is consequently a bijection
between the unitals of $\Pi$ and those of $\Pi^*$, with singleton
fibres within those respective classes. This argument asserts no
existence of unitals in every plane of square order.

The construction and tangent counts are explicitly recorded in
[Krčadinac–Smoljak, p.255, §1](https://sjm.ba/index.php/sjm/article/download/294/291/294).
It is known dual reconstruction, not a new all-subset orbit or inverse
theorem. No polarity was chosen and no additional autonomous carrier
was nominated to turn this known bijection into a fresh map.

## Corrections or missing assumptions

The unital hypothesis in Claim 3 cannot be dropped from the proof:
both partition equations use the precise intersection numbers and
cardinality. Arbitrary point subsets need not share them. A proposal
on arbitrary subsets would require its own specified carrier/update
and all-parameter temporal and inverse arguments; none is supplied here.

Nor does Claim 1 apply automatically to iterated $M_3[-]$ constructions.
The source's §9 Problem 3 is a historical question about modularity rank,
not a verified current open problem or an independently nominated map.

## Open risks

No mathematical gap is identified in the three restricted certificates.
There is no claim of an exhaustive literature search, global absence of
new finite-geometric dynamics, independent acceptance, or scientific
execution. The source and scope exclusions justify only this desk's
NO_FRESH_SLATE decision.

