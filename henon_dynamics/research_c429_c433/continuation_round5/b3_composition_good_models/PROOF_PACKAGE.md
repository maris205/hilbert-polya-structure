# CGR5 — Complete affine good-model classification for Hénon words

2026-09-09 UTC. Author proof, with no mathematical program executions.
The complete frozen question is in [REPORT.md](REPORT.md). This file
does not assign admission, manuscript numbering or an evaluator grade.

## Claim, assumptions and status

**Author proof status: PROVABLE AS STATED.** The original full quantifiers
are retained. Independent mathematical/source review and the
coordinator's substance/admission decision are separate pending gates.

Let $K$ be any number field, $R=\mathcal O_K$, and
$$
F=H_r\circ\cdots\circ H_1,\qquad
H_i(x,y)=(y,f_i(y)-a_i x),\qquad r\ge1,
$$
where $a_i\in K^\times$, $f_i\in K[Y]$, and $d_i=\deg f_i\ge2$.
Write $b_i\ne0$ for the leading coefficient of $f_i$, and set
$$
D=\prod_{i=1}^r d_i,\qquad \delta=\prod_{i=1}^r a_i,
$$
$$
B=\prod_{i=1}^r b_i^{\prod_{j=i+1}^r d_j},\qquad
C=\prod_{i=1}^r(b_i/a_i)^{\prod_{j=1}^{i-1}d_j}. \tag{1}
$$
Empty products in exponents are $1$. Thus $B$ and $C$ are nonzero.
Let $F=(F_1,F_2)$ and $F^{-1}=(V_1,V_2)$, all in $K[x,y]$.
Define the scalar coefficients and centres
$$
\eta_y=[x^0y^{D-1}]F_2,\qquad
\eta_x=[x^{D-1}y^0]V_1,
$$
$$
c_x^0=-\frac{\eta_x}{DC},\qquad
c_y^0=-\frac{\eta_y}{DB}. \tag{2}
$$
These are coefficients of the *full expanded maps*, not of an
individual factor. Characteristic zero makes every division in (2)
legitimate; it does not make $D$ a local unit.

At a finite place $v$ put $E=K_v$, $O=\mathcal O_{K_v}$, and let
$v:E^\times\to\mathbb Z$ be normalized. Write $\kappa_v$ for the
residue field and $q_v=|\kappa_v|$. An affine coordinate map $T$ sends
new coordinates to the original ones, so its model is $T^{-1}FT$.
It is **regular-good** if this model and its inverse have coefficients
in $O$, both coefficient reductions retain degree $D$, and their
degree-$D$ projective homogenizations have disjoint indeterminacy sets
over $\overline{\kappa_v}$. Globally, the same $K$-affine $T$ must be
good at every finite place. There is no condition at infinite places.

All matrices in $\mathrm{GL}_2(E)$ or $\mathrm{GL}_2(K)$ and all
translations are allowed. No field extension, factorwise-good
assumption, individual-unit-$a_i$ assumption, nonaffine conjugacy or
change of compactification is allowed. The dynamics is iterated in the
native clock consisting of one full application of $F$.

## Main theorem

**Theorem CGR5.** For every word specified above:

1. At $v$, a good affine coordinate map exists if and only if
   $$
   v(\delta)=0,\qquad
   k_x=-\frac{v(C)}{D-1}\in\mathbb Z,
   \qquad k_y=-\frac{v(B)}{D-1}\in\mathbb Z, \tag{3}
   $$
   and the finite coefficient test below has a passing centre pair.
   Choose any $s,t\in E^\times$ with $v(s)=k_x$, $v(t)=k_y$, and a
   complete set $\mathcal B_v$ of representatives of $O/DO$. Test
   $$
   c_x=c_x^0+(s/D)\alpha,\qquad
   c_y=c_y^0+(t/D)\beta,
   \qquad \alpha,\beta\in\mathcal B_v. \tag{4}
   $$
   For each pair, put
   $$
   S(z)=(s z_1+c_x,t z_2+c_y). \tag{5}
   $$
   A pair passes precisely when **every coefficient of both**
   $S^{-1}FS$ and $S^{-1}F^{-1}S$ is in $O$. There are
   $q_v^{2v(D)}$ pairs. At most one pair passes modulo
   $sO\times tO$. The bound is exhaustive, not asserted minimal.

