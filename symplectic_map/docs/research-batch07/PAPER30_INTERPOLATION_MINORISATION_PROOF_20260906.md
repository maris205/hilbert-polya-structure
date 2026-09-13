# Proof package: bounded-order interpolation and coefficient-uniform mixing

Date: 2026-09-06. New author proof, not a revision of the frozen three-point
proof or a manuscript/capacity decision. `route_applicability: NOT_APPLICABLE`.

## Claim

For every integer $d\geq2$ there exists $\delta_d^*>0$ such that, for
every prime $p\geq16d^2$, every monic degree-$d$ polynomial
$P\in\mathbb F_p[t]$, and every integer $1\leq m\leq d+1$, the law
$$
\mu_P=\tfrac12\delta_{\mathrm{id}}+
\tfrac18\sum_{j=0}^1(\delta_{H_j}+\delta_{H_j^{-1}}),
\qquad H_j(x,y)=(P(x)+j-y,x),
\tag{1}
$$
acting simultaneously on all coordinates of
$\Omega_{p,m}=\operatorname{Conf}_m(\mathbb F_p^2)$ has
$$
\mathcal D_{\mu_P}(f)\geq\delta_d^*\operatorname{Var}(f).
\tag{2}
$$
Configurations are ordered and consist of pairwise distinct points;
the measure is uniform on this full configuration space. The genuinely
non-affine range is $3\leq m\leq d+1$; the first two orders are included
without treating them as separate new results. The same $\delta_d^*$
works throughout the stated finite range of $m$ and over all coefficients.

## Status

`PROVABLE AS STATED` at author level, relative to the explicitly proved
bounded-shear input below and the previously independently checked
affine-comparison input. A new independent check of the interpolation
and assembled higher-order argument is still required.

The initial/final randomization and two polynomial shear layers are an
auxiliary comparison kernel. A close earlier architecture is
Naor–Reingold's pairwise-independent outer permutations and two Feistel
rounds. The dedicated new prior report must deduct that framework; the
present proof does not claim a new general pseudorandom-permutation
architecture. Mathematical correctness and novelty are separate questions.

## Assumptions and notation

Let $G_p=\operatorname{ASL}_2(\mathbb F_p)$ and let $E$ average a function
over each $G_p$ orbit on $\Omega_{p,m}$. Put
$$
N_{p,m}=|\Omega_{p,m}|=(p^2)_m=
\prod_{i=0}^{m-1}(p^2-i),\qquad h=f-Ef.
$$
Use the normalized $L^2$ norm. For every permutation $T$ define
$\mathcal E_T(f)=\tfrac12\|f\circ T-f\|_2^2$. The symmetric law (1)
satisfies $\mathcal E_{H_0}(f)\leq4\mathcal D_{\mu_P}(f)$.

Write $\mathcal P_d=\{R\in\mathbb F_p[t]:\deg R\leq d\}$, including
the zero polynomial, with uniform coefficient measure. Define
$$
T_R(x,y)=(x+R(y),y),\qquad V_R(x,y)=(x,y+R(x)).
\tag{3}
$$
These maps are permutations whether or not $R$ is a permutation polynomial.
The prime-field assumption is essential in the bounded-shear input's
Cauchy–Davenport step. The bound $m\leq d+1$ is essential to the interpolation
argument; no failure or optimality theorem is asserted above that range.

## Strategy and dependency map

1. Reuse the unchanged coefficient-uniform affine energy comparison from
   Steps 1–3 of the three-point proof: its representation-theoretic part
   applies to any finite permutation representation.
2. Produce arbitrary degree-at-most-$d$ shears in uniformly bounded length
   in the auxiliary alphabet $G_p\cup\{H_0^{\pm1}\}$.
3. Use random affine maps to separate the appropriate coordinates of both
   a prescribed source and a prescribed target configuration.
4. Uniform polynomial evaluations at at most $d+1$ distinct nodes give
   two exact independent refresh probabilities, hence a pointwise
   minorisation for a stationary auxiliary kernel.
5. Bound that kernel's energy by (1) using Step 1. No bounded-length
   simulation of an arbitrary affine map in the original four letters
   is asserted or needed.

## Proof

### Step 1. The unchanged affine comparison in arbitrary representations

