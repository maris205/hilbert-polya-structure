# Round 3 A2: two construction-specific degree obstructions

2026-09-09 UTC. New exclusive Round 3 author work. First-pass and
Round 2 files are read-only. The original PC424-L question remains the
same A1/A2 candidate; this report is not a separate paper.

## Frozen claim, mechanism and falsifiable target

Fix an odd prime $p$, $k=\overline{\mathbb F}_p$, $c\in k$ and
$f=x^2+c$. Write $\Delta Q=Q\circ f-Q$, $B_c=\Delta k[x]$, and

$$K_c=\left\{h\in k[x]:\sum_{a\in O}h(a)=0
\text{ for every ordinary primitive }f\text{-orbit }O\right\}.$$

The unchanged original goal is $K_c=B_c$, equivalently, by the accepted
R6 descent theorem, existence of one finite stable algebraic transfer.
Every distinct orbit point is counted once, including when $p$ divides
the primitive length. The native clock is $T(x,y)=(f(x),y+h(x))$.

The assigned degree target is to construct, for one fixed $h\in K_c$,
compatible actual periodic transfer graphs $\Gamma_j$ with cardinalities
$N_j\to\infty$ and nonzero equations of total degrees
$D_j=o(N_j^{1/3})$. Here $N_j$ means actual selected periodic points,
not the size of a containing finite field. The accepted Round 2 theorem
then gives a polynomial transfer. This round does not assume that target.

The initial announced mechanism was special pullback geometry combined
with optimization of the additive constant on every selected cycle.
The two falsifiable versions pursued are:

1. **Additive-separated compression:** use an additive polynomial
   $L(Y)=\sum_{i=0}^r\lambda_iY^{p^i}$, $\lambda_r\ne0$, and seek
   $L(Y)=A(X)$ on the transfer graph. The predicted pullback residual
   has degree $\max(2\deg A,p^r\deg v)$ after the imported odd
   normal-form shear $h=\Delta Q_0+v$.
2. **Optimized finite-data interpolation:** choose all cycle constants
   jointly and then interpolate a completely general plane equation.
   If $S$ has $N$ points and $m$ cycles, the dimension bottleneck to
   test is $\binom{D+2}{2}-1\ge N-m$, not an assumed independent
   $N$-equation count in a nonlinear parameter space.

The report proves precise obstructions to these two named constructions.
It does not prove that the restriction of one fixed $h\in K_c$ is
generic finite data, or turn such finite data into a PC424-L counterexample.

## Status, source subtraction and dependencies

Original PC424-L / requested graph construction: **NOT CURRENTLY
JUSTIFIED**. The auxiliary claims below are **PROVABLE AS STATED**
by the author hand proofs; no nonauthor Round 3 review is claimed.

Imported and not counted as new:

- The [initial normal form](../../../research_c424_c428/positive_characteristic/PROOF_PACKAGE.md)
  $k[x]=B_c\oplus(k\oplus xk[x^2])$, cycle-by-cycle solvability and
  finite interpolation.
- [First-pass A1](../../lanes/a1_periodic_coboundary/PROOF_SUPPLEMENT.md),
  especially the noncancellation of finite Frobenius combinations of a
  nonzero odd normal representative, and
  [A1 Section C](../../lanes/a1_periodic_coboundary/REPORT.md), finite-field
  coefficient descent. A coherent profinite transfer supplies no degree bound.
- [First-pass A2, Section 2](../../lanes/a2_transfer_bridge/PROOF_SUPPLEMENT.md),
  the global Artin--Schreier certificate. The first theorem below is a
  **finite-set quantitative consequence**, not a new global certificate.
- The [Round 2 cubic theorem](../../continuation_round2/a2_algebraic_transfer/REPORT.md)
  and its [E1 nonauthor review](../../continuation_round2/reviews/e1_periodic_graph/REVIEW.md).
  That general theorem is neither reproved nor improved for unrestricted curves.
