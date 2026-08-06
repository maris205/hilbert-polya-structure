# Independent audit of the C02/C02B paper route

Date: 2026-08-05  
Scope: C02B theorem, `PAPER_PLAN.md`, Route-A boundary, and primary-source
collision risk  
Verdict: **C02B theorem valid; manuscript freeze blocked pending WP0 source
delta**

## 1. Theorem audit

No mathematical blocker was found in the C02B complex signed-root theorem.
The audit independently checked:

- the two radicand disks
  \(\overline D(1/6,7/144)\) and
  \(\overline D(47/144,7/144)\);
- their right-half-plane gaps \(17/144\) and \(5/18\);
- the strict image margins
  \[
  \frac{\sqrt{17}-4}{12},\qquad
  \frac58+\frac{\sqrt{10}-\sqrt{47}}6;
  \]
- the Fréchet derivative bound
  \(\|DT_\varepsilon\|_{\infty\to\infty}\le2/\sqrt{17}<1\);
- genuine open-neighborhood holomorphy on \(\ell^\infty\);
- retention of both chronological neighbor occurrences at cyclic periods one
  and two.

A clean temporary-directory rerun passed the producer and all 18 independent
checks with 32,768 boundary samples per radicand disk.  Sampling is a
regression diagnostic, not part of the proof.

The audit found and prompted repair of two package defects: a theorem
typesetting typo and a checker that previously accepted a truncated cyclic
ledger because `zip` compared only the common prefix.  The checker now
requires exactly 12 persisted and recomputed rows; a deliberately truncated
two-row ledger fails as intended.

## 2. What is already proved versus open

T1 already proves a unique fixed sequence for every admissible finite cyclic
word.  Therefore “existence of cyclic closure” is not a new T2 claim.  The
open assertions are:

- endpoint-diagonal equivalence with the T1 cyclic solution;
- two-coordinate pinning/crossed-map composition;
- derivative and matching-Jacobian bookkeeping;
- relation to the chronological Hénon monodromy and a frozen flat trace.

The finite-window endpoint lemma should freeze the extended symbols
\(\varepsilon_0,\ldots,\varepsilon_{N+1}\), use the full domains
\(D_{\varepsilon_0}\times D_{\varepsilon_{N+1}}\), and impose the local rule
\(\neg(\varepsilon_{i-1}=\varepsilon_{i+1}=+1)\) for internal sites.

Set

\[
a_0=\frac1{\sqrt{17}},\qquad
\kappa=\frac2{\sqrt{17}}.
\]

The internal derivative matrix has sup norm at most \(\kappa\).  Neumann paths
therefore give the natural explicit targets

\[
|\partial_uQ_i|
\le\frac{a_0\kappa^{i-1}}{1-\kappa},
\qquad
|\partial_vQ_i|
\le\frac{a_0\kappa^{N-i}}{1-\kappa},
\]

and the interface response constant

\[
\beta=\frac{a_0}{1-\kappa}=\frac1{\sqrt{17}-2}<1.
\]

Thus most of T2 is expected to be a short analytic corollary of C02B.
Enumeration should test implementation and sharpness, not serve as evidence
for existence.

## 3. Direct prior-art collision risk

The original route understated prior work on pinning coordinates.

- H. H. Rugh, *The correlation spectrum for hyperbolic analytic maps*,
  Nonlinearity 5 (1992), 1237--1263,
  DOI: https://doi.org/10.1088/0951-7715/5/6/003, already introduces analytic
  pinning coordinates/half-inverses for hyperbolic analytic maps.
- V. Baladi, E. R. Pujals, and M. Sambarino, *Dynamical zeta functions for
  analytic surface diffeomorphisms with dominated splitting*,
  https://arxiv.org/abs/math/0307045, gives a particularly direct iterated
  pinning-map formulation; Proposition 2.6 and Corollary 2.8 cover analytic
  iteration/composition and symbolic-cycle closure.
- H. H. Rugh, *Generalized Fredholm determinants and Selberg zeta functions
  for Axiom A dynamical systems*,
  https://doi.org/10.1017/S0143385700009111, already supplies generalized
  determinant and entire-continuation results for Axiom-A surface settings.

Hubbard--Oberste-Vorth II should not be cited as directly subsuming the
area-preserving map: its stated regime assumes sufficiently small Jacobian
parameter, whereas the present map has determinant one.  It remains relevant
context, as does general complex-horseshoe theory, but not yet a direct theorem
for the certified \(H_6\) domains.

## 4. Minimum potentially publishable delta

Existence, holomorphy, pinning composition, and cyclic closure are not presumed
novel.  A paper route survives only if WP0 identifies and WP1--WP3 proves at
least one substantive project-specific delta:

1. explicit complex endpoint domains and sharp/uniform \(H_6\) constants;
2. a certified crossed-map composition and quantitative extension-error
   theorem;
3. an exact matching-Jacobian identity tied to
   \(\det(I-DH_6^n)\) on the certified local survivor;
4. complex-\(q\) recertification of the projective fibre domains with a new
   distortion or trace estimate;
5. a reproducible certificate that makes a previously nonconstructive theorem
   effective.

If none survives claim-by-claim comparison, C02B remains valuable analytic
infrastructure but there is no new paper on this route.

## 5. Operator and Route-A boundary

The proposed flat trace must be restricted to
\(\operatorname{Fix}(H_6^n)\cap\Lambda_*\), use the chronological product
\(g_n(x)=\prod_{j=0}^{n-1}g(H_6^j x)\), and freeze the signed holomorphic
denominator before computation.  Replacing \(\det(I-DH_6^n)\) by an absolute
value is a different construction.

No ordinary Hardy/Bergman composition space should be assumed in advance.
Pinning-coordinate theory can require mixed interior/exterior holomorphic
variables, Cauchy kernels, and orientation signs.  The exact space, kernel,
potential/clock, norm, and trace must be source-locked in a separate operator
experiment plan.

C02/C02B is formally `NOT_TESTABLE` at the Route-A input stage because it has
no frozen clock, normalization, or determinant.  The recorded A1--A4 tuple is
only an informal layer ceiling, and Route B remains closed.

## 6. Final recommendation

Run the primary-source delta audit as WP0 before implementing C02C.  If a
quantitative \(H_6\) delta survives, prove the full-disk endpoint bounds and
crossed-map/trace Jacobian theorem.  Otherwise stop cleanly and return to the
breadth-first RH candidate search.