For a centered monic $P$, the already proved words yield the fixed affine
maps $X=(x+1,y)$, $Y=(x,y+1)$, $U=(x+d!y,y)$ and $V=(x,y+d!x)$.
With
$$
c_d=d!(d-1)/2,\quad L_d=10\,2^{d-2}-4+2c_d,\quad
C_d=\frac{8+L_d^2+(L_d+2)^2}{2},
\tag{4}
$$
their lengths in $H_0^{\pm1},H_1^{\pm1}$ are bounded by
$2,2,L_d,L_d+2$. The lazy law on these four affine maps has regular
representation gap $\gamma_d>0$, uniformly for all $p>d$, by the fixed
integer-generator theorem of Bourgain–Gamburd followed by
Lindenstrauss–Varjú's affine theorem. The exact inputs and their conditions
are proved and directly source-checked in
[three-point author proof, Steps 1–3](PAPER30_UNIFORM_THREE_POINT_MIXING_PROOF_V1_20260906.md)
and independently verified in
[affine-chain audit, Sections 1–6](PAPER30_THREE_POINT_AFFINE_CHAIN_INDEPENDENT_CHECK_20260906.md).

Crucially, those six audit sections do not use the number of points or
any classification of affine orbits. The regular-representation gap
passes to the complement of all invariant vectors in any finite unitary
representation, and the word comparison uses only unitarity. Thus on
the current $m$-point space they give
$$
\|f-Ef\|_2^2\leq\frac{C_d}{\gamma_d}\mathcal D_{\mu_P}(f).
\tag{5}
$$
To handle every uncentered $P$, use exactly the prior conjugacy
$C_s(x,y)=(x+s,y+s)$, $s=-a_{d-1}/d$; it simultaneously centers both
generators. Since $C_s\in G_p$, conjugation preserves the whole affine
group, and its unitary action commutes with the invariant projection.
Consequently (5) holds for every original $P$ with the same constants.
There is no replacement of the arbitrary coefficients by bounded integer
lifts, and no use of the old three-point quotient lemma in this argument.

### Step 2. Bounded realization of arbitrary polynomial shears

The separate [bounded-shear proof](PAPER30_BOUNDED_POLYNOMIAL_SHEAR_PROBE_20260906.md)
supplies the following statement, with the full derivation summarized
here to make the exact dependency and alphabet unambiguous:
$$
\operatorname{length}_{G_p\cup\{H_0^{\pm1}\}}(T_R)
\leq B_d:=12\,2^d-4d-11
\quad(R\in\mathcal P_d).
\tag{6}
$$
In particular this length does not refer to the original four-letter
Hénon alphabet. Each arbitrary member of $G_p$ counts as one auxiliary
letter, and its energy will be handled separately in Step 6.

Here is the construction. Let $J(x,y)=(-y,x)$ and $Y(x,y)=(x,y+1)$.
Then $T_P=H_0J^{-1}$ has auxiliary length two, and
$Y^{-1}T_RYT_R^{-1}=T_{\Delta R}$. Thus the shear with polynomial
$Q_r=\Delta^{d-r}P$ has length at most $4\,2^{d-r}-2$ and leading
coefficient $b_r=d!/r!\neq0$ for $1\leq r\leq d$.
For $t\neq0$, the determinant-one dilation
$D_t(x,y)=(tx,t^{-1}y)$ conjugates it to $T_{tQ_r(ty)}$.

Put $g_r=\gcd(r+1,p-1)$ and
$A_r=\{t^{r+1}:t\in\mathbb F_p\}$. Since the nonzero multiplicative
group is cyclic, $|A_r|=1+(p-1)/g_r$. Cauchy–Davenport iterated
$g_r-1$ times gives $g_rA_r=\mathbb F_p$, because
$g_r(|A_r|-1)+1=p$. Therefore any prescribed leading coefficient $a$
is a sum of at most $g_r\leq r+1$ coefficients $b_rt_i^{r+1}$.
Zero summands are omitted, never implemented with $D_0$.
The product of the corresponding conjugated shears has the desired
leading coefficient. Its lower terms are removed using the induction
statement for arbitrary polynomials of degree at most $r-1$.
Constants are affine translations, with initial bound $B_0=1$.
At degree $r$ the extra length is at most
$4(r+1)2^{d-r}$, giving
$$
B_d\leq1+4\sum_{r=1}^d(r+1)2^{d-r}
=12\,2^d-4d-11.
$$
The right side is used as the common upper bound in (6).
Finally $V_R=J^{-1}T_{-R}J$, so it has length at most $B_d+2$.

