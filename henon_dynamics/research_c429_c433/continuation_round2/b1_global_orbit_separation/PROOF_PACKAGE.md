# Proof Package — the scope of polynomial invariant separators

2026-09-09 UTC. B1, Round 2. This is an auxiliary proof package, not an
admitted paper or a proof of LG4. No mathematical program was used.

## Claim

The original claim is left unchanged. For every polynomial automorphism
$F\in\operatorname{Aut}_{\mathbb Z}(\mathbb A^2)$ and $P,Q\in\mathbb Z^2$,
does
$$
\bigl[\forall m\ge2\ \exists n_m\in\mathbb Z:
F^{n_m}(P)\equiv Q\pmod m\bigr]
\quad\Longrightarrow\quad
Q\in\{F^n(P):n\in\mathbb Z\}?                     \tag{LG4}
$$
Here $\operatorname{Aut}_{\mathbb Z}$ means that both $F$ and its inverse
have integer polynomial coordinates. In particular, every finite reduction
of $F$ is a permutation. All mixed moduli and both signs of time remain in
the original claim.

This package proves two auxiliary statements and an exact finite control.

**BDQ — bounded-degree quotient limitation.** Suppose additionally that
$\mathbb Q[x,y]^F=\mathbb Q$. For each integer $D\ge1$ there is an explicitly
specified positive integer $\Delta(F,D)$ with the following property. For
every $m\ge2$, every degree-at-most-$D$ polynomial
$h\in(\mathbb Z/m\mathbb Z)[x,y]$ satisfying
$$
h(F(z))=h(z)\quad\text{for every }z\in(\mathbb Z/m\mathbb Z)^2,       \tag{1}
$$
and every $P,Q\in\mathbb Z^2$,
$$
P\equiv Q\pmod{\Delta(F,D)}\quad\Longrightarrow\quad
h(P)=h(Q)\pmod m.                                                   \tag{2}
$$
The modulus and coefficients of $h$ may vary independently and there is no
limit on the number of tested polynomials.

**UPI — unrestricted polynomial-invariant equivalence.** No no-invariant
hypothesis is needed for this statement. For fixed $F,P,Q$, the following
conditions are equivalent:

1. For every $m\ge2$ and every $h\in(\mathbb Z/m\mathbb Z)[x,y]$ satisfying
   (1), without a degree restriction, $h(P)=h(Q)\pmod m$.
2. For every prime $p$ and integer $r\ge1$, $P$ and $Q$ belong to the same
   finite $F$-cycle modulo $p^r$.

If condition 2 fails at $q=p^r$, one can construct an invariant separator
modulo $p^K$ of total degree at most $2(q-1)$, where
$$
K=2v_p((q-1)!)+1.                                                   \tag{3}
$$
The increase from modulus $p^r$ to $p^K$ is allowed because condition 1
quantifies over every modulus.

**Finite mixed-phase control.** For
$$
F(x,y)=(y,x+6y^2),\qquad P=(0,1),\quad Q=(4,3),                     \tag{4}
$$
$Q$ is not in the orbit of $P$ modulo $6$, but every invariant polynomial
function modulo $6$, of any degree, takes equal values at $P$ and $Q$.
This is a statement at one modulus, not a counterexample to LG4 or UPI.

## Status

- Original LG4: `NOT CURRENTLY JUSTIFIED`.
- BDQ, with its stated no-invariant assumption: `PROVABLE AS STATED`.
- UPI and the finite mixed-phase control: `PROVABLE AS STATED`.
- Paper admission and novelty: not claimed. The interpolation and primary
  decomposition mechanisms are established mathematics; see source
  ownership below. The present output records their exact dynamical scope.

## Assumptions and notation

- $F=(F_1,F_2)$ and $F^{-1}$ lie in $\mathbb Z[x,y]^2$.
- $\mathbb Q[x,y]^F=\{g\in\mathbb Q[x,y]:g\circ F=g\}$; this condition is
  used only for BDQ and its explicit Hénon application.
