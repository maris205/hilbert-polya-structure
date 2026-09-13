# Proof Package

## Claim

Let $K$ be a field of characteristic zero.

### Part I: support-row factorization

Let

$$
A=-I_n+\mathsf P\mathsf Q,\qquad
B=-I_n+\mathsf R\mathsf S,\qquad
C=BA,
$$

where

$$
\mathsf P\in K^{n\times\alpha},\quad
\mathsf Q\in K^{\alpha\times n},\quad
\mathsf R\in K^{n\times\beta},\quad
\mathsf S\in K^{\beta\times n}.
$$

Put

$$
r=\operatorname{rank}
\begin{pmatrix}\mathsf Q\\ \mathsf S\end{pmatrix}.
$$

Then there are explicitly constructible matrices
$T_0\in K^{r\times n}$ and $X\in K^{n\times r}$ such that

$$
\boxed{
\chi_C(t)=(t-1)^{n-r}
\det\bigl((t-1)I_r-T_0X\bigr).}
$$

The factor after $(t-1)^{n-r}$ is monic of degree $r$. Consequently the
algebraic multiplicity of the unit eigenvalue is at least $n-r$, and the
characteristic degree not forced into this unit factor is at most $r$. The
reduced determinant may contain further copies of $t-1$.

### Part II: sharp positive Hamiltonian families

For every integer $d\ge2$, the following parameters can be chosen in order:

$$
d\longrightarrow p,c\longrightarrow
a_1<\cdots<a_d\longrightarrow b,R_0.
$$

They satisfy:

1. $p$ is prime and $p\equiv1\pmod d$;
2. $c\in\mathbb F_p^\times$ has order $p-1$;
3. the residues of $a_1,\ldots,a_d$ are exactly the $d$-th roots of unity
   in $\mathbb F_p$, and $a_1+1>4d$;
4. with $S_a=\sum_i a_i$ and $M=a_d$,

   $$
   bd\equiv1-(-1)^dc\pmod p,\qquad
   R_0=1+\frac{2M}{bS_a};
   $$

5. $b\ge2$, $R_0^2<2$, and

   $$
   b(a_i-a_1)S_a>a_i^2R_0-a_1^2
   \qquad(2\le i\le d).
   $$

Define on $\mathbb A_K^{2d}$:

$$
V(q)=\prod_{j=1}^d q_j^2+\sum_{i=1}^d q_i^{a_i+1},
\qquad
W(p)=\prod_{j=1}^d p_j^b,
$$

$$
S_V(q,p)=(q,p+\nabla V(q)),\qquad
T_W(q,p)=(q+\nabla W(p),p),\qquad
F=T_W\circ S_V.
$$

Let

$$
D=\operatorname{diag}(a_1,\ldots,a_d),\qquad
a=(a_1,\ldots,a_d)^{\mathsf T},\qquad
J=\mathbf1\mathbf1^{\mathsf T},
$$

$$
B_0=bJ-I_d,\qquad
C=B_0D=b\mathbf1a^{\mathsf T}-D.
$$

Then $S_V$, $T_W$, and $F$ are polynomial symplectomorphisms. The matrices
$D$ and $B_0$ are selected from the literal gradient supports, and the
ordinary total degrees satisfy

$$
\boxed{\deg(F^n)=e_1^{\mathsf T}C^n\mathbf1\qquad(n\ge0).}
$$

The coordinate $q_1$ is the unique degree-maximal coordinate for $n\ge1$.
Moreover,

$$
\boxed{
\chi_C(t)=
t^d+\sum_{k=1}^d(1-bk)e_k(a_1,\ldots,a_d)t^{d-k}}
$$

is irreducible over $\mathbb Q$ and reduces to $t^d-c$ modulo $p$.
Therefore

$$
\lambda_1(F)=\rho(C),
$$

the Perron algebraic integer $\rho(C)$ has algebraic degree exactly $d$, and
the scalar sequence

$$
s_n=e_1^{\mathsf T}C^n\mathbf1
$$

has minimal rational constant-coefficient recurrence order exactly $d$.
Finally, the support-row factorization bound is attained for every
constructed rank $r=d\ge2$.

## Status

**PROVABLE AS STATED**

The status applies to the exact restricted claim above. It does not apply to
any broader sign, support, exponent, coefficient, characteristic, inverse,
higher-degree, genericity, classification, or exact-unit-profile statement.

## Assumptions

1. The base field has characteristic zero.
2. Ordinary total degree is used for polynomial coordinate tuples.
3. The family has exactly the displayed positive integer coefficients and
   supports.
4. The parameters are chosen in the stated order and satisfy all displayed
   strict inequalities.
5. The scalar recurrence coefficients are rational constants. An order-$k$
   recurrence means a nonzero polynomial
   $f(x)=\sum_{j=0}^k f_jx^j$ with $f_k\ne0$ such that
   $\sum_{j=0}^k f_js_{n+j}=0$ on the stated range of $n$.