2. If one pair passes, the complete set of local good coordinate maps
   is the left coset
   $$
   S\operatorname{Aff}_2(O),\qquad
   \operatorname{Aff}_2(O)=\mathrm{GL}_2(O)\ltimes O^2. \tag{6}
   $$
   Its unique image lattice is the rectangle
   $$
   (c_x+sO)\times(c_y+tO). \tag{7}
   $$
   This rectangle equals the set of points of $E^2$ having bounded
   two-sided native $F$-orbit.

3. If every finite place passes, define the fractional ideals
   $$
   I_x=\prod_v\mathfrak p_v^{-v(C)/(D-1)},\qquad
   I_y=\prod_v\mathfrak p_v^{-v(B)/(D-1)}. \tag{8}
   $$
   They satisfy
   $$
   (C)I_x^{D-1}=R,\qquad (B)I_y^{D-1}=R. \tag{9}
   $$
   There is $c^*=(c_x^*,c_y^*)\in K^2$ whose local image rectangle
   is $(c_x^*+I_xO_v)\times(c_y^*+I_yO_v)$ everywhere. Such centres
   form one coset of $I_x\oplus I_y$.

   A global affine good coordinate map exists if and only if
   $$
   I_x\oplus I_y\text{ is free over }R
   \quad\Longleftrightarrow\quad I_x I_y\text{ is principal}
   \quad\Longleftrightarrow\quad [I_x I_y]=1. \tag{10}
   $$
   If (10) holds, all global good maps are exactly
   $$
   \left\{T(z)=Az+c:
      AR^2=I_x\oplus I_y,\quad c-c^*\in I_x\oplus I_y\right\}.
   \tag{11}
   $$
   This is one left coset of $\operatorname{Aff}_2(R)$.

The prescriptions are finite and independent of the chosen local scale
generators, residue representatives and patched centre. The determinant
class in (10) is invariant under a global affine reexpression. It is
the product of two possibly distinct ideal classes, not in general the
square of a common class. The theorem gives every failure branch and
every model, with no restriction on word length, coefficients,
ramification, residue characteristic or the class group.

## Proof strategy and dependency map

The proof uses the primitive-row mechanism already established in
single-factor GR5, with its new composition hypotheses verified below.
It does not cite GR5's conclusion outside its single-factor domain.

1. The exact forward and inverse leading forms force arbitrary affine
   matrices into integral row directions and two independent scales.
2. Two pure subleading coefficients bound both centre classes. A full
   coefficient test handles all remaining cancellations and wild cases.
3. Two-sided escape for the complete good map makes the rectangle
   intrinsic and unique.
4. Additive CRT patches both centres. The determinant ideal is necessary
   and an explicit two-ideal matrix proves sufficiency and all models.
5. Explicit unequal-ideal examples distinguish product repair from a
   square rule; a telescoping word rules out factorwise Jacobian tests.

## 1. Degrees and both leading forms

**Lemma 1.** The full maps have degree $D$, constant Jacobians $\delta$
and $\delta^{-1}$, and top homogeneous parts
$$
F_D(x,y)=(0,B y^D),\qquad (F^{-1})_D(x,y)=(C x^D,0). \tag{12}
$$
In fact $\deg F_1=D/d_r$ and $\deg V_2=D/d_1$.

