# Phase 3 — Packet Trace No-Go Audit

Date: 2026-08-13  
Frozen candidate: DEN-WITT-Z-FIN  
Scope: mathematical audit only; no determinant construction and no inference from the Riemann Euler product

## Verdict

The frozen source supports one unconditional obstruction and one conditional
non-uniqueness theorem:

1. **PROVED:** the conventional individual-orbit Euler/Ruelle product is not
   defined.  A single \(\Gamma_p\) contains uncountably many primitive orbits
   with the identical least period \(\log p\), so primitive-orbit counting is
   not locally finite in length.
2. **CONDITIONAL:** even if every packet base is assigned its normalized Haar
   probability, the current homogeneous axioms do not select a unique global
   trace.  They leave both a global scale and, absent cross-packet relations,
   independent component masses \(m_p\).
3. **OPEN / NOT_TESTABLE:** a measured, groupoid, clean-family, or Lefschetz
   trace may exist only after additional structure is supplied.  It is not
   derived by the frozen Deninger object.
4. **PROVED source distinction:** Deninger Section 11 contains a genuine
   Haar-normalized group convolution algebra, but no theorem connects it to
   packet return traces or a flow determinant.

The calibrated Route-A outcome remains
\(A1=\mathrm{WEAK}\), conventional \(A2=\mathrm{FAIL}\), alternative measured
\(A2=\mathrm{NOT\_TESTABLE/OPEN}\), and \(A3=\mathrm{FAIL}\).

## Evidence labels

- **PROVED:** stated in the source, or follows by the displayed complete
  elementary argument.
- **CONDITIONAL:** a theorem after assumptions stated here; the frozen source
  does not supply all those assumptions.
- **OPEN:** meaningful, but not proved or refuted for the frozen object.
- **NOT_TESTABLE:** the required domain, topology, action, or operator has not
  been defined for the frozen object.

## 1. Uncountable orbit family and the ordinary product

The source proves that every orbit in \(\Gamma_p\) has least period
\(\log p\), and gives a choice-dependent, set-level equivariant
parametrization of its orbit set by

\[
B_p=\widehat{\mathbb Z}_{(p)}^\times/p^{\widehat{\mathbb Z}}.
\]

It does not prove that this parametrization is a canonical homeomorphism of
the quotient-topological orbit space.  The following obstruction needs only
the set-level statement.

### Proposition 1 — \(B_p\) is uncountable

**Status: PROVED.**

The compact group \(\widehat{\mathbb Z}_{(p)}^\times\) contains an uncountable
exponent-two subgroup obtained by independently choosing \(\pm1\) in
infinitely many odd local factors.  Its intersection with the procyclic
subgroup \(p^{\widehat{\mathbb Z}}\) has at most two elements.  Its image in
\(B_p\) is therefore uncountable.

Consequently \(\Gamma_p\) contains uncountably many distinct primitive orbits,
all at the single length \(\log p\).  “Primitive” is justified because this is
their least period.

### Theorem 2 — conventional orbitwise Ruelle product is undefined

**Status: PROVED.**

Let \({\cal P}\) be the set of individual primitive orbits.  For every
\(T\ge\log p\),

\[
\#\{\gamma\in{\cal P}:\ell(\gamma)\le T\}
\]

is uncountable.  Thus the primitive-orbit counting measure is not locally
finite in length.

For the ordinary direct-product convention, a fixed packet would contribute

\[
\prod_{\gamma\subset\Gamma_p}
  \left(1-e^{-s\ell(\gamma)}\right)^{-1}.
\]

For real \(s>0\), every factor is the same number
\((1-p^{-s})^{-1}>1\); the finite-subset net diverges to \(+\infty\).
For complex \(s\), the identical nonzero logarithmic terms are not
unconditionally summable.  Therefore this is not a nonzero finite
holomorphic product.

Replacing the whole packet by one factor \((1-p^{-s})^{-1}\) changes the
counting measure from one atom per orbit to one atom per packet.  That is the
normalization under investigation, not a consequence of the ordinary
isolated-orbit product.

**Boundary:** this theorem rules out only the conventional orbit-counting
product.  It does not rule out a separately justified measured, clean-family,
groupoid, or cohomological trace.

## 2. Three distinct normalization layers

### N1 — normalized invariant probability on one packet base

If the abstract compact-group structure of \(B_p\) is fixed, normalized Haar
probability \(\mu_p\) is uniquely determined.

**Status: PROVED as a compact-group theorem; source-to-packet use is
CONDITIONAL.**

Deninger's packet/base coordinates depend on auxiliary choices, and the source
does not prove that the quotient topology on \(\Gamma_p/\mathbb R\) is
homeomorphic to the compact-group topology or that all choice changes preserve
the transported measure.  Even if these issues are resolved, N1 proves only
\(\mu_p(B_p)=1\).  It does not identify this mass with a fixed-point or
operator-trace coefficient.

### N2 — lift or disintegration from the base to \(\Gamma_p\)

A lift requires a canonical measurable quotient map, a measurable family of
conditional measures on the circular flow fibres, invariance under the flow,
and independence of all auxiliary choices.

**Status: OPEN / NOT_TESTABLE.**

The source supplies the orbit periods and a set-level fibration description,
but no canonical disintegration theorem.  Therefore N1 does not imply N2.

### N3 — relative masses of all prime components

Suppose conditionally that every packet has a normalized local functional
\(\tau_p\).  On the finite-support component algebra every functional

\[
\tau((a_p)_p)=\sum_p m_p\,\tau_p(a_p),\qquad m_p>0,
\]

