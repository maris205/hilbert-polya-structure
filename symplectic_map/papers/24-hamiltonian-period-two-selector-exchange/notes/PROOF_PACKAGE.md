# Proof Package

## Claim

Let $K$ be a field of characteristic zero, let $m\ge2$ and $s\ge1$ be
integers, and let $A,B,C,D\in K^\times$. Define

$$
V_m(q)=Aq_1^m q_2^2+Bq_1q_2^{2m},
\qquad
W_{m,s}(p)=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1},
$$

$$
S(q,p)=(q,p+\nabla V_m(q)),
\qquad
T(q,p)=(q+\nabla W_{m,s}(p),p),
\qquad
F_{m,s}=T\circ S.
$$

Then:

1. $F_{m,s}$ is a polynomial symplectomorphism of $K^4$.
2. The actual $q$-degree orbit of the ordinary seed $u_0=(1,1)^{\mathsf T}$
   switches strictly between the two chambers $r=u_1/u_2<2$ and $r>2$.
3. The selected first-phase matrices are
   $$
   A_-=
   \begin{pmatrix}
   0&2m\\
   1&2m-1
   \end{pmatrix},
   \qquad
   A_+=
   \begin{pmatrix}
   m-1&2\\
   m&1
   \end{pmatrix},
   $$
   and the second phase uses
   $$
   B_m=\operatorname{diag}(2m+1,m).
   $$
4. Writing
   $$
   C_-=sB_mA_-,
   \qquad
   C_+=sB_mA_+,
   \qquad
   P=(B_mA_+)(B_mA_-),
   $$
   the exact parity formulas are
   $$
   u_{2j}=(s^2P)^j(1,1)^{\mathsf T},
   \qquad
   u_{2j+1}=sB_mA_-(s^2P)^j(1,1)^{\mathsf T}.
   $$
5. For every $n\ge1$, the first position coordinate is strictly maximal among
   all four coordinate degrees. Hence
   $$
   d_n:=\deg(F_{m,s}^n)=u_{n,1}
   \qquad(n\ge1),
   $$
   with $d_0=1$.
6. The two eigenvalues of $P$ are
   $$
   H=m^2(2m+1)^2,
   \qquad
   L=2m(m+1),
   $$
   so
   $$
   \lambda_1(F_{m,s})=sm(2m+1).
   $$
7. The visible degree sequence satisfies
   $$
   d_{n+4}=s^2(H+L)d_{n+2}-s^4HL\,d_n,
   $$
   with initial values
   $$
   d_0=1,
   \qquad
   d_1=2m(2m+1)s,
   $$
   $$
   d_2=2m(m+1)(2m-1)(2m+1)s^2,
   \qquad
   d_3=8m^4(m+1)(2m+1)s^3.
   $$
8. The exact wall gaps are
   $$
   u_{2j,1}-2u_{2j,2}=-(s^2L)^j,
   \qquad
   u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j.
   $$
9. Inside the crossed-binomial / diagonal-pure-power ansatz, strict chamber
   exchange forces the wall-fixing ratio
   $$
   \frac ef=\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R}.
   $$
10. The abstract period-$k$ selector-to-monodromy statement is valid only as
    a conditional technique lemma with explicit selector, carry,
    noncancellation, linearity, and visibility hypotheses.

## Status

`PROVABLE AS STATED`

## Assumptions

- $K$ is a field of characteristic zero.
- $m$ and $s$ are integers with $m\ge2$ and $s\ge1$.
- $A,B,C,D$ are all nonzero.
- Degree means ordinary total degree in $K[q_1,q_2,p_1,p_2]$.
- The standard seed is $u_0=(1,1)^{\mathsf T}$.

## Notation

- For a positive degree vector $u=(u_1,u_2)^{\mathsf T}$, write
  $$
  r=\frac{u_1}{u_2}.
  $$
- Let
  $$
  \Delta=H-L=m(4m^3+4m^2-m-2).
  $$
- Let
  $$
  \delta_n=u_{n,1}-2u_{n,2}.
  $$
- Let $v_{n+1}$ denote the selected first-phase degree vector produced from
  $u_n$ before the pure second phase.

## Proof strategy

1. Differentiate literally and check symplecticity by the Hessian-block
   calculation.
2. Read the competitive rows, derive the common wall, and compute the two
   branch maps.
3. Prove strict chamber exchange for the abstract $q$-degree transport.
4. Prove actual polynomial carry in both phases, first at the seed and then
   inductively.
