# Proof Package

<!-- HENON_PROOF_SCHEMA_ID: integral-area-henon-proof-v2 -->

## Claim

<!-- HENON_PROOF_SECTION_ID: THEOREM_A -->
### Theorem A (integral area-preserving Hénon obstruction)

Let $K$ be a number field and let $a\in\mathcal O_K$.  Define

$$
H_a(X,Y)=(X^2-a-Y,X).
$$

If $P=(x,y)\in\mathbb A^2(\mathbb C)$ is a finite periodic point of
$H_a$, then $x$ and $y$ are algebraic integers.  For every $n\ge1$ such that
$H_a^n(P)=P$, both eigenvalues of $D_PH_a^n$ are algebraic units.  In
particular, for either eigenvalue $\lambda$,

$$
|\lambda|\in\mathbb Q \quad\Longrightarrow\quad |\lambda|=1.
$$

As a special case, if $\lambda\in\mathbb Q$, then $\lambda=+1$ or $-1$.

<!-- HENON_PROOF_SECTION_ID: COROLLARY_B -->
### Corollary B (frozen all-period prime-modulus obstruction)

Let $u$ be the unique real root of
$u^3-2u^2+2u-2=0$ and put

$$
H_u(X,Y)=(X^2-u-Y,X).
$$

For every multiplier $\lambda$ of every finite periodic orbit of $H_u$,

$$
|\lambda|\in\mathbb Q \quad\Longrightarrow\quad |\lambda|=1.
$$

Consequently no positive rational prime, or any rational integer greater
than one, is a multiplier modulus.  The multiplier itself need not be
rational.

<!-- HENON_PROOF_SECTION_ID: THEOREM_C -->
### Theorem C ($S$-integral rational-modulus prime-support certificate)

Let $K$ be a number field.  Let $S$ be a finite set of places containing the
archimedean places, and write $R=\mathcal O_{K,S}$.  For $1\le i\le m$, let
$p_i\in R[X]$ be monic of degree $d_i\ge2$, and set

$$
H_i(X,Y)=(p_i(X)-Y,X),
\qquad F=H_m\circ\cdots\circ H_1.
$$

Every finite periodic point of $F$ has coordinates integral over $R$.  For
every $n\ge1$ and every $P$ with $F^n(P)=P$, the two eigenvalues of
$D_PF^n$ are units in the integral closure of $R$.  Fix the given embedding
into $\mathbb C$.  If an eigenvalue $\lambda$ has
$|\lambda|=q\in\mathbb Q_{>0}$, then

$$
q\in\mathbb Z[S_{\mathbb Q}^{-1}]^\times_{>0},
$$

where $S_{\mathbb Q}$ is the set of rational primes lying below the finite
places in $S$.  Equivalently,

$$
q=\prod_{p\in S_{\mathbb Q}}p^{e_p}
\quad\text{for integers }e_p.
$$

Consequently an exact rational-prime multiplier modulus $|\lambda|=p$
forces $p\in S_{\mathbb Q}$, without requiring $\lambda\in\mathbb Q$.
If $\lambda$ itself lies in $\mathbb Q$, then the same support conclusion
holds for $\lambda$.

## Status

`PROVABLE AS STATED`

`INDEPENDENTLY AUDITED AFTER EXPLICIT GALOIS-CLOSURE REPAIR`

The frozen theorem and the finite-composition $S$-integral strengthening are
provable.  The statement deliberately includes **exact rational** complex
absolute values.  It does not classify irrational absolute values, general
spectral radii, singular values, or Lyapunov exponents.  In dimension two
with determinant one, an exactly rational spectral radius is covered as a
direct corollary.

## Assumptions

- All periodic points are finite affine points in $\mathbb A^2(\mathbb C)$.
  Step 2 proves that their coordinates are algebraic over $K$; this is not
  assumed.
- In Theorem C, every $p_i$ is monic and has degree at least two.
- Every factor has coefficient $-1$ on the memory coordinate, so
  $\det DH_i=1$.  A generalized factor with another Jacobian coefficient
  requires that coefficient to be an $S$-unit and a correspondingly modified
  determinant statement.
