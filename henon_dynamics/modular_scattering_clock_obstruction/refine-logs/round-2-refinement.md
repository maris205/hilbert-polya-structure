# Round 2 Refinement

## Disposition

**Status after revision:** READY as a sharply scoped Route-A obstruction project.  This is not a claim of a new scattering theory, a new Selberg zeta, or a Hilbert--Pólya operator.

The revision implements every mathematical correction in `round-2-review.md`.  In particular, it separates the open object
\[
P\backslash\Gamma/P
\]
from the closed object of hyperbolic conjugacy classes, strengthens the literal logarithmic counterexample to an arbitrary-function theorem with fixed cusp scale \(\alpha>0\), promotes stable power homogenization to a main result, and states the divisor argument only for a precisely defined zero-free normalization class.

## Frozen Scope and Objects

Let
\[
\Gamma=\operatorname{PSL}_2(\mathbb Z),\qquad
P=\Gamma_\infty=\langle T\rangle,\qquad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

Two different indexing objects are used and are never identified.

1. **Open cusp channels.**  These are oriented nonidentity double cosets in the big Bruhat cell,
   \[
   PgP\in P\backslash\Gamma/P.
   \]
   After choosing the \(\operatorname{SL}_2(\mathbb Z)\) lift with lower-left entry \(c(g)>0\), their arithmetic height is \(2\log c(g)\).  They do not carry a canonical primitive-power operation.

2. **Closed geodesics.**  These are primitive hyperbolic conjugacy classes \([g]\).  A closed total-period clock must be representative independent and must satisfy
   \[
   L([g^n])=nL([g]).
   \]

Powers \(g^n\) are used below only to test a proposed descent of a final-monodromy denominator to a closed total-period clock.  The expression \(Pg^nP\) is not called the \(n\)-fold repetition of the open channel \(PgP\).

The no-go class is exactly
\[
R_F(g)=F(\alpha |c(g)|),
\qquad
F:\alpha\mathbb N_{>0}\to\mathbb R,
\qquad \alpha>0\text{ fixed}.
\]
No regularity, monotonicity, or logarithmic form is assumed for \(F\).

## Changes Required by the Round-2 Review

### 1. Double-coset terminology and normalization

The phrase “parabolic double cosets” has been replaced by “double cosets relative to the parabolic cusp subgroup” or “cusp double cosets in the big Bruhat cell.”  The \(c=0\) identity double coset is kept separate.  For \(c>0\), the exact classification is
\[
PgP\longleftrightarrow (c,\bar d),qquad
c\ge1,\quad \bar d\in(\mathbb Z/c\mathbb Z)^\times.
\]
Consequently, for \(\Re s>1\),
\[
\sum_{PgP\ne P}e^{-s\tau_P(PgP)}
=\sum_{c\ge1}\frac{\varphi(c)}{c^{2s}}
=\frac{\zeta(2s-1)}{\zeta(2s)},
\qquad \tau_P(PgP)=2\log c.
\]
This is only the finite arithmetic factor.  The full standard one-cusp coefficient is
\[
\Phi(s)
=\sqrt\pi\frac{\Gamma(s-\tfrac12)}{\Gamma(s)}
 \frac{\zeta(2s-1)}{\zeta(2s)}
=\frac{\Lambda(2s-1)}{\Lambda(2s)}.
\]

### 2. Conjugacy is a typing diagnostic, not a universal roof no-go

The lower-left entry does not descend to hyperbolic conjugacy classes.  For example,
\[
g=\begin{pmatrix}1&1\\2&3\end{pmatrix},
\qquad
S^{-1}gS=\begin{pmatrix}3&-2\\-1&1\end{pmatrix},
\qquad
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Both matrices have trace \(4\), but their lower-left absolute values are \(2\) and \(1\).

This excludes a total period defined literally by \(F(\alpha|c(g)|)\) unless representative independence is separately repaired.  It does not exclude a local roof whose Birkhoff sum is cyclically invariant, an endpoint extension, or a matrix cocycle.

The positive Gauss-word witness is kept inside \(\operatorname{PSL}_2(\mathbb Z)\).  With
\[
A_a=\begin{pmatrix}0&1\\1&a\end{pmatrix},
\]
let
\[
g=A_1A_1A_1A_2=\begin{pmatrix}2&5\\3&8\end{pmatrix},
\quad
g'=A_1A_2A_1A_1=\begin{pmatrix}3&5\\4&7\end{pmatrix},
\]
and
\[
Q=A_1A_1=\begin{pmatrix}1&1\\1&2\end{pmatrix}\in\operatorname{SL}_2(\mathbb Z).
\]
Then \(g'=Q^{-1}gQ\), while \(|c(g)|=3\) and \(|c(g')|=4\).  The shift is by two digits, so the conjugator has determinant \(+1\).

### 3. Arbitrary denominator-only \(F\): scale-stable square-law rigidity

The main exact-clock theorem now includes an arbitrary fixed \(\alpha>0\).

**Theorem B.**  Let \(F:\alpha\mathbb N_{>0}\to\mathbb R\).  If
\[
F(\alpha|c(g^2)|)=2F(\alpha|c(g)|)
\]
for every hyperbolic \(g\in\operatorname{SL}_2(\mathbb Z)\), then \(F\equiv0\) on \(\alpha\mathbb N_{>0}\).

The proof uses
\[
g_{m,n}=\begin{pmatrix}1&m\\n&1+mn\end{pmatrix},
\qquad m,n\ge1,
\]
for which
\[
c(g_{m,n})=n,qquad
\operatorname{tr}(g_{m,n})=2+mn,qquad
c(g_{m,n}^2)=n(2+mn).
\]
Taking \(n=1\) gives
\[
F(\alpha r)=2F(\alpha),\qquad r\ge3.
\]
Taking \(m=1,n=r\ge3\) compares the same value \(F(\alpha r(r+2))\) in two ways and yields \(F(\alpha)=0\).  Hence \(F(\alpha r)=0\) for all \(r\ge3\).  Finally \((m,n)=(1,2)\) gives
\[
F(8\alpha)=2F(2\alpha),
\]
so \(F(2\alpha)=0\).  Thus all points of \(\alpha\mathbb N_{>0}\) vanish.

Only the square law is used.  The theorem is stronger than failure of \(F(x)=2\log x\), but it remains restricted to a total clock depending only on the final lower-left denominator.

### 4. Chebyshev identity and stable power homogenization

For an \(\operatorname{SL}_2\) lift with trace \(t\), Cayley--Hamilton gives, for \(n\ge1\),
\[
g^n
=U_{n-1}(t/2)g-U_{n-2}(t/2)I,
\]
where \(U_{-1}=0\), \(U_0=1\), and
\[
U_{k+1}(x)=2xU_k(x)-U_{k-1}(x).
\]
Therefore
\[
c(g^n)=c(g)U_{n-1}(t/2).
\]

If \(g\) is hyperbolic, choose its lift with \(t>2\), and put
\[
\lambda=\frac{t+\sqrt{t^2-4}}2>1,
\qquad
\ell(g)=2\log\lambda.
\]
Since
\[
U_{n-1}(t/2)
=\frac{\lambda^n-\lambda^{-n}}{\lambda-\lambda^{-1}},
\]
the scaled denominator height
\[
H_\alpha(g)=2\log(\alpha|c(g)|)
\]
satisfies the exact identity
\[
H_\alpha(g^n)
=n\ell(g)
+2\log\frac{\alpha|c(g)|}{\sqrt{t^2-4}}
+2\log(1-\lambda^{-2n}).
\]
Hence
\[
\lim_{n\to\infty}\frac{H_\alpha(g^n)}n=\ell(g).
\]

This is called the **canonical stable power homogenization of this specific height**.  It is not called the unique repair.  The only additional rigidity claimed is conditional: if a power-homogeneous closed clock \(L\) satisfies
\[
L([g^n])-H_\alpha(g^n)=o(n)
\]
along the powers of a fixed hyperbolic \(g\), then \(L([g])=\ell(g)\).  No assertion is made about homogeneous class functions outside this asymptotic-equivalence class.

### 5. Euler-product corollary

A standard primitive closed-orbit Euler product requires a representative-independent total period and exact repetition.  If its proposed period is
\[
R_F(g)=F(\alpha|c(g)|),
\]
then Theorem B forces \(F\equiv0\).  The resulting local norm \(e^{R_F(g)}=1\) is degenerate.  Therefore there is no nontrivial primitive-hyperbolic Euler product whose total period is a final-denominator-only function and which obeys the standard repetition law.

This corollary does not apply to open-channel Dirichlet series, local cocycles, trace-dependent norms, or groupoid determinants.

### 6. Divisor no-go with an explicit allowed normalization class

Define
\[
\Lambda(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u),
\qquad
\xi(u)=\tfrac12u(u-1)\Lambda(u).
\]
Then
\[
\Phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}
=\frac{s}{s-1}\frac{\xi(2s-1)}{\xi(2s)}.
\]

