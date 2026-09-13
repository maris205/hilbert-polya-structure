# Paper29 periodic-lift viability: exact cocycles and low periods

Date: 2026-09-05. Independent, bounded feasibility report by the
`p29_periodic_lifting` agent. This is not a review or rehabilitation of
the discarded candidate V1, not a paper project, and not an acceptance.
Only its coordinate reduction is used. The proof-writer skill governs
the separation of proved claims from missing classification steps.

## Claim

Determine when a nonvanishing periodic orbit of the reduced map on
$D_h=\{QP=h(x)\}$ lifts to an actual periodic orbit of
$F=T_gS_f$. In the special case $f=g=t$, determine the small-period
consequences and whether they support an independent substantial paper.

## Status

**PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION** for a general-period
classification. The exact cocycle, its polynomial closure criterion,
the corrected bound $n\le r$, exclusion of periods $1,2,4$ in the
stated ranges, and the complete nonvanishing three-periodic
classification below are **PROVED**. The five-period statement below
additionally assumes that the five integer-time $x$ values are distinct.
No complete classification for arbitrary periods is claimed.

**Independent long-paper assessment: NOT CURRENTLY JUSTIFIED.** There
is a sound short-result package, but the general odd-period lifting
mechanism is an elementary inversion identity on an abelian torsor.
The three-period formula is its first nontrivial explicit case. A
new substantial theorem beyond these computations is still needed;
no Paper29 project should be opened on the strength of this report alone.

`route_applicability: NOT_APPLICABLE`. No arithmetic-orbit determinant,
Riemann hypothesis, spectral, numerical-certification, or PDF claim is made.

## Assumptions and notation

