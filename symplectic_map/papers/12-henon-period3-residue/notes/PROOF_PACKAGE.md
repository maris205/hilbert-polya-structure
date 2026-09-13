# Proof Package

## Claim

Let \(k\) be an algebraically closed field of characteristic zero.  For an
integer \(m\ge 2\) and \(a\in k\), put

\[
p_{m,a}(x)=(x^m-a)^2,
\qquad
q_{m,a}(x)=p'_{m,a}(x)=2m x^{m-1}(x^m-a),
\]

and

\[
f_{m,a}(x,y)=\bigl(y+p_{m,a}(x),x\bigr).
\]

The following statements are the source-locked theorem package.

1. The formal period-one trace multiset is

   \[
   0^{\times 2m}.
   \]

   The formal exact-period-two trace multiset is

   \[
   2^{\times((2m)^2-2m)}.
   \]

2. In the monic-centered Friedland--Milnor normalization,

   \[
   f_{m,a}\sim f_{m,b}
   \quad\Longleftrightarrow\quad
   a^{2m-1}=b^{2m-1}.
   \]

3. With indices in \(\mathbb Z/3\mathbb Z\), define

   \[
   F_i=(x_i^m-a)^2+\varepsilon(x_{i-1}-x_{i+1}),
   \qquad
   q_i=2m x_i^{m-1}(x_i^m-a).
   \]

   Then

   \[
   t_\varepsilon
   :=\det\left(\frac{\partial F_i}{\partial x_j}\right)
   =q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2).
   \]

   At \(\varepsilon=1\), the equations \(F_i=0\) encode
   \(\operatorname{Fix}(f_{m,a}^3)\), and \(t_1\) is
   \(\operatorname{tr}Df_{m,a}^3\).

4. The cyclic quotient

   \[
   \mathcal A_m=
   k[a,\varepsilon,x_0,x_1,x_2]/(F_0,F_1,F_2)
   \]

   is free of rank \((2m)^3\) over \(k[a,\varepsilon]\).  If

   \[
   S_m(a,\varepsilon)
   =\operatorname{Tr}_{\mathcal A_m/k[a,\varepsilon]}
      (M_{t_\varepsilon^m}),
   \]

   then the complete-intersection trace--residue identity gives

   \[
   S_m(a,\varepsilon)=\operatorname{Res}(t_\varepsilon^{m+1}).
   \]

5. There are integers \(C_m,D_m\) such that

   \[
   \boxed{
   S_m(a,\varepsilon)
   =C_m\varepsilon^{3m}
    +D_m a^{2m-1}\varepsilon^{2m}.}
   \]

   Consequently,

   \[
   S_m(a,1)=C_m+D_m a^{2m-1}.
   \]

   Moreover, \(C_m=0\) whenever \(m\) is odd.

6. The slope has the following exact finite coefficient certificate.  Define

   \[
   H(r,k)=
   \sum_{\substack{u+v=k\\2u\le r,\;2v\le r}}
   \binom{k}{u}\binom{r}{2u}\binom{r}{2v}
   \]

   and

   \[
   A_{m,r}=
   \sum_{k=\lceil m/2\rceil}^{\min(m-1,r)}
   (-1)^{r+k}
   \binom{m-1}{2(m-k)-1}H(r,k).
   \]

   Then

   \[
   \boxed{
   D_m=3\sum_{j=0}^{\lfloor m/2\rfloor}
   \binom{m+1}{j}(2m)^{3m+3-2j}A_{m,m-j}.}
   \]

   Equivalently, if \(q=\lfloor m/2\rfloor\),

   \[
   E_m=\sum_{j=0}^{q}\binom{m+1}{j}
   (2m)^{2(q-j)}A_{m,m-j},
   \qquad
   D_m=3(2m)^{3m+3-2q}E_m.
   \]

7. For \(m=2\), every monic-centered quartic \(p\) whose formal fixed
   trace multiset is \(0^4\) has the form

   \[
   p(x)=(x^2-L)^2
   \]

   for a unique parameter \(L\in k\).  On this complete normalized fiber,

   \[
   \boxed{
   S_2^{(3)}(L)
   =-1296000-1572864L^3
   =-384(3375+4096L^3).}
   \]

   The formal fixed contribution to this second trace moment is zero.
   Periods one and two are constant on the fiber, while the displayed
   period-three moment is an affine coordinate in the normalized moduli
   coordinate \(L^3\).  Thus period three is the minimal separating period
   on this fiber.  The pointwise exact-period-three zero-cycle has formal
   length \(60\), and the corresponding cyclewise sum is

   \[
   -432000-524288L^3.
   \]

The statement \(D_m\ne0\) for every \(m\ge2\) is **not** part of the
theorem.  It is an open combinatorial conjecture in this project.

## Status

**PROVABLE AS STATED**, with “formal trace multiset” interpreted through the
characteristic polynomial of multiplication by the trace function on the
finite periodic-point algebra.  Step 9 proves the frozen coefficient formula
by an exact Laurent-series fiber sum.  Step 12 also proves the quartic slope
independently of that all-degree collapse, so the sharp quartic conclusion
does not rest on a single coefficient derivation.

Two stronger readings are not justified:

- the trace function is not literally zero in every nonreduced fixed algebra;
  it is nilpotent and therefore has only the formal eigenvalue zero;
- the all-degree separation claim would require \(D_m\ne0\) for every
  \(m\), which remains unproved.

## Assumptions

- The base field is algebraically closed of characteristic zero.  In
  particular, \(m\), \(2m\), and \(2m-1\) are nonzero, every nonzero
  parameter has \(m\) distinct \(m\)-th roots, and Newton--Puiseux
  valuation arguments are available.
- “Normalized polynomial conjugacy” means conjugacy in the monic-centered
  Friedland--Milnor Hénon normal-form category.  The normal-form uniqueness
  theorem is used in exactly one place: a conjugacy between two one-factor
  monic-centered Hénon forms is induced by a simultaneous affine change in
  the two coordinates, and centering removes its translation part.
- The standard trace--residue theorem for a finite zero-dimensional complete
  intersection is used: if \(A=K[x_1,\ldots,x_n]/(G_1,\ldots,G_n)\) and
  \(J=\det(\partial G_i/\partial x_j)\), then

  \[
  \operatorname{Tr}_{A/K}(M_h)=\operatorname{Res}_G(hJ).
  \]

  This identity remains valid for nonreduced complete intersections.
- Period-one and period-two statements are scheme-theoretic.  “Exact period
  two” means the formal period-two spectral zero-cycle minus the formal
  fixed spectral zero-cycle.  The analogous period-three subtraction is used
  below.

## Notation

- For a finite-dimensional \(k\)-algebra \(B\) and \(h\in B\), let
  \(M_h:B\to B\) be multiplication by \(h\).  The **formal multiset of
  values of \(h\)** is the multiset of roots of
  \(\det(TI-M_h)\), counted with algebra dimension.  Nilpotent thickening
  changes multiplicity but not the eigenvalue attached to a support point.