5. Prove arbitrary-nonzero-coefficient leading-form survival in a domain.
6. Prove $q_1$ visibility against $q_2,p_1,p_2$.
7. Multiply the two-step monodromy, close its spectrum, and derive the
   recurrence and wall-gap formulas.
8. Write parity closed forms and explain integrality from the matrix law.
9. Separate the bounded structural lemma from the carry/visibility proof.

## Proof

### Step 1 — Literal gradients, inverses, and symplecticity

Literal differentiation gives

$$
\partial_{q_1}V_m=mAq_1^{m-1}q_2^2+Bq_2^{2m},
$$

$$
\partial_{q_2}V_m=2Aq_1^mq_2+2mBq_1q_2^{2m-1},
$$

$$
\partial_{p_1}W_{m,s}=(s(2m+1)+1)Cp_1^{s(2m+1)},
$$

$$
\partial_{p_2}W_{m,s}=(sm+1)Dp_2^{sm}.
$$

The subtraction inverses are

$$
S^{-1}(q,p)=(q,p-\nabla V_m(q)),
\qquad
T^{-1}(q,p)=(q-\nabla W_{m,s}(p),p).
$$

Let

$$
H_V=\nabla^2V_m(q),
\qquad
H_W=\nabla^2W_{m,s}(p).
$$

Then

$$
J_S=
\begin{pmatrix}
I_2&0\\
H_V&I_2
\end{pmatrix},
\qquad
J_T=
\begin{pmatrix}
I_2&H_W\\
0&I_2
\end{pmatrix}.
$$

Both Hessians are symmetric. With

$$
\Omega=
\begin{pmatrix}
0&I_2\\
-I_2&0
\end{pmatrix},
$$

one computes

$$
J_S^{\mathsf T}\Omega J_S=\Omega,
\qquad
J_T^{\mathsf T}\Omega J_T=\Omega.
$$

Hence $S$, $T$, and $F_{m,s}=T\circ S$ are polynomial symplectomorphisms.

### Step 2 — Support rows, common wall, and branch matrices

There are two competitive first-phase rows and no competitive second-phase
rows.

For $\partial_{q_1}V_m$, the mixed exponent $(m-1,2)$ has weight

$$
(m-1)u_1+2u_2,
$$

and the pure exponent $(0,2m)$ has weight

$$
2mu_2.
$$

Their difference is

$$
(m-1)u_1+2u_2-2mu_2=(m-1)(u_1-2u_2).
$$

For $\partial_{q_2}V_m$, the mixed exponent $(m,1)$ has weight

$$
mu_1+u_2,
$$

and the pure exponent $(1,2m-1)$ has weight

$$
u_1+(2m-1)u_2.
$$

Their difference is

$$
mu_1+u_2-\bigl(u_1+(2m-1)u_2\bigr)=(m-1)(u_1-2u_2).
$$

Thus both competitive rows switch synchronously at the common wall $r=2$.
The selected matrices are

$$
A_-=
\begin{pmatrix}
0&2m\\
1&2m-1
\end{pmatrix}
\qquad(r<2),
$$

$$
A_+=
\begin{pmatrix}
m-1&2\\
m&1
\end{pmatrix}
\qquad(r>2).
$$

The second phase is pure-power, so

$$
B_m=\operatorname{diag}(2m+1,m),
$$

and therefore

$$
C_-=sB_mA_-=
s\begin{pmatrix}
0&2m(2m+1)\\
m&m(2m-1)
\end{pmatrix},
$$

$$
C_+=sB_mA_+=
s\begin{pmatrix}
(m-1)(2m+1)&2(2m+1)\\
m^2&m
\end{pmatrix}.
$$

### Step 3 — Correct branch algebra and strict chamber exchange

If $r<2$, then the complete-step ratio is

$$
h_m(r)=
\frac{s(2m+1)\cdot 2mu_2}{sm(u_1+(2m-1)u_2)}
=\frac{2(2m+1)}{r+2m-1}.
$$

Hence

$$
h_m(r)-2=\frac{2(2-r)}{r+2m-1}>0
\qquad(0<r<2),
$$

so $h_m(r)>2$.

If $r>2$, then the complete-step ratio is

$$
\ell_m(r)=
\frac{s(2m+1)\bigl((m-1)u_1+2u_2\bigr)}{sm(mu_1+u_2)}
=\frac{(2m+1)\bigl((m-1)r+2\bigr)}{m(mr+1)}.
$$

