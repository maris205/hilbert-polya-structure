# Round 1 Refinement

## Problem Anchor

- **Bottom-line problem:** determine whether the noncompact modular surface supplies a source-faithful dynamical route from cusp returns to the Riemann scattering divisor and a Hilbert--Pólya structure, without treating a classical zeta ratio as a new construction.
- **Must-solve bottleneck:** the same intrinsic clock must support primitive-cycle repetition, a dynamical determinant, and the claimed Riemann arithmetic.  It is not enough for these properties to occur in different parts of the modular theory.
- **Non-goals:** no proof of RH; no direct zero fitting; no claim that Gauss/Mayer, Selberg zeta, Eisenstein scattering, or cuspidal acceleration is new; no replacement of chronological products by an averaged transition matrix.
- **Constraints:** use the fixed source object \(\Gamma=\mathrm{PSL}_2(\mathbb Z)\), its cusp stabilizer \(\Gamma_\infty\), exact matrix chronology, and standard normalizations.  Riemann-zero data are forbidden in candidate selection and may be used only for a post-theorem divisor illustration.
- **Success condition:** prove a normalization-stable theorem deciding whether the cusp-denominator weight that produces \(\zeta(2s-1)/\zeta(2s)\) can be the periodic roof of the same return dynamics; provide exact witnesses, independent code checks, and a scoped Route-A ruling.

## Anchor Check

- **Original bottleneck:** a Riemann factor in scattering is useful to Route A only if its source-derived clock also has the homogeneous primitive/repetition structure needed by a closed-orbit determinant.
- **Why the revised method still addresses it:** the revision replaces a single logarithmic counterexample by a rigidity theorem for every denominator-only clock, and identifies the unique stable closure.
- **Reviewer suggestions rejected as drift:** constructing a two-cusp or \(S\)-arithmetic system now would change the question before the modular positive control has been closed.  Those systems remain next-round candidates.

## Simplicity Check

- **Dominant contribution after revision:** exact non-homogenization plus stable-closure rigidity for the modular cusp denominator.
- **Components removed or demoted:** the statement that \(Pg^nP\) is an open-channel repetition is removed; non-conjugacy alone is demoted to a typing diagnostic; numerical zero illustrations are optional and cannot support the proof.
- **Unnecessary complexity rejected:** no multi-cusp coding, finite-memory twist, learned operator, or new nuclear space is added.
- **Why this is the smallest adequate route:** four explicit matrix families and Cayley--Hamilton decide the exact clock question globally.

## Changes Made

### 1. Corrected the open-versus-closed typing

- **Reviewer said:** a parabolic double coset \(PgP\) is an open cusp-to-cusp channel and has no canonical primitive-power monoid; \(Pg^nP\) must not be called its \(n\)-fold repetition.
- **Action:** the proposal now uses powers only as a falsification test for a proposed descent to hyperbolic closed conjugacy classes.
- **Impact:** the theorem no longer claims that open scattering dynamics is inconsistent.  It rules out only its literal denominator as an exact closed-cycle clock.

### 2. Strengthened one logarithmic obstruction to a denominator-only rigidity theorem

- **Reviewer said:** failure of \(2\log c\) alone is too narrow.
- **Action:** prove that any function \(F:\mathbb N\to\mathbb R\) satisfying
  \(F(|c(g^n)|)=nF(|c(g)|)\) for every hyperbolic \(g\in\mathrm{SL}_2(\mathbb Z)\) and \(n\ge1\) must vanish identically.
- **Impact:** no nontrivial exact closed clock can be built from the denominator alone, independently of the choice \(F(q)=2\log q\).

### 3. Added the stable-closure theorem

- **Reviewer said:** the denominator clock and closed length are asymptotically related, not unrelated.
- **Action:** derive the exact defect formula and prove its homogeneous limit is the hyperbolic translation length.
- **Impact:** the obstruction becomes a sharp dichotomy: retain the open clock, or homogenize and return uniquely to Selberg length.

### 4. Tightened prior-art and orientation language

- **Reviewer said:** Guillemin, Ji--Zworski, and Pujahari--Satpathy already identify scattering geodesics and denominator sojourn times; unoriented geometric scattering geodesics are not counted by the raw totient in every convention.
- **Action:** the totient series is explicitly an oriented parabolic-double-coset/Eisenstein coefficient ledger.  Geometric reversal quotienting is kept separate and all sojourn-time novelty claims are removed.
- **Impact:** novelty is limited to the exact Route-A closure rigidity and its consequence for a closed Euler product.

## Revised Proposal

# Research Proposal: Denominator-Clock Non-Homogenization and Stable Closure

## Problem Anchor