has the same linearity, positivity, within-packet invariance, locality, and
disjoint-union additivity properties.  The distinct clocks
\(\log p\ne\log q\) prevent flow-equivariant clock-preserving symmetries from
identifying different packet components.

**Status: CONDITIONAL NON-UNIQUENESS THEOREM.**

The listed homogeneous axioms do not determine \((m_p)\).  In particular they
do not derive \(m_p=1\).  Closed-point counting measure is canonical
arithmetic data and does assign one atom per closed point, but no source theorem
identifies its pushforward with a flow return trace or derives repetition
coefficients from it.  That bridge remains **OPEN**.

There is also an independent operator gate: N1, N2, and N3 together would
still not make a Koopman/transfer operator trace class or yield a Lefschetz
coefficient.

## 3. Rescaling, copied-packet, and arbitrary-base controls

### Rescaling

If \(\tau\) obeys homogeneous trace axioms, then \(c\tau\) obeys them for every
\(c>0\).  Componentwise, arbitrary \(m_p\tau_p\) also survives.

**Status: PROVED conditional no-go for uniqueness.**

A nonhomogeneous source-derived normalization or cross-component theorem is
necessary.  The expected Euler factor and the expected convergence half-plane
cannot supply it.  Indeed the abscissa depends on
\(\sum_p m_p p^{-s}\), so it must be derived after the masses.

### Copied packet

For a disjoint union \(P\sqcup P\), additivity forces

\[
\tau(P\sqcup P)=2\tau(P).
\]

Renormalizing both \(P\) and \(P\sqcup P\) to mass one violates additivity;
counting once per isomorphism class erases geometric multiplicity.

**Status: PROVED consistency control, not an absolute existence no-go.**

### Arbitrary equal-period base

Replacing \(B_p\) by any infinite compact group still provides unique
normalized Haar probability and equal-period circle fibres.

**Status: PROVES-TOO-MUCH control.**

Haar probability alone is not arithmetic-specific and cannot establish the
packet-to-trace bridge.  A successful theorem must use source-derived
arithmetic/Frobenius structure at an explicit trace step.

Together these controls prove non-uniqueness under the current minimal axioms.
They do not prove that every possible enriched trace is nonexistent.

## 4. Section 11 is not the missing bridge

Deninger Section 11 constructs a locally compact group
\(\varprojlim K^\times\), normalizes its Haar measure by the mass of a compact
open subgroup, defines convolution on \(C_c(\varprojlim K^\times)\), and gives
an algebra homomorphism to functions on the source space.

**Status: PROVED source structure.**

However, the source gives no:

- map from this group convolution algebra to \(\Gamma_p/\mathbb R\);
- selected locally compact packet groupoid and Haar system;
- representation of the suspension flow whose periodic return is traced;
- trace-class, flat-trace, or renormalized-trace theorem;
- formula deriving primitive and repeated packet coefficients; or
- Fredholm determinant theorem.

**Status of the bridge: OPEN / NOT_TESTABLE.**

Thus “the source contains a Haar-normalized algebra” is true, while “the source
contains the canonical packet trace” is false as a source claim.  A group Haar
normalization fixes that group convolution's scale; it does not fix a packet
base lift, cross-\(p\) masses, or a flow fixed-point coefficient.

## 5. Independent trace gates

- **Naive Koopman trace — CONDITIONAL no-go.**  Under any full-support
  realization with infinite-dimensional \(L^2(\Gamma_p)\), the return at
  \(\log p\) is the identity.  The identity on an infinite-dimensional Hilbert
  space is not trace class.
- **Clean-family trace — NOT_TESTABLE.**  Existing theorems require a smooth
  fixed submanifold, the clean tangent identity, a nondegenerate normal return
  map, and symbol/density/phase data.  The frozen topological object supplies
  none of these.
- **Groupoid trace — NOT_TESTABLE.**  No packet groupoid, arrow topology, Haar
  system, convolution domain, or invariant transverse measure is source-locked.
- **Lefschetz/cohomological trace — OPEN / NOT_TESTABLE.**  No source-derived
  cohomology, induced return action, trace domain, or fixed-point theorem has
  been frozen.

Any general von Neumann-algebra construction is a ROUND2_CLUE under the
proposal's scope rule, not the main Stage-2 result.

## 6. Final calibration

| Question | Decision | Evidence |
|---|---|---|
| Can all individual primitive orbits define the ordinary Ruelle product? | No | **PROVED:** length-local finiteness fails already inside one packet |
| Does packet-base Haar probability exist abstractly? | Yes | **PROVED:** standard compact-group Haar theorem |
| Does it canonically lift to the source packet? | Not established | **OPEN / NOT_TESTABLE** |
| Does it determine global packet masses? | No under current axioms | **CONDITIONAL non-uniqueness theorem** |
| Do rescaling and copied packets expose hidden normalization? | Yes | **PROVED controls** |
| Does Section 11 supply a packet return trace? | No source theorem | **OPEN / NOT_TESTABLE bridge** |
| Is there a legitimate determinant to continue or root-test? | No | **A2_FAIL / not applicable** |

The evaluator's root, divisor, cutoff-drift, and continuation fields must be
recorded as not applicable because no candidate determinant exists.

The smallest non-circular positive next step is a choice-independent measured
orbit quotient plus either (i) a flow-specific packet groupoid with a proved
trace theorem, or (ii) a cohomological/Lefschetz return construction deriving
all repetition coefficients.  Without such new structure, the correct Paper 2
endpoint is the no-go/non-uniqueness result above, not a formal packet Euler
product.