- $\deg$ means total polynomial degree. The phrase “degree at most $D$”
  refers to existence of a polynomial representative of that degree.
- $h\circ F=h$ in (1) is equality of functions on the finite residue set,
  not an identity of formal polynomials. The proof never identifies these
  two notions over a finite ring.
- $v_p$ is the usual valuation of a nonzero integer, normalized by
  $v_p(p)=1$.
- $C_m(P)$ is the full cycle of the reduction of $P$ under the permutation
  induced by $F$ on $(\mathbb Z/m\mathbb Z)^2$.
- Binomial polynomials $\binom{T}{j}$ are evaluated as rational polynomials
  before reduction. Their values at every integer, including negative
  integers, are integers.

## Proof strategy

For BDQ, evaluate the coboundaries of a finite monomial basis on an exact
integer interpolation grid. A full-rank integer minor then bounds the
torsion of every coefficient vector modulo every integer. No determinant
or factorial is inverted in a residue ring.

For UPI, interpolate the indicator of a separated prime-power cycle by
integer-valued rational polynomials. Clearing denominators while increasing
the prime-power modulus turns it into an ordinary integer polynomial
separator. The converse uses the Chinese remainder theorem (CRT) on values,
which also explains the missing cross-prime time information.

## Dependency map

1. BDQ uses the integer-grid lemma, rational interpolation, the stated
   no-invariant assumption, and the adjugate identity for an integer minor.
2. The concrete BDQ false-positive family uses an independently proved
   no-invariant fact for a generalized Hénon map and elementary orbit growth.
3. UPI uses integer-valued binomial interpolation, its prime-power
   periodicity modulo $p$, denominator clearing, and CRT.
4. The finite mixed-phase control uses only the explicit inverse of (4)
   and two finite swap cycles.
5. None of these dependencies supplies the missing implication in LG4.

## Proof

### Step 1. An integer grid detects zero functions over every residue ring

**Grid lemma.** Let $A\in\mathbb Z[x,y]$ have degree at most $L$ in each
variable separately, where $L\ge0$. For every integer $m\ge2$,
$$
A(u,v)\equiv0\pmod m\quad(0\le u,v\le L)
\quad\Longleftrightarrow\quad
A(u,v)\equiv0\pmod m\quad((u,v)\in\mathbb Z^2).                     \tag{5}
$$

For the nontrivial implication, let $\nabla_x A(x,y)=A(x+1,y)-A(x,y)$
and define $\nabla_y$ in the other variable. The Newton expansion is the
rational-polynomial identity
$$
A(x,y)=\sum_{i=0}^{L}\sum_{j=0}^{L}
c_{ij}\binom{x}{i}\binom{y}{j},\qquad
c_{ij}=(\nabla_x^i\nabla_y^jA)(0,0).                              \tag{6}
$$
To verify it, in one variable the polynomials $\binom{T}{j}$ form a basis
of degree-at-most-$L$ rational polynomials and satisfy
$\nabla\binom{T}{j}=\binom{T}{j-1}$. Applying this basis expansion in
each variable yields (6). Explicitly,
$$
c_{ij}=\sum_{u=0}^{i}\sum_{v=0}^{j}
(-1)^{i-u+j-v}\binom{i}{u}\binom{j}{v}A(u,v).                      \tag{7}
$$
Thus every $c_{ij}$ is an integer divisible by $m$ under the grid
hypothesis. Every product of binomial values in (6) is an integer at an
integer point, including a point with negative coordinates. Equation (6)
therefore proves divisibility by $m$ at every integer point. The reverse
implication in (5) is restriction to the grid. This argument does not
divide by a factorial modulo $m$. Repeated grid residues when $L\ge m$
cause no problem. $\square$

### Step 2. The precise matrix and a nonzero integer minor