6. The dynamical degree in this package is the forward first dynamical
   degree defined from ordinary degree growth:

   $$
   \lambda_1(F)=\lim_{n\to\infty}\deg(F^n)^{1/n}.
   $$

   The proof establishes existence of this limit for the displayed family.

## Notation

- $\mathbf1$ is the all-ones column vector and $e_i$ is the $i$-th coordinate
  vector.
- $e_k(a_1,\ldots,a_d)$ is the $k$-th elementary symmetric polynomial.
- $D=\operatorname{diag}(a_1,\ldots,a_d)$.
- $S_a=\sum_i a_i$ and $M=a_d$.
- $R_0$ is the scalar cone ratio. The distinct symbol $\mathsf R$ is used for
  the matrix in Part I.
- The broad ratio cone and fine visibility chamber are

  $$
  \mathcal K_{\rm ratio}(R_0)
  =\{u\in\mathbb R_{>0}^d:
  \max_i u_i\le R_0\min_i u_i\},
  $$

  $$
  \mathcal K_{\rm vis}(R_0)
  =\{u\in\mathbb R_{>0}^d:
  u_i\le u_1<R_0u_i\ \text{and}\
  a_1u_1<a_i u_i\ \text{for every }i>1\}.
  $$

- For a nonzero polynomial $G$, $\operatorname{LF}(G)$ denotes its
  top-degree homogeneous form.
- $\rho(C)$ denotes the spectral radius of $C$.

## Proof Strategy

Part I is a direct row-space factorization followed by the rectangular
Sylvester determinant identity.

Part II is constructive. Dirichlet's theorem and finite-field cyclicity
provide residues; a large-lift and large-$b$ argument closes all parameter
inequalities. Direct differentiation identifies the selected degree
matrices. Two nested invariant regions separate the selection problem from
the fixed-coordinate visibility problem. A phase-labelled induction in the
positive integer coefficient semiring then upgrades selected weighted
degrees to exact polynomial degrees. A rank-one determinant calculation and
the finite-field irreducible-binomial criterion give irreducibility in every
$d$. Perron--Frobenius gives the growth limit, while cyclic reachability and
observability give exact scalar recurrence order. The selected presentations
then attain the abstract rank bound.

## Dependency Map

1. Part I depends on the row-basis factorization and Sylvester identity.
2. Parameter existence depends on Dirichlet's theorem, cyclicity of
   $\mathbb F_p^\times$, and a finite simultaneous large-$b$ choice.
3. Exact degree visibility depends on:
   - literal gradient rows;
   - broad-cone spike selection and strict invariance;
   - fine-chamber weighted invariance;
   - cross-phase domination and both temporal carries;
   - positive-semiring top-form survival.
4. Irreducibility depends on the characteristic formula, the prescribed
   residues, the exact binomial criterion, and Gauss's lemma.
5. Perron degree depends on exact visibility, strict positivity of $C$, and
   irreducibility.
6. Scalar minimality depends on irreducibility, cyclic reachability,
   cyclic observability, and the Hankel-rank criterion. A separate Perron
   limit argument covers recurrences required only on a tail.
7. Sharpness depends on Part I, the literal selected presentations, and the
   irreducible degree-$d$ characteristic polynomial.
8. Boundary cases $d=2$, $4\mid d$, $r=0$, the cone-boundary seed, and
   $n=0$ are checked separately below.

## Proof

### Step 1. Factor through the selected support-row space

Direct multiplication gives

$$
\begin{aligned}
C-I_n
&=(-I_n+\mathsf R\mathsf S)
  (-I_n+\mathsf P\mathsf Q)-I_n\\
&=-\mathsf P\mathsf Q-\mathsf R\mathsf S
  +\mathsf R\mathsf S\mathsf P\mathsf Q.
\end{aligned}
$$

Define

$$
U=
\begin{bmatrix}
\mathsf R\mathsf S\mathsf P-\mathsf P&-\mathsf R
\end{bmatrix}
\in K^{n\times(\alpha+\beta)},
\qquad
Y=
\begin{bmatrix}
\mathsf Q\\ \mathsf S
\end{bmatrix}
\in K^{(\alpha+\beta)\times n}.
$$

Their product is

$$
UY=
(\mathsf R\mathsf S\mathsf P-\mathsf P)\mathsf Q
-\mathsf R\mathsf S
=C-I_n.
$$

Choose a matrix $T_0\in K^{r\times n}$ whose rows are a basis of the row
space of $Y$. Every row of $Y$ is a linear combination of these basis rows,
so there is a matrix

$$
L\in K^{(\alpha+\beta)\times r}
$$

such that $Y=LT_0$. With $X=UL\in K^{n\times r}$, one obtains