For each nontrivial zeta zero \(\rho\), \(\Phi\) has a pole at \(s=\rho/2\) and a zero at \(s=(1+\rho)/2\), with the same multiplicity and without cross-cancellation.  Indeed,
\[
\Lambda(\rho-1)=\Lambda(2-\rho)\ne0,
\qquad
\Lambda(1+\rho)\ne0,
\]
because the displayed arguments on the right have real part greater than \(1\).

The allowed normalization class is:

- a cusp coordinate scaling \(y'=r y\), \(r>0\), followed by incoming-term normalization, which gives
  \[
  \Phi_r(s)=r^{2s-1}\Phi(s);
  \]
- multiplication after a nonconstant affine change of variable by an entire zero-free scalar \(h(s)\):
  \[
  h(s)\Phi(as+b),\qquad a\ne0.
  \]

These factors cannot cancel any nontrivial pole.  Thus \(h(s)\Phi(as+b)\) is not entire and cannot equal the entire function \(\xi(s)\) as a global meromorphic identity.

The theorem expressly allows neither zeros in \(h\) nor a meromorphic compensator carrying the missing zeta divisor.  If such factors are allowed, pole cancellation is possible by construction and the no-go no longer applies.

## Strict Scope Exclusions

The revised theorem package does **not** exclude:

- a local denominator-increment cocycle whose periodic Birkhoff sum is not a function of final \(|c(g)|\) alone;
- cyclic symmetrization or a cohomological correction that changes the total observable;
- clocks depending jointly on \(c(g)\), \(\operatorname{tr}(g)\), endpoints, or the full word chronology;
- matrix-valued or projective cocycles and subadditive pressure;
- open scattering groupoids, relative trace formulae, or non-Euler-product Dirichlet series;
- multi-cusp, congruence, or \(S\)-arithmetic systems;
- homogeneous class functions not \(o(n)\)-close to \(H_\alpha(g^n)\) along powers;
- divisor-carrying, non-zero-free compensators;
- a separately derived self-adjoint Hilbert--Pólya candidate.

It also does not assert that the stable power limit is the only conceivable repair.  It proves only the displayed limit for \(H_\alpha\) and the conditional rigidity inside its stated \(o(n)\) asymptotic class.

## Validation Status

The existing computation is a proof audit rather than evidence replacing proof.  It reports:

- exact agreement with \(\varphi(c)\) through \(c=80\);
- 400 exact checks of the \(g_{m,n}\) square formula;
- 48 exact Chebyshev power checks;
- 274 positive Gauss-word audits, with 259 exhibiting cyclic denominator variation and none passing literal denominator square additivity;
- maximum high-precision residual below \(2.7\times10^{-79}\) for the stable defect formula;
- no prime table or Riemann-zero table used in the producer.

These checks are regression certificates.  The proofs in `DERIVATION_PACKAGE.md` establish the universal claims.

## Final Contribution Statement

The defensible contribution is a sharp compatibility obstruction assembled around a fixed source:

1. the totient Dirichlet factor is indexed by oriented open cusp double cosets;
2. no nonzero function of a scaled final denominator satisfies even square repetition on all modular hyperbolic elements;
3. the canonical stable power limit of the literal logarithmic denominator height is exactly the Selberg translation length;
4. the completed scattering quotient retains two shifted nontrivial divisors under the allowed zero-free normalizations.

The external novelty remains modest, while the Route-A termination value is high.  The project should be presented as a scoped obstruction and synthesis theorem, not as a new scattering determinant.
