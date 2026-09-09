# Proof supplement: the scale-free higher-jet boundary

2026-09-09. Companion to the single frozen question in
[REPORT.md](REPORT.md). Pure proof; no mathematical code was executed.

## Claim and status

**PROVABLE AS STATED.** The scale-free forward/inverse coefficient-norm
observable of any finite return jet equals the joint spectral radius of
its linear part and inverse. An entire native periodic cycle admits
compatible integral charts, in every order at once, if and only if all
return multipliers are units. For the WM6 family this gives exactly the
false-positive locus stated in the report. Two structural lemmas explain
the boundary for spectral and continuous/regular jet enrichments.

This is a complete proof of that specified question, not of the much
broader assertion that *every* intrinsic finite-jet construction fails.

## Assumptions and notation

- Unless a lemma explicitly says otherwise, $K$ is a finite extension of
  $\mathbb Q_p$, with absolute value extending $|p|=p^{-1}$, valuation
  ring $O_K$, maximal ideal $\mathfrak p_K$, and a uniformizer $\pi$.
- $V=K^s$, where $s\ge1$ is any finite dimension. A lattice is a free
  rank-$s$ $O_K$-submodule of $V$ spanning $V$.
- An invertible $N$-jet at the origin is a polynomial tuple
  $g(z)=Mz+\sum_{j=2}^NH_j(z)$ modulo monomials of total degree $N+1$,
  where $M\in\mathrm{GL}_s(K)$ and $H_j$ is homogeneous of degree $j$.
  Its inverse jet exists uniquely by substitution and recursive solution
  using $M^{-1}$. Coefficients mean the coefficients of monomials, not
  derivatives lacking division by factorials. This is the Hasse/Taylor
  convention and is valid in every residue characteristic.
- For a polynomial or finite jet $h$ fixing zero,
  $\|h\|_{\rm coeff}$ is the maximum absolute value of all its
  nonconstant coefficients. Its linear part is included.
- For $M\in\mathrm{GL}_s(K)$ define
  $$
  T(M)=\max_i\{1,|\lambda_i(M)|,|\lambda_i(M)|^{-1}\},       \tag{P1}
  $$
  where eigenvalues are taken in an algebraic closure and counted with
  algebraic multiplicity. Nonsemisimple matrices are allowed.
- Potential all-affine regular good reduction means a finite extension
  and a single affine conjugacy for which forward and inverse polynomial
  maps are integral, both reductions preserve degree, and their geometric
  indeterminacy points at infinity remain disjoint. It is not merely an
  integral formal germ or a collection of local analytic models.

## Strategy and dependency map

1. Lemma 1 proves the exact finite-jet norm formula by a lower spectral
   bound, a controlled Jordan basis, and scalar contraction of nonlinear
   terms. Polynomiality makes the all-orders version simultaneous.
2. Lemma 2 constructs a return-stable lattice by Cayley–Hamilton, transports
   it around a native cycle, and contracts all finitely many transition
   polynomials and their inverses together.
3. Theorem 3 applies only the already proved WM6 parameter classification;
   its phase formulas and the GR5 all-affine theorem remain imported work.
4. Lemma 4 computes finite local-jet spectra using the degree filtration.
   Theorem 5 uses scalar contraction to classify continuous and regular
   observables extending to the linear locus.
5. Section 6 checks the exact limits of each claim, including the failure
   of a universal no-go for unqualified higher-jet information.

## 1. Exact scale-free jet norm

**Lemma 1.** Let $g$ be an invertible $N$-jet over $K$ and let $M=Dg_0$.
Set

$$
J_N(g)=\inf_{L/K\ {\rm finite},\ A\in\mathrm{GL}_s(L)}
 \max\{1,\|A^{-1}gA\|_{\rm coeff},
             \|A^{-1}g^{-1}A\|_{\rm coeff}\},              \tag{P2}
$$

where compositions are truncated at degree $N$. Then

$$
J_N(g)=T(M),                                               \tag{P3}
$$

and a finite extension and a matrix attain the infimum. If $g$ and
$g^{-1}$ are actual polynomial maps fixing zero, there is one such matrix
for which the maximum norm of the entire two polynomials is $T(M)$;
the same matrix then attains (P3) simultaneously for every $N\ge1$.

**Proof.**

