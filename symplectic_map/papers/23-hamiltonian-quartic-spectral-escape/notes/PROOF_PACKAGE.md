# Proof Package

## Claim

Let $K$ be a field of characteristic zero and let $g\ge10$ be an integer.
For $q=(q_1,q_2,q_3,q_4)$ and $p=(p_1,p_2,p_3,p_4)$, define

$$
V_g(q)=q_1^2q_2^2q_3^2q_4^2+q_1^g+q_2^{g-1},
$$

$$
W_g(p)=p_1^2p_2^2p_3^2p_4^2+p_3^{g-1}+p_4^g,
$$

and the positive-sign shears

$$
S_g^+(q,p)=(q,p+\nabla V_g(q)),\qquad
T_g^+(q,p)=(q+\nabla W_g(p),p).
$$

Fix the phase order

$$
F_g=T_g^+\circ S_g^+.
$$

Then:

1. $F_g$ is a polynomial symplectic automorphism of $K^8$.
2. The actual coordinate degrees of its iterates are governed by
   $$
   A_g=
   \begin{pmatrix}
   g-1&0&0&0\\
   0&g-2&0&0\\
   2&2&1&2\\
   2&2&2&1
   \end{pmatrix},
   \qquad
   B_g=
   \begin{pmatrix}
   1&2&2&2\\
   2&1&2&2\\
   0&0&g-2&0\\
   0&0&0&g-1
   \end{pmatrix},
   $$
   and
   $$
   C_g=B_gA_g=
   \begin{pmatrix}
   g+7&2g+4&6&6\\
   2g+6&g+6&6&6\\
   2g-4&2g-4&g-2&2g-4\\
   2g-2&2g-2&2g-2&g-1
   \end{pmatrix}.
   $$
3. If $u_n$ is the four-vector of $q$-coordinate degrees after $n$
   complete iterates and $v_n$ is the four-vector of $p$-coordinate degrees,
   then
   $$
   u_n=C_g^n\mathbf1\quad(n\ge0),\qquad
   v_n=A_gC_g^{n-1}\mathbf1\quad(n\ge1).
   $$
4. For every $n\ge1$, the fourth $q$ coordinate is the unique maximum among
   all eight coordinate degrees.  At $n=0$, all eight degrees are tied at
   one.  Hence
   $$
   \deg(F_g^n)=e_4^{\mathsf T}C_g^n\mathbf1\quad(n\ge0),
   \qquad
   \lambda_1(F_g)=\rho(C_g).
   $$
5. The characteristic polynomial is
   $$
   \begin{aligned}
   R_g(t)=\chi_{C_g}(t)
   ={}&t^4-(4g+10)t^3+(-2g^2-26g+45)t^2\\
   &+(12g^3-70g^2+126g-72)t
   +9(g-1)^2(g-2)^2.
   \end{aligned}
   $$
6. For every $g\ge10$ satisfying $g\equiv3\pmod5$, $R_g$ is irreducible
   over $\mathbb Q$, and $\lambda_1(F_g)$ is a quartic Perron number.  These
   give a pairwise distinct infinite subfamily for $g=13,18,23,\ldots$.

The abstract support-profile common-kernel statement proved below is an
explanatory lemma, not a novelty claim or the headline theorem.

## Status

`PROVABLE AS STATED`

The statement survives unchanged under its explicit positive-sign,
characteristic-zero, integer-$g\ge10$ assumptions.  It is not asserted under
any of the excluded variants listed at the end of this package.

## Assumptions

- $K$ is a field of characteristic zero.
- $g$ is an integer with $g\ge10$.
- Both potentials and every displayed coefficient are fixed exactly as above.
- Both shear signs are positive and $F_g=T_g^+\circ S_g^+$.
- Degree means ordinary total polynomial degree in the eight canonical
  coordinates.
- The first dynamical degree is
  $$
  \lambda_1(F_g)=\lim_{n\to\infty}\deg(F_g^n)^{1/n},
  $$
  whose existence here follows from the exact matrix formula.

## Notation

- $\mathbf1=(1,1,1,1)^{\mathsf T}$.
- $e_i$ is the $i$th standard basis vector.
- For a positive weight $u=(u_1,u_2,u_3,u_4)$ and exponent
  $\alpha\in\mathbb N^4$, the weighted score is
  $$
  \operatorname{wt}_u(\alpha)=\alpha^{\mathsf T}u.
  $$
