# Two return rows and congruence-compatible conjugacy in SL(2,Z)

Status: **PROVABLE AS STATED — author proof, awaiting independent review.**
No paper number or admission is assigned. Publication priority and substantive
value are separate from the proof status; see `SOURCE_AUDIT.md`.

## 1. Frozen claim and scope

The family is **all** $A\in\mathrm{SL}_2(\mathbb Z)$, including the scalar,
elliptic and parabolic cases. This explicitly strengthens the initially
scouted hyperbolic contract; none of those boundary cases is silently omitted.
The domain is $X=\widehat{\mathbb Z}^{\,2}=\prod_p\mathbb Z_p^2$ and its
labelled quotients $X_q=(\mathbb Z/q\mathbb Z)^2$. The owner acts by $x\mapsto Ax$.
The ordinary iteration clock is $n\ge1$; the modulus $q$ is a resolution
label, not iteration time. The observation is

$$F_A(q,n)=\#\ker(A^n-I:X_q\longrightarrow X_q).$$

A **congruence isomorphism** is a bijection $H:X\to X$ such that, for every
$q\ge1$ and every $x,y\in X$,

$$x\equiv y\pmod q\quad\Longleftrightarrow\quad H(x)\equiv H(y)\pmod q.$$

It is a homeomorphism and induces compatible permutations of all $X_q$.
It need not preserve addition. Write $c(M)$ for the positive gcd of the
entries of a nonzero integral matrix, set $c(0)=0$, and define

$$t_A=\operatorname{tr}A,\qquad h_A=c(2A-t_AI),\qquad
g_A=\gcd(A_{12},A_{21},A_{22}-A_{11}),$$

with the gcd of three zero entries equal to zero.

**Theorem 1.** For any $A,B\in\mathrm{SL}_2(\mathbb Z)$, these conditions
are equivalent:

1. $F_A(q,n)=F_B(q,n)$ for all $q,n\ge1$.
2. $F_A(q,j)=F_B(q,j)$ for all $q\ge1$ and $j=1,2$.
3. $(t_A,h_A)=(t_B,h_B)$.
4. There is a congruence isomorphism $H$, with $H(0)=0$, satisfying
   $H\circ A=B\circ H$ on $X$.
5. On $L^2(X,\mu)$, where $\mu$ is normalized Haar measure, there is a
   unitary $V$ such that $U_AV=VU_B$ and $VE_q=E_qV$ for every $q$.
   Here $U_Af=f\circ A$ and $E_q$ is conditional expectation onto functions
   of $x\bmod q$.

The conclusion is not linear conjugacy. A complete description of the
linear-conjugacy classes merged by this observation is given in Theorem 2.
No determinant on $L^2(X)$ is asserted to exist merely because $U_A$ is unitary.

## 2. Dependencies and ownership

The proof uses Smith normal form, Cayley--Hamilton and elementary valuations.
The following two general classification results are classical:

- Baake--Roberts--Weiss (2008), Theorem 2 and Corollary 4: integral
  $2\times2$ matrices have the same trace, determinant and matrix gcd exactly
  when they are conjugate over every finite ring and over
  $\widehat{\mathbb Z}$. [Published author PDF](https://web.maths.unsw.edu.au/~jagr/BRW08.pdf).
- Gawron--Nekrashevych--Sushchansky (2001): rooted-tree automorphisms are
  conjugate exactly when their orbit trees, labelled by cycle sizes, are
  isomorphic. The exact criterion is explicitly restated in Ivanov (2008),
  §1.1, [arXiv:0806.4024](https://arxiv.org/pdf/0806.4024).
  We also give a direct lifting construction for our homogeneous case below.

The older unadmitted finite-lattice notes already derived the $(t,h)$ census
quotient and the two possible $g$ values in the hyperbolic subfamily. Those
facts are **not claimed as a new contribution in this batch**. This proof does
not assume their publication priority is resolved. The new question concerns
one compatible nonlinear conjugacy and the entire congruence-filtered Koopman
system. The nonhyperbolic cases are explicitly verified rather than inferred
from the former hyperbolic statement.

Dependency map: two Smith rows recover $(t,h)$; centered matrices reduce the
problem to one or two BRW classes; the two-class case reduces at the prime 2
to a homogeneous lifting lemma; product local conjugacies give $H$; pullback
gives $V$; finite-dimensional traces give the reverse spectral implication.

## 3. Two rows recover the label, including singular Smith cases

For an integral $2\times2$ matrix $M$ write its Smith factors as
$(s_1,s_2)$, using zero factors for the nullspace and the order
$s_1\mid s_2$. Thus a rank-one matrix has $(s_1,0)$ and the zero matrix
has $(0,0)$. With $\gcd(q,0)=q$,

$$\#\ker(M\bmod q)=\gcd(q,s_1)\gcd(q,s_2). \tag{1}$$

For each prime $p$, set $\alpha_i=v_p(s_i)$, allowing $\alpha_i=\infty$
when $s_i=0$. If $e_k=\log_p\#\ker(M\bmod p^k)$, then

$$e_k-e_{k-1}=\#\{i:\alpha_i\ge k\}. \tag{2}$$

The eventual slope gives the number of zero factors. All finite valuations
are recovered by the same formula. Hence the complete labelled modulus row
recovers the Smith factors, the rank, $c(M)$, and, in rank two, $|\det M|$.
For full rank the last number is also the maximum of (1) over all $q$.

Cayley--Hamilton gives

$$A^2-I=A(2A-t_AI),\qquad \det(A-I)=2-t_A,
\qquad \det(A^2-I)=4-t_A^2. \tag{3}$$

Left multiplication by the integral unimodular matrix $A$ preserves entry
content, so the second row always recovers $h_A=c(A^2-I)$.
The signed trace is recovered as follows.

- If $A-I$ has rank zero, then $A=I$ and $t_A=2$.
- If $A-I$ has rank one, then $t_A=2$ and $A\ne I$.
- Suppose $A-I$ has rank two. If $A^2-I$ has rank zero, then $A^2=I$.
  Since $X^2-1$ has distinct roots, $A$ is diagonalizable over $\mathbb Q$.
  Determinant one excludes the mixed pair of eigenvalues $1,-1$; the first
  row excludes $I$. Thus $A=-I$ and $t_A=-2$.
- In the same rank-two first-row case, if the second matrix has rank one,
  (3) gives $t_A=-2$.
- If both matrices have rank two, put $D_1=|2-t_A|$ and $D_2=|4-t_A^2|$.
  For integral $t_A\ne\pm2$, $D_2=3$ gives $|t_A|=1$, $D_2=4$ gives
  $t_A=0$, and $D_2\ge5$ gives $|t_A|=\sqrt{D_2+4}$. In every nonzero
  case $D_1$ distinguishes the two signs. These possibilities cover all
  integral traces in this branch.

This proves $2\Rightarrow3$ without assuming hyperbolicity or using an
all-period recurrence.

## 4. The centered matrix and the exceptional local bit

If $h_A=0$, then $A=(t_A/2)I$, so determinant one gives $A=I$ or $-I$.
The trace already distinguishes them. We henceforth suppose $h_A>0$.

For odd $t=t_A$, the integer $A_{22}-A_{11}$ is odd. Therefore

$$h_A=\gcd(2A_{12},2A_{21},A_{11}-A_{22})=g_A. \tag{4}$$

For even $t=2T$, write

$$A=TI+rN,\qquad
N=\begin{pmatrix}x&y\\z&-x\end{pmatrix},\qquad
\gcd(x,y,z)=1,\qquad r=c(A-TI)>0.$$

Then

$$h_A=2r,\qquad x^2+yz=D=\frac{T^2-1}{r^2},\qquad
g_A=r\gcd(y,z,2x)\in\{r,2r\}. \tag{5}$$

The gcd in (5) divides $2\gcd(x,y,z)=2$. If it equals 2, $x$ is odd and
$y,z$ are even, which implies $D\equiv1\pmod4$.
If two matrices have the same $(t,h)$ and the same $g$, BRW already gives a
linear conjugacy over $\widehat{\mathbb Z}$, which is a congruence isomorphism
fixing zero. It remains to handle differing $g$ values. In that case
$t=2T$, $h=2r$ and $D\equiv1\pmod4$.

These conditions force $r$ even and $T$ odd: for odd $r$, the equation
$T^2-1=r^2D$ is impossible modulo 4, whether $T$ is even or odd.
Let $s=v_2(r)$. Since $D$ is odd,

$$v_2(T-1)+v_2(T+1)=2s.$$

The smaller of the two valuations is 1 and the larger is at least 2. Thus
$s\ge2$, and there is a common sign $\varepsilon\in\{1,-1\}$ with

$$v_2(T-\varepsilon)=2s-1\ge s+1. \tag{6}$$

In particular $|T|>1$: the exceptional case is automatically hyperbolic.
For either matrix in this two-class situation, $\det N=-D$ is odd. Writing
$r=2^su$ with $u$ odd, (6) gives

$$A=\varepsilon I+2^s C_A,\qquad C_A\in\mathrm{GL}_2(\mathbb Z_2). \tag{7}$$

Indeed $C_A=uN+((T-\varepsilon)/2^s)I$ reduces modulo 2 to the invertible
matrix $uN$. The same sign and depth apply to $B$.

At every odd prime $p$, the matrices are linearly conjugate over $\mathbb Z_p$.
Here is a direct check that does not mistake equality of global matrix gcds
for equality at a single prime. Both normalized centered matrices $N_A,N_B$
are primitive modulo $p$, have trace zero and determinant $-D$. A scalar
trace-zero matrix modulo an odd prime is zero, so each reduction is nonscalar.
Every nonscalar endomorphism of a two-dimensional vector space has a cyclic
vector: otherwise the two coordinate lines and their sum are invariant with
every vector an eigenvector, forcing equal eigenvalues and a scalar matrix.
Lift such a vector $v$; the basis $(v,Nv)$ has unit determinant over
$\mathbb Z_p$. In this basis both matrices have companion form
$\left(\begin{smallmatrix}0&D\\1&0\end{smallmatrix}\right)$.
The resulting conjugacy also conjugates $TI+rN_A$ to $TI+rN_B$.

## 5. The homogeneous dyadic lifting lemma

**Lemma 3.** Fix $d\ge1$, $s\ge2$ and $\varepsilon\in\{1,-1\}$.
All maps $L_C:x\mapsto(\varepsilon I+2^sC)x$ on $\mathbb Z_2^d$, with
$C\in\mathrm{GL}_d(\mathbb Z_2)$, are conjugate by a zero-fixing isometry
for the maximum 2-adic norm. The conjugacies preserve every quotient modulo
$2^k$.

For a nonzero residue $x\bmod2^k$, put $j=\min_i v_2(x_i)<k$ and
$m=k-j$. Its orbit length is independent of $C$ and equals

$$\ell_+(m)=2^{\max(0,m-s)} \quad(\varepsilon=1), \tag{8}$$

$$\ell_-(m)=
\begin{cases}1,&m\le1,\\2^{\max(1,m-s)},&m\ge2\end{cases}
\quad(\varepsilon=-1). \tag{9}$$

**Proof.** First let $P=I+2^sC$. For odd positive $u$,

$$P^u-I=2^sC\bigl(uI+2^sR\bigr),\qquad R\in M_d(\mathbb Z_2),$$

by the binomial expansion, and the parenthesized matrix is invertible.
If $P^{2^a}=I+2^{s+a}C_a$ with $C_a$ invertible, then

$$P^{2^{a+1}}=I+2^{s+a+1}(C_a+2^{s+a-1}C_a^2),$$

whose new coefficient is invertible modulo 2. Induction followed by the odd
power calculation proves, for every $n\ge1$,

$$P^n-I=2^{s+v_2(n)}C_n,\qquad C_n\in\mathrm{GL}_d(\mathbb Z_2). \tag{10}$$

Since an invertible integral 2-adic matrix preserves the maximum norm,
$(P^n-I)x$ has valuation $j+s+v_2(n)$. The smallest return exponent is (8).

For $P=-I+2^sC$, odd powers satisfy $P^n-I\equiv-2I\pmod4$, so their
displacement valuation at $x$ is $j+1$. Also

$$P^2=I+2^{s+1}(-C+2^{s-1}C^2),$$

with invertible coefficient. Applying (10) to $P^2$ shows that, for even $n$,
the displacement valuation is $j+s+v_2(n)$. This gives (9).

To pass from these lengths to a compatible conjugacy, retain the rooted tree
of residue classes, not only its levelwise histograms. The zero classes form
one distinguished infinite spine. At level $j+1$ there are exactly $2^d-1$
nonzero children of its level-$j$ vertex; they all have vector valuation $j$.
Every descendant of any such child has that same valuation.

At level $k>j$, an orbit of size $\ell_\varepsilon(k-j)$ has $2^d$ lifts
per point. Every lifted point has orbit size $\ell_\varepsilon(k+1-j)$.
Thus this orbit has exactly

$$\frac{2^d\ell_\varepsilon(k-j)}{
\ell_\varepsilon(k+1-j)} \tag{11}$$

child orbits, all with the same label and the same subsequent branching.
Formula (11) and the zero spine determine the labelled orbit tree, independently
of $C$. The classical orbit-tree criterion therefore gives the isometry.

For an explicit compatibility argument, start with the zero map on the trivial
quotient and match the new nonzero children of each zero-spine vertex. At a
matched pair of nonzero parent cycles of common length $L$, choose a base point
in each cycle. A child cycle has common length $L'$ on both sides and projects
onto the parent cycle. Match child cycles using (11), choose representatives
projecting to the already matched base points, and map their successive
iterates to successive iterates. This is well-defined after $L'$ steps and
agrees with the previous-level map under reduction. Repeat for every parent
cycle. At the zero parent, match zero children to zero and the remaining
$2^d-1$ children to one another; all have length one. Induction gives compatible
bijective equivariant maps at every finite level. Their inverse limit is the
required zero-fixing isometry. This construction also proves the lemma without
appealing to the general tree classification theorem. $\square$

## 6. Completion of the classification

Condition 1 implies 2, and §3 gives $2\Rightarrow3$. Suppose 3 holds.
The scalar case is immediate. Equal $g$ gives a linear congruence isomorphism
by BRW. If $g$ differs, §4 gives linear conjugacies at all odd primes, and
Lemma 3 applied to (7) gives a zero-fixing isometry at 2. Their product is a
homeomorphism $H$ of $X$ conjugating $A$ to $B$. For every prime power it
preserves congruence in both directions, and the Chinese remainder theorem
gives the same statement for every $q$. Hence $3\Rightarrow4$.
Condition 4 induces an equivariant permutation of every $X_q$, proving
$4\Rightarrow1$.

Every $q$-coset has Haar measure $q^{-2}$, and $H$ permutes such cosets.
These cylinders generate the Borel sigma-algebra, so $H$ preserves Haar
measure. Pullback $Vf=f\circ H$ is unitary and satisfies

$$U_AVf=f\circ H\circ A=f\circ B\circ H=VU_Bf.$$

Since $H$ preserves the partition into $q$-cosets, $V$ preserves both the
range of $E_q$ and its orthogonal complement. Thus $VE_q=E_qV$, proving
$4\Rightarrow5$.

Finally, condition 5 restricts $V$ to a unitary intertwiner of the
$q^2$-dimensional space $\operatorname{ran}E_q$. In its normalized indicator
basis, $U_A$ is the permutation operator of $A\bmod q$ (with the harmless
inverse convention on basis vectors). Consequently

$$\operatorname{tr}(U_A^n|_{\operatorname{ran}E_q})=F_A(q,n).$$

Unitary equivalence gives equality of these traces for every $q,n$.
This proves $5\Rightarrow1$ and completes Theorem 1. $\square$

## 7. Exact arithmetic fibres and realization

**Theorem 2.** Quotient all matrices in Theorem 1 by
$\mathrm{GL}_2(\widehat{\mathbb Z})$-conjugacy. The fibres of the resulting
map to congruence-isomorphism classes, or equivalently to the observation
in Theorem 1, are as follows.

- There are the two scalar labels $(2,0)$ and $(-2,0)$, each a singleton.
- For odd $t$, labels are precisely the positive odd $h$ such that
  $h^2\mid t^2-4$. Each fibre is one linear class, with $g=h$.
- For even $t=2T$ and $h>0$, labels are precisely $h=2r$, with $r>0$ and
  $r^2\mid T^2-1$. Set $D=(T^2-1)/r^2$, allowing $D=0$ or $-1$.
  There is always one class with $g=r$, and one additional class with
  $g=2r$ exactly when $D\equiv1\pmod4$.

Divisibility by a nonzero integer into zero has its usual meaning, so the
parabolic traces allow every $r>0$. All two-class fibres are hyperbolic.

**Proof.** Necessity and the possible $g$ values were proved in §4. For odd
$t$ and an admissible $h$, put $E=(t^2-4)/h^2$; then $E\equiv1\pmod4$.
The matrix

$$\begin{pmatrix}(t+h)/2&h\\h(E-1)/4&(t-h)/2\end{pmatrix}$$

has determinant one, trace $t$, centered content $h$ and matrix gcd $h$.
For even trace, the two representatives, when allowed, are

$$A_0(T,r)=\begin{pmatrix}T&r\\rD&T\end{pmatrix},\qquad
A_1(T,r)=\begin{pmatrix}T+r&2r\\r(D-1)/2&T-r\end{pmatrix}. \tag{12}$$

The second matrix is used only for $D\equiv1\pmod4$. Both have determinant
one and centered content $2r$. Their matrix gcds are $r$ and $2r$.
These checks hold for all the indicated signs; when $D=0$ or $-1$ only the
first matrix occurs. BRW gives one linear class for each resulting
$(t,\det,g)$, and no additional class is possible. Theorem 1 gives the stated
forgetful fibres. $\square$

For example

$$A=\begin{pmatrix}1&4\\4&17\end{pmatrix},\qquad
B=\begin{pmatrix}5&8\\8&13\end{pmatrix}$$

have $(t,h)=(18,8)$ and $(g_A,g_B)=(4,8)$. They possess the compatible
nonlinear conjugacy of Theorem 1, but $B\equiv5I\pmod8$ while $A$ is
nonscalar modulo 8. This forbids linear conjugacy already at that quotient.
The old hyperbolic notes own the derivation of this pair and the minimal
absolute collision trace 18; neither is counted as a new finding here.

## 8. Congruence-spectral and differentiability consequences

Let $\mathcal H_m$ be the space spanned by characters of $X$ of exact
additive order $m$. Its orthogonal projection is

$$Q_m=\sum_{d\mid m}\mu(m/d)E_d.$$

The character basis gives $L^2(X)=\widehat{\bigoplus}_{m\ge1}\mathcal H_m$.
For any real sequence $(\lambda_m)$, the operator

$$D_\lambda f=\sum_m\lambda_mQ_mf,\qquad
\mathcal D(D_\lambda)=\left\{f:\sum_m\lambda_m^2\|Q_mf\|_2^2<\infty\right\}$$

is self-adjoint by its orthogonal direct-sum definition. The unitary $V$
constructed above commutes with every $Q_m$, preserves this domain and
intertwines $D_\lambda$ together with $U_A,U_B$. Thus even the joint source
system consisting of return dynamics and every such congruence-radial
self-adjoint operator cannot recover the missing local linear-conjugacy bit.
The sequence $(\lambda_m)$ is not selected here to fit target zeros, and no
trace-class or zeta-regularized determinant is inferred from self-adjointness.

In a two-class fibre the local conjugacy at 2 cannot be differentiable at zero
with invertible derivative. Indeed, if $H_2A=BH_2$ and the derivative
$J=DH_2(0)$ exists, the chain rule gives $JA=BJ$. For a zero-fixing
2-adic isometry, if this derivative exists then it is itself norm-preserving:
apply the difference quotient along $2^kx$ for each fixed $x\in\mathbb Q_2^2$
and pass to the limit. Consequently $J\in\mathrm{GL}_2(\mathbb Z_2)$,
contradicting the different local linear classes. In particular, no
zero-fixing congruence-isometry conjugacy in a two-class fibre has a
2-adic Frechet derivative at zero. This statement concerns the local factor,
not a purported real derivative on the profinite product.

## 9. Verification and open risks

`orbit_tree_check.py` constructs actual finite permutations, their cycles,
and the cycle parent maps under reduction. Its canonical signatures retain
the entire labelled finite orbit tree. Exact tuple equality, not hash equality,
is the diagnostic comparison. It tests traces $18,-18,66,-66$ through $2^8$,
the trace-18 pair through $3^4$ and $5^3$, a different-depth rejection control,
the scalar/nonscalar obstruction modulo 8, nine elliptic/parabolic/scalar
boundary cases through $2^4$, and a signed-scalar rejection control.
Its finite output does not
establish any infinite quantifier or publication priority.

The universal claims rest on the proof above. Independent proof/source review
is still required. The old 1996/1999/2003 BF source-access limitation remains
relevant to the inherited observation quotient; retrieving Ivanov does not
erase it. The substantive question is whether the compatible-conjugacy and
joint-filtration result, after crediting all these inputs, merits an independent
paper. It is not answered by the proof's existence.

AI assistance was used for source discovery, derivation and checks. No human
or external-model peer review is represented by this author document.