- Write

  \[
  \nu=2m-1,
  \qquad
  X_{\mathrm{top}}=x_0^\nu x_1^\nu x_2^\nu.
  \]

- Let \(\operatorname{NF}\) denote the unique normal form for the Gröbner
  basis \(F_0,F_1,F_2\), with standard monomials
  \(x_0^{e_0}x_1^{e_1}x_2^{e_2}\), \(0\le e_i<2m\).
- For a polynomial \(G\), set

  \[
  \rho_m(G)=[X_{\mathrm{top}}]\operatorname{NF}(G).
  \]

  Because the leading homogeneous forms are
  \(x_0^{2m},x_1^{2m},x_2^{2m}\), the monic complete-intersection residue is
  \(\rho_m\).
- All indices on \(x_i,F_i,q_i\) are read modulo three.

## Proof Strategy

The proof first computes periods one and two in their finite algebras, where
nilpotence gives the constant formal spectra.  It then computes normalized
conjugacy by the unique diagonal action on the monic-centered Hénon form.

For period three, the three orbit equations form a monic complete
intersection.  Its Jacobian is also the derivative trace, so the
trace--residue theorem turns the desired moment into one top-coefficient
extraction.  Weighted scaling leaves only four possible parameter monomials.
The separated algebra removes the constant-in-\(\varepsilon\) term, and a
Puiseux valuation analysis of every root-triple cluster removes the
order-\(\varepsilon^m\) term.  Reversal gives the parity statement.  A
monomial recurrence and an exact Laurent fiber sum then give the displayed
nested-binomial expression for \(D_m\).  Finally, the quartic slope is
recomputed by an independent tensor-residue argument, the quartic constant is
evaluated by a short exact normal-form ledger, and the fixed-cycle subtraction
is shown to vanish.

## Dependency Map

1. The period-one and period-two spectra depend on \(q^2=0\) in
   \(k[x]/((x^m-a)^2)\).
2. The normalized quotient coordinate depends on normal-form uniqueness and
   the diagonal scaling calculation.
3. The trace--residue identity depends on monic freeness and the Jacobian
   determinant calculation.
4. The two-term law depends on weighted homogeneity, the separated algebra at
   \(\varepsilon=0\), and the local valuation lemma at \(\varepsilon=0\).
5. The odd-\(m\) vanishing of \(C_m\) depends on cyclic reversal.
6. The formula for \(D_m\) depends on the explicit normal-form recurrence,
   the local binomial fiber identity (9.14), the distinguished-coordinate
   congruence, and the transfer-flow bijection in Step 9.
7. The quartic separator depends on the full-fiber root-multiplicity lemma,
   the exact quartic residue ledgers, the vanishing fixed contribution, and
   the normalized quotient coordinate \(L^3\).  Its slope is proved directly
   in Step 12 as well as by specialization of Step 9.
8. No theorem in this package depends on a numerical check for
   \(2\le m\le7\).

## Proof

### Step 1. The finite fixed algebras and their formal spectra

Write \(p=p_{m,a}\) and \(q=q_{m,a}\).  A fixed point satisfies

\[
y+p(x)=x,
\qquad
x=y.
\]

Thus the fixed algebra is

\[
B_1=k[x]/(p(x))=k[x]/((x^m-a)^2),
\]

which has dimension \(2m\).  In this algebra,

\[
q=2m x^{m-1}(x^m-a)
\qquad\text{and}\qquad
q^2=0.
\]

The trace of

\[
Df_{m,a}(x,y)=
\begin{pmatrix}q(x)&1\\1&0\end{pmatrix}
\]

is \(q\).  Since \(M_q\) is nilpotent, its characteristic polynomial on
the \(2m\)-dimensional algebra is \(T^{2m}\).  This proves the formal
period-one multiset \(0^{\times2m}\).  Notice that this argument uses
nilpotence; for \(a\ne0\), \(q\) is generally not the zero element of
\(B_1\).

Now compute

\[
f_{m,a}^2(x,y)
=\bigl(x+p(y+p(x)),\;y+p(x)\bigr).
\]

The second fixed equation gives \(p(x)=0\), and then the first gives
\(p(y)=0\).  Hence

\[
B_2=k[x,y]/(p(x),p(y))
\]

has dimension \((2m)^2\).  On this algebra,

\[
\operatorname{tr}Df_{m,a}^2
=2+q(x)q(y).
\]

The element \(q(x)q(y)\) has square zero.  Therefore multiplication by the
displayed trace has the sole eigenvalue \(2\), with multiplicity \((2m)^2\).
On the embedded fixed algebra, the same trace is \(2+q^2=2\).  Subtracting
the length-\(2m\) formal fixed spectral cycle leaves

\[
2^{\times((2m)^2-2m)}.
\]

This computation remains valid at \(a=0\), because it took place in the
monic quotient algebras and did not reduce the schemes.

### Step 2. The normalized conjugacy coordinate

Let \(h_c(x,y)=(cx,cy)\) for \(c\in k^\times\).  A direct computation gives

\[
h_c^{-1}f_{m,a}h_c(x,y)
=\left(y+c^{-1}(c^m x^m-a)^2,x\right)
=\left(y+c^{2m-1}(x^m-ac^{-m})^2,x\right).
\]

It lies again in the monic family precisely when

\[
c^{2m-1}=1,
\]

and its new parameter is \(b=ac^{-m}\).  It follows immediately that

\[
b^{2m-1}=a^{2m-1}.
\]

Conversely, suppose \(a^{2m-1}=b^{2m-1}\).  If \(a=0\), then \(b=0\).
If \(a\ne0\), put \(\zeta=b/a\).  Then \(\zeta^{2m-1}=1\).  Since
\(\gcd(m,2m-1)=1\), exponentiation by \(-m\) is an automorphism of the
group of \((2m-1)\)-st roots of unity.  There is therefore a
\(c\) satisfying

\[
c^{2m-1}=1,
\qquad
c^{-m}=\zeta.
\]

The preceding diagonal calculation conjugates \(f_{m,a}\) to \(f_{m,b}\).

For necessity, normal-form uniqueness says that a polynomial conjugacy
between two one-factor monic-centered Hénon normal forms is affine diagonal
after comparing their reduced Hénon decompositions.  If an affine diagonal
map is initially written as

\[
(x,y)\longmapsto(cx+d,cy+d),
\]

the coefficient of \(x^{2m-1}\) in the transformed degree-\(2m\)
polynomial is \(2m d/c\).  Centering on both sides and characteristic zero
force \(d=0\).  Thus the preceding \(h_c\) calculation exhausts normalized
conjugacies and proves the equivalence.

### Step 3. Cyclic equations, Jacobian, and derivative trace

Represent an orbit by states \((x_i,x_{i-1})\).  The equation

\[
f_{m,a}(x_i,x_{i-1})=(x_{i+1},x_i)
\]

is