The corrected exact identities are

$$
\ell_m(r)-1=
\frac{(m^2-m-1)r+3m+2}{m(mr+1)},
$$

and

$$
2-\ell_m(r)=
\frac{(m+1)(r-2)}{m(mr+1)}.
$$

For $m\ge2$ and $r>2$, both numerators are positive. Hence

$$
1<\ell_m(r)<2.
$$

Therefore every positive degree ray off the wall alternates strictly between
the two chambers. In particular, the ordinary seed

$$
u_0=(1,1)^{\mathsf T}
$$

has $r_0=1<2$, so its itinerary is

$$
-,+,-,+,\ldots.
$$

The wall itself is a real tie boundary:

$$
h_m(r)=2\iff r=2,
\qquad
\ell_m(r)=2\iff r=2.
$$

It is excluded from the theorem.

### Step 4 — Actual temporal carry

The abstract selector story is not yet enough. One must prove that the newly
selected rows beat the carried coordinates in both phases.

At the seed,

$$
A_-(1,1)^{\mathsf T}=(2m,2m)^{\mathsf T}>(1,1)^{\mathsf T},
$$

so the fresh momentum degrees beat the carried degree-one momentum seed. The
second phase then produces

$$
sB_mA_-(1,1)^{\mathsf T}=
\bigl(2m(2m+1)s,\ 2m^2s\bigr)^{\mathsf T}>(1,1)^{\mathsf T},
$$

so the fresh position degrees beat the carried degree-one position seed.

Now assume $n\ge1$ and the actual $q$-degree vector after $n$ full steps is
$u_n=(u_{n,1},u_{n,2})^{\mathsf T}$. Because the second phase is pure-power,
the carried momentum degrees are exactly

$$
\deg p_n=
\left(
\frac{u_{n,1}}{s(2m+1)},
\frac{u_{n,2}}{sm}
\right).
$$

If $r_n<2$, then the next selected first-phase degrees are

$$
v_{n+1}=
\begin{pmatrix}
2mu_{n,2}\\
u_{n,1}+(2m-1)u_{n,2}
\end{pmatrix}.
$$

They beat the carried momentum degrees because

$$
2mu_{n,2}>\frac{u_{n,1}}{s(2m+1)}
$$

follows from $u_{n,1}<2u_{n,2}$, and

$$
u_{n,1}+(2m-1)u_{n,2}>\frac{u_{n,2}}{sm}
$$

is immediate for $m\ge2$ and $s\ge1$.

The pure second phase then gives

$$
u_{n+1}=
\begin{pmatrix}
s(2m+1)\cdot 2mu_{n,2}\\
sm\bigl(u_{n,1}+(2m-1)u_{n,2}\bigr)
\end{pmatrix},
$$

and these fresh position degrees beat the carried position degrees because

$$
2m(2m+1)su_{n,2}>u_{n,1},
$$

and

$$
sm\bigl(u_{n,1}+(2m-1)u_{n,2}\bigr)>u_{n,2}.
$$

If $r_n>2$, then the next selected first-phase degrees are

$$
v_{n+1}=
\begin{pmatrix}
(m-1)u_{n,1}+2u_{n,2}\\
mu_{n,1}+u_{n,2}
\end{pmatrix}.
$$

They beat the carried momentum degrees because

$$
(m-1)u_{n,1}+2u_{n,2}>\frac{u_{n,1}}{s(2m+1)},
$$

and

$$
mu_{n,1}+u_{n,2}>\frac{u_{n,2}}{sm}.
$$

The pure second phase then yields

$$
u_{n+1}=
\begin{pmatrix}
s(2m+1)\bigl((m-1)u_{n,1}+2u_{n,2}\bigr)\\
sm\bigl(mu_{n,1}+u_{n,2}\bigr)
\end{pmatrix},
$$

and both coordinates beat the carried position degrees:

$$
s(2m+1)\bigl((m-1)u_{n,1}+2u_{n,2}\bigr)>u_{n,1},
$$

$$
sm\bigl(mu_{n,1}+u_{n,2}\bigr)>u_{n,2}.
$$

Thus actual temporal carry closes in both phases and in both chambers, already
at $s=1$.

### Step 5 — Arbitrary nonzero coefficients via top homogeneous parts

The theorem is not positivity-only in $A,B,C,D$. The argument is a domain
argument for top homogeneous parts.