- Put
  $$
  a_g=\frac{g-1}{g-2},\qquad H_g=\frac{g-5}{2}.
  $$
- The explicit sufficient ratio cone is
  $$
  \mathcal K_g=left\{
  u_1(1,x,y,z)^{\mathsf T}:
  u_1>0,
  1\le x\le a_g,
  1\le y\le z\le a_gy,
  y+z<H_g
  \right\}.
  $$
- $u_n$ and $v_n$ denote the actual $q$- and $p$-degree vectors of $F_g^n$.

## Proof Strategy

The proof is a simultaneous support-and-degree induction.

1. Literal differentiation identifies all possible outer support rows.
2. Four strict weighted-score inequalities choose $A_g$ and $B_g$ on
   $\mathcal K_g$.
3. A face-by-face calculation proves $C_g\mathcal K_g\subseteq\mathcal K_g$.
4. Separate temporal carry inequalities show that freshly selected gradient
   rows beat inherited coordinates.
5. Positive integer coefficients and characteristic zero keep every selected
   leading form nonzero.
6. Row comparisons identify $q_4$ as the fixed visible total-degree row.
7. A principal-minor derivation gives the quartic, after which
   Cayley–Hamilton, Perron–Frobenius, and a complete mod-five factor audit give
   the spectral conclusions.

## Dependency Map

1. Polynomial symplecticity uses only the triangular inverses and symmetric
   Hessians.
2. The phase matrices depend on the complete support ledger and four strict
   selectors.
3. Iteration of the selectors depends on seed containment and every cone face.
4. Exact actual degrees depend on selectors, both carries, and leading-form
   survival; none of those three can replace another.
5. The scalar degree identity depends on the vector recurrence and fixed-row
   visibility.
6. The dynamical-degree identity depends on the scalar degree identity and
   primitive-matrix asymptotics.
7. Quartic algebraic degree depends on the exact characteristic polynomial,
   its mod-five irreducibility, and Perron–Frobenius dominance.
8. The support-profile lemma explains the absence or presence of a unit
   sector but does not imply the selector, recurrence, visibility, or quartic
   claims.

## Proof

### Step 1 — Gradients, inverses, and symplecticity

Literal differentiation gives

$$
\nabla V_g=
\begin{pmatrix}
2q_1q_2^2q_3^2q_4^2+gq_1^{g-1}\\
2q_1^2q_2q_3^2q_4^2+(g-1)q_2^{g-2}\\
2q_1^2q_2^2q_3q_4^2\\
2q_1^2q_2^2q_3^2q_4
\end{pmatrix},
$$

and

$$
\nabla W_g=
\begin{pmatrix}
2p_1p_2^2p_3^2p_4^2\\
2p_1^2p_2p_3^2p_4^2\\
2p_1^2p_2^2p_3p_4^2+(g-1)p_3^{g-2}\\
2p_1^2p_2^2p_3^2p_4+gp_4^{g-1}
\end{pmatrix}.
$$

The inverses are the subtraction shears

$$
(S_g^+)^{-1}(q,p)=(q,p-\nabla V_g(q)),
$$

$$
(T_g^+)^{-1}(q,p)=(q-\nabla W_g(p),p).
$$

Thus both maps are polynomial automorphisms.  The inverses are not alternate
theorem families; they only verify invertibility.

Let $H_V=\nabla^2V_g(q)$ and $H_W=\nabla^2W_g(p)$.  Hessian symmetry gives
$H_V^{\mathsf T}=H_V$ and $H_W^{\mathsf T}=H_W$.  The Jacobian blocks are

$$
J_{S_g^+}=
\begin{pmatrix}I_4&0\\H_V&I_4\end{pmatrix},
\qquad
J_{T_g^+}=
\begin{pmatrix}I_4&H_W\\0&I_4\end{pmatrix}.
$$

For

$$
\Omega=\begin{pmatrix}0&I_4\\-I_4&0\end{pmatrix},
$$

block multiplication gives

$$
J_{S_g^+}^{\mathsf T}\Omega J_{S_g^+}
=
\begin{pmatrix}
H_V-H_V^{\mathsf T}&I_4\\-I_4&0
\end{pmatrix}
=\Omega,
$$

and