\[
p_{m,a}(x_i)+x_{i-1}-x_{i+1}=0.
\]

Hence \(F_i=0\) at \(\varepsilon=1\) is exactly the period-three cyclic
system.

The Jacobian matrix of the deformed system is

\[
\begin{pmatrix}
q_0&-\varepsilon&\varepsilon\\
\varepsilon&q_1&-\varepsilon\\
-\varepsilon&\varepsilon&q_2
\end{pmatrix}.
\]

Expansion of its determinant gives

\[
t_\varepsilon=q_0q_1q_2+
\varepsilon^2(q_0+q_1+q_2).
\]

Put

\[
M(q)=\begin{pmatrix}q&1\\1&0\end{pmatrix}.
\]

Along a three-cycle,

\[
Df_{m,a}^3=M(q_2)M(q_1)M(q_0).
\]

Multiplying these three \(2\times2\) matrices and taking the trace gives

\[
\operatorname{tr}Df_{m,a}^3
=q_0q_1q_2+q_0+q_1+q_2=t_1.
\]

### Step 4. Flatness, absence of points at infinity, and residue

Choose any degree-compatible monomial order.  The leading monomials of
\(F_0,F_1,F_2\) are

\[
x_0^{2m},\qquad x_1^{2m},\qquad x_2^{2m}.
\]

They are pairwise coprime, so Buchberger's coprime-leading-monomial
criterion makes \(F_0,F_1,F_2\) a Gröbner basis over
\(k[a,\varepsilon]\).  The standard monomials are

\[
x_0^{e_0}x_1^{e_1}x_2^{e_2},
\qquad 0\le e_i<2m.
\]

They form a free basis, proving rank \((2m)^3\) and flatness for every
\((a,\varepsilon)\), including \(a=0\) and \(\varepsilon=0\).

The highest homogeneous parts \(x_i^{2m}\) have no common zero in
\(\mathbb P^2\).  Thus the projective closure adds no solution at infinity,
and the affine quotient accounts for the full intersection multiplicity.

The Jacobian of this complete intersection is \(t_\varepsilon\).  Apply the
trace--residue identity with \(h=t_\varepsilon^m\):

\[
S_m(a,\varepsilon)
=\operatorname{Tr}(M_{t_\varepsilon^m})
=\operatorname{Res}(t_\varepsilon^m t_\varepsilon)
=\operatorname{Res}(t_\varepsilon^{m+1}).
\]

For the present monic leading forms, Macaulay's coefficient form of the
global residue is

\[
\operatorname{Res}(G)=
[x_0^{2m-1}x_1^{2m-1}x_2^{2m-1}]\operatorname{NF}(G)
=\rho_m(G).
\]

This also proves that \(S_m\in\mathbb Z[a,\varepsilon]\): the defining
relations, multiplication matrices, and normal-form recurrence all have
integer coefficients.

### Step 5. Weighted homogeneity leaves four terms

Give the variables weights

\[
\operatorname{wt}(x_i)=1,
\qquad
\operatorname{wt}(a)=m,
\qquad
\operatorname{wt}(\varepsilon)=2m-1=\nu.
\]

Each \(F_i\) has weight \(2m\), each \(q_i\) has weight \(\nu\), and
\(t_\varepsilon\) has weight \(3\nu\).  Equivalently, under

\[
x_i\mapsto\lambda x_i,
\quad
a\mapsto\lambda^m a,
\quad
\varepsilon\mapsto\lambda^\nu\varepsilon,
\]

the quotient algebras are identified and multiplication by
\(t_\varepsilon^m\) scales by \(\lambda^{3m\nu}\).  Its trace has the same
weight.  Hence every parameter monomial \(a^r\varepsilon^s\) appearing in
\(S_m\) satisfies

\[
mr+\nu s=3m\nu.
\]

Because \(\gcd(m,\nu)=1\), \(r\) is a multiple of \(\nu\).  Nonnegative
solutions are exactly

\[
(r,s)=(0,3m),(\nu,2m),(2\nu,m),(3\nu,0).
\]

Therefore

\[
S_m=
c_{0,m}\varepsilon^{3m}
+c_{1,m}a^\nu\varepsilon^{2m}
+c_{2,m}a^{2\nu}\varepsilon^m
+c_{3,m}a^{3\nu}.
\]

### Step 6. The separated algebra removes \(c_{3,m}\)

At \(\varepsilon=0\), the quotient is the tensor product of three copies of

\[
k[a,x]/((x^m-a)^2).
\]

In each factor \(q_i^2=0\), while

\[
t_0=q_0q_1q_2.
\]

Since \(m\ge2\), \(t_0^m=0\).  Thus

\[
S_m(a,0)=0,
\]

and comparison with the four-term expression gives \(c_{3,m}=0\).

### Step 7. Local degeneration removes \(c_{2,m}\)

Fix \(a\ne0\), and choose the \(m\) distinct roots of \(x^m=a\).  Work
over an algebraic closure of the Puiseux field in \(\varepsilon\), with
valuation \(v(\varepsilon)=1\).  Flatness implies that all \((2m)^3\)
solutions, with their algebra multiplicities, specialize into clusters
indexed by triples

\[
(\alpha_0,\alpha_1,\alpha_2),
\qquad \alpha_i^m=a.
\]

Write \(x_i=\alpha_i+\delta_i\).  Since \(\alpha_i\ne0\), Taylor expansion
gives

\[
(x_i^m-a)^2=c_i\delta_i^2+O(\delta_i^3),
\qquad
q_i=d_i\delta_i+O(\delta_i^2),
\]

with \(c_i,d_i\ne0\).  Thus, whenever \(\delta_i\ne0\),
\(v(q_i)=v(\delta_i)\).

There are three root-pattern cases.

**All roots distinct.**  Each constant
\(\alpha_{i-1}-\alpha_{i+1}\) is nonzero.  In \(F_i=0\), the terms of
valuations \(2v(\delta_i)\) and \(1\) must balance.  Hence

\[
v(q_i)=v(\delta_i)=\tfrac12
\]

for all \(i\), and

\[
v(t_\varepsilon)\ge\tfrac32.
\]

**Exactly two roots equal.**  After cyclic relabeling, suppose
\(\alpha_0=\alpha_1\ne\alpha_2\).  The equations for \(i=0,1\) have
nonzero constant coupling terms, so

\[
v(q_0)=v(q_1)=\tfrac12.
\]

In the remaining equation the coupling is
\(\varepsilon(\delta_1-\delta_0)\), of valuation at least \(3/2\).
If \(v(\delta_2)<3/4\), its square would be the unique term of least
valuation in that equation, which is impossible.  Therefore

\[
v(q_2)\ge\tfrac34,
\qquad
v(t_\varepsilon)\ge\tfrac74.
\]

**All three roots equal.**  Let \(r\) be the minimum valuation among the
nonzero \(\delta_i\).  Every coupling term has valuation at least \(1+r\).
If \(r<1\), choose an index attaining \(r\); its square term has valuation
\(2r<1+r\) and cannot cancel.  Hence every nontrivial branch in this cluster
satisfies \(r\ge1\), and