Step 1: lower bound. The maximum coefficient norm of a polynomial tuple
dominates the maximum-entry norm of its derivative at zero. For a matrix
$B$ over a valued field, this entry norm is the operator norm for the
maximum vector norm. Extend the field to contain an eigenvalue $\lambda$
and nonzero eigenvector $v$. The inequality

$$
|\lambda|\|v\|=\|Bv\|\le\|B\|\|v\|
$$

gives $|\lambda|\le\|B\|$. Apply this to $A^{-1}MA$ and its inverse.
Every quantity inside the infimum in (P2) is at least $T(M)$.

Step 2: choose a linear basis attaining the joint spectral bound. Over
some finite extension $L/K$, write $M$ in Jordan form. In a block of size
$h$ with eigenvalue $\lambda\ne0$, the Jordan matrix is $\lambda I+U$,
where $U$ has ones immediately above the diagonal and $U^h=0$. Conjugation
by $\operatorname{diag}(1,\epsilon,\ldots,\epsilon^{h-1})$ changes this to

$$
B_\lambda=\lambda I+\epsilon U,
\qquad
B_\lambda^{-1}=\lambda^{-1}
 \sum_{q=0}^{h-1}(-\epsilon U/\lambda)^q.                  \tag{P4}
$$

Choose $0\ne\epsilon\in L$ with
$|\epsilon|\le\min(1,\min_i|\lambda_i|)$, possible by taking a
sufficiently large power of a uniformizer. Then
$\|B_\lambda\|\le\max(1,|\lambda|)\le T(M)$ and
$\|B_\lambda^{-1}\|\le|\lambda|^{-1}\le T(M)$.
Combining all blocks gives a basis $A_0$ with

$$
\max\{1,\|A_0^{-1}MA_0\|,
              \|(A_0^{-1}MA_0)^{-1}\|\}=T(M).             \tag{P5}
$$

The equality follows also from Step 1; a diagonal eigenvalue or its
inverse attains any part of the maximum exceeding one. This argument
includes repeated eigenvalues and arbitrary Jordan block sizes.

Step 3: contract the nonlinear coefficients. Write $h=A_0^{-1}gA_0$.
For any $t\in L^\times$, the scalar change $z=tw$ gives

$$
t^{-1}h(tw)=Bw+\sum_{j=2}^N t^{j-1}H_j'(w),              \tag{P6}
$$

where $B=A_0^{-1}MA_0$. The inverse jet transforms by the identical
rule, with linear part $B^{-1}$. There are finitely many nonlinear
coefficients in these two jets. Taking $t$ sufficiently small makes
every transformed nonlinear coefficient have norm at most $T(M)$.
With $A=tA_0$, equation (P5) supplies the linear contribution and Step 1
supplies the lower bound, proving (P3) with attainment.

If the two germs are polynomial, apply the same argument to all their
nonlinear coefficients, of which there are finitely many even when their
degrees differ. This single choice of $t$ works for both entire
polynomials, and hence for every truncation. $\square$

**Coordinate invariance.** For an affine map $T$ with linear part $B$,
the conjugate $T^{-1}FT$ at $Q=T^{-1}(P)$ has return germ $B^{-1}g_PB$.
In (P2), replacing $A$ by $B^{-1}A$ gives a bijection of admissible
coordinate changes after taking a common finite extension. Therefore
$J_N$ is intrinsically affine-conjugacy invariant. In fact (P3) also
proves its invariance under every invertible formal change of coordinates
at the finite-jet level, because the new derivative is similar to $M$.
The latter statement does not assert affine equivalence of the germs.

**Attainment versus a limiting argument.** Lemma 1 constructs an actual
finite-extension coordinate change. It does not replace a minimum by an
unattained radius-zero germ. The possibility of arbitrarily shrinking
the *nonlinear* terms explains the numerical collapse, while the linear
spectral obstruction survives every nonzero scaling.

## 2. Simultaneously integral charts on a native cycle

**Lemma 2.** Let $F$ be a polynomial automorphism of $\mathbb A^s_K$,
and let $P_0,\ldots,P_{n-1}$ be an actual cycle of least period $n$ in
$\overline K$. The following conditions are equivalent.

