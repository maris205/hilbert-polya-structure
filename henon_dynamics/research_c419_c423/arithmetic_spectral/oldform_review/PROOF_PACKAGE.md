# AS2 independent proof package: the principal oldform block

Date: 2026-09-07 UTC. Independent review of the coordinator's frozen
prime-power question, not an admission or a proof of the original
all-level conjecture.

## Claim

For every prime $p$, every integer $e\geq 0$, and
$x=p^s=\exp(s\log p)$, define
$$
C(x)_{j,a}=x^{e-\min(2a,e)+2\min(a,j)-j},\qquad 0\leq j,a\leq e.
$$
Put $y=p/x=p^{1-s}$ and, initially when $x^2\ne1$,
$$
P_{p,e}(s)=C(x)^{-1}C(y).
$$
There is an explicitly specified basis depending only on $p,e$, not on
$s$, which diagonalizes every $P_{p,e}(s)$. Consequently the entire
meromorphic family is pairwise commuting wherever its values are
regular. Moreover this is the genuine principal, denominator-class
constant scattering block for $\Gamma_0(p^e)$ with width-one cusp
scalings, after removal of the common level-one scalar scattering
factor. Passing to orthonormal class channels uses a fixed similarity.

## Status

PROVABLE AS STATED for the claim above.

The claim above is the exact independent-review subtask. It is not the
full statement in [AS2_CONJECTURE.md](../AS2_CONJECTURE.md). In
particular, this proof says nothing that would remove the separately
reported nonprincipal-character obstruction at level $50$.

## Assumptions and notation

- The nebentypus is trivial. Only the oldforms of the level-one
  Eisenstein series, or equivalently the denominator-class constant
  cusp channel, are being considered.
- $\mathbf e_0,\ldots,\mathbf e_e$ is the fixed coordinate basis indexed
  by cusp denominator $p^a$; $J\mathbf e_a=\mathbf e_{e-a}$.
- $m=\lfloor e/2\rfloor$, $r=y/x=p/x^2$, and
  $d_a=\mathbf e_a-\mathbf e_{a+1}$.
- Euler's totient is denoted by $\varphi$, with $\varphi(1)=1$.
  The number of cusps of denominator $p^a$ is
  $\mu_a=\varphi(p^{\min(a,e-a)})$; write
  $D_\mu=\operatorname{diag}(\mu_0,\ldots,\mu_e)$.
- The standard level-one series is normalized to have constant term
  $Y^s+\phi_1(s)Y^{1-s}$. A capital $Y$ is used here for the
  hyperbolic height to distinguish it from $y=p^{1-s}$.

## Proof strategy

First verify the width-one incoming/outgoing matrix independently.
Then diagonalize the rational matrix family by fixed differences on
the two halves of the denominator chain. Two elementary reciprocal
polynomial identities supply the remaining central channel or channels.
No parameter-dependent conjugacy is used to compare two scattering
matrices.

## Dependency map

1. The arithmetic matrix formula follows from reduction of a rational
   cusp under $z\mapsto p^jz$ and the level-one constant term. The
   Eisenstein-basis identity is also a direct specialization of the
   primary source cited in Step 1.
2. Invertibility follows from elimination on the matrix
   $(x^{-|j-a|})_{j,a}$.
3. Left and right difference vectors are handled by a finite geometric
   sum and reversal.
4. The even central vector uses a reciprocal polynomial of even degree;
   the two odd central vectors use a related reciprocal quotient.
5. Dimension and support arguments show these vectors form a basis.
6. Meromorphic continuation, a fixed multiplicity similarity, and
   optionally a tensor product give the stated scattering consequence.

## Proof

### Step 1. Width-one applicability and the precise reduced matrix

Let a cusp be $u/p^a$, with $(u,p)=1$ when $a>0$, and set
$$
w_a=p^{e-\min(2a,e)}.
$$
Choose $\gamma\in\mathrm{SL}_2(\mathbb Z)$ with first column
$(u,p^a)^{\mathsf T}$. A width-one scaling carrying infinity to this
cusp is
$$
\sigma=\gamma\operatorname{diag}(\sqrt{w_a},1/\sqrt{w_a}).
$$
The transformation $z\mapsto p^jz$ is represented in
$\mathrm{SL}_2(\mathbb R)$ by
$\alpha_j=\operatorname{diag}(p^{j/2},p^{-j/2})$.
Let $g=p^{\min(a,j)}$, and choose
$\delta\in\mathrm{SL}_2(\mathbb Z)$ with first column
$(p^ju/g,p^a/g)^{\mathsf T}$. The first column of
$\alpha_j\sigma$ is $t$ times this primitive integral column, where
$$
t=g\sqrt{w_a/p^j}>0.
$$
Hence $\delta^{-1}\alpha_j\sigma$ is upper triangular with diagonal
$(t,t^{-1})$, and its action multiplies hyperbolic height by
$$
t^2=p^{e-\min(2a,e)+2\min(a,j)-j}.
$$
Level-one modular invariance gives incoming coefficient $C(x)_{j,a}$
and outgoing coefficient $\phi_1(s)C(y)_{j,a}$ for
$E(p^jz,s)$. Both are independent of the representative $u$.
The translations in the upper triangular matrix do not affect either
coefficient. Since $p^j\mid p^e$, conjugation of $\Gamma_0(p^e)$ by
$\alpha_j$ lies in $\mathrm{SL}_2(\mathbb Z)$, so these really are
level-$p^e$ oldforms.

