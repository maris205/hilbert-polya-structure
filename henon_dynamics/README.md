# Hilbert–Pólya dynamical structure exploration

This directory is the continuously updated Hénon-dynamics research track of
the Hilbert–Pólya Structure Exploration project.  It starts from the original
area-preserving Hénon manuscript, but treats every proposed bridge to
arithmetic or spectral structure as a hypothesis to be tested rather than an
assumption.

The working style is breadth-first:

```text
candidate dynamics
    -> exact periodic/symbolic structure
    -> weighted dynamical zeta
    -> transfer/operator test
    -> Route-A or Route-B decision
```

Positive constructions, obstructions, and well-scoped failures are all kept.
Chronological products are preserved in non-autonomous systems; they are not
replaced by averaged transition matrices.

## Entry points

- [`propose.md`](propose.md) — research framework and workflow.
- [`docs/prior_work/README.md`](docs/prior_work/README.md) — earlier papers and
  experiments.
- [`docs/related_programs/README.md`](docs/related_programs/README.md) — related
  dynamical-zeta and transfer-operator programs.
- [`docs/candidate_registry.md`](docs/candidate_registry.md) — candidate and
  closure registry.
- [`docs/obstruction_registry.md`](docs/obstruction_registry.md) — reusable
  no-go mechanisms.
- [`next_paper_henon_candidate_search/`](next_paper_henon_candidate_search/) —
  breadth-first candidate generation and paper planning.
- [`skills/`](skills/) — Route-A and Route-B evaluation rules used by this
  research track.

The foundational local source is
[`5-An Area-Preserving Henon-Map Model.pdf`](docs/prior_work/papers/5-An%20Area-Preserving%20Henon-Map%20Model.pdf).

## Current theorem packages

| Project | Main result | Hilbert–Pólya status |
|---|---|---|
| [`henon_instability_roof_zeta/`](henon_instability_roof_zeta/) | Certified Hénon survivor and instability-roof clock | Current HP gate negative |
| [`henon_pinning_trace_obstruction/`](henon_pinning_trace_obstruction/) | Exact pinning-kernel and sign obstructions | Route-A rejected |
| [`henon_frobenius_scheme_obstruction/`](henon_frobenius_scheme_obstruction/) | Fixed-period Frobenius/local-zeta collapse | Scoped obstruction |
| [`henon_dihedral_chronology_obstruction/`](henon_dihedral_chronology_obstruction/) | Loss of chronology under coarse dihedral quotienting | Scoped obstruction |
| [`fibonacci_trace_map_clock_obstruction/`](fibonacci_trace_map_clock_obstruction/) | Trace-map clock and analytic-germ obstructions | Route-A rejected |
| [`s_integer_solenoid_chronology_zeta/`](s_integer_solenoid_chronology_zeta/) | Same-Parikh returns with rational versus natural-boundary zeta; full-zeta continuation | Structural theorem; Route-A rejected |
| [`nonabelian_voltage_zeta_obstruction/`](nonabelian_voltage_zeta_obstruction/) | Order collapse, finite-roof zero density, and exact-conductor branch return | Scoped obstruction; Route-A rejected |
| [`s_arithmetic_height_clock_obstruction/`](s_arithmetic_height_clock_obstruction/) | Explicit real/tree clock, near-wall divergence, canonical Weil height, and bounded-Hecke Weyl obstruction | Worked arithmetic example; Route-A rejected |
| [`modular_scattering_clock_obstruction/`](modular_scattering_clock_obstruction/) | Modular open-channel zeta arithmetic, denominator-only repetition no-go, and stable Selberg closure | Scoped obstruction; Route-A rejected |
| [`modular_open_trace_obstruction/`](modular_open_trace_obstruction/) | Algebraic endpoint coboundary, full-boundary Selberg periods, commuting squarefree scattering channels, and projector scope boundary | Scoped obstruction; Route-A rejected |
| [`henon_period7_frobenius_curve/`](henon_period7_frobenius_curve/) | Generic Hénon seven-cycle, degree-14 oriented time lift, genus-three scalar quotient, and finite-prime candidates | Route-A exploratory |
| [`henon_period7_dihedral_cover/`](henon_period7_dihedral_cover/) | Genus-eight \(D_7\) closure, chronology-induced real multiplication, and selected-prime local factors | Route-A exploratory |
| [`henon_chiral_chronology_threshold/`](henon_chiral_chronology_threshold/) | Genus-one period-six \(D_6\) cover, \(H^1\)-chronology collapse, scoped \(n=7\) threshold, and lower-period marker shadow | Route-A exploratory |
| [`henon_time_ordered_ruelle_cocycle/`](henon_time_ordered_ruelle_cocycle/) | Common switched survivor; convergent instability Euler product; common complex/projective domains; orbitwise scalar-denominator no-go | Route-A exploratory |
| [`henon_graded_ruelle_complex/`](henon_graded_ruelle_complex/) | Corrected \(\mathbb C^3\) cross map, exact residue parity, and explicit unresolved nuclear/all-word gates | Conditional blueprint; C22 closed |
| [`henon_adelic_lefschetz_ramification/`](henon_adelic_lefschetz_ramification/) | Exact fixed-algebra chronology certificates and cyclic-resultant collapse of every fixed-word tower | Scoped negative result; C23 closed |

