# Source and dependency audit

> Priority note (2026-08-05): the mathematical audit remains active, but its
> former N+1 scheduling language is superseded by
> `../next_paper_henon_candidate_search/`.

## Primary local source

- `../docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`

Paper 5 is treated as the origin of the exact map

\[
H_a(q,p)=(1-aq^2-p,q),
\]

not as an authority for its critical-parameter, quartic-surrogate, fitted
spectral, or Markov claims.

## Exact normalization bridge

The linear change

\[
C_a(q,p)=(-aq,ap)
\]

gives

\[
C_aH_aC_a^{-1}(X,Y)=(X^2+Y-a,-X).
\]

Thus Paper 5's parameter is directly the standard conservative Hénon
parameter in this convention. This bridge must be included when comparing
classical parameter regimes.

The conjugating matrix has determinant \(-a^2\); this is a classical linear
conjugacy, not a symplectic/metaplectic equivalence and therefore not a bridge
between quantum spectra.

## Tangent-norm gauge bridge

The inherited positive roof is defined in adapted tangent coordinates, not by
Euclidean unit vectors. With

\[
\widetilde u=\delta q/(7/48),\qquad
\widetilde v=\delta p/(41/256),
\qquad r=123/112,
\]

at \(z=(q,p)\in\Lambda_*\), with
\(E^u(z)=\{(\widetilde u,m^u(z)\widetilde u)\}\), the inherited physical
representative is

\[
\bar J^u_{\rm ad}(z)=|-12q-rm^u(z)|,\qquad
\bar\tau_{\rm ad}=\log\bar J^u_{\rm ad},
\qquad \bar J^u_{\rm ad}\ge773/224.
\]

Hausdorff dimension uses the Euclidean unit-vector expansion. The production
protocol must therefore certify, rather than merely assert, the coboundary

\[
DH_6(z)\bar e^u_{\rm ad}(z)
=(-12q-rm^u(z))\bar e^u_{\rm ad}(H_6z),
\]

with bounded Hölder
\(\bar b_u=\log\|\bar e^u_{\rm ad}\|_2\). Taking norms then yields

\[
\bar\tau_E^u(z)=\log\|DH_6(z)|_{E^u(z)}\|_2
=\bar\tau_{\rm ad}(z)+\bar b_u(H_6z)-\bar b_u(z),
\quad
\bar b_u(z)=\log\|(7/48,(41/256)m^u(z))\|_2.
\]

For \(x\in\Sigma_A\), define the pullbacks
\(\tau_{\rm ad}=\bar\tau_{\rm ad}\circ\pi\),
\(\tau_E^u=\bar\tau_E^u\circ\pi\), and
\(b_u=\bar b_u\circ\pi\). Then

\[
\tau_E^u(x)=\tau_{\rm ad}(x)+b_u(\sigma x)-b_u(x).
\]

Only after this bridge may the adapted pressure root be identified with the
Euclidean Bowen root. The stable/unstable angle identity is a second,
separately certified Euclidean coboundary.

## Exact low-parameter correction

The positive fixed point is

\[
q_+(a)=\frac{\sqrt{1+a}-1}{a},
\qquad
\operatorname{tr}DH_a(q_+,q_+)=2(1-\sqrt{1+a}).
\]

It is linearly elliptic for \(-1<a<3\); in particular the trace at
\(a=1.02\) is about \(-0.842\). This exactly refutes the strong legacy phrase
that only a chaotic saddle remains. It does not by itself prove KAM curves or
the survival of any specified global transport barrier.

The legacy \(a\simeq1.00561\) routine minimizes a sampled distance. Without a
zero of the tangency derivative, quadratic nondegeneracy, parameter
transversality, branch tracking, and exclusion of earlier competitors, it is
not a first-tangency certificate.

## Why the quartic surrogate is not the N+1 object

For the static one-dimensional Paper-5 surrogate with
\(V(q)=\lambda q^4+O(q^3)\), \(\lambda>0\), the Weyl law has
\(N(E)\sim C E^{3/4}\). No fixed affine energy rescaling turns this into the
Riemann--von Mangoldt \(T\log T\) growth. This is a useful foundations no-go,
but it concerns a chosen continuum surrogate rather than the exact Hénon
dynamics and is too small to replace the geometry-to-dimension paper as N+1.

## Inherited local dependencies to hash in R001

Geometry and symbolic base:

- `../docs/related_programs/henon_weighted_zeta/R058_COVERING_PROOF.md`
- `../docs/related_programs/henon_weighted_zeta/research/refine-logs/R059_SYMBOLIC_CONTRACTION_PROOF.md`
- `../docs/related_programs/henon_weighted_zeta/results/certified_domain_r059.json`
- `../docs/related_programs/henon_weighted_zeta/results/certified_domain_r059_check.json`
- `../docs/related_programs/henon_weighted_zeta/results/complex_root_census_a6_n12_merged.json`

Instability roof and expanded catalogue:

- `../henon_instability_roof_zeta/refine-logs/INHERITED_DEPENDENCIES.json`
- `../henon_instability_roof_zeta/refine-logs/R000_FROZEN_PROTOCOL.json`
- `../henon_instability_roof_zeta/results/catalog_robustness.json`
- `../henon_instability_roof_zeta/results/independent_check.json`
- `../henon_instability_roof_zeta/results/manifest.json`
- `../henon_instability_roof_zeta/results/ANALYSIS.md`

The new project inherits the certified interfaces but must hash and re-check
them. It does not count inherited cycles, roof values, or symbolic dynamics as
new results.

## Literature boundary

The relevant external baseline includes:

- Sterling, Dullin, and Meiss on homoclinic bifurcations and the conservative
  Hénon horseshoe: <https://arxiv.org/abs/chao-dyn/9904019>.
- Wilczak and Zgliczyński on computer-assisted homoclinic tangency methods:
  <https://arxiv.org/abs/0905.3924>.
- Liverani on dynamical determinants and spectra of transfer operators:
  <https://arxiv.org/abs/math/0505049>.
- Bandtlow and Jenkinson on explicit eigenvalue estimates for transfer
  operators on holomorphic spaces:
  <https://arxiv.org/abs/0802.1638>.
- Pollicott and Slipantschuk on validated high-precision bounds for leading
  transfer-operator eigenvalues and pressure:
  <https://doi.org/10.1088/1361-6544/ad6053>.
- Keller and Liverani on spectral stability under strong/weak perturbations:
  <https://www.numdam.org/item/ASNSP_1999_4_28_1_141_0/>.
- Blank, Keller, and Liverani on finite-rank approximation of transfer
  operators: <https://arxiv.org/abs/nlin/0104031>.
- Mitchell et al. on periodic-orbit transport calculations for the
  area-preserving Hénon map:
  <https://doi.org/10.1063/1.4998219>.
- Friedland and Ochs on Hausdorff dimension for hyperbolic area-preserving
  Hénon maps: <https://doi.org/10.3934/dcds.1998.4.405>.
- McCluskey and Manning, *Hausdorff dimension for horseshoes*, together with
  its official erratum; G000 must identify which unaffected theorem is used:
  <https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/hausdorff-dimension-for-horseshoes/D378674623E11E51F7CDA747E3EB93E3>
  and
  <https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/errata-to-hausdorff-dimension-for-horseshoes/914EF3D524EEAA933D6903D0148BE871>.
- Jenkinson and Pollicott on rigorous effective Hausdorff-dimension bounds via
  transfer operators: <https://arxiv.org/abs/1611.09276>.
- Parry and Pollicott on zeta functions and the prime-orbit theorem for
  hyperbolic dynamics:
  <https://annals.math.princeton.edu/1983/118-3/p07>.
- General thermodynamic formalism and effective/validated numerics must be
  cited at theorem level in the manuscript; a standard abstract RPF theorem is
  not claimed as new.

The publication novelty must therefore be the explicit certified bridge from
the exact Hénon geometry to effective roof, cohomology, finite-memory, and root
errors. Merely assembling a transfer matrix is not novel.

G000 must test that the proposed **certified local-Hénon dimension interval**
is more than a routine application of the listed validated methods and must
name the exact surface-basic-set dimension theorem used. If it is not, either
a reusable geometry-to-operator-to-dimension certificate theorem or the
fixed-contour determinant theorem becomes compulsory.

The theorem ledger must also state whether the dimension theorem is local on
a noncompact surface. If it assumes a compact ambient surface, the project
must certify an extension agreeing with \(H_6\) on a neighborhood of the
isolating set. The stable Bowen convention must begin with \(H_6^{-1}\) along
\(E^s\) and record the exact reindexing to symbolic \(\sigma\)-pressure.

## Separation from the deferred quantum route

Direct quantizations of area-preserving/Hénon maps and their semiclassical
analysis already have substantial prior art, including:

- Fornæss--Weickert, unitary quantized Hénon maps:
  <https://doi.org/10.3934/dcds.2000.6.723>;
- Weickert, spectral properties of the quantized Hénon family:
  <https://doi.org/10.1090/S0002-9947-04-03475-0>;
- Helleman, quantum levels of area-preserving maps:
  <https://doi.org/10.1016/S0167-2789(98)90014-8>;
- Shudo--Ikeda on quantum Hénon/Stokes structures:
  <https://doi.org/10.1088/0951-7715/21/8/007> and
  <https://doi.org/10.1088/0951-7715/29/2/375>.

That audit prevents direct quantization from being a default next paper. The
quantum trace project is now candidate HCS-C09, and the Ruelle project makes no
quantum-spectrum claim.

## Non-claims locked by this audit

- Paper 5's \(a\simeq1.00561\) is not treated as a certified first tangency.
- \(a\simeq1.02\) is not treated as a globally hyperbolic or pure-saddle
  regime.
- The \(H_6\) local survivor is not the full horseshoe or bounded repeller.
- A Hölder-space quasi-compact operator is not automatically nuclear.
- Finite-section complex roots are not infinite determinant zeros.
- No arithmetic correspondence follows from non-lattice behavior.
