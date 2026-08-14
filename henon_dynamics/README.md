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

## Batch research papers

henon_cubic_kummer_functorial_obstruction - C38 complete - Functorial three-channel Kummer lifts preserve the C37 gauge coboundary and have identity closed holonomy.
henon_kummer_character_divisor_obstruction - C39 complete - Every nonzero virtual cubic channel creates an interior all-prime zero/pole accumulation at s=1/2.
henon_kummer_schatten_clock_obstruction - C40 complete - Prime damping has a sharp Schatten threshold but introduces a noncanonical second clock absent from Kummer conductor data.
henon_cubic_cm_frobenius_bridge - C41 complete - The cubic channel admits an intrinsic j=0 CM elliptic Frobenius completion, but its L-function is not a Henon/Riemann determinant.
henon_cm_three_prime_supercancellation_obstruction - C42 complete - Three local primes force every finite Tate-plus-CM Riemann match to delete the cubic H1 factor.
henon_entropy_von_mangoldt_bridge - HCS-P43 complete - The intrinsic H6 entropy clock makes exact-period marked chronology asymptotic to cumulative von Mangoldt mass.
henon_instability_amplitude_overconvergence - HCS-P44 complete - Raw instability Euler factors have exact prime-power amplitudes but the full trace overconverges on the critical line.
henon_pressure_normalized_prime_orbit_bridge - HCS-P45 complete - Bowen-pressure normalization gives the same H6 survivor entropy one and a source-backed e^T/T prime-orbit law.
henon_integral_monodromy_units - HCS-P46 complete - Every all-period H6 monodromy trace is integral and every periodic multiplier is an algebraic unit.
henon_repetition_label_classification - HCS-P47 complete - Rational repetition-compatible scalar labels are exactly monomials, so H6 algebraic units cannot become rational primes.
henon_pressure_label_six_exponentials_obstruction - HCS-P48 complete - Three exact H6 multiplier fields and Six Exponentials rule out all-prime pressure labels for every common real exponent.
henon_cyclic_resultant_packet_obstruction - HCS-P49 complete - Full multiplier-field cyclic norms are forced squares, while trace-field Lehmer--Pierce sequences and ideal packets survive as collective arithmetic structures.
henon_tagged_prime_ideal_packet_assembly - HCS-P50 complete - Tagged trace-field prime-ideal packets assemble exactly at finite cutoff, while rational-prime pushforward has kernel rank 30 and merges incompatible residue clocks.
henon_abel_graded_all_orbit_packet_germ - HCS-P51 complete - The finite packet ledger extends to an all-primitive-orbit Banach-valued holomorphic germ, while one exact orbit forces radius one and divergence at the ungraded Abel boundary.
henon_totient_abel_boundary_escape - HCS-P52 complete - The exact period-four packet has a totient-driven Abel constant and Gamma(2,1) scaled-index profile, while its renormalized tagged divisor vectors have no norm or weak boundary.
henon_pressure_weighted_all_orbit_abel_law - HCS-P53 complete - Full multiplier Mahler heights govern a proved pressure-weighted all-orbit Abel boundary and joint pressure-height/Gamma product law in the certified safe half-plane.
henon_mahler_pressure_pole_galois_excess_gate - HCS-P54 complete - The physical Mahler summand reaches a proved pressure pole at s=1, while the positive nonphysical Galois excess becomes the exact thermodynamic completion gate.
henon_galois_excess_three_block_obstruction - HCS-P55 complete - Exact period-three through period-five block homology rejects every width-at-most-three Galois-excess potential, while width four interpolates the finite witness and leaves the all-period Hölder gate open.
henon_galois_excess_four_block_incidence_ladder - HCS-P56 complete - Two primitive orbit families give an exact all-width incidence ladder; its first new period-six field proves a width-at-most-four excess obstruction, while a determinant-one width-five minor isolates the remaining Hölder-asymptotic gate.

`P43`--`P56` are the unique registry aliases for the pressure/orbit lane.
The `P43`--`P47` project bundles retain legacy internal `HCS-C43`--`HCS-C47`
strings to preserve their published hashes; `P48`--`P56` were born
namespaced. The unqualified IDs `C43`--`C48` in this repository belong to
the full-kernel cubic lane listed in the theorem table below.