- Absolute value is taken in the fixed embedding into $\mathbb C$.  The
  rational-modulus claim does not assume that the eigenvalue itself is real
  or rational.
- $S$ contains the archimedean places.  Integrality and units always refer to
  finite places outside $S$.

## Notation

- $\overline R$ is the integral closure of $R=\mathcal O_{K,S}$ in
  $\overline K$.
- A point has coordinates integral over $R$ if its coordinates belong to
  $\overline R$.
- For a finite non-archimedean place $w$ of a finite extension of $K$,
  $|\cdot|_w$ is normalized in any fixed way; only comparisons with $1$ are
  used.
- A periodic multiplier is an eigenvalue of the return derivative.
- $S_{\mathbb Q}$ is the set of rational primes below finite places of $S$.
- $\mathbb Z[S_{\mathbb Q}^{-1}]^\times_{>0}$ denotes the positive elements
  of the rational $S_{\mathbb Q}$-unit group.

## Proof Strategy

<!-- HENON_PROOF_SECTION_ID: PROOF_STRATEGY -->

First prove algebraicity of a periodic point from the fixed-point equations.
Then fix any non-archimedean place outside $S$ and expand the orbit through
the individual Hénon factors.  The largest coordinate modulus on this finite
cyclic substep orbit cannot exceed one: monicity makes the polynomial term at
a maximal coordinate strictly larger than both neighboring coordinates,
contradicting the recurrence.  This proves $S$-integrality.

The derivative matrices therefore have entries in $\overline R$ and
determinant one.  Their product lies in $\mathrm{SL}_2(\overline R)$, so its
characteristic polynomial is monic with constant term one.  Each eigenvalue
and its reciprocal are integral over $R$, hence each is a unit in the
integral closure.

To control modulus, place all relevant algebraic numbers in a finite Galois
extension of $\mathbb Q$ and use the set of places above the rational bad
primes $S_{\mathbb Q}$.  This set is conjugation-stable, so both $\lambda$
and $\overline\lambda$ are units away from it.  Thus an exact rational value
$|\lambda|=q$ satisfies that $q^2=\lambda\overline\lambda$ is a rational
$S_{\mathbb Q}$-unit, forcing the same prime-support restriction on $q$.

## Dependency Map

<!-- HENON_PROOF_SECTION_ID: DEPENDENCY_MAP -->

1. Algebraicity depends on homogenizing the cyclic recurrence system: its
   projective zero set has no point on the hyperplane at infinity, and hence
   is zero-dimensional.
2. Coordinate integrality depends on the cyclic scalar recurrence through
   factor substeps and the ultrametric maximum principle.
3. Multiplier integrality depends on polynomial derivatives having
   $S$-integral values at $S$-integral coordinates.
4. Reciprocal integrality depends on determinant one.
5. The rational-modulus conclusion uses complex conjugation in a Galois
   closure and the valuation characterization of rational $S$-units.
6. Corollary B uses that $u$ is an algebraic integer and takes $S$ to contain
   no finite place.

## Proof

<!-- HENON_PROOF_SECTION_ID: PROOF -->

<!-- HENON_PROOF_SECTION_ID: STEP_1_SYMPLECTIC -->
### Step 1: the maps are polynomial symplectic automorphisms

For each factor,

$$
H_i^{-1}(X,Y)=(Y,p_i(Y)-X),
$$

<!-- HENON_PROOF_EQUATION_ID: POLYNOMIAL_INVERSE -->

so $H_i$ and $F$ are polynomial automorphisms.  Moreover

$$
DH_i(X,Y)=
\begin{pmatrix}p_i'(X)&-1\\1&0\end{pmatrix},
\qquad
\det DH_i(X,Y)=1.
$$

<!-- HENON_PROOF_EQUATION_ID: DERIVATIVE_DETERMINANT_ONE -->

In dimension two, determinant one is equivalent to preservation of the
standard algebraic symplectic form $dX\wedge dY$.  Thus every factor and
$F$ are globally symplectic polynomial automorphisms.