$$
J_{T_g^+}^{\mathsf T}\Omega J_{T_g^+}
=
\begin{pmatrix}
0&I_4\\-I_4&H_W^{\mathsf T}-H_W
\end{pmatrix}
=\Omega.
$$

Their composition $F_g$ is therefore symplectic.

### Step 2 — Complete support ledger and the phase matrices

The eight gradient rows have the following exponent supports:

| Gradient row | Exponent support |
|---|---|
| $\partial_{q_1}V_g$ | $(1,2,2,2)$ and $(g-1,0,0,0)$ |
| $\partial_{q_2}V_g$ | $(2,1,2,2)$ and $(0,g-2,0,0)$ |
| $\partial_{q_3}V_g$ | $(2,2,1,2)$ |
| $\partial_{q_4}V_g$ | $(2,2,2,1)$ |
| $\partial_{p_1}W_g$ | $(1,2,2,2)$ |
| $\partial_{p_2}W_g$ | $(2,1,2,2)$ |
| $\partial_{p_3}W_g$ | $(2,2,1,2)$ and $(0,0,g-2,0)$ |
| $\partial_{p_4}W_g$ | $(2,2,2,1)$ and $(0,0,0,g-1)$ |

Hence there are exactly four competitive rows: the first two rows of
$\nabla V_g$ and the last two rows of $\nabla W_g$.  The other four rows are
single-support rows.

If the pure exponent wins in each competitive row, the selected first-phase
matrix is

$$
A_g=
\begin{pmatrix}
g-1&0&0&0\\
0&g-2&0&0\\
2&2&1&2\\
2&2&2&1
\end{pmatrix},
$$

and the selected second-phase matrix is

$$
B_g=
\begin{pmatrix}
1&2&2&2\\
2&1&2&2\\
0&0&g-2&0\\
0&0&0&g-1
\end{pmatrix}.
$$

Because $S_g^+$ acts first, a complete step is $B_gA_g$.  Multiplying row by
column gives

$$
C_g=B_gA_g=
\begin{pmatrix}
g+7&2g+4&6&6\\
2g+6&g+6&6&6\\
2g-4&2g-4&g-2&2g-4\\
2g-2&2g-2&2g-2&g-1
\end{pmatrix}.
$$

The seed audit records both phases:

$$
A_g\mathbf1=(g-1,g-2,7,7)^{\mathsf T},
$$

$$
C_g\mathbf1=(3g+23,3g+24,7g-14,7g-7)^{\mathsf T}.
$$

The reversed product does not have this phase interpretation.

### Step 3 — The four selectors and seed threshold

Let

$$
u=u_1(1,x,y,z)^{\mathsf T}\in\mathcal K_g.
$$

The first competitive $V_g$ row compares pure score $(g-1)u_1$ with mixed
score $u_1+2u_2+2u_3+2u_4$.  Dividing pure-minus-mixed by $u_1$ gives

$$
\Delta_{S,1}=(g-2)-2x-2y-2z.
$$

The second competitive row gives

$$
\Delta_{S,2}=(g-3)x-2-2y-2z.
$$

The intermediate vector $v=A_gu$ satisfies

$$
\frac{v}{u_1}=
\begin{pmatrix}
g-1\\
(g-2)x\\
2+2x+y+2z\\
2+2x+2y+z
\end{pmatrix}.
$$

The pure-minus-mixed score in the third $W_g$ row is

$$
(g-2)v_3-(2v_1+2v_2+v_3+2v_4).
$$

After dividing by $u_1$ and collecting terms, this is

$$
\Delta_{T,3}=-8-6x+(g-7)y+(2g-8)z.
$$

The fourth $W_g$ row gives

$$
(g-1)v_4-(2v_1+2v_2+2v_3+v_4),
$$

hence

$$
\Delta_{T,4}=-6-4x+(2g-6)y+(g-6)z.
$$

These formulas show why the second phase must be evaluated at $v=A_gu$.

On $\mathcal K_g$,

$$
\begin{aligned}
\Delta_{S,1}
&>g-2-2a_g-2H_g\\
&=3-2a_g\\
&=\frac{g-4}{g-2}>0.
\end{aligned}
$$

Also, because $x\ge1$ and $y+z<H_g$,

$$
\begin{aligned}
\Delta_{S,2}
&\ge(g-3)-2(1+y+z)\\
&>g-3-2(1+H_g)=0.
\end{aligned}
$$

