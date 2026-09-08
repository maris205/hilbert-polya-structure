# Four-map proof and subtraction package

Date: 2026-09-08 UTC. Author: `/root/round211_algebra_scout`.
These are author deductions, not an independent gate or novelty verdict.
The four literal carriers and all boundary conventions are in INTAKE.md.
No proof below is inferred from the two pilot boxes.

## Status and dependency map

| Map | Proved as stated below | Missing or consumed contribution |
|---|---|---|
| WFS | Complete recurrent set and its exact census; universal height bound; every-target source decoder; unique maximum-fibre target | General sharp height is unproved. The temporal mechanism is completely general inverse aggregation; the extremum is completely general autocorrelation plus elementary nonperiodicity. No primitive novelty credit remains in those mechanisms. |
| TPE | Complete recurrent set and transpose action; coarse clock; all-target fibres and unique maximum for $n\ge2$ | Erasure-to-transpose and independent row parity counts; no sharp clock or fresh temporal mechanism claimed. |
| FLD | Complete image/recurrent set; height at most one; uniform nonempty fibres | Classical logarithmic-derivative ghost identity plus a triangular permutation; no separate inverse mechanism. |
| CGD | Square-zero dynamics, sharp height, complete transfer decoder, evaluated zero fibre | Temporal image-annihilation is an elementary alternating-form transfer. All-target extremum unproved; transfer traces are generic encodings. |

WFS dependencies: pointed inverse-aggregation lemma -> recurrent core ->
partial-injection counts. Independently: labelled assignment decoder ->
autocorrelation -> Cauchy--Schwarz -> nonperiodic marginals -> unique zero
maximum. TPE depends on support erasure and rowwise parity. FLD depends on
Euler derivation and the classical ghost relation. CGD depends on one
quadratic-extension alternating form and a dependence-graph quotient.

## 1. WFS: an exact all-prime theorem with an exact generic adapter

Fix an odd prime $p$, put $Y=\mathbb F_p^*$, $N=p-1$, and let
$S(f)(y)=\sum_{x:f(x)=y}x$ on all $f:\mathbb F_p\to\mathbb F_p$.

### 1.1 Pointed inverse aggregation, not a field-specific temporal result

**Lemma 1.** Let $Y$ be any finite set of size $N$ disjoint from a symbol
$0$. For every subset $B\subseteq Y$, choose $a(B)\in Y\cup\{0\}$ with
$a(\varnothing)=0$ and $a(\{y\})=y$. On maps
$g:Y\to Y\cup\{0\}$ define
$$R_a(g)(z)=a(\{y\in Y:g(y)=z\}),\qquad z\in Y.$$
Its recurrent states are exactly the partial injections: the restriction
of $g$ to $U(g)=\{y:g(y)\ne0\}$ is injective. On this set $R_a$ is
inversion of the partial bijection. For $N\ge2$ every tail is at most
$N-1$; for $N\le1$ every state is already recurrent.

*Proof.* Put $s(g)=|U(g)|$. There are at most $s(g)$ distinct nonzero
values of $g$, with strict inequality unless the stated restriction is
injective. The nonzero positions of $R_a(g)$ form a subset of those values,
because an empty fibre has aggregate zero. Therefore
$$s(R_a(g))\le |g(U(g))|\le s(g),$$
and the second inequality is strict outside the partial-injection set.
For a partial injection, every nonempty relevant fibre is a singleton;
the singleton convention makes $R_a$ exactly its partial inverse. Inversion
is an involution. A periodic orbit cannot contain a strict drop of $s$,
so these are all recurrent states. Until the first partial injection,
$s$ decreases by at least one each epoch. Values $s=0,1$ are always partial
injections. This proves the clock bound and both small-$N$ cases. ∎

This proves the entire temporal engine for **every** such aggregator,
including nonadditive ones. Field summation is not used. The conclusion
is deducted rather than presented as a new phenomenon of WFS.

### 1.2 Exact factorization and recurrent census for WFS

Take $a(B)=\sum_{y\in B}y$ in $\mathbb F_p$. Let $\pi(f)=f|_Y$ and
define $\iota(g)|_Y=g$, $\iota(g)(0)=-\sum_{y\in Y}g(y)$.
Every output of $S$ has total sum zero, because its fibres partition
$\mathbb F_p$ and $\sum_{x\in\mathbb F_p}x=0$. The term at source index
$0$ contributes nothing regardless of $f(0)$. Consequently
$$S=\iota R_a\pi,\qquad \pi\iota=\operatorname{id}.$$
This is a fully specified factor/section adapter, not just similar-looking
graphs. The recurrent set is exactly
$$\mathcal R_p=
 \{\iota(g):g|_{U(g)}:U(g)\longrightarrow Y\text{ is injective}\}.$$