- Classical dimension-of-fibres and constructible-image results, checked
  in the Stacks Project's [Section 29.29](https://stacks.math.columbia.edu/tag/02FW)
  and [Chevalley's theorem](https://stacks.math.columbia.edu/tag/054K).
  The parameter-space application below is elementary current-team work,
  not a claim of a new algebraic-geometry dimension theorem.

Dependency map: odd normal form and polynomial root counting imply
Theorem 1; the cycle recurrence gives its exact constant/descent interface;
curve-coefficient incidence stratification and the linear cycle difference
map imply Theorem 2; an explicit $f=x^2$ periodic set gives its asymptotic
finite-data control. Neither theorem requires R6 or the cubic theorem
inside its proof.

## 1. Linear degree obstruction for additive-separated equations

### Theorem 1

Let $v\in k\oplus xk[x^2]$ have positive degree $d$, necessarily odd.
Let $S\subset k$ be a finite union of ordinary $f$-cycles and let
$U:S\to k$ satisfy $U(f(a))-U(a)=v(a)$. Put $N=|S|$.
Let $L(Y)=\sum_{i=0}^r\lambda_iY^{p^i}$ with $\lambda_r\ne0$,
and put $b=p^r$. If

$$L(U(a))=A(a)\quad(a\in S),\qquad A\in k[X],$$

then, putting $a_A=\max(0,\deg A)$ with $a_A=0$ also for $A=0$,

$$N\le\max(2a_A,db).\tag{R3-A2.1}$$

The nonzero equation $P(X,Y)=L(Y)-A(X)$ has total degree
$D=\max(a_A,b)$, so

$$D\ge\frac{N}{\max(2,d)}.\tag{R3-A2.2}$$

No assumption that $L$ is separable, or that $p\nmid |O|$, is used.
Every choice of every per-cycle constant is covered.

### Proof

For each $a\in S$, additivity gives

$$A(f(a))-A(a)=L(U(f(a)))-L(U(a))=L(v(a)).$$

Thus $R(X)=\Delta A(X)-L(v(X))$ vanishes on all $N$ distinct
points of $S$. Its second summand has degree exactly $db$:
the highest Frobenius power has that degree, while every lower power
has strictly smaller degree. The integer $db$ is odd since $d,p$ are odd.
If $A$ is nonconstant, $\Delta A$ has even degree $2a_A$; if
$A$ is constant or zero, $\Delta A=0$. Therefore the two leading
terms cannot cancel, $R\ne0$, and

$$\deg R=\max(2a_A,db).$$

The bound on the number of distinct roots of a nonzero univariate
polynomial proves (R3-A2.1). Its right side is at most
$\max(2,d)\max(a_A,b)$, proving (R3-A2.2). $\square$

### Application to the unchanged fixed-$h$ problem

For fixed $h\in K_c$, write the imported normal decomposition
$h=\Delta Q_0+v$. Then $v\in K_c$; a nonzero constant cannot
belong to $K_c$, by a fixed point. Thus either $v=0$, already giving
the desired transfer, or $v$ has positive odd degree $d$.
Subtracting $Q_0$ from transfer values replaces $T$ by the conjugate
skew product with increment $v$, without changing $S$, $N$ or any
cycle length. This is an explicitly declared proof coordinate, not a
change to the original equation.

For a hypothetical nonzero $v\in K_c$, Theorem 1 rules out even
$D_j=o(N_j)$ in the normalized additive-separated construction.
More sharply, if $b_j<N_j/d$, then $a_{A,j}\ge N_j/2$; if
$a_{A,j}<N_j/2$, then $b_j\ge N_j/d$.

The same linear-order obstruction also applies to original-coordinate
additive-separated equations $L(Y)=A_0(X)$. After setting
$Y=Z+Q_0(X)$, their right side becomes
$A=A_0-L(Q_0)$. Set $q_0=\max(0,\deg Q_0)$, with $q_0=0$
for $Q_0=0$. If the original total degree is $D_0$, then
$\deg A\le\max(D_0,bq_0)$ and $b\le D_0$, so

$$N\le\max(2,2q_0,d)D_0.\tag{R3-A2.3}$$

All constants depend only on the fixed $h,f$ and chosen normal
decomposition, not on the selected cycles or additive-polynomial rank.
No hypothetical defect is constructed by this implication.

## 2. What cycle constants and finite-field descent actually require

### Geometric constant optimization: exact equivalence

Fix nonzero additive $L$, polynomial $A$, and finite union $S$ of
cycles on which the increment $h$ has zero ordinary sums. There is
some transfer $U:S\to k$ with $L(U)=A|_S$ if and only if

$$\Delta A=L(h)\quad\text{at every point of }S.\tag{R3-A2.4}$$

Necessity is the residual calculation. For sufficiency choose one point
$a_O$ in each orbit $O$, put
$s_j=\sum_{i=0}^{j-1}h(f^i(a_O))$, and choose $z_O\in k$ with
$L(z_O)=A(a_O)$. Such a root exists because $L(Y)-A(a_O)$ is
nonconstant and $k$ is algebraically closed. Define
$U(f^j(a_O))=z_O+s_j$. The zero orbit sum makes this well-defined
on the closing step. Equation (R3-A2.4) gives
$A(f^j(a_O))=A(a_O)+L(s_j)$, hence $L(U)=A$.

This proves that geometric per-cycle constant optimization cannot hide
the univariate residual. It is equivalent to its vanishing, not an
independent source of additional degree reduction.

### Prescribed finite field

If $S,h|_S,A|_S$ and the coefficients of $L$ are in a finite field
$F$, then a transfer taking values in $F$ and satisfying the prescribed
equation exists exactly when (R3-A2.4) holds and

$$A(a_O)\in L(F)\quad\text{for one representative }a_O
\text{ of each cycle}.\tag{R3-A2.5}$$

The same construction proves sufficiency with $z_O\in F$; necessity
is $A(a_O)=L(U(a_O))$. The condition is independent of the chosen
representative, because its change is $L(s_j)$ with $s_j\in F$.
Surjectivity of $L:k\to k$ must not be replaced by surjectivity on $F$.

### Frobenius-equivariant choices: the exact orbit-block test

Assume $c,h,A,L$ are defined over $\mathbb F_q$ and $S$ is stable
under $\varphi(a)=a^q$. Partition the set of native $f$-cycles
in $S$ into orbits under $\varphi$. For one such block choose a
cycle $O$, let $e$ be the least positive integer with
$\varphi^e(O)=O$, and choose $a\in O$. There is a unique
$t\in\{0,\ldots,m-1\}$, $m=|O|$, such that
$a^{q^e}=f^t(a)$. Define $s_t=\sum_{i=0}^{t-1}h(f^i(a))$,
including $s_0=0$.

Under (R3-A2.4) and zero native orbit sums, a transfer on this block
with $L(U)=A$ and $U(a^q)=U(a)^q$ exists if and only if the two
equations

$$L(z)=A(a),\qquad z^{q^e}-z=s_t\tag{R3-A2.6}$$

have a simultaneous root $z\in k$.

Necessity follows by setting $z=U(a)$. For sufficiency set
$U(f^j(a))=z+s_j$ on $O$ and transport values by the $q$-power
map to the other $e-1$ cycles. It remains to check the return to $O$.
From the coefficients of $h$ and the equality $a^{q^e}=f^t(a)$,

$$s_j^{q^e}=s_{t+j}-s_t,$$

where cumulative sums use periodic indices, valid because the full
orbit sum is zero. Thus
$(z+s_j)^{q^e}=z+s_{t+j}$ by the second equation in (R3-A2.6),
which gives the required return compatibility for every point of $O$.
The first equation and (R3-A2.4) establish $L(U)=A$ there; defined
coefficients propagate it to the other cycles. This proves sufficiency.
On a point of $q$-Frobenius period $r_a$, equivariance automatically
forces $U(a)\in\mathbb F_{q^{r_a}}$. No containing field size is
used as a substitute for $N$.

Even a zero increment shows why the prescribed equation has a separate
descent condition: take $q=p$, $f=x^2$, $S=\{0\}$, $h=0$,
$L(Y)=Y^p-Y$, and $A=1$. The residual vanishes and geometric roots
exist, but (R3-A2.6) would require both $z^p-z=1$ and $z^p-z=0$.
There is no Frobenius-equivariant choice for this prescribed curve.
Of course $h=0$ has the polynomial transfer $U=0$; the example only
refutes automatic descent of an arbitrarily prescribed graph equation.

## 3. Generic finite-data interpolation cannot beat square-root degree

### Theorem 2

Let $S=\{x_1,\ldots,x_N\}\subset k$ be $N\ge1$ distinct points
and let $\pi$ be a permutation of $S$ with $m$ cycles. Define

$$\delta:k^S\to k^S,\qquad
(\delta U)(x)=U(\pi(x))-U(x),$$

and the vector space of zero-cycle-sum data

$$H_S=\left\{w\in k^S:\sum_{x\in O}w(x)=0
\text{ for every }\pi\text{-cycle }O\right\}.$$

For an integer $D\ge0$, put $M_D=\binom{D+2}{2}$. Let
$E_D\subset H_S$ be the data admitting at least one transfer
$\delta U=w$ whose graph lies on some nonzero plane equation of
total degree at most $D$. Then

$$\dim\overline{E_D}\le M_D-1,\qquad
\dim H_S=N-m.\tag{R3-A2.7}$$

Here the bar denotes Zariski closure. In particular, if

$$M_D-1<N-m,\tag{R3-A2.8}$$

a nonempty Zariski-open subset of $H_S$ admits no such degree-$D$
equation for **any** choice of all $m$ cycle constants.

This is a theorem about finite data, with no hypothesis that $w$ is the
restriction of one fixed polynomial satisfying all ordinary cycle sums.

### Proof, Step 1: cycle quotient

The kernel of $\delta$ consists exactly of functions constant on
each of the $m$ cycles, so has dimension $m$ in every characteristic.
Its image is $H_S$: telescoping proves containment and cumulative
sums on each cycle prove reverse containment without division by the
cycle length. Hence $\dim H_S=N-m$.

### Step 2: incidence with arbitrary degree-$D$ curves

Nonzero polynomials of total degree at most $D$, modulo nonzero
scalar multiplication, form $\mathbb P^{M_D-1}$. Define the closed
incidence set

$$I_D=\{([P],U)\in\mathbb P^{M_D-1}\times k^S:
P(x,U(x))=0\ \text{for all }x\in S\}.$$

We claim $\dim I_D\le M_D-1$. To handle possible vertical
components, stratify the coefficient space by the exact subset

$$J(P)=\{x\in S:P(x,Y)\equiv0\text{ as a polynomial in }Y\}.$$

There are finitely many such subsets. On a stratum with $|J|=t$,
the polynomial is divisible by $V_J(X)=\prod_{x\in J}(X-x)$,
because those distinct linear factors are pairwise coprime. If $t>D$
the stratum is empty; otherwise write $P=V_JR$, where $R$ has
total degree at most $D-t$. Thus the stratum has dimension at most
$M_{D-t}-1$.

For a fixed $[P]$ in this stratum, each coordinate $U(x)$ with
$x\notin J$ is a root of the nonzero univariate polynomial
$P(x,Y)$, so has finitely many choices (possibly none). The $t$
coordinates over $J$ are unrestricted. A nonempty fibre therefore
has dimension $t$, even for inseparable or nonreduced root equations.
The dimension-of-fibres inequality for finite-type schemes over $k$
gives

$$\dim(I_D|_J)\le M_{D-t}-1+t\le M_D-1.$$

The last inequality uses
$M_D-M_{D-t}=\sum_{j=D-t+1}^{D}(j+1)\ge t$.
Taking the finite union of strata proves the claim. This stratification
is necessary: without it, the incidence projection need not have finite
fibres because a vertical factor leaves an ordinate unconstrained.

### Step 3: project under the cycle difference map

The morphism $I_D\to H_S$, $([P],U)\mapsto\delta U$, has
set-theoretic image exactly $E_D$. The dimension of an image closure
of a finite-type morphism is at most the dimension of its source:
on each irreducible component dominating its image closure, the
inclusion of function fields bounds transcendence degrees in that
direction. Thus $\dim\overline{E_D}\le\dim I_D\le M_D-1$.
Chevalley's theorem also gives constructibility, though the closure
bound already suffices here. If (R3-A2.8) holds, the closure is a
proper closed subset of the affine space $H_S$. Its complement is
nonempty open. This proves Theorem 2. $\square$

### Rectangular support: the originally proposed bidegree mechanism

If the candidate equations have $X$-degree at most $A$ and $Y$-degree
at most $B$, with integers $A,B\ge0$, the same proof gives

$$\dim\overline{E_{A,B}}\le(A+1)(B+1)-1.\tag{R3-A2.9}$$

Here $E_{A,B}$ is defined as in Theorem 2 with this rectangular
support constraint. Indeed the full projective coefficient space has
dimension $(A+1)(B+1)-1$. On a stratum with $t$ vertical factors
through $S$, the residual $R$ has bidegree at most $(A-t,B)$;
the stratum plus its $t$ free ordinates has dimension at most

$$(A-t+1)(B+1)-1+t
=(A+1)(B+1)-1-tB\le(A+1)(B+1)-1.$$

All later projection steps are unchanged. Therefore generic finite
zero-sum data require $(A+1)(B+1)-1\ge N-m$, even with cycle
constants optimized and without assuming that the interpolation
equations are independent. Balancing a rectangle cannot by itself
change the square-root total-degree exponent.

### Actual quadratic periodic sets exhibiting the finite-data barrier

Fix any odd $p$ and use $f=x^2$. Let $t_p$ be the multiplicative
order of $2$ modulo $p$; it is greater than one. Choose arbitrarily
large prime integers $n$ with $n\ne t_p$ when $t_p$ is prime.
Then $t_p\nmid n$, so $p\nmid2^n-1$. The polynomial
$f^{\circ n}(X)-X=X(X^{2^n-1}-1)$ has exactly $2^n$ distinct
roots. All have native period dividing $n$. Removing the two fixed
points $0,1$ leaves a set $S_n$ of actual primitive $n$-periodic
points with

$$N_n=2^n-2,\qquad m_n=N_n/n.$$

Consequently $N_n-m_n=N_n(1-1/n)$. For every fixed $0<\epsilon<\sqrt2$
and all sufficiently large such $n$, Theorem 2 shows that generic
zero-sum data on $S_n$ have no optimized transfer graph equation
of degree at most $(\sqrt2-\epsilon)\sqrt{N_n}$ (take the integer
floor). Indeed $M_D-1=(D^2+3D)/2$, whose ratio to $N_n$ tends
to a number strictly below one at this scale.

Every vector of these finite data is represented by a unique polynomial
$h_n$ of degree below $N_n$, via ordinary interpolation at the distinct
points of $S_n$. The coefficients lie in some finite extension of
$\mathbb F_p$, since they are finitely many elements of $k$.
This does **not** keep $h_n$ fixed as $n$ grows, bound its degree,
or impose sums on cycles outside $S_n$.

Conversely every fixed transfer graph on $N$ points has a nonzero
degree-$D$ equation once $M_D>N$, by a homogeneous linear system
with $N$ equations and $M_D$ unknowns. Thus these finite-data lower
and upper controls have the same square-root exponent even after
all cycle constants are optimized. Generic finite interpolation alone
cannot establish the requested sub-cube-root degree recurrence.

## 4. Exact remaining bridge and handoff

No compatible sequence of sub-cube-root equations for a fixed
$h\in K_c$ was constructed. The original implication is unchanged
and open. The two proved interfaces delimit particular next attempts:

- Additive-separated curves are more rigid than general curves: a
  nonzero normal increment forces linear degree growth, and the exact
  residual/descent conditions above survive arbitrary cycle constants.
- Finite zero-sum data by themselves cannot give a universal low-degree
  interpolation rule. To beat the square-root barrier for the original
  problem, an argument must use that all restrictions come from one
  fixed bounded-degree $h$ satisfying **every** cycle condition. Theorem 2
  says nothing adverse about that special family.

The results are method obstructions, not PC424-L no-go theorems,
new counterexamples, invariant finite algebraic transfers, or separate
paper admissions. The unrestricted Round 2 cubic theorem remains the
accepted threshold; no stronger unrestricted threshold is asserted.

## 5. Source access and execution receipt

The local source comparison read the actual A1 normal/Frobenius proof,
A1 finite-field Section C, A2 Artin--Schreier proof, Round 2 graph proof
and E1 review. Installed Zotero/Obsidian retrieval tools were absent.
A filename-filtered local PDF lookup found no relevant additional
interpolation/incidence source; unrelated paper-stream files were not read.
The expected arXiv fetch script was not found, so arXiv discovery used
web search. Search-only incidence papers were not imported as theorems.

Primary inputs read in body: Stacks Section 29.29, especially Lemmas
29.29.1--2 and their displayed proofs; Theorem 29.23.3 with its proof;
and [Lemma 10.116.3](https://stacks.math.columbia.edu/tag/00P1) with its
proof. These support classical dimension bookkeeping, not the full
cohomological claim. No claim of exhaustive literature coverage or
global novelty follows from this targeted search.

The proof-writer skill kept the unchanged original claim separate from
the proved method-specific results. The research-lit skill supplied
local-source subtraction and primary-source checking; the batch workflow
kept previous rounds read-only and required a concrete falsifiable
degree mechanism. New writes: only this report in the assigned Round 3
directory. Mathematical runs, old reruns, manuscripts/PDFs, evaluations,
Git writes, external model/API calls and nested workers: **0**.

Open review risks: verify the vertical-factor incidence stratification,
the Frobenius orbit-block return condition, and the explicit finite-data
versus fixed-all-cycle quantifier boundary. No remaining proof step is
intentionally assumed without statement; nonauthor checking is pending.