Inductively assume that each coordinate polynomial currently has a nonzero top
homogeneous part.

- In the first phase, one competitive derivative term has strictly larger
  degree than the losing derivative term and than the carried momentum
  coordinate. Its top homogeneous part is a nonzero scalar multiple of a
  product of already nonzero top homogeneous parts of $q_1$ and $q_2$.
- In the second phase, each updated position coordinate is the old coordinate
  plus a pure power of one momentum coordinate. The power of a nonzero top
  homogeneous part is again nonzero.

Because $K[q_1,q_2,p_1,p_2]$ is a domain and $A,B,C,D$ are nonzero, the
selected top homogeneous parts cannot cancel. Characteristic zero is used only
to keep derivative scalars such as $m$, $2m$, $s(2m+1)+1$, and $sm+1$
nonzero.

Hence the actual degree transport theorem is valid for arbitrary nonzero
coefficients in characteristic zero.

### Step 6 — Visibility of $q_1$

The branch maps already show that every complete-step ratio is greater than
one:

$$
h_m(r)>2,
\qquad
1<\ell_m(r)<2.
$$

Therefore

$$
u_{n,1}>u_{n,2}
\qquad(n\ge1).
$$

It remains to compare $q_1$ against both momentum coordinates.

If $r_n<2$, then

$$
u_{n+1,1}=s(2m+1)\cdot 2mu_{n,2},
$$

and

$$
v_{n+1,2}=u_{n,1}+(2m-1)u_{n,2}.
$$

Using the definition of $h_m(r_n)$,

$$
u_{n+1,1}=sm\,h_m(r_n)\,v_{n+1,2}.
$$

This is the corrected exact identity from the candidate-review correction.
Since $h_m(r_n)>2$, $m\ge2$, and $s\ge1$, it follows that

$$
u_{n+1,1}>v_{n+1,2}.
$$

Also $u_{n+1,1}>v_{n+1,1}$ is immediate because
$u_{n+1,1}=s(2m+1)v_{n+1,1}$.

If $r_n>2$, then

$$
v_{n+1,1}=(m-1)u_{n,1}+2u_{n,2},
\qquad
v_{n+1,2}=mu_{n,1}+u_{n,2},
$$

and

$$
u_{n+1,1}=s(2m+1)v_{n+1,1}>v_{n+1,1}.
$$

Moreover,

$$
u_{n+1,1}-v_{n+1,2}
=s(2m+1)\bigl((m-1)u_{n,1}+2u_{n,2}\bigr)-(mu_{n,1}+u_{n,2})>0.
$$

Thus for every $n\ge1$, $q_1$ is strictly maximal among
$q_1,q_2,p_1,p_2$. Hence

$$
d_n=\deg(F_{m,s}^n)=u_{n,1}
\qquad(n\ge1),
$$

while $d_0=1$ is the tied seed value.

### Step 7 — Two-step monodromy and its spectrum

The exact two-step monodromy is

$$
P=(B_mA_+)(B_mA_-).
$$

Direct multiplication gives

$$
P=
\begin{pmatrix}
2m(2m+1)&2m(2m+1)(2m^2+m-2)\\
m^2&m^2(4m^2+4m-1)
\end{pmatrix}.
$$

The vector $(2,1)^{\mathsf T}$ is a right eigenvector:

$$
P
\begin{pmatrix}
2\\
1
\end{pmatrix}
=
m^2(2m+1)^2
\begin{pmatrix}
2\\
1
\end{pmatrix}.
$$

Hence one eigenvalue is

$$
H=m^2(2m+1)^2.
$$

The trace is

$$
\operatorname{tr}(P)=2m(2m+1)+m^2(4m^2+4m-1)
=4m^4+4m^3+3m^2+2m,
$$

and the determinant is

$$
\det(P)=H\,L
=2m^3(m+1)(2m+1)^2.
$$

Therefore the second eigenvalue is

$$
L=\frac{\det(P)}{H}=2m(m+1).
$$

Since $H>L>0$, the monodromy eigenvalues for the actual two-step map
$C_+C_-=s^2P$ are $s^2H$ and $s^2L$. Consequently

$$
\lambda_1(F_{m,s})=\sqrt{\rho(s^2P)}=sm(2m+1).
$$

### Step 8 — Exact recurrence and wall-gap laws

From the strict itinerary,

$$
u_{2j}=(s^2P)^j(1,1)^{\mathsf T},
\qquad
u_{2j+1}=sB_mA_-(s^2P)^j(1,1)^{\mathsf T}.
$$