There $S$ inverts the partial bijection in the $Y$ coordinates and restores
the displayed zero coordinate. Every period is one or two. The full height
is at most $p-2$. To check the extra zero coordinate: outside the partial
injections the reduced tail is positive and the first $S$ step already
normalizes that coordinate; inside them the only possible extra depth is
one. Since $p\ge3$, one is at most $p-2$.

Let $I_k=\sum_{j=0}^{\lfloor k/2\rfloor}k!/(2^j j!(k-2j)!)$, the ordinary
number of involutions on a prescribed $k$-set. Then
$$|\mathcal R_p|=\sum_{k=0}^{N}\binom Nk^2 k!,\qquad
 |\operatorname{Fix}(S)|=\sum_{k=0}^{N}\binom Nk I_k,$$
and the number of strict two-cycles is half their difference.
For the first formula choose domain, range, and a bijection. For a fixed
partial inverse, domain and range must be equal and the bijection must be
an involution, which gives the second formula. These are classical partial
injection/involution counts, with no claimed new enumeration primitive.

The pilot's $(p,\text{core},\text{fixed})=(3,7,5),(5,209,43)$ agrees with
these formulas. This statement checks the printed counts by substitution;
the producer was **not** rerun after the theorem was derived. General
sharpness of $p-2$ is not asserted.

### 1.3 All-target sources and the true maximum mechanism

For $b\in\mathbb F_p^{\mathbb F_p}$, every source is exactly a labelled
partition $(B_y)_{y\in\mathbb F_p}$ of $\mathbb F_p$, empty blocks allowed,
such that $\sum_{x\in B_y}x=b(y)$. The assignment $f(x)=y$ for $x\in B_y$
is a bijection, proving completeness and uniqueness of this decoder.
Equivalently, in the integral group algebra with $X_y^p=1$,
$$C_p(b):=|S^{-1}(b)|
 =p\,[X^b]\prod_{x\in\mathbb F_p^*}
                    \left(\sum_{y\in\mathbb F_p}X_y^x\right).$$
The factor $p$ is the independent choice of $f(0)$. Coefficients here are
in the group-algebra basis indexed by $\mathbb F_p^p$, not ordinary
unreduced monomials. In particular this is a finite exact formula for all
targets, not a polynomial-time evaluation claim.

Choose one representative set $P$ for the pairs $\{x,-x\}$ in $Y$ and
write $h=|P|=(p-1)/2$. Let $A(v)$ count assignments $c:P\to\mathbb F_p$
whose contribution vector is
$$v_y=\sum_{x\in P:c(x)=y}x.$$
The assignments on $-P$ are independent and contribute minus a vector
with the same multiplicities. Therefore the **whole fibre distribution** is
the autocorrelation
$$C_p(b)=p\sum_{v\in\mathbb F_p^p}A(v)A(v-b).$$
This identity is the complete adapter requested in the parent value check.
It does not leave the zero-maximum inequality as a distinct new mechanism.

**Proposition 2.** For every odd prime $p$, $b=0$ is the unique maximizer
of $C_p(b)$, with the exact finite value
$$C_p(0)=p\sum_v A(v)^2.$$

*Proof.* Cauchy--Schwarz applied to the displayed autocorrelation gives
$C_p(b)\le p\|A\|_2^2=C_p(0)$, since translation preserves the norm.
Equality holds exactly when $A(v)=A(v-b)$ for all $v$: the proportionality
constant in Cauchy--Schwarz is one because both vectors have the same
positive norm.

Suppose equality holds, and let $\zeta$ be a primitive complex $p$th root.
For each coordinate $j$, the Fourier coefficient at the coordinate vector
$e_j$ is
$$\widehat A(e_j)=\sum_v A(v)\zeta^{v_j}
 =\prod_{x\in P}\bigl(p-1+\zeta^x\bigr)\ne0.$$
Every factor is nonzero since $p-1>1=|\zeta^x|$. Translation invariance by
$b$ then forces $\zeta^{b_j}=1$, so $b_j=0$. This applies at every
coordinate, giving $b=0$. Conversely $b=0$ attains equality. ∎

Thus positive-definite Fourier or autocorrelation/Cauchy--Schwarz completely
explains the maximum; the uniqueness step is elementary nonperiodicity of
the one-coordinate marginals. No independent novelty credit is claimed
for either. The decoder and zero count are standard labelled zero-sum
assignment problems. A source non-hit cannot turn this general argument
into a second new research mechanism.