- **Bottom-line problem:** determine whether the noncompact modular surface supplies a source-faithful dynamical route from cusp returns to the Riemann scattering divisor and a Hilbert--Pólya structure, without treating a classical zeta ratio as a new construction.
- **Must-solve bottleneck:** the same intrinsic clock must support primitive-cycle repetition, a dynamical determinant, and the claimed Riemann arithmetic.  It is not enough for these properties to occur in different parts of the modular theory.
- **Non-goals:** no proof of RH; no direct zero fitting; no claim that Gauss/Mayer, Selberg zeta, Eisenstein scattering, or cuspidal acceleration is new; no replacement of chronological products by an averaged transition matrix.
- **Constraints:** use the fixed source object \(\Gamma=\mathrm{PSL}_2(\mathbb Z)\), its cusp stabilizer \(\Gamma_\infty\), exact matrix chronology, and standard normalizations.  Riemann-zero data are forbidden in candidate selection and may be used only for a post-theorem divisor illustration.
- **Success condition:** prove a normalization-stable theorem deciding whether the cusp-denominator weight that produces \(\zeta(2s-1)/\zeta(2s)\) can be the periodic roof of the same return dynamics; provide exact witnesses, independent code checks, and a scoped Route-A ruling.

## Technical Gap

Let \(P=\Gamma_\infty=\langle T\rangle\).  For an oriented parabolic double coset represented by
\[
g=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad c>0,
\]
the integer \(c\) is well defined, while \(d\bmod c\) ranges over the units.  The resulting coefficient ledger is
\[
\sum_{PgP}e^{-s\tau_P(PgP)}
=\sum_{c\ge1}\varphi(c)c^{-2s}
=\frac{\zeta(2s-1)}{\zeta(2s)},
\qquad \tau_P(PgP)=2\log c.
\]
After a horocycle cutoff \(T_0\), the geometric sojourn time is \(2\log(cT_0)\); this is established scattering geometry, not a new result.

Closed geodesics instead correspond to primitive hyperbolic conjugacy classes and require a clock \(L\) with
\[
L(g^n)=nL(g).
\]
The gap is to decide whether any nontrivial function of the same denominator can satisfy this closed-cycle axiom, and, if exact equality fails, what canonical homogeneous limit remains.

## Method Thesis

The oriented cusp denominator has genuine arithmetic and scattering meaning, but no nonzero denominator-only function is an exact homogeneous closed-orbit clock on all modular hyperbolic elements.  Its stable power homogenization exists and equals the Selberg translation length.  Consequently, exact closure fails, while asymptotic closure returns to the already-known Mayer--Selberg system.

## Contribution Focus

- **Dominant theorem:** denominator-only repetition rigidity plus stable closure.
- **Supporting corollary:** no Euler product can simultaneously use primitive hyperbolic conjugacy classes, local norm \(c(g)^2\), and standard repetition, unless the denominator clock is discarded or homogenized to Selberg length.
- **Secondary analytic obstruction:** the scattering coefficient is a meromorphic quotient with two shifted zeta divisors and cannot be changed into one entire \(\xi\) by a zero-free cusp normalization.
- **Non-contributions:** scattering geodesics, sojourn times, the totient Dirichlet identity, Selberg/Mayer transfer operators, and resonance theory remain cited inputs.

## Exact Theorem Package

### Theorem A: open-channel classification and non-descent

Oriented nontrivial double cosets \(P\backslash\Gamma/P\) with chosen \(c>0\) are parametrized by
\[
(c,d),\qquad c\ge1,\quad d\in(\mathbb Z/c\mathbb Z)^\times.
\]
Thus level \(c\) has \(\varphi(c)\) algebraic channels.  The height \(2\log c\) is double-coset invariant but does not descend to hyperbolic conjugacy classes.  For example,
\[
g=\begin{pmatrix}2&1\\3&2\end{pmatrix}
\]
has \(|c(g)|=3\), while an \(S\)-conjugate has lower-left absolute value \(1\).

This theorem is a type boundary, not a claim that a local roof or an enlarged endpoint cocycle must be conjugacy invariant.

### Theorem B: denominator-only exact-clock no-go

If \(F:\mathbb N\to\mathbb R\) satisfies
\[
F(|c(g^n)|)=nF(|c(g)|)
\]
for every hyperbolic \(g\in\mathrm{SL}_2(\mathbb Z)\) and every \(n\ge1\), then \(F\equiv0\).

The proof uses only two exact families.  Set
\[
A_m=\begin{pmatrix}m&-1\\1&0\end{pmatrix},\qquad m\ge3.
\]
Since \(c(A_m)=1\) and \(c(A_m^2)=m\),
\(F(m)=2F(1)\).  But \(c(A_3^3)=8\), so \(F(8)=3F(1)\), while the square relation at \(m=8\) gives \(F(8)=2F(1)\).  Hence \(F(1)=0\) and \(F(m)=0\) for all \(m\ge3\).

For
\[
B_k=\begin{pmatrix}1&1\\k&k+1\end{pmatrix},\qquad k\ge1,
\]
one has \(c(B_k)=k\) and \(c(B_k^2)=k(k+2)\ge3\), so \(2F(k)=0\).  This proves the claim.