$$
C=I_n+XT_0.
$$

Put $z=t-1$. Over the rational function field $K(z)$,

$$
\begin{aligned}
\det(zI_n-XT_0)
&=z^n\det(I_n-z^{-1}XT_0)\\
&=z^n\det(I_r-z^{-1}T_0X)\\
&=z^{n-r}\det(zI_r-T_0X).
\end{aligned}
$$

The middle equality is the rectangular Sylvester identity
$\det(I_n+XY)=\det(I_r+YX)$ for compatible
$X\in K(z)^{n\times r}$ and $Y\in K(z)^{r\times n}$. Both outer
expressions are polynomials in $z$, so equality in $K(z)$ gives equality in
$K[z]$, including at $z=0$. Hence

$$
\chi_C(t)
=(t-1)^{n-r}
\det\bigl((t-1)I_r-T_0X\bigr).
$$

The determinant on the right is monic of degree $r$ because its highest
term is $\det((t-1)I_r)=(t-1)^r$.

There is also a kernel check. Since $T_0$ and $Y$ have the same row space,

$$
\ker T_0=\ker Y=\ker\mathsf Q\cap\ker\mathsf S
$$

has dimension $n-r$. If $v$ belongs to this kernel, then

$$
Av=-v,\qquad Bv=-v,\qquad Cv=B(-v)=v.
$$

Thus the geometric multiplicity of the unit eigenvalue is at least $n-r$,
and so is its algebraic multiplicity. The reduced determinant can vanish at
$t=1$; neither derivation rules that out. This proves Part I with the stated
lower-bound-only conclusion.

### Step 2. Construct the parameters in the required order

Fix $d\ge2$. Dirichlet's theorem on primes in arithmetic progressions applies
to the coprime residue and modulus pair $(1,d)$, so there is a prime
$p\equiv1\pmod d$. In particular, $d\mid p-1$ and $p\nmid d$.

The multiplicative group $\mathbb F_p^\times$ is cyclic of order $p-1$.
Choose a generator $c$, so

$$
\operatorname{ord}_{\mathbb F_p^\times}(c)=p-1.
$$

In a cyclic group of order $p-1$, the equation $x^d=1$ has
$\gcd(d,p-1)=d$ solutions. Let

$$
1\le r_1<r_2<\cdots<r_d\le p-1
$$

be the least positive integer representatives of these $d$ roots, sorted as
integers. Choose one integer $N$ large enough that

$$
a_1=Np+r_1
$$

satisfies $a_1+1>4d$, and put

$$
a_i=Np+r_i\qquad(1\le i\le d).
$$

Then $a_1<\cdots<a_d$, every $a_i$ is positive, and their residue set is
exactly the set of $d$-th roots of unity.

Because $p\nmid d$, multiplication by $d$ is invertible modulo $p$. Hence

$$
bd\equiv1-(-1)^dc\pmod p
$$

defines one residue class for $b$. That class contains arbitrarily large
positive integers. Freeze the $a_i$, set $S_a=\sum_i a_i$ and $M=a_d$, and
let $b$ tend to infinity within the prescribed class. Then

$$
R_0=1+\frac{2M}{bS_a}\longrightarrow1.
$$

Therefore $b\ge2$ and $R_0^2<2$ hold for all sufficiently large choices in
that class. For each fixed $i>1$,

$$
b(a_i-a_1)S_a
$$

tends linearly to positive infinity, whereas

$$
a_i^2R_0-a_1^2
$$

tends to the finite number $a_i^2-a_1^2$. Only $d-1$ inequalities occur.
One sufficiently large $b$ in the fixed residue class therefore satisfies
all of them at once. The lifts were frozen before this final choice, so the
quantifier order is noncircular.

### Step 3. Prove symplecticity and identify the literal selected rows

For the standard symplectic form

$$
\omega=\sum_{i=1}^d dq_i\wedge dp_i,
$$

the pullback under $S_V$ is

$$
S_V^*\omega
=\sum_i dq_i\wedge
\left(dp_i+\sum_j
\frac{\partial^2V}{\partial q_i\partial q_j}dq_j\right).
$$

The extra double sum vanishes because the Hessian of $V$ is symmetric:
the $(i,j)$ and $(j,i)$ terms have equal coefficients and opposite wedge
products, while diagonal wedge products vanish. Thus $S_V^*\omega=\omega$.
The corresponding calculation for $T_W$ uses the symmetric Hessian of $W$
and gives $T_W^*\omega=\omega$. The inverses are

$$
S_V^{-1}(q,p)=(q,p-\nabla V(q)),\qquad
T_W^{-1}(q,p)=(q-\nabla W(p),p).
$$

Hence both shears and their composition are polynomial
symplectomorphisms.

The derivatives are

$$
\frac{\partial V}{\partial q_i}
=2q_i\prod_{j\ne i}q_j^2
+(a_i+1)q_i^{a_i},
$$