<!-- HENON_PROOF_SECTION_ID: STEP_2_ALGEBRAICITY -->
### Step 2: every complex periodic orbit is algebraic

Let $P\in\mathbb A^2(\mathbb C)$ satisfy $F^n(P)=P$.  Expand its orbit
through the $m$ individual factors during each of the $n$ returns.  Its
successive first coordinates form a cyclic sequence

$$
(z_j)_{j\in\mathbb Z/N\mathbb Z},
\qquad N=mn,
$$

satisfying

$$
p_{i_j}(z_j)-z_{j+1}-z_{j-1}=0,
$$

<!-- HENON_PROOF_EQUATION_ID: CYCLIC_RECURRENCE -->

where the factor index $i_j$ is periodic with period $m$.

Introduce one homogenizing coordinate $Z$.  If $d_{i_j}=\deg p_{i_j}$ and
$P_{i_j}(Z_j,Z)$ is the degree-$d_{i_j}$ homogenization of $p_{i_j}$, the
projective closure of this cyclic system in $\mathbb P^N$ is contained in
the common zero set of

$$
P_{i_j}(Z_j,Z)
-Z_{j+1}Z^{d_{i_j}-1}
-Z_{j-1}Z^{d_{i_j}-1}=0
\quad(j\bmod N).
$$

On the hyperplane $Z=0$, monicity and $d_{i_j}\ge2$ reduce these equations
to

$$
Z_j^{d_{i_j}}=0
\quad\text{for every }j.
$$

<!-- HENON_PROOF_EQUATION_ID: NO_INFINITY_EQUATIONS -->

They force all homogeneous coordinates to vanish, which is impossible in
projective space.  Hence the projective zero set does not meet $Z=0$.

It follows that this projective zero set is zero-dimensional.  Indeed, every
positive-dimensional projective subvariety of $\mathbb P^N$ meets every
hyperplane (equivalently, the hyperplane class is ample); such a component
would have to meet $Z=0$.  Thus the affine cyclic system has finitely many
complex solutions.  Since its equations have coefficients in $K$, the
coordinates of every solution are algebraic over $K$.

Choose a finite extension $L/K$ containing the coordinates of the selected
orbit and every coefficient.  This supplies the number field for the
place-by-place argument below.

<!-- HENON_PROOF_SECTION_ID: STEP_3_MAXIMUM -->
### Step 3: the non-archimedean maximum lemma

Fix a finite extension $L/K$ containing all coordinates of a periodic orbit
and all coefficients, and fix a finite place $w$ of $L$ above a place not in
$S$.  Expand one $F$-orbit through its individual factor substeps.  This
gives a finite cyclic sequence $(z_j)_{j\in\mathbb Z/N\mathbb Z}$ satisfying

$$
z_{j+1}+z_{j-1}=p_{i_j}(z_j),
$$

where $i_j$ is periodic and each $p_{i_j}$ is monic with all coefficients of
$w$-absolute value at most one.

Assume for contradiction that

$$
M=\max_j|z_j|_w>1.
$$

<!-- HENON_PROOF_EQUATION_ID: CYCLIC_MAXIMUM_ASSUMPTION -->

Choose $j$ with $|z_j|_w=M$.  Since $p_{i_j}$ is monic of degree
$d_{i_j}\ge2$ and its other coefficients have absolute value at most one,
the ultrametric inequality gives

$$
|p_{i_j}(z_j)|_w=|z_j|_w^{d_{i_j}}=M^{d_{i_j}}>M.
$$

<!-- HENON_PROOF_EQUATION_ID: STRICT_NONARCHIMEDEAN_DOMINATION -->

On the other hand, the recurrence and the choice of $M$ give

$$
|p_{i_j}(z_j)|_w
=|z_{j+1}+z_{j-1}|_w
\le\max\{|z_{j+1}|_w,|z_{j-1}|_w\}
\le M,
$$

a contradiction.  Hence $|z_j|_w\le1$ for every $j$ and every finite
$w$ outside $S$.  Since the coordinates are algebraic, the valuation
criterion for integrality shows that every periodic coordinate belongs to
$\overline R$.

