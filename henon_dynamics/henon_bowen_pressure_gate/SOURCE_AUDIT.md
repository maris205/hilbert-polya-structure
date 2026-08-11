# HCS-C31 source and theorem-delta audit

## Audit conclusion

The qualitative conclusions are classical: positive Hölder potentials have a
unique real pressure root; locally constant cylinder potentials have finite
transfer matrices; geometric pressure gives slice dimension under an
appropriate Bowen theorem; and analytic all-word pinning/nuclearity already
belongs to the BPS/Rugh framework.

The C31 theorem delta is the exact, machine-checkable bridge

\[
\text{certified local Hénon geometry}
\longrightarrow
\text{full-cylinder roof intervals}
\longrightarrow
\text{Perron pressure signs}
\longrightarrow
\text{a narrow real root interval},
\]

together with the self-consistent slope bound and the obstruction
interpretation of the old positive finite-section signal.

## 1. Primary local dependencies

### R058 covering and cones

Path:

henon_dynamics/docs/related_programs/henon_weighted_zeta/R058_COVERING_PROOF.md

Used results:

- exact four h-sets and six allowed covering relations;
- exclusion of every other one-step transition;
- normalized derivative matrices;
- invariant disjoint stable/unstable cones;
- uniform hyperbolicity on the survivor.

R058 did not claim conjugacy, uniqueness of coding, local maximality as a
separate theorem, or Hausdorff dimension.

### R059 symbolic contraction

Path:

henon_dynamics/docs/related_programs/henon_weighted_zeta/research/refine-logs/R059_SYMBOLIC_CONTRACTION_PROOF.md

Used results:

- exact square-root recurrence and radicand ranges;
- contraction constant \(2/\sqrt{17}\);
- one orbit for every admissible bi-infinite itinerary;
- topological conjugacy with \(\Sigma_A\);
- exact primitive-period preservation;
- compact survivor definition.

C31 adds two short deductions:

1. the radicand ranges imply
   \(\sqrt{17}/12\le|q|\le\sqrt{3/8}\);
2. strict interior realization implies
   \(\Lambda_*=\operatorname{Inv}(\operatorname{int}N)\).

### Instability-roof project

Path:

henon_dynamics/henon_instability_roof_zeta/

Used results:

- tangent scales \(7/48\) and \(41/256\);
- the adapted roof

  \[
  \tau_{\rm ad}=\log|-12q-(123/112)\mu^u|;
  \]

- positivity via the inherited \(773/224\) bound;
- periodic sums equal \(\log|\Lambda_{u,p}|\);
- the exact non-lattice witness;
- the frozen positive finite-section value near
  \(0.277982981676189\), source-locked through
  `refine-logs/R000_FROZEN_PROTOCOL.json`,
  `results/roots_robustness.json` at sector (0), cutoff (20),
  `results/analysis_summary.json`, and
  `results/independent_check.json`.

The raw ledger records the 80-digit high-precision numerical value and the
summary reproduces it byte for byte; the independent audit checks the same
cutoff-20 root to 20 significant digits.  This is high-precision numerical
provenance, not an interval certification of all 80 digits.

C31 inherits no infinite determinant or pressure convergence theorem from
that project.  The old project explicitly labels its zeros as finite-section
observations.

### Planned Ruelle/dimension project

Path:

henon_dynamics/next_paper_henon_ruelle_operator/

Its audit correctly identifies the norm-gauge, local-maximality,
ambient-surface, cylinder-envelope, and determinant-semantics obligations.
No production result is inherited from that directory.

## 2. Bowen/McCluskey--Manning scope

Primary paper:

Heather McCluskey and Anthony Manning, “Hausdorff dimension for horseshoes,”
Ergodic Theory and Dynamical Systems 3 (1983), 251--260,
<https://doi.org/10.1017/S0143385700001966>.

The paper begins with a compact surface without boundary and an Axiom-A
diffeomorphism.  Theorem 1 identifies the Hausdorff dimension of the unstable
slice of a basic set with the unique root of