*Proof.* Start with $P_0=x,P_1=y$ and recursively set
$$
P_{i+1}=f_i(P_i)-a_iP_{i-1}\quad(1\le i\le r).
$$
Then $H_i\cdots H_1=(P_i,P_{i+1})$. For $i=1$, $P_2$ has leading
term $b_1y^{d_1}$; its subtracted term has degree one. If $P_i$ has
degree $d_1\cdots d_{i-1}$ and leading term a nonzero multiple of that
power of $y$, then $f_i(P_i)$ has degree $d_1\cdots d_i$, strictly
larger than $\deg P_{i-1}$. Thus no top cancellation with $a_iP_{i-1}$
is possible. The top coefficient is multiplied recursively by $b_i$
and raised to $d_i$, giving $B$ in (1). This proves the forward claims,
including $r=1$ and the empty product $D/d_r=1$.

For the inverse use
$$
H_i^{-1}(x,y)=((f_i(x)-y)/a_i,x),
$$
applied in order $H_r^{-1},H_{r-1}^{-1},\ldots,H_1^{-1}$. Its first
coordinate grows successively in the degrees $d_r,d_{r-1},\ldots,d_1$;
the subtracted previous coordinate always has smaller degree. The same
explicit induction, now in $x$, gives coefficient
$(b_1/a_1)(b_2/a_2)^{d_1}\cdots(b_r/a_r)^{d_1\cdots d_{r-1}}=C$,
and the second coordinate has degree $D/d_1$. Finally each factor has
Jacobian $a_i$, so the chain rule gives $\delta$ and its inverse.
$\square$

## 2. Every affine good lattice is a rectangle

Fix $E,O,v$. Let $T(z)=Az+c$ be a good affine coordinate map. Write
$\ell_1,\ell_2$ for the row forms of $A$ and $e_1,e_2$ for standard
column vectors. Affine translation does not alter top homogeneous
parts, so (12) gives
$$
(T^{-1}FT)_D=B A^{-1}e_2\,\ell_2^D,
\qquad
(T^{-1}F^{-1}T)_D=C A^{-1}e_1\,\ell_1^D. \tag{13}
$$
Write $\ell_1=s u_1$, $\ell_2=t u_2$, where each $u_i$ is a primitive
integral linear form: at least one of its two coefficients is a unit.
The polynomial $u_i^D$ is primitive in every residue characteristic,
because a unit coefficient gives a unit coefficient of a pure power
monomial. This requires no invertibility of any binomial coefficient.

Set $w_+=Bt^D A^{-1}e_2$, $w_-=Cs^D A^{-1}e_1$. Integrality of the
degree-$D$ coefficients in (13) forces both vector entries of each
$w_\pm$ into $O$. Degree preservation forces at least one entry of each
vector to be a unit. Consequently the geometric indeterminacy sets on
the line at infinity are exactly
$$
\{\bar u_2=0\},\qquad \{\bar u_1=0\}. \tag{14}
$$
For justification, the last homogeneous coordinate is $Z^D$, there is
no affine indeterminacy, and the unit top term precludes a common factor
$Z$ in the homogeneous coordinate tuple. At $Z=0$ the simultaneous
zeros of the other coordinates are exactly the zeros of the displayed
nonzero linear form. The finite affine chart is regular because
reduction of the integral composition identities leaves inverse
polynomial automorphisms.

Disjointness in (14) says that the two primitive row reductions are
linearly independent. Their row matrix therefore lies in
$\mathrm{GL}_2(O)$, and
$$
A=\operatorname{diag}(s,t)U,\qquad U\in\mathrm{GL}_2(O). \tag{15}
$$
Integral affine right composition preserves goodness: the new model is
an integral affine conjugate of the old one, and both affine maps and
their reductions extend to projective linear automorphisms preserving
degree and indeterminacy separation. Right-composing $T$ by $U^{-1}$
therefore yields the good rectangle chart $S$ of (5).

For this chart the leading parts are
$$
(S^{-1}FS)_D=(0,Bt^{D-1}y^D),\qquad
(S^{-1}F^{-1}S)_D=(Cs^{D-1}x^D,0). \tag{16}
$$
Degree preservation and integrality say exactly that both scalar top
coefficients in (16) are units. This forces the two integer exponents
in (3). The Jacobian of any conjugate remains $\delta$; integrality of
the forward and inverse derivative determinants forces $v(\delta)=0$.
No inference about an individual $v(a_i)$ is made.