## Latest large-gate closures: HCS-C22G and HCS-C23

The C22 operator lineage is closed honestly at a conditional blueprint. Its
corrected three-dimensional cross map proves the one-step domain constants,
the block-residue identity, and the required parity shift \(k+1\). It does
**not** yet prove the all-word vector-kernel trace or an order-zero nuclear
factorization. Consequently

\[
D_{\rm inst}(z,s)
=\frac{D_1(z,s)D_3(z,s)}{D_0(z,s)D_2(z,s)}
\]

is a conditional consequence, not a theorem of this release. Filling the
remaining functional-analysis gates would be substantial, while the
mechanism itself is classical Ruelle--Rugh/Lefschetz machinery and supplies
no arithmetic primitive law, so the lineage is not pursued through smaller
operator variants.

HCS-C23 then treated the Lefschetz denominator as arithmetic ramification
data. For each chronological word \(w\), its fixed algebra is
canonically finite free of rank \(2^{|w|}\), and

\[
\Delta_{w,r}
=\operatorname{Norm}_{A_w/R}\det(I-D F_w^r)
\]

detects multiplier-one packets modulo degree-good primes. Finite
chronology separation passes twice:

\[
11\mid\Delta_{0000101,1},
\qquad
11\nmid\Delta_{0001001,1},
\]

for the certified same-bigram period-seven pair, while

\[
3\nmid\Delta_{00101011,1},
\qquad
3\mid\Delta_{00101101,1},
\]

for the same-trigram period-eight pair.  Explicit residue-degree-one
nontransverse fixed points witness the event sides; full quotient-algebra
rank proves the paired non-events over the algebraic closure. Thus Galois
packet norm does not erase chronological information.

The decisive negative is the exact identity

\[
\Delta_{w,r}
=\operatorname{Res}_X\!\left(P_w(X),X^r-1\right),
\qquad
P_w(X)=\operatorname{Norm}_{A_w/R}(X^2-t_wX+1).
\]

For every fixed word, the full repetition tower is therefore a classical
cyclic-resultant sequence. No exact cross-word, cross-period theorem was
available before opening the proposed broad ledger, so the
\(n\le10,r\le12,\ell\le251\) scan is cancelled and C23 closes. The finite
chronology theorem and exact code remain reusable infrastructure; no Euler
product is authorized.

- [C23 project overview](henon_adelic_lefschetz_ramification/README.md)
- [C23 derivation package](henon_adelic_lefschetz_ramification/DERIVATION_PACKAGE.md)
- [C23 closure/reopening criteria](henon_adelic_lefschetz_ramification/EXPERIMENT_PLAN.md)
- [C23 exact certificate](henon_adelic_lefschetz_ramification/results/c23_first_gate_certificate.json)
- [C23 independent check](henon_adelic_lefschetz_ramification/results/c23_first_gate_independent_check.json)
- [C22G audited conditional blueprint](henon_graded_ruelle_complex/THEOREM_PACKAGE.md)
- [C22G compiled note](henon_graded_ruelle_complex/paper/main.pdf)