Since

$$
a_g=1+\frac1{g-2}\le\frac98
$$

for $g\ge10$, and $y,z\ge1$, one has

$$
\begin{aligned}
\Delta_{T,3}
&\ge-8-6a_g+(g-7)+(2g-8)\\
&=3g-23-6a_g\\
&\ge\frac{12g-119}{4}>0,
\end{aligned}
$$

and

$$
\begin{aligned}
\Delta_{T,4}
&\ge-6-4a_g+(2g-6)+(g-6)\\
&=3g-18-4a_g\\
&\ge\frac{6g-45}{2}>0.
\end{aligned}
$$

Thus all four outer support faces are uniquely selected on the entire cone.

At the ordinary seed, $(x,y,z)=(1,1,1)$.  The cone inequalities hold because

$$
1\le a_g,\qquad 2<H_g
$$

for integer $g\ge10$.  The four seed selector margins are

$$
g-8,\qquad g-9,\qquad 3g-29,\qquad 3g-22.
$$

At $g=10$ they are $(2,1,1,8)$.

### Step 4 — Face-by-face invariance of the ratio cone

Let $u'=C_gu$.  Factoring out $u_1$, write

$$
u'=u_1(D,N_2,N_3,N_4)^{\mathsf T},
$$

where

$$
\begin{aligned}
D&=g+7+(2g+4)x+6y+6z,\\
N_2&=2g+6+(g+6)x+6y+6z,\\
N_3&=2g-4+(2g-4)x+(g-2)y+(2g-4)z,\\
N_4&=2g-2+(2g-2)x+(2g-2)y+(g-1)z.
\end{aligned}
$$

All four quantities are positive.  Define

$$
X'=\frac{N_2}{D},\qquad
Y'=\frac{N_3}{D},\qquad
Z'=\frac{N_4}{D}.
$$

It remains to verify every defining face.

#### Face 1: $X'\ge1$

The exact numerator is

$$
N_2-D=(g-1)-(g-2)x.
$$

Since $x\le a_g=(g-1)/(g-2)$, this is nonnegative.  The target lower face is
allowed to be closed.

#### Face 2: $X'<a_g$

Multiplication by the positive number $g-2$ gives

$$
(g-2)(a_gD-N_2)=(g-1)D-(g-2)N_2=E_X,
$$

where

$$
E_X=-g^2+4g+5+(g^2-2g+8)x+6(y+z).
$$

Using $x\ge1$ and $y+z\ge2$,

$$
E_X\ge2g+25>0.
$$

Hence $X'<a_g$.

#### Face 3: $Y'>1$

Subtracting gives

$$
N_3-D=g-11-8x+(g-8)y+(2g-10)z.
$$

The negative $x$ coefficient requires the upper bound $x\le a_g$, whereas
the other two coefficients are positive for $g\ge10$.  Therefore

$$
\begin{aligned}
N_3-D
&\ge g-11-8a_g+(g-8)+(2g-10)\\
&=4g-29-8a_g\\
&\ge4g-38\ge2.
\end{aligned}
$$

Thus $Y'>1$.

#### Face 4: $Z'>Y'$

One has

$$
N_4-N_3=2+2x+gy-(g-3)z.
$$

Since $z\le a_gy$,

$$
\begin{aligned}
N_4-N_3
&\ge2+2x+\bigl(g-(g-3)a_g\bigr)y\\
&=2+2x+\frac{2g-3}{g-2}y>0.
\end{aligned}
$$

Hence $Z'>Y'$.

#### Face 5: $Z'\le a_gY'$

An exact cancellation gives

$$
(g-1)N_3-(g-2)N_4=(g-1)(g-2)(z-y).
$$

After division by $g-2$,

$$
a_gN_3-N_4=(g-1)(z-y)\ge0.
$$

Therefore $Z'\le a_gY'$.  This target face can be closed; it does not cause
a selector tie because the selector gaps were proved strictly positive on
the whole cone.

#### Face 6: $Y'+Z'<H_g$

The height inequality is equivalent to

$$
E_H:=(g-5)D-2(N_3+N_4)>0.
$$

Expanding every coefficient yields

$$
E_H=
g^2-6g-23+(2g^2-14g-8)x-22y-20z.
$$

For $g\ge10$,

$$
2g^2-14g-8=52+(g-10)(2g+6)>0.
$$