Conversely, for any scales satisfying (3), if the two full maps in the
coefficient test are integral, (16) supplies unit top coefficients.
Their reduced indeterminacy points are $[1:0:0]$ and $[0:1:0]$.
Thus the coefficient test is sufficient for all regular-good
conditions, not just for lattice preservation.

## 3. A finite centre test in every residue characteristic

**Lemma 2 (no mixed-term contamination).** The coefficient of $y^{D-1}$
in the second coordinate of $S^{-1}FS$ equals
$$
t^{D-2}(DBc_y+\eta_y).
\tag{17}
$$
The coefficient of $x^{D-1}$ in the first coordinate of
$S^{-1}F^{-1}S$ equals
$$
s^{D-2}(DCc_x+\eta_x).
\tag{18}
$$

*Proof.* By (12) every monomial of $F_2$ other than $B y^D$ has total
degree at most $D-1$. A monomial with $y$-degree $D-1$ and positive
$x$-degree would have total degree at least $D$, and the only possible
degree-$D$ monomial is the pure $y^D$. Hence the only term of
$y$-degree $D-1$ is $\eta_y y^{D-1}$. Under substitution
$(x,y)=(sX+c_x,tY+c_y)$, lower $y$-degree cannot increase. The pure
top term contributes $DBc_y t^{D-1}$ and the pure subleading term
contributes $\eta_y t^{D-1}$. Dividing the output by $t$ gives (17);
the subtracted centre changes only the constant term. The identical
argument with $V_1$ and $x$ proves (18). This includes $D=2$, since
then $D-1=1$ is still not a constant term. $\square$

Let $e=v(D)$. By the forced top-unit valuations,
$$
v(DBt^{D-2})=e-k_y,\qquad
v(DCs^{D-2})=e-k_x.
$$
The integrality of (17)–(18) therefore forces
$$
c_y\in c_y^0+(t/D)O,\qquad
c_x\in c_x^0+(s/D)O. \tag{19}
$$
For $u,w\in O$, replacing $(c_x,c_y)$ by $(c_x+su,c_y+tw)$ right-composes
$S$ with the integral translation $(X,Y)\mapsto(X+u,Y+w)$. Thus
goodness depends only on the centre classes modulo $sO\times tO$.
The two quotients in (19) each identify with $O/DO$, which has $q_v^e$
elements. This proves completeness of (4) and the pair count.

For clarity, the coefficient test itself can be written without
derivatives or factorial division. If $W(x,y)=\sum w_{ij}x^i y^j$ is
one of $F_1,F_2,V_1,V_2$, and the corresponding output scale and centre
are $(\lambda,c_o)=(s,c_x)$ or $(t,c_y)$, its coefficient at $X^mY^n$
after the full coordinate change is
$$
\frac{s^m t^n}{\lambda}
\sum_{i\ge m,\ j\ge n}
w_{ij}\binom{i}{m}\binom{j}{n}
c_x^{i-m}c_y^{j-n}
-\mathbf1_{m=n=0}\frac{c_o}{\lambda}. \tag{20}
$$
Here $(s,c_x)$ applies to $F_1,V_1$ and $(t,c_y)$ to $F_2,V_2$.
Testing (20) for all four polynomials and all monomials is a finite
exact test of every coefficient. Necessary top/subleading tests alone
are never promoted to sufficiency.

## 4. Uniqueness from the native two-sided bounded set

**Lemma 3.** Suppose $G,G^{-1}$ are integral and their top parts are
$(0,u y^D)$ and $(w x^D,0)$ with $u,w\in O^\times$, $D\ge2$.
Then
$$
\{z\in E^2:\{G^n(z):n\in\mathbb Z\}\text{ is bounded}\}=O^2.
\tag{21}
$$

