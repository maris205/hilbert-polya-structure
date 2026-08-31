# Batch review: HCS-C264–HCS-C268

## Release basis

This review is extracted from the five final release manifests, not from an
earlier draft or batch plan.  Every package is `RELEASE_COMPLETE`, is bound to
source commit `a24c701881d22a4e49eaa2a44b94395c3c540b3d`, evaluator v0.2.0
SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
fixed epoch `1788048000`, and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  Each package closes 27 manifest payloads plus
its self-excluded manifest, retains three substantively different PDF rounds,
uses two fresh builds per round, and makes the final PDF byte-identical to
round 2.

Across the batch, the independent checkers close 245,718 assertions, SymPy
closes 2,736 checks, and hostile testing rejects 121/121 changes.  The evidence
files contain 2,527,934 bytes.  The five final papers total 12 pages and report
103 embedded/subset font instances across their independent PDFs.  These sums
are release-accounting totals; heterogeneous row and cell types are not
collapsed into a scientifically meaningless single observation count.

## Five theorem-scale advances

### HCS-C264 — finite abelian power maps

The package classifies every power map on the frozen finite-abelian corpus as
a periodic automorphism factor carrying all cycles and a uniform nilpotent
rooted tree attached to every periodic vertex.  It closes fixed and primitive
counts, the finite source dynamical zeta function, exact tail layers and
saturation height, and the complete full-function Koopman characteristic and
zero-Jordan atlas.  The constant-map and identity faces are separated rather
than hidden in a singular normalization.

Evidence scale: 646 cases over 19 exponents and 34 group types; 21,280 group
elements; 1,320 fixed-point cells; 933 cycle-factor cells; 1,132 tail-layer
cells; 485 zero-Jordan cells; 34 constant-boundary cases and 34 identity cases.
The evidence is 712,715 bytes.  The independent checker closes 202,656
assertions, SymPy closes 1,029 checks, and the repaired-hash hostile gate
rejects 33/33 changes.  The final paper has 2 pages and 22 embedded/subset
fonts.

Release-integrity repair: the sole primary-source item had previously been a
bibliography-only ghost reference.  The final revision cites it in the body at
its exact lineage role, while every displayed theorem remains proved locally;
no theorem is imported from that citation.  This repair is present in the
final PDF `d3d604ea…` and final manifest `f2bf73c…` recorded below.

Route-A verdict: `ROUTE_A_PARTIAL`, Route B disabled,
`(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL,
A4_FORMAL_HINT)`.

### HCS-C265 — stationary exponential Hawkes process

The package closes the joint affine transform of intensity and counts, the
stationary Laplace law and all moments, and keeps three covariance objects
distinct: intensity covariance, the off-diagonal counting covariance, and the
counting covariance measure with its diagonal Dirac mass.  It further closes
the Bartlett spectrum with its Fourier convention, finite-window variance,
Borel cluster law, and stability/boundary faces.

Evidence scale: 320 stable cases; 3,520 moment cells; 3,200 window cells; 160
cluster rows and 6 boundary rows.  The evidence is 376,531 bytes.  The
independent checker closes 27,893 assertions, SymPy closes 1,304 checks, and
hostile testing rejects 28/28 changes: 27 semantic mutations with a repaired
payload hash plus one stale-hash control.  Attacks cover the predictable
pre-jump convention, Fourier normalization, affine/Laplace equations, all
three covariance objects, spectrum, moments, window coefficients, cluster
data, route locks, and source locks.  The final paper has 3 pages and 21
embedded/subset fonts.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`.

### HCS-C266 — skew Brownian interface

For the zero-drift, symmetric-local-time owner, the package closes the image
kernel, generator interface condition, speed-symmetric semigroup, resolvent,
two-sided scale exits, both discounted exit transforms, unequal-endpoint mean
exit time, and the generalized-arcsine occupation law with endpoint faces.
It does not claim drifted, sticky, or unequal-diffusivity interfaces.

Evidence scale: 275 regression rows comprising 135 kernel rows, 6
Chapman–Kolmogorov rows, 9 speed-symmetry rows, 18 resolvent rows, 50 exit rows,
54 exit-transform rows, and 3 occupation rows.  The evidence is 68,565 bytes.
The independent checker closes 963 assertions, SymPy closes 133 checks, and
hostile testing rejects 16/16 changes, including repaired-hash attacks on the
local-time convention, interface ratio, reference measure, kernel, exits,
occupation mean, route locks, and claim firewall.  The final paper has 3 pages
and 21 embedded/subset fonts.

Final textual and source-history repair:

1. The resolvent proof now states the source derivative jump as `-2`, so the
   generator factor `-1/2` produces the unit delta.
2. Two stale equation-number cross-references were repaired.  Together with
   the normalization sentence, these are the three corrected body defects.
3. The final paper incorporates the 2011 correction
   (`doi:10.1214/11-AAP775`) and the 2024 second errata
   (`doi:10.1214/24-AAP2106`) in the source history.
4. No corrected multivariate-density formula is imported: the certificate's
   zero-drift occupation density is derived independently from a stable-
   `1/2` ratio and regression-checked.

These repairs are bound into final PDF `eaeabde9…` and final manifest
`9fd08354…` below.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`.