Thus $x\ge1$ may be substituted in the positive-coefficient direction.
Furthermore,

$$
-22y-20z=-22(y+z)+2z>-22H_g+2,
$$

because $y+z<H_g$ and $z\ge1$.  Consequently

$$
\begin{aligned}
E_H
&>g^2-6g-23+(2g^2-14g-8)-22H_g+2\\
&=3g^2-31g+26\\
&=16+(g-10)(3g-1)>0.
\end{aligned}
$$

Hence $Y'+Z'<H_g$.

All six target faces have now been verified, so

$$
C_g\mathcal K_g\subseteq\mathcal K_g.
$$

This is a sufficient cone certificate.  No necessity, maximality, or chamber
classification follows from it.

### Step 5 — Temporal carry, exact phase induction, and no cancellation

Let $(Q^{(n)},P^{(n)})=F_g^n(q,p)$, and let $u_n$ and $v_n$ be the vectors
of the four coordinate degrees of $Q^{(n)}$ and $P^{(n)}$, respectively.
At $n=0$,

$$
u_0=v_0=\mathbf1.
$$

The selector result at the seed gives fresh first-phase degree candidates
$A_g\mathbf1$.  Since

$$
A_g\mathbf1=(g-1,g-2,7,7)^{\mathsf T}>\mathbf1,
$$

each fresh gradient row strictly beats the corresponding carried coordinate
of $P^{(0)}$.

Every entry of

$$
C_g-I_4=
\begin{pmatrix}
g+6&2g+4&6&6\\
2g+6&g+5&6&6\\
2g-4&2g-4&g-3&2g-4\\
2g-2&2g-2&2g-2&g-2
\end{pmatrix}
$$

is positive for $g\ge10$.  Therefore

$$
(C_g-I_4)u>0
$$

for every positive $u$.  At the base step, the freshly selected second-phase
rows $C_g\mathbf1$ consequently beat the carried $q$ coordinates
$\mathbf1$.

Suppose inductively that

$$
u_n=C_gu_{n-1},\qquad v_n=A_gu_{n-1},
$$

and that $u_n\in\mathcal K_g$.  The positivity of $C_g-I_4$ gives

$$
u_n-u_{n-1}=(C_g-I_4)u_{n-1}>0.
$$

The matrix $A_g$ is nonnegative and each row has a positive entry, so

$$
A_gu_n-A_gu_{n-1}=A_g(u_n-u_{n-1})>0.
$$

Thus the newly selected $S_g^+$ gradient rows beat the carried vector
$v_n=A_gu_{n-1}$ coordinate by coordinate.  The first phase therefore gives

$$
v_{n+1}=A_gu_n.
$$

The four selector inequalities apply because $u_n\in\mathcal K_g$, and the
second phase sees exactly $v_{n+1}=A_gu_n$.  Its fresh rows have degree
$B_gA_gu_n=C_gu_n$.  They beat the carried $q$ vector because

$$
C_gu_n-u_n=(C_g-I_4)u_n>0.
$$

Hence

$$
u_{n+1}=C_gu_n.
$$

Step 4 returns $u_{n+1}$ to $\mathcal K_g$, closing the simultaneous
induction.

It remains to justify that the selected formal degrees occur in the actual
polynomials.  Every coefficient in the displayed positive-sign gradients is
a positive integer: it is one of $2$, $g-1$, or $g$.  Starting from coordinate
polynomials with coefficients in $\{0,1\}$, forward application of $S_g^+$
and $T_g^+$ uses only addition and multiplication.  Inductively every
coefficient of every forward iterate lies in $\mathbb Z_{\ge0}$.

The strict outer selector picks one support exponent in every competitive
gradient row; the other rows have singleton outer support.  A selected outer
support may expand into several monomials on the same leading face, but each
contribution is a positive integer product.  Contributions to the same
monomial add to a positive integer.  Characteristic zero makes the image of
that positive integer nonzero in $K$.  Therefore the selected leading form
cannot cancel.

This proves the actual phase recurrence

$$
u_n=C_g^n\mathbf1\quad(n\ge0),
$$

and

$$
v_n=A_gC_g^{n-1}\mathbf1\quad(n\ge1).
$$

### Step 6 — Strict fourth-coordinate visibility

