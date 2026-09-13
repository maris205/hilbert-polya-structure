# Proof Package

## Claim

Let $K$ be a field of characteristic zero, let $r\ge4$, and let
$g\ge2r+1$ be integers. For
$q=(q_1,\ldots,q_r)$ and $p=(p_1,\ldots,p_r)$, define

$$
V_{r,g}(q)=\prod_{i=1}^r q_i^2+q_1^g,\qquad
W_{r,g}(p)=\prod_{i=1}^r p_i^2+p_r^g,
$$

$$
S(q,p)=(q,p+\nabla V_{r,g}(q)),\qquad
T(q,p)=(q+\nabla W_{r,g}(p),p),\qquad
F_{r,g}=T\circ S.
$$

Put $h=g-1$, $m=r-2$, and

$$
M_r=2\mathbf1\mathbf1^{\mathsf T}-I_r.
$$

Let $A=A_{r,g}$ be obtained from $M_r$ by replacing its first row by
$h e_1^{\mathsf T}$, let $B=B_{r,g}$ be obtained from $M_r$ by replacing
its last row by $h e_r^{\mathsf T}$, and put $C=C_{r,g}=BA$.

The following statements hold.

1. The maps $S$, $T$, and $F$ are polynomial automorphisms preserving
   $\omega=\sum_{i=1}^r dq_i\wedge dp_i$.
2. For $u>0$, set

   $$
   x_i=\frac{u_i}{u_1}\quad(2\le i\le r),\qquad
   \sigma(u)=\sum_{i=2}^r x_i.
   $$

   The set

   $$
   \mathcal K_{r,g}=
   \left\{u\in\mathbb R_{>0}^r:
   x_i\ge1\ (2\le i\le r),\
   \sigma(u)<\frac{g-2}{2}\right\}
   $$

   is an explicit sufficient invariant selector cone. It contains
   $\mathbf1$, both gradient phases select exactly $A$ and $B$, and
   $C\mathcal K_{r,g}\subset\mathcal K_{r,g}$ with strict output
   inequalities on every cone wall.
3. If $u_0=\mathbf1$, then the actual coordinate degrees satisfy

   $$
   v_{n+1}=Au_n,\qquad u_{n+1}=Cu_n\qquad(n\ge0),
   $$

   where $u_n$ is the $q$-degree vector after $F^n$ and $v_{n+1}$ is the
   intermediate $p$-degree vector after the next first shear. The selected
   leading homogeneous forms do not cancel.
4. For every $n\ge1$, the last $q$-coordinate strictly dominates the other
   $2r-1$ coordinate degrees. Consequently

   $$
   \deg(F_{r,g}^n)=e_r^{\mathsf T}C^n\mathbf1\qquad(n\ge1),
   $$

   and the same equality holds trivially at $n=0$, when all coordinate
   degrees tie. Moreover,

   $$
   \lambda_1(F_{r,g})=\rho(C).
   $$
5. Define

   $$
   U=\left\{z\in K^r:z_1=z_r=0,\
   \sum_{i=2}^{r-1}z_i=0\right\}.
   $$

   Then $\dim U=r-3$, $A|_U=B|_U=-I_U$, and $C|_U=I_U$. On the
   complementary equal-middle subspace, in coordinates
   $(a,b,c)\mapsto(a,b,\ldots,b,c)$, the restriction of $C$ is

   $$
   Q_{m,h}=
   \begin{pmatrix}
   h+4m+4 & 2m(2m+1) & 2(2m+1)\\
   2h+4m+2 & 4m^2+1 & 4m\\
   2h & 2mh & h
   \end{pmatrix}.
   $$

   Hence

   $$
   \chi_C(t)=(t-1)^{r-3}P_{m,h}(t),
   $$

   where

   $$
   \begin{aligned}
   P_{m,h}(t)
   ={}&t^3-(2h+4m^2+4m+5)t^2\\
   &+(h^2-8hm(m+1)+2h+4)t\\
   &-h^2(2m+1)^2.
   \end{aligned}
   $$

   Furthermore,

   $$
   P_{m,h}(1)=-4m(m+1)(h+1)^2\ne0.
   $$

   Thus the eigenvalue $1$ has algebraic and geometric multiplicity exactly
   $r-3$, and the exact degree sequence has the cubic $P_{m,h}$ as an
   annihilator.