Reproduce both exact regression packages with:

```bash
cd henon_graded_ruelle_complex && ./code/run_c22g.sh
cd ../henon_adelic_lefschetz_ramification && ./code/run_c23.sh
```

## Next big system switch: HCS-C24 source lock

No further Hénon ledger is active. The proposed next one-round gate changes
the dynamical form to a Rauzy--Veech--Zorich return system with the
chronological Kontsevich--Zorich homology cocycle and its metaplectic unitary
fibre. Its first target is an all-period compactness obstruction, not a
low-period spectral fit: if one nonzero branch compression is
\(K_h\otimes U_h\) with \(U_h\) infinite-dimensional unitary, the ordinary
Fredholm route is noncompact and closes immediately.

The exact Rauzy component, homology convention, acceleration, roof, and
metaplectic lift must pass the primary-source lock before HCS-C24 becomes a
testable candidate. Heat regularization and finite oscillator truncations are
forbidden repairs.

- [HCS-C24 source-lock roadmap](docs/hcs_c24_system_switch.md)

## Predecessor result: HCS-C22

The Paper-5-coordinate maps

\[
H_a(q,p)=(1-aq^2-p,q),
\qquad a\in\{59/10,61/10\},
\]

now have one exact common four-box survivor for every chronological binary
schedule.  The signed-root contraction satisfies
\(\theta=\sqrt{240/1003}<0.49\), the common covering margin is \(7/720\),
and the binary skew product is conjugate to
\(\Sigma_2\times\Sigma_A\) with entropy \(\log(2\varphi)\).

Complete local instability-sector coefficients distinguish the minimal
tested non-dihedral parameter words with identical cyclic bigram and trigram
ledgers:

\[
Q_{0000101}(1)-Q_{0001001}(1)
\approx-1.37085831069617\times10^{-8},
\]

\[
Q_{00101011}(1)-Q_{00101101}(1)
\approx 1.70852115874693\times10^{-9}.
\]

All 29 and 49 state branches per sector are included in exact-rational
interval certificates.  The result is finite and scoped: it defeats
parameter-only cyclic statistics through trigram order, not every
finite-memory potential.

The complementary global theorem is negative.  Every nonzero length-\(n\)
protocol has cyclic fixed-scheme length \(2^n\), and a Hill identity plus
global residues makes the unit-numerator all-complex signed residue
determinant exactly one.  The formal bare global scheme zeta is
\((1-4z)^{-1}\).  Ordinary pointwise flat-determinant equality additionally
requires all-repetition nondegeneracy; local real absolute/instability weights
are not killed by this residue theorem.

The intrinsic instability determinant is now rigorous in a nonzero domain.
The all-period multiplier bounds are

\[
E^2=\frac{129299641}{14112000},
\qquad
U^2=\frac{11420060341}{189778176},
\]

and normal convergence holds whenever

\[
2\varphi|z|\chi(\Re s)<1.
\]

At \(s=1\), this gives \(|z|<0.9353771139\ldots\).  Both Hénon letters
also share strict complex base-pinning and projective slope domains.  The
oriented instability factor has a common principal logarithm, and every base
periodic orbit has exactly one lifted unstable periodic point in the slope
domain.

The natural orbitwise scalar geometric route nevertheless closes exactly.  A
scalar pinning trace carries a fixed-point denominator, and termwise
primitive/double compatibility would require

\[
|\det(I-M^2)|=|\det(I-M)|^2,
\]

which fails for every area-preserving saddle.  This leaves aggregate
same-period compensation unexcluded.  The authorized large-step continuation
is a different dynamical form: a projective, exterior-degree
Ruelle--Lefschetz complex with an alternating supertrace.