For a complete step with input $u\in\mathcal K_g$, the final $p$ degrees are
$A_gu$ and the final $q$ degrees are $C_gu$.  Their coordinatewise
difference is governed by

$$
C_g-A_g=
\begin{pmatrix}
8&2g+4&6&6\\
2g+6&8&6&6\\
2g-6&2g-6&g-3&2g-6\\
2g-4&2g-4&2g-4&g-2
\end{pmatrix},
$$

which is entrywise positive for $g\ge10$.  Thus the $i$th complete $q$ row
strictly beats the $i$th final $p$ row for every $i$.

It remains to show that the fourth complete $q$ row beats the other three.
For $u=u_1(1,x,y,z)^{\mathsf T}$,

$$
\frac{(C_gu)_4-(C_gu)_1}{u_1}
=g-9-6x+(2g-8)y+(g-7)z.
$$

Using $x\le a_g$ and $y,z\ge1$,

$$
g-9-6x+(2g-8)y+(g-7)z
\ge4g-24-6a_g>0.
$$

The second comparison is

$$
\frac{(C_gu)_4-(C_gu)_2}{u_1}
=-8+(g-8)x+(2g-8)y+(g-7)z.
$$

All three variable coefficients are positive for $g\ge10$, so

$$
-8+(g-8)x+(2g-8)y+(g-7)z\ge4g-31>0.
$$

The third comparison is

$$
\frac{(C_gu)_4-(C_gu)_3}{u_1}
=2+2x+gy-(g-3)z.
$$

Step 4 already gave the strict bound

$$
2+2x+gy-(g-3)z
\ge2+2x+\frac{2g-3}{g-2}y>0.
$$

Thus the fourth complete $q$ degree is larger than the other three complete
$q$ degrees.  For each $i$, it is then larger than the $i$th complete $q$
degree, which in turn is larger than the $i$th final $p$ degree; for $i=4$,
the positivity of $C_g-A_g$ supplies the direct comparison.  Hence $q_4$ is
the unique maximum among all eight coordinates after every positive iterate.

At $n=0$, all coordinate degrees equal one.  Therefore strict visibility is
asserted only for $n\ge1$, while the scalar identity holds for all $n\ge0$:

$$
\deg(F_g^n)=e_4^{\mathsf T}C_g^n\mathbf1.
$$

### Step 7 — Hand derivation of the quartic and exact scalar recurrence

For a $4\times4$ matrix, write $e_j(C_g)$ for the sum of its principal
$j\times j$ minors.  Then

$$
\det(tI_4-C_g)=t^4-e_1t^3+e_2t^2-e_3t+e_4.
$$

The trace is

$$
e_1=4g+10.
$$

The six principal $2\times2$ minors are:

| Indices | Minor |
|---|---:|
| $12$ | $-3g^2-7g+18$ |
| $13$ | $g^2-7g+10$ |
| $14$ | $g^2-6g+5$ |
| $23$ | $g^2-8g+12$ |
| $24$ | $g^2-7g+6$ |
| $34$ | $-3g^2+9g-6$ |

Their sum is

$$
e_2=-2g^2-26g+45.
$$

The four principal $3\times3$ minors are:

| Indices | Minor |
|---|---:|
| $123$ | $-3g^3+23g^2-52g+36$ |
| $124$ | $-3g^3+20g^2-35g+18$ |
| $134$ | $-3g^3+12g^2-15g+6$ |
| $234$ | $-3g^3+15g^2-24g+12$ |

Their sum is

$$
e_3=-12g^3+70g^2-126g+72.
$$

For the determinant, $A_g$ is block lower triangular and $B_g$ is block
upper triangular with the $2\times2$ mixed block

$$
\begin{pmatrix}1&2\\2&1\end{pmatrix},
$$

whose determinant is $-3$.  Hence

$$
\det A_g=-3(g-1)(g-2),
$$

$$
\det B_g=-3(g-1)(g-2),
$$

and

$$
e_4=\det C_g=9(g-1)^2(g-2)^2.
$$

Substitution into the principal-minor formula gives

$$
\begin{aligned}
R_g(t)={}&t^4-(4g+10)t^3+(-2g^2-26g+45)t^2\\
&+(12g^3-70g^2+126g-72)t
+9(g-1)^2(g-2)^2.
\end{aligned}
$$

The coefficient of $t$ has the independent factorization

$$
12g^3-70g^2+126g-72=2(g-3)(2g-3)(3g-4).
$$

