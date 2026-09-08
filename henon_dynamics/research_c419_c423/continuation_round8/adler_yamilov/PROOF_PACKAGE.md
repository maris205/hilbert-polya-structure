# AY7: exact quotient, zero-safe lift and a global native-period bound

2026-09-08 UTC. AI-assisted author proof; no nonauthor review is claimed
by this file. The [frozen attempt](FROZEN_ATTEMPT.md) retains the original
all-integer-parameter structural atlas. This package does not replace it
by a finite-period theorem.

## Claim and status

**Original AY7 question:** structurally classify every ordinary integral
periodic state of $Y_k$, for every integer $k$, with its least native
period and all zero/exceptional branches. **NOT CURRENTLY JUSTIFIED.**

**Auxiliary theorem proved here:** for every $k\in\mathbb Z\setminus\{0\}$,
every nonzero ordinary rational periodic state has least native period
$$
N=m\quad\hbox{or}\quad N=2m,
\qquad m\in\{3,4,5,6,7,8,9,10,12\}.
\tag{1}
$$
In particular $N\le24$. The origin is fixed. For $k=0$, the retained
ordinary-domain pair swap has least period one or two, as already proved
in the seventh pass. Thus the bound covers the entire frozen integer
family, without an integrality or height assumption on the periodic
coordinates in the nonzero-parameter part.

Status of this auxiliary theorem: **PROVABLE AS STATED**, with the explicitly
stated external input of Mazur's rational elliptic torsion theorem.
The exact cubic and all singular-fibre and zero-product arguments are
given below. No smooth-generic-fibre hypothesis is being added to (1).

The bound is a classical-torsion consequence of the quotient and lift,
not an assertion that every number in (1) occurs, and not the original
integral cycle atlas. No fourth contract is proposed from it alone.

## Assumptions and notation

Keep the displayed map and inverse:
$$
Y_k(p,q,r,s)=(r-hp,s,p,q+hs),\qquad h=\frac{k}{1+ps},
\tag{2}
$$
$$
Y_k^{-1}(p,q,r,s)=
\left(r,s-\frac{kq}{1+rq},p+\frac{kr}{1+rq},q\right).
\tag{3}
$$
Ordinary means that (2) and (3) remain defined at every positive and
negative iterate. One application of (2) is one native step. Individual
zero coordinates are allowed. No hole is filled when a numerator vanishes.

At time $n$, put
$$
D_n=1+p_ns_n,\quad E_n=1+r_nq_n=D_{n-1},\quad h_n=k/D_n.
$$
Thus $D_n,E_n\ne0$. The lag identities and scalar recurrences are
$$
r_n=p_{n-1},\quad q_n=s_{n-1},\qquad
p_{n+1}=p_{n-1}-h_np_n,\quad
s_{n+1}=s_{n-1}+h_ns_n.                         \tag{4}
$$
The corrected classical invariants are
$$
I=pq+rs,\qquad J=pqrs+ps+qr+krs.
$$
Their preservation was checked in the
[seventh-pass correction](../../continuation_round7/nonlinear_scout/CORRECTION_RECEIPT.md)
and [nonauthor helper review](../../continuation_round7/nonlinear_review/INDEPENDENT_HELPER_REVIEW.md).
For the proof define constants
$$
C=J+1,\quad L=J+1-kI,\quad a=C+L-k^2,
\quad e=CL+k^2,\quad A_2=\frac{a^2-4e}{4k^2}.       \tag{5}
$$
The letter $L$ here is a scalar, not a matrix or a length bound.

## Strategy and dependency map

1. Use products, not coordinate quotients, to derive a two-dimensional
   recurrence and its cubic model. This retains every ordinary zero stratum.
2. Identify its exact one-step translation point $P=(0,k/2)$.
3. On smooth cubics use Mazur. On nodal/cuspidal cubics use explicit
   rational parametrizations, including split and nonsplit nodes.
4. Remove the unique singular point and quotient periods one/two as
   possible nonzero periodic lifts.