The formal verdict is
**(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)** with overall status
**ROUTE_A_EXPLORATORY**.  T4 and the complex/projective geometry now pass;
the orbitwise scalar T5 route is refuted.  The graded nuclear/supertrace gate
is the next and final authorized continuation of this lineage.

- [Project overview](henon_time_ordered_ruelle_cocycle/README.md)
- [Derivation package](henon_time_ordered_ruelle_cocycle/DERIVATION_PACKAGE.md)
- [T4 and orbitwise scalar-T5 derivation](henon_time_ordered_ruelle_cocycle/T4_T5_DERIVATION.md)
- [Graded pivot roadmap](henon_time_ordered_ruelle_cocycle/GRADED_PIVOT_ROADMAP.md)
- [Research synthesis](henon_time_ordered_ruelle_cocycle/RESEARCH_SYNTHESIS.md)
- [Exact certificate](henon_time_ordered_ruelle_cocycle/results/c22_certificate.json)
- [Independent check](henon_time_ordered_ruelle_cocycle/results/c22_independent_check.json)
- [T4/orbitwise-scalar certificate](henon_time_ordered_ruelle_cocycle/results/c22_t4_certificate.json)
- [T4/orbitwise-scalar independent check](henon_time_ordered_ruelle_cocycle/results/c22_t4_independent_check.json)
- [Current Route-A record](henon_time_ordered_ruelle_cocycle/evaluations/route_a/hcs_c22/20260809T081750Z.yaml)

Reproduce the frozen result with:

```bash
cd henon_time_ordered_ruelle_cocycle
python -m pip install -r requirements.txt
./code/run_c22.sh
./code/run_c22_t4.sh
sha256sum -c results/ARTIFACT_HASHES.sha256
```

## Predecessor result: HCS-C21

The published period-six chiral doublet now has a fully certified ordered
geometry.  Its twelve-state ordered-edge normalization is a connected
genus-one $D_6$ splitting curve, with $D_6$ of order twelve.  Point-level
Hénon time has exact order six, yet its action on weight-one cohomology is
completely trivial:

\[
g(E_6)=1,
\qquad
\tau^*|_{H^1(E_6)}=1.
\]

By contrast, the byte-locked HCS-C20 period-seven component has genus eight
and a twelve-dimensional nontrivial time sector.  Thus, among
source-identified and repository-certified chiral ordered components through
period seven, the first period at which at least one certified component has
nontrivial weight-one chronology is seven.  This is an existential scoped
threshold, not a classification of the saturated period-seven scheme.

A tempting period-six/period-seven arithmetic coincidence also collapses.
The period-six reversible marker and period-seven chiral marker both descend
from the fixed-point marker:

\[
D^{\mathrm{mark}}_6(s_6)=4D_1(s_6/2),
\qquad
C^{\mathrm{mark}}_7(s_7)=D_1(s_7-2).
\]

Their common field $\mathbb Q(A,\sqrt{A+1})$ is therefore a period-one
shadow, not a primitive chronology-preserving Hecke bridge.  The Route-A
tuple remains
**(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)**: no all-period repetition
law, Fredholm determinant, Riemann divisor, or Hilbert--Pólya operator has
been constructed.

- [Project overview](henon_chiral_chronology_threshold/README.md)
- [Derivation package](henon_chiral_chronology_threshold/DERIVATION_PACKAGE.md)
- [Source audit](henon_chiral_chronology_threshold/SOURCE_AUDIT.md)
- [Research synthesis](henon_chiral_chronology_threshold/RESEARCH_SYNTHESIS.md)
- [Exact certificate](henon_chiral_chronology_threshold/results/c21_certificate.json)
- [Independent check](henon_chiral_chronology_threshold/results/c21_independent_check.json)
- [Route-A record](henon_chiral_chronology_threshold/evaluations/route_a/hcs_c21/20260808T134051Z.yaml)

Reproduce the compact artifacts with:

~~~bash
cd henon_chiral_chronology_threshold
python code/c21_producer.py --output results/c21_certificate.json
python code/c21_independent_check.py \
  --certificate results/c21_certificate.json \
  --output results/c21_independent_check.json
