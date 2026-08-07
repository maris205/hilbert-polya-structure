# Final Proposal: A Final-Denominator-Only Modular Open--Closed Clock Obstruction

## Project Status

**READY for execution as a scoped Route-A obstruction.**

The project proves an exact incompatibility between a final-denominator clock inherited from modular cusp scattering and the axioms of a primitive closed-orbit Euler product.  It also identifies the stable power limit of the literal logarithmic denominator height.  It does not construct a Hilbert--Pólya operator and does not claim that all cusp-derived observables are obstructed.

## Problem Anchor

For the modular group, the standard one-cusp scattering coefficient contains
\[
\frac{\zeta(2s-1)}{\zeta(2s)}.
\]
This finite arithmetic factor comes from an open-channel ledger indexed by double cosets relative to the cusp stabilizer.  By contrast, the Mayer--Selberg determinant is indexed by primitive closed geodesics, hence by primitive hyperbolic conjugacy classes, and uses the translation length.

The project asks one narrow compatibility question:

> Can a total clock depending only on the scaled final lower-left denominator \(\alpha|c(g)|\) be promoted from the modular open-channel arithmetic to a representative-independent, exactly repeating closed-orbit clock?

The answer is no.  Moreover, for the literal logarithmic height, the stable power limit is the ordinary Selberg translation length.

## Source Lock