- [Pressure-lane Batch Review HCS-P43--P47](BATCH_REVIEW_C43_C47.md) — entropy mass, raw-clock
  obstruction, pressure normalization, integral monodromy, and the final
  rational-label classification.

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
| [henon_galois_excess_four_block_incidence_ladder/](henon_galois_excess_four_block_incidence_ladder/) | P56: the primitive families \(A_m=0^{m-2}21\) and \(B_m=0^{m-3}231\) satisfy an exact incidence relation for every width; the radical period-six member makes the width-four excess identity fail exactly, while a determinant-one width-five minor proves finite sharpness | Infinite symbolic regularity gate inside Route A; the one-sided Hölder discrepancy asymptotics, full Galois-weighted determinant and Route B remain open |
| [henon_galois_excess_three_block_obstruction/](henon_galois_excess_three_block_obstruction/) | P55: an exact width-three incidence relation among five primitive H6 cycles violates the corresponding Galois-excess identity; a unimodular width-four minor proves finite sharpness, and a one-sided exponential discrepancy condition identifies the genuine Hölder gate | Exact finite-memory obstruction inside Route A; unrestricted Hölder realization, the full Galois-weighted determinant and Route B remain open |
| [henon_mahler_pressure_pole_galois_excess_gate/](henon_mahler_pressure_pole_galois_excess_gate/) | P54: the P53 Mahler coefficient splits exactly into physical instability length plus nonnegative Galois excess; the physical primitive series has a source-backed simple pressure pole with residue \(3/(\pi^2h_*)\), while three exact orbits rule out scalar pressure retuning | First pressure-critical pole in this lane, scoped to the physical subsystem; Route A exploratory with physical A2 analytic determinant, full Galois-weighted A2 and Route B still open |
| [henon_pressure_weighted_all_orbit_abel_law/](henon_pressure_weighted_all_orbit_abel_law/) | P53: every orbit packet has leading coefficient \(\varphi(n)\log M(f_{\lambda_\gamma})/2\), and the Abel boundary interchanges with the complete pressure-weighted primitive-orbit sum; the joint limit is the pressure-height orbit law times Gamma\((2,1)\) | First pressure-weighted all-orbit packet boundary; Route A exploratory, A3 partial, pressure-critical continuation still open |
| [henon_totient_abel_boundary_escape/](henon_totient_abel_boundary_escape/) | P52: the exact period-four packet mass is \(\varphi(n)\log L/2+O_L(1)\), giving a scalar Abel constant and Gamma\((2,1)\) scaled-index escape profile; the tagged vectors have no norm or weak limit | First source-native packet boundary law; Route A exploratory, A3 partial, all-orbit boundary still open |
| [henon_abel_graded_all_orbit_packet_germ/](henon_abel_graded_all_orbit_packet_germ/) | P51: all primitive H6 cyclotomic packet divisors form a jointly holomorphic two-variable germ in a universal tagged Banach space; the period-four orbit has exact Abel radius one | First all-orbit arithmetic packet germ; Route A exploratory, A3 partial, raw boundary refuted |
| [henon_mu3_weight_clock_bifurcation/](henon_mu3_weight_clock_bifurcation/) | C51: the second, third, and fourth cohomological Hénon moments split uniformly into weight-zero and weight-one packets of total rank \(4^n-1\); their exact \(2/n\) Log-\(L\) extraction aligns only the leading odd rail and proves a Tate-invariant factorwise center bifurcation | Structural completion audit, weight--clock theorem, and scoped direct-packet obstruction; inherited continuation remains \(\Re s>1/5\), Route A exploratory |
| [henon_mu3_elliptic_resummation_fourth_moment/](henon_mu3_elliptic_resummation_fourth_moment/) | C50: explicit \(K=\mathbb Q(\sqrt{-3})\)-rational symmetries split the genus-four second-moment Jacobian as \(E_+^2\times E_-^2\) up to \(K\)-isogeny; modular resummation of that wall and a fourth-moment Fermat-sixfold/\((2,3)\)-fivefold cancellation extend the normalized Euler object and a tenth-order normalized-semifinite determinant to \(\Re s>1/5\) | Strongest current analytic continuation; Route A remains exploratory and A3 partial |
| [henon_mu3_fano_threefold_third_moment/](henon_mu3_fano_threefold_third_moment/) | C49: the third moment is an exact Fermat-fourfold/Fano-threefold Frobenius cancellation, extending the normalized Euler germ and an eighth-order normalized-semifinite determinant to \(\Re s>1/4\) | Previous third-moment advance; analytically extended by C50 |
| [henon_mu3_fixed_coefficient_field_obstruction/](henon_mu3_fixed_coefficient_field_obstruction/) | C44: every paired first Hénon moment generates the full real cyclotomic field, with degree \((p-1)/2\) for every split prime | Fixed-coefficient compatible-system repair rejected |
| [henon_mu3_galois_norm_rank_obstruction/](henon_mu3_galois_norm_rank_obstruction/) | C45: ordinary Galois norm has unbounded virtual rank, while its canonical normalized logarithmic root gives a holomorphic nonzero Euler germ on \(\Re s>1/2\) | Route-A exploratory analytic germ |
| [henon_mu3_normalized_root_branch_obstruction/](henon_mu3_normalized_root_branch_obstruction/) | C46: exact \(p=7\) norm has finite divisor orders \(\pm2\), forcing cubic branching of the normalized root | Ordinary determinant promotion rejected |
| [henon_mu3_normalized_trace_operator_gate/](henon_mu3_normalized_trace_operator_gate/) | C47: the normalized germ is exactly a fourth-order regularized graded determinant relative to the field-normalized semifinite trace, with three chronological counterterms | Positive A2 operator-category realization on \(\Re s>1/2\); not a classical Fredholm determinant |
| [henon_mu3_genus4_second_moment/](henon_mu3_genus4_second_moment/) | C48: the second moment is a genus-four Frobenius trace, extending the Euler germ and a sixth-order normalized-semifinite determinant to \(\Re s>1/3\) | Genus-four wall identified; its elliptic modular resummation is completed in C50 |
| [henon_mu3_augmented_euler_superproduct/](henon_mu3_augmented_euler_superproduct/) | C43: intrinsic order-three reversing Hénon symmetry, exact chronological augmentation Euler germ, complete split-prime coprimality controls through 73, and a first-prime conjugation obstruction | Positive A2 analytic germ; raw promotion rejected; finite Tate--CM repair closed; C44 fixed-field then Hankel-rank gate selected |
| [henon_homogeneous_boundary_index_obstruction/](henon_homogeneous_boundary_index_obstruction/) | Homogeneous cubic Hénon scaling cocycle, exact equivariant trivialization, zero pre-Poisson essential codimension, and non-VMO Hardy obstruction | Scalar anomaly Route-A rejected; nonscalar cubic grading selected |
| [henon_mellin_parity_obstruction/](henon_mellin_parity_obstruction/) | Reciprocal and critical-line-unitary H6 Mellin symbol with a certified off-critical strip divisor | Unrenormalized candidate Route-A rejected; homogeneous boundary-index pivot open |
| [adelic_henon_theta_route/](adelic_henon_theta_route/) | Global adelic H6 unitary, theta stabilizer, local noncompactness no-go, static rank-two range bound, and infinite scaling-orbit obstruction | Route-A exploratory; a scaling-covariant Poisson anomaly is the next big gate |
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
| [`rauzy_metaplectic_obstruction/`](rauzy_metaplectic_obstruction/) | Exact genus-two Rauzy chronology, fixed-vector character obstruction, and two metaplectic noncompactness theorems | Two realization classes closed; canonical analytic application open |
| [`agy_metaplectic_transfer_obstruction/`](agy_metaplectic_transfer_obstruction/) | All-length Rauzy matrix decoder and exact noncompactness on source-standard AGY vector-valued `C_b^1` and normalized `L^2` spaces | Ordinary determinant rejected; holomorphic/generalized trace open |
| [`agy_holomorphic_slice_obstruction/`](agy_holomorphic_slice_obstruction/) | Common complex AGY domain, scalar trace-class determinant with Perron-characteristic trace atoms, and same-domain oscillator noncompactness | Scalar determinant proved; literal infinite oscillator Route-A rejected |
| [`agy_finite_weil_determinant/`](agy_finite_weil_determinant/) | Fixed-prime finite-Weil Fredholm determinants, exact Legendre--Gauss traces, and class-function chronology collapse | Route-A exploratory; natural fixed-prime quantization, no global prime assembly |
| [`agy_prime_direct_sum_determinant/`](agy_prime_direct_sum_determinant/) | Sharp prime-Schatten phase diagram, ordinary Dirichlet-damped all-prime Fredholm determinant, and canonicality trilemma | Route-A exploratory; exact global determinant with an external second clock |
| [`rauzy_groupoid_identity_determinant/`](rauzy_groupoid_identity_determinant/) | Natural-extension trace-log no-go; exact C25/C26 identity-holonomy relations; nonconstant normalized finite-Weil groupoid determinant germ | Phase 2 certified; Route-A exploratory, Route B closed |
| [`rauzy_inverse_roof_trace_obstruction/`](rauzy_inverse_roof_trace_obstruction/) | All-phase positive-cone failure, inverse-time roof theorem, same-space nuclearity and isolated-flat-trace obstruction | C29-to-AGY promotion rejected; finite C29 graph germ retained |
| [`henon_bowen_pressure_gate/`](henon_bowen_pressure_gate/) | Exact full-cylinder Bowen-pressure bracket, adapted/Euclidean coboundary, and local Hausdorff dimension theorem | Positive signal pressure-consistent at certified resolution; arithmetic interpretation rejected |
| [`phase3_hcs_c32_artin_schreier_quantum_trace/`](phase3_hcs_c32_artin_schreier_quantum_trace/) | Exact Hénon Morse-germ collision with unequal Hill values and a source-certified local no-recovery theorem | Morse-local bridge stopped; global discriminant-monodromy gate open |
| [`phase3_hcs_c33_henon_action_collision_kummer/`](phase3_hcs_c33_henon_action_collision_kummer/) | Exact period-five equal-action node, \(S_9\) collision field, and nontrivial descended Hill--Kummer class | Positive fixed-period arithmetic theorem; Route-A rejected |
| [`henon_maxwell_hill_wreath_monodromy/`](henon_maxwell_hill_wreath_monodromy/) | Rank-nine conjugate Hill--Kummer module and full \(C_2\wr S_9\) Maxwell monodromy | Maximal fixed-period arithmetic theorem; Route-A rejected |

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