Work over $\mathbb C$, or over $\mathbb R$ where expressly stated. Set
$r\ge3$, $c_r=0$, and
$$
Q=\prod_{i=1}^r q_i,\qquad P=\prod_{i=1}^r p_i,\qquad
x=q_rp_r,\qquad q_ip_i=x+c_i,\qquad
h(z)=\prod_{i=1}^r(z+c_i).
$$
The map uses the plus-sign shears
$$
S_f(q,p)_i=\left(q_i,p_i+f'(Q)\prod_{j\ne i}q_j\right),\quad
T_g(q,p)_i=\left(q_i+g'(P)\prod_{j\ne i}p_j,p_i\right).
$$
The $c_i$ are fixed along the orbit. Unless a statement expressly counts
only their distinct values, they are pairwise distinct.

An orbit is **nonvanishing** here if every $q_i,p_i$ at every integer
time and every intermediate $S_f$ state is nonzero. For a periodic orbit
of $F$, integer-time nonvanishing already implies the intermediate
condition: $S_f$ leaves $q$ unchanged, while the intermediate $p$ is the
next integer-time $p$. This definition excludes coordinate divisors,
and the conclusions do not classify their periodic points.

Indices $k$ are modulo the specified return time $n$. Write $x_k$ for
the integer-time value of $x$, $y_k$ for its value after $S_f$, and
$P_{k+1}$ for the product of the intermediate $p$ coordinates. A return
time need not initially be the least period.

## Proof strategy and dependency map

1. Compute one full-step coordinate multiplier, then multiply it around
   a reduced cycle. This proves exact closure, independently of any
   periodic-point counting theorem.
2. Evaluate the difference of two monic polynomials at the distinct
   $c_i$. Their leading terms cancel, improving $n<r$ to $n\le r$.
3. For $f=g=t$, use the alternating scalar recurrence to constrain the
   permutation of the two equal multisets. This gives the low periods.
4. Recognize $F$ as the square of an inversion-equivariant map. This
   explains odd-period lifting and limits novelty claims.
5. In rank three, calculate the reduced return derivative explicitly.
   This yields a real existence boundary and reduced hyperbolicity,
   not an unproved full-phase-space stability theorem.

## Proof

### 1. Exact full-step cocycle and return criterion

Define
$$
a_k=Q_k f'(Q_k),\qquad y_k=x_k+a_k,\qquad
b_k=P_{k+1}g'(P_{k+1}),\qquad x_{k+1}=y_k+b_k.
$$
Since the intermediate products satisfy $q_i(k)p_i(k+1)=y_k+c_i$,
the $T_g$ update gives
$$
\frac{q_i(k+1)}{q_i(k)}
=1+\frac{b_k}{y_k+c_i}
=\frac{x_{k+1}+c_i}{y_k+c_i}.                 \tag{1}
$$
All denominators are nonzero by hypothesis. Suppose the reduced orbit
returns after $n$ steps. Let
$$
A(t)=\prod_{k=0}^{n-1}(t+x_k),\qquad
B(t)=\prod_{k=0}^{n-1}(t+y_k).
$$
The full return on a quotient fiber is
$$
q_i(n)=C_iq_i(0),\qquad p_i(n)=C_i^{-1}p_i(0),\qquad
C_i=\frac{A(c_i)}{B(c_i)}.                    \tag{2}
$$
The numerator in the direct product of (1) is
$\prod_k(t+x_{k+1})$, which equals $A(t)$ by periodic indexing. This
settles the indexing ambiguity. The formula for $p_i$ follows from
$x_n=x_0$ and $q_i(n)p_i(n)=x_0+c_i\ne0$.

The product of the $C_i$ is $1$, because $Q_n=Q_0\ne0$. Therefore
the return is translation by one element of
$$
H=\{(t_1,\ldots,t_r)\in(\mathbb G_m)^r:\prod_i t_i=1\}.
$$
It is independent of the choice of initial lift. It follows that
**either every point of this nonvanishing quotient fiber returns after
$n$ steps, or none does**. Exact return is equivalent to
$$
C_i=1\ \text{for all }i
\quad\Longleftrightarrow\quad
A(c_i)=B(c_i)\ \text{for all }i.              \tag{3}
$$

If the reduced orbit has least period $n$, a lift has a finite period
if and only if $C=(C_i)$ has finite order, and its least period is
$n\operatorname{ord}(C)$. Over $\mathbb R$, this says that every $C_i$
must lie in $\{1,-1\}$, giving least period $n$ or $2n$. This torsion
criterion concerns a fixed reduced orbit; it does not assert that
either sign case can occur for every $h$ or every $n$.

### 2. Polynomial closure and the correct degree threshold

Let $d_1,\ldots,d_s$ be the distinct values among the $c_i$, and put
$$
H_c(t)=\prod_{a=1}^s(t-d_a).
$$
Equation (3) is equivalent to
$$
H_c(t)\mid A(t)-B(t).                         \tag{4}
$$
Both $A$ and $B$ are monic of degree $n$, so
$\deg(A-B)\le n-1$ unless the difference is zero. If $n\le s$,
(4) forces
$$
A=B\quad\Longleftrightarrow\quad
\{x_0,\ldots,x_{n-1}\}_{\rm multiset}
=\{y_0,\ldots,y_{n-1}\}_{\rm multiset}.       \tag{5}
$$
Conversely, (5) gives exact return without any restriction on $n$.
For pairwise distinct $c_i$, the range is **$n\le r$, not just $n<r$**.

This degree argument is algebraically sharp: at $n=s+1$, arbitrary
monic polynomials $B$ and $A=B+\lambda H_c$, with $\lambda\ne0$, satisfy
the required evaluations while $A\ne B$. Choose $B(d_a)\ne0$ to
avoid zero denominators. These arbitrary polynomials have **not** been
shown to arise from a dynamical orbit. Dynamical sharpness at $n=r+1$
therefore remains open in this report.

### 3. The alternating recurrence for the linear shears

From here through the low-period and derivative statements, take
$f=g=t$. Then
$$
Q_k=y_k-x_k,\qquad P_{k+1}=x_{k+1}-y_k,
$$
and
$$
h(x_k)=(y_k-x_k)(x_k-y_{k-1}),\qquad
h(y_k)=(y_k-x_k)(x_{k+1}-y_k).                \tag{6}
$$
Equivalently, setting $z_{2k}=x_k$, $z_{2k+1}=y_k$ gives
$$
h(z_j)=(z_j-z_{j-1})(z_{j+1}-z_j).           \tag{7}
$$
All adjacent differences in this alternating sequence are nonzero.

### 4. No nonvanishing return times one or two

For $n=1$, (5) gives $y_0=x_0$, contradicting $Q_0\ne0$.
For $n=2$, every $y_0$ belongs to the multiset $\{x_0,x_1\}$, but
$Q_0\ne0$ forbids $y_0=x_0$ and $P_1\ne0$ forbids $y_0=x_1$.
Thus there are no nonvanishing fixed points of $F$ or $F^2$ when the
number of distinct momentum values is at least two; in particular this
holds throughout the pairwise-distinct $r\ge3$ setting.

### 5. Complete nonvanishing three-periodic classification

Assume $s\ge3$. Then (5) applies to any nonvanishing point of
$\operatorname{Fix}(F^3)$. Its three values $x_0,x_1,x_2$ must be
distinct. If, for example, two consecutive values are equal to $a$
and the remaining one is $b$, then at a subsequent consecutive pair
$(a,b)$ the intermediate value would have to be neither $a$ nor $b$,
although those are the entire available multiset. The all-equal case
already violates $Q_k\ne0$.

Each $y_k$ is different from both $x_k$ and $x_{k+1}$. Hence
$$
y_k=x_{k+2}.                                \tag{8}
$$
Let $D(z)=\prod_{j=0}^2(z-x_j)$. At each root $x_j$, (6) gives
$$
h(x_j)=(x_{j+2}-x_j)(x_j-x_{j+1})=-D'(x_j).
$$
Because $D$ is squarefree, this is equivalent to
$$
D\mid h+D'.                                \tag{9}
$$

Conversely, let $D$ be any monic squarefree cubic satisfying (9).
Choose either cyclic ordering of its three roots, and set
$$
Q_k=x_{k+2}-x_k,\qquad P_k=x_k-x_{k+1},\qquad y_k=x_{k+2}.
$$
The equalities $h(x_k)=-D'(x_k)=Q_kP_k$ and
$h(y_k)=Q_kP_{k+1}$ verify every equation of the reduced map. The
differences are nonzero. Also $h(x_k)\ne0$, so no root of $D$ equals
any $-c_i$. Choose arbitrary nonzero $q_i(0)$ with product $Q_0$,
and set $p_i(0)=(x_0+c_i)/q_i(0)$. Formula (1) gives a nonvanishing
lift, and $A=B$ proves that it closes after three steps. Its least
period is three by Section 4.

Thus (9), with $D$ squarefree and monic of degree three, is a complete
classification in the stated nonvanishing, $s\ge3$ setting. Each $D$
gives exactly two reduced three-cycles, corresponding to the two
cyclic root orderings, and the full nonvanishing quotient fibers over
their six points are $(\mathbb C^*)^{r-1}$ families of exact period
three. For real phase-space orbits, $D$ must have three distinct real
roots; that condition is also sufficient when the $c_i$ are real.

### 6. Rank-three formula and an exact real family

When $r=3$, the monic degree-three polynomial $h+D'$ divisible by
the monic cubic $D$ must equal $D$. Thus
$$
D-D'=h,\qquad D=h+h'+h''+h'''.              \tag{10}
$$
The last formula follows by multiplying the finite operator sum
$1+\partial+\partial^2+\partial^3$ by $1-\partial$ on cubics.
It proves uniqueness without solving any root equations.

If this unique $D$ is squarefree, the preceding two reduced cycles
are the complete nonvanishing three-periodic set. If it has a repeated
root, no nonvanishing three-cycle exists.

For the real, pairwise-distinct momentum family
$$
h(z)=z(z^2-a^2),\qquad a\in\mathbb R\setminus\{0\},
$$
formula (10) gives
$$
D(z)=z^3+3z^2+(6-a^2)z+(6-a^2).
$$
With $u=z+1$, this is $u^3+(3-a^2)u+2$, and hence
$$
\operatorname{Disc}(D)=4(a^2-3)^3-108.       \tag{11}
$$
The real depressed-cubic discriminant criterion gives three distinct
real roots exactly when $a^2>6$. This proves an exact boundary:
nonvanishing real three-cycles exist if and only if $a^2>6$.
At $a^2=6$, the cubic is not squarefree; below that boundary it has
only one real root. For example, $a=3$ gives
$D=z^3+3z^2-3z-3$ and two real reduced three-cycles with their full
real torus fibers. No numerical approximation is used in this argument.

### 7. No nonvanishing return time four in the balanced range

Suppose $A=B$ for a putative nonvanishing four-step return. Match the
multisets by a permutation $\sigma$ with $y_k=x_{\sigma(k)}$.
Nonvanishing excludes $\sigma(k)=k,k+1$ even if some $x$ values are
repeated. The only two allowed permutations of four indices are
$$
\sigma=(2,3,0,1),\qquad \sigma=(3,0,1,2),
$$
where a tuple lists the four images. This enumeration follows by
choosing $\sigma(0)\in\{2,3\}$ and enforcing one-to-one use of the
remaining images.

For the first permutation, the two expressions for $h(x_0)$ in (6)
give
$$
(x_2-x_0)(x_0-x_1)=(x_0-x_2)(x_3-x_0),
$$
so $(x_2-x_0)(x_3-x_1)=0$. Its factors are $Q_0,Q_1$, both nonzero.
For the second permutation, the two expressions give
$$
(x_3-x_0)(x_0-x_2)=(x_0-x_1)(x_2-x_0),
$$
so $(x_0-x_2)(x_3-x_1)=0$. Its factors are $P_0,-P_1$, both nonzero.
Both permutations are impossible. Consequently $F^4$ has no
nonvanishing fixed point when $s\ge4$. The argument does not cover
$r=3,n=4$, where polynomial degree no longer forces $A=B$.

### 8. Why odd periods automatically lift: the short mechanism

This section applies more generally to identical shears $f=g$, not
only to $f=g=t$. Let $R(q,p)=(p,q)$ and $G=R\circ S_f$.
Then $T_f=RS_fR$, so
$$
F=G^2.                                     \tag{12}
$$
The map $R$ is anti-symplectic, although the following proof needs
only its action on the torus. The shear $S_f$ commutes with $H$,
whereas $R(t\cdot u)=t^{-1}\cdot R(u)$. Therefore
$$
G(t\cdot u)=t^{-1}\cdot G(u).
$$
Let $\kappa$ be its quotient map. Suppose $n$ is odd and a
nonvanishing quotient point is fixed by $\kappa^n$. Choose a lift $u$.
The free transitive action of $H$ on that quotient fiber gives a
unique $b\in H$ with $G^n u=b\cdot u$. Since $n$ is odd,
$$
G^{2n}u=G^n(b\cdot u)=b^{-1}\cdot G^nu=u.   \tag{13}
$$
The same identity holds for every lift. Thus $F^n$ is the identity
on the entire fiber. If the quotient $\kappa$-period is exactly the
odd integer $n$, its $\kappa^2$-period is also $n$, so every lift has
exact $F$-period $n$.

For $f=t$, $\kappa$ advances the half-step sequence in (7). The
three-period construction has half-step sequence
$$
x_0,x_2,x_1,x_0,x_2,x_1,\ldots,
$$
so it is precisely this odd-period mechanism. Equation (13) is an
elementary cancellation on an abelian torsor, not a new general
reconstruction theory. It does **not** prove the converse that all
balanced $F$-periodic orbits must be odd-periodic for $\kappa$.

### 9. A bounded five-period converse with distinct integer values

Assume $A=B$ and $x_0,\ldots,x_4$ are pairwise distinct. The allowed
matching permutations satisfy $\sigma(k)\notin\{k,k+1\}$. There
are thirteen. Up to simultaneous cyclic relabeling of domain and
range, they are represented by
$$
(2,0,4,1,3),\ (2,4,0,1,3),\ (2,3,4,0,1),\
(3,4,0,1,2),\ (4,0,1,2,3),
$$
with respective orbit sizes $5,5,1,1,1$. The list is obtained by
assigning one permitted unused image to each of the five rows;
the sizes sum to thirteen and exhaust the assignments.

At a matched value $x_j=y_{\sigma^{-1}(j)}$, compatibility means
$$
(x_{\sigma(j)}-x_j)(x_j-x_{\sigma(j-1)})
=(x_j-x_{\sigma^{-1}(j)})
 (x_{\sigma^{-1}(j)+1}-x_j).                 \tag{14}
$$
The first representative forces
$(x_0-x_2)(x_1-x_3)=0$, and the second forces
$(x_1-x_4)(x_2-x_3)=0$. Distinctness excludes both, including all
their cyclic relabelings.

For uniform shift $+2$, normalize $x_0=0,x_1=1$ by an affine change
of variables in the homogeneous difference equations (14), and set
$(x_2,x_3,x_4)=(a,b,c)$. Four of those equations are
$$
a=bc,\qquad a+b-c-ab=0,\qquad
a(b+c-1)-bc=0,\qquad a-b-ab+bc=0.
$$
Since $a,b\ne0$, the first, third, and fourth imply
$b+c=2$ and $a=2c-1$. The second then gives
$(c-1)(a-2)=0$. Distinctness gives $c\ne1$, hence
$a=2,c=3/2,b=1/2$, contradicting $a=bc$.
The equations for uniform shift $-1$ are the negatives of the same
five compatibility equations, so that case is also excluded.
The sole remaining permutation is
$\sigma(k)=k+3\pmod5$. It makes (14) an identity and makes the
half-step sequence five-periodic. Thus this distinct-value subcase
does come from a $\kappa$ five-cycle. Repeated integer-time values
and arbitrary $n$ remain outside this converse.

### 10. Optional rank-three reduced stability computation

For the three-cycle of Section 6, write its $\kappa$-ordered scalar
values as $a,b,c$, and put
$u=b-a$, $v=c-b$, $w=a-c$, so $u+v+w=0$.
In successive-coordinate variables, recurrence (7) is
$$
(z_{j-1},z_j)\longmapsto
\left(z_j,z_j+\frac{h(z_j)}{z_j-z_{j-1}}\right).
$$
Its derivative at the value $a$, using $h=D-D'$, is
$$
M_a=\begin{pmatrix}0&1\\u/w&u/w-1-u\end{pmatrix}.
$$
The derivatives $M_b,M_c$ replace $(u,v,w)$ by $(v,w,u)$ and
$(w,u,v)$, respectively. Their determinant product is $-1$.
Writing $r_a=u/w$, $s_a=u/w-1-u$ and cycling the suffixes gives
$$
\operatorname{tr}(M_cM_bM_a)
=s_as_bs_c+s_cr_b+r_cs_a+s_br_a=-uvw.
$$
The last equality follows by expanding the four terms and substituting
$w=-u-v$; it is an identity of rational functions wherever $uvw\ne0$.
Consequently
$$
\det D\kappa^3=-1,\qquad
(\operatorname{tr}D\kappa^3)^2=(uvw)^2=\operatorname{Disc}(D).
$$
Since the point is fixed by $\kappa^3$ and $F^3=G^6$, the reduced
return derivative is $(D\kappa^3)^2$. For a two-by-two matrix,
$\operatorname{tr}(M^2)=(\operatorname{tr}M)^2-2\det M$. Hence
$$
\det D\phi^3=1,\qquad
\operatorname{tr}D\phi^3=2+\operatorname{Disc}(D).             \tag{15}
$$
For a real three-cycle, $D$ has three distinct real roots, so its
discriminant is positive. Equation (15) gives two positive reciprocal
reduced multipliers, one larger and one smaller than one. This is
hyperbolicity on the two-dimensional reduced surface. It does not
remove the symmetry-induced neutral directions in the full phase space.

### 11. Odd-period inverse constructions do not solve fixed-$h$ counting

For any odd $n\ge3$ and $r\ge n$, one can construct real simple
momentum values admitting exact nonvanishing period $n$. Take distinct
real numbers $a_0,\ldots,a_{n-1}$ and let $E_0$ be the degree-less-than-
$n$ interpolation polynomial with
$$
E_0(a_j)=(a_j-a_{j-1})(a_{j+1}-a_j)\ne0.
$$
Choose a monic degree-$r-n$ polynomial $L_0$ with simple real roots
different from all $a_j$; use $L_0=1$ when $r=n$. Set
$D_0=\prod_j(z-a_j)$. For a positive real parameter $t$, define
the monic degree-$r$ polynomial by
$$
h_t(tz)=t^rD_0(z)L_0(z)+t^2E_0(z).            \tag{16}
$$
The values $z_j=ta_j$ satisfy (7). Since
$h_t(tz)/t^r\to D_0(z)L_0(z)$ as $t\to\infty$ and the latter has
simple real roots, the real implicit-function theorem at each root
shows that for all sufficiently large $t$ the polynomial $h_t$ has
$r$ simple real roots. Translate one of those roots to zero to meet
the convention $c_r=0$. Translation preserves all differences in
(7). The scalar $\kappa$ cycle has exact period $n$ because its
values are distinct, and (13) yields exact $F$-period $n$ on its
nonvanishing real torus fibers.

This is a symbolic inverse construction within the same system family,
not a numerical zero fit or a statement for a preassigned momentum
fiber. It does not count odd cycles for any fixed arbitrary $h$, and
does not supply the missing general-period converse.

## Corrections and missing assumptions

- The degree threshold is $n\le s$ for $s$ distinct momentum values;
  in the simple case it is $n\le r$. Multiplicity does not give extra
  root conditions on $A-B$.
- Nonvanishing is essential for the multiplier formula and the simple
  low-period exclusions. Coordinate-divisor cycles are not classified.
- The cubic classification is complete for $s\ge3$, but its unique
  closed formula uses $r=3$. For larger $r$, solving (9) for all
  monic squarefree cubics remains an algebraic problem.
- The four-period exclusion needs $A=B$, guaranteed by $s\ge4$;
  it does not decide the rank-three four-period problem.
- The five-period converse assumes distinct integer-time $x$ values.
- No claim is made that the polynomial threshold is dynamically sharp,
  that every balanced orbit is a quotient odd cycle of $G$, or that
  every quotient periodic orbit lifts periodically.

## Limited primary-source check and value assessment

A bounded public search was run on 2026-09-05 for relative-periodic
reconstruction, anti-symplectic torus inversion, and periodic points
of Danielewski-surface automorphisms. This is a collision check, not
an exhaustive novelty certificate.

- Wulff and Roberts, *Hamiltonian Systems Near Relative Periodic
  Orbits*, [SIAM journal page](https://epubs.siam.org/doi/10.1137/S1111111101387760),
  treats dynamics near relative periodic orbits as periodically forced
  transverse motion together with motion along the group orbit.
  It provides existing reconstruction context, not the exact formula
  (9) or a theorem that directly proves this discrete classification.
- Fassò, García-Naranjo and Giacobbe, *Quasi-periodicity in relative
  quasi-periodic tori*, [author preprint](https://arxiv.org/abs/1411.7976),
  describes reconstruction and distinguishes relative-periodic from
  relative-quasiperiodic difficulties. Nothing in the inspected
  abstract establishes novelty of the present low-period calculation.
- Leuenberger and Regeta, *Automorphism Groups of Danielewski
  Surfaces*, [author preprint](https://arxiv.org/abs/1710.06045),
  concerns the established automorphism-group setting for
  $xy=p(z)$ with simple roots. It is background, not evidence that
  the specific lifted-period formula is already published.
- Abboud, *Rigidity of periodic points for loxodromic automorphisms
  of affine surfaces*, [author preprint](https://arxiv.org/abs/2406.11510),
  addresses equality and density of periodic-point sets on affine
  surfaces. Its abstract does not classify the torus return elements
  or low periods computed here.

No exact prior statement of (9), (10), or (15) was identified in this
limited check. That negative search result must not be converted into
an originality claim. More importantly, the internal proof gives a
reason for caution independent of literature: the main lifting theorem
is the two-line identity (13), while the rank-three classification and
stability formula are finite low-degree computations.

**Action-changing conclusion.** Keep these proved results as a useful
family-specific lemma package. They refute the idea that actual
nonvanishing periodic lifts are automatically absent, and give explicit
real periodic families. They do not yet justify a substantial independent
Paper29. A genuinely stronger fixed-$h$ classification/counting theorem,
or a new general converse with a complete proof, would be needed to
change that assessment. Do not pad the present package with repeated
reduction material or advertise the open converse as solved.

## Open risks

1. No classification on coordinate divisors or collided momentum fibers.
2. No full classification of balanced cycles for arbitrary $n$; even
   the repeated-$x$ five-period case has not been closed here.
3. No proof or counterexample establishing dynamical sharpness at $n=r+1$.
4. No full-phase-space stability or persistence theorem; (15) is reduced.
5. No exhaustive literature or Papers1–28 collision clearance. These
   remain separate from the correctness proofs in this bounded report.

The symbolic checks used during exploration only expanded the
permutation compatibility equations and the three-cycle derivative.
All claims marked proved above have their algebraic arguments displayed;
finite CAS output is not used as a substitute for proof.