\[
v(t_\varepsilon)\ge3.
\]

The exact diagonal fixed branch is treated separately in Step 10; its
contribution is identically zero for the present power.

For a finite algebra over a characteristic-zero field, the trace of
multiplication by an element is the sum, over support points, of the element's
residue-field value multiplied by the local algebra length.  Nilpotent parts
have trace zero.  The Puiseux bounds above therefore imply that every
nonfixed cluster contributes to \(S_m\) with \(\varepsilon\)-valuation
strictly greater than \(m\): the lower bounds are respectively
\(3m/2\), \(7m/4\), and \(3m\).  Summation can only increase, not decrease,
the valuation.  Consequently

\[
v_\varepsilon(S_m(a,\varepsilon))>m
\qquad(a\ne0).
\]

After \(c_{3,m}=0\), the only possible term of exact
\(\varepsilon\)-order \(m\) is
\(c_{2,m}a^{2\nu}\varepsilon^m\).  Since \(a\ne0\), the valuation estimate
forces \(c_{2,m}=0\).  Setting

\[
C_m=c_{0,m},\qquad D_m=c_{1,m}
\]

proves the two-term law.

### Step 8. Reversal removes \(C_m\) for odd \(m\)

Apply the involution \(x_i\mapsto x_{-i}\).  It sends the system with
parameter \(\varepsilon\) to the system with parameter \(-\varepsilon\):

\[
F_i(x_{-\bullet};\varepsilon)=F_{-i}(x_\bullet;-\varepsilon).
\]

The expression \(t_\varepsilon\) is unchanged because it contains
\(\varepsilon\) only through \(\varepsilon^2\).  Hence the induced algebra
isomorphism gives

\[
S_m(a,\varepsilon)=S_m(a,-\varepsilon).
\]

The term \(D_m a^\nu\varepsilon^{2m}\) is always even in
\(\varepsilon\).  If \(m\) is odd, \(3m\) is odd, so comparison in

\[
S_m=C_m\varepsilon^{3m}+D_m a^\nu\varepsilon^{2m}
\]

forces \(C_m=0\).

### Step 9. Exact coefficient extraction for \(D_m\)

The normal-form recurrence used in this step is obtained directly from
\(F_i=0\): for every exponent \(e_i\ge2m\),

\[
\begin{aligned}
x_i^{e_i}\equiv{}&
2a x_i^{e_i-m}-a^2x_i^{e_i-2m}\\
&-\varepsilon x_i^{e_i-2m}x_{i-1}
+\varepsilon x_i^{e_i-2m}x_{i+1}
\pmod{(F_0,F_1,F_2)}.
\end{aligned}
\tag{R}
\]

To make the reduction certificate precise, let
\(\boldsymbol\delta_i\) be the \(i\)-th standard basis vector of
\(\mathbb Z^3\), and, for
\(\boldsymbol e=(e_0,e_1,e_2)\in\mathbb Z^3\) and
\(\alpha,\beta\in\mathbb Z\), define the reduction-state coefficient

\[
\mathscr R_m(\boldsymbol e;\alpha,\beta)
=
[a^\alpha\varepsilon^\beta X_{\mathrm{top}}]
\operatorname{NF}(x_0^{e_0}x_1^{e_1}x_2^{e_2}).
\tag{9.1}
\]

It is zero if some \(e_i<0\), or if \(\alpha<0\) or \(\beta<0\).  Its
complete set of base cases is

\[
\mathscr R_m(\boldsymbol e;\alpha,\beta)
=
\begin{cases}
1,&\boldsymbol e=(\nu,\nu,\nu)\text{ and }(\alpha,\beta)=(0,0),\\
0,&0\le e_i<2m\text{ for all }i\text{ and otherwise}.
\end{cases}
\tag{9.2}
\]

If \(e_i\ge2m\), recurrence (R) gives exactly four branches:

\[
\begin{aligned}
\mathscr R_m(\boldsymbol e;\alpha,\beta)
={}&2\mathscr R_m(\boldsymbol e-m\boldsymbol\delta_i;
                    \alpha-1,\beta)\\
&-\mathscr R_m(\boldsymbol e-2m\boldsymbol\delta_i;
                    \alpha-2,\beta)\\
&-\mathscr R_m(\boldsymbol e-2m\boldsymbol\delta_i
                    +\boldsymbol\delta_{i-1};
                    \alpha,\beta-1)\\
&+\mathscr R_m(\boldsymbol e-2m\boldsymbol\delta_i
                    +\boldsymbol\delta_{i+1};
                    \alpha,\beta-1).
\end{aligned}
\tag{9.3}
\]

These are, respectively, the
\(2a x_i^{e_i-m}\), \(-a^2x_i^{e_i-2m}\),
\(-\varepsilon x_i^{e_i-2m}x_{i-1}\), and
\(+\varepsilon x_i^{e_i-2m}x_{i+1}\) branches.  Each child has strictly
smaller total exponent \(e_0+e_1+e_2\): the decreases are
\(m,2m,2m-1,2m-1\).  Thus (9.2)--(9.3), with any fixed choice rule for a
reducible coordinate, are a terminating induction certificate.  They also
show directly which branch changes the requested \(a\)- or
\(\varepsilon\)-degree.

There is no reduction-order ambiguity.  Indeed, Step 4 gives a unique normal
form, so (9.3) holds for every reducible coordinate.  Equivalently, the same
coefficient is the Laurent coefficient at infinity

\[
\mathscr R_m(\boldsymbol e;\alpha,\beta)
=
[a^\alpha\varepsilon^\beta x_0^{-1}x_1^{-1}x_2^{-1}]
\frac{x_0^{e_0}x_1^{e_1}x_2^{e_2}}{F_0F_1F_2},
\tag{9.4}
\]

where each reciprocal is expanded as

\[
\frac1{F_i}
=x_i^{-2m}\sum_{h\ge0}
\left(
\frac{2a x_i^m-a^2-\varepsilon x_{i-1}
      +\varepsilon x_{i+1}}{x_i^{2m}}
\right)^h.
\tag{9.5}
\]

The product in (9.5) canonically groups reduction strings by the number of
uses of each of the four branches at each coordinate.  Interleavings of
reductions at different coordinates are not different terms; they are
different orders for the same Laurent monomial.  This is the promised
order-independent, no-double-counting interpretation of the recurrence.

Expand the residue integrand as

\[
t_\varepsilon^{m+1}
=\sum_{j=0}^{m+1}\binom{m+1}{j}
\varepsilon^{2j}(q_0q_1q_2)^{m+1-j}
(q_0+q_1+q_2)^j.
\tag{9.6}
\]

After extracting the scalar \(2m\) from every \(q_i\), the term indexed by
\(j\) contains