## Predecessor big-door result: HCS-C35 isolates the scaling-covariance gate

C35 leaves the fixed-period tower and puts the original area-preserving H6
map on one adelic Hilbert space:

\[
\mathcal U_H=\mathcal F_{\mathbb A}\mathcal M_{2q^3-q}.
\]

The restricted product is canonical because every finite spherical vacuum is
fixed. Adelic Poisson summation and rational triviality of the global
character give the exact nonlinear stabilizer

\[
\Theta\mathcal U_H=\Theta.
\]

On a transported Hénon-adapted domain this recovers the standard Tate/Connes
scaling range exactly. The simpler-parent control is therefore explicit:
the known Riemann divisor is inherited and cannot yet be credited to Hénon.

Two new theorems locate the correct escape. First, for every \(p>3\) and
\(m\ge0\),

\[
\int_{p^{-m}\mathbb Z_p}\psi_p(2x^3-x)\,dx=1.
\]

The normalized dilation tower then proves
\(\mathcal M_{P_6}-I\) is noncompact, killing a naive same-space relative
Fredholm determinant. Second, at one fixed phase the standard and chirped
test spaces are two hyperplanes with a common codimension-two kernel. If
their images extend to closed subspaces in a common Hilbert completion,
their static range projections consequently satisfy

\[
\operatorname{rank}(P_H-P_0)\le2.
\]

This bound is not a dynamical two-channel theorem. Under dilation the cubic
phase becomes

\[
P_a(x)=2a^3x^3-ax,
\]

and the boundary kernels attached to distinct positive \(a\) are linearly
independent already before applying the Poisson map. The naive promotion of
static rank two to finite-channel scattering is therefore refuted.

The exact Poisson defect formula nevertheless sends every fixed-scale
inversion defect into the same outgoing asymptotic mode \(|x|^{1/2}\). Its
Hilbert-space membership is unproved and its coefficient functional still
ranges over the infinite orbit, so this is a concrete compression mechanism
rather than a bounded finite-rank operator or determinant theorem.

The next RH gate is sharper and larger: construct a genuine scaling-site
Hénon bundle or crossed-product cocycle, then prove that Poisson
renormalization turns this infinite boundary orbit into a determinant-class
relative anomaly \(\Delta_H(s)\). Identity gives rigidity; failure of
determinant class closes the adelic H6 route; a nonconstant reciprocal,
zero-free anomaly would promote the same global object toward analytic
Route A.

The strict current tuple is
**(A1_WEAK, A2_FAIL, A3_PARTIAL_ANALYTIC_STRUCTURE,
A4_NATURAL_QUANTIZATION)** with overall **ROUTE_A_EXPLORATORY**. Route B is
not authorized.

- [C35 project overview](adelic_henon_theta_route/README.md)
- [C35 theorem package](adelic_henon_theta_route/THEOREM_PACKAGE.md)
- [C35 derivation package](adelic_henon_theta_route/DERIVATION_PACKAGE.md)
- [C35 exact certificate](adelic_henon_theta_route/results/c35_certificate.json)
- [C35 Route-A record](adelic_henon_theta_route/evaluations/route_a/HCS-C35/20260812T150757Z.yaml)

## Latest big-door result: HCS-C36 symmetry does not control the divisor

C36 executes the scaling gate by Mellin-diagonalizing the infinite H6
boundary orbit. In the forced parity basis, the formal scattering symbol
satisfies

\[
S_H(z)S_H(1-z)=I,
\qquad
S_H(1/2+it)^*S_H(1/2+it)=I
\]

exactly. The apparent Route-A symmetry is nevertheless insufficient. A
complex-ball/Rouché certificate proves one simple zero of the zeta-even
symbol in a radius-\(10^{-12}\) disc centered at

\[
0.7286922241147175+1.6054479123346985i.
\]