*Proof.* Integral maps in both directions preserve $O^2$, proving one
inclusion. Suppose $M=\max(|x|,|y|)>1$. If $|y|=M$, the unique
degree-$D$ monomial of $G_2$ has norm $M^D$, while every other term has
norm at most $M^{D-1}$. Also $\deg G_1<D$, so
$$
|G_2(x,y)|=M^D,\qquad |G_1(x,y)|\le M^{D-1}<M^D.
$$
At every subsequent forward iterate the second coordinate is strictly
maximal, and its norm grows successively to $M^{D^2},M^{D^3},\ldots$.
The forward orbit is unbounded. If instead $|x|=M$, the same argument
with the displayed top form of $G^{-1}$ shows that its first coordinate
becomes strictly maximal and backward iteration is unbounded. These
cases cover every point outside $O^2$, including equality of the two
initial coordinate norms. $\square$

An invertible affine map over $E$ preserves boundedness in both
directions: both it and its inverse bound output norms by a constant
times the maximum of one and the input norm. Hence every good rectangle
chart $S$ has image equal to the same intrinsic set in (21), transported
back to the full $F$. Its image rectangle is unique.

The forced exponents already fix the side ideals $sO,tO$. Equality of
two such rectangles is exactly congruence of their centres modulo
$sO,tO$. Thus at most one candidate pair passes. Two scales with the
same prescribed valuations differ by units; the associated rectangle
charts for the same image differ by right composition with an integral
affine map. Combined with (15), this gives exactly (6). It proves the
whole local part of CGR5 without using bounded orbits of a factor or of
an auxiliary one-dimensional map.

## 5. Only finitely many places and global centre patching

First reject globally unless $\delta\in R^\times$ and all valuations
of $B$ and $C$ are divisible by $D-1$. These are finite principal-ideal
factorization checks. Let $\mathcal S$ consist of the finite places
where $v(B)\ne0$, $v(C)\ne0$, or some coefficient of $F$ or $F^{-1}$
has negative valuation. Outside $\mathcal S$, $s=t=1$ and $c_x=c_y=0$
already give good reduction by (12). Primes dividing $D$ need no
separate search merely because they are wild.

At each place of $\mathcal S$, a scale with the prescribed integer
valuation can be chosen in $K^\times$: select an element of
$\mathfrak p\setminus\mathfrak p^2$ and raise it to that integer
power. This does not require the prime ideal to be principal. The
residue classes of $O_v/DO_v$ can be represented by $R$, using
$R/\mathfrak p^{v(D)}\simeq O_v/DO_v$. Thus every candidate centre
in (4), and in particular the passing centres, can be taken in $K$.
Set the passing local centres to zero outside $\mathcal S$.

The ideals (8) have finite support and satisfy (9) by their valuations.
We record explicitly the additive patching used separately for $I_x$
and $I_y$. Let $I$ be either ideal and $c_v\in K$ its finitely supported
list of local centres. Choose $0\ne h\in R$ such that $J=hI$ is an
integral ideal and all the finitely many $hc_v$ lie in $R$. For every
place with $n_v=v(J)>0$, impose
$$
z\equiv hc_v\pmod{\mathfrak p_v^{n_v}O_v}.
$$
The residue has a representative in $R$, so CRT supplies one $z\in R$
satisfying all these conditions. This includes any additional places
introduced by clearing denominators. At a place with $n_v=0$, both
$z$ and $hc_v$ are already integral, which is the required congruence.
It follows that $c=z/h$ obeys $c-c_v\in IO_v$ everywhere.

Two solutions differ by an element of
$K\cap\bigcap_v IO_v=I$, by fractional-ideal valuations. Conversely
every translate by $I$ remains a solution. Applying this construction
in both directions proves the asserted centre coset and gives $c^*$.
No additional translation obstruction remains.

## 6. The exact global determinant-product obstruction