Set
$$
d=\max(\deg F_1,\deg F_2)\ge1,\quad L=dD,\quad
N=\frac{(D+1)(D+2)}2-1.
$$
List the nonconstant monomials of total degree at most $D$ as
$b_1,\ldots,b_N$, ordering first by total degree and then by the exponent
of $x$. Order $G=\{0,\ldots,L\}^2$ lexicographically. Define the integer
matrix $M$ with row set $G$ and $N$ columns by
$$
M_{(u,v),j}=b_j(F(u,v))-b_j(u,v).                                  \tag{8}
$$
This is the promised exact finite evaluation set, independent of $m$.

The matrix has full column rank over $\mathbb Q$. Indeed, if a rational
vector $a=(a_1,\ldots,a_N)$ satisfies $Ma=0$, put
$g=\sum_j a_jb_j$. The polynomial $g\circ F-g$ has total degree at most
$L$ and vanishes on $G$. Rational interpolation on the $(L+1)$ distinct
values in each variable implies that this polynomial is identically zero:
fixing $y\in\{0,\ldots,L\}$ first kills the polynomial in $x$, and then
interpolating its coefficients in $y$ kills each coefficient. Therefore
$g\in\mathbb Q[x,y]^F=\mathbb Q$. Its constant coefficient is zero, so
$g=0$ and $a=0$.

Let $B$ be the square $N\times N$ submatrix of $M$ with the
lexicographically first ordered $N$-element row set for which the
determinant is nonzero. Full column rank guarantees such a set. Define
$$
\Delta(F,D)=|\det B|\ge1.                                         \tag{9}
$$
This is an effective symbolic definition, not a claim that a determinant
was numerically computed. No Gram matrix is needed.

### Step 3. Function invariance is exactly the matrix congruence

For $h=c+\sum_j a_jb_j$ over $\mathbb Z/m\mathbb Z$, choose arbitrary
integer lifts of the coefficients. The resulting integer polynomial
$A=h\circ F-h$ has degree at most $L$ in each variable. Consequently (5)
gives the equivalence
$$
h(F(z))=h(z)\ (z\in(\mathbb Z/m\mathbb Z)^2)
\quad\Longleftrightarrow\quad Ma=0\pmod m.                         \tag{10}
$$
The left-to-right direction follows by evaluation on the grid. In the
other direction, (5) shows the integer lift vanishes modulo $m$ at every
integer point, hence on every residue class. Changing coefficient lifts
adds a multiple of $m$ and does not change either condition.

In particular, pointwise invariants that are not formal polynomial
invariants are included in (10); they are not discarded by the matrix.

### Step 4. The adjugate gives the all-modulus BDQ conclusion

From $Ma=0\pmod m$ we get $Ba=0\pmod m$. Multiplying by the integer
adjugate of $B$ gives
$$
\Delta(F,D)a_j=0\pmod m\quad(1\le j\le N).                         \tag{11}
$$
The possible sign of $\det B$ has no effect on this congruence. Put
$g_m=\gcd(m,\Delta(F,D))$. For integer lifts of the $a_j$, (11) implies
$$
\frac m{g_m}\mid a_j.                                             \tag{12}
$$
To see this without illegal cancellation, write $m=g_mm'$ and
$\Delta=g_m\Delta'$ with $\gcd(m',\Delta')=1$. Divisibility of
$\Delta a_j$ by $m$ is equivalent to $m'\mid\Delta'a_j$, and Bézout's
identity gives $m'\mid a_j$.

If $P\equiv Q\pmod\Delta$, then $P\equiv Q\pmod{g_m}$ and
$g_m\mid b_j(P)-b_j(Q)$ for every monomial. Multiplying this divisibility
with (12) yields
$$
h(P)-h(Q)=\sum_{j=1}^N a_j\bigl(b_j(P)-b_j(Q)\bigr)\equiv0\pmod m.
$$
The constant coefficient cancels. This proves BDQ for every $m$, including
all bad-prime powers and every mixed modulus. In particular, when
$\gcd(m,\Delta)=1$, (11) forces all nonconstant coefficients to vanish;
this special case was not used to omit the other moduli. $\square$