### 1.4 Explicit boundaries, including failures of tempting strengthenings

- For every permutation $f$, $S(f)=f^{-1}$. For every constant $f$,
  $S(f)=0$. These slices are fully deducted.
- The pilot contains the original source $(0,1,1,2,3)$ at $p=5$ with
  depth three. Its first two images are $(0,3,3,4,0)$ and $(4,0,0,3,3)$.
  This disproves a one-step inverse-selection or first-image recurrence
  claim. It does not prove the full-prime height bound is sharp.
- The small values $C_3(0)=9$ and $C_5(0)=125$ do not establish
  $C_p(0)=p^{(p+1)/2}$. At $p=7$ every function constant on each pair
  $\{x,-x\}$ is a zero source, giving $7^4$ sources. In addition, the
  disjoint nonzero blocks $\{1,2,4\}$ and $\{3,5,6\}$ both sum to zero;
  assigning them distinct output labels gives further sources not constant
  on the opposite pairs. This is a symbolic counterexample to that proposed
  counting formula, **not a $p=7$ execution**.
- P167's minimum-first-preimage operation uses the source label itself on
  missing fibres and cannot merge old weak components (it may split them).
  WFS does neither. For $f=(0,1,1,3,4)$ at $p=5$, the new arrow $1\to3$
  joins old components. P209 preserves component vertex sets and fixes every
  permutation, whereas WFS inverts them. These are exact limits on those
  literal adapters, not proof of new value after Lemma 1 is deducted.

## 2. TPE: parity erasure followed by transpose

Let $E(A)=A^\mathsf T\operatorname{Diag}(A\mathbf1)$ over $\mathbb F_2$.
Each old even-parity row is erased, each odd row retained, then transposed.
If $w(A)$ is its number of ones, $w(E(A))\le w(A)$, with strict inequality
exactly when an old nonzero even-parity row exists.

**Proposition 3.** Recurrent matrices are exactly those for which every
nonzero row and every nonzero column has odd parity. There $E(A)=A^\mathsf T$,
so all periods divide two, and fixed states are precisely the symmetric
members of that core.

*Proof.* On a periodic orbit $w$ cannot decrease. Hence every nonzero row
at every epoch has odd parity; the update is transpose. Applying the same
statement at the next epoch gives the column condition. Conversely both
conditions are preserved by transpose and give $E^2(A)=A$. ∎

A coarse all-size clock is $h(A)\le2\lfloor n^2/2\rfloor$: every deletion
epoch removes at least two ones; if two successive epochs delete none,
the matrix was already in the transpose core at the earlier epoch. Thus
each two-epoch block before the core contains a deletion. This is not a
sharp bound, and it receives no new temporal-mechanism credit.

For any target $B$, every nonzero column must have odd parity. If this
fails its fibre is empty. Otherwise let $z$ be its number of zero columns.
A nonzero column determines the corresponding old odd row uniquely; a zero
column permits any old even row, of which there are $2^{n-1}$. Consequently
$$|E^{-1}(B)|=2^{(n-1)z}$$
for such targets. For $n\ge2$ the zero matrix uniquely maximizes the
fibre at $2^{n(n-1)}$; for $n=1$ both matrices are fixed and both fibres
have size one. These are independent parity-hyperplane choices, not a
new inverse mechanism. The literature's player-selected parity deletion
game is not claimed to equal this simultaneous alternating process.

## 3. FLD: a classical ghost image with a triangular return permutation

Work modulo $x^{N+1}$ over $\mathbb F_q$, $q=p^e$. The Euler derivation
$\delta=x\,d/dx$ preserves the ideal $(x^{N+1})$, so
$L(f)=1+\delta(f)/f$ is well defined for every unit with constant one.

Write $L(f)=1+\sum b_i x^i$. The classical logarithmic-derivative identity
is $b_{pi}=b_i^p$ whenever $pi\le N$. One direct proof factors a polynomial
representative over a splitting field and checks
$\delta(1-\alpha x)/(1-\alpha x)=-\sum_{i\ge1}\alpha^i x^i$; products
add logarithmic derivatives. Truncation preserves the asserted coefficients.
The exact source is Hesselholt--Madsen, Lemma 5.4.1, not a new FLD lemma.