Put $L=I_x\oplus I_y$. If $T(z)=Az+c$ is globally good, local
rectangle uniqueness forces
$$
AO_v^2=I_xO_v\oplus I_yO_v,\qquad c-c^*\in I_xO_v\oplus I_yO_v.
$$
Taking local intersections inside $K^2$ yields
$AR^2=L$ and $c-c^*\in L$. To justify the module equality directly,
one inclusion follows from localization. If $z\in L$, then
$A^{-1}z\in O_v^2$ for every finite $v$, so $A^{-1}z\in R^2$,
proving the other inclusion. Taking second exterior powers gives
$$
(\det A)=I_x I_y. \tag{22}
$$
This proves necessity of (10) for every possible mixed affine matrix.

Here is an explicit sufficient construction, valid for distinct ideals.
Every fractional ideal $I$ has two generators: choose $0\ne\alpha\in I$;
only finitely many primes have $v(\alpha)>v(I)$. At each choose a nonzero
class of $I/\mathfrak pI$, and use module CRT to choose $\beta\in I$
representing these classes. At the other primes $\alpha$ already has
minimal possible valuation. Thus $I=(\alpha,\beta)$. If there are no
exceptional primes, $\beta=0$ is allowed.

Suppose now $I_x I_y=(\gamma)$, and write $I_x=(\alpha,\beta)$. Since
$I_x I_x^{-1}=R$, choose $u,v\in I_x^{-1}$ such that
$\alpha u+\beta v=1$. Then $I_y=\gamma I_x^{-1}$ and the matrix
$$
A=\begin{pmatrix}
\alpha&\beta\\-\gamma v&\gamma u
\end{pmatrix},\qquad \det A=\gamma, \tag{23}
$$
has its first row in $I_x$ and second row in $I_y$. For $x\in I_x$,
$y\in I_y$,
$$
A^{-1}\binom{x}{y}
=\binom{ux-\beta y/\gamma}{vx+\alpha y/\gamma}\in R^2, \tag{24}
$$
because $I_x^{-1}I_x=R$ and $I_xI_y=(\gamma)$. Thus $AR^2=L$.
This proves the freeness equivalence and constructs an actual matrix
over $K$, not merely an abstract module isomorphism.

Take $T(z)=Az+c^*$. At $v$, let $S_v$ be a passing rectangle chart,
with scales $s_v,t_v$ and centre $c_v$. Then
$$
S_v^{-1}T(z)
=\operatorname{diag}(s_v^{-1},t_v^{-1})Az
+\operatorname{diag}(s_v^{-1},t_v^{-1})(c^*-c_v). \tag{25}
$$
The linear part is in $\mathrm{GL}_2(O_v)$ by equality of the image
lattices; the translation is integral by centre patching. Hence (25)
belongs to $\operatorname{Aff}_2(O_v)$, proving that $T$ is good
everywhere. The same argument proves sufficiency for every $A,c$ in
(11); necessity has already been proved. The resulting forward and
inverse coefficients lie in $K\cap\bigcap_v O_v=R$.

If $T_1,T_2$ satisfy (11), then $T_1^{-1}T_2$ carries $R^2$ bijectively
to itself, so its linear part and inverse are integral and its
translation is integral. Thus it is in $\operatorname{Aff}_2(R)$,
giving the stated single left coset, an orbit under right composition.

Changing local scale generators by units preserves the ideals.
Changing passing representatives or the patched centre preserves the
same affine lattices. The full bounded set of $F$ establishes their
intrinsic local meaning. Under any global affine reexpression with
linear part $M$, the lattices transform by $M^{-1}$; their determinant
ideal is multiplied by $(\det M)^{-1}$. Thus its ideal class and the
vanishing of (10) are coordinate-invariant. Equations (3)–(25) prove
the full classification and a terminating arithmetic prescription.
$\square$

## 7. Arithmetic and boundary examples

### 7.1 Two nonprincipal order-three directions repaired by mixing