Evaluating at one yields

$$
R_g(1)=3g(g-1)(3g^2-11g+4)>0
$$

for $g\ge10$.  In particular, $1$ is not an eigenvalue of this $C_g$.

Let

$$
d_n=e_4^{\mathsf T}C_g^n\mathbf1=\deg(F_g^n).
$$

Cayley–Hamilton applied to $C_g$ and then to this visible scalar functional
gives

$$
\begin{aligned}
d_{n+4}={}&(4g+10)d_{n+3}+(2g^2+26g-45)d_{n+2}\\
&-(12g^3-70g^2+126g-72)d_{n+1}\\
&-9(g-1)^2(g-2)^2d_n.
\end{aligned}
$$

Every entry of $C_g$ is positive for $g\ge10$, so $C_g$ is primitive.
Perron–Frobenius gives a positive simple eigenvalue $\rho(C_g)$ strictly
larger in modulus than all other eigenvalues.  Because both the seed
$\mathbf1$ and the visible functional $e_4^{\mathsf T}$ are nonnegative and
nonzero, Perron asymptotics give

$$
\lim_{n\to\infty}d_n^{1/n}=\rho(C_g).
$$

Thus

$$
\lambda_1(F_g)=\rho(C_g).
$$

This is not an entropy conclusion.

### Step 8 — Complete mod-five irreducibility certificate

Assume $g\equiv3\pmod5$.  Reducing every coefficient of $R_g$ gives

$$
\overline R_g(t)=f(t):=t^4-2t^3-t^2+1\in\mathbf F_5[t].
$$

The five values are

$$
\begin{array}{c|ccccc}
t&0&1&2&3&4\\ \hline
f(t)&1&4&2&4&3.
\end{array}
$$

Thus $f$ has no linear factor.

If this quartic were reducible without a linear factor, it would factor as

$$
f(t)=(t^2+at+b)(t^2+ct+d)
$$

with $a,b,c,d\in\mathbf F_5$.  Coefficient comparison gives

$$
a+c=3,\qquad ac+b+d=4,\qquad ad+bc=0,\qquad bd=1.
$$

The last equation leaves exactly

$$
(b,d)\in\{(1,1),(2,3),(3,2),(4,4)\}.
$$

If $(b,d)=(1,1)$ or $(4,4)$, then

$$
ad+bc=b(a+c)=3b\ne0,
$$

contradicting the required zero coefficient of $t$.

If $(b,d)=(2,3)$, then

$$
3a+2c=0,\qquad a+c=3.
$$

These equations give $a=c=4$, but then

$$
ac+b+d=4\cdot4+2+3=1\ne4
$$

in $\mathbf F_5$.

If $(b,d)=(3,2)$, the equations

$$
2a+3c=0,\qquad a+c=3
$$

again give $a=c=4$, and the same $t^2$ contradiction follows.  Hence $f$
has no product of two monic quadratic factors.  It is irreducible over
$\mathbf F_5$.

Because $R_g$ is monic over $\mathbb Z$ and its reduction remains a monic
quartic, Gauss's lemma and reduction modulo five show that $R_g$ is
irreducible over $\mathbb Q$.

For $g=13,18,23,\ldots$, the spectral radius of the positive integer matrix
$C_g$ is therefore an algebraic integer of degree four.  Every other algebraic
conjugate is another root of the irreducible characteristic polynomial and
hence another eigenvalue of $C_g$.  Perron–Frobenius makes every such modulus
strictly smaller than $\rho(C_g)$.  Thus $\lambda_1(F_g)=\rho(C_g)$ is a
quartic Perron number.

These Perron numbers are pairwise distinct.  If parameters $g\ne g'$ gave the
same algebraic number, their monic irreducible minimal polynomials would be
equal.  But the $t^3$ coefficient $-(4g+10)$ determines $g$, a contradiction.

### Step 9 — Support-profile common-kernel obstruction and exact escape

Let

$$
A=-I_r+\sum_{i=1}^p u_iv_i^{\mathsf T},\qquad
B=-I_r+\sum_{j=1}^q s_jt_j^{\mathsf T}
$$

over any field for which the displayed matrices are defined.  Put

$$
E=\bigcap_{i=1}^p\ker(v_i^{\mathsf T})
\cap
\bigcap_{j=1}^q\ker(t_j^{\mathsf T}).
$$