1. Every eigenvalue of $M=D(F^n)_{P_0}$ has norm one.
2. There is a finite extension $L/K$ containing the cycle and invertible
   matrices $A_j\in\mathrm{GL}_s(L)$, with $A_n=A_0$, such that
   $$
   G_j(z)=A_{j+1}^{-1}\bigl(F(P_j+A_jz)-P_{j+1}\bigr)
                                                               \tag{P7}
   $$
   and $G_j^{-1}$ both belong to $O_L[z_1,\ldots,z_s]^s$ for every
   $j$ modulo $n$.
3. The same charts can be chosen so that every nonlinear coefficient of
   every $G_j$ and $G_j^{-1}$ lies in $\mathfrak p_L$ and every linear
   part lies in $\mathrm{GL}_s(O_L)$.

In particular a single set of charts works for all jet orders at once.
The affine lattice neighborhoods $P_j+A_jO_L^s$ are sent bijectively
around the cycle. They can also be chosen pairwise disjoint if $n>1$.

**Proof.**

Step 1: a stable return lattice. Take a finite extension $L/K$ containing
$P_0$; since $F$ is defined over $K$, it contains the whole cycle. Put
$V=L^s$ and fix any lattice $\Lambda'\subset V$. Under condition 1, all
coefficients of the characteristic polynomial

$$
\chi_M(X)=X^s+b_{s-1}X^{s-1}+\cdots+b_0
$$

lie in $O_L$, because they are elementary symmetric polynomials in
unit-norm eigenvalues; moreover $b_0\in O_L^\times$. This assertion
does not require the eigenvalues themselves to lie in $L$. Define

$$
\Lambda_0=\Lambda'+M\Lambda'+\cdots+M^{s-1}\Lambda'.       \tag{P8}
$$

It is a finitely generated $O_L$-module containing $\Lambda'$ and
contained in a finite sum of lattices, hence a full lattice: over the
discrete valuation ring $O_L$, every finite torsion-free module is free.
Cayley–Hamilton expresses $M^s$ as an $O_L$-linear combination of
$I,M,\ldots,M^{s-1}$, so $M\Lambda_0\subseteq\Lambda_0$.
Multiplying the same identity by $M^{-1}$ and using $b_0$ a unit gives

$$
M^{-1}=-b_0^{-1}
 (M^{s-1}+b_{s-1}M^{s-2}+\cdots+b_1I).                    \tag{P9}
$$

Thus $M^{-1}\Lambda_0\subseteq\Lambda_0$, and therefore
$M\Lambda_0=\Lambda_0$.

Step 2: transport around the actual one-step clock. Let
$L_j=DF_{P_j}$ and define

$$
\Lambda_j=L_{j-1}\cdots L_0\Lambda_0\quad(1\le j\le n).
                                                               \tag{P10}
$$

The chain rule gives $\Lambda_n=M\Lambda_0=\Lambda_0$.
Choose a basis matrix $A_j$ for $\Lambda_j$, and use $A_n=A_0$.
Then

$$
B_j=A_{j+1}^{-1}L_jA_j\in\mathrm{GL}_s(O_L)               \tag{P11}
$$

for every $j$, including the last step back to $P_0$. These are exactly
the linear parts of (P7). Its inverse is the actual polynomial

$$
G_j^{-1}(z)=A_j^{-1}\bigl(F^{-1}(P_{j+1}+A_{j+1}z)-P_j\bigr),
                                                               \tag{P12}
$$

whose linear part is $B_j^{-1}\in\mathrm{GL}_s(O_L)$.

Step 3: one common shrink. Replace every $A_j$ by $tA_j$ using the
same $t\in L^\times$. Every transition and inverse transition changes
to $t^{-1}G_j(tz)$ or $t^{-1}G_j^{-1}(tz)$. The linear parts are
unchanged; a coefficient of degree $q\ge2$ is multiplied by $t^{q-1}$.
There are finitely many such coefficients across the $2n$ polynomial
maps. A sufficiently small power of $\pi$ makes every one lie in
$\mathfrak p_L$. This proves condition 3, which implies condition 2.
The mutually inverse integral polynomials then map $O_L^s$ bijectively
to $O_L^s$, giving the stated action on neighborhoods. If $n>1$, the
finitely many distinct centers have a positive minimum pairwise
distance in the maximum norm. Shrinking $t$ further puts every
$t\Lambda_j$ inside a ball of radius strictly smaller than that minimum;
the resulting neighborhoods are disjoint by the ultrametric inequality.