5. Prove the product-matrix fibre is a free rational scaling orbit whenever
   an original nonzero periodic state lies above it. Its finite return
   multiplier is $1$ or $-1$, establishing the original native clock.

Mazur is the only deep external theorem used. The elementary chord law
on a smooth Weierstrass cubic, and the definition of the group identity
at its point at infinity, use their usual algebraic meaning over $\mathbb Q$.
Singular group laws are derived rather than inferred from smooth fibres.

## Proof

### 1. Exact product quotient without deleting zero coordinates

At one state write
$$
x=ps=D-1,\quad y=rq=E-1,\quad z=pq,\quad w=rs.
$$
Then $xy=zw$, $z+w=I$, and
$$
J=xy+x+y+kw=DE-1+kw.
$$
Consequently
$$
w=\frac{C-DE}{k},\qquad z=\frac{DE-L}{k}.        \tag{6}
$$
Only $k\ne0$ is divided out in (6); $p,q,r,s,x,y$ may vanish.
The relation $xy=zw$ becomes
$$
(DE-C)(DE-L)+k^2(D-1)(E-1)=0,
$$
or equivalently
$$
D^2E^2-aDE-k^2(D+E)+e=0.                         \tag{7}
$$

Directly from (2),
$$
x'=y+h(w-z)-h^2x,\qquad E'=D.
$$
Substituting (5), (6) and $h=k/D$ yields
$$
D'=\frac aD+\frac{k^2}{D^2}-E,\qquad E'=D.
\tag{8}
$$
For example, the intermediate expression for $D'$ is
$E+(C+L-2DE)/D-k^2(D-1)/D^2$, which reduces to (8).
Thus no division by $D-1=ps$ has entered this quotient.

On an integral orbit $D_n\mid k$: the first update gives
$D_n\mid kp_n$, while $\gcd(D_n,p_n)=1$ since $D_n-p_ns_n=1$.
This inherited divisor fact is not required for the bound (1), but
remains the arithmetic condition for the original atlas.

### 2. Cubic model and exact native translation

On $D\ne0$ set
$$
X=D,\qquad
Y=\frac{2D^2E-aD-k^2}{2k}.                       \tag{9}
$$
Completing the square in (7) gives
$$
\mathcal E:\quad
Y^2=X^3+A_2X^2+\frac a2X+\frac{k^2}{4}.          \tag{10}
$$
Conversely, for $X\ne0$ recover
$$
D=X,\qquad E=\frac{2kY+aX+k^2}{2X^2}.            \tag{11}
$$
The original ordinary quotient is therefore an open part of this cubic,
with $D,E$ nonzero. Points of (10) for which (11) gives $E=0$ are not
silently admitted as ordinary points.

The projective cubic is irreducible even if singular. Indeed its affine
equation is $Y^2=f(X)$ with $f$ a monic cubic. Reducibility over an
algebraic closure would require $f$ to be a square in the rational
function field; its pole order three at infinity rules this out. Its
unique point at infinity $O$ is nonsingular.

Let $P=(0,k/2)$. It belongs to (10), is nonsingular since $k\ne0$,
and is neither $O$ nor its own inverse. For a nonsingular ordinary point
$Q=(X,Y)$, the line through $P,Q$ has slope
$\lambda=(Y-k/2)/X$. The chord law gives
$$
X(Q+P)=\lambda^2-A_2-X
      =\frac{a}{2X}+\frac{k^2}{2X^2}-\frac{kY}{X^2}.