$$
\frac{\partial W}{\partial p_i}
=b\,p_i^{b-1}\prod_{j\ne i}p_j^b.
$$

For a positive degree vector $u=(u_1,\ldots,u_d)^{\mathsf T}$ assigned to
the $q$-coordinates, the two $V$ competitors in component $i$ have weighted
degrees

$$
2\sum_{j=1}^d u_j-u_i
\quad\text{and}\quad
a_i u_i.
$$

When the spike is selected, the momentum degree vector is $Du$. For a
momentum degree vector $v$, the unique $W$ monomial in component $i$ has
degree

$$
b\sum_{j=1}^d v_j-v_i,
$$

so its row matrix is $B_0=bJ-I_d$. The complete selected matrix is

$$
C=B_0D=b\mathbf1a^{\mathsf T}-D.
$$

Its entries are

$$
C_{ii}=(b-1)a_i>0,\qquad C_{ij}=ba_j>0\quad(i\ne j).
$$

Thus $C$ is strictly positive.

### Step 4. Establish the two-level cone relation and seed entry

Since $R_0=1+2M/(bS_a)$, one has $R_0>1$. The ordinary seed
$\mathbf1$ belongs to $\mathcal K_{\rm ratio}(R_0)$.

It also belongs to $\mathcal K_{\rm vis}(R_0)$. For every $i>1$,

$$
1\le1<R_0
$$

verifies the coordinate inequalities, and $a_1<a_i$ verifies
$a_1<a_i$. Equality at $u_i\le u_1$ is permitted by the definition.

If $u\in\mathcal K_{\rm vis}(R_0)$, then $u_i\le u_1$ for every $i$ and
$u_i>u_1/R_0$ for every $i>1$. Hence the largest coordinate is $u_1$ and
every coordinate is greater than or equal to $u_1/R_0$, with a strict
inequality away from the first coordinate. Therefore

$$
\frac{\max_i u_i}{\min_i u_i}<R_0,
$$

so

$$
\mathcal K_{\rm vis}(R_0)
\subset\mathcal K_{\rm ratio}(R_0).
$$

The broad cone will control selection and blockwise carry. The finer chamber
will control which position coordinate is visible.

### Step 5. Prove spike selection and strict invariance on the broad cone

Take $u\in\mathcal K_{\rm ratio}(R_0)$ and set

$$
m=\min_i u_i,\qquad H=a^{\mathsf T}u.
$$

Since every $u_j\le R_0m$,

$$
2\sum_j u_j-u_i
\le(2dR_0-1)m.
$$

The spike degree satisfies

$$
a_i u_i\ge a_1m.
$$

The assumptions $a_1+1>4d$ and $R_0<\sqrt2<2$ give

$$
a_1>4d-1>2dR_0-1.
$$

Thus

$$
a_i u_i>2\sum_j u_j-u_i
$$

for every component. Every spike is selected strictly on the entire broad
cone.

Now write

$$
z=Cu,\qquad z_i=bH-a_i u_i.
$$

Positivity of $C$ gives $z_i>0$. Also,

$$
H\ge S_am,\qquad a_i u_i\le MR_0m.
$$

Consequently

$$
\frac{\max_i z_i}{\min_i z_i}
\le
\frac{bH}{bH-MR_0m}
\le
\frac{bS_a}{bS_a-MR_0}
=
\frac{1}{1-\frac{MR_0}{bS_a}}.
$$

The middle inequality follows because $x/(x-k)$ decreases for $x>k>0$ and
$bH\ge bS_am$. From the definition of $R_0$,

$$
\frac{M}{bS_a}=\frac{R_0-1}{2}.
$$

The denominator is positive because

$$
R_0(R_0-1)=R_0^2-R_0<2-R_0<1.
$$

Finally,

$$
\frac{1}{1-\frac{R_0(R_0-1)}2}<R_0
$$

is equivalent, after multiplying by the positive denominator, to

$$
(R_0-1)\left(1-\frac{R_0^2}{2}\right)>0.
$$

Both factors are positive. Therefore

$$
C\mathcal K_{\rm ratio}(R_0)
\subset\operatorname{int}\mathcal K_{\rm ratio}(R_0).
$$

### Step 6. Prove fine-chamber invariance and fixed-coordinate ordering

Take $u\in\mathcal K_{\rm vis}(R_0)$, put $s=u_1$, and set

$$
H=a^{\mathsf T}u,\qquad w=Cu.
$$

The chamber inequalities imply

$$
u_j\le s\quad\text{for every }j,\qquad
u_j>\frac{s}{R_0}\quad\text{for }j>1.
$$

Since $s>s/R_0$ as well,

$$
H>\frac{S_a}{R_0}s.
$$

For each $i>1$, the weighted chamber inequality gives