### Theorem C: stable closure is Selberg length

For hyperbolic \(g\) with a lift of trace \(t>2\), lower-left entry \(c\ne0\), and
\[
\lambda=\frac{t+\sqrt{t^2-4}}2,
\qquad \ell(g)=2\log\lambda,
\]
Cayley--Hamilton gives
\[
c(g^n)=c(g)U_{n-1}(t/2).
\]
Hence
\[
2\log|c(g^n)|
=n\ell(g)
+2\log\frac{|c(g)|}{\sqrt{t^2-4}}
+2\log(1-\lambda^{-2n}).
\]
In particular,
\[
\lim_{n\to\infty}\frac{2\log|c(g^n)|}{n}=\ell(g).
\]
More generally, any power-homogeneous \(L\) satisfying
\(L(g^n)-2\log|c(g^n)|=o(n)\) must obey \(L(g)=\ell(g)\).  Thus the stable closed clock is rigidly the Selberg clock.

### Theorem D: zero-free-normalization divisor no-go

For
\[
\Phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},
\]
each nontrivial zeta zero \(\rho\) supplies a pole at \(s=\rho/2\) and a zero at \(s=(1+\rho)/2\), without cancellation.  Cusp scaling multiplies \(\Phi\) by a zero-free exponential.  Therefore no entire zero-free factor multiplying an affine reparametrization of \(\Phi\) can turn it into the single entire function \(\xi\).

## Reproducible Experiment

The code is a proof audit, not a discovery fit.

1. Enumerate oriented double-coset representatives through a frozen denominator cutoff and verify exactly that their counts are \(\varphi(c)\).
2. Recompute the conjugacy witness and a positive Gauss-word cyclic-shift witness using exact integer matrices.
3. Verify \(c(g^n)=c(g)U_{n-1}(t/2)\) for a broad exact census of hyperbolic matrices and powers.
4. Generate the complete \(A_m,B_k\) rigidity certificate.
5. Evaluate the exact defect formula at high precision and show convergence of \(2\log|c(g^n)|/n\) to \(\ell(g)\).
6. Compare finite totient Dirichlet sums with \(\zeta(2s-1)/\zeta(2s)\) at frozen \(\Re s>1\) points, with an explicit absolute tail bound.
7. Use a second implementation that does not import the producer.

## Controls and Falsifiers

- **Closed-clock positive control:** \(\ell(g^n)=n\ell(g)\) and cyclic/conjugacy invariance.
- **Orientation control:** raw totient counts are labeled oriented algebraic channels; reversal-identified geometric scattering geodesics are not conflated with them.
- **Gauge control:** changing \(T_0\) adds a constant to a single sojourn time and a zero-free exponential to scattering normalization; it cannot repair exact closed repetition.
- **Chronology control:** every Gauss word is multiplied in order, and cyclic shifts/repetitions are stored separately.
- **Target-blindness:** no prime table, zeta-zero list, fitted scale, or offset enters the producer.
- **Immediate falsifier:** any nonzero \(F\) passing Theorem B's universal hypotheses, or any exact failure of the Chebyshev/defect formula.

## Novelty and Claim Boundary

Guillemin and Ji--Zworski establish the geometric role of sojourn times; Pujahari--Satpathy give the explicit modular denominator formula and scattering-geodesic counting; Mayer, Series, Lewis--Zagier, and Pohl--Wabnitz cover the closed geodesic and transfer-operator side.  The defensible delta is therefore narrow: a source-faithful exact-clock rigidity theorem and the identification of its stable closure, used as a Hilbert--Pólya Route-A obstruction.

The result does not exclude endpoint-extended transfer operators, matrix cocycles, subadditive pressure, open groupoid traces, multi-cusp scattering, or a separately derived self-adjoint construction.  It closes the literal denominator-only hyperbolic Euler-product route.

## Claim-Driven Validation

### Primary claim

- **Evidence:** self-contained proofs of Theorems B and C, exact machine certificates, and an independent implementation.
- **Pass criterion:** all integer identities pass; the stable defect matches the closed formula to the declared precision; no source or orientation ambiguity remains.

### Supporting claim

- **Evidence:** exact divisor mapping and zero-free-normalization proof for \(\Phi\), with physical-line unitarity only as a classical control.
- **Pass criterion:** all poles and zeros are classified symbolically; no numerical zero fit is used.

## Experiment Handoff

- **Must-run:** exact double-coset census, rigidity families, general Chebyshev audit, stable-limit table, Dirichlet convergence with tail bounds, independent checker.
- **Nice-to-have:** post-theorem plots of the stable defect and open/closed clock convergence.
- **Highest risk:** low standalone novelty.  The paper must present itself as a scoped obstruction and positive-control closure, not as a new scattering theory.
- **Compute:** CPU seconds/minutes, no GPU, Python standard library plus pinned `mpmath` for high-precision illustrations.