\[
(2m)^{3(m+1-j)+j}=(2m)^{3m+3-2j}.
\]

Let \(\bar q_i=x_i^{m-1}(x_i^m-a)\), and define the integer

\[
\begin{aligned}
\mathcal C_{m,j}:={}&
[a^{\nu}\varepsilon^{2m-2j}X_{\mathrm{top}}]\\
&\operatorname{NF}\left(
(\bar q_0\bar q_1\bar q_2)^{m+1-j}
(\bar q_0+\bar q_1+\bar q_2)^j
\right).
\end{aligned}
\tag{9.7}
\]

Equations (9.6)--(9.7) give the proved identity

\[
D_m=\sum_{j=0}^{m+1}
\binom{m+1}{j}(2m)^{3m+3-2j}\mathcal C_{m,j}.
\tag{9.8}
\]

Here is a mechanically checkable evaluation of every
\(\mathcal C_{m,j}\).  Put \(r=m-j\), and first suppose \(0\le j\le m\).
Choose \(\boldsymbol s=(s_0,s_1,s_2)\in\mathbb N^3\) with
\(|\boldsymbol s|=j\), and put

\[
N_i=r+1+s_i.
\]

Choosing the low term in exactly \(\ell_i\) of the \(N_i\) factors of
\(\bar q_i=x_i^{2m-1}-a x_i^{m-1}\) gives

\[
e_i=(2m-1)N_i-m\ell_i,
\qquad 0\le\ell_i\le N_i.
\]

Consequently (9.1)--(9.3) give the finite induction certificate

\[
\begin{aligned}
\mathcal C_{m,j}
={}&\sum_{|\boldsymbol s|=j}\binom{j}{s_0,s_1,s_2}
\sum_{0\le\ell_i\le N_i}
(-1)^{|\boldsymbol\ell|}
\prod_{i=0}^2\binom{N_i}{\ell_i}\\
&\hspace{32mm}\cdot
\mathscr R_m(\boldsymbol e;
\nu-|\boldsymbol\ell|,2r).
\end{aligned}
\tag{9.9}
\]

For \(j=m+1\), the requested \(\varepsilon\)-degree is negative, so
\(\mathcal C_{m,m+1}=0\) by convention.

For an explicit nonrecursive certificate, unfold (9.5).  At source
coordinate \(i\), let

\[
A_i,B_i,U_i,V_i
\]

be the numbers of choices of, respectively,
\(2a x_i^m\), \(-a^2\),
\(-\varepsilon x_{i-1}\), and
\(+\varepsilon x_{i+1}\), and put

\[
h_i=A_i+B_i+U_i+V_i,
\qquad
T_i=U_{i+1}+V_{i-1}.
\]

Thus \(T_i\) is the number of transfer branches whose monomial contributes
one power of \(x_i\).  A tuple

\[
(\boldsymbol s,\boldsymbol\ell,
  \boldsymbol A,\boldsymbol B,\boldsymbol U,\boldsymbol V)
\tag{9.10}
\]

is **admissible** precisely when all entries are nonnegative integers,
\(|\boldsymbol s|=j\), \(0\le\ell_i\le N_i\), and

\[
\begin{aligned}
|\boldsymbol\ell|+\sum_i(A_i+2B_i)&=\nu,\\
\sum_i(U_i+V_i)&=2r,\\
e_i+mA_i+T_i-2m(h_i+1)&=-1
\quad(i=0,1,2).
\end{aligned}
\tag{9.11}
\]

The first two lines select the requested parameter powers.  The last line is
exactly the condition that the Laurent exponent of \(x_i\) in (9.4) be
\(-1\).  The signed multiplicity of an admissible tuple is

\[
\begin{aligned}
W={}&(-1)^{|\boldsymbol\ell|+
                 \sum_i(B_i+U_i)}
2^{\sum_i A_i}
\binom{j}{s_0,s_1,s_2}\\
&\cdot\prod_{i=0}^2
\binom{N_i}{\ell_i}
\frac{h_i!}{A_i!B_i!U_i!V_i!}.
\end{aligned}
\tag{9.12}
\]

The signs in (9.12) come from the low term of \(\bar q_i\), the
\(-a^2\) branch, and the \(-\varepsilon x_{i-1}\) branch.  The power of two
comes from \(2a x_i^m\), and the multinomial is the exact number of branch
words at source \(i\) having the prescribed counts.  Equations
(9.4)--(9.5) now prove

\[
\boxed{\mathcal C_{m,j}=\sum_{\text{admissible tuples in (9.10)}}W.}
\tag{9.13}
\]

This sum is finite because (9.11) bounds the total numbers of \(a\)- and
\(\varepsilon\)-branches.  Every fully expanded choice in (9.5) has one and
only one tuple of branch counts, and (9.12) is exactly the sum of the words
with that tuple.  Thus no expanded choice is omitted or counted twice;
different tuples producing the same Laurent monomial are retained as the
distinct summands that they are.  Conversely, every admissible tuple has the
required three Laurent exponents and parameter degrees, so none is spurious.
This supplies the base cases, all four recurrence branches, their signs and
multiplicities, termination, exhaustiveness, and reduction order
independence.

It remains to evaluate the fibers in (9.13).  The required local summation is
the following elementary coefficient identity.  For
\(N,n,\alpha\in\mathbb N\),

\[
\begin{aligned}
&\sum_{\substack{\ell,A,B\ge0\\
                  \ell+A+2B=\alpha}}
(-1)^{\ell+B}2^A
\binom N\ell
\frac{(n+A+B)!}{n!A!B!}\\
&\hspace{35mm}
=(-1)^\alpha\binom{N-2n-2}{\alpha}.
\end{aligned}
\tag{9.14}
\]

Generalized binomial coefficients are understood on the right.  To prove
(9.14), take the coefficient of \(z^\alpha\) in

\[
\begin{aligned}
(1-z)^N
\sum_{A,B\ge0}
\frac{(n+A+B)!}{n!A!B!}(2z)^A(-z^2)^B
&=(1-z)^N(1-2z+z^2)^{-n-1}\\
&=(1-z)^{N-2n-2}.
\end{aligned}
\]

This identity performs exactly the missing signed fiber sum.  Fix
\((\boldsymbol s,\boldsymbol U,\boldsymbol V)\) and put

\[
n_i=U_i+V_i,
\qquad
\lambda_i=N_i-2n_i-2,
\qquad
\alpha_i=
\frac{(2m-1)(N_i-1)+T_i}{m}-2n_i.
\tag{9.15}
\]

These local exponents automatically have the required global degree.  Indeed,
\(\sum_i(N_i-1)=m+2r\) and
\(\sum_iT_i=\sum_i n_i=2r\), so

\[
\sum_i\alpha_i
=\frac{(2m-1)(m+2r)+2r}{m}-4r
=2m-1=\nu.
\]

The Laurent exponent equation in (9.11) says precisely that
\(\ell_i+A_i+2B_i=\alpha_i\).  Multiplying (9.14) by the orientation factor