Step 4: necessity. Under condition 2, the product
$G_{n-1}\circ\cdots\circ G_0$ and its inverse are integral and fix
zero. Their derivatives are integral, invertible matrices with integral
inverses; they are conjugate to $M$ and $M^{-1}$ by $A_0$. The
eigenvalue estimate from Lemma 1 gives both $|\lambda_i|\le1$ and
$|\lambda_i|^{-1}\le1$. Hence every $|\lambda_i|=1$.
This establishes all equivalences. $\square$

**What compatibility was actually obtained.** The charts retain each
one-step transition of the native orbit, not only its $n$-step return.
They are simultaneously defined over one finite extension for that
cycle. They need not arise from one ambient affine coordinate change,
nor need different cycles use the same lattice scale. Their reductions
in condition 3 are linear; requiring the original polynomial degrees to
survive reduction is a different condition and is not implied.

## 3. Exact WM6 consequence

**Theorem 3.** Fix all parameters of the frozen B4 family,

$$
F(x,y)=(y,y^{p^m}+cy^{p^r}-ax),\quad m>r\ge1,
\quad a\ne0,
$$

over an arbitrary finite extension $E/\mathbb Q_p$. Set
$d=p^m$, $k=p^r$, and

$$
C_*=|p|^{-r(d-k)/(d-1)}.
$$

For every fixed $N\ge1$, the following are equivalent:

- $\mathcal J_N(P)=1$ at every actual periodic point $P$;
- $\mathcal J_N(P)=1$ for every $N\ge1$ and every periodic $P$;
- every native periodic cycle has the compatible all-orders charts of
  Lemma 2;
- $|a|=1$ and $|c|\le C_*$.

The potential-all-affine-regular-good-reduction locus is strictly smaller,
namely $|a|=1$ and $|c|\le1$. Thus the false-positive locus for each
of the three equivalent local tests is exactly

$$
|a|=1,\quad 1<|c|\le C_* .                               \tag{P13}
$$

On the entire unit-Jacobian branch, for every $N\ge1$,

$$
\sup_{P\ {\rm periodic}}
 \frac1{n(P)}\log\mathcal J_N(P)
=\log\max\left\{1,|p|^r
             \max(1,|c|)^{(d-1)/(d-k)}\right\},            \tag{P14}
$$

where $n(P)$ is the actual least period of $P$ and the supremum is over
all actual periodic points. A fixed point attains this supremum.

**Proof.** Lemma 1 makes either jet-norm condition equivalent to unit
return multipliers. Lemma 2 makes the cyclic-chart condition equivalent
to the same statement. The proved WM6 theorem, in its
[proof package, Claim and Sections 1–5](../../../research_c424_c428/continuation_round6/arithmetic_spectral/PROOF_PACKAGE.md),
classifies that condition exactly by $|a|=1$, $|c|\le C_*$ and proves
the potential-good-reduction classification. Those results include every
parameter and endpoint displayed here and are imported, not reproved.

For (P14), $\det D(F^n)_P=a^n$. When $|a|=1$, the two eigenvalue norms
have product one, so

$$
\max_i\{1,|\lambda_i|,|\lambda_i|^{-1}\}
=\max_i|\lambda_i|.
$$

Equation (P14) is then Lemma 1 followed by WM6's proved all-period
spectral-envelope formula and its fixed-point attainment. The factor
$1/n$ measures growth per native step; it does not replace the clock.
This completes the proof. $\square$

**Parameter and quantifier checks.** No step divided by a factorial or
assumed $p$ odd. The stable-lattice proof allows Jordan blocks. For
$|a|\ne1$, WM6's fixed point $0$ already has both multiplier norms
$|a|^{1/2}\ne1$, so every local jet test fails there. For $c=0$ and
$|a|=1$, (P13) is absent and the tests pass in the good region. The
case $a=-1$ and the equality $|c|=C_*$ are retained. Finite base change
preserves absolute values and the threshold. If a displayed real
threshold is not in a particular field's value group, it asserts no
nonexistent parameter in that field; the classification is evaluated at
the actual available values. Equation (P14) is asserted only for
$|a|=1$, exactly as in WM6.

## 4. Spectra of every finite jet action

**Lemma 4 (any characteristic).** Let $K$ now be any field and let $g$
be an invertible formal germ at zero on $K^s$, with derivative $M$.
Let $\mathfrak m=(z_1,\ldots,z_s)$ and
$W_N=\mathfrak m/\mathfrak m^{N+1}$. Pullback by $g$ defines an
invertible linear map $U_N=g^*|_{W_N}$. Over an algebraic closure,