$$
w_1-w_i
=(bH-a_1s)-(bH-a_i u_i)
=a_i u_i-a_1s>0.
$$

Hence $w_i<w_1$. For the upper ratio wall,

$$
\begin{aligned}
R_0w_i-w_1
&=(R_0-1)bH-R_0a_i u_i+a_1s\\
&>
\left(
\frac{(R_0-1)bS_a}{R_0}
-R_0M+a_1
\right)s\\
&=
\left(
\frac{2M}{R_0}-R_0M+a_1
\right)s\\
&=
\left(
\frac{M(2-R_0^2)}{R_0}+a_1
\right)s>0.
\end{aligned}
$$

Therefore $w_1<R_0w_i$.

For the weighted wall,

$$
\begin{aligned}
a_iw_i-a_1w_1
&=b(a_i-a_1)H-a_i^2u_i+a_1^2s\\
&>
\left(
\frac{b(a_i-a_1)S_a}{R_0}
-a_i^2+a_1^2
\right)s.
\end{aligned}
$$

The parameter inequality

$$
b(a_i-a_1)S_a>a_i^2R_0-a_1^2
$$

implies

$$
\frac{b(a_i-a_1)S_a}{R_0}
>a_i^2-\frac{a_1^2}{R_0}.
$$

Substitution yields

$$
a_iw_i-a_1w_1
>a_1^2\left(1-\frac1{R_0}\right)s>0.
$$

Every defining wall is preserved, so

$$
C\mathcal K_{\rm vis}(R_0)
\subset\mathcal K_{\rm vis}(R_0).
$$

The inequalities $w_i<w_1$ are strict for $i>1$. Starting from
$u_0=\mathbf1$, the orbit

$$
u_n=C^n\mathbf1
$$

remains in the fine chamber, and its first coordinate is uniquely largest
for every $n\ge1$.

### Step 7. Prove all carries, top-form survival, and exact ordinary degrees

First establish a comparison that holds throughout the broad cone. For
$u\in\mathcal K_{\rm ratio}(R_0)$ and $m=\min_i u_i$,

$$
(Cu)_i=bH-a_i u_i\ge(bS_a-MR_0)m.
$$

Also,

$$
\max_j a_j u_j\le MR_0m.
$$

It remains to compare the two right sides. From
$bS_a=2M/(R_0-1)$,

$$
bS_a>2MR_0
$$

is equivalent to $R_0(R_0-1)<1$. This inequality was proved in Step 5 from
$R_0^2<2$. Therefore

$$
\boxed{(Cu)_i>\max_j a_j u_j\quad\text{for every }i.}
$$

Since $a_j>1$, this also gives $(Cu)_i>u_i$ for each $i$.

We now track literal coordinate polynomials. Let
$Q_i^{(n)}$ and $P_i^{(n)}$ be the coordinates of $F^n$, with
$F^0$ the identity. Initially all coordinate degrees are one and all
coefficients lie in

$$
\mathbb Z_{\ge0}[q_1,\ldots,q_d,p_1,\ldots,p_d].
$$

Suppose the $q$-degree vector at the start of the $(n+1)$-st application is
$u_n$. On the $V$-half-step, Step 5 proves that the spike term

$$
(a_i+1)(Q_i^{(n)})^{a_i}
$$

has strictly larger degree than the product-gradient competitor in
component $i$. At $n=0$, its degree $a_i$ is greater than the carried
momentum degree one. For $n\ge1$, the carried momentum degree is

$$
a_i u_{n-1,i},
$$

while the fresh spike degree is $a_i u_{n,i}$. The cross comparison above
gives $u_n>u_{n-1}$ componentwise, so the fresh spike wins strictly. Hence
the momentum degree vector after the $V$-half-step is exactly

$$
Du_n.
$$

On the $W$-half-step, component $i$ has one gradient monomial. Its degree is

$$
(B_0Du_n)_i=(Cu_n)_i.
$$

The boxed cross comparison shows that this degree exceeds every component of
$Du_n$, and it also exceeds the carried position degree $u_{n,i}$. Thus the
position degree vector after the complete step is exactly

$$
u_{n+1}=Cu_n.
$$

This proves all temporal carries at both half-steps.

It remains to justify that no selected top form vanishes. The coordinate
variables start with coefficient one. Both shears use only addition,
multiplication, and positive integer coefficients. Composition therefore
keeps every coordinate in the nonnegative integer coefficient semiring.
Strict selection gives one greater-degree source at every addition where
two sources compete. The top form of a positive power or product of nonzero
polynomials is the corresponding power or product of their nonzero top
forms, and a polynomial ring over an integral domain has no zero divisors.
The embedding $\mathbb Z\hookrightarrow K$ is injective because
$\operatorname{char}K=0$. Hence every positive integer coefficient remains
nonzero after base change to $K$, and every selected top form survives.