6. The threshold is sharp for the stated ordinary-degree seed and strict
   selected face: at $g=2r$, the first pure and mixed scores tie and the seed
   lies on the cone-height boundary. No global failure theorem at or below
   that parameter is asserted.
7. The same degree and spectral conclusions hold after replacing the
   potentials by

   $$
   \alpha\prod q_i^2+\beta q_1^g,\qquad
   \gamma\prod p_i^2+\delta p_r^g,
   \qquad \alpha,\beta,\gamma,\delta\in K^\times.
   $$

   This corollary covers only these four nonzero coefficients on the fixed
   supports.

The cubic conclusion is an annihilating-equation statement. It is not a claim
that $\rho(C)$ has algebraic degree exactly three for every parameter.

## Status

PROVABLE AS STATED

This is the source-design author's proof classification required by the
proof-writing protocol. It is not an independent SOURCE_DESIGN_PASS.
Independent review of the frozen ten-file package remains pending.

## Assumptions

- $K$ is a field of characteristic zero. Algebraic closedness is not used.
- $r$ and $g$ are integers with $r\ge4$ and $g\ge2r+1$.
- Total degree is the ordinary polynomial degree with all $2r$ initial
  coordinates of degree one.
- The shear word is exactly $F=T\circ S$.
- The potentials contain exactly the displayed product monomial and endpoint
  pure power. The coefficient corollary assumes all four displayed
  coefficients are nonzero.
- Perron–Frobenius arguments are applied to the real positive integer matrix
  $C$, independently of the coefficient field $K$.

## Notation

- $h=g-1$ and $m=r-2$, so $m\ge2$ and $h\ge2m+4$.
- $\mathbf1$ is the all-one column in $\mathbb R^r$.
- $e_i$ is the $i$-th standard column.
- $M=2\mathbf1\mathbf1^{\mathsf T}-I$ has diagonal entries $1$ and
  off-diagonal entries $2$.
- For $u>0$, $x_i=u_i/u_1$ only for $2\le i\le r$, and
  $\sigma=\sum_{i=2}^r x_i$. There is no $x_1$ term in $\sigma$.
- $u_n$ is the vector of degrees of the $q$-coordinates after $F^n$.
- $v_{n+1}$ is the vector of degrees of the intermediate $p$-coordinates
  after applying $S$ to the $n$-th full iterate.
- $\operatorname{LH}(f)$ is the highest-total-degree homogeneous form of a
  nonzero polynomial $f$.
- $\rho(C)$ is the spectral radius of $C$.

## Proof Strategy

The proof follows the actual coordinate word. First, literal gradient
supports produce the two phase matrices. Second, an explicit homogeneous cone
gives strict selection and is proved invariant by exact row formulas. Third,
a phase-labelled induction controls carried coordinates, while a
highest-homogeneous-form argument in a polynomial domain prevents
cancellation. Fourth, row differences identify the total-degree observable.
Finally, middle-coordinate permutation symmetry splits off an
$(r-3)$-dimensional identity space and reduces all nontrivial spectral data to
one explicit three-dimensional restriction.

## Dependency Map

1. Polynomial automorphism and symplectic claims depend only on the gradients,
   subtraction inverses, and Hessian symmetry.
2. The phase matrices depend on the complete gradient support ledger and both
   strict selector margins.
3. The recurrence depends on seed containment, strict cone invariance, both
   carried-coordinate comparisons, and leading-form survival.
4. The exact degree formula depends on the recurrence, $C-A>0$, and strict
   last-row visibility for inputs in the cone.