$$
\operatorname{Spec}(U_N)
=\{\lambda_1^{\alpha_1}\cdots\lambda_s^{\alpha_s}:
          \alpha_i\ge0,\ 1\le|\alpha|\le N\},             \tag{P15}
$$

with each monomial index counted once. In particular the characteristic
polynomial depends only on the eigenvalues of $M$, not on any higher
coefficient of $g$.

**Proof.** Since $g(0)=0$, pullback preserves every ideal power
$\mathfrak m^q$. On
$\mathfrak m^q/\mathfrak m^{q+1}$, substituting any term of order two
or higher into a monomial of total degree $q$ raises its total degree
to at least $q+1$. Therefore the induced map is exactly
$\operatorname{Sym}^q(M^*)$. Choose a triangular basis for $M^*$ after
passing to an algebraic closure. The corresponding monomial basis of
its $q$th symmetric power is triangular with diagonal entries
$\lambda_1^{\alpha_1}\cdots\lambda_s^{\alpha_s}$ for $|\alpha|=q$.
Finally, choose a basis adapted to the finite degree filtration of $W_N$.
The characteristic polynomial of a block triangular matrix is the
product of the characteristic polynomials of its diagonal blocks.
Multiplying over $1\le q\le N$ gives (P15). No separability,
diagonalizability, or characteristic-zero argument was used. $\square$

Over a nonarchimedean valued field, write $\rho$ for the maximum
eigenvalue norm. The immediate precise norm consequence is

$$
\max\{1,\rho(U_N),\rho(U_N^{-1})\}^{1/N}=T(M).             \tag{P16}
$$

Indeed every monomial or its inverse has norm at most $T(M)^N$;
a pure monomial of total degree $N$ in an eigenvalue attaining
$T(M)$ or its inverse attains this upper bound whenever $T(M)>1$.
If $T(M)=1$, all monomial norms are one. Thus the degree-normalized
forward/inverse jet spectral norm equals precisely the same quantity
as the optimized full-coefficient norm of Lemma 1.

**A4 interface boundary.** The ambient jet algebra $W_N$ has a fixed
dimension. It is not the dynamical local algebra obtained by quotienting
by the equations $F^n(z)-z$, whose length can encode wild multiplicity.
Lemma 4 rules out recovery from characteristic polynomials of this
ambient jet action alone; it does not rule out retaining the ideal,
nontrivial extensions, an integral lift, or the actual local algebra.

## 5. The extension-to-linear-locus barrier

**Theorem 5.** Let $\mathscr G_N(K)$ be the full space of invertible
$N$-jets at zero on $K^s$, with its coefficient topology when $K$ is a
finite extension of $\mathbb Q_p$.

(a) If $X$ is a Hausdorff topological space and
$\Phi:\mathscr G_N(K)\to X$ is continuous and invariant under every
linear conjugacy, then

$$
\Phi(g)=\Phi(Dg_0).                                      \tag{P17}
$$

(b) Over any characteristic-zero field $K$, every globally regular
algebraic function on $\mathscr G_N$ invariant under linear conjugacy
depends only on the matrix entries of the linear part and is invariant
under matrix similarity. In dimension two the invariant ring is

$$
K[\mathscr G_N]^{\mathrm{GL}_2}
 =K[\operatorname{tr}M,\det M,(\det M)^{-1}].              \tag{P18}
$$

The same ring results if invariance under the full group of invertible
$N$-jet conjugacies is imposed.

**Proof.**

Step 1: topological contraction. Write
$g(z)=Mz+\sum_{j=2}^NH_j(z)$. For $t\ne0$, scalar conjugacy gives

$$
g_t(z)=t^{-1}g(tz)=Mz+\sum_{j=2}^Nt^{j-1}H_j(z).           \tag{P19}
$$

Taking $t=\pi^\ell$ and $\ell\to\infty$ gives $g_t\to M$ in the
coefficient topology, with the derivative invertible throughout.
Conjugacy invariance gives $\Phi(g_t)=\Phi(g)$ for every $\ell$;
continuity gives convergence to $\Phi(M)$. A constant sequence in a
Hausdorff space has only its constant value as a limit. This proves (a).

