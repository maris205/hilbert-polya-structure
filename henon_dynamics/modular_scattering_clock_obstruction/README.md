# Modular scattering denominator-clock obstruction

**Candidate:** HCS-C17

**Research status:** exact open/closed clock separation with reproducible controls

**Hilbert--Pólya status:** Route-A rejected for the frozen denominator-only
closed-clock proposal; the classical modular scattering system is retained as
a positive noncompact control

## Outcome

This project makes the system switch requested after HCS-C16: from compact
quaternionic periodic flats to the one-cusp modular surface

\[
\mathrm{PSL}_2(\mathbb Z)\backslash\mathbb H.
\]

The switch exposes real arithmetic structure.  Oriented cusp double cosets in
the big Bruhat cell are indexed by

\[
(c,d\bmod c),\qquad c\geq 1,\quad (c,d)=1,
\]

and therefore have multiplicity \(\varphi(c)\).  Their Dirichlet series is

\[
\sum_{c\geq1}\frac{\varphi(c)}{c^{2s}}
=\frac{\zeta(2s-1)}{\zeta(2s)},\qquad \Re s>1.
\]

With the Archimedean factor, this is the standard one-cusp scattering
coefficient

\[
\Phi(s)=\sqrt\pi\frac{\Gamma(s-\tfrac12)}{\Gamma(s)}
\frac{\zeta(2s-1)}{\zeta(2s)}
=\frac{\Lambda(2s-1)}{\Lambda(2s)}.
\]

Thus the arithmetic signal is genuine.  The decisive question is whether its
denominator can also define the total clock of a closed hyperbolic orbit.

## Main obstruction

Fix any cusp scale \(\alpha>0\).  Suppose a final-monodromy denominator-only
clock has the form

\[
R_F(g)=F(\alpha |c(g)|),
\]

and is required to obey the closed-orbit repetition law
\(R_F(g^2)=2R_F(g)\) for every hyperbolic
\(g\in\mathrm{SL}_2(\mathbb Z)\) whose four entries are strictly positive.
Then

\[
F\equiv0\quad\text{on }\alpha\mathbb N_{>0}.
\]

The proof uses only

\[
\gamma_{m,n}=
\begin{pmatrix}1&m\\n&1+mn\end{pmatrix},
\qquad
c(\gamma_{m,n})=n,
\qquad
c(\gamma_{m,n}^2)=n(2+mn).
\]

It requires no continuity, monotonicity, or logarithmic ansatz.  Consequently,
no nonzero function of the final denominator alone can supply a standard
primitive/repetition clock for all closed hyperbolic classes.

This statement does **not** identify \(P g^n P\) with the \(n\)-fold repeat of
an open scattering channel.  Powers enter only when one tries to descend
final-denominator data to a closed conjugacy-class clock.

## Stable closure

For a hyperbolic lift with trace \(t>2\), let

\[
\lambda=\frac{t+\sqrt{t^2-4}}2,
\qquad \ell(g)=2\log\lambda.
\]

Cayley--Hamilton gives

\[
c(g^n)=c(g)U_{n-1}(t/2),
\]

and hence the exact identity

\[
2\log|c(g^n)|
=n\ell(g)
+2\log\frac{|c(g)|}{\sqrt{t^2-4}}
+2\log(1-\lambda^{-2n}).
\]

Therefore

\[
\lim_{n\to\infty}\frac{2\log|c(g^n)|}{n}=\ell(g).
\]

The canonical stable homogenization of the denominator height is exactly the
Selberg hyperbolic length.  It repairs repetition, but returns to the
Selberg--Mayer clock rather than producing a new Riemann-scattering clock.
This is not a uniqueness statement about all homogeneous class functions or
all possible repairs.

## Reproducible checks

The exact producer verifies the double-coset classification through
\(c=80\), 400 members of the positive rigidity family, and 48
Cayley--Hamilton identities.  A frozen primitive even-word audit contains
274 Gauss words:

- 259 have cyclically varying final denominators;
- 0 satisfy literal denominator square-additivity;
- all exact theorem witnesses pass.

The finite word census illustrates the theorem; it does not prove it.
Eighty-digit checks also recover the totient Dirichlet identity, physical-line
unitarity of \(\Phi\), and the stable-length formula without using prime or
Riemann-zero tables.

Run from this directory:

```bash
python code/modular_clock.py --output results
python code/independent_check.py \
  --results results --output results/independent_check.json
(cd code && python -m unittest -v test_modular_clock.py)
```

## Route-A interpretation

The frozen proposal fails as a closed dynamical-zeta/Hilbert--Pólya
construction:

- open cusp double cosets are not primitive closed hyperbolic conjugacy
  classes;
- every exact final-denominator-only closed clock satisfying square
  repetition is trivial;
- stable homogenization recovers the standard Selberg length;
- \(\Phi(s)\) is a meromorphic completed-zeta quotient, not one entire
  \(\xi\)-function after an affine change and zero-free normalization;
- the physical-line scattering operator is natural and unitary, but its
  resonant divisor is not a discrete self-adjoint Hilbert--Pólya spectrum.

The result leaves open local denominator cocycles, cyclic sums, trace- or
word-dependent clocks, cohomological corrections, endpoint-extended transfer
operators, matrix cocycles, subadditive pressure, open groupoid traces,
multi-cusp scattering, and normalizations that deliberately carry a zeta
divisor.

## Directory guide

- `paper/`: manuscript source and compiled PDF.
- `code/`: exact producer, independent checker, and tests.
- `results/`: compact machine-readable certificates and audits.
- `evaluations/route_a/`: frozen Route-A ruling.
- `DERIVATION_PACKAGE.md`: theorem statements and full derivations.
- `SOURCE_AUDIT.md`: primary-source and novelty boundary.
- `EXPERIMENT_PLAN.md`: claim-driven protocol and falsifiers.
- `IDEA_REPORT.md`: breadth-first system-switch screen.
- `AUTO_REVIEW.md`: adversarial review and remaining limitations.

## Claim boundary

This is a sharp compatibility obstruction and synthesis result.  It is not a
new derivation of modular scattering theory, a no-go theorem for every
cusp-derived roof, a new Selberg/Mayer determinant, a proof of the Riemann
hypothesis, or a Hilbert--Pólya operator.