5. The Perron formula depends on the exact visible degree identity and
   positivity of $C$.
6. The characteristic factorization depends on the direct invariant
   decomposition $K^r=U\oplus E$ and the exact quotient matrix.
7. Exact multiplicity depends on the factorization and
   $P_{m,h}(1)\ne0$.
8. The coefficient corollary depends on strict uniqueness of every selected
   degree and the integral-domain leading-form lemma.
9. The sharp boundary and $r=3$ specialization are separate audits and are
   not used to prove the headline range.

## Proof

### Step 1 — Gradients, inverses, and symplecticity

Differentiate the two potentials:

$$
\frac{\partial V}{\partial q_1}
=2q_1\prod_{j=2}^r q_j^2+gq_1^{g-1},
$$

$$
\frac{\partial V}{\partial q_i}
=2q_i\prod_{j\ne i}q_j^2
\qquad(2\le i\le r),
$$

$$
\frac{\partial W}{\partial p_i}
=2p_i\prod_{j\ne i}p_j^2
\qquad(1\le i<r),
$$

$$
\frac{\partial W}{\partial p_r}
=2p_r\prod_{j=1}^{r-1}p_j^2+gp_r^{g-1}.
$$

The inverse of $S$ is

$$
S^{-1}(q,p)=(q,p-\nabla V(q)),
$$

and the inverse of $T$ is

$$
T^{-1}(q,p)=(q-\nabla W(p),p).
$$

Thus both maps and their composition are polynomial automorphisms.

Let $H_V=\nabla^2V$ and $H_W=\nabla^2W$. Their Jacobians have block form

$$
J_S=\begin{pmatrix}I&0\\H_V&I\end{pmatrix},\qquad
J_T=\begin{pmatrix}I&H_W\\0&I\end{pmatrix}.
$$

Both Hessians are symmetric. With

$$
\Omega=\begin{pmatrix}0&I\\-I&0\end{pmatrix},
$$

direct block multiplication gives

$$
J_S^{\mathsf T}\Omega J_S=\Omega,\qquad
J_T^{\mathsf T}\Omega J_T=\Omega.
$$

Equivalently, the extra $dq_i\wedge dq_j$ terms in $S^*\omega$ and the extra
$dp_i\wedge dp_j$ terms in $T^*\omega$ cancel in symmetric pairs. Therefore
$S$, $T$, and $F$ preserve $\omega$.

### Step 2 — Literal support rows and the exact matrices

The mixed monomial in the $i$-th gradient row has exponent $1$ in coordinate
$i$ and exponent $2$ in every other coordinate. Its degree score on a weight
column $u$ is

$$
2\sum_{j=1}^r u_j-u_i=(Mu)_i.
$$

The only additional rows are $h e_1^{\mathsf T}$ in the first $V$ derivative
and $h e_r^{\mathsf T}$ in the last $W$ derivative. Hence the selected first
phase is $A$ and the selected second phase is $B$ once their two competitive
rows are proved strict. Every other derivative row is a singleton.

Multiplication $C=BA$ yields the following complete entry ledger:

$$
\begin{aligned}
C_{11}&=h+4m+4,&
C_{1j}&=4m+2 &&(2\le j\le r),\\
C_{i1}&=2h+4m+2 &&(2\le i<r),&
C_{ij}&=4m+\mathbf1_{\{i=j\}}
&&(2\le i<r,\ 2\le j\le r),\\
C_{rj}&=2h &&(1\le j<r),&
C_{rr}&=h.
\end{aligned}
$$

Thus, for $u_1>0$ and the normalized variables in the claim,

$$
\frac{(Cu)_1}{u_1}
=h+4m+4+(4m+2)\sigma, \tag{2.1}
$$

$$
\frac{(Cu)_i}{u_1}
=2h+4m+2+4m\sigma+x_i
\qquad(2\le i<r), \tag{2.2}
$$

and

$$
\frac{(Cu)_r}{u_1}=h(2+2\sigma-x_r). \tag{2.3}
$$