Induction gives

$$
u_n=C^n\mathbf1.
$$

At $n\ge1$, Step 6 makes $q_1$ the unique largest coordinate within the
position block. Applied to $u_{n-1}$, the boxed comparison shows that every
position degree in $u_n$ is greater than every momentum degree in
$Du_{n-1}$. Thus $q_1$ is the unique total-degree coordinate for every
$n\ge1$. At $n=0$, every coordinate has degree one. Therefore

$$
\deg(F^n)=e_1^{\mathsf T}C^n\mathbf1
\qquad(n\ge0).
$$

This is an equality of ordinary polynomial degrees, not a matrix upper
bound.

### Step 8. Derive the characteristic polynomial

Since

$$
tI_d-C=tI_d+D-b\mathbf1a^{\mathsf T},
$$

the rank-one matrix determinant lemma over $\mathbb Q(t)$ gives

$$
\begin{aligned}
\chi_C(t)
&=\det(tI_d+D)
\left(1-ba^{\mathsf T}(tI_d+D)^{-1}\mathbf1\right)\\
&=\prod_{i=1}^d(t+a_i)
-b\sum_{i=1}^d a_i\prod_{j\ne i}(t+a_j).
\end{aligned}
$$

For a fixed $k$, each squarefree product of $k$ distinct $a_i$ occurs once
in $e_k(a)$. In

$$
\sum_i a_i\prod_{j\ne i}(t+a_j),
$$

the same product occurs once for each choice of its distinguished index
$i$, hence exactly $k$ times. Therefore the coefficient of $t^{d-k}$ is

$$
(1-bk)e_k(a_1,\ldots,a_d),
$$

and

$$
\chi_C(t)=
t^d+\sum_{k=1}^d(1-bk)e_k(a_1,\ldots,a_d)t^{d-k}.
$$

### Step 9. Prove modular and rational irreducibility

Modulo $p$, the residues of the $a_i$ are exactly the roots of $x^d-1$.
Thus

$$
\prod_{i=1}^d(x-a_i)\equiv x^d-1\pmod p.
$$

Comparing coefficients gives

$$
e_k(a_1,\ldots,a_d)\equiv0\pmod p
\qquad(1\le k<d),
$$

and comparison of constant terms gives

$$
(-1)^de_d(a_1,\ldots,a_d)\equiv-1\pmod p,
$$

so

$$
e_d(a_1,\ldots,a_d)\equiv(-1)^{d+1}\pmod p.
$$

The congruence for $b$ is equivalent to

$$
1-bd\equiv(-1)^dc\pmod p.
$$

Using Step 8,

$$
\begin{aligned}
\chi_C(t)
&\equiv
t^d+(1-bd)e_d(a)\pmod p\\
&\equiv
t^d+(-1)^dc\,(-1)^{d+1}\pmod p\\
&\equiv t^d-c\pmod p.
\end{aligned}
$$

We now check every hypothesis of the finite-field irreducible-binomial
criterion. For $x^m-\gamma\in\mathbb F_q[x]$ with $\gamma\ne0$, that
criterion states that the binomial is irreducible precisely when:

1. every prime divisor of $m$ divides
   $\operatorname{ord}_{\mathbb F_q^\times}(\gamma)$;
2. $\gcd\!\left(m,
   (q-1)/\operatorname{ord}_{\mathbb F_q^\times}(\gamma)\right)=1$;
3. if $4\mid m$, then $q\equiv1\pmod4$.

Here $m=d$, $q=p$, and $\gamma=c$. Since $c$ is a generator,

$$
\operatorname{ord}(c)=p-1.
$$

Every prime divisor of $d$ divides $p-1$ because $d\mid p-1$. The quotient

$$
\frac{p-1}{\operatorname{ord}(c)}
$$

equals one, so its greatest common divisor with $d$ is one. If $4\mid d$,
then $p\equiv1\pmod d$ implies $p\equiv1\pmod4$. All three conditions hold,
so $t^d-c$ is irreducible in $\mathbb F_p[t]$.

The polynomial $\chi_C$ is monic with integer coefficients, and its reduction
is monic of the same degree $d$. If $\chi_C$ factored over $\mathbb Q$,
Gauss's lemma would give a factorization into positive-degree monic
polynomials in $\mathbb Z[t]$. Reducing those monic factors modulo $p$ would
give a nontrivial factorization of $t^d-c$, a contradiction. Therefore
$\chi_C$ is irreducible over $\mathbb Q$.

### Step 10. Identify the Perron dynamical degree and its algebraic degree

Step 3 showed that every entry of $C$ is strictly positive. The
Perron--Frobenius theorem for a strictly positive real matrix therefore gives:

1. a positive eigenvalue $\rho(C)$ equal to the spectral radius;
2. positive right and left eigenvectors $r$ and $\ell$;
3. algebraic and geometric simplicity of $\rho(C)$; and
4. an inequality $|\mu|<\rho(C)$ for every other eigenvalue $\mu$.