\tag{12}
$$
Using (11), this is exactly $a/X+k^2/X^2-E$, the first coordinate
of (8). For the second coordinate the same chord gives
$$
Y(Q+P)=-\frac k2-\frac{Y-k/2}{X}\,X(Q+P).
$$
Substitution of (10) and (12), or the inverse chord using $-P$, gives
$$
Y(Q+P)=\frac{2X(Q+P)^2X-aX(Q+P)-k^2}{2k},       \tag{13}
$$
which is (9) for the updated pair $(D',D)$. Hence the quotient is
**addition by $P$ in one original step**, not by $2P$ and not after
parameter exchange. All formulas used here are valid along the ordinary
orbit, where $X$ and the updated $X$ remain nonzero.

### 3. Nonsingular cubics

Suppose $f$ has distinct roots. Then (10), with $O$ as identity, is an
elliptic curve over $\mathbb Q$. If a rational quotient point has least
period $m$, equations (12), (13) show
$Q+mP=Q$. Cancellation in the group gives $mP=O$, and minimality shows
that $m$ is exactly the order of the rational point $P$.

Mazur's theorem says that a rational elliptic torsion point has order
in $\{1,2,\ldots,10,12\}$. Since $P\ne O$ and $P\ne-P$, orders
one and two are impossible. This gives precisely the set for $m$ in
(1) on all nonsingular fibres.

The theorem is an external classical input, not proved here. The exact
list was read in the author's later primary exposition,
[Balakrishnan–Mazur, Section 1.4](https://arxiv.org/pdf/2307.04752),
which points to Mazur's original Theorem 8. The
[1977 publication record](https://numdam.org/item/PMIHES_1977__47__33_0/)
was checked; both attempted original-PDF endpoints exceeded the browser
size limit, so no original-1977-body reading is asserted.

### 4. Singular cubics: rational node and cusp parameters

If $f$ has a repeated root, that repeated root $r$ is rational: it is
the unique repeated root and is Galois invariant. The triple-root case
also has $r=-A_2/3\in\mathbb Q$. Since $f(0)=k^2/4\ne0$, $r\ne0$.
There are two cases.

For a node write $f(X)=(X-r)^2(X-s)$ with $r,s\in\mathbb Q$,
$r\ne s$, and put $c=r-s\ne0$. The normalization parameter is
$$
t=\frac{Y}{X-r},\qquad X=t^2+s,\qquad
Y=t(t^2-c).
$$
The point $O$ is $t=\infty$ and the omitted node branches are
$t=\pm d$, where $d^2=c$. On the smooth locus set
$$
u(t)=\frac{t-d}{t+d}\in\mathbb Q(d)^*.
$$
This parametrizes the chord group multiplicatively. To verify the law,
a nonvertical line $Y=\lambda X+b$ intersects the parameter line in
the three roots of
$t^3-\lambda t^2-ct-(\lambda s+b)$.
Its values at $d$ and $-d$ agree. Consequently the three values of
$u(t)$ have product one. Reflection $Y\mapsto-Y$ takes
$t\mapsto-t$ and $u\mapsto u^{-1}$, proving
$u(Q_1+Q_2)=u(Q_1)u(Q_2)$; tangent cases follow by repeated roots,
and a vertical line gives inverse points directly. Also $u(O)=1$.

This proof includes a split node ($d\in\mathbb Q$) and a nonsplit
node. In the latter case rational $Q$ gives a value in the quadratic
field $\mathbb Q(d)$ with conjugate its inverse. A periodic translation
therefore makes $u(P)$ a root of unity in a field of degree at most two.
Its order belongs to $\{1,2,3,4,6\}$: the cyclotomic degree formula
$[\mathbb Q(\zeta_j):\mathbb Q]=\varphi(j)$ forces
$\varphi(j)\le2$. Again $P\ne O$ and $Y(P)\ne0$ exclude orders
one and two. Thus nodal smooth-locus quotient periods are $3,4,6$.

For a cusp write $f(X)=(X-r)^3$. The normalization is
$X=r+t^2$, $Y=t^3$. Its smooth locus has $t\ne0$ and includes
$t=\infty$ at $O$. Put $u=1/t=(X-r)/Y$, with $u(O)=0$.
A nonvertical line yields a cubic in $t$ whose linear coefficient is
zero. Hence the sum of the three reciprocal roots is zero. Reflection
negates $u$, proving the additive chord law. Since
$u(P)=-2r/k\ne0$, translation by $P$ has no periodic smooth point
in characteristic zero.

The unique singular point $S=(r,0)$ needs separate treatment, because
it does not belong to either smooth group. From $f(r)=f'(r)=0$ one
gets
$$
\frac{a}{2r}+\frac{k^2}{2r^2}=r,
\qquad 2r^3-ar-k^2=0.
$$
Thus (11) sends $S$ to $(D,E)=(r,r)$ and (8) fixes it. It is
a quotient fixed point, not an additional high-period orbit.

### 5. Quotient period one and two cannot hide nonzero periodic lifts

If $D_n$ is constant, then $h_n=h\ne0$. The first recurrence in
(4) is represented by
$$
B(h)=\begin{pmatrix}-h&1\\1&0\end{pmatrix}.
$$
Its characteristic roots are real and distinct, since its discriminant
is $h^2+4>0$. Neither root is $1$ or $-1$, because substitution in
$\lambda^2+h\lambda-1$ gives respectively $h$ and $-h$.
A real root of unity can only be $1$ or $-1$; hence $B(h)^N-I$
is invertible for every positive integer $N$. Periodicity forces
$p_n=0$ for every $n$. It then forces $D_n=1$, $h_n=k$, and the
second recurrence, represented by $B(-k)$, forces $s_n=0$.
Thus this lift is the origin. This argument covers the singular point
of the preceding section as well as any other quotient fixed point.

A true quotient two-cycle would alternate distinct nonzero values
$u,v$. Equation (8) would give
$$
2v=a/u+k^2/u^2,\qquad 2u=a/v+k^2/v^2.
$$
After multiplying by $u$ and $v$, respectively, these imply
$a=2uv-k^2/u=2uv-k^2/v$, so $u=v$, a contradiction.
The exclusions $m=1,2$ therefore do not rely only on a generic elliptic
argument.

### 6. Zero-product matrices and the free scaling lift

Associate to a state the product matrix
$$
R(p,q,r,s)=
\begin{pmatrix}pq&ps\\rq&rs\end{pmatrix}
=\begin{pmatrix}p\\r\end{pmatrix}\begin{pmatrix}q&s\end{pmatrix}.
\tag{14}
$$
If this matrix is zero over $\mathbb Q$, either $(p,r)=(0,0)$
or $(q,s)=(0,0)$. The corresponding channel is invariantly zero
under (2) and (3). In the first case $D_n=1$, and multiplying
$s_{n+1}-s_{n-1}=ks_n$ by $s_n$ and summing over a period gives
$k\sum_n s_n^2=0$. Hence $s_n=0$ for all $n$. In the second
case the same argument with $p_{n+1}-p_{n-1}=-kp_n$ gives
$p_n=0$ for all $n$. Thus the only periodic state with $R=0$
is the origin. This uses that rational numbers are real; it is not
a claim over all complex coordinates.

For a nonzero periodic state, $R$ is consequently a nonzero rank-one
matrix at every time. Its four entries are recovered from $(D,E,I,J)$
by (6), together with $ps=D-1$, $rq=E-1$. Any two rational
factorizations of this same nonzero rank-one matrix differ by a unique
scalar $t\in\mathbb Q^*$:
$$
(p,q,r,s)\longmapsto S_t(p,q,r,s)=(tp,q/t,tr,s/t).
\tag{15}
$$
For completeness, choose a nonzero column of $R$. It makes the first
factor in (14) a nonzero scalar multiple of that column, so the two
first factors are proportional over $\mathbb Q$. A nonzero entry of
the first factor then determines the entire second factor. This proves
(15) even if several individual entries of $R$ or of the state vanish.
The action is free because $(p,r)\ne(0,0)$.

The displayed map commutes with every $S_t$: $ps$ and hence $h$
are unchanged, and the two channels scale reciprocally in (2).
If the quotient has least period $m$, the original point $v$ therefore
satisfies $Y_k^m(v)=S_t(v)$ for one $t\in\mathbb Q^*$, and
$$
Y_k^{jm}(v)=S_{t^j}(v)\qquad(j\ge1).             \tag{16}
$$
If $v$ has least native period $N$, then $m\mid N$. Freeness and
(16) imply $t^{N/m}=1$, so $t=1$ or $t=-1$. For $t=1$ minimality
gives $N=m$; for $t=-1$ freeness gives $N=2m$.
This proves the exact clock assertion in (1) without dividing by any
individual coordinate or treating a nonfree zero-product fibre as free.

### 7. Conclusion and unchanged atlas gap

Every nonzero ordinary rational periodic state has a quotient point on
(10). A singular quotient point would be fixed and is excluded by
Section 5. A smooth quotient point has period in the set of Section 3
or in its nodal subset from Section 4. Section 6 then gives (1), hence
$N\le24$. The origin and the inherited $k=0$ boundary complete the
auxiliary theorem. $\square$

This does **not** solve the original structural atlas. It leaves the
arithmetic of the possible quotient periods, divisibility
$D_n\mid k$, integral factorization of (14), and the finite scaling
multiplier to be exhausted uniformly across the variable parameter.
The missing implication is not “finite height implies periodicity” or
“a torsion quotient automatically lifts periodically.” In particular a
rational multiplier different from $\pm1$ defeats a periodic lift.
Listing the fixed loci of the finitely many possible iterates, without
solving their integral families, is not presented as the requested atlas.

## Exact hand controls after the diagnostic

The discarded origin-only proposal has a whole-parameter counterfamily.
For every nonzero integer $k$, the three consecutive states
$$
v_0=(-k-1,0,2,1),\quad
v_1=(1-k,1,-k-1,-1),\quad
v_2=(-2,-1,1-k,0)
$$
have respective denominators $-k,k,1$ and map successively to
$v_1,v_2,-v_0$. Since $Y_k(-v)=-Y_k(v)$, they form
$(v_0,v_1,v_2,-v_0,-v_1,-v_2)$. No state is zero, and all
displayed forward and inverse denominators are nonzero. Its least
period is six: $Y_k^3(v_0)=-v_0\ne v_0$, while a period dividing
two in (4) would force both channels zero. The cases $k=\pm1$
retain their zero coordinates and cause no degeneration of this period.

At $k=4$ and any signed divisor $b$ of $3$, put
$v=(b,-3/b,b,3/b)$. Four hand updates are
$$
v\longmapsto(0,3/b,b,0)
\longmapsto(b,0,0,3/b)
\longmapsto(-b,3/b,b,3/b)
\longmapsto-v.
$$
Their denominators are $4,1,4,-2$. The quotient has true period
four, so the native orbit has least period eight. This is an exact
coordinate replay, not reliance on the diagnostic's count. The linear
involution $U(p,q,r,s)=(s,r,q,p)$ satisfies
$Y_{-k}U=UY_k$ by substitution, giving the corresponding $k=-4$
family with the same native period. No general all-parameter exhaustion
is inferred from these controls.

## Source ownership, execution and open risks

The source map and corrected $I,J$ are classical. Fordy–Kassotakis
already reduce AY by its scaling symmetry to a two-dimensional QRT
map with a scalar lift; see their
[Example 3.3](https://arxiv.org/pdf/1301.1927). Thus Section 1's
zero-safe $D,E$ formulas are an explicit adaptation, not a claim to
discover the quotient mechanism. Mazur supplies the deep uniformity in
Section 3. The bound and short controls are not automatically a
substantial independent paper after these deductions.

[SOURCE_AUDIT.md](SOURCE_AUDIT.md) records exact accessed portions and
access failures. [DIAGNOSTIC_RECEIPT.md](DIAGNOSTIC_RECEIPT.md) records
the only mathematical execution in this pass. The proof of (1) uses no
finite-census result. No old program, GPU, paid model or Git mutation
was run. The author has checked signs, native time, fixed/singular fibres
and all zero-product cases; a nonauthor internal proof review remains a
separate gate. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.