Mirror and odd factors, together with the natural linear parent, are
certified nonzero on the required discs, and direct Arb evaluation gives
\(\inf_D|\xi|>9/20\). Hence the unrenormalized determinant has a genuinely
additional off-critical pole--zero quartet in the open strip. The global Mellin
multiplier is also noncompact, so its pointwise determinant is not an
ordinary Fredholm determinant.

This closes the inhomogeneous H6 Mellin-scattering candidate and registers
HEN-O73: reciprocity plus critical-line unitarity does not imply an
RH-compatible divisor. The next large gate changes the dynamics to the
homogeneous area-preserving form \(H_0(q,p)=(-6q^2-p,q)\). Its Mellin symbol
is strip-safe; the decisive question is whether the Poisson boundary quotient
turns its ambient scaling coboundary into a nontrivial index/anomaly or
trivializes it exactly.

- [C36 theorem package](henon_mellin_parity_obstruction/THEOREM_PACKAGE.md)
- [C36 compiled note](henon_mellin_parity_obstruction/paper/main.pdf)
- [C36 interval certificate](henon_mellin_parity_obstruction/results/c36_certificate.json)

## Predecessor big-door result: HCS-C34 reaches full Maxwell--Hill wreath monodromy

C34 closes the principal arithmetic gate left open by C33.  Let \(L\) be
the \(S_9\) splitting field of the period-five equal-action collision
polynomial \(P_9\), and let \(\beta_1,\ldots,\beta_9\) be the conjugates of
the intrinsic two-branch Hill product.  An exact Newton polygon at \(p=19\)
produces a valuation parity row

\[
e_1+e_2.
\]

The full \(S_9\)-orbit of this row forces every square relation among the
nine conjugates into the all-ones line.  That final relation is excluded by
the exact rational square classes

\[
[N_{K/\mathbb Q}(\beta)]
=3\cdot13\cdot19\cdot41\cdot59,
\qquad
[\operatorname{Disc}(P_9)]
=13\cdot19\cdot41\cdot59.
\]

Hence the conjugate square classes have rank nine and

\[
\operatorname{Gal}\left(
L(\sqrt{\beta_1},\ldots,\sqrt{\beta_9})/\mathbb Q
\right)
=C_2\wr S_9,
\]

of order \(185794560\).  The proof explicitly avoids a bad-prime Dedekind
shortcut: it uses the \(19\)-adic Newton roots and Hill valuations directly.

This is a maximal fixed-period arithmetic theorem, not an all-period zeta or
Hilbert--Pólya construction.  The strict tuple remains
**(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)** with
**ROUTE_A_REJECTED**.

- [C34 overview](henon_maxwell_hill_wreath_monodromy/README.md)
- [C34 theorem package](henon_maxwell_hill_wreath_monodromy/THEOREM_PACKAGE.md)
- [C34 derivation package](henon_maxwell_hill_wreath_monodromy/DERIVATION_PACKAGE.md)
- [C34 exact certificate](henon_maxwell_hill_wreath_monodromy/results/c34_certificate.json)
- [C34 compiled paper](henon_maxwell_hill_wreath_monodromy/paper/main.pdf)

Reproduce with:

~~~bash
henon_maxwell_hill_wreath_monodromy/code/run_c34.sh
~~~

## Predecessor big-door result: HCS-C33 lifts the C32 collision to characteristic zero

C33 replaces the isolated-prime C32 event by an exact parameter-family
theorem.  The period-five cyclic action image has discriminant

\[
\operatorname{Disc}_c W_5
=2^{12}3^{30}A^{60}P_2^5P_5^3P_9^2,
\]

where the coprime degree-nine factor \(P_9\) has Galois group \(S_9\).  Over
\(K_9=\mathbb Q[A]/(P_9)\), its repeated action value comes from exactly two
distinct normalization points whose image is a transverse ordinary node.
Both points have exact period five and neither return map has multiplier
\(+1\) or \(-1\).

The two chronological Hill determinants descend through branch exchange as
\(N_H=h_1h_2\).  Their exact rational field norm is

\[
N_{K_9/\mathbb Q}(N_H)
=\frac{2^6\,13\,19^5\,41\,59^5\,5653^2}{3^5},
\]

so \(N_H\) is not a square in \(K_9\).  Thus \(u^2=N_H\) is a nontrivial
quadratic Kummer extension of the generic collision field.  The action curve
itself is birational to the known period-five marker cover; the new
information lies in its singular action embedding and intrinsic stability
decoration.

This is positive Hénon arithmetic structure, but it remains fixed-period.
The formal tuple is
**(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)** with
**ROUTE_A_REJECTED**.  No full Kummer wreath group, Picard--Lefschetz action,
all-period zeta, or self-adjoint operator is claimed.

- [C33 Phase-3 overview](phase3_hcs_c33_henon_action_collision_kummer/README.md)
- [C33 theorem package](phase3_hcs_c33_henon_action_collision_kummer/THEOREM_PACKAGE.md)
- [C33 exact certificate](phase3_hcs_c33_henon_action_collision_kummer/results/c33_kummer_certificate.json)
- [C33 compiled paper](phase3_hcs_c33_henon_action_collision_kummer/paper/main.pdf)

Reproduce the release with:

~~~bash
phase3_hcs_c33_henon_action_collision_kummer/code/run_c33.sh
~~~

## Predecessor big-door result: HCS-C32 closes Morse-local Hill recovery

C32 keeps the chronological H6 dynamics and replaces the exhausted scalar
pressure interpretation with a finite-field Artin--Schreier kernel.  Its
global rank/purity and finite-field unitarity are mathematically valid but
generic, so Phase 3 tested the one Hénon-specific possibility: whether an
isolated Morse vanishing-cycle factor retains the full Hill multiplier.

It does not.  Over \(\mathbb F_{61}\), the two primitive period-five cycles

\[
(12,12,40,27,40),
\qquad
(33,58,36,36,58)
\]

have the same action value \(45\).  Their Hessian/Hill determinants are \(44\)
and \(7\), but \(44/7=25^2\pmod{61}\), and an explicit
\(C\in\operatorname{GL}_5(\mathbb F_{61})\) satisfies