Normalize only by requiring $\ell^{\mathsf T}r\ne0$. With

$$
s_n=e_1^{\mathsf T}C^n\mathbf1,
$$

the spectral projection onto the Perron eigenspace gives

$$
s_n=
\gamma\rho(C)^n+O(\theta^n),
$$

where

$$
\gamma=
\frac{(e_1^{\mathsf T}r)(\ell^{\mathsf T}\mathbf1)}
{\ell^{\mathsf T}r}>0
$$

and $0\le\theta<\rho(C)$. Step 7 identifies $s_n$ with
$\deg(F^n)$. Taking $n$-th roots yields

$$
\lambda_1(F)
=\lim_{n\to\infty}\deg(F^n)^{1/n}
=\rho(C).
$$

The number $\rho(C)$ is a root of the irreducible degree-$d$ polynomial
$\chi_C\in\mathbb Z[t]$. Its minimal polynomial over $\mathbb Q$ is
therefore $\chi_C$. Hence $\rho(C)$ is an algebraic integer of degree
exactly $d$. The strict Perron spectral gap shows that all its other
conjugates have modulus strictly below $\rho(C)$, so it is a Perron
algebraic integer.

### Step 11. Prove exact scalar recurrence order

Write

$$
\chi_C(t)=t^d+\eta_1t^{d-1}+\cdots+\eta_d.
$$

Cayley--Hamilton gives

$$
C^d+\eta_1C^{d-1}+\cdots+\eta_dI_d=0.
$$

Multiplying on the left by $e_1^{\mathsf T}C^n$ and on the right by
$\mathbf1$ gives an order-$d$ rational recurrence for $s_n$ for every
$n\ge0$. This proves order at most $d$.

To prove minimality, first show reachability. If the vectors

$$
\mathbf1,C\mathbf1,\ldots,C^{d-1}\mathbf1
$$

were linearly dependent over $\mathbb Q$, a nonzero polynomial $f$ of
degree less than $d$ would satisfy $f(C)\mathbf1=0$. Since $\chi_C$ is
irreducible and $\deg f<d$, the polynomials $f$ and $\chi_C$ are coprime.
Bézout's identity supplies $g,h\in\mathbb Q[t]$ with

$$
g(t)f(t)+h(t)\chi_C(t)=1.
$$

Applying this identity at $C$ to $\mathbf1$, and using
$\chi_C(C)=0$, would give $\mathbf1=0$, a contradiction. Thus the
reachability matrix

$$
\mathcal R_C=
\begin{bmatrix}
\mathbf1&C\mathbf1&\cdots&C^{d-1}\mathbf1
\end{bmatrix}
$$

is invertible.

Apply the same argument to $C^{\mathsf T}$ and the nonzero vector $e_1$.
The characteristic polynomial of $C^{\mathsf T}$ is the same irreducible
$\chi_C$, so

$$
e_1,C^{\mathsf T}e_1,\ldots,
(C^{\mathsf T})^{d-1}e_1
$$

is a basis. Equivalently, the observability matrix

$$
\mathcal O_C=
\begin{bmatrix}
e_1^{\mathsf T}\\
e_1^{\mathsf T}C\\
\vdots\\
e_1^{\mathsf T}C^{d-1}
\end{bmatrix}
$$

is invertible.

Their product is the $d\times d$ Hankel matrix

$$
\mathcal H_d=
\mathcal O_C\mathcal R_C
=
\left(
e_1^{\mathsf T}C^{i+j}\mathbf1
\right)_{0\le i,j<d}
=(s_{i+j})_{0\le i,j<d}.
$$

Therefore

$$
\operatorname{rank}\mathcal H_d=d.
$$

If a recurrence of order $k<d$ held for every $n\ge0$, every Hankel column
from index $k$ onward would be a rational linear combination of the first
$k$ columns. That would force
$\operatorname{rank}\mathcal H_d\le k<d$, contradicting the displayed
rank. Hence no lower-order recurrence holds from the start.

The same lower bound holds even if a recurrence is required only for all
sufficiently large $n$. Suppose

$$
\sum_{j=0}^k f_js_{n+j}=0
$$

for every $n\ge N$, where $f_k\ne0$ and $k<d$. Put
$f(t)=\sum_{j=0}^k f_jt^j$. Using Step 10,

$$
\sum_{j=0}^k f_js_{n+j}
=\gamma\rho(C)^n f(\rho(C))+O(\theta^n).
$$

Divide by $\rho(C)^n$ and let $n$ tend to infinity. The left side is zero
and $\theta/\rho(C)<1$, so

$$
f(\rho(C))=0.
$$

This contradicts the fact that the minimal polynomial of $\rho(C)$ has
degree $d>k$. Thus the minimal rational constant-coefficient recurrence
order is exactly $d$.