These formulas derive from the gradient monomials; $A$, $B$, and $C$ are not
free matrices.

### Step 3 — Both strict phase selectors

Let $u\in\mathcal K$ and put $v=Au$. The pure first-row score minus its mixed
competitor is

$$
hu_1-\left(u_1+2\sum_{i=2}^r u_i\right)
=u_1(h-1-2\sigma).
$$

Define

$$
\delta=h-1-2\sigma.
$$

The open height inequality gives $\delta>0$, so the first selector is strict.
The remaining first-phase rows have only their mixed monomial. Division by
$u_1$ gives

$$
\frac{v_1}{u_1}=h,\qquad
\frac{v_i}{u_1}=2+2\sigma-x_i\quad(2\le i\le r). \tag{3.1}
$$

For the second phase, the pure last-row score minus its mixed competitor is

$$
\Delta_T=(h-1)v_r-2\sum_{j<r}v_j.
$$

Substitution of (3.1) gives

$$
\frac{\Delta_T}{u_1}
=(2h-4m)\sigma-(h+1)x_r-4m-2. \tag{3.2}
$$

There are $m$ middle variables $x_2,\ldots,x_{r-1}$, each at least one, so

$$
x_r\le\sigma-m.
$$

Put $b_T=h-4m-1$. Equation (3.2) then gives

$$
\frac{\Delta_T}{u_1}
\ge b_T\sigma+m(h-3)-2. \tag{3.3}
$$

If $b_T<0$, multiplication of
$\sigma<(h-1)/2$ by $b_T$ reverses the inequality. Therefore

$$
\frac{\Delta_T}{u_1}
>\frac{b_T(h-1)}2+m(h-3)-2
=\frac{(h+1)(h-2m-3)}2>0. \tag{3.4}
$$

If $b_T\ge0$, use $\sigma\ge m+1$ in (3.3):

$$
\frac{\Delta_T}{u_1}
\ge b_T(m+1)+m(h-3)-2
=(2m+1)(h-2m-3)>0. \tag{3.5}
$$

The final factors are positive because $h\ge2m+4$. Hence the second selector
is strict everywhere in $\mathcal K$, including the least parameter.

### Step 4 — Seed containment and strict cone invariance

At $u_0=\mathbf1$, every $x_i=1$ and

$$
\sigma(u_0)=r-1=m+1.
$$

Since

$$
m+1<\frac{2m+3}{2}\le\frac{h-1}{2},
$$

the seed lies strictly in $\mathcal K$.

Let $U'=Cu$. For a middle index $2\le i<r$, subtract (2.1) from (2.2):

$$
\frac{U'_i-U'_1}{u_1}
=h-2-2\sigma+x_i
=\delta+(x_i-1)>0. \tag{4.1}
$$

Thus every allowed lower face $x_i=1$ maps strictly above its output lower
face.

For the last coordinate, subtract (2.1) from (2.3):

$$
L_1:=\frac{U'_r-U'_1}{u_1}
=h-4m-4+(2h-4m-2)\sigma-hx_r. \tag{4.2}
$$

Using $x_r\le\sigma-m$ and $b_1=h-4m-2$ gives

$$
L_1\ge(m+1)(h-4)+b_1\sigma. \tag{4.3}
$$

If $b_1<0$, the open upper bound on $\sigma$ gives

$$
L_1>
(m+1)(h-4)+\frac{b_1(h-1)}2
=\frac{(h+2)(h-2m-3)}2>0. \tag{4.4}
$$

If $b_1\ge0$, the lower bound $\sigma\ge m+1$ gives

$$
L_1\ge2(m+1)(h-2m-3)>0. \tag{4.5}
$$

The last lower face also maps strictly above one.

It remains to prove the height inequality. Define

$$
H_2=(h-1)U'_1-2\sum_{i=2}^rU'_i.
$$

Equations (2.1)–(2.3) give