When $S$ has no finite places, $R=\mathcal O_K$ and the coordinates are
ordinary algebraic integers.  This proves the coordinate assertions in
Theorems A and C.

<!-- HENON_PROOF_SECTION_ID: STEP_4_MONODROMY -->
### Step 4: periodic monodromies are integral special-linear matrices

At every factor substep, $p_i'(z_j)\in\overline R$.  Therefore

$$
DH_i(z_j,z_{j-1})
=\begin{pmatrix}p_i'(z_j)&-1\\1&0\end{pmatrix}
\in\mathrm{SL}_2(\overline R).
$$

The return monodromy $M_P=D_PF^n$ is a product of these matrices, so

$$
M_P\in\mathrm{SL}_2(\overline R).
$$

<!-- HENON_PROOF_EQUATION_ID: INTEGRAL_SL2_MONODROMY -->

Its characteristic polynomial is

$$
\chi_P(T)=T^2-\operatorname{tr}(M_P)T+1
\in\overline R[T].
$$

<!-- HENON_PROOF_EQUATION_ID: UNIT_CHARACTERISTIC_POLYNOMIAL -->

If $\lambda$ is one eigenvalue, then $\lambda$ is integral over
$\overline R$ because it is a root of this monic polynomial.  Since
$\overline R$ is integral over $R$, transitivity of integrality shows that
$\lambda$ is integral over $R$, hence belongs to $\overline R$ by its
definition.  The other eigenvalue is $\lambda^{-1}$ and obeys the same
argument.  Thus $\lambda,\lambda^{-1}\in\overline R$, and $\lambda$ is a
unit of $\overline R$.

<!-- HENON_PROOF_SECTION_ID: STEP_5_RATIONAL_MODULUS -->
### Step 5: rational moduli have only the declared prime support

Fix the embedding $\overline K\hookrightarrow\mathbb C$ used to state the
absolute value.  Choose a finite Galois extension $M/\mathbb Q$ inside
$\mathbb C$ containing $K$, the periodic orbit, and $\lambda$.  Let $T$ be
the set of finite places of $M$ lying above the rational primes in
$S_{\mathbb Q}$.

Step 4 implies that $\lambda$ and $\lambda^{-1}$ are integral at every place
of $M$ not in $T$.  Indeed, such a place lies above a rational prime not in
$S_{\mathbb Q}$, so its restriction to $K$ is outside $S$.  Therefore
$\lambda\in\mathcal O_{M,T}^{\times}$.

The set $T$ is stable under $\operatorname{Gal}(M/\mathbb Q)$ because it was
defined using underlying rational primes, not selected places of $K$.
Complex conjugation on $M\subset\mathbb C$ is an element of this Galois
group.  It follows that $\overline\lambda$ is also a $T$-unit, and hence

$$
\lambda\overline\lambda=|\lambda|^2
$$

<!-- HENON_PROOF_EQUATION_ID: MODULUS_CONJUGATION_IDENTITY -->

is a $T$-unit.

This does not assert that $\overline\lambda$ is the reciprocal eigenvalue,
nor is that assertion needed.  It uses only that complex conjugation is a
field automorphism of $M$ and therefore preserves its $T$-unit group.

Now suppose $|\lambda|=q\in\mathbb Q_{>0}$.  Then $q^2$ is a rational
$T$-unit.  For a place $W$ of $M$ above a rational prime
$\ell\notin S_{\mathbb Q}$, the equality
$v_W(q^2)=e(W/\ell)v_\ell(q^2)=0$ therefore gives

$$
0=v_\ell(q^2)=2v_\ell(q),
$$

so $v_\ell(q)=0$.  Consequently

$$
q\in\mathbb Z[S_{\mathbb Q}^{-1}]^\times_{>0}
=\left\{\prod_{p\in S_{\mathbb Q}}p^{e_p}:e_p\in\mathbb Z\right\}.
$$

<!-- HENON_PROOF_EQUATION_ID: RATIONAL_BAD_PRIME_SUPPORT -->