### Step 12. Attain the support-rank bound

For the selected family,

$$
D=-I_d+I_d(D+I_d),
$$

so in the notation of Part I one may take

$$
\mathsf P=I_d,\qquad \mathsf Q=D+I_d.
$$

Also,

$$
B_0=bJ-I_d=-I_d+(b\mathbf1)\mathbf1^{\mathsf T},
$$

so one may take

$$
\mathsf R=b\mathbf1,\qquad \mathsf S=\mathbf1^{\mathsf T}.
$$

The matrix $D+I_d$ is diagonal with nonzero diagonal entries
$a_i+1$, so it is invertible. Hence

$$
\operatorname{rank}
\begin{pmatrix}
D+I_d\\ \mathbf1^{\mathsf T}
\end{pmatrix}
=d.
$$

Thus the stacked support-row rank is $r=d$. The characteristic polynomial
is irreducible of degree $d\ge2$, so it cannot contain the linear factor
$t-1$. Its entire degree $d$ is nonunit. Therefore the upper bound $r$ from
Part I is attained for each constructed rank $r=d\ge2$. This is existential
sharpness; it does not say that every rank-$r$ presentation attains the
bound.

The two parts of the claim are now proved. $\square$

## Boundary Cases

### The case $d=2$

The congruence $p\equiv1\pmod2$ selects an odd prime, so
$\mathbb F_p^\times$ has even order. A generator $c$ is not a square because
the squares form the index-two subgroup. Thus $t^2-c$ is irreducible. The
congruence for $b$ is soluble because $p\nmid2$. There is one visibility
inequality, and the large-$b$ argument satisfies it together with
$a_1+1>8$ and $R_0^2<2$.

### The case $4\mid d$

The irreducible-binomial criterion has a separate condition
$p\equiv1\pmod4$. Since $p\equiv1\pmod d$ and $4\mid d$, this condition
holds. It is checked rather than omitted.

### The cases $r=0$ and $r=n$ in Part I

If $r=0$, then $Y=0$, $C=I_n$, and the formula reads

$$
\chi_C(t)=(t-1)^n
$$

with the determinant of the empty matrix interpreted as one. If $r=n$, the
forced unit factor has exponent zero and the reduced determinant has degree
$n$. Part II uses the latter boundary with $n=r=d$.

### The ordinary seed and $n=0$

The seed $\mathbf1$ lies on the permitted walls $u_i=u_1$ of
$\mathcal K_{\rm vis}$. The other chamber inequalities are strict because
$R_0>1$ and $a_i>a_1$. At $n=0$, all $2d$ coordinate degrees equal one, so
$q_1$ is not uniquely visible. The exact scalar formula still gives
$e_1^{\mathsf T}\mathbf1=1$. Unique visibility begins at $n=1$.

### Additional unit roots in the abstract factor

Part I does not prevent

$$
\det((t-1)I_r-T_0X)
$$

from vanishing at $t=1$. Exact unit multiplicity and an exact rank profile
would require additional hypotheses not present here.

### Characteristic zero

The determinant calculations themselves have a broader algebraic range, but
the family theorem is stated only in characteristic zero. This restriction
ensures that every positive integer derivative coefficient remains nonzero
and that the positive-semiring top-form induction survives base change. No
positive-characteristic family theorem is inferred from the modular
irreducibility device.

## Corrections or Missing Assumptions

No missing mathematical assumption remains after the following explicit
normalizations:

1. “Primitive” means order exactly $p-1$ in $\mathbb F_p^\times$.
2. The broad ratio cone and fine visibility chamber are distinct, nested
   proof devices with separately proved roles.
3. Unit multiplicity in Part I is a lower bound, not an equality.
4. Visibility is unique only for positive iterates.
5. Minimal scalar recurrence order is over rational constant coefficients;
   both from-start and eventual versions are proved.
6. “Every rank” means every nontrivial rank $r=d\ge2$ constructed by Part II.
   No rank-zero or rank-one Hamiltonian sharp family is claimed.
7. Characteristic zero and the displayed positive supports are essential
   stated restrictions.

## Open Risks

1. An independent source-design reviewer has not yet rederived this package.
2. The exact bibliographic metadata and theorem number for the
   irreducible-binomial criterion must be verified from a primary record
   before bibliography lock.
3. A future manuscript must preserve the direction and strictness of every
   cone, carry, and visibility inequality; compressing the two-level cone
   proof could reintroduce a gap.
4. A future manuscript must keep matrix dimension, scalar recurrence order,
   and algebraic degree as distinct notions until Steps 10 and 11 connect
   them.
5. The bounded literature screen supports no exhaustive collision or
   priority conclusion.

No numerical, CAS, genericity, or hidden-certificate risk remains because
none is used as evidence.