Fix
\[
\Gamma=\operatorname{PSL}_2(\mathbb Z),
\qquad
P=\Gamma_\infty=\langle T\rangle,
\qquad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

Every calculation uses explicit lifts in \(\operatorname{SL}_2(\mathbb Z)\).  In the open big cell, the sign of a lift is fixed by requiring \(c(g)>0\).  For a hyperbolic element, the sign is fixed by requiring \(t=\operatorname{tr}(g)>2\).

No prime table, list of Riemann zeros, fitted affine scale, or fitted spectral offset enters the theorem or its computational audit.

## Type Separation

### Open object

An oriented cusp channel is a nonidentity double coset
\[
PgP\in P\backslash\Gamma/P.
\]
It is represented in the big Bruhat cell by
\[
g=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad c>0.
\]
The integer \(c\) is double-coset invariant.  The open set \(P\backslash\Gamma/P\) has no canonical single-valued primitive-power operation compatible with group powers.  In particular, the project never interprets \(Pg^nP\) as the \(n\)-fold repetition of \(PgP\).

### Closed object

A closed geodesic is indexed by a hyperbolic conjugacy class \([g]\).  A closed total-period clock is a class function \(L\) satisfying
\[
L([g^n])=nL([g]),\qquad n\ge1.
\]
For primitive-orbit Euler products, this exact repetition law is not optional: it is what identifies the contribution of the \(n\)-fold traversal of one primitive orbit.

The power tests below are therefore conditional tests of a proposed descent from a final monodromy denominator to a closed clock.  They are not claims about repetition inside the open double-coset space.

## Classical Arithmetic Input

### Proposition 1: cusp double-coset classification

The identity cell \(P\) is the unique double coset with \(c=0\).  Every nonidentity double coset has a unique label
\[
(c,\bar d),\qquad
c\ge1,\quad \bar d\in(\mathbb Z/c\mathbb Z)^\times,
\]
after choosing \(c>0\).

Thus the number of oriented algebraic channels at denominator \(c\) is \(\varphi(c)\).  With
\[
\tau_P(PgP)=2\log c,
\]
one obtains, initially for \(\Re s>1\),
\[
\sum_{PgP\ne P}e^{-s\tau_P(PgP)}
=\sum_{c\ge1}\frac{\varphi(c)}{c^{2s}}
=\frac{\zeta(2s-1)}{\zeta(2s)}.
\]

This is the finite arithmetic part of the standard coefficient
\[
\Phi(s)
=\sqrt\pi\frac{\Gamma(s-\tfrac12)}{\Gamma(s)}
 \frac{\zeta(2s-1)}{\zeta(2s)}
=\frac{\Lambda(2s-1)}{\Lambda(2s)}.
\]

The double-coset count is oriented.  Any reversal quotient used to count unoriented geometric scattering geodesics is a separate convention and is not silently identified with \(\varphi(c)\).

## Main Theorem Package

### Theorem 2: non-descent of the lower-left denominator

The function \(|c(g)|\) does not descend from matrix representatives to hyperbolic conjugacy classes.  For example,
\[
g=\begin{pmatrix}1&1\\2&3\end{pmatrix},
\qquad
S^{-1}gS=\begin{pmatrix}3&-2\\-1&1\end{pmatrix},
\qquad
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
The two matrices are conjugate and have trace \(4\), but the absolute lower-left entries are \(2\) and \(1\).

This is a representative-independence obstruction for a total clock \(F(\alpha|c(g)|)\).  It is not a theorem that a local roof function must itself be a class function.

### Theorem 3: arbitrary denominator-only square-repetition no-go

Fix \(\alpha>0\), and let
\[
F:\alpha\mathbb N_{>0}\longrightarrow\mathbb R
\]
be arbitrary. Suppose that for every hyperbolic
\(g\in\operatorname{SL}_2(\mathbb Z)\) whose four entries are strictly
positive,
\[
F(\alpha|c(g^2)|)=2F(\alpha|c(g)|).
\]
Then
\[
F\equiv0\quad\text{on }\alpha\mathbb N_{>0}.
\]

No continuity, monotonicity, measurability, boundedness, or logarithmic ansatz is used.  The result is stable under every fixed positive cusp scale \(\alpha\), and it uses only the square law rather than all repetitions.

The proof uses the entry-positive hyperbolic family
\[
g_{m,n}=\begin{pmatrix}1&m\\n&1+mn\end{pmatrix},
\qquad m,n\ge1,
\]
whose lower-left entries obey
\[
c(g_{m,n})=n,qquad
c(g_{m,n}^2)=n(2+mn).
\]

### Proposition 4: Chebyshev power law

For \(g\in\operatorname{SL}_2(\mathbb Z)\), \(t=\operatorname{tr}(g)\), and \(n\ge1\),
\[
g^n=U_{n-1}(t/2)g-U_{n-2}(t/2)I,
\]
where \(U_{-1}=0\), \(U_0=1\), and \(U_{k+1}(x)=2xU_k(x)-U_{k-1}(x)\).  Therefore
\[
c(g^n)=c(g)U_{n-1}(t/2).
\]

This identity explains why a final lower-left entry is not an exactly additive periodic total: its growth depends on both the initial entry and the trace.

### Theorem 5: stable power homogenization of the logarithmic height

Let \(g\) be hyperbolic, choose the lift with
\[
t=\operatorname{tr}(g)>2,
\]
and define
\[
\lambda(g)=\frac{t+\sqrt{t^2-4}}2,
\qquad
\ell(g)=2\log\lambda(g),
\qquad
H_\alpha(g)=2\log(\alpha|c(g)|).
\]
Then, for every \(n\ge1\),
\[
H_\alpha(g^n)
=n\ell(g)
+2\log\frac{\alpha|c(g)|}{\sqrt{t^2-4}}
+2\log(1-\lambda(g)^{-2n}).
\]
Consequently,
\[
\boxed{
\lim_{n\to\infty}\frac{H_\alpha(g^n)}n
=\ell(g)
}.
\]

Thus the canonical stable power homogenization of this particular open-derived logarithmic height is the classical closed geodesic length used by Selberg and Mayer.

The proposal does **not** call this the unique repair.  It proves only this stable limit and the following conditional rigidity statement: if a power-homogeneous closed clock \(L\) is \(o(n)\)-close to \(H_\alpha(g^n)\) along the powers of a fixed \(g\), then \(L([g])=\ell(g)\).

### Corollary 6: nontrivial denominator-only hyperbolic Euler products do not exist

Assume a proposed primitive-hyperbolic Euler product assigns total period
\[
R_F(g)=F(\alpha|c(g)|)
\]
and requires standard repetition
\[
R_F(g^n)=nR_F(g).
\]
Then Theorem 3 forces \(F\equiv0\).  The corresponding local norm is identically \(1\), so the construction is degenerate rather than a nontrivial dynamical Euler product.

Therefore the modular scattering denominator cannot be used literally as the sole final-monodromy clock of a nontrivial primitive-hyperbolic Euler product.  Retaining the open double-coset ledger gives a Dirichlet/scattering series; taking the displayed stable power limit gives the Selberg translation length.  These facts do not exhaust all enlarged constructions.

## Supporting Divisor Theorem

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

### Theorem 7: zero-free-normalization divisor no-go

Let \(a,b\in\mathbb C\) with \(a\ne0\), and let \(h\) be an entire zero-free function.  Then
\[
h(s)\Phi(as+b)
\]
has nontrivial poles and therefore is not entire.  In particular, it cannot equal the entire function \(\xi(s)\) as a global meromorphic identity.

Indeed, every nontrivial zero \(\rho\) of \(\zeta\) gives a pole of \(\Phi\) at \(\rho/2\) and a zero at \((1+\rho)/2\), with multiplicity preserved and no cross-cancellation.  A cusp rescaling \(y'=r y\), followed by incoming-term normalization, multiplies the coefficient by
\[
r^{2s-1},
\]
which is an entire zero-free exponential and hence belongs to the allowed class.

The theorem is global.  It does not rule out a local identity on a pole-free domain.  It also does not allow a compensator with zeros or a meromorphic zeta divisor; such a compensator can cancel poles precisely because it inserts the missing divisor by hand.

## Claim Boundary

### What is proved

- Exact classification of the oriented cusp double cosets and the source of the totient Dirichlet series.
- Failure of the final lower-left denominator to descend to hyperbolic conjugacy classes.
- Vanishing of every scaled denominator-only function satisfying the universal square-repetition law.
- The exact Chebyshev formula for lower-left entries of powers.
- The stable power limit of \(2\log(\alpha|c(g^n)|)\), equal to the hyperbolic translation length.
- Nonexistence of a nontrivial denominator-only primitive-hyperbolic Euler product with standard repetition.
- Persistence of the shifted scattering poles under affine reparametrization and entire zero-free normalization.

### What is not proved or excluded

- No theorem is claimed for a local denominator-increment cocycle whose periodic sum uses more than the final denominator.
- Cyclic symmetrizations and cohomological corrections are not excluded.
- Clocks depending on trace, endpoints, complete words, or chronological matrix products are not excluded.
- Matrix-valued cocycles, subadditive thermodynamic formalisms, and projective extensions are not excluded.
- Open scattering groupoid determinants or relative trace constructions are not excluded.
- Multi-cusp, congruence, and \(S\)-arithmetic systems are outside scope.
- Homogeneous class functions outside the stated \(o(n)\) asymptotic class are outside scope.
- Divisor-carrying compensators are outside the zero-free-normalization theorem.
- No self-adjoint operator, Hilbert--Pólya realization, RH proof, or new zero-free region is constructed.

## Validation Plan and Existing Certificates

The computational layer audits the proof but does not replace it.

| Claim | Exact or numerical audit | Existing status |
|---|---|---|
| Double-coset multiplicity | Enumerate \((c,\bar d)\) and compare with \(\varphi(c)\) | Exact pass through \(c=80\) |
| Conjugacy/cyclic witness | Integer matrix conjugation | Exact pass |
| Square-family formula | Enumerate \(g_{m,n}\) | 400 exact passes |
| Chebyshev identity | Integer recurrence versus matrix powers | 48 exact passes |
| Gauss-word diagnostic | Preserve word order, cyclic shifts, and squares | 274 words audited; 259 cyclic variations; zero literal square-additivity passes |
| Stable defect formula | High-precision evaluation of the exact identity | Maximum residual below \(2.7\times10^{-79}\) |
| Scattering controls | Functional equation and physical-line modulus | Residuals at approximately \(10^{-81}\) |

The producer uses no Riemann-zero table.  Any future zero illustration must be labeled post-theorem regression material rather than discovery evidence.

## Novelty and Positioning

The double-coset description, scattering coefficient, scattering-geodesic interpretation, Chebyshev identity, translation length, and Mayer--Selberg endpoint are classical.  The defensible project delta is their exact compatibility synthesis:

1. a no-regularity, arbitrary-\(F\), fixed-scale square-law rigidity theorem;
2. the exact stable-closure formula showing where the literal denominator height goes under power homogenization;
3. a formally scoped Euler-product and divisor termination certificate.

The project should be presented as a sharp negative theorem with a positive-control limit, primarily valuable for terminating a false Route-A identification.  Its Route-A value is higher than its standalone external novelty.

## Deliverables

1. A theorem note containing Propositions 1 and 4, Theorems 2, 3, 5, and 7, and Corollary 6.
2. A fully explicit proof appendix matching `DERIVATION_PACKAGE.md`.
3. Frozen exact certificates and a reproducible CPU-only checker.
4. A literature boundary section distinguishing established scattering-geodesic geometry from the new compatibility obstruction.

## Stop/Go Rule

The current literal denominator-only Route-A branch is **stopped** by Theorem 3 and Corollary 6.  A successor branch may proceed only if its proposed clock leaves the proved class—for example by using a genuinely local cocycle, extra endpoint or chronology state, trace dependence, or a non-closed open-channel groupoid—and states that extra structure explicitly.