### Step 5. A concrete nonperiodic all-modulus false positive for each cutoff

For completeness, the required no-invariant hypothesis for the following
example is proved here. Let
$$
H(x,y)=(y,p(y)-a x),\qquad p\in\mathbb C[y],\quad
\deg p=e\ge2,\quad a\ne0.                                         \tag{13}
$$
There is no algebraic curve $C\subset\mathbb A^2_{\mathbb C}$ with
$H^r(C)=C$ for some $r\ge1$.

Suppose there were an irreducible such curve. Pass to its normalization
and smooth projective completion $\overline C$. The automorphism of $C$
induced by $H^r$ lifts to the normalization and extends to an automorphism
of $\overline C$: a birational map of nonsingular projective curves is an
isomorphism. It permutes the finite set $S$ of points omitted from the
affine normalization. At some $v\in S$, at least one coordinate function
$x,y$ has a pole, because otherwise both are regular functions on a
projective integral curve and hence constant, which cannot describe a
curve in the plane.

Write $u=-\operatorname{ord}_v(x)$ and $w=-\operatorname{ord}_v(y)$,
allowing negative integers and assigning $-\infty$ to an identically zero
coordinate function; then $\max(u,w)>0$. If $w\ge u$,
then $w>0$ and the pole orders of the two terms in $p(y)-a x$ are $ew$
and $u$, with $ew>u$. They cannot cancel. Under successive forward
iterates of $H$, the coordinate pole-order pairs therefore become
$$
(w,ew),\ (ew,e^2w),\ (e^2w,e^3w),\ldots.                          \tag{14}
$$
If $u>w$, then $u>0$ and the inverse
$H^{-1}(x,y)=(a^{-1}(p(x)-y),x)$ gives under successive backward
iterates the pairs
$$
(eu,u),\ (e^2u,eu),\ (e^3u,e^2u),\ldots.                          \tag{15}
$$
In either case, the coordinate pole orders at $v$ are unbounded even
along the iterates whose indices are multiples of $r$. On that
subsequence, however, they equal the orders of the fixed functions $x,y$
at points in the finite permutation orbit of $v$ in $S$. Those orders
are bounded. This contradiction proves the assertion for irreducible
curves, and the reducible case follows by taking a further iterate that
fixes an irreducible component.

If a nonconstant polynomial $g$ satisfied $g\circ H=g$, its nonempty
curve fibre $g=c$ would be preserved. Its finitely many irreducible
components would be permuted, contradicting the preceding conclusion.
Thus $\mathbb C[x,y]^H=\mathbb C$, and the corresponding rational
no-invariant assertion follows when $H$ is defined over $\mathbb Q$.

Now fix
$$
F_0(x,y)=(y,y^3-x),\qquad P=(1,2),\qquad
Q_D=(1+10\Delta(F_0,D),\,2).                                      \tag{16}
$$
This map and its inverse $(x^3-y,x)$ have integer coordinates. The
preceding argument verifies the no-invariant assumption, so BDQ applies.
The two points are congruent modulo $\Delta(F_0,D)$ and hence are
indistinguishable by every degree-at-most-$D$ invariant polynomial at
every modulus.

They are not on the same integer orbit. To prove this, define the
two-sided sequence by $a_0=1$, $a_1=2$ and
$a_{n+2}=a_{n+1}^3-a_n$. Then $F_0^nP=(a_n,a_{n+1})$. For
$n\ge0$, induction gives $0<a_n<a_{n+1}$, since for integers
$b>a>0$ with $b\ge2$ one has $b^3-a>b$. The backward terms satisfy
$$
a_{-r}=-a_{r-1}\qquad(r\ge1).                                    \tag{17}
$$
For $r=1$ this is $1^3-2=-1$. If (17) holds for two successive backward
terms, the recurrence proves it for the next one; the starting value
$a_{-2}=(-1)^3-1=-2$ supplies the second base case. Consequently the
second coordinate of $F_0^nP$ equals $2$ only at $n=0$. Since $Q_D\ne P$,
it is outside the two-sided orbit of $P$.