### HCS-C267 — Wannier–Stark lattice

For `(H psi)_n=Fn psi_n-J(psi_{n+1}+psi_{n-1})` on `ell^2(Z)`, `F != 0`, the
package proves the periodic Fourier-gauge equivalence, simple pure-point
ladder `F Z`, complete Bessel eigenbasis, exact propagator, and least full-space
return `2pi/|F|`.  It adds the exact delta-source Bessel shell and second
moment, proves that every time propagator is noncompact and in no finite
Schatten class, and proves that the resolvent is in `S_p` exactly for `p>1`
and is not trace class.  The `J=0` face and changed-owner `F=0` free lattice
are explicit.

Evidence scale: 210 parameter-time rows; 1,050 kernel cells; 5,250 shell cells;
1,890 eigen cells; 1,248,266 evidence bytes.  The independent checker closes
12,335 assertions, including direct Schrödinger residuals fixing phase and
Bessel-index signs; SymPy closes 142 checks.  All 20/20 repaired-hash hostile
mutations are rejected, including attacks on phase, shell, moment, eigenvalue,
minimal period, compactness, Schatten threshold, trace class, and route locks.
The final paper has 2 pages and 21 embedded/subset fonts.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`.

### HCS-C268 — constant electromagnetic Lorentz flow

With Minkowski metric `diag(1,-1,-1,-1)`, the package freezes the mixed-tensor
sign convention giving `E+v cross B`, proves `A^T eta+eta A=0`, and factors
`chi_A(z)=(z^2-a^2)(z^2+b^2)`.  It constructs the hyperbolic and rotational
projectors, exact exponential, exact position integral, Lorentz-norm and
determinant invariants, and the sharp proper-time velocity-period criterion.
It distinguishes periodic velocity from physical-worldline closure, closes
generic/electric-like/magnetic-like/zero regimes, and handles the nonzero null
field by `A^3=0 != A^2` with polynomial exponential and integral.

Evidence scale: 12 field cases, 48 proper-time samples, 1,536 exponential and
integral cells, and 121,857 evidence bytes.  The independent checker closes
1,871 assertions using exact characteristic/Lie/null identities and direct
matrix-exponential/augmented-integral comparisons; SymPy closes 128 checks.
All 24/24 repaired-hash hostile mutations are rejected, including invariant
sign, projector swap, null truncation, proper-time/coordinate-time confusion,
false closed-worldline, period, cross-product sign, and route attacks.  The
final paper has 2 pages and 18 embedded/subset fonts.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`.