python -m unittest discover -s code -p 'test_c21.py' -v
~~~

## Predecessor result: HCS-C20

The ordered-edge lift of the adopted period-seven septic is now proved to be
the connected genus-eight \(D_7\) splitting curve.  Its rotation quotient is
the genus-two discriminant curve
\[
B:w^2=Q_6(\sigma),
\]
its scalar reflection quotient is the genus-three HCS-C19 curve, and the
cyclic map \(E\to B\) is unramified of degree seven.

Hénon chronology induces a Rosati-self-adjoint correspondence on
\(\operatorname{Jac}(C)\) with exact minimal polynomial
\[
T^3+T^2-2T-1,
\]
so \(\mathbb Q(\zeta_7+\zeta_7^{-1})\) embeds in its rational endomorphism
algebra.  The quotient-character identity gives
\[
\operatorname{Jac}(E)\sim_{\mathbb Q}
\operatorname{Jac}(B)\times\operatorname{Jac}(C)^2.
\]

A selected-prime theorem closes HCS-C19's arithmetic caveat at
\(p=5,11,13\).  Nontrivial vertical \(C_7\) inertia would force
\(\mu_7\subset\mathbb F_p\), purity extends the cover finite étale, and a
two-chart normalization plus irreducible specializations identifies the
smooth quotient with the normalization of the plane septic after reduction.
Independent extension-field enumeration then certifies the displayed
\(L_C\) and \(L_E=L_B L_C^2\) as genuine local Hasse--Weil factors at exactly
those primes.

The Route-A verdict remains
**(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)**.  The result supplies real
arithmetic and self-adjoint structure, but it is locked to \(n=7\);
ordinary cohomology adds no eigenvalues beyond \(B\) and two copies of \(C\),
and no cross-period Fredholm determinant or Riemann divisor exists.

- [Project overview](henon_period7_dihedral_cover/README.md)
- [Compiled paper](henon_period7_dihedral_cover/paper/main.pdf)
- [Good-reduction theorem](henon_period7_dihedral_cover/SELECTED_PRIME_GOOD_REDUCTION.md)
- [Derivation package](henon_period7_dihedral_cover/DERIVATION_PACKAGE.md)
- [Exact certificate](henon_period7_dihedral_cover/results/c20_certificate.json)
- [Independent check](henon_period7_dihedral_cover/results/c20_independent_check.json)
- [Route-A record](henon_period7_dihedral_cover/evaluations/route_a/hcs_c20/20260808T065044Z.yaml)

Reproduce the compact release artifacts with:

```bash
cd henon_period7_dihedral_cover
python code/c20_producer.py --output results/c20_certificate.json
python code/c20_independent_check.py \
  --certificate results/c20_certificate.json \
  --output results/c20_independent_check.json
python -m unittest discover -s code -p 'test_c20.py' -v
```

## Predecessor result: HCS-C19

The latest paper returns to the original area-preserving Hénon program and
studies a corrected period-seven chiral coordinate equation.  An exact
\(\mathbb F_{103}\) orbit witness shows that the literal constant term in
Endler--Gallas Eq. (16) is inconsistent with the stated dynamics; the project
therefore records an adopted placement of the constant that passes that
fibre.  No official publisher erratum is claimed.

\[
\operatorname{Disc}_xP=(4\sigma-9)^2Q_6(\sigma)^3.
\]

The six roots of the irreducible sextic \(Q_6\) each support three simple
ramification points.  The remaining finite discriminant point is an ordinary
node and infinity splits into seven unramified normalization branches.
Riemann--Hurwitz and an independent plane-septic delta calculation both give
\(g=3\) for the explicit characteristic-zero septic.  Exact affine counts and
a frozen branch correction at \(p=5,11,13\) produce three reciprocal
degree-six candidate numerators; a second implementation reproduces all
counts and a sealed \(p=5,r=4\) prediction.  Simultaneous normalization and
good reduction at these primes were left open in HCS-C19 and are closed by
HCS-C20 above.