Applying Cayley–Hamilton to $s^2P$ gives, for every visible scalar coordinate
and in particular for $d_n$,

$$
d_{n+4}=s^2(H+L)d_{n+2}-s^4HL\,d_n.
$$

The initial values are obtained directly:

$$
u_1=sB_mA_-(1,1)^{\mathsf T}
=
\begin{pmatrix}
2m(2m+1)s\\
2m^2s
\end{pmatrix},
$$

$$
u_2=s^2P(1,1)^{\mathsf T}
=
\begin{pmatrix}
2m(m+1)(2m-1)(2m+1)s^2\\
4m^3(m+1)s^2
\end{pmatrix},
$$

so

$$
d_0=1,
\quad
d_1=2m(2m+1)s,
\quad
d_2=2m(m+1)(2m-1)(2m+1)s^2.
$$

Also

$$
u_3=sB_mA_-u_2
=
\begin{pmatrix}
8m^4(m+1)(2m+1)s^3\\
2m^2(m+1)(2m-1)(2m^2+2m+1)s^3
\end{pmatrix},
$$

so

$$
d_3=8m^4(m+1)(2m+1)s^3.
$$

This is the corrected third vector demanded by the review corrections.

For the wall gaps, set $\ell=(1,-2)$. Direct multiplication gives

$$
\ell C_-=-2ms\,\ell,
\qquad
\ell C_+=-(m+1)s\,\ell.
$$

Since $\ell u_0=-1$,

$$
\delta_{2j}
=\ell u_{2j}
=-(s^2L)^j,
$$

and

$$
\delta_{2j+1}
=\ell u_{2j+1}
=2ms(s^2L)^j.
$$

Hence the orbit approaches the wall from alternating sides but never lands on
it.

### Step 9 — Parity closed forms and integrality

Let

$$
\Delta=H-L=m(4m^3+4m^2-m-2).
$$

The even subsequence has the spectral closed form

$$
d_{2j}
=
s^{2j}\left(
\frac{d_2/s^2-L}{\Delta}H^j
+
\frac{H-d_2/s^2}{\Delta}L^j
\right).
$$

After substitution,

$$
d_{2j}
=
\frac{s^{2j}}{4m^3+4m^2-m-2}
\left(
4(m+1)(2m^2-1)H^j
-
(2m+1)(2m^2+m-2)L^j
\right).
$$

The full even vector may be written as

$$
u_{2j}
=
\frac{s^{2j}}{4m^3+4m^2-m-2}
\left(
2(m+1)(2m^2-1)H^j
\begin{pmatrix}
2\\
1
\end{pmatrix}
+
L^j
\begin{pmatrix}
-(2m+1)(2m^2+m-2)\\
m
\end{pmatrix}
\right).
$$

Because

$$
u_{2j+1}=sB_mA_-u_{2j},
$$

the odd visible subsequence is

$$
d_{2j+1}
=
2m(2m+1)s\,u_{2j,2}
=
\frac{2m(2m+1)s^{2j+1}}{4m^3+4m^2-m-2}
\left(
2(m+1)(2m^2-1)H^j+mL^j
\right).
$$

Equivalently,

$$
d_{2j+1}
=
s^{2j+1}\left(
\frac{d_3/s^3-L\,d_1/s}{\Delta}H^j
+
\frac{H\,d_1/s-d_3/s^3}{\Delta}L^j
\right).
$$

Integrality does not depend on these rational-looking coefficient formulas.
It follows directly from the exact matrix recurrences

$$
u_{2j}=(s^2P)^j(1,1)^{\mathsf T},
\qquad
u_{2j+1}=sB_mA_-(s^2P)^j(1,1)^{\mathsf T},
$$

because $P$, $B_mA_-$, and the seed all have integer entries for integer
$m,s$. Equivalently, the stride-two recurrence has integer coefficients and
integer initial values. No denominator-divisibility handwaving is needed.

### Step 10 — The bounded crossed-binomial lemma

Take

$$
V=Aq_1^a q_2^b+Bq_1^c q_2^d,
\qquad
a>c\ge1,
\qquad
d>b\ge1,
$$

and

$$
W=Cp_1^{e+1}+Dp_2^{f+1}.
$$

Set

$$
R=\frac{d-b}{a-c},
\qquad
L_{\mathrm{wall}}=aR+b=cR+d.
$$