$$
\frac{H_2}{u_1}
=h^2-h-8m^2-8m-4+c\sigma+2(h+1)x_r, \tag{4.6}
$$

where

$$
c=(4m-2)h-8m^2-4m-4.
$$

At $h=2m+4$ one has $c=8m-12>0$ because $m\ge2$, and $c$ increases with
$h$. Therefore (4.6) is bounded below on the allowed lower faces by setting
$\sigma=m+1$ and $x_r=1$. Exact collection yields

$$
\frac{H_2}{u_1}
\ge(h-2m-3)(h+4m^2+4m+2)>0. \tag{4.7}
$$

The inequality $H_2>0$ is equivalent to

$$
\sum_{i=2}^r\frac{U'_i}{U'_1}<\frac{h-1}{2}.
$$

Equations (4.1), (4.4)–(4.5), and (4.7) prove
$C\mathcal K\subset\mathcal K$ with strict output inequalities. At the least
parameter $h=2m+4$, every factored occurrence of $h-2m-3$ equals one; no
threshold equality is hidden.

### Step 5 — Carried coordinates and leading-form survival

The entry ledger for $C$ shows that $C-I$ is entrywise positive:

- the first row after subtracting $I$ has diagonal entry $h+4m+3$ and all
  other entries $4m+2$;
- a middle row has first entry $2h+4m+2$ and every middle-or-last entry
  $4m$ after its diagonal subtraction;
- the last row has entries $2h$ before the last position and $h-1$ in the
  last position.

Hence

$$
Cu>u\qquad(u>0). \tag{5.1}
$$

At the seed,

$$
A\mathbf1=(h,2r-1,\ldots,2r-1)^{\mathsf T}>\mathbf1. \tag{5.2}
$$

Initially, (5.2) makes every fresh first-phase gradient degree exceed the
carried $p$-degree. Suppose after $n\ge1$ full steps that

$$
u_n=Cu_{n-1},\qquad v_n=Au_{n-1}.
$$

Equation (5.1) gives $u_n>u_{n-1}$. Every row of $A$ is nonnegative and
nonzero, so

$$
Au_n>Au_{n-1}=v_n. \tag{5.3}
$$

Thus the next first-phase gradient degree beats every carried
$p$-coordinate row by row. For the second phase,

$$
BAu_n-u_n=(C-I)u_n>0, \tag{5.4}
$$

so every fresh second-phase gradient degree beats its carried
$q$-coordinate. The two strict selector margins from Step 3 choose the
competitive gradient rows. Equations (5.2)–(5.4) close the phase-labelled
degree induction, subject only to survival of the selected leading forms.

For nonzero polynomials $f$ and $g$ over a field,

$$
\operatorname{LH}(fg)=\operatorname{LH}(f)\operatorname{LH}(g)\ne0
$$

because the polynomial ring is an integral domain. If $\deg f>\deg g$, then

$$
\operatorname{LH}(f+g)=\operatorname{LH}(f).
$$

At each coordinate update, Steps 3 and 5 provide a unique highest-degree
source among the carried term and every gradient competitor. That source is
a nonzero scalar times a product or power of earlier nonzero leading forms.
The domain property makes the product nonzero, and the strict degree gap
prevents another summand from canceling it. Induction now proves

$$
v_{n+1}=Au_n,\qquad u_{n+1}=Cu_n\qquad(n\ge0). \tag{5.5}
$$

No positivity-of-coefficients assumption is needed for this conclusion.

### Step 6 — Last-coordinate visibility and exact degree

Direct subtraction gives $C-A>0$ entrywise. More explicitly:

- its first row is
  $(4m+4,4m+2,\ldots,4m+2)$;
- in a middle row $i$, the first entry is $2h+4m$, and the entry in column
  $j\ge2$ is $4m-2+2\mathbf1_{\{i=j\}}$;
- its last row has entries $2h-2$ before the last position and $h-1$ in the
  last position.

All entries are positive for $m\ge2$ and $h\ge2m+4$. Hence