For $x\in E$, every rank-one correction vanishes, so

$$
Ax=-x,\qquad Bx=-x.
$$

It follows that

$$
BAx=B(-x)=-Bx=x,
$$

and therefore

$$
E\subseteq\ker(BA-I_r).
$$

If $\mathcal V$ is the span of the combined covector profile
$\{v_i,t_j\}$, rank-nullity gives

$$
\dim E=r-\dim\mathcal V\ge r-p-q.
$$

Equivalently, one may first note

$$
\ker(A+I_r)\cap\ker(B+I_r)\subseteq\ker(BA-I_r)
$$

and then use

$$
\dim\ker(A+I_r)\cap\ker(B+I_r)\ge r-p-q.
$$

When $r\ge p+q$, the algebraic multiplicity of the eigenvalue one is at
least $r-p-q$, so the non-unit residual characteristic factor has degree at
most $p+q$.  This is a general obstruction, not a sufficient condition for a
particular residual degree.

For the present family,

$$
A_g+I_4
=g e_1e_1^{\mathsf T}+(g-1)e_2e_2^{\mathsf T}
+2(e_3+e_4)\mathbf1^{\mathsf T},
$$

and

$$
B_g+I_4
=2(e_1+e_2)\mathbf1^{\mathsf T}
+(g-1)e_3e_3^{\mathsf T}+g e_4e_4^{\mathsf T}.
$$

The combined covector profile is

$$
\{e_1^{\mathsf T},e_2^{\mathsf T},\mathbf1^{\mathsf T},
e_3^{\mathsf T},e_4^{\mathsf T}\},
$$

which spans the full four-dimensional dual space.  The exact kernels are

$$
\ker(A_g+I_4)=\operatorname{span}(0,0,1,-1)^{\mathsf T},
$$

and

$$
\ker(B_g+I_4)=\operatorname{span}(1,-1,0,0)^{\mathsf T}.
$$

Their intersection is zero.  The independent spectral check

$$
R_g(1)=3g(g-1)(3g^2-11g+4)\ne0
$$

shows that no unrelated unit eigenvector remains for $g\ge10$.

This calculation explains how the displayed four-spike support profile avoids
the common unit sector behind the endpoint-spike cubic collapse.  It does not
state that every full-rank profile has quartic growth; the quartic conclusion
here still depends on Steps 2--8.

### Step 10 — Boundary audit and theorem closure

At the ordinary seed the four margins are

$$
g-8,\qquad g-9,\qquad 3g-29,\qquad 3g-22.
$$

At $g=9$ they become

$$
(1,0,-2,5).
$$

Thus the second first-phase row ties at iteration zero, and the third
second-phase pure branch loses.  The cone height also reaches its boundary:

$$
y+z=2=\frac{g-5}{2}.
$$

Therefore $g\ge10$ is the sharp integer threshold for the ordinary seed and
these four selected faces.  Nothing in this proof excludes a different
branch regime or different theorem for a smaller parameter.

Combining Steps 1--10 proves every item in the Claim. ∎

## Corrections or Missing Assumptions

- The immutable R1 sign correction is essential: the theorem uses positive
  signs in both phases.  No sign-invariance assertion remains.
- Characteristic zero is essential to the positive-integer coefficient
  survival proof.
- The source design uses the explicit sufficient ratio cone written here.
  It does not claim equivalence with every alternative sufficient cone,
  maximality, necessity, or chamber classification.
- Strict $q_4$ visibility begins at $n=1$; the scalar formula at $n=0$ is a
  tied identity case.
- Quartic irreducibility is proved only when $g\equiv3\pmod5$.
- The common-kernel lemma is explanatory and nonnovel.

No further assumption is silently used.

## Open Risks

No theorem-critical algebraic gap is known in this author package.  A fresh
independent reviewer should nevertheless recompute:

1. all four second-phase score coefficients at $v=A_gu$;
2. every target-cone numerator, especially the height expression $E_H$;
3. all ten nontrivial principal minors;
4. the signs in the order-four recurrence;
5. all four quadratic constant-term cases over $\mathbf F_5$;
6. the distinction between outer-face uniqueness and a potentially
   multi-monomial positive leading form;
7. every identity/permission boundary in the other nine source-design files.

These are independent-review targets, not invitations to use computational
output as proof.