The two competitive first-phase differences are

$$
\bigl((a-1)r+b\bigr)-\bigl((c-1)r+d\bigr)
=(a-c)(r-R),
$$

and

$$
\bigl(ar+b-1\bigr)-\bigl(cr+d-1\bigr)
=(a-c)(r-R).
$$

Hence both rows switch synchronously at the common wall $r=R$.

If the selected exponent is $(x,y)$, then the induced projective branch is

$$
g_{x,y}(r)=
\frac ef\,
\frac{(x-1)r+y}{xr+y-1}.
$$

Its derivative is

$$
g_{x,y}'(r)=
-\frac ef\,
\frac{x+y-1}{(xr+y-1)^2}<0.
$$

At the wall, both branches take the common value

$$
g(R)=
\frac ef\,
\frac{L_{\mathrm{wall}}-R}{L_{\mathrm{wall}}-1}.
$$

Therefore the two branches globally exchange the two open chambers if and only
if $g(R)=R$, namely

$$
\frac ef=
\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R}.
$$

This proves only the wall-fixing exponent ratio inside this ansatz. It does
not prove temporal carry, actual polynomial degree transport, or visibility.

For the explicit Paper-24 family,

$$
(a,b,c,d)=(m,2,1,2m),
$$

so

$$
R=2,
\qquad
L_{\mathrm{wall}}=2m+2,
\qquad
\frac ef=\frac{2m+1}{m}.
$$

The integral realizations are therefore exactly the pairs

$$
(e,f)=s(2m+1,m).
$$

If $R=1$, then the ordinary seed $(1,1)$ lies on the wall and no strict
seed-based theorem follows automatically.

### Step 11 — Conditional period-$k$ selector-to-monodromy lemma

The abstract period-$k$ statement is valid only under the following explicit
hypotheses:

1. every phase has a unique selected face with a strict gap over all
   unselected faces on the claimed domain;
2. every selected fresh row strictly beats the carried coordinates in its
   target block;
3. all selected top homogeneous parts remain nonzero in a domain;
4. the selected faces induce linear degree maps $C_0,\dots,C_{k-1}$;
5. a coordinate or linear functional sees the true total degree on the
   residue classes under study;
6. the Perron class of the monodromy is visible to that coordinate or
   functional.

Then, for $M=C_{k-1}\cdots C_0$, one has

$$
u_{k\ell+j}=D_jM^\ell u_0
$$

for suitable residue matrices $D_j$, every visible residue subsequence
satisfies the Cayley--Hamilton recurrence of $M$, and

$$
\lambda_1=\rho(M)^{1/k}
$$

once the visible Perron-class hypothesis is verified.

This is a technical lemma only. It is not the public novelty claim of Paper
24.

### Step 12 — Boundary audit and content-page architecture

The theorem fails or narrows under the following changes:

- on the wall $r=2$, both competitive $V$-rows tie exactly;
- if any of $A,B,C,D$ vanishes, the support profile changes;
- in positive characteristic, derivative scalars can vanish;
- at $m=1$, the switching factor $(m-1)(u_1-2u_2)$ collapses;
- in the structural lemma, $R=1$ places the ordinary seed on the wall.

As a sanity check only, the first values at $m=2$ are

$$
d_0=1,\qquad d_1=20s,\qquad d_2=180s^2,\qquad d_3=1920s^3.
$$

This illustration is not theorem evidence.

A proof-first article of 22--30 content pages is credible:

| Component | Pages |
|---|---:|
| introduction and bounded related work | 3 |
| family, symplecticity, and support rows | 4 |
| wall algebra and strict exchange | 4 |
| carry, no-cancellation, and visibility | 6 |
| monodromy, recurrence, wall gaps, and parity formulas | 6 |
| structural lemma, conditional period-$k$ lemma, and limits | 3 |
| total target | 26 |

## Locked nonclaims

This paper does not claim:

1. any theorem on the wall $r=2$;
2. any classification beyond the crossed-binomial / two-pure-power ansatz;
3. any maximal or necessary selector fan;
4. arbitrary period words, period $>2$, or automaton realization;
5. positive-characteristic validity;
6. inverse-degree, entropy-equality, integrability, genericity,
   periodic-point, or nonconjugacy theorems;
7. novelty of the abstract period-$k$ monodromy lemma;
8. first Perron realization, first tropical switching, or absolute priority.

## Final status

`PROVABLE AS STATED`