\[
(-1)^{U_i}\binom{n_i}{U_i}
\]

turns its factorial into

\[
\binom{n_i}{U_i}
\frac{(n_i+A_i+B_i)!}{n_i!A_i!B_i!}
=\frac{h_i!}{A_i!B_i!U_i!V_i!}.
\]

Thus (9.14), including its signs and \(2^{A_i}\), is exactly the sum of
(9.12) over all \((\ell_i,A_i,B_i)\) with the fixed coupling orientations.
Every decorated Laurent term has a unique
\((\boldsymbol s,\boldsymbol U,\boldsymbol V)\), so this regrouping is
exhaustive and has no double counting.  Define

\[
B(\lambda,\alpha)=
\begin{cases}
(-1)^\alpha\binom\lambda\alpha,&\alpha\in\mathbb N,\\
0,&\text{otherwise}.
\end{cases}
\tag{9.16}
\]

The integrality condition in (9.15) is

\[
T_i\equiv N_i-1=r+s_i\pmod m.
\tag{9.17}
\]

Write \(T_i=r+s_i+mz_i\).  Because
\(\sum_iT_i=2r\) and
\(\sum_i(r+s_i)=m+2r\),

\[
z_0+z_1+z_2=-1.
\tag{9.18}
\]

Also \(0\le r+s_i\le m\).  Hence \(T_i\ge0\) implies \(z_i\ge-1\), and
\(z_i=-1\) is possible only when
\(0\le r+s_i-m=s_i-j\), that is, only when
\(s_i=j\) and \(T_i=0\).

Suppose first that \(j\ge1\).  Two indices cannot both have \(s_i=j\),
because \(\sum_i s_i=j\).  Equation (9.18) therefore forces a unique
distinguished coordinate \(d\) such that

\[
s_d=j,\quad T_d=0,
\qquad
s_i=0,\quad T_i=r\quad(i\ne d).
\tag{9.19}
\]

This conclusion holds for every \(1\le j\le m\).  By cyclic symmetry take
\(d=0\), and set

\[
u=U_0,\qquad v=V_0,\qquad k=n_0=u+v.
\]

The incoming-transfer equations uniquely give

\[
U_1=0,\quad V_2=0,\quad
V_1=r-u,\quad U_2=r-v,\quad
n_1=r-u,\quad n_2=r-v.
\tag{9.20}
\]

Conversely, every nonnegative \((k,u,v)\) with \(u+v=k\) and the ranges
below gives exactly one such transfer configuration.  At the distinguished
coordinate,

\[
\lambda_0=m-1-2k,\qquad
\alpha_0=2m-1-2k,
\]

whereas at the other two coordinates

\[
(\lambda_1,\alpha_1)=(2u-r-1,2u),
\qquad
(\lambda_2,\alpha_2)=(2v-r-1,2v).
\]

Using

\[
(-1)^\alpha\binom{\alpha-M}{\alpha}
=\binom{M-1}{\alpha}
\qquad(M\ge1,\ \alpha\ge0),
\]

the three local factors become

\[
B(\lambda_0,\alpha_0)
=\binom{m-1}{2(m-k)-1},\quad
B(\lambda_1,\alpha_1)=\binom r{2u},\quad
B(\lambda_2,\alpha_2)=\binom r{2v}.
\tag{9.21}
\]

They are nonzero exactly when

\[
\left\lceil\frac m2\right\rceil\le k\le m-1,
\qquad 2u\le r,\qquad 2v\le r.
\]

The orientation multiplicity is \(\binom{k}{u}\); the other two choices are
forced by (9.20).  Its sign is

\[
(-1)^{U_0+U_1+U_2}
=(-1)^{u+r-v}=(-1)^{r+k}.
\]

Hence the exact signed fiber over \((d,k,u,v)\) is

\[
(-1)^{r+k}
\binom{m-1}{2(m-k)-1}
\binom{k}{u}
\binom r{2u}
\binom r{2v}.
\tag{9.22}
\]

Since \(2u\le r\), \(2v\le r\), and \(u+v=k\) imply \(k\le r\), summing
(9.22) and then the three possible distinguished coordinates proves

\[
\mathcal C_{m,j}=3A_{m,r}
\qquad(1\le j\le m).
\tag{9.23}
\]

When \(j>\lfloor m/2\rfloor\), one has
\(r=m-j<\lceil m/2\rceil\), so the defining range is empty and

\[
\mathcal C_{m,j}=0.
\tag{9.24}
\]

For \(j=0\), one has \(r=m\), \(s_i=0\), and
\(T_i=m(1+z_i)\).  The nonnegative incoming-transfer patterns are exactly
the cyclic permutations of

\[
(0,m,m)\qquad\text{and}\qquad(0,0,2m).
\tag{9.25}
\]

For the first type, its unique zero coordinate plays the role of \(d\), and
the preceding argument gives \(3A_{m,m}\).  For the second type, take
\(T_0=2m\) and \(T_1=T_2=0\).  The flow equations force \(n_0=0\), so at
coordinate zero

\[
N_0=m+1,qquad \lambda_0=m-1,qquad \alpha_0=2m+1,
\]

and consequently

\[
B(\lambda_0,\alpha_0)
=-\binom{m-1}{2m+1}=0.
\tag{9.26}
\]

All three rotations of the second type vanish.  Therefore

\[
\mathcal C_{m,0}=3A_{m,m}.
\]

Finally, \(\mathcal C_{m,m+1}=0\) because its requested
\(\varepsilon\)-degree is negative.  Combining these identities with (9.8)
proves

\[
\boxed{
D_m=3\sum_{j=0}^{\lfloor m/2\rfloor}
\binom{m+1}{j}(2m)^{3m+3-2j}A_{m,m-j}.}
\tag{9.27}
\]

Factoring the smallest power of \(2m\), with
\(q=\lfloor m/2\rfloor\), gives

\[
\boxed{
D_m=3(2m)^{3m+3-2q}
\sum_{j=0}^{q}\binom{m+1}{j}
(2m)^{2(q-j)}A_{m,m-j}
=3(2m)^{3m+3-2q}E_m.}
\tag{9.28}
\]

This proves the frozen nested-binomial certificate.  It does not prove that
\(D_m\ne0\) in every degree; that separate nonvanishing statement remains
open.

### Step 10. The fixed contribution to the period-three moment is zero

On the fixed algebra \(B_1\), all three cyclic coordinates agree and the
deformed Jacobian restricts to

\[
t_\varepsilon=q^3+3\varepsilon^2q.
\]

Since \(q^2=0\), its \(m\)-th power vanishes identically for every
\(\varepsilon\):

\[
(q^3+3\varepsilon^2q)^m=0
\qquad(m\ge2).
\]

This supplies the diagonal-cluster vanishing used in Step 7.  At
\(\varepsilon=1\), \(t_1=\operatorname{tr}Df_{m,a}^3=q^3+3q\), so its algebra
trace contribution is zero.  The formal exact-period-three moment is the raw
\(f^3\)-fixed moment minus this fixed contribution and hence equals
\(S_m(a,1)\).