$$
Cu>Au\qquad(u>0). \tag{6.1}
$$

Step 4 already proves $(Cu)_r>(Cu)_1$. Fix a middle index
$2\le i<r$ and put

$$
s=\sum_{j=2}^{r-1}x_j.
$$

Then $s\ge m$, $\sigma=s+x_r$, and
$x_r<(h-1)/2-s$. Direct row subtraction gives

$$
L_i:=\frac{(Cu)_r-(Cu)_i}{u_1}
=(2h-4m)\sigma-hx_r-x_i-4m-2. \tag{6.2}
$$

Equivalently,

$$
L_i=(2h-4m)s+(h-4m)x_r-x_i-4m-2.
$$

Put $b_i=h-4m$. If $b_i<0$, use the strict upper bound on $x_r$ with the
reversed inequality:

$$
\begin{aligned}
L_i
&>hs-x_i+\frac{b_i(h-1)}2-4m-2\\
&\ge hm-1+\frac{b_i(h-1)}2-4m-2\\
&=\frac{(h+2)(h-2m-3)}2>0.
\end{aligned} \tag{6.3}
$$

The second line uses

$$
hs-x_i=(h-1)x_i+h\sum_{\substack{2\le j<r\\j\ne i}}x_j
\ge(h-1)+h(m-1)=hm-1.
$$

If $b_i\ge0$, every coefficient is minimized on the lower faces
$x_2=\cdots=x_r=1$, and

$$
L_i\ge(2m+1)(h-2m-3)>0. \tag{6.4}
$$

Therefore $(Cu)_r$ strictly exceeds every other component of $Cu$. At the
$n$-th full iterate with $n\ge1$, the $q$-degree vector is

$$
u_n=C^n\mathbf1,
$$

and the $p$-degree vector is

$$
v_n=AC^{n-1}\mathbf1.
$$

Equation (6.1) makes $u_{n,i}>v_{n,i}$ for every $i$, while (6.3)–(6.4)
and Step 4 make $u_{n,r}>u_{n,i}$ for $i<r$. Thus the last $q$-coordinate
strictly dominates all other $2r-1$ coordinates for $n\ge1$, and

$$
\deg(F^n)=e_r^{\mathsf T}C^n\mathbf1\qquad(n\ge1). \tag{6.5}
$$

At $n=0$, every coordinate degree is one, and
$e_r^{\mathsf T}C^0\mathbf1=1$; the equality extends to $n=0$ without
strict visibility.

The matrix $C$ is entrywise positive. Perron–Frobenius gives a positive
Perron eigenvector and a simple eigenvalue $\rho(C)>0$ dominating the modulus
of every other eigenvalue. Both the seed $\mathbf1$ and the functional
$e_r^{\mathsf T}$ are positive on that Perron direction. Applying the theorem
to (6.5) gives

$$
\lim_{n\to\infty}\deg(F^n)^{1/n}=\rho(C).
$$

By the definition of the first dynamical degree in this package,

$$
\lambda_1(F)=\rho(C). \tag{6.6}
$$

### Step 7 — Invariant unit space and the three-dimensional complement

Define

$$
U=\left\{z\in K^r:z_1=z_r=0,\
\sum_{i=2}^{r-1}z_i=0\right\}.
$$

There are $m$ middle coordinates subject to one linear relation, so
$\dim U=m-1=r-3$. Every $z\in U$ has total coordinate sum zero. The mixed
matrix therefore satisfies $Mz=-z$. Replacing the first row by $he_1^{\mathsf
T}$ leaves its value zero because $z_1=0$, and replacing the last row by
$he_r^{\mathsf T}$ leaves its value zero because $z_r=0$. Hence

$$
Az=-z,\qquad Bz=-z,\qquad Cz=z\qquad(z\in U). \tag{7.1}
$$

Let

$$
E=\{(a,b,\ldots,b,c)^{\mathsf T}:a,b,c\in K\}.
$$