### Step 3. Exact polynomial evaluation probabilities

For any pairwise distinct $y_1,\ldots,y_m\in\mathbb F_p$ with
$m\leq d+1$, the evaluation map
$$
\mathcal P_d\longrightarrow\mathbb F_p^m,
\qquad R\longmapsto(R(y_1),\ldots,R(y_m))
\tag{7}
$$
is a surjective linear map. Indeed the Lagrange polynomials
$\prod_{j\neq i}(t-y_j)/(y_i-y_j)$ have degree $m-1\leq d$ and take
the standard coordinate-vector values at the nodes. Every fiber of (7)
has cardinality $p^{d+1-m}$. A uniform $R$ consequently has independent
uniform values at these nodes, with probability exactly $p^{-m}$ for
each prescribed vector of values. This is an exact interpolation fact,
not an exponential-sum approximation.

### Step 4. Affine separation of arbitrary configurations

For a fixed nonzero difference vector $v$ and uniform $A\in G_p$, the
linear part of $Av$ is uniform among the $p^2-1$ nonzero vectors.
Exactly $p-1$ of them have zero second coordinate, so that probability
is $1/(p+1)$. The same statement holds for the first coordinate. Applying
the union bound to the $\binom m2$ nonzero pairwise differences shows
that the probability a given coordinate of all $m$ transformed points
is pairwise distinct is at least
$$
a_{p,m}:=1-\frac{\binom m2}{p+1}.
\tag{8}
$$
This holds for every initial configuration, including highly collinear
ones and configurations with repeated original coordinate values.
Uniform $A^{-1}$ has the same distribution as uniform $A$, so the same
bound holds for inverse images of every prescribed target configuration.

### Step 5. A pointwise minorisation, with no reversibility assumption

Independently choose $A_0,A_1$ uniformly in $G_p$ and $R,S$ uniformly
in $\mathcal P_d$. Let $K$ be the transition kernel on $\Omega_{p,m}$
of the random permutation
$$
W=A_1 V_S T_R A_0.
\tag{9}
$$
Fix arbitrary configurations $z,w$. Restrict to those $A_0$ for which
the second coordinates of $A_0z$ are distinct and those $A_1$ for which
the first coordinates of $A_1^{-1}w$ are distinct. Their independent
joint probability is at least $a_{p,m}^2$.

For each such pair write $A_0z=((x_i,y_i))_i$ and
$A_1^{-1}w=((u_i,v_i))_i$. First require
$R(y_i)=u_i-x_i$ for all $i$. By Step 3 this has probability $p^{-m}$;
after $T_R$ the configuration is $((u_i,y_i))_i$. Its first coordinates
are distinct by the choice of $A_1$. Next require $S(u_i)=v_i-y_i$ for
all $i$, independently with probability $p^{-m}$. The resulting image
under (9) is exactly $w$. Thus
$$
K(z,w)\geq a_{p,m}^2p^{-2m}
=a_{p,m}^2\frac{N_{p,m}}{p^{2m}}\,\frac1{N_{p,m}}
\quad\text{for every }z,w.
\tag{10}
$$
There is no assumption on the equality pattern of the coordinates of
the original $z,w$. The coordinate separation occurs only in auxiliary
affine frames; all intermediate maps are permutations and preserve
pairwise distinctness.

The common coefficient in (10) is uniformly bounded below in the
stated range. Since $m\leq d+1$ and $d\geq2$,
$\binom m2\leq d(d+1)/2\leq d^2$. Consequently $a_{p,m}\geq15/16$.
The elementary inequality $\prod_i(1-t_i)\geq1-\sum_i t_i$ for
$0\leq t_i\leq1$ gives
$$
\frac{N_{p,m}}{p^{2m}}
=\prod_{i=0}^{m-1}(1-i/p^2)
\geq1-\frac{\binom m2}{p^2}\geq\frac{15}{16}.
\tag{11}
$$
Here the final estimate follows from $d^2/p^2\leq1/(16p)\leq1/16$.
As $(15/16)^3>1/2$, (10) proves the simple minorisation
$$
\boxed{K(z,w)\geq\frac1{2N_{p,m}}\quad(z,w\in\Omega_{p,m}).}
\tag{12}
$$