Both points are nonperiodic. The forward coordinates of $P$ are
unbounded by the strict positive integer growth just proved. Put
$u=1+10\Delta\ge11$ for $Q_D$. Its first backward image is
$(u^3-2,u)$, with first coordinate larger than the second and both
positive. Applying $(x,y)\mapsto(x^3-y,x)$ repeatedly preserves those
inequalities and strictly increases the first coordinate, so its
backward orbit is unbounded.

This is an all-modulus false positive for the bounded-degree test only.
The point $Q_D$ depends on $D$. The argument does not produce one pair
passing every degree, nor a pair passing the original orbit test. $\square$

### Step 6. Integer-valued interpolation of a prime-power cycle indicator

Let $q=p^r$ with $p$ prime and $r\ge1$. For $a\in\{0,\ldots,q-1\}$
define the rational Lagrange polynomial
$$
L_a(T)=\prod_{\substack{0\le j<q\\j\ne a}}\frac{T-j}{a-j}.
                                                                        \tag{18}
$$
It has degree $q-1$ and takes the values $L_a(b)=1$ if $b=a$ and $0$
otherwise for $0\le b<q$. Its Newton expansion is
$$
L_a(T)=\sum_{j=a}^{q-1}(-1)^{j-a}\binom ja\binom Tj.                \tag{19}
$$
Indeed, its $j$th difference at zero is the alternating sum of its values
at $0,\ldots,j$, which is zero for $j<a$ and
$(-1)^{j-a}\binom ja$ for $j\ge a$. Equation (19) proves that $L_a$
is integer-valued on all of $\mathbb Z$.

For $0\le j<q$, the function $t\mapsto\binom tj$ on integers has period
$q$ modulo $p$. The polynomial identity
$(1+X)^q=1+X^q$ in $\mathbb F_p[X]$ gives
$p\mid\binom qi$ for $0<i<q$. Vandermonde's identity then gives,
for every integer $t$,
$$
\binom{t+q}{j}
=\sum_{i=0}^j\binom qi\binom{t}{j-i}
\equiv\binom tj\pmod p.                                          \tag{20}
$$
Vandermonde's identity holds for negative $t$ as well, since it is a
rational-polynomial identity in $t$. Iterating (20) in both directions
and using (19) proves
$$
L_a(t)\equiv
\begin{cases}1,&t\equiv a\pmod q,\\0,&t\not\equiv a\pmod q
\end{cases}\pmod p.                                               \tag{21}
$$
Only the values, not the rational coefficients, are reduced modulo $p$.

Suppose $Q\notin C_q(P)$ and write $C=C_q(P)$ using coordinate
representatives in $\{0,\ldots,q-1\}^2$. Define
$$
f(x,y)=\sum_{(a,b)\in C}L_a(x)L_b(y)\in\mathbb Q[x,y].              \tag{22}
$$
This is integer-valued on $\mathbb Z^2$, has total degree at most
$2(q-1)$, and modulo $p$ its values are the indicator of membership in
$C$ modulo $q$. Since $F$ permutes the finite residue set and preserves
the full cycle $C$, it also preserves its complement. Hence
$$
f(F(z))-f(z)\in p\mathbb Z\quad(z\in\mathbb Z^2),\qquad
f(P)-f(Q)\equiv1\pmod p.                                          \tag{23}
$$

### Step 7. Clearing denominators constructs an ordinary polynomial separator

Let
$$
A_q=((q-1)!)^2,\qquad H=A_q f,\qquad s=v_p(A_q),\quad K=s+1.
                                                                        \tag{24}
