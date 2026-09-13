# Uniform finite-order obstruction locus for polynomial Hamiltonian gauges

Date: 2026-09-06. Author proof preflight; not independently checked.
Route applicability: NOT_APPLICABLE. No Paper30 project or capacity PASS.

## Claim

Fix integers $d\ge2$ and $D\ge0$. Let $p\in\mathbb C[t]$ have exact
degree $d$, and let $h\in\mathbb C[x,y]$ have ordinary degree at most $D$.
Set $\sigma=(p(x)-y,x)^*$, $\operatorname{ad}_h(f)=\{h,f\}$, and
$$
U_\varepsilon=\exp(\varepsilon\operatorname{ad}_{h-\sigma h})\sigma.
$$
All formal series below are in $\varepsilon$, with global polynomial
coefficients in $x,y$, and automorphisms fix the parameter.

There is an integer $N(d,D)\ge2$, independent of all coefficients of
$p,h$, such that the following are equivalent:

1. $U_\varepsilon=C_\varepsilon\sigma C_\varepsilon^{-1}$ for a formal
   symplectic automorphism $C_\varepsilon=\mathrm{id}+O(\varepsilon)$.
2. The same equation has a symplectic conjugator modulo
   $\varepsilon^{N(d,D)+1}$.

When a conjugator exists, it is unique among those tangent to the identity.
The locus of such pairs $(p,h)$ is Zariski closed in the coefficient space
with the leading coefficient of $p$ inverted. Its equations can be chosen
homogeneous in the coefficients of $h$; in particular each fixed-$p$ fiber
is an algebraic cone containing all constant Hamiltonians.

There is a specialization-compatible, explicit order-by-order recursion
for the conjugator and for polynomial obstruction equations. No value,
effective bound, practical complexity, or recognizable stopping criterion
for $N(d,D)$ is asserted here. A plateau of successive obstruction ideals
does not on its own certify final stabilization.

## Status and dependencies

**PROVABLE AS STATED.** The proof uses the accepted scalar orbit basis and
coefficient criterion of Paper29, the BCH series, elementary polynomial
Hamiltonian calculus, and the Hilbert basis theorem. These general tools
are deducted; in particular Noetherian finite determination is not itself
a new principle.

Dependency map: orbit splitting gives a parameter-regular inverse on the
image of $1-\sigma$; this gives a unique formal recursion and equations;
Noetherianity makes their infinite ideal finitely generated. The absence
of polynomial invariants gives uniqueness, which also makes finite-order
existence equivalent to vanishing of the same canonical equations.

## Proof

### 1. A coefficient-ring orbit splitting

Use the universal coefficient ring
$$
R=\mathbb Q[a_0,\ldots,a_d,a_d^{-1},(b_{uv})_{u+v\le D}],
\qquad p(t)=\sum_{j=0}^d a_jt^j,\quad
h=\sum_{u+v\le D}b_{uv}x^uy^v.
$$
Write $A_R=R[x,y]$. The proof of the accepted orbit basis applies over
$R$: reduction divides only by the unit $a_d$, leading pure powers are
monic after that division, and the degree-lowering reductions and overlap
identity use no field argument. Thus the standard words
$\prod_i X_i^{e_i}$, $0\le e_i<d$, form an $R$-basis, with
$\sigma X_i=X_{i+1}$.

Choose the representative $M_O$ of every nonconstant word orbit to have
least support index zero. Every word is uniquely $\sigma^rM_O$ for some
integer $r$. Define an $R$-linear projection $P$ by
$$
P(1)=1,\qquad P(\sigma^rM_O)=M_O.
$$
Define another $R$-linear map $G$ by $G(1)=0$ and
$$
G(\sigma^rM_O)=
\begin{cases}
-\sum_{j=0}^{r-1}\sigma^jM_O,&r>0,\\
0,&r=0,\\
\sum_{j=r}^{-1}\sigma^jM_O,&r<0.
\end{cases}
$$
Each input is a finite sum, so these maps always produce polynomials.
Termwise telescoping gives
$$
(1-\sigma)G=1-P. \tag{1}
$$
Write $P_+$ for the nonconstant part of $P$. The orbit-coefficient
criterion over $R$ says
$$
f\in(1-\sigma)A_R+R\quad\Longleftrightarrow\quad P_+f=0. \tag{2}
$$
In addition $\ker(1-\sigma)=R$. If $(1-\sigma)f$ is constant, its
normal constant coefficient is zero and (2) shows it must be zero;
therefore $f$ is constant. These assertions follow directly by summing
finite coefficient differences on each infinite nonconstant orbit.

Normal form, $P$, and $G$ commute with every specialization of $R$ to a
characteristic-zero field with $a_d\ne0$. The abstract standard-word
labels and translation rule are independent of the parameter values.

### 2. Formal symplectic logarithms are Hamiltonian

For a formal automorphism $C=1+O(\varepsilon)$, its logarithm is a
continuous derivation. One way to verify the assertion is to write
$C^t=\exp(t\log C)$. At each fixed parameter order its coefficients
are polynomial in $t$, and the algebra-homomorphism identity holds for
every nonnegative integer $t$ by composition. It therefore holds as a
polynomial identity. Differentiating at $t=0$ proves Leibniz's rule for
$\log C$. If $C$ is Poisson, the identical argument applied to bracket
preservation makes its logarithm a Poisson derivation. This works in a
truncated parameter ring too.