The intersection $U\cap E$ is zero: a vector there has $a=c=0$ and
$mb=0$, and characteristic zero makes the nonzero integer $m$ invertible in
$K$. Since $\dim U+\dim E=(r-3)+3=r$,

$$
K^r=U\oplus E. \tag{7.2}
$$

Rows with middle indices are permutation-symmetric, so $A$, $B$, and $C$
preserve $E$. In the coordinate convention
$(a,b,c)\mapsto(a,b,\ldots,b,c)$, the restrictions of $A$ and $B$ are

$$
A_E=
\begin{pmatrix}
h&0&0\\
2&2m-1&2\\
2&2m&1
\end{pmatrix},
\qquad
B_E=
\begin{pmatrix}
1&2m&2\\
2&2m-1&2\\
0&0&h
\end{pmatrix}. \tag{7.3}
$$

Multiplication $Q=B_EA_E$ gives

$$
Q=
\begin{pmatrix}
h+4m+4 & 2m(2m+1) & 2(2m+1)\\
2h+4m+2 & 4m^2+1 & 4m\\
2h & 2mh & h
\end{pmatrix}. \tag{7.4}
$$

This fixes the quotient coordinate convention before any spectral
calculation.

### Step 8 — Cubic factor, exact unit multiplicity, and degree recurrence

The trace of $Q$ is

$$
\operatorname{tr}Q=2h+4m^2+4m+5. \tag{8.1}
$$

Its three principal $2\times2$ minors are

$$
h\bigl(1-4m(m+1)\bigr)+4,\qquad
h(h-4m),\qquad
h(1-4m^2). \tag{8.2}
$$

Their sum is

$$
h^2-8hm(m+1)+2h+4. \tag{8.3}
$$

From (7.3),

$$
\det A_E=-h(2m+1),\qquad
\det B_E=-h(2m+1).
$$

Therefore

$$
\det Q=h^2(2m+1)^2. \tag{8.4}
$$

The characteristic polynomial of $Q$ is consequently

$$
\begin{aligned}
P_{m,h}(t)
={}&t^3-(2h+4m^2+4m+5)t^2\\
&+(h^2-8hm(m+1)+2h+4)t\\
&-h^2(2m+1)^2.
\end{aligned} \tag{8.5}
$$

The invariant direct sum (7.2), together with (7.1), gives

$$
\chi_C(t)=(t-1)^{r-3}P_{m,h}(t). \tag{8.6}
$$

Direct substitution into (8.5) and collection yield

$$
P_{m,h}(1)=-4m(m+1)(h+1)^2. \tag{8.7}
$$

This value is nonzero in characteristic zero. Thus the restriction to $E$
has no eigenvalue $1$. The whole eigenvalue-$1$ generalized eigenspace is
therefore $U$, on which $C$ is the identity. Its algebraic and geometric
multiplicities are both exactly $r-3$.

The seed $\mathbf1$ belongs to $E$. Hence Cayley–Hamilton for $Q$ applies to
the entire orbit $C^n\mathbf1$. Define

$$
\begin{aligned}
T_0&=2h+4m^2+4m+5,\\
S_0&=h^2-8hm(m+1)+2h+4,\\
D_0&=h^2(2m+1)^2,
\end{aligned}
$$

and

$$
d_n=e_r^{\mathsf T}C^n\mathbf1.
$$

Then

$$
d_{n+3}=T_0d_{n+2}-S_0d_{n+1}+D_0d_n
\qquad(n\ge0), \tag{8.8}
$$

with

$$
d_0=1,\qquad d_1=h(2m+3),
$$

and $d_2=e_r^{\mathsf T}C^2\mathbf1$. This is an exact cubic annihilating
recurrence. Equation (8.8) need not be the minimal recurrence at every
parameter.

The positive Perron vector of $C$ is fixed by every permutation of the
middle coordinates, because $C$ commutes with those permutations and its
positive Perron ray is unique. It lies in $E$. Thus the Perron class belongs
to the three-dimensional restriction and is a root of $P_{m,h}$. No
irreducibility statement is used.

