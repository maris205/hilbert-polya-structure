# Round 1 Review: Embedded-Formal Claim Requires Structural Repair

**Record type:** evidence-bound reconstruction of the first review stage, not
a verbatim response from an external model.

**Date:** 2026-08-16 UTC

**Verdict:** REVISE BEFORE SOURCE LOCK

**Criteria binding:** `criteria_binding_unavailable`.  No target venue or
venue-specific rubric was supplied, so this review does not assert venue fit.

**Reviewer independence limitation:** the available refinement and review
work used the same model family.  Role separation reduces direct authorship
bias but does not remove correlated mathematical blind spots.  No cross-model
review is represented here.

## Problem Anchor

> For the normalized two-parameter Hénon family
> \(H_{a,c}(x,y)=(ay+x^d+c,x)\), with fixed integers \(d,n\ge2\), construct
> the generic cover of actual exact-period-\(n\) cycles without confusing the
> full fixed scheme, formal-period points, or special fibers; determine its
> cycle monodromy; and decide whether the cycle observables
> \(\tau=\sum_i z_i\) and
> \(\rho=\operatorname{tr}(DH_{a,c}^{n})\) each generate the generic
> primitive-cycle field.

## Anchor and Focus Assessment

The initial direction addressed the right family and the right periodic-cycle
question, but it identified several non-equivalent schemes.  The dominant
contribution should be a normalized generic actual-period cover with a proved
special line and cycle monodromy.  The two primitive observables can remain a
single supporting claim only if they are treated separately and share the same
field-theoretic mechanism.

The proposal must not grow into a classification of arbitrary generalized
Hénon maps.  It also does not need numerical orbit tables, parameter scans, or
additional dynamical observables.

## Fail-Fast Findings

### F1. Formal period is not actual period on the branch locus

For the scalar family \(f_t(z)=z^2+t\),

\[
 \Phi_2(z,t)=z^2+z+t+1.
\]

At \(t=-3/4\), the point \(z=-1/2\) is fixed, has multiplier \(-1\), and
also satisfies \(\Phi_2=0\).  Thus a formal period-two point can have actual
period one.  Any global embedded-actual-period interpretation of a formal
dynatomic equation is false.

**Required repair:** define the actual-exact-\(n\) block only over the generic
étale algebra, then take relative normalization.

### F2. Generic étaleness does not control every special fiber

The finite algebra

\[
 \mathbb Q[a,t]/(t^2-a)
\]

is generically separable, but its \(a=0\) fiber is
\(\mathbb Q[t]/(t^2)\).  A nonreduced special fiber is therefore compatible
with a well-behaved generic cover.

**Required repair:** prove the exact special fiber and explicitly avoid an
all-fibers-smooth or everywhere-torsor claim.

### F3. The embedded algebra need not be its normalization

The cusp inclusion

\[
 \mathbb Q[t^2,t^3]\subsetneq\mathbb Q[t]
\]

is finite and birational.  A coordinate algebra and its normal overring can
have the same fraction field without being equal.

**Required repair:** distinguish \(B_n\), the generic field \(E_n\), its
relative normalization \(S\), and the invariant ring \(S_0\).

### F4. The monodromy restriction direction must not be reversed

After removing the relevant branch locus, the image of a good special line is
a subgroup of the global geometric monodromy image.  It is not generally true
that global monodromy injects into the monodromy of an arbitrary special
fiber.

**Required repair:** use the known full special-line action as a lower bound
and the time-shift centralizer as an upper bound; state the hypotheses under
which this comparison is made.

### F5. The two traces are different categorical objects

The proposed \(\rho\) is

\[
 \rho=\operatorname{tr}\!\left(DH_{a,c}^{n}\right)
\]

evaluated on a marked cycle.  It is neither the field trace of an element of
the cycle field nor the base-valued determinant \((-a)^n\).  Likewise,
\(\tau=\sum_i z_i\) is an orbit-coordinate sum, not an algebra trace.

**Required repair:** prove cyclic invariance and non-base behavior for each
observable independently before applying any primitive-element argument.

### F6. The \(r=1\) boundary defeats a blanket non-base claim

For \((d,n)=(2,2)\),

\[
 \nu=2,\qquad r=1,\qquad \tau=a-1,
\]

\[
 z_0z_1=(a-1)^2+c,
 \qquad
 \rho=4z_0z_1+2a=4a^2-6a+4+4c.
\]

Both observables lie in \(K\), as they must for a degree-one cycle field.
Their linear characteristic polynomials are irreducible only in the trivial
degree-one sense.

**Required repair:** separate \(r=1\) from the \(r>1\) non-base and monodromy
argument.

## Minimum Acceptable Repair

The next proposal is acceptable only if it supplies this chain:

1. a monic Gröbner proof that \(B_n\) is \(A\)-free of rank \(d^n\);
2. the generic actual-exact-\(n\) étale idempotent factor \(E_n\), of dimension
   \(\nu=\sum_{e\mid n}\mu(n/e)d^e\);
3. a proof, using the \(a=0\) dynatomic field and idempotent lifting, that
   \(E_n\) is one field;
4. the finite, geometrically integral relative normalization \(S\), local
   freeness of rank \(\nu\), and a separate height-one/ramification/birational
   proof that \(S/aS\) is the stated reduced dynatomic algebra;
5. \(S_0=S^{\langle\sigma\rangle}\), rank
   \(r=\nu/n\), with the special affine cycle curve identified by Reynolds
   base change;
6. full \(S_r\) geometric monodromy on cycles, with the specialization
   direction written correctly;
7. separate non-base lemmas for \(\tau\) and \(\rho\), followed by the
   \(S_{r-1}\)-maximal-stabilizer argument and basis-free characteristic
   polynomials on \(\bigwedge_A^rS_0\);
8. the explicit \((2,2)\) degree-one boundary.

## Scope Decision

- Preserve: normalized family, fixed \((d,n)\), actual primitive cycles,
  special line, cycle monodromy, \(\tau\), and \(\rho\).
- Delete: global embedded formal-period scheme, every-fiber smoothness,
  everywhere free cyclic action, automatic normalization/base-change, and
  arbitrary-Hénon generalization.
- Validation cap: at most three bounded proof audits; no \((d,n)\) grid, no
  prime/modulus/parameter scan, and no table of exploratory values.

The proposal is promising after these repairs, but this record itself supplies
no proof verdict and no source-lock authorization.