$$
For each $L_a$, the denominator in (18), up to sign, is
$a!(q-1-a)!$, which divides $(q-1)!$. Thus $A_q$ clears every
coefficient denominator in (22), and $H\in\mathbb Z[x,y]$.
Multiplying (23) by $A_q$ shows
$$
H(F(z))-H(z)\in p^{s+1}\mathbb Z\quad(z\in\mathbb Z^2),\qquad
v_p(H(P)-H(Q))=s.                                                  \tag{25}
$$
Therefore the reduction of $H$ is an invariant polynomial function
modulo $p^K$ and separates $P$ from $Q$ there. Its degree is at most
$2(q-1)$, and (24) gives (3). Even if $p$ divides the clearing factor,
the separator survives because the modulus was raised to $p^{s+1}$;
one does not cancel $A_q$ inside a residue ring.

If condition 1 of UPI held while condition 2 failed, (25) would contradict
condition 1. This proves condition 1 implies condition 2.

### Step 8. CRT proves the converse and identifies what is missing

Assume condition 2 of UPI. Fix $m\ge2$ and an invariant polynomial
$h$ modulo $m$. For each exact prime-power divisor $p^r\Vert m$, the
reduction of $h$ modulo $p^r$ is invariant on every residue point: lift
any such point to an integer point and use (1). Since $Q\in C_{p^r}(P)$,
invariance along that finite cycle gives
$h(P)=h(Q)\pmod{p^r}$. CRT gives equality modulo $m$. This proves
condition 2 implies condition 1, completing UPI. $\square$

The CRT argument concerns values, not times. To make that distinction
exact, when $Q\in C_q(P)$ put $t_q=|C_q(P)|$ and choose a hitting time
$a_q$ modulo $t_q$. The complete set of hitting times modulo $q$ is
$$
\{n\in\mathbb Z:F^n(P)\equiv Q\pmod q\}=a_q+t_q\mathbb Z.         \tag{26}
$$
This follows because, in a permutation cycle of length $t_q$, two
iterates agree precisely when their indices differ by a multiple of
$t_q$. For $m=\prod_{i=1}^kq_i$ with distinct underlying primes, an
orbit hit modulo $m$ exists exactly when
$$
\bigcap_{i=1}^k(a_{q_i}+t_{q_i}\mathbb Z)\ne\varnothing.            \tag{27}
$$
Necessity follows by reducing a common hit; sufficiency follows by CRT
on the two point coordinates. The generalized CRT for congruences in
one integer says that (27) holds exactly when
$$
a_{q_i}\equiv a_{q_j}\pmod{\gcd(t_{q_i},t_{q_j})}
\quad(1\le i,j\le k).                                             \tag{28}
$$
For justification, for each prime dividing any $t_{q_i}$ select a
congruence with maximal exponent of that prime. Pairwise compatibility
ensures its reduction satisfies every smaller exponent. The selected
prime-power congruences have pairwise coprime moduli, so ordinary CRT
solves them all; the solution satisfies the original congruences.

UPI condition 2 asserts that each coset (26) is nonempty, without
asserting (28) across primes. This proof does not show whether the
all-level prime-power conditions for integral $F,P,Q$ might nonetheless
force those compatibilities through some additional dynamical theorem.
No all-level counterexample to that possible implication is claimed.

### Step 9. The explicit mixed-phase control

For (4), the inverse is
$F^{-1}(x,y)=(y-6x^2,x)\in\mathbb Z[x,y]^2$. Modulo $6$, the map
is the coordinate swap. Its cycle through $P$ is
$$
C_6(P)=\{(0,1),(1,0)\},
$$
which does not contain the reduction $(4,3)$ of $Q$.

Modulo $2$, however, $Q\equiv P$, so its hitting times are the even
integers. Modulo $3$, $Q\equiv F(P)$, so its hitting times are the odd
integers. The two local cycle lengths both equal $2$, and (28) fails.