### Step 9 — Sharp seed/selected-face boundary and low-rank consistency

At the ordinary-degree seed, the first pure-row score is $h=g-1$ and the
mixed-row score is

$$
1+2(r-1)=2r-1.
$$

Their difference is

$$
g-2r. \tag{9.1}
$$

When $g=2r$, (9.1) vanishes. At the same parameter,

$$
\sigma(\mathbf1)=r-1=\frac{g-2}{2},
$$

so the seed lies on the boundary of the open cone. At $g=2r+1$, the selector
margin is one and the cone-height slack is one half. This proves sharpness
only for the stated seed and strict selected face. The argument does not
determine the true degree dynamics at $g=2r$ or below.

Formally set $r=3$, so $m=1$ and $h=g-1$. Equation (7.4) becomes

$$
\begin{pmatrix}
g+7&6&6\\
2g+4&5&4\\
2(g-1)&2(g-1)&g-1
\end{pmatrix},
$$

and (8.5) becomes

$$
t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2.
$$

These are exactly the matrix and cubic of Paper 21. This substitution is a
predecessor-consistency check. Paper 22 makes no new $r=3$ claim, does not
alter Paper 21's declared parameter range, and does not present a Paper 21
correction.

### Step 10 — Arbitrary nonzero coefficients on the fixed supports

Replace the potentials by

$$
V_{\alpha,\beta}
=\alpha\prod_{i=1}^r q_i^2+\beta q_1^g,\qquad
W_{\gamma,\delta}
=\gamma\prod_{i=1}^r p_i^2+\delta p_r^g,
$$

where $\alpha,\beta,\gamma,\delta\in K^\times$. Their derivative scalars are
$2\alpha$, $g\beta$, $2\gamma$, and $g\delta$, all nonzero because
$K$ has characteristic zero. The exponent supports and every strict degree
comparison remain unchanged.

For a universal bookkeeping argument, work first in the localization

$$
\mathbb Z[\alpha,\beta,\gamma,\delta,
q_1,\ldots,q_r,p_1,\ldots,p_r]
[(\alpha\beta\gamma\delta)^{-1}],
$$

which is an integral domain. Every uniquely selected leading form is a
nonzero scalar monomial in $\alpha,\beta,\gamma,\delta$ times a product of
earlier nonzero leading forms. After specialization to nonzero elements of
$K$, the same source term remains unique in degree, and its scalar factors
remain nonzero. Therefore no sign or phase choice among the four coefficients
can cancel it.

The matrices, exact degree sequence, quotient factorization, and Perron
formula are unchanged. If a coefficient vanishes or an additional monomial
is inserted, this proof no longer applies.

Combining Steps 1–10 proves every item in the claim. $\square$

## Corrections or Missing Assumptions

- The normalized sum is corrected and locked as
  $\sigma=\sum_{i=2}^r x_i$; it never includes $x_1$.
- Strict last-coordinate visibility is restricted to $n\ge1$; the exact
  degree formula at $n=0$ is a separate tied initial case.
- The cone is called an explicit sufficient invariant selector cone, not an
  exact, maximal, necessary, or classified cone.
- The sharp threshold is restricted to the stated seed and selected face.
- The coefficient corollary is restricted to four nonzero coefficients on
  the fixed supports.
- Characteristic zero is essential for the stated field-uniform result.
- No extra mathematical assumption beyond those displayed above is being
  silently added.

## Open Risks

- An independent reviewer must recompute every matrix entry and inequality;
  this author document is not a source-design PASS.
- A later manuscript must preserve the quotient coordinate convention and
  all index ranges without transcription drift.
- The bounded literature screen does not establish global priority.
- No claim is made that $P_{m,h}$ is irreducible or minimal for every
  parameter.
- Any extension to new supports, positive characteristic, or a broader
  selector classification requires a separate theorem and authorization.