The map $f\mapsto\delta(f)/f$ is a group homomorphism from multiplication
of units to addition. Its kernel is exactly the units supported at degrees
divisible by $p$, since $\delta(f)=\sum i f_i x^i$. Its size is
$q^{\lfloor N/p\rfloor}$, so every nonempty fibre has this size.
The candidate image set
$$\mathcal C=\{1+\sum_{i=1}^N b_i x^i:b_{pi}=b_i^p\ (pi\le N)\}$$
has $q^{N-\lfloor N/p\rfloor}$ elements: choose the coefficients at
indices not divisible by $p$ and propagate by Frobenius. The image has
the same cardinality and is contained in $\mathcal C$, hence equals it.

For $f=1+\sum a_i x^i$, the coefficient of $x^i$ in $L(f)-1$ is
$i a_i$ plus a polynomial in earlier coefficients. On $\mathcal C$, the
independent coefficients have $p\nmid i$, so the restricted map can be
inverted successively, its leading scalar $i$ being nonzero. Thus $L$ is
a permutation of $\mathcal C$. This is the complete recurrent set;
points outside it have depth one. If $N<p$, the whole carrier is recurrent;
if $N\ge p$, the height is exactly one since the image is then proper.
For $N=0$ there is one fixed state. No cycle census beyond this permutation
description is claimed. Both mechanisms are generic ghost/triangular
algebra, with no independent fibre contribution.

## 4. CGD: common trace-zero output and a classical dependence decoder

Let $K=\mathbb F_{q^2}$, $D(z)_i=z_i z_{i+1}^q-z_i^q z_{i+1}$.
Every coordinate satisfies $D(z)_i^q=-D(z)_i$, so lies in the same
one-dimensional $\mathbb F_q$-space $W=\ker\operatorname{Tr}_{K/\mathbb F_q}$.
Any two elements of $W$ are proportional over $\mathbb F_q$, and their
displayed alternating determinant is zero. Therefore $D^2=0$; zero is
the only recurrent point. For $m=1$, $D$ is the zero map and has sharp
height one. For $m\ge2$, taking adjacent coordinates $1,\alpha$ with
$\alpha\notin\mathbb F_q$ gives a nonzero first image, so the height is
exactly two. This is a generic common-line annihilation argument.

Choose a basis $(1,\alpha)$ of $K$, put $\kappa=\alpha^q-\alpha\ne0$,
and write $z_i=u_i+\alpha v_i$. Then
$$D(z)_i=\kappa(u_i v_{i+1}-v_i u_{i+1}).$$
Targets outside $W^m$ are impossible. For $b_i=\kappa c_i$, the full
source set is exactly the cyclic vector sequences $w_i=(u_i,v_i)$ with
$\det(w_i,w_{i+1})=c_i$. With
$M_c(u,v)=\mathbf1\{\det(u,v)=c\}$ on $\mathbb F_q^2$, its fibre count is
$$\operatorname{tr}(M_{c_0}\cdots M_{c_{m-1}}).$$
This is a complete decoder but only generic transfer-matrix encoding,
not an evaluated all-target inverse or an extremal theorem.

The zero fibre can be evaluated without running code. The relation
$\det(u,v)=0$ has vertex zero adjacent to every vector; its nonzero
vertices split into $q+1$ projective lines, each a complete block of size
$q-1$, with no edges between different blocks. The group-difference
subspace has eigenvalue $q-1$ with multiplicity $q$; within-block zero-sum
vectors have eigenvalue zero. On the remaining two-dimensional quotient
the matrix is $\left(\begin{smallmatrix}1&q^2-1\\1&q-1\end{smallmatrix}\right)$.
If $u_0=2$, $u_1=q$, and $u_m=q u_{m-1}+q(q-1)u_{m-2}$, then
$$|D^{-1}(0)|=u_m+q(q-1)^m\qquad(m\ge1).$$
The first two values are $q^2$ and $q^3+q^2-q$. This static projective-line
count does not restore a fresh temporal mechanism. No all-target maximum
claim is made.

## Final author disposition boundary

The strongest package is WFS, but its full recurrence has an exact generic
inverse-aggregation adapter and its full maximum argument has an exact
autocorrelation adapter. The author initially handed this subtraction to
the parent to decide whether a residual conjunction deserved a value gate;
the author did not claim that correct mathematics or a bounded owner
non-hit established admission. The parent subsequently read this package
and closed **all four** maps as `NO_PROMOTION`, with no additional WFS
value gate or scientific run. TPE, FLD and CGD already had author-side
`NO_PROMOTION_MECHANISM_THIN` recommendations. No larger cutoff, repaired
carrier, paper number, reserve or review has been produced. The full
mathematics remains valid within its stated assumptions; this disposition
does not falsely identify these maps with old literal systems.