For completeness, the exact expansion into incoming cusp series is the
trivial-character specialization of Booker--Lee--Strömbergsson,
*Twist-minimal trace formulas and the Selberg eigenvalue conjecture*,
arXiv:1803.06016v2 (17 April 2020),
[Section 2.7, Lemma 2.19 and Remark 2.20](https://arxiv.org/html/1803.06016v2#S2.SS7).
Their level-one primitive-pair series is twice our normalized $E$;
that common factor cancels. Their Section 2.5 also gives the width
scalings and the cusp equivalence relation producing $\mu_a$.
These particular formulas were directly accessed for this review;
no claim to a new incoming-coefficient formula is made.

Define $\mathcal E_a(z,s)$ to be the sum of the standard incoming
Eisenstein series over the $\mu_a$ cusps of denominator $p^a$.
Its incoming coefficient at each cusp of its class is $1$.
The expansion just verified is
$$
E(p^jz,s)=\sum_{a=0}^e C(x)_{j,a}\mathcal E_a(z,s).
$$
The outgoing coefficient of the left side is independent of the cusp
representative at each denominator. Once $C(x)$ is invertible, the
same is true for every $\mathcal E_a$. Thus the denominator-class
constant channel is invariant, and its row-convention scattering
matrix is exactly $\phi_1(s)P_{p,e}(s)$, because
$$
C(x)\bigl(\phi_1(s)P_{p,e}(s)\bigr)=\phi_1(s)C(y).
$$
This argument does not discard a nontrivial-character term from a full
scattering matrix; it proves invariance of this particular subspace.

### Step 2. Invertibility and reversal

Write $q_a=\max(a,e-a)$. The exponent in the definition of $C$ is
$q_a-|j-a|$, so
$$
C(x)=K(x)\operatorname{diag}(x^{q_a}),
\qquad K(x)_{j,a}=x^{-|j-a|}.
$$
With $t=x^{-1}$, subtract $t$ times row $j-1$ from row $j$ of $K$,
in descending order $j=e,e-1,\ldots,1$. The resulting matrix is upper
triangular with diagonal $1,1-t^2,\ldots,1-t^2$. Therefore
$$
\det C(x)=x^{\sum_a q_a}(1-x^{-2})^e.
$$
It is nonzero for $x\ne0$ and $x^2\ne1$. For $e=0$, it is $1$.
Also $q_{e-a}=q_a$ and $|(e-j)-(e-a)|=|j-a|$, which prove
$C(x)J=JC(x)$.

### Step 3. Fixed left and right eigenvectors

For each $0\leq b\leq m-1$ set
$$
v_b^L=\sum_{a=0}^b p^a d_a,
\qquad v_b^R=Jv_b^L.
$$
Since $a,a+1\leq m$, direct subtraction of the corresponding columns
gives
$$
(C(x)d_a)_j=
\begin{cases}
(x^2-1)x^{e-2a+j-2},&0\leq j\leq a,\\
0,&a+1\leq j\leq e.
\end{cases}
$$
It follows that
$$
(C(x)v_b^L)_j=
\begin{cases}
(x^2-1)x^{e+j-2}\displaystyle\sum_{a=j}^b r^a,
   &0\leq j\leq b,\\
0,&j>b.
\end{cases}
$$
Replacing $x$ by $y$ replaces $r=p/x^2$ by $r^{-1}$, and
$$
\sum_{a=j}^b r^{-a}=r^{-(j+b)}\sum_{a=j}^b r^a.
$$
Thus, without dividing by a possibly zero finite sum,
$$
C(y)v_b^L=\lambda_b(s)C(x)v_b^L,
\qquad
\lambda_b(s)=\frac{y^2-1}{x^2-1}r^{e-2-b}.
$$
Reversal proves the identical formula for $v_b^R$.
After multiplying by $C(x)^{-1}$, both are fixed eigenvectors of
$P_{p,e}(s)$ with the displayed common eigenvalue.

### Step 4. The even central channel

Suppose $e=2m$ with $m\geq1$, and put
$$
v^{\mathrm{cen}}=\sum_{a=0}^{2m}\mu_a\mathbf e_a.
$$
We have $\sum_{a=0}^j\mu_a=p^j$ for $0\leq j\leq m$.
For $0\leq j<m$, summing the three ranges $a\leq j$,
$j<a\leq m$, and $a>m$ gives
$$
(C(x)v^{\mathrm{cen}})_j=p^jx^jQ_{m-j}(x),
$$
where, for $h\geq1$,
$$
Q_h(X)=X^{2h}+(p-1)\sum_{b=1}^{h-1}p^{b-1}X^{2h-2b}+p^h.
$$
At $j=m$ the result is $p^{m-1}(p+1)x^m$.
The coefficients of $Q_h$ in reverse order give the exact polynomial
identity
$$
Q_h(p/X)=p^hX^{-2h}Q_h(X).
$$
For the endpoint coefficients this pairs $1$ with $p^h$; for an
interior coefficient it uses
$(p-1)p^{h-b-1}=p^{h-2b}(p-1)p^{b-1}$.
Consequently every row $0\leq j\leq m$ satisfies
$$
(C(y)v^{\mathrm{cen}})_j=r^m(C(x)v^{\mathrm{cen}})_j.
$$
The remaining rows obey the same identity because the vector and the
matrix are invariant under reversal. Hence
$v^{\mathrm{cen}}$ is a fixed eigenvector with eigenvalue $r^m$.
When $e=0$, $C(x)=P_{p,0}(s)=(1)$ and the same conclusion holds with
$m=0$ and $v^{\mathrm{cen}}=\mathbf e_0$.

### Step 5. The two odd central channels

Suppose $e=2m+1$, including $m=0$. Put
$$
u_L=\sum_{a=0}^m\varphi(p^a)\mathbf e_a,\qquad
u_R=Ju_L,\qquad v_\varepsilon=u_L+\varepsilon u_R
\quad(\varepsilon\in\{1,-1\}).
$$
For $0\leq j\leq m$, set $h=m-j$. The same explicit range summation
now gives
$$
(C(x)v_\varepsilon)_j=p^jx^jT_h^\varepsilon(x),
$$
where
$$
T_h^\varepsilon(X)=X^{2h+1}
 +(p-1)\sum_{b=1}^h p^{b-1}X^{2h+1-2b}
 +\varepsilon p^h.
$$
The sum is empty for $h=0$. Its value at $X=-\varepsilon$ is zero,
so $U_h^\varepsilon(X)=T_h^\varepsilon(X)/(X+\varepsilon)$ is a
polynomial. Finite geometric summation gives the useful rational
presentation
$$
U_h^\varepsilon(X)
=\frac{X^{2h+2}-\varepsilon X^{2h+1}
       +\varepsilon p^hX-p^{h+1}}{X^2-p}.
$$
The numerator evaluated at $p/X$ is $-p^{h+1}X^{-2h-2}$ times
the numerator at $X$, while
$(p/X)^2-p=-pX^{-2}(X^2-p)$. Thus
$$
U_h^\varepsilon(p/X)=p^hX^{-2h}U_h^\varepsilon(X).
$$
This is a polynomial identity after clearing powers of $X$; the
intermediate expression has no exclusion at $X^2=p$.
Restoring the factor $X+\varepsilon$ yields
$$
C(y)v_\varepsilon
=r^m\frac{y+\varepsilon}{x+\varepsilon}C(x)v_\varepsilon.
$$
We obtained this for the left rows. For the right rows it follows
from $Jv_\varepsilon=\varepsilon v_\varepsilon$ and $JC=CJ$.
The two fixed central eigenvalues are therefore
$$
\lambda_\varepsilon^{\mathrm{cen}}(s)
=r^m\frac{y+\varepsilon}{x+\varepsilon}.
$$

### Step 6. Basis, commutativity and exceptional parameters

The vectors $v_b^L$ span the same subspace as $d_0,\ldots,d_{m-1}$:
the coefficient array is triangular with nonzero diagonal $p^b$.
The corresponding statement holds on the right by reversal.

For $e=2m$, the left difference space consists of vectors supported
in $[0,m]$ with coordinate sum zero. The right space has support
$[m,2m]$ and coordinate sum zero. Their intersection is zero because
a vector in it could be supported only at $m$, but would have sum
zero. Their direct sum has dimension $2m$. The central vector has
positive coordinate sum and so is outside that sum. This gives
$e+1$ linearly independent fixed vectors.

For $e=2m+1$, the two support intervals $[0,m]$ and $[m+1,2m+1]$
are disjoint. Each difference space has codimension one on its
interval; $u_L$ and $u_R$, each of coordinate sum $p^m$, supply the
respective complements. Their sum and difference are also independent.
This again gives $e+1$ fixed vectors.

Let $B_{p,e}$ be the matrix formed from these vectors in any fixed
order. Steps 3--5 prove
$$
P_{p,e}(s)=B_{p,e}\Lambda_{p,e}(s)B_{p,e}^{-1}
$$
with $B_{p,e}$ independent of $s$ and $\Lambda_{p,e}$ diagonal.
Therefore
$$
[P_{p,e}(s),P_{p,e}(t)]=0.
$$
The identity first holds away from the finitely specified rational
denominators in $p^s,p^t$ and then holds identically as a meromorphic
matrix identity. If multiplication by $\phi_1$ removes a displayed
singularity, the identity also holds at that regular value of the
actual scattering block, by taking limits. Repeated eigenvalues cause
no difficulty: the same explicit basis remains a basis. This includes
$s=1/2$, where $x=y$ and $P_{p,e}(s)=I$.

### Step 7. Fixed cusp multiplicities and composite principal levels

Normalize the fixed class series as
$\widehat{\mathcal E}_a=\mathcal E_a/\sqrt{\mu_a}$. Their incoming
class indicators form an orthonormal basis in the full finite cusp
space with counting measure. The reduced row-convention scattering
matrix in this basis is
$$
\phi_1(s)D_\mu^{-1/2}P_{p,e}(s)D_\mu^{1/2}.
$$
Indeed the outgoing coefficient at a target cusp of class $b$ is
divided by $\sqrt{\mu_a}$, and expressing that constant in the
normalized target indicator multiplies it by $\sqrt{\mu_b}$.
Both diagonal matrices are fixed. A column-coefficient convention
transposes the family, which also preserves vanishing of all
commutators. No $s$-dependent weighting is permitted or needed.

As an immediate principal-sector corollary, for any positive integer
$N=\prod p^{e_p}$ and divisor coordinates ordered multiplicatively,
the same cusp reduction gives
$$
C_N(s)_{d,c}=
\left(\frac{N\gcd(d,c)^2}{d\gcd(c^2,N)}\right)^s
=\bigotimes_{p\mid N} C_{p,e_p}(p^s).
$$
It follows that the principal reduced matrix is
$\bigotimes_{p\mid N}P_{p,e_p}(s)$ and has the fixed tensor-product
basis $\bigotimes B_{p,e_p}$. This establishes only the principal
channel at general level, not commutativity of the full cusp matrix.
The proof of the claim is complete. $\square$

## Algebraic real-sign corollary, with its applicability boundary

Let $\eta\in\{1,-1\}$ and suppose a proposed local incoming matrix
is exactly
$$
C_\eta(x)_{j,a}=\eta^{|j-a|}C(x)_{j,a}.
$$
Set $D_\eta=\operatorname{diag}(1,\eta,\ldots,\eta^e)$.
Since $\eta^{|j-a|}=\eta^{j+a}$ and $D_\eta^2=I$,
$$
C_\eta(x)=D_\eta C(x)D_\eta,
\qquad
C_\eta(x)^{-1}C_\eta(y)=D_\eta P_{p,e}(s)D_\eta.
$$
The latter family is therefore pairwise commuting in a fixed basis.
This is an algebraic conditional corollary. The precise primitive-pair
normalization, conjugate-character block and any other local scalars
must still be supplied by the separate full-level analysis; they have
not been silently inferred here.

## Corrections or missing assumptions

None for the principal claim. The necessary restrictions to the
principal channel and to fixed width-one cusp coordinates are explicit.
Dropping the principal-channel restriction would assert a different,
unproved statement, and does not follow from the calculation.

## Open risks and classical-substance assessment

The incoming coefficient formula and the general Eisenstein decomposition
are classical inputs. The displayed diagonalization is an elementary
algebraic consequence of those inputs, with no new dynamical clock,
Euler factor, or Hilbert--Pólya realization. An independent derivation
does not establish literature novelty. This principal-sector result
alone should be treated as a verification lemma, not a paper admission.

This review did not classify nonprincipal blocks, prove the proposed
repaired all-level criterion, or audit the independently reported
level-$50$ counterexample. Those remain separately owned obligations.
No numerical evidence is used in the proof. The coordinator's existing
40-cell calculation was inspected through its source and receipt but
was not rerun, and no new mathematical computation was executed here.