\[
C^{\mathsf T}B_1C=B_2.
\]

The henselian Morse lemma therefore makes the complete local function germs
and their standard Morse-local Fourier representations isomorphic.  The
local object sees the discriminant square class, not the chosen determinant
representative.  An independent permutation-cycle checker passes 14/14 exact
gates, the mutation suite passes 22/22 tests, and the full Phase-3 artifact
manifest verifies 19 files.

This is a scoped negative theorem, not a global Artin--Schreier no-go.  C33
subsequently opened the parameter-family equal-action discriminant rather
than extending the isolated-prime scan, and proved the characteristic-zero
node/Hill--Kummer theorem summarized above.

- [C32 Phase-1 question](phase1_hcs_c32_artin_schreier_quantum_trace/RESEARCH_QUESTION_BRIEF.md)
- [C32 Phase-2 source verification](phase2_hcs_c32_artin_schreier_quantum_trace/SOURCE_VERIFICATION_REPORT.md)
- [C32 Phase-3 theorem package](phase3_hcs_c32_artin_schreier_quantum_trace/THEOREM_PACKAGE.md)
- [C32 exact certificate](phase3_hcs_c32_artin_schreier_quantum_trace/results/c32_morse_gate_certificate.json)
- [C32 independent check](phase3_hcs_c32_artin_schreier_quantum_trace/results/c32_morse_gate_independent_check.json)
- [C32 Devil's-Advocate checkpoint](phase3_hcs_c32_artin_schreier_quantum_trace/DEVILS_ADVOCATE_CHECKPOINT2.md)

Reproduce the complete Phase-3 gate with:

```bash
phase3_hcs_c32_artin_schreier_quantum_trace/code/run_c32_phase3.sh
```

## Predecessor big-door result: HCS-C31 identifies the H6 positive signal

C31 returns to the strongest certified H\'enon base rather than opening
another small prime or cycle scan.  The earlier instability-roof sections had
a stable positive zero near \(0.277982981676189\), but no infinite-system
theorem showed whether that value tracked an intrinsic quantity.

The new project encloses the adapted unstable roof on every admissible
length-13 cylinder.  The chronological higher-block graph has 714 vertices
and 1,156 edges.  Outward rational square-root, logarithm, and exponential
arithmetic, followed by exact Collatz--Wielandt inequalities, proves

\[
0.277980<h_*<0.277987,
\qquad P_{\Sigma_A}(-h_*\tau_{\rm ad})=0.
\]

The old value lies strictly inside this independently certified interval.
An explicit bounded H\"older coboundary identifies the adapted roof with the
Euclidean unstable geometric potential.  Strict interior realization makes
the survivor a mixing locally maximal hyperbolic set, so local Bowen theory
gives

\[
h_*=\dim_H(\Lambda_*\cap W^u_{\rm loc}(z)),
\qquad
0.555960<\dim_H\Lambda_*<0.555974.
\]

Thus the certified root is geometric: it is the pressure boundary and
unstable dimension of the local horseshoe.  The old finite-section value is
consistent with it to the certified resolution, without any claim of equality
or cutoff convergence, so it supplies no independent arithmetic resonance.
Longer cutoff scans alone are no longer a large door.
The strict Route-A tuple for that interpretation is
**(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)** with overall
**ROUTE_A_REJECTED**.  A reopening must add a canonical arithmetic fibre or
twist while preserving the proven chronology and roof.

- [C31 project overview](henon_bowen_pressure_gate/README.md)
- [C31 theorem package](henon_bowen_pressure_gate/THEOREM_PACKAGE.md)
- [C31 exact certificate](henon_bowen_pressure_gate/results/c31_certificate.json)
- [C31 independent check](henon_bowen_pressure_gate/results/c31_independent_check.json)
- [C31 compiled paper](henon_bowen_pressure_gate/paper/main.pdf)
- [C31 Route-A record](henon_bowen_pressure_gate/route_a_evaluation.yaml)

Reproduce the complete gate with:

```bash
henon_bowen_pressure_gate/code/run_c31.sh
```

## Predecessor big-door result: HCS-C30 closes the formal-inverse AGY promotion

C30 attacks the roof/operator gate left open by C29 without extending the
word or prime scan.  It returns to the source raw matrices and separates three
chronological actions: genuine Rauzy lengths \(B^{-\mathsf T}\), the
contravariant transfer action \(B^{\mathsf T}\), and the raw covariant
homology recurrence used only as a convention control.

For every cyclic phase of the two C25 length-six kernel words and the C26
length-twenty-four kernel word, exact integer Farkas descriptors prove that
the positive length cone is empty:

\[
6/6,\qquad 6/6,\qquad 24/24.
\]

The independent transfer replay has the same complete failure census.  By
contrast, C1 and C2 have positive raw-homology controls, which proves that the
negative result does not come from silently confusing \(B\) with
\(B^{-\mathsf T}\).

The theoretical gate closes as well.  A real additive groupoid cocycle changes
sign on inverse arrows.  The projective normalizer has zero period on a
matrix-identity return wherever defined, whereas a positive symmetric edge
length declares a different non-backtracking graph suspension.  Faithful
bounded inverse edge operators on one infinite-dimensional space cannot form
a compact or nuclear Hashimoto operator.  Enlarging the branch domain instead
makes the full return the identity with a neutral fixed continuum and
\(\det(I-Dh_W)=0\), outside the standard isolated-hyperbolic trace formula.

The distinction between a unit path and identity matrix holonomy is retained:
an arbitrary edge cocycle need not vanish on the C25 kernel words.  General
clean-fixed-set regularization is not ruled out.

The finite C29 group-trace determinant remains valid for its explicitly new
graph system.  Only its proposed identification with the AGY natural
extension is rejected.  The scoped Route-A tuple is
**(A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)**.  The next large move is an
all-word composition/determinant-tail theorem or genuinely new twist on the
already certified hyperbolic Hénon pinning infrastructure—not a longer formal
inverse-word or small-prime scan.

- [C30 project overview](rauzy_inverse_roof_trace_obstruction/README.md)
- [C30 theorem package](rauzy_inverse_roof_trace_obstruction/THEOREM_PACKAGE.md)
- [C30 exact certificate](rauzy_inverse_roof_trace_obstruction/results/c30_certificate.json)
- [C30 independent check](rauzy_inverse_roof_trace_obstruction/results/c30_independent_check.json)
- [C30 Route-A record](rauzy_inverse_roof_trace_obstruction/route_a_evaluation.yaml)

Reproduce the round with:

```bash
cd rauzy_inverse_roof_trace_obstruction && ./code/run_c30.sh
```

## Previous big-door result: HCS-C29 reversible Rauzy groupoid

C29 has completed its Phase-2 exact gate.  The phrase “two-sided AGY
extension” splits into two different objects.  The genuine natural extension
keeps the original positive periodic products, so the regular-group/periodic-
product trace-log germ built from them is still exactly one; no trace-class
operator on a new two-sided space is claimed.  A declared symmetric
non-backtracking Rauzy groupoid is a new dynamics, and it does contain
nontrivial reduced identity-holonomy loops.

At elementary-edge level, exhaustive exact enumeration through length nine
gives

\[
(N_1,\ldots,N_9)=(0,0,0,0,0,24,0,32,144).
\]

Two explicit primitive length-six loops already prove the matching lower
bound of 24 based oriented contributions.  More
importantly, the frozen C26 branch matrices satisfy an exact braid relation
which expands to a primitive cyclically reduced length-24 identity word in
the actual `gamma_star`, second and third branch alphabet.  Thus C25 positive
monoid freeness does not extend to freeness of the inverse-completed group.

The C28 normalized finite-Weil character limit then produces a nonconstant
group-trace determinant germ, locally uniformly on the common disc
\(|u|<1/5\).  The C26 relation proves (N_{24}\ge48), not a total
length-24 census.  This is an algebraic reopening only: formal
inverse arrows are not forward AGY branches, no intrinsic positive reversible
roof is known, and C26 Bergman nuclearity does not apply to expanding inverse
maps.

The deterministic certificate passes 14 independent gates and 38
regression/mutation tests.  The conservative tuple is
**(A1_WEAK, A2_ANALYTIC_DETERMINANT,
A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)** with overall
**ROUTE_A_EXPLORATORY**.  Route B is not authorized.  The next large gate is
an intrinsic positive reversible roof together with a genuine two-sided trace
theorem; longer small-word or small-prime scans are not the next move.

- [C29 project overview](rauzy_groupoid_identity_determinant/README.md)
- [C29 research question](rauzy_groupoid_identity_determinant/RESEARCH_QUESTION.md)
- [C29 theorem package](rauzy_groupoid_identity_determinant/THEOREM_PACKAGE.md)
- [C29 Phase-2 checkpoint](rauzy_groupoid_identity_determinant/PHASE2_CHECKPOINT.md)
- [C29 exact certificate](rauzy_groupoid_identity_determinant/results/c29_certificate.json)
- [C29 independent check](rauzy_groupoid_identity_determinant/results/c29_independent_check.json)
- [C29 Route-A record](rauzy_groupoid_identity_determinant/route_a_evaluation.yaml)

Reproduce the round with:

```bash
cd rauzy_groupoid_identity_determinant && ./code/run_c29.sh
```

## Latest big-door result: HCS-C28 sharp all-prime threshold

HCS-C28 resolves the global assembly question left by C27 without extending
the small-prime scan.  For the full \(p^2\)-dimensional finite-Weil twist,
the local Schatten norms have the exact large-prime order

\[
\|\mathcal L_{s,p}\|_{S_q}\asymp p^{2/q}.
\]

It follows that

\[
\bigoplus_p c_p\mathcal L_{s,p}\in S_q
\iff \sum_p p^2|c_p|^q<\infty,
\]

and the undamped direct sum is not compact.  The Dirichlet-damped family

\[
\mathfrak L_{s,z}=\bigoplus_{p\ {\rm odd}}p^{-z}\mathcal L_{s,p}
\]

is trace class exactly when \(\Re z>3\).  On this sharp half-plane it has an
ordinary prime-order-independent determinant

\[
\det(I-u\mathfrak L_{s,z})
=\prod_{p\ {\rm odd}}D_p(s,u p^{-z}),
\]

and its trace keeps the unreordered chronological matrix of every AGY word.

The theorem also closes the two canonical-looking alternatives.  Normalized
finite-Weil characters converge to the regular character, but the positive
AGY return monoid is free, so every nonempty normalized moment vanishes and
the determinant germ becomes one.  In the ambient C24 full-Rauzy ledger,
P073 has a two-dimensional fixed plane and exact character \(\Theta_p=p\)
for every odd prime, making its dimension-normalized marked sum the divergent
prime harmonic series.  P073 is not claimed to be a C26 induced branch.

Thus the positive object is a prime-graded Dirichlet--Fredholm determinant,
not an adelic Weil representation.  Its \(z\log p\) clock is external to the
AGY roof, and orbit conductors fragment.  The conservative tuple is
**(A1_WEAK, A2_ANALYTIC_DETERMINANT,
A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)** with overall
**ROUTE_A_EXPLORATORY**. Route B is not authorized.

- [C28 project overview](agy_prime_direct_sum_determinant/README.md)
- [C28 theorem package](agy_prime_direct_sum_determinant/THEOREM_PACKAGE.md)
- [C28 exact certificate](agy_prime_direct_sum_determinant/results/c28_certificate.json)
- [C28 independent check](agy_prime_direct_sum_determinant/results/c28_independent_check.json)
- [C28 compiled paper](agy_prime_direct_sum_determinant/paper/main.pdf)

Reproduce the round with:

```bash
cd agy_prime_direct_sum_determinant && ./code/run_c28.sh
```

The next big door is a two-sided based/path-groupoid trace with genuine
identity-holonomy loops, or a new local \(p\)-adic oscillator and automorphic
theta architecture.  More finite-field prime scans cannot alter the sharp
C28 threshold.

## Predecessor big-door result: HCS-C27 finite-Weil determinant and collapse

HCS-C27 executes the finite-fibre gate left by C26. For every fixed odd
prime \(p\), the C25 chronological symplectic cocycle reduces to
\(\operatorname{Sp}(4,\mathbb F_p)\) and acts through the genuine
\(p^2\)-dimensional Weil representation. Finite tensoring preserves the C26
trace-class Bergman theorem, so the target operator has an ordinary jointly
holomorphic determinant

\[
D_p(s,u)=\det(I-u\mathcal L_{s,p}),
\qquad \Re s>-\sigma_0.
\]

A forward periodic word contributes its scalar Perron atom multiplied by
\(\Theta_p(g_w)\). Thomas's exact character formula gives the quadratic law

\[
\Theta_p(g)=\left(\frac{\det(g-I)}p\right)
\]

whenever \(p\) does not divide \(\det(g-I)\).

The finite fibre detects the frozen C26 three-return noncyclic order at
\(p=3,5,7\), and the complete degree-\(p^2\) fibre polynomials differ at all
three primes. Across odd \(p\le97\) and \(1\le r\le24\), 328 of 576 exact
power characters differ.

Two exact collapses show that the present class-function fibre does not by
itself justify promotion to a global Hilbert--Pólya object. At
\(p=43\), the C26 forward and reverse matrices both have order 925 and their
Weil characters agree over the complete period, so their degree-1849
finite-fibre polynomials coincide even though the base characteristic
polynomials differ. Their scalar Perron atoms remain different. More
strongly, C24-P076/P082 are distinct primitive symbolic cycles but are
explicitly conjugate in \(\operatorname{Sp}(J_{24},\mathbb Z)\), where
\(J_{24}\) is the frozen C24 symplectic form. Every
class-function fibre collapses their entire repetition towers over every
prime.

The bounded arithmetic census also fragments: all 150 positive-prefix AGY
branches through bridge length 12 have different discriminants,
characteristic polynomials, and Legendre signatures over the odd primes below
100. This is finite evidence, not an all-length theorem.

The conservative verdict is
**(A1_WEAK, A2_ANALYTIC_DETERMINANT,
A3_PARTIAL_ANALYTIC_STRUCTURE, A4_NATURAL_QUANTIZATION)** with overall
**ROUTE_A_EXPLORATORY**. Route B is not authorized. A continuation must derive
an intrinsic adelic measure/trace and convergent same-clock prime assembly;
otherwise this fibre route should stop rather than add smaller prime scans.

- [C27 project overview](agy_finite_weil_determinant/README.md)
- [C27 theorem package](agy_finite_weil_determinant/THEOREM_PACKAGE.md)
- [C27 exact certificate](agy_finite_weil_determinant/results/c27_certificate.json)
- [C27 independent check](agy_finite_weil_determinant/results/c27_independent_check.json)
- [C27 compiled paper](agy_finite_weil_determinant/paper/main.pdf)

Reproduce the round with:

```bash
cd agy_finite_weil_determinant && ./code/run_c27.sh
```

## Predecessor big-door result: HCS-C26 scalar/twisted AGY dichotomy

HCS-C26 closes the holomorphic/no-localizer escape left open by C25 and
simultaneously extracts a positive scalar determinant.  Every AGY return
matrix factors as

\[
B_\gamma^T=P C_\gamma,
\qquad P=B_{\gamma_*}^T>0,
\qquad C_\gamma\ge0.
\]

Nonnegative projective maps preserve a canonical complex positive cone, and
the fixed positive prefix maps its closure strictly inside.  Consequently
there is one bounded domain \(\Omega\subset\mathbb C^3\) whose compact core
contains every countable inverse-branch image.  The raw weights

\[
w_{s,\gamma}(z)
=\bigl(\mathbf1^TB_\gamma^Tz\bigr)^{-(s+4)}
\]

share a principal logarithm and have summable sup norms for every
\(\Re s> -\sigma_0\).  The scalar operator on \(A^2(\Omega)\) is therefore
trace class.

For a literal operator-expansion word, later branches multiply on the left:

\[
A_{\boldsymbol\gamma}
=A_{\gamma_n}\cdots A_{\gamma_1}
=(B_{\gamma_1}\cdots B_{\gamma_n})^T.
\]

If \(\lambda_{\boldsymbol\gamma}\) is its Perron root and
\(\chi_{\boldsymbol\gamma}\) its characteristic polynomial, the ordinary
scalar trace atom is exactly

\[
\operatorname{tr}T_{s,\boldsymbol\gamma}
=\frac{\lambda_{\boldsymbol\gamma}^{-(s+1)}}
       {\chi_{\boldsymbol\gamma}'(\lambda_{\boldsymbol\gamma})}.
\]

The raw integer word matrix lies in \(SL(4,\mathbb Z)\), so its Perron root
is an algebraic unit.  This provides a genuine arithmetic and chronological
trace structure, but no prime law or Riemann-divisor identification.

On the same domain, the literal vector-valued series on
\(A^2(\Omega;L^2(\mathbb R^2))\) is bounded.  Constants followed by one
interior evaluation compress the full countable operator to an `ell^1` sum
of distinct metaplectic atoms.  C24's atomic theorem and C25's all-length
decoder give

\[
\|\mathcal L_s^{\rm Mp}\|_{\rm ess}
\ge
\frac{\bigl(\sum_\gamma|w_{s,\gamma}(x_0)|^2\bigr)^{1/2}}
     {\|E_{x_0}\|\,\|J\|}>0.
\]

Thus scalar holomorphic nuclearity survives, but the unsmoothed infinite
oscillator twist is noncompact on that very space.  The exact suite passes
14 independent checks and 21 registered mutations; it reconstructs the
length-128 rational lower bound, the positive-prefix cone constants, three
Perron trace examples, a two-return contravariant-order sentinel, and a
three-return noncyclic reversal whose characteristic polynomial changes.

The formal target verdict remains
**(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)** with overall
**ROUTE_A_REJECTED**.  The next large door changes the fibre to finite Weil
representations over odd finite fields, rather than trying more base norms.

- [C26 project overview](agy_holomorphic_slice_obstruction/README.md)
- [C26 theorem package](agy_holomorphic_slice_obstruction/THEOREM_PACKAGE.md)
- [C26 exact certificate](agy_holomorphic_slice_obstruction/results/c26_certificate.json)
- [C26 independent check](agy_holomorphic_slice_obstruction/results/c26_independent_check.json)
- [C26 compiled note](agy_holomorphic_slice_obstruction/paper/main.pdf)
- [C26 Route-A record](agy_holomorphic_slice_obstruction/evaluations/route_a/HCS-C26/20260810T044618Z.yaml)

Reproduce the round with:

```bash
cd agy_holomorphic_slice_obstruction && ./code/run_c26.sh
```

## Predecessor big-door result: HCS-C25 AGY transfer obstruction

HCS-C25 closes the concrete application gate left open by C24.  It freezes
one explicit Avila--Gou\"ezel--Yoccoz precompact Rauzy first-return section
and applies the infinite-fibre obstruction to the actual published
bounded-derivative transfer regularity, rather than another finite periodic
ledger.

For the state `(1342)/(4321)`, put

\[
\eta=\texttt{tbttbtbb},
\qquad
\gamma_*=t^{64}\eta^8.
\]

The length-128 word is eight-complete, meeting the exact AGY threshold
`3d-4=8`.  Its maximal initial top run has length 65, it ends bottom, and it
has no nonempty proper border.  The independently verified chronological
matrix is positive, determinant one, and preserves the full-rank crossing
form.  The exact projective inverse branch satisfies

\[
j_{\gamma_*}=e^{-4r_{\gamma_*}}.
\]

There is also an all-length structural theorem.  For a path from a fixed
labeled state, the true first Rauzy edge is the unique candidate whose winner
row dominates its loser row in \(B_\gamma^T\).  Subtracting those rows peels
the edge and strictly lowers the matrix-entry sum.  Hence the full matrix
uniquely determines the complete path.  In this four-letter
\(\mathcal H(2)\) class the crossing form is nondegenerate, so distinct AGY
return branches cannot collide after passage to absolute homology.  The
declared edge lifts then recover the true metaplectic central sign.

On

\[
C_b^1(\Delta;L^2(\mathbb R^2)),
\]

the raw twisted branch series converges in operator norm throughout the AGY
half-plane \(\Re s>-\sigma_0\).  A branch-supported source-provided bump and
point evaluation compress the full operator exactly to a nonzero scalar
multiple of one infinite-dimensional metaplectic unitary.  The operator is
therefore noncompact and nonnuclear.  The invariant-density normalized
operator on \(L^2(\mu;L^2(\mathbb R^2))\) is contractive but noncompact for
\(\Re s\ge0\); on \(s=it\) it is a coisometry with essential norm one.
The normalized \(L^2\) failure is already present for the scalar fibre on
the whole half-plane, so it is a generic Hilbert-space control; the
oscillator-specific result is the raw \(C_b^1\) multi-branch compression.

The independent checker passes eleven registered gates and fourteen mutation
tests.  A finite non-proof sentinel decodes all 35,420 central first returns
through elementary length 22 with zero collision; the theorem, not that
window, proves the all-length claim.

The formal verdict remains
**(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)** with overall
**ROUTE_A_REJECTED**.  The two tested ordinary Fredholm realizations are
closed.  Holomorphic/no-localizer spaces, flat or distributional traces,
semifinite determinants, and geometrically forced continuous smoothing are
different candidates and remain open.  The next large step must enter one of
those spaces rather than extend the elementary period cutoff.

- [C25 project overview](agy_metaplectic_transfer_obstruction/README.md)
- [C25 theorem package](agy_metaplectic_transfer_obstruction/THEOREM_PACKAGE.md)
- [C25 exact certificate](agy_metaplectic_transfer_obstruction/results/c25_certificate.json)
- [C25 independent check](agy_metaplectic_transfer_obstruction/results/c25_independent_check.json)
- [C25 compiled note](agy_metaplectic_transfer_obstruction/paper/main.pdf)

Reproduce the round with:

```bash
cd agy_metaplectic_transfer_obstruction && ./code/run_c25.sh
```

## Predecessor big-door result: HCS-C24 Rauzy--metaplectic obstruction

HCS-C24 made the planned change of dynamical form.  The literal reversal
permutation \((1234)/(4321)\) passes source lock as a seven-state,
fourteen-edge labeled Rauzy class in \(\mathcal H(2)\).  Open edges transport
their changing crossing forms and later edges multiply on the left; no
averaged cocycle replaces the chronology.

The exact ledger through elementary length 12 contains 828 primitive
fixed-label directed cycle codes.  Exactly 146 are eventually positive in
every cyclic phase, but 21 of these have

\[
\det(I-M)=0
\]

and characteristic polynomial divisible by \((x-1)^2\).  Hence the same
singularity persists for every repetition.  The regular point formula for
the Weil distribution character therefore cannot be used as a finite
pointwise weight on the full selected labeled-cycle set.  These are coded
orbit counts; no claim is made that all 146 codes give distinct primitive
unmarked Teichmüller geodesics.  The 146 selected codes realize only 41
distinct reciprocal characteristic polynomials, and no cycles are quotiented
by this homological spectral coincidence.

Two operator classes close exactly.  First,

\[
\|K\otimes U\|_{\rm ess}=\|K\|
\]

for an infinite-dimensional unitary fibre, so any nonzero
exact/modulo-compact branch compression obstructs compactness.  Second, an
absolutely norm-summable discrete metaplectic atomic sum on Hilbert base
spaces is noncompact whenever one aggregate over equal projected matrices is
nonzero after retaining the true central signs.  A particular canonical
analytic Zorich space has not yet been shown to satisfy either application
hypothesis, so this is a scoped two-class obstruction rather than a global
no-go theorem.

The formal verdict is
**(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)** with overall
**ROUTE_A_REJECTED**; Route B is not authorized.

- [C24 project overview](rauzy_metaplectic_obstruction/README.md)
- [C24 theorem package](rauzy_metaplectic_obstruction/THEOREM_PACKAGE.md)
- [C24 exact certificate](rauzy_metaplectic_obstruction/results/c24_certificate.json)
- [C24 independent check](rauzy_metaplectic_obstruction/results/c24_independent_check.json)
- [C24 compiled note](rauzy_metaplectic_obstruction/paper/main.pdf)
- [C24 original source-lock roadmap](docs/hcs_c24_system_switch.md)

Reproduce the round with:

```bash
cd rauzy_metaplectic_obstruction && ./code/run_c24.sh
```

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

Last synchronized research snapshot: **2026-08-14**.