Every instance of (9) is a configuration permutation. Thus $K$ preserves
uniform measure, although it need not be symmetric. Its real energy is
$$
\mathcal E_K(f)=\frac1{2N_{p,m}}\sum_{z,w}K(z,w)|f(w)-f(z)|^2.
\tag{13}
$$
Stationarity makes this equal to
$\operatorname{Re}\langle f,(I-K)f\rangle$.
The all-pairs identity
$\sum_{z,w}|f(w)-f(z)|^2=2N_{p,m}^2\operatorname{Var}(f)$ and (12)
give
$$
\mathcal E_K(f)\geq\tfrac12\operatorname{Var}(f).
\tag{14}
$$
No assertion about the eigenvalues of this non-symmetric kernel is used.

### Step 6. Transfer to the original four Hénon actions

Every word (9) has length at most
$\ell_d=2B_d+4$ in $G_p\cup\{H_0^{\pm1}\}$. For every affine letter
$A$, the function $Ef$ is invariant, so
$$
\mathcal E_A(f)=\tfrac12\|h\circ A-h\|_2^2\leq2\|h\|_2^2.
\tag{15}
$$
Each $H_0$ or $H_0^{-1}$ letter has energy $\mathcal E_{H_0}(f)$.
Telescoping an auxiliary word and applying Cauchy–Schwarz, using that
every intermediate map preserves the uniform norm, gives
$$
\mathcal E_W(f)\leq\ell_d^2
\bigl(2\|h\|_2^2+\mathcal E_{H_0}(f)\bigr).
\tag{16}
$$
The bounded realizations may depend on $R,S,P,p$. Their existence with
one uniform length bound suffices for (16); there is no need to choose
them by a uniform or efficiently computable rule. Averaging (16) over
the exact distribution (9), and then using (5), proves
$$
\mathcal E_K(f)\leq\ell_d^2
\left(2\frac{C_d}{\gamma_d}+4\right)\mathcal D_{\mu_P}(f).
\tag{17}
$$
Combining (14) and (17) yields (2) with the legitimate common constant
$$
\boxed{\delta_d^*=
\left[\ell_d^2\left(4C_d/\gamma_d+8\right)\right]^{-1}>0.}
\tag{18}
$$
This comparison does not claim that uniform affine randomization itself
can be sampled in a bounded number of original Hénon letters. Its cost
is precisely accounted for by the affine spectral gap in (5).
$\square$

## Mixing consequence and its scope

Uniform measure is stationary for (1). Inequality (2) excludes more
than one communicating class by applying it to the indicator of a
class. Laziness and symmetry put the spectrum in $[0,1]$; therefore,
for every start and all $n\geq0$,
$$
\|\mathcal L(Z_n)-u_{p,m}\|_{\mathrm{TV}}
\leq\tfrac12\sqrt{N_{p,m}-1}(1-\delta_d^*)^n
\leq\tfrac12p^m e^{-\delta_d^*n}.
\tag{19}
$$
The support after $n$ steps is at most $5^n$, so distance at most
$\varepsilon\in(0,1)$ requires
$$
n\geq\frac{\log((1-\varepsilon)N_{p,m})}{\log5}.
\tag{20}
$$
Thus for fixed $d,\varepsilon$ the mixing time is
$\Theta_{d,\varepsilon}(\log p)$ simultaneously for all
$1\leq m\leq d+1$ and all allowed coefficients. These are configuration
distributions generated by a common word, not independent coordinate
walks. They do not imply full symmetric/alternating-group Cayley expansion.

## Corrections, nonclaims and proof provenance

- The earlier three-point author theorem is retained unchanged, together
  with its actual independent PASS. This new result strictly increases
  the admissible point order when $d\geq3$ and has a different quotient-
  mixing mechanism. No claim beyond $d+1$ points is included.
- The older area/Jacobi/Weil proof is not needed here. It remains valid
  structural evidence, not a second copy of the same proof to count toward
  any future body-page requirement.
- Interpolation, Cauchy–Davenport, elementary shear arithmetic, outer
  randomization and general comparison principles are prior tools. The
  explicit all-coefficient fixed-two-Hénon theorem is the possible combined
  increment to assess; proof completion alone does not establish novelty.
- This file applies the `proof-writer` structure. Its new algebraic input
  is undergoing a separate bounded proof check, and the new interpolation
  and transfer require an independent assembled audit before candidate
  evaluation. No manuscript or capacity exception has been requested.