Let $K=\mathbb Q(\sqrt{-23})$, $\omega=(1+\sqrt{-23})/2$,
$R=\mathbb Z[\omega]$, and
$$
P=(2,\omega-1),\qquad \lambda=\omega+1.
$$
As in accepted GR5, $P^3=(\lambda)$ and $P$ has exact class order three:
$N(\lambda)=8$ and it lies at only this prime above two, while
$N(m+n\omega)=m^2+mn+6n^2$ cannot equal $2$.

Take the two quadratic factors
$$
H_1(x,y)=(y,y^2/\lambda-x),\qquad H_2(x,y)=(y,y^2-x).
$$
Their full return is
$$
F(x,y)=\bigl(y^2/\lambda-x,(y^2/\lambda-x)^2-y\bigr),
\quad D=4,\quad B=\lambda^{-2},\quad C=\lambda^{-1}. \tag{26}
$$
Hence the forced ideals are $I_x=P$, $I_y=P^2$, unequal and both
nonprincipal, with $I_x I_y=P^3=(\lambda)$.

All places do pass, not just the ideal test. Choose $sO=PO$, $tO=P^2O$.
Put $\mu=t^2/(\lambda s)$ and $\nu=s^2/t$. Both are units, and direct
conjugation gives
$$
S^{-1}FS(x,y)
=\bigl(\mu y^2-x,\nu(\mu y^2-x)^2-y\bigr). \tag{27}
$$
Its inverse is integral, because (27) is the composition of the two
integral Hénon maps $(y,\mu y^2-x)$ and $(y,\nu y^2-x)$.
It retains degree four in both directions with separated
indeterminacy points. Thus (27) is genuinely regular-good.

An explicit global matrix is
$$
M=\begin{pmatrix}2&\omega-1\\ \omega-3&-\omega-1\end{pmatrix},
\qquad \det M=\lambda,\qquad MR^2=P\oplus P^2. \tag{28}
$$
For example, (23) gives exactly (28) by taking
$\alpha=2$, $\beta=\omega-1$, $u=-1$, $v=-\omega/2$;
$v\in P^{-1}$ because $P(\omega/2)\subset R$, and
$2u+(\omega-1)v=1$. Formula (24) verifies the image equality.
Consequently $T(z)=Mz$ is globally good. No global diagonal good chart
exists, since it would make both $P$ and $P^2$ principal.

This is not a same-ideal square repair: a nonprincipal order-three class
in single-factor degree four would obstruct a good model by GR5, while
the inverse order-three direction here cancels it. The degree-four full
map also cannot be affinely conjugate to a single-factor degree-four
Hénon map. Its coordinates in (26), together with $1$, span no nonconstant
affine-linear polynomial: cancelling the degree-four term first forces
the coefficient of $F_2$ to vanish, then cancelling the degree-two term
forces that of $F_1$ to vanish. A map affinely conjugate to a single
Hénon map would have a nonzero affine output combination that is affine
linear in the input, transported from that map's first coordinate.

### 7.2 A genuinely rectangular global obstruction

Let $K=\mathbb Q(\sqrt{-47})$, $\theta=(1+\sqrt{-47})/2$,
$R=\mathbb Z[\theta]$, and
$$
P=(2,\theta),\qquad \lambda=\theta+4.
$$
The polynomial $\theta^2-\theta+12$ has distinct roots $0,1$ modulo
two. Since $N(\lambda)=32$, $\lambda$ is in $P$ but not the other
prime above two, so $P^5=(\lambda)$. The norm form
$$
N(m+n\theta)=m^2+mn+12n^2=(m+n/2)^2+47n^2/4
$$
has no integral solution equal to $2$. Thus $P$ is nonprincipal and its
class has exact order five.