This proves Theorem C.  If $S$ has no finite places, a positive rational
unit is $1$, proving the rational-modulus assertion in Theorem A.  If in
addition $\lambda\in\mathbb Q$, then $|\lambda|=1$ gives
$\lambda=\pm1$.

<!-- HENON_PROOF_SECTION_ID: STEP_6_FROZEN_SPECIALIZATION -->
### Step 6: specialize to the frozen parameter

The polynomial $P(U)=U^3-2U^2+2U-2$ is monic, so its selected root $u$ is an
algebraic integer.  Theorem A applies to $a=u$.  Every multiplier $\lambda$
of a periodic orbit of $H_u$ with rational absolute value satisfies
$|\lambda|=1$.  Hence no positive rational prime is the modulus of any
multiplier.  This proves Corollary B.  In particular, every rational
multiplier equals $+1$ or $-1$.

<!-- HENON_PROOF_SECTION_ID: STEP_7_SHARPNESS -->
### Step 7: verify sharpness

Take $a=-15/16$ and $r=5/4$.  Since

$$
r^2-a-r=r^2+\frac{15}{16}-r=r,
$$

the point $(r,r)$ is fixed by $H_a$.  More directly, the fixed-point equation
is $a=r^2-2r=-15/16$.  At this point,

$$
DH_a(r,r)=\begin{pmatrix}5/2&-1\\1&0\end{pmatrix},
$$

whose characteristic polynomial is

$$
T^2-\frac52T+1=(T-2)(T-1/2).
$$

<!-- HENON_PROOF_EQUATION_ID: SHARP_CONTROL_MULTIPLIERS -->

Thus an area-preserving polynomial Hénon map can have exact multipliers
$2$ and $1/2$ when the coefficient has denominator supported at $2$.  This
is compatible with Theorem C for $S_{\mathbb Q}=\{2\}$ and proves the
prime-support conclusion is sharp at the level of allowed primes. $\square$

## Corrections or Missing Assumptions

- Monicity and degree at least two are used in the strict maximum argument.
  With a nonunit leading coefficient, its valuation must be included in the
  bad set.
- Determinant one is used to make the reciprocal multiplier integral.  For a
  generalized Hénon factor with determinant an $S$-unit, an analogous
  $S$-unit conclusion can be recovered after tracking that determinant, but
  it is not part of the frozen theorem.
- Algebraicity precedes valuation integrality and is supplied by the
  projective cyclic-system argument in Step 2.
- For a general $(K,S)$, complex conjugation need not preserve $K$ or the
  originally selected places of $S$.  Step 5 therefore passes to a Galois
  closure and enlarges to all places above $S_{\mathbb Q}$.  This enlargement
  changes no rational-prime support and is essential to the clean argument.
- The modulus argument is not an application of Kronecker's theorem and does
  not require every Galois conjugate of $\lambda$ to lie on the unit circle.
  It uses only the chosen complex conjugate and the exact identity
  $|\lambda|^2=\lambda\overline\lambda$.
- The argument proves integrality of all complex periodic coordinates, not
  that they lie in the base field $K$.
- A spectral radius can be an irrational algebraic number larger than one.
  It is not constrained to $1$.  What is excluded in the integral case is
  an **exactly rational** spectral radius larger than one.
- In the $S$-integral setting the conclusion controls support, not
  rationality of $\lambda$: for example $2i$ is an abstract
  $\{2\}$-unit of modulus $2$.  This is only an arithmetic boundary example,
  not a claim that $2i$ is realized by the frozen Hénon map.

## Open Risks

- The non-archimedean maximum argument is a standard good-reduction
  filtration idea in arithmetic Hénon dynamics.  The finite-composition
  packaging and prime-clock consequence are best positioned as an exact
  certificate, not as priority for a deep new theorem.
- The projective Step 2 uses monicity and degree at least two twice: to remove
  every point at infinity and to infer zero-dimensionality.  Any extension
  to nonmonic factors must redo this argument with unit-leading-coefficient
  bookkeeping.
- The theorem does not decide whether $+1$ or $-1$ actually occurs for the
  frozen map.
- No finite-period computation can extend the exact rational-modulus theorem
  to irrational or approximate modulus claims.