## Exact release hashes

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C264 | `49361eea2b980df326258c854cb6a2c95adb9256b77b73ea130d04c0ea667228` | `9a0a03dff8c93f0e1e6a17cf40795f6132f2ebc5601d96dca74bd80e00b0dc4f` | `21252916e5cc1074b2f4eb2ac55c4c171dd2f54f251febeb19a1a758a616756b` | `d3d604ea273a27c1286463b23e07ab7bda78895fd5d998a281800343a2aefc3a` | `f2bf73c353bf611612747f12d4efd078d02de79378078b962691403d95ff1271` |
| C265 | `0279c47f770a143f7dffc17a3ec5ee8c340044fec93bde7f7c2c00297644ceff` | `b030f6146a351a7b1bfc735e752ab30f24dc60d90135a87e9600ad2255db603e` | `3f08ebc6287720f72655c6628ae13111ea212ff3286d57cd52c8fd3a9a05b4c8` | `3c0283170bb6cf7d807e53fbcd814b268c59670649726200e0dcc9d44a98bc24` | `aadf727563c4305a28f319a11f0c729ee9376a492de7fe30f59225bc81345654` |
| C266 | `5bd9602bec64332a2bce324cdec758e83ac46fcdf15b3664fb285a7f56a68d4e` | `333752ccf96062155172a5a7e4e0903b060df49f05fff221a92cd347975dd547` | `8f941766e6a9dd981bf28972a675e91ea816f2c6b5ea38844b9e7c2371eed920` | `eaeabde91cd9e40e80222a85e913e0706c1a9d0a548318d09a054b515a928ca3` | `9fd0835457c39465abf3081d307274a6447b6ae393eea692cd94b133e68180f6` |
| C267 | `44bc9f241c34ca2bca666afd54d5e4cc23e7a558376d6f54d94d05928b44f0e6` | `3e394dcec95bcd4a111eca9f0075179ff751a9280cfa12af4f608e4b7ee689f5` | `e1b1f682df03ebdc755349ad709de4f6566dc8d5efc9a34e55c2ce23f2865104` | `83c5a7eb7e17e770251ed769104c287e912f5a0909d8092e0926f42f472b3862` | `a2e405471520516757e89386cd8d1302860f4dafe7244404534f937e13e8d3db` |
| C268 | `ca8f58ee1df391f1af7c46ab6075a7add38c36db9701d11f3922599ea424e7dc` | `6af4f2ccf1e5bbb286c204a937ff46ea5de9523ac157398493ca57b6114e198e` | `b8bcc8f73fcc86cca88967c09532c559c469b40ec207a78b294eaafa4da77256` | `1076dfc4469cd42aa86a2addc1bd757ebb5139d2b633d5c1a7c761bcf0db180a` | `8a7d0d578c2c5fd4f4537ab8f9addab0042efd41ac1e203b50a67ec4d25ef2df` |

For every row, the three retained round hashes are distinct and the final PDF
hash equals the round-2 hash.  All five manifests report deterministic fresh
build, embedded/subset-font, settled-log/text/visual, replay, mutation, and
manifest-hash gates as `PASS`; the target-operator/Route-B gate is explicitly
`NOT_CLAIMED` rather than silently inferred.

## Claim firewall and batch verdict

The firewall is common and literal:
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No package claims a target arithmetic local
datum, bad Euler factor, root number, automorphy statement, target divisor,
functional equation, or Hilbert–Pólya identification.  In particular:

- C264's zeta function is the finite **source dynamical** zeta function, and
  its finite Koopman composition operator is generally nonnormal.
- C265's Bartlett spectrum is a source point-process spectrum, not a target
  divisor or Euler product; its Markov generator is not promoted to a target
  operator.
- C266's speed-symmetric Markov generator is not a Hilbert–Pólya operator,
  and finite quadrature is only a regression oracle.
- C267's natural lattice Hamiltonian earns `A4_NATURAL_QUANTIZATION`, but is
  not identified with a target Hilbert–Pólya operator; finite cells do not
  prove the infinite-dimensional statements.
- C268's Lorentz Lie-algebra functional calculus is only a formal structural
  hint; proper-time velocity periodicity is not a closed physical worldline.

Workspace ownership is not literature priority.  Finite enumeration,
high-precision evaluation, and numerical matrix comparisons are explicitly
bounded regression receipts; the all-parameter conclusions are proved in the
theorem packages and papers.  Route B is disabled in all five manifests.

The batch therefore records one partial Route-A result, C264, because it has
an analytic primitive-cycle/zeta clock but still fails target-data and
target-divisor matching.  C265–C268 are conservatively
`ROUTE_A_REJECTED`.  No partial or rejected verdict is upgraded by a source
zeta, stochastic spectrum, natural Hamiltonian, or Lorentz generator.