Choose
$$
H_1=(y,y^2/\lambda-x),\qquad H_2=(y,y^3-x).
$$
Here $D=6$, $B=\lambda^{-3}$ and $C=\lambda^{-1}$, so
$I_x=P$ and $I_y=P^3$. Locally choose their generators $s,t$. The
quantities $\mu=t^2/(\lambda s)$ and $\nu=s^3/t$ are units, and the
local full model is
$$
(x,y)\longmapsto
\bigl(\mu y^2-x,\nu(\mu y^2-x)^3-y\bigr),
$$
the composition of integral quadratic and cubic Hénon maps with unit
top coefficients. All local tests therefore pass. But
$I_xI_y=P^4$ is nonprincipal, so no global affine good model exists.
This obstruction involves distinct direction ideals; it is not merely
a repeated single-factor square example.

### 7.3 Individual Jacobians must not be tested as though necessary

For any rational prime $p$, let $G=(y,y^2-x)$ and set
$$
H_1=(y,p y^2-px),\quad
H_2=(y,p^{-2}y^2-x),\quad
H_3=(y,y^2-p^{-1}x). \tag{29}
$$
Let $T_0=T_3=\mathrm{Id}$, $T_1=\operatorname{diag}(1,p)$ and
$T_2=\operatorname{diag}(p,1)$. Direct substitution gives
$H_i=T_iGT_{i-1}^{-1}$ for $i=1,2,3$, and hence
$$
H_3H_2H_1=G^3.
$$
The full return is already regular-good at every prime, of degree
eight, while $a_1=p$, $a_3=p^{-1}$ are nonunits at $p$. Their
individual maps have no good affine model there because their
Jacobians and inverse Jacobians cannot both be integral. Thus a
factorwise-good hypothesis would exclude genuine cases of the complete
question. This example also checks that cancellation among the
coefficients in a presented word is allowed by the theorem's full-map
coefficient test.

### 7.4 Wild centre pairs and the single-factor boundary

Over $\mathbb Q_2$, take $H=(y,y^2+y-x)$ and $F=H^2$. Here
$D=4$, $B=C=1$, and $\eta_x=\eta_y=2$, so both base centres in (2)
are $-1/2$. The original chart is good, so the unique passing pair is
$(0,0)$ modulo $\mathbb Z_2^2$, not the base pair. The two lists each
have four classes $-1/2+\beta/4$ with $\beta\bmod4$; the passing
class has $\beta=2$ in both coordinates. The uniqueness proof, not a
claimed execution of sixteen tests, establishes that no other pair
passes. This shows why wild centres cannot be replaced by (2) alone.

When $r=1$, $B=b_1$ and $C=b_1/a_1$. The product-Jacobian condition
then makes the two scales equal up to a unit. The forward first
coordinate and inverse second coordinate force the two centres to
agree modulo that scale. The rectangle therefore becomes the square
of GR5, and (10) reduces to its ideal-square obstruction. The present
two-coordinate candidate bound need not be as sharp as GR5's
single-coordinate bound; no extra single-factor classification is
claimed.

## Corrections, ownership and open risks

No hypothesis was weakened or silently strengthened. The scout formulas
were verified rather than assumed. The proof's local classification
checks the entire full map and inverse; it does not infer goodness from
the leading coefficients, product Jacobian or ideal product alone.

The original GR5 primitive-row argument, integral-affine invariance,
classical local escape estimates, CRT and determinant/Steinitz theory
are substantive imported mechanisms. The proved extension concerns the
entire unrestricted word family, the independent direction scales and
centres, its unique native two-sided filled rectangle, and the exact
possibly unequal-ideal global obstruction and all models. Source
subtraction and whether this complete extension is independently
substantial are recorded separately in `REPORT.md`; author completion
does not decide admission.

Pending risks are independent checking of the actual proof and primary
source ownership, not an intentionally omitted mathematical lemma.
No polynomial program, finite census, old execution, PDF build,
external-model upload or Git/shared-file mutation was performed.
This is AI-assisted author mathematics, not human peer review or global
priority certification. `NO_BAD_EULER_OR_ROOT_NUMBER` applies throughout.