### Step 11. Classification of the complete quartic fixed-trace-zero fiber

Let \(p\) be any monic-centered quartic, and let

\[
B_p=k[x]/(p).
\]

The formal fixed trace multiset of \(f_p\) is the formal multiset of
multiplication by \(p'(x)\) on \(B_p\).  For every distinct root \(\alpha\)
of \(p\), the corresponding eigenvalue is \(p'(\alpha)\), repeated with the
local algebra length.  Thus the multiset is \(0^4\) if and only if

\[
p'(\alpha)=0
\]

for every root \(\alpha\) of \(p\).  This condition says that every root is
multiple.

A degree-four polynomial all of whose distinct roots have multiplicity at
least two has multiplicity partition \(4\) or \(2+2\).

- In the first case, \(p=(x-\alpha)^4\).  Centering makes the coefficient of
  \(x^3\), namely \(-4\alpha\), vanish, so \(\alpha=0\) and \(p=x^4\).
- In the second case, \(p=(x-\alpha)^2(x-\beta)^2\).  Centering gives
  \(2\alpha+2\beta=0\), hence \(\beta=-\alpha\) and

  \[
  p=(x^2-\alpha^2)^2.
  \]

Writing \(L=\alpha^2\) covers both cases, including \(L=0\), and proves

\[
p=(x^2-L)^2.
\]

The coefficient of \(x^2\) is \(-2L\), so \(L\) is unique.

### Step 12. Two independent exact quartic coefficient ledgers

For \(m=2\), \(\nu=3\).  The elementary evaluations of the closed
expression are

\[
H(2,1)=2,
\qquad
A_{2,2}=-2,
\qquad
A_{2,1}=0.
\]

The proved formula (9.27) gives

\[
D_2=3\cdot4^9(-2)=-1572864.
\]

For an independent derivation that does not use the all-degree collapse, put

\[
P_a(x)=(x^2-a)^2,\qquad
g_a(x)=x(x^2-a),\qquad
L_i=x_{i-1}-x_{i+1}.
\]

Then \(F_i=P_a(x_i)+\varepsilon L_i\), \(q_i=4g_a(x_i)\), and

\[
t_\varepsilon
=4^3g_0g_1g_2+4\varepsilon^2(g_0+g_1+g_2).
\]

Thus

\[
t_\varepsilon^3
=\sum_{j=0}^3\binom3j4^{9-2j}\varepsilon^{2j}G_j,
\qquad
G_j=(g_0g_1g_2)^{3-j}(g_0+g_1+g_2)^j.
\]

Let

\[
\mathscr L_j(a,\varepsilon)
=[x_0^{-1}x_1^{-1}x_2^{-1}]
\frac{G_j}{F_0F_1F_2}.
\]

In the Laurent normalization of (9.4),

\[
\mathcal C_{2,j}
=[a^3\varepsilon^{4-2j}]\mathscr L_j(a,\varepsilon),
\qquad
D_2=\sum_{j=0}^3\binom3j4^{9-2j}\mathcal C_{2,j}.
\]

The weights \(\operatorname{wt}(x_i)=1\),
\(\operatorname{wt}(a)=2\), and
\(\operatorname{wt}(\varepsilon)=3\) show that the selected coefficient is
a constant multiple of \(a^3\).  We may therefore put \(a=1\).  Write

\[
P(x)=(x^2-1)^2,\qquad g(x)=x(x^2-1),
\]

and expand

\[
\frac1{P_i+\varepsilon L_i}
=\sum_{h_i\ge0}(-1)^{h_i}\varepsilon^{h_i}
\frac{L_i^{h_i}}{P_i^{h_i+1}}.
\tag{12.1}
\]

Define the one-variable Laurent coefficients

\[
\rho_{n,h}(d)
=[x^{-1}]\frac{x^d g(x)^n}{P(x)^{h+1}}
\qquad(d\ge0).
\]

The identities

\[
\frac{g^3}{P}=x^3(x^2-1),\qquad
\frac{g^3}{P^2}=\frac{x^3}{x^2-1},\qquad
\frac{g^3}{P^3}=\frac{x^3}{(x^2-1)^3}
\]

give

\[
\rho_{3,0}(d)=0\quad(d\ge0),
\]

\[
\rho_{3,1}(0)=\rho_{3,1}(2)=1,
\qquad \rho_{3,1}(1)=0,
\]

and

\[
\rho_{3,2}(0)=\rho_{3,2}(1)=0,
\qquad \rho_{3,2}(2)=1.
\]

For \(j=0\), equation (12.1) must supply total
\(h_0+h_1+h_2=4\).  The first displayed vanishing forces every
\(h_i\ge1\), so the only possibilities are the three cyclic arrangements of
\((2,1,1)\).  For \(h_0=2\), \(h_1=h_2=1\), the tensor coefficient is

\[
(\rho_{3,2}\otimes\rho_{3,1}\otimes\rho_{3,1})
(L_0^2L_1L_2).
\]

Since

\[
L_0=x_2-x_1,\quad L_1=x_0-x_2,\quad L_2=x_1-x_0,
\]

one has

\[
L_1L_2=-x_0^2+x_0(x_1+x_2)-x_1x_2.
\]

Taking the \(x_0\)-coefficient leaves \(-(x_2-x_1)^2\), and the remaining
two coefficients give \(-(1+0+1)=-2\).  The other cyclic arrangements give
the same value.  The total sign in (12.1) is \((-1)^4=1\), whence

\[
\mathcal C_{2,0}=-6.
\]

For \(j=1\), every monomial in \(G_1\) contains powers \(g^3,g^2,g^2\),
while the required total denominator order is only
\(h_0+h_1+h_2=2\).  At any coordinate with \(h_i=0\), both
\(g^2/P=x^2\) and \(g^3/P=x^3(x^2-1)\) are polynomials; multiplication by
nonnegative powers from the \(L_i\) cannot create an \(x_i^{-1}\) term.
Nonvanishing would require all three \(h_i\ge1\), a contradiction.  Hence

\[
\mathcal C_{2,1}=0.
\]

For \(j=2\), the required internal \(\varepsilon\)-degree is zero.  Put

\[
\mu_n=[x^{-1}]\frac{g(x)^n}{P(x)}.
\]

Directly,

\[
\mu_1=1,\qquad \mu_2=0,\qquad \mu_3=0.
\]

The square terms in \(G_2\) have exponent type \((3,1,1)\), and the cross
terms have type \((2,2,1)\); their tensor coefficients are respectively
\(\mu_3\mu_1^2\) and \(\mu_2^2\mu_1\), both zero.  Thus

\[
\mathcal C_{2,2}=0.
\]

The \(j=3\) summand already contains \(\varepsilon^6\), so it cannot
contribute to \(\varepsilon^4\).  This second derivation yields

\[
\boxed{D_2=4^9(-6)=-1572864}
\]

without using the all-degree binomial collapse.

It remains to obtain \(C_2\).  Set \(a=0\) and
\(\varepsilon=1\).  Then

\[
F_i=x_i^4+x_{i-1}-x_{i+1},
\qquad
t=64x_0^3x_1^3x_2^3+4(x_0^3+x_1^3+x_2^3).
\]

Let \(R(e_0,e_1,e_2)\) be the coefficient of
\(x_0^3x_1^3x_2^3\) in the normal form of
\(x_0^{e_0}x_1^{e_1}x_2^{e_2}\).  The three exact recurrences are

\[
\begin{aligned}
R(e_0,e_1,e_2)
&=R(e_0-4,e_1+1,e_2)-R(e_0-4,e_1,e_2+1),\\
R(e_0,e_1,e_2)
&=-R(e_0+1,e_1-4,e_2)+R(e_0,e_1-4,e_2+1),\\
R(e_0,e_1,e_2)
&=R(e_0+1,e_1,e_2-4)-R(e_0,e_1+1,e_2-4),
\end{aligned}
\tag{12.2}
\]

used when the respectively reduced exponent is at least four.  The terminal
condition is \(R(3,3,3)=1\), while every other standard exponent triple has
value zero.  Applying (12.2) gives the complete list needed for the expansion
of \(t^3\):

| Exponent pattern | \(R\)-value |
|---|---:|
| \((9,9,9)\) | \(-6\) |
| a cyclic permutation of \((9,6,6)\) | \(2\) |
| a cyclic permutation of \((9,3,3)\) | \(0\) |
| a cyclic permutation of \((6,6,3)\) | \(-1\) |
| a permutation of \((9,0,0)\) | \(0\) |
| a permutation of \((6,3,0)\) | \(0\) |
| \((3,3,3)\) | \(1\) |

For example,

\[
R(9,6,6)=R(5,7,6)-R(5,6,7)=1-(-1)=2,
\]

and

\[
R(9,9,9)=2R(5,10,9)=2(1-4)=-6;
\]

the signs in these two symmetry shortcuts are also obtained directly from
(12.2).  The remaining rows require at most two reductions, or have total
degree nine without already being the top standard monomial.

Put \(Q=64x_0^3x_1^3x_2^3\) and
\(R_0=4(x_0^3+x_1^3+x_2^3)\).  Grouping
\((Q+R_0)^3\) by the preceding exponent patterns gives

| Source | Top-coefficient contribution |
|---|---:|
| \(Q^3\) | \(262144(-6)=-1572864\) |
| \(3Q^2R_0\) | \(3\cdot49152\cdot2=294912\) |
| square terms in \(3QR_0^2\) | \(0\) |
| mixed terms in \(3QR_0^2\) | \(3\cdot6144(-1)=-18432\) |
| pure and \(2+1\) terms in \(R_0^3\) | \(0\) |
| fully mixed term in \(R_0^3\) | \(384\) |

Their sum is

\[
C_2=-1572864+294912-18432+384=-1296000.
\]

Thus \(C_2=-1296000\) and the independently reproduced slope
\(D_2=-1572864\) give

\[
S_2^{(3)}(L)
=-1296000-1572864L^3.
\]

Step 10 proves that this is already the exact-period-three moment.

### Step 13. Minimality and the cyclewise normalization

Steps 1 and 11 show that the full normalized quartic fixed-trace-zero fiber
is \(p=(x^2-L)^2\), and that its formal period-one and exact-period-two
trace data are independent of \(L\).  Step 2 specializes to

\[
f_{2,L}\sim f_{2,M}
\quad\Longleftrightarrow\quad
L^3=M^3.
\]

The coefficient of \(L^3\) in the period-three moment is
\(-1572864\ne0\).  Hence this moment separates exactly the normalized
conjugacy classes on the fiber, and no lower period can do so because both
lower formal trace multisets are constant.  Period three is therefore the
minimal separating period on this complete normalized fiber.

For completeness, the formal subtraction at fixed support preserves the
expected local multiplicity.  Let \(\alpha\) be a root of \(p\) of
multiplicity \(r\ge2\), and put

\[
\delta=x_0-\alpha,\qquad u=x_1-x_0,\qquad v=x_2-x_0.
\]

At \((\delta,u,v)=(0,0,0)\), the \((u,v)\)-Jacobian of
\((F_1,F_2)\) is

\[
\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]

so formal elimination gives

\[
u=-p(\alpha+\delta)+O(\delta^{2r-1}),
\qquad
v=p(\alpha+\delta)+O(\delta^{2r-1}).
\]

The remaining equation is

\[
F_0
=p(\alpha+\delta)+v-u
=3p(\alpha+\delta)+O(\delta^{2r-1}).
\]

Because \(2r-1>r\) and the characteristic is zero, its order is exactly
\(r\).  Thus the local length of \(\operatorname{Fix}(f^3)\) at every fixed
point equals its fixed-scheme length; no residual fixed support remains after
the prime-period subtraction.

The \(f^3\)-fixed algebra has length \(4^3=64\), and the subtracted fixed
algebra has length \(4\), so the formal exact-period-three zero-cycle has
length \(60\).  Every exact period-three orbit has three points, and cyclic
invariance of matrix trace makes the trace moment equal at those three
points.  Dividing the pointwise sum by three gives

\[
\frac{-1296000-1572864L^3}{3}
=-432000-524288L^3.
\]

This completes the theorem package.

## Corrections or Missing Assumptions

- The safe scheme-theoretic statement is that \(q\) is nilpotent on the fixed
  algebra, not that \(q=0\) as an algebra element.  Likewise,
  \(\operatorname{tr}Df^2=2+q(x)q(y)\) on the period-two algebra; its formal
  spectrum is constant at \(2\).  Replacing these with literal equalities on
  nonreduced schemes would be false.
- The conjugacy equivalence is asserted only in the normalized
  Friedland--Milnor Hénon category.  It is not a classification of arbitrary
  polynomial automorphisms by the parameter \(a^{2m-1}\).
- Although the exact coefficient certificate is proved, any statement that
  period three separates the family for every \(m\) must additionally prove
  \(D_m\ne0\).

## Open Risks

- **Open conjecture / nonclaim:** \(D_m\ne0\) for every \(m\ge2\).  The exact
  checks at \(m=2,\ldots,7\) were development diagnostics and are not a proof
  or evidence used above.
- “Minimal separator” is confined to the complete normalized quartic
  fixed-trace-zero fiber and to formal multiplier-trace data by period.  The
  proof does not establish a global cutoff \(P(4)=3\), a theorem for all
  quartic Hénon maps, or global multiplier rigidity.
- The residue machinery, global-residue trace identity, and the underlying
  exceptional quartic family are not claimed as new.  The candidate
  contribution is the Hénon-specific two-term law, its exact finite
  coefficient formula, and the sharp full-fiber quartic separator.