\[
P\!\left(-t\log\|Df|_{E^u}\|\right)=0.
\]

The stable statement applies it to \(f^{-1}\).  Theorem 2 gives the sum of
stable and unstable slice dimensions for a \(C^2\) surface basic set.

Official erratum:

Anthony Manning, “Errata to ‘Hausdorff dimension for horseshoes’,”
Ergodic Theory and Dynamical Systems 5 (1985), 319,
<https://doi.org/10.1017/S0143385700002947>.

The erratum deletes Section 3 and its bifurcation theorem; it says the rest is
unaffected.  It does not invalidate the slice-pressure or total-set results.

### Exact local slice theorem: interface passed

Pesin and Sadovskaya, “Multifractal Analysis of Conformal Axiom A Flows,”
Communications in Mathematical Physics 216 (2001), 277--312,
<https://doi.org/10.1007/s002200000329>, Remark 4.1 (printed page 284),
states the map version needed here.  If \(f\) is \(u\)-conformal on a locally
maximal hyperbolic set \(X\), then for an open unstable piece \(U\),

\[
\dim_H(U\cap X)=t^u,
\qquad
P_X(f,-t^u\log b^u)=0.
\]

It does not impose the global Axiom-A/compact-ambient hypothesis that blocked
a literal application of McCluskey--Manning.  In the present surface system
\(\dim E^u=1\), so the Euclidean derivative on \(E^u\) is conformal.  Theorem 4
of the C31 theorem package proves local maximality, and Theorem 3 identifies
the Euclidean pressure with the adapted pressure.  Hence the unstable-slice
dimension statement is **PROVED**.

### Exact total-dimension theorem: interface passed

Luís Barreira, *Dimension Theory of Hyperbolic Flows*, Springer Monographs in
Mathematics (2013), <https://doi.org/10.1007/978-3-319-00548-5>,
Introduction, Theorem 1.2, states:

> If \(\Lambda\) is a locally maximal hyperbolic set for a \(C^1\) surface
> diffeomorphism and
> \(\dim E^s(x)=\dim E^u(x)=1\), then
> \(\dim_H\Lambda=t_s+t_u\), where \(t_s,t_u\) are the stable and unstable
> pressure roots.

No global Axiom-A or compact ambient surface is assumed in this statement.
Theorem 7 of the C31 package proves \(t_s=t_u=h_*\).  Therefore
\(\dim_H\Lambda_*=2h_*\) is **PROVED**.

The McCluskey--Manning compact/global scope remains an important audit fact,
but C31 no longer relies on broadening that theorem.

## 3. Pressure baseline

These are standard inputs, not new claims:

- the variational principle and pressure monotonicity;
- Ruelle--Perron--Frobenius for a mixing finite-type shift;
- pressure of a locally constant edge potential as log Perron root;
- pressure invariance under a continuous coboundary;
- the leading pressure singularity for a positive non-arithmetic suspension
  under the hypotheses of a cited zeta theorem.

Primary context already identified by the repository includes:

- Parry--Pollicott on zeta functions and prime-orbit asymptotics,
  <https://annals.math.princeton.edu/1983/118-3/p07>;
- Liverani on dynamical determinants,
  <https://arxiv.org/abs/math/0505049>;
- Pollicott--Slipantschuk on validated pressure bounds,
  <https://doi.org/10.1088/1361-6544/ad6053>;
- Jenkinson--Pollicott on effective dimension bounds,
  <https://arxiv.org/abs/1611.09276>.

C31's novelty is the end-to-end Hénon certificate and its error interval, not
the Perron theorem.

## 4. BPS/Rugh pinning prior art

Primary source:

Viviane Baladi, Enrique R. Pujals, and Martine Sambarino,
“Dynamical zeta functions for analytic surface diffeomorphisms with dominated
splitting,” arXiv:math/0307045,
<https://arxiv.org/abs/math/0307045>.

Relevant audited locations:

- Definition 2.4: pinning coordinates;
- Proposition 2.6: unique iterated pinning coordinates;
- equation (2.13) and Definition 3.5: mixed kernels and graph operator;
- Remark 3.6: chronological composition warning;
- Lemmas 3.7--3.8: word kernels, nuclearity of order zero, and the absolute
  flat-trace/Fredholm identity.

Local audit:

henon_dynamics/henon_pinning_trace_obstruction/SOURCE_AUDIT.md

| Proposed claim | Verdict |
|---|---|
| First Hénon pinning coordinates | rejected; the classical framework specializes |
| First one-step-to-all-word composition | rejected; BPS Proposition 2.6/Lemma 3.7 |
| First nuclear holomorphic word operator | rejected qualitatively |
| First flat-trace identity | rejected qualitatively |
| Explicit useful \(H_6\) tails | potentially project-specific |
| Certified Hénon pressure interval | C31's main project-specific result |

The BPS flat trace and instability-weight trace are different objects.

## 5. Exact C31 theorem delta

### New exact analytic lemmas

1. Realized-coordinate bound:

   \[
   \frac{\sqrt{17}}{12}\le|q|\le\sqrt{\frac38}.
   \]

2. Self-consistent cone refinement:

   \[
   |\mu^u|\le\frac{112}{123}
   \frac{\sqrt{17}-\sqrt{13}}2.
   \]

3. Adapted expansion bound:

   \[
   J^u_{\rm ad}\ge\frac{\sqrt{17}+\sqrt{13}}2.
   \]

4. Explicit adapted/Euclidean coboundary.
5. Explicit local-maximality deduction.
6. Stable-angle lower bound and stable/unstable coboundary.
7. Improved absolute instability-trace radius:

   \[
   |z|<
   \frac{\sqrt{17}+\sqrt{13}}{1+\sqrt5}
   =2.388286326\ldots .
   \]

### New computer-assisted theorem target

Full interval roofs on all \(1156\) chronological length-\(13\) cylinders,
combined with directed Perron bounds on \(714\times714\) sparse matrices, give

\[
\frac{277980}{10^6}<h_*<\frac{277987}{10^6}.
\]

This is the dominant result once the checker passes.

### New obstruction interpretation

The independent interval contains the old finite-section value, so that
signal is consistent with pressure geometry at the certified resolution.
Containment does not prove equality or convergence of the old sections.  The
two exact local dimension theorems identify the certified pressure root---not
the finite-section sequence---with the unstable-slice and total-set
dimensions.  The comparison supplies no new arithmetic spectral line.

## 6. Locked nonclaims

- The finite cycle sections are not proved to converge at \(s=h_*\).
- A pressure root is not automatically a Fredholm determinant zero.
- A zeta pole and inverse-determinant zero are different conventions.
- The local survivor is not the full bounded Hénon set.
- The literal compact-surface scope of McCluskey--Manning is not waived; C31
  instead uses the exact local statements located above.
- Generic BPS pinning/nuclearity is not new.
- The instability radius is not a BPS flat-trace radius.
- No arithmetic correspondence, functional equation, critical-line theorem,
  Riemann--von Mangoldt law, or Hilbert--Pólya operator is established.

## 7. Final source-lock fields

Record for every external theorem:

- title, authors, identifier, version/date, and theorem number;
- exact hypotheses;
- compact/noncompact ambient applicability;
- local maximality versus global Axiom A;
- smoothness for slice and total dimension;
- erratum impact;
- determinant/zeta weight and sign convention;
- hashes of inherited proofs and all C31 mathematical documents.

## 8. Final evaluation firewall

The exact local source audit removes the former dimension blocker but does
not improve any Hilbert--Pólya criterion:

~~~text
pressure: NUMERICALLY_CERTIFIED
analytic_pressure_implication: PROVED
unstable_slice_dimension: PROVED
total_Hausdorff_dimension: PROVED

Route-A: (A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
overall: ROUTE_A_REJECTED
Route B authorized: false
~~~

The first four entries are theorem-ledger statuses.  They are not additions
to the allowed Route-A vocabulary.