A polynomial vector field $V=a\partial_x+b\partial_y$ is Poisson
precisely when $a_x+b_y=0$. Integrating $b$ with respect to $x$ gives a
polynomial $F_0$ with $(F_0)_x=b$. The condition implies
$(-a-(F_0)_y)_x=0$, so the parenthesis is a polynomial in $y$ alone.
Integrate it in $y$ and add the result to $F_0$, obtaining $F$ with
$F_x=b$ and $F_y=-a$. Then $V=\operatorname{ad}_F$ for the stated
Poisson convention. Characteristic zero permits all divisions in these
integrations. The kernel consists precisely of constants.

Applying this separately to every coefficient shows
$$
C_\varepsilon=\exp(\operatorname{ad}_{H_\varepsilon}),\qquad
H_\varepsilon=\sum_{n\ge1}\varepsilon^n h_n,
$$
uniquely if every $h_n$ is required to have zero normal constant
coefficient. There is no analytic convergence assertion.

### 3. Canonical obstruction recursion

Replace the universal $h$ by its zero-normal-constant representative
$h_1$; this does not change $U_\varepsilon$. Let
$\operatorname{BCH}(F,-\sigma F)$ mean the Hamiltonian BCH series,
with Lie bracket given by the Poisson bracket. Its exponential as an
inner derivation equals
$\exp(\operatorname{ad}_F)\exp(-\operatorname{ad}_{\sigma F})$.

Assume $h_1,\ldots,h_{n-1}$ have been constructed for $n\ge2$ and set
$$
E_n=[\varepsilon^n]\operatorname{BCH}
 \left(\sum_{j<n}\varepsilon^jh_j,
       -\sigma\sum_{j<n}\varepsilon^jh_j\right),\qquad
h_n=-G(E_n),\qquad \Theta_n=P_+(E_n). \tag{3}
$$
At fixed order the BCH expression is a finite rational linear combination
of iterated brackets, so all these quantities belong to $A_R$ and are
explicitly computable. Adding $\varepsilon^nh_n$ changes the order-$n$
coefficient only by $(1-\sigma)h_n$: any bracket containing this new
term has order at least $n+1$. By (1), the corrected coefficient is
$P(E_n)$, and its induced derivation vanishes precisely when
$\Theta_n=0$.

Consequently, after any specialization, vanishing of all
$\Theta_2,\ldots,\Theta_m$ constructs a conjugator through order $m$.
Conversely suppose such a conjugator exists. Its first Hamiltonian
coefficient $f_1$ satisfies $(1-\sigma)(f_1-h_1)\in\mathbb C$, hence
$f_1-h_1$ is constant by Step 1 and is zero after normalization. Inductively,
if its first $n-1$ normalized coefficients agree with (3), order $n$
requires $(1-\sigma)f_n+E_n$ to be constant. Applying $P_+$ proves
$\Theta_n=0$; subtracting the equation for $h_n$ proves $f_n=h_n$.
This establishes both directions at each finite order and at all orders.

The same induction proves uniqueness of the full conjugator. It does not
assert uniqueness of Hamiltonians without the constant normalization.

### 4. Finite determination and algebraicity

Expand each $\Theta_n$ in its finitely many representative words $M_O$
and let $I_m\subset R$ be the ideal generated by all these coefficients
for $2\le n\le m$. Put
$$
I_\infty=\bigcup_{m\ge2} I_m.
$$
This is an ideal because the $I_m$ form an ascending chain. The ring $R$
is a localization of a polynomial ring in finitely many variables over
$\mathbb Q$, and is Noetherian. Thus $I_\infty$ has a finite generating
set. Each generator belongs to some $I_m$, so taking the largest of these
finitely many indices gives $I_\infty=I_N$ for an integer depending only
on the universal family, hence only on $d,D$.

For each complex parameter specialization, the vanishing of the first
$N$ stages is now equivalent to vanishing of every stage. Step 3 proves
the asserted finite-order/full-order equivalence. The same coefficient
equations define the closed locus $V(I_\infty)$ in the coefficient space
$a_d\ne0$, without a generic-parameter restriction.

Give every $b_{uv}$ degree one and every $a_j,a_d^{-1}$ degree zero.
The operations $\sigma,P,G$ preserve this grading. Inductively $h_n$ and
$E_n$ are homogeneous of degree $n$ in the $b$ variables: each BCH term
of parameter order $n$ is a bracket product whose input orders add to
$n$. Hence each coefficient of $\Theta_n$ is homogeneous of degree $n$.
This proves the cone assertion. Adding a constant to $h$ does not change
$h-\sigma h$, so constants lie in every fiber. The proof is complete.

## Deductions and open risks

- The general bounded-parameter Noetherian argument is established prior
  technique. For a close dynamical comparison, Mardešić, Novikov,
  Ortiz-Bobadilla and Pontigo-Herrera, *Noetherianity and Length of Melnikov
  Functions* (2026), §2.1, explicitly note this principle for finite-dimensional
  perturbation families. Their main theorem concerns a different, stronger
  orbit-length phenomenon and is not invoked here. Primary full text:
  [DOI 10.1007/s00574-026-00521-7](https://link.springer.com/article/10.1007/s00574-026-00521-7).
- The present proof supplies a specific global polynomial splitting and
  the exact conjugacy quantifiers; it does not claim that BCH obstruction
  theory, algebraic obstruction loci, or the Hilbert basis theorem are new.
- No finite index has been calculated in this universal theorem. The
  separate all-parameter low-degree classification may provide an explicit
  index in its own narrower family; its proof must be checked separately.
- The theorem does not say that an arbitrary perturbation agreeing with
  $U_\varepsilon$ through order $N$ is conjugate. The prescribed entire
  exponential curve, fixed $d,D$, and global polynomial category are essential.