The decisive generic calculation takes the gcd in \(y\) of
\(P(\sigma,y)\) and \(P(\sigma,a-y^2-x)\) over
\(\mathbb Q(\sigma)[x]/(P)\).  It has degree two, and its neighbor roots sum
to \(a-x^2\).  Exact nondegeneracy plus prime-degree monodromy force one
seven-cycle.  The 14 ordered edges therefore carry

\[
\tau(x,y)=(a-x^2-y,x),\qquad \tau^7=1,
\]

together with time reversal.  This generically certifies the adopted septic
as a true Hénon period-seven carrier and restores the orientation lost on the
scalar genus-three quotient.

The Hilbert--Pólya verdict is exploratory but still far from positive:
**(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)**.  Hénon time is now genuine,
but period remains fixed at seven and the scalar candidate Frobenius rows are
not time sectors upstairs.  The next large step is the geometry of the
ordered-edge cover and joint
\(\#\operatorname{Fix}(\operatorname{Frob}_p^r\tau^s)\) data without
orientation averaging.

- [Project overview](henon_period7_frobenius_curve/README.md)
- [Compiled paper](henon_period7_frobenius_curve/paper/main.pdf)
- [Derivation package](henon_period7_frobenius_curve/DERIVATION_PACKAGE.md)
- [Source audit](henon_period7_frobenius_curve/SOURCE_AUDIT.md)
- [Neighbor correspondence](henon_period7_frobenius_curve/NEIGHBOR_CORRESPONDENCE.md)
- [Certificate producer](henon_period7_frobenius_curve/code/c19_producer.py)
- [Independent checker](henon_period7_frobenius_curve/code/c19_independent_check.py)
- [Latest Route-A record](henon_period7_frobenius_curve/evaluations/route_a/hcs_c19/20260808T060207Z.yaml)
- [Historical pre-lift Route-A record](henon_period7_frobenius_curve/evaluations/route_a/hcs_c19/20260808T051445Z.yaml)

Reproduce its frozen artifacts with:

```bash
cd henon_period7_frobenius_curve
python -m pip install -r requirements.txt
python code/c19_producer.py --output results
python code/c19_independent_check.py \
  --certificate results/c19_certificate.json \
  --output results/c19_independent_check.json
python code/c19_neighbor_correspondence.py \
  --output results/c19_neighbor_correspondence.json
python code/c19_neighbor_independent_check.py \
  --certificate results/c19_neighbor_correspondence.json \
  --output results/c19_neighbor_independent_check.json
python -m unittest discover -s code -p 'test_c19.py' -v
```

## Mirrored-data boundary

The related `henon_weighted_zeta` source, scripts, final paper, and compact
R058/R059 certificates are mirrored here.  Its large historical R052--R061
matrix/NPZ sweeps are deliberately not mirrored; the complete historical test
suite expects those local data assets and is therefore not a code-only CI
target.  The data-independent source tests can be run with:

```bash
cd docs/related_programs/henon_weighted_zeta
python -m pytest -q \
  tests/test_controls.py tests/test_geometry.py tests/test_homotopy.py \
  tests/test_interval_cover.py tests/test_operator.py tests/test_orbits.py \
  tests/test_precision.py tests/test_subdivided_cover.py tests/test_zeta.py
```

At the current snapshot this subset passes 45/45 tests.  Artifact-dependent
claims should instead be checked against the compact certificates and hashes
retained by their consuming theorem packages.

## Update discipline

When a research round reaches a meaningful stage:

1. add or update its project-level `README.md`;
2. keep exact code, compact result certificates, and independent checks;
3. append rather than overwrite formal Route-A evaluation records;
4. update the candidate, obstruction, and related-program registries;
5. state explicitly what is proved, what failed, and what remains open.

Regenerable caches, nested Git metadata, TeX auxiliary files, and bulky raw
array dumps are intentionally excluded from synchronization.  Papers,
source, compact certificates, and audit records remain versioned.

Last synchronized research snapshot: **2026-08-09**.