For any invariant polynomial function $h$ modulo $6$, invariance and
these separate cycle hits imply $h(P)=h(Q)\pmod2$ and
$h(P)=h(Q)\pmod3$. Hence $h(P)=h(Q)\pmod6$, regardless of degree.
The set-theoretic indicator of $C_6(P)$ does separate the two points and
is invariant, so it cannot be represented by a polynomial over
$\mathbb Z/6\mathbb Z$.

This example fails the all-level prime-power condition: directly
reducing the four successive iterates modulo $4$ gives
$$
C_4(P)=\{(0,1),(1,2),(2,1),(1,0)\},
$$
whereas $Q\equiv(0,3)\pmod4$. Thus it cannot be misread as an
all-modulus or all-prime-power false positive. All listed iterations
are exact hand substitutions, not a mathematical program. $\square$

## Source ownership and subtraction

The interpolation input is not new. Uwe Schauz,
“Classification of Polynomial Mappings Between Commutative Groups,”
*Journal of Number Theory* **139** (2014), 1–28,
[DOI](https://doi.org/10.1016/j.jnt.2013.12.010),
[author preprint, arXiv:1212.5522v3](https://arxiv.org/pdf/1212.5522),
was checked at Theorem 2.5 (integer-grid information), Corollary 3.7 and
Theorem 3.8 (finite $p$-group interpolation), and Theorems 3.14–3.17
(primary-component decomposition). Its polyfracts are integer-valued
binomial expressions, not automatically ordinary coefficient polynomials
over the same residue ring. Steps 6–8 give a self-contained elementary
dynamical corollary with explicit denominator clearing and the resulting
modulus increase. Neither the interpolation machinery nor primary
decomposition is claimed as a new theorem. BDQ is an auxiliary integer
linear-algebra obstruction, not an independently admitted paper.

## Corrections or missing assumptions

1. BDQ requires $\mathbb Q[x,y]^F=\mathbb Q$; it is not asserted for
   automorphisms with nonconstant rational polynomial invariants. The
   concrete map (16) satisfies the assumption by Step 5.
2. UPI concerns invariant polynomial **functions**. Replacing them by
   formal polynomial identities would discard the separator constructed
   in Step 7 and would be a different, weaker test.
3. The UPI equivalence concerns all moduli on the polynomial side and
   all separate prime-power moduli on the orbit side. It is not an
   equality of the two tests at the same fixed modulus.
4. The fixed-degree false-positive pair varies with $D$; quantifiers
   cannot be interchanged to obtain an unrestricted-degree false positive.
5. The finite mixed-phase example cannot establish that separate
   prime-power membership at every level is strictly weaker than the
   all-mixed-modulus hypothesis for integral triples.

## Open risks and exact remaining interface

The auxiliary arguments above have no deliberately omitted proof step,
but await a nonauthor internal check. Particular audit targets are (5),
(10), the pole argument in Step 5, the integer-valued rather than
coefficientwise use of (21), the valuation in (25), and the quantifier
distinction after (28).

For an unrestricted polynomial-invariant strategy to prove LG4 by
separating **every** off-orbit integer point, UPI shows that it would
suffice, and be necessary for that strategy, to prove the stronger
prime-power separation assertion
$$
Q\notin\{F^n(P):n\in\mathbb Z\}
\quad\Longrightarrow\quad
\exists p,r:\ Q\notin C_{p^r}(P).                                 \tag{29}
$$
This package does not prove (29). It is stronger in its demanded
separating modulus than the contrapositive of LG4, which allows a mixed
modulus. Thus unbounded degree removes the fixed-degree obstruction but
does not supply the missing arithmetic theorem.

A viable quotient route that retains the full LG4 contract can instead
use the actual finite orbit quotient (set-theoretic cycle labels), or
retain the hitting-time cosets (26) and their cross-prime compatibilities
(28). A finite orbit indicator exists once a separating modulus is
known; producing that modulus uniformly for each off-orbit integer
point is exactly the unresolved mathematical task, not a consequence of
interpolation.

No conclusion about a general arithmetic height gap, no all-modulus
off-orbit pair, and no new paper admission follows from this package.