Step 2: algebraic contraction. The coordinate ring of $\mathscr G_N$
is the polynomial ring in all jet coefficients localized by $\det M$.
The central multiplicative group acting in (P19) gives weight zero to
every linear coefficient and weight $j-1>0$ to every coefficient of
$H_j$, while $\det M$ has weight zero. Any regular function has a
finite decomposition into these nonnegative weights. Invariance under
this central group forces every positive-weight component to vanish.
Thus it is independent of all nonlinear coefficients. The remaining
invariance is exactly conjugation invariance of a matrix in
$\mathrm{GL}_s$.

Step 3: the plane invariant ring. Restrict a regular conjugation
invariant of $\mathrm{GL}_2$ to diagonal matrices
$\operatorname{diag}(u,v)$. The restriction is a symmetric Laurent
polynomial with a denominator a power of $uv$. Multiplying by a large
enough power of $uv$ makes it a symmetric polynomial in $u,v$.
The elementary symmetric-polynomial theorem writes the latter as a
polynomial in $u+v$ and $uv$. Hence the restriction is a member of
$K[u+v,uv,(uv)^{-1}]$. Matrices with two distinct nonzero eigenvalues
are diagonalizable over an algebraic closure and form a Zariski-dense
open subset of $\mathrm{GL}_2$. The proposed function of trace and
determinant agrees with the original invariant there, so it agrees
everywhere as a regular function. This proves (P18); the reverse
inclusion follows directly from invariance of trace and determinant.

Step 4: full jet conjugacy. Its invariant ring is contained in the
ring invariant under the linear subgroup. Conversely, the derivative
of a conjugate germ is conjugate to $M$ by the derivative of the
coordinate change. Trace, determinant, and inverse determinant remain
invariant under every invertible jet conjugacy. The rings coincide.
$\square$

## 6. Corrections, exclusions, and proof audit

The following qualifications are part of the theorem, not post hoc
weakenings of a universal reconstruction claim.

1. **No fixed or canonical volume.** Formula (P2) optimizes over all
   $\mathrm{GL}_s$, including scalars. Under a prescribed determinant,
   fixed lattice volume, or global leading-term calibration, Step 3 of
   Lemma 1 may be illegal. No formula for such a different norm is
   asserted.
2. **No degree-preserving local conclusion.** In Lemma 2 the reduced
   polynomials can be linear. GR5's local all-affine proof uses retained
   highest homogeneous terms and separated infinity points to force the
   unique common disk scale. Those hypotheses are exactly what the
   independent shrinking charts do not retain.
3. **No uniform neighborhood over all cycles.** One finite cycle uses
   one finite extension and one common contraction. The theorem does not
   produce a single extension, radius, or ambient affine chart valid for
   every periodic point of $F$.
4. **No claim that raw jet conjugacy is linear data.** For $N\ge2$, the
   identity and the shear $g(x,y)=(x,y+x^2)$ have the same derivative but
   are not conjugate as $N$-jets: the identity is fixed by every
   conjugacy, whereas the shear jet is not the identity. Scalar
   conjugates of the shear converge to the identity. Therefore a raw
   conjugacy-class discriminator can distinguish them, but no
   continuous Hausdorff-valued one extending to the identity can do so.
5. **Regular is not rational on a smaller open set.** For a one-variable
   jet $z+uz^2+vz^3$ with $u\ne0$, the ratio $v/u^2$ survives scalar
   conjugacy. It has no continuous extension to the linear jet along
   all paths and is not a globally regular function on the full jet
   space. Consequently it does not contradict Theorem 5. Analogous
   singular normalizations must be analyzed separately.
6. **Norm spectrum is not exact spectrum.** Theorem 5 only proves that
   regular/continuous higher-jet invariants add no information beyond
   the derivative. It does not say the exact derivatives are constant
   in (P13). Cantat–Dujardin's exact trace-spectrum results are separate
   primary-source input, not contradicted by WM6 or by this proof.
7. **No wild local-length theorem.** Lemma 4 preserves algebraic
   multiplicities of eigenvalues in the fixed ambient jet space, but
   does not determine lengths of dynamical fixed-point schemes.

The original scale-free/cycle-local frozen question survives unchanged
and is completely answered. No remaining internal proof step is asserted
without an argument. Independent current-team verification and a
coordinator decision on research substance remain separate gates; this
author proof is neither peer review nor manuscript admission.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
