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
henon_galois_excess_five_block_obstruction - HCS-P57 complete - Exact reflection reductions give a cubic A6 trace field and one totally real degree-fourteen A7/B7 field; the certified positive Delta5 excludes every width-at-most-five excess potential, while a unimodular width-six minor preserves the genuine Hölder-asymptotic gate.
henon_physical_tail_galois_parity_obstruction - HCS-P58 complete - Period-eight/nine trace fields and opposite exact discrepancy signs separate physical stable-tail data from all-conjugate Galois excess.
henon_reflection_half_entropy_law - HCS-P59 complete - Exact odd/even-axis Möbius formulas give reflection entropy `(1/2)log(phi)`, half the full H6 survivor entropy.
henon_mixed_axis_dynatomic_entropy_gap - HCS-P60 complete - Odd mixed-axis closure polynomials have exact degree `2^((n+1)/2)` and formal primitive entropy `(1/2)log(2)`, exposing an effectivity/transversality gate above the physical half-entropy law.
henon_survivor_reflection_transversality - HCS-P61 complete - Every primitive odd mixed-axis root in the certified H6 survivor is transverse/simple and counted by the reversible-necklace law, but these roots are exponentially sparse in formal degree.
henon_mu3_yukawa_lambda_square_shadow - C62 prefreeze complete - The exterior/symmetric lambda-square shadows of the C61 W(E6) Gassmann pair have complete finite-group atlases and a 16-type fixed-field dictionary; arithmetic/local claims remain explicitly out of scope.
henon_mu3_yukawa_burnside_kernel_rank - C63 prefreeze complete - The C62 exterior shadow exposes a primitive four-versus-four Burnside relation with a 25-by-16 character matrix of rank 13; the full Burnside ring and arithmetic/local claims are not asserted.
henon_mu3_yukawa_burnside_marks - C64 prefreeze complete - The restricted 16-type table-of-marks matrix has rank 16 and determinant (2^{23}3^3), separating the C63 character-zero relation; full Burnside-ring and arithmetic/local claims are not asserted.
henon_mu3_yukawa_mark_defect - C65 prefreeze complete - The C63 character-kernel image has restricted Smith forms (2,8) and (2,2,8), with a precise relative Z/2 dyadic saturation class generated by the normalized four-versus-four direction; no full-Burnside or arithmetic/local claim is made.
henon_mu3_yukawa_mark_cokernel - C66 prefreeze complete - The restricted 16-by-16 mark map has Smith invariants (1,2^{10},4^3,24,144), cokernel (Z/2)^10 + (Z/4)^3 + Z/24 + Z/144, and primary parts Z/2/Z/4/Z/8/Z/16 at 2 and Z/3 + Z/9 at 3; the result is restricted to the frozen support.
henon_mu3_yukawa_mark_coordinate_profile - C67 prefreeze complete - Fixing the named S_i mark coordinates gives exact least-integral-multiplier profiles (36,12,6,6,2,2,36,6,16,8,6,12,2,2,36,36) and transpose profile (1,4,2,2,2,2,36,6,16,8,2,4,2,2,2,2), both with global denominator 144.
henon_mu3_yukawa_mark_defect_duality - C68 prefreeze complete - The C65 saturation defect embeds in the C66 restricted cokernel as (Z/8) + (Z/2)^2; the quotient and transpose-side annihilator have Smith invariants (1^4,2^8,4^2,12,144), with annihilator coordinate types S1,S4,S7,S8.
henon_mu3_yukawa_mark_defect_splitting - C69 prefreeze complete - The actual C68 defect inclusion splits via rho([x])=(x10 mod 8,x3 mod 2,x1+x15 mod 2); an explicit complement has Smith invariants (1^4,2^8,4^2,12,144), and the fixed subgroup has exactly 2^41 complements.
henon_mu3_yukawa_mark_direct_factor_orbit - C70 prefreeze complete - Aut(C) is transitive on D-type direct factors, ordered (D,K) decompositions, and split embeddings; counts are 5846893330432, 12857454406351852314558464, and 2245207038885888, while 2947589144576 of 8794482475008 abstract D-type subgroups are non-direct.
henon_mu3_yukawa_mark_complement_geometry - C71 prefreeze complete - The fixed complement family has 2^41 members, universal intersection 8C ~= Z/3 + Z/18 of order 54, an exact intersection-index spectrum, and 25 named generating triples.
henon_mu3_yukawa_mark_coordinate_core_atlas - C72 prefreeze complete - The named Z/9 + Z/3 + Z/2 coordinate atlas classifies all 65536 supports, reaches all 20 subgroups of 8C, and separates named minimum 3 from abstract minimum 2.
henon_mu3_yukawa_mark_generation_blocker_reliability - C73 prefreeze complete - The named generation hypergraph has non-isolated cone K_{1,1,2,5} geometry, five minimal blockers, exact 35136/30400 deletion counts, and homogeneous/heterogeneous reliability formulae.
henon_mu3_yukawa_mark_named_core_affine_rigidity - C74 prefreeze complete - The named Q=Z/9+Z/3+Z/2 core has |Aut(Q)|=108 and |Aff(Q)|=5832, while both named-multiset and underlying-point affine stabilizers are trivial; the C73 abstract hypergraph symmetry is not an affine core symmetry.
henon_mu3_yukawa_mark_closure_incidence_lift - C75 prefreeze complete - The lifted closure-incidence symmetry has order 11520 with a C6 lattice-action kernel, weighted stabilizer 12, duplicate-fibre kernel 960, and pure 20-subgroup image 18.
henon_mu3_yukawa_mark_closure_orbit_atlas - C76 prefreeze complete - The effective 1920-element label image partitions all 65536 supports into 3024 orbits, with 98 closure-minimal supports and 25 full-core minimal triples; the 11520 ambient lift remains distinct.
henon_mu3_yukawa_mark_subgroup_mobius_reliability - C77 prefreeze complete - Möbius inversion on the actual 20-subgroup lattice matches direct enumeration of all 65536 supports and reproduces the C73 top reliability polynomial, without claiming a full Burnside ring.
henon_mu3_yukawa_mark_repair_distance_geometry - C78 prefreeze complete - Deletion/repair geometry for all 65536 supports has exact distance distribution 30400/32704/2368/64, maximum repair distance 3, and a verified bivariate generating function with x marking deletions.
henon_mu3_yukawa_mark_repair_witness_multiplicity - C79 prefreeze complete - Minimum-repair witness multiplicities are enumerated exactly over all 65536 supports, with maximum repair distance 3 and witness values 1,4,7,8,25.
henon_mu3_yukawa_mark_threshold_repair_atlas - C80 prefreeze complete - The complete 65536-by-20 threshold-repair atlas reaches every frozen subgroup target and recovers the C78 repair-distance marginal.
henon_mu3_yukawa_mark_effective_orbit_repair_profile - C81 prefreeze complete - The effective 1920 label action (distinct from the 11520 ambient lift) gives 3024 repair-profile orbits and 14 profile classes.
henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum - C82 prefreeze complete - The full-core Boolean predicate has an exact 1024-term Walsh spectrum, degree 10, and an exact Hamming bit-flip autocorrelation law.
henon_mu3_yukawa_mark_random_order_assembly_stopping_time - C83 prefreeze complete - Uniform random label order has an exact prefix-assembly stopping distribution with minimum 3 and expectation 36499/3960.
henon_mu3_yukawa_mark_minimum_repair_matroid - C84 prefreeze complete - Every minimum-repair family is a direct-sum truncated partition matroid; five exact basis-exchange graph types are certified over all 65536 deletion sets.
henon_mu3_yukawa_mark_threshold_vector_poset_rigidity - C85 prefreeze complete - The 20-dimensional threshold vector is a closure invariant whose zero ideal recovers the subgroup and reverses the complete 20-subgroup poset.
henon_mu3_yukawa_mark_effective_orbit_flip_chain - C86 prefreeze complete - The faithful order-1920 action strongly lumps the 16-cube to a 3024-state one-bit flip chain with exact reversible flows and invariant Walsh spectrum.
henon_mu3_yukawa_mark_label_influence_interaction_atlas - C87 prefreeze complete - All 16 coalition-size first-order rows and 120 signed second-order pair rows are certified, with 7 label orbits, 27 pair orbits, and 10 numerical classes.
henon_mu3_yukawa_mark_subgroup_first_passage_atlas - C88 prefreeze complete - Exact random-order first-passage laws for all 20 subgroup targets are certified with 102 pointwise subgroup-order relations.
henon_mu3_yukawa_mark_first_passage_moments_cumulants - C89 prefreeze complete - Exact raw, factorial, central moments, and cumulants through order six for all 20 C88 first-passage targets.
henon_mu3_yukawa_mark_first_passage_joint_coupling - C90 prefreeze complete - Exact joint survival arrays, mixed moments, and covariance for all 400 ordered target pairs.
henon_mu3_yukawa_mark_first_passage_race_atlas - C91 prefreeze complete - Exact left-first, tie, and right-first race laws for all 108 incomparable target pairs.
henon_mu3_yukawa_mark_first_passage_label_sensitivity - C92 prefreeze complete - Exact 20-by-16 first-passage pivotal-rank and label-sensitivity atlas with efficiency identities.
henon_mu3_yukawa_mark_first_passage_orbit_quotient - C93 prefreeze complete - Effective order-1920 quotient of the first-passage laws with 16 target orbits, distinct from the ambient order-11520 lift.
henon_mu3_yukawa_mark_first_passage_hazard_residual - C94 prefreeze complete - Exact discrete hazard and residual-life atlas for all 20 first-passage targets.
henon_mu3_yukawa_mark_first_passage_comparable_delay - C95 prefreeze complete - Exact conditional delay laws for all 102 comparable ordered target pairs, including reflexive pairs.
henon_mu3_yukawa_mark_first_passage_coverage_order_statistics - C96 prefreeze complete - Exact coverage order-statistic laws for all 20 target ranks over all 65536 supports.
henon_mu3_yukawa_mark_first_passage_pair_orbit_quotient - C97 prefreeze complete - Faithful order-1920 quotient of all 400 ordered target-pair C90 laws into 272 pair orbits.
henon_mu3_yukawa_mark_first_passage_conditional_kernel - C98 prefreeze complete - Exact forward/reverse conditional kernels for all 400 target pairs with Bayes and total-moment identities.

## C64-C68 package index

This finite-group/mark-map round uses the scope firewall
`NO_BAD_EULER_OR_ROOT_NUMBER`. The manifests are scoped ledgers for the
canonical executable, evidence, and paper artifacts; each package also keeps
its source audit, theorem package, replay, hostile-mutation report, and
compiled manuscript.

| paper | package / paper | evidence | manifest | PDF |
|---|---|---|---|---|
| C64 | [package](henon_mu3_yukawa_burnside_marks/README.md) · [paper](henon_mu3_yukawa_burnside_marks/paper/main.pdf) | `7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212` | `eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6` | `2228e29506b39f2fb0aaa45ddb38b5739caef786ba5695ca1091cffdc52c523d` |
| C65 | [package](henon_mu3_yukawa_mark_defect/README.md) · [paper](henon_mu3_yukawa_mark_defect/paper/main.pdf) | `ebdd80fd2292225b98248aacd6b21bafab2987bdccb801c22c10adef7e7b4e4c` | `f8709e490d0c077c6498ce96617d6711b58790d245e93e20124aa43b3dadc913` | `2bf84d08510f8de277ea4e1897efd886084fed9aceefcb9528824a8f07088362` |
| C66 | [package](henon_mu3_yukawa_mark_cokernel/README.md) · [paper](henon_mu3_yukawa_mark_cokernel/paper/main.pdf) | `ce74edeec04b245637e5b12165a7fcdeb42475b0dead7373b1bcf3e37f22beb1` | `aa9a750fd87cfd09948167e0af93145823dff7d34c7bdb1ed13d1a8df493c626` | `df9c1ea9cac5c22d47b445145c353ef659629dff285bcddd13824d495119a1cb` |
| C67 | [package](henon_mu3_yukawa_mark_coordinate_profile/README.md) · [paper](henon_mu3_yukawa_mark_coordinate_profile/paper/main.pdf) | `357cd372b2341a36e483adcf771512d08d5207f71796550b6759c25813d3badd` | `473cf1172f13bb3b61eb78c92de4026e552dd751549c4131cff904d4845a9cb8` | `cb37a923fe9dd0364a9b752bc6523621d86b3f16829f0805382cb188fb19d708` |
| C68 | [package](henon_mu3_yukawa_mark_defect_duality/README.md) · [paper](henon_mu3_yukawa_mark_defect_duality/paper/main.pdf) | `6d99afb5ec5e291f068f603060c79c72114e3fd2c26e0c9c21fdd5281add9ab9` | `aab32e57216e091c2eeedc2486a6651d83bfac713ad6f290d9c1bb9b45a947bc` | `0d466021cb0fd3f764afb3f9322ed5079636a4d1410c41d739cb1246709ab072` |

- [C64--C68 batch plan](BATCH_PLAN_C64_C68.md)

## C79--C83 package index

Each package below contains its research question, source audit, theorem
package, reproducibility code, canonical evidence, compiled paper, and a
file-hash manifest.  The round remains finite/combinatorial and uses the
scope firewall `NO_BAD_EULER_OR_ROOT_NUMBER`.

| paper | package / paper | evidence | manifest | PDF |
|---|---|---|---|---|
| C79 | [package](henon_mu3_yukawa_mark_repair_witness_multiplicity/README.md) · [paper](henon_mu3_yukawa_mark_repair_witness_multiplicity/paper/main.pdf) | `147a9b77e0ee7459040a7cc3c026bb21bce950a806e4fbc3ce0441dc9bb6c879` | `982cce509de371d59c4b87cda75af057d994c6fc36146daddc3b983c9c63246c` | `d6f75f6988400da3723bded7de4c523f1cb0d802b65459bc647b0fae82bbdbb2` |
| C80 | [package](henon_mu3_yukawa_mark_threshold_repair_atlas/README.md) · [paper](henon_mu3_yukawa_mark_threshold_repair_atlas/paper/main.pdf) | `8d27428b14dbd7354e9c8308ad76b1108e3f551702165833301509cd52de7df5` | `a674116ab6f8f9478130219cc525478525f10f2e42f515e71418a3066e2b229c` | `853886c1cc20424eeb3eb71227df6135a90ccc3166c97a31e1119ea59cd73a31` |
| C81 | [package](henon_mu3_yukawa_mark_effective_orbit_repair_profile/README.md) · [paper](henon_mu3_yukawa_mark_effective_orbit_repair_profile/paper/main.pdf) | `c3cc35f45e1c8f7c9d4ecaecca820bf9dbc4db1c6a5769c20c75bad21f32fd9f` | `ff3028fd68817795b08ff24332ef44de4cf520ccba543f053fbd78140ac1b512` | `d6bb73164b5e4602604944d359d54c83e2e0bfe1c40044ae653ea8d13b4bdf80` |
| C82 | [package](henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum/README.md) · [paper](henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum/paper/main.pdf) | `6fc49cad02956f463b1e37d017506f437edce6717414da74770ad94913ccefa1` | `5934de3a933e559e941fc636860db2f9f5ceca181acd9d4915396e9facdc8f8b` | `b111d8ea403d5c87c0565a99633b0815b861d4a532eae356b6e295e40c78fa30` |
| C83 | [package](henon_mu3_yukawa_mark_random_order_assembly_stopping_time/README.md) · [paper](henon_mu3_yukawa_mark_random_order_assembly_stopping_time/paper/main.pdf) | `033f42f0eea2518f7cb269dd465d82d4871a729d2b93679fcd9f3af38cf9ca28` | `981f9b07297f1b69676e8ced2625e69df5bd8fcd366415a2f984eb6311ddaa85` | `47fdd116564bac2790593f67a4d65e1b664d98e3f3206231c131c7827fe0722c` |

## C84-C88 package index

| paper | package / paper | evidence | manifest | PDF |
|---|---|---|---|---|
| C84 | [package](henon_mu3_yukawa_mark_minimum_repair_matroid/README.md) · [paper](henon_mu3_yukawa_mark_minimum_repair_matroid/paper/main.pdf) | `9c3b20c703b680a391ad1834c0f55cabaf27bfed14cee2099b0c3afa1eb259ca` | `2957c0837803155fdca24a896accdb95aee147440093fabc1b9ac49bb09e9c8d` | `2a37dacc711e5a42dc7b4a33f87d2cc47d31cae20cf05ac345ebcec198c2f4f0` |
| C85 | [package](henon_mu3_yukawa_mark_threshold_vector_poset_rigidity/README.md) · [paper](henon_mu3_yukawa_mark_threshold_vector_poset_rigidity/paper/main.pdf) | `22bdaf9fa2fe08532b45eae51cf7704a1509764b5a09f10eebb98012224be152` | `d1e0af8c896e8975ef7544714d379499b2d69e50bdaabf4d8d55621e4c42d261` | `55126890b5bea6894dc2b7bbb90db6525df4e90cebbc3fc80a0e1c952ac5edcc` |
| C86 | [package](henon_mu3_yukawa_mark_effective_orbit_flip_chain/README.md) · [paper](henon_mu3_yukawa_mark_effective_orbit_flip_chain/paper/main.pdf) | `7b3e2179590c3dc8662a59f1d79ffbb12f2a4a787438a6902d6c28b2842e70b8` | `eb223600feb511a52051317b8d80c51423df022a934ca87b6d0ad90b2a4c381f` | `544418e44bdf5a22a7a1f416fc4f6367aff6f9320c24986e9de626d0511e4423` |
| C87 | [package](henon_mu3_yukawa_mark_label_influence_interaction_atlas/README.md) · [paper](henon_mu3_yukawa_mark_label_influence_interaction_atlas/paper/main.pdf) | `bedeb7a3d912330e5eadc72629ee24d773648993f73f20f23eaf477028334d6e` | `3f93dddf1421db6f0acb641aa95691ba1b7afcbd17315a79b2b33b3c27e97831` | `6b676d65b14aaf6f93f8d8d5e7226cbac45f1fb1a8379a0240dcbdf1c6cabd13` |
| C88 | [package](henon_mu3_yukawa_mark_subgroup_first_passage_atlas/README.md) · [paper](henon_mu3_yukawa_mark_subgroup_first_passage_atlas/paper/main.pdf) | `4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b` | `aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5` | `d8341a25856ac4d26de0a6398c39c625f8475ab624a923e498fa81a4fca1125b` |

## C89-C93 package index

This five-paper round extends the C88 first-passage receipt.  C89, C91, and
C92 are independently regenerated from frozen source receipts; C90 binds its
C89 marginal checks explicitly, and C93 binds its C92 sensitivity transport
check explicitly.  All packages use the scope firewall
`NO_BAD_EULER_OR_ROOT_NUMBER` and make no arithmetic, Euler-factor,
root-number, automorphy, full Burnside/table-of-marks, or Hilbert--Polya
operator claim.

| paper | package / paper | evidence | manifest | PDF |
|---|---|---|---|---|
| C89 | [package](henon_mu3_yukawa_mark_first_passage_moments_cumulants/README.md) · [paper](henon_mu3_yukawa_mark_first_passage_moments_cumulants/paper/main.pdf) | `86a589505280721590674235626ddc21e37d57c891c726c7e6fbba98b2bd3af9` | `81daf852ce48765f5804b675133e77cb086ae2ee94f3973237ec3ce6d5c3b16e` | `5f7d98c1a62a8bb1ebe2ffaf88cb9331ea1f53d2fe89dc816ca3463f9e9c797b` |
| C90 | [package](henon_mu3_yukawa_mark_first_passage_joint_coupling/README.md) · [paper](henon_mu3_yukawa_mark_first_passage_joint_coupling/paper/main.pdf) | `c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978` | `4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737` | `d1dcd62d535729aa36c6c173421c7e5ff9789d6520c464da6be3dfc23ae55af3` |
| C91 | [package](henon_mu3_yukawa_mark_first_passage_race_atlas/README.md) · [paper](henon_mu3_yukawa_mark_first_passage_race_atlas/paper/main.pdf) | `36b0fffda585ea483ba5603101c83c361b85ca4ba9a49c878f1e366d3c13ff0f` | `542de9625733b94e9aaec3f430d048d8878f6fe1b556e2f0493b5c7a50a31495` | `468d2f66b2296bd96a05760cc6d70e25e850d94b89c9bafa17fc0040a162b26b` |
| C92 | [package](henon_mu3_yukawa_mark_first_passage_label_sensitivity/README.md) · [paper](henon_mu3_yukawa_mark_first_passage_label_sensitivity/paper/main.pdf) | `902d6b2fd688abc525d2fab187559bfc9904c7f3c97dc51af62050586d145812` | `ca0c6435c6a69c845ae663f25ff3fcc002c2b6ea119c14b8205da2c529594642` | `960f7c5869ed49a40f21cf22dd5eb2c1a14b652b982ce0ee69407454406b4a95` |
| C93 | [package](henon_mu3_yukawa_mark_first_passage_orbit_quotient/README.md) · [paper](henon_mu3_yukawa_mark_first_passage_orbit_quotient/paper/main.pdf) | `4104f181b88d83666c9fcff814a7029a148c498e6393ad181c60fe5133adb9fe` | `a60e0855482e205b0174281c4a20b8f86d2eb9531a3f980cb76d92fcfb77c608` | `956588842f57ec297299fd12c4de52bd37d2d3d9b6a4eaeec9e10f81790bcc20` |

- [C89--C93 batch plan](BATCH_PLAN_C89_C93.md)

## C94-C98 package index

This five-paper round deepens the C88 first-passage atlas with hazards,
comparable delays, coverage order statistics, ordered-pair symmetry, and
conditional kernels.  All packages use the scope firewall
`NO_BAD_EULER_OR_ROOT_NUMBER` and make no arithmetic, Euler-factor,
root-number, automorphy, full Burnside/table-of-marks, or Hilbert--Polya
operator claim.

| paper | package / paper | evidence | manifest | PDF |
|---|---|---|---|---|
| C94 | [package](henon_mu3_yukawa_mark_first_passage_hazard_residual/README.md) · [paper](henon_mu3_yukawa_mark_first_passage_hazard_residual/paper/main.pdf) | `e185462629459a7d6602e3d1e3f49977a82d3fdee86007c3f906b224f028d1b` | `c2eafa0f604aeb817a010afcf9f4e1841f4c02ca7b91ce303b31e9ad04930912` | `c9678e7a39c3ae4aeaff56ce20f809cd2bd894bae4ca98cf5164cd18c2dddf54` |
| C95 | [package](henon_mu3_yukawa_mark_first_passage_comparable_delay/README.md) · [paper](henon_mu3_yukawa_mark_first_passage_comparable_delay/paper/main.pdf) | `53e5c9a1dbda2fa7e01af34ce6fc161ac102a312b003e1c86402ae7ec7373a3c` | `ba03e5e86ec6a9f3d7a31d9e6b57533c4af5e65db0e4f9fa3dfeddba15d47176` | `60caec178a32d3d33d459cd0103c922fb5e967d25e06830fcd4011705ac3698c` |
| C96 | [package](henon_mu3_yukawa_mark_first_passage_coverage_order_statistics/README.md) · [paper](henon_mu3_yukawa_mark_first_passage_coverage_order_statistics/paper/main.pdf) | `75a93c80b5e44f6aca1885073cf12e943de02751ad4e99aa37e83bf211b6ca23` | `bfd172a456330ea7d5c0c821e4a3ef93f0a39db9e49a9159b16ecbea3932bb4a` | `9222c35bd7d0d8c097ffadf47eeb086e735adbfccd98bff142143087c4626e18` |
| C97 | [package](henon_mu3_yukawa_mark_first_passage_pair_orbit_quotient/README.md) · [paper](henon_mu3_yukawa_mark_first_passage_pair_orbit_quotient/paper/main.pdf) | `099d8f32794d6967b3f2653f92dcaa0b096c711b67ed070330d7763a146bc696` | `94f4b3c8e15977e0882194bc6c0165291694902169d01f9ff278a542e74ed516` | `7c52b3081c1941b8c18aec7cfce89e2a95f4f85581e6135505061af0260422b1` |
| C98 | [package](henon_mu3_yukawa_mark_first_passage_conditional_kernel/README.md) · [paper](henon_mu3_yukawa_mark_first_passage_conditional_kernel/paper/main.pdf) | `49179ea34f6f10b7e20c68914cdd7aa5bb5df775cefade69f1a40163f2e933cb` | `feeeaa4af1959b804e21923f47bf24df161fb78d69b624ead768473cb652f4d1` | `774fa65062106e611c3d597b56aa4865a341f880263b1431bc4a6661f5820cfb` |

- [C94--C98 batch plan](BATCH_PLAN_C94_C98.md)

`P43`--`P57` are the unique registry aliases for the pressure/orbit lane.
The `P43`--`P47` project bundles retain legacy internal `HCS-C43`--`HCS-C47`
strings to preserve their published hashes; `P48`--`P57` were born
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
| [henon_mu3_yukawa_line_field/](henon_mu3_yukawa_line_field/) | C56: the Fano line scheme of the frozen C55 cubic surface is the connected finite-etale point \(\operatorname{Spec}E\) with \([E:\mathbf Q]=27\); \(E\) is non-Galois, its normal closure has Galois group \(W(E_6)\) of order \(51840\), and the surface has geometric/arithmetic Picard ranks \(7/1\), no \(\mathbf Q\)-line, and the divisibility obstruction \(27\mid[L:\mathbf Q]\) for every finite field \(L\) defining a line | Exact arithmetic classification of one frozen Yukawa cubic; the arithmetic rank uses the written Hochschild--Serre torsion/rank bridge after the machine fixed-space computation, and no \(\mathbf Q\)-point, rationality, Hasse/Brauer--Manin, motive, VHS, automorphy, functional equation, or Hilbert--Pólya operator follows, Route A exploratory |
| [henon_mu3_rational_yukawa_surface/](henon_mu3_rational_yukawa_surface/) | C55: a four-dimensional \(\mathbf Q\)-defined transverse equivariant deformation germ carries an intrinsic relative Reynolds image on \(R^5f_*\mathbf Q(1)\), giving a polarizable rank-\(10\) CY3-type VHS with Hodge numbers \((1,4,4,1)\) and locally immersive period map; exact Cayley multiplication produces a primitive rational projective Yukawa cubic whose zero surface is smooth and geometrically irreducible | A new exact local Hodge/Yukawa invariant of the fourth-moment core; no full fixed-Hilbert dimension claim, literal linear family, relative Chow--Kunneth projector, honest CY3, motive, BCD comparison, automorphy, functional equation, or Hilbert--Polya operator, Route A exploratory |
| [henon_mu3_universal_dihedral_denominator_rigidity/](henon_mu3_universal_dihedral_denominator_rigidity/) | C54: for every \(n\ge2\), the full projective monomial ideal stabilizer of the cubic--weighted-cycle-quadric source is \(\operatorname{Dih}(C_{3n})\) of order \(6n\), and its C53 descent is a nonconstant rank-\(6n\) rational group scheme with two rational geometric elements; on packet-admissible smooth rows, the complete good-split local exponent \(4/n\) is realized by an actual finite-rank rational compatible system exactly when \(n\mid4\), while the exact \(n=3\) character and split-invisible counterpacket gates cannot clear the denominator | All-order equation/group classification and packet-conditioned split-local rigidity; the group is not promoted to the full PGL stabilizer, rows \(n\ge5\) have no smoothness or motive theorem, and no inert/global root, automorphy, continuation, functional equation, or Hilbert--Pólya operator is obtained, Route A exploratory |
| [henon_mu3_dihedral_core_rational_descent/](henon_mu3_dihedral_core_rational_descent/) | C53: an explicit Hilbert--90 basis descends the ordered cubic/quadric source equations to \(\mathbb Q\) for every \(n\); on the certified fourth-moment row the twisted order-24 symmetry and its rank-10 Chow core descend to \(\mathbb Q\), with degree-ten integral, weight-five, reciprocal good-prime local polynomials and exact split/inert quadratic-base-change identities | First rational compatible-system package for the rank-10 core and exact split-local half-root repair; no new Euler half-plane, global continuation, functional equation, or Hilbert--Pólya operator, Route A exploratory |
| [henon_mu3_d12_calabi_yau_core_projector/](henon_mu3_d12_calabi_yau_core_projector/) | C52: the complete order-\(24\) projective monomial source group gives \(K\)-rational middle Chow projectors of ranks \(10\) and \(158\); the rational graph algebra cannot isolate the desired rank-two extreme Hodge pair | First algebraic splitting of the fourth-moment odd packet; A3 packet control improved, A2/A4 inherited, Route A exploratory |
| [henon_galois_excess_five_block_obstruction/](henon_galois_excess_five_block_obstruction/) | P57: reflection reduction produces an irreducible cubic `A6` trace field and a shared totally real degree-fourteen `A7/B7` field; exact Sturm intervals and an integer-product margin prove \(\Delta_5>0\), while determinant \(\pm1\) width-six minors prove finite sharpness | Exact width-at-most-five regularity obstruction inside Route A; the whole-sequence \(\Delta_m\) asymptotics, unrestricted Hölder realization, full Galois-weighted determinant and Route B remain open |
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

## HCS-P58 physical-tail/Galois-scale interface

P58 derives the three period-eight/nine reflection trace fields and proves
`Delta_6<0<Delta_7` exactly.  The negative-fixed-point tail controls one
physical embedding, whereas Galois excess sums all nonphysical embeddings;
the missing bridge is therefore a uniform primitive reflection-ensemble
count/height theorem.

- [P58 overview](henon_physical_tail_galois_parity_obstruction/README.md)
- [P58 paper](henon_physical_tail_galois_parity_obstruction/paper/paper.pdf)
- [P58 proof package](henon_physical_tail_galois_parity_obstruction/PROOF_PACKAGE.md)
- [P58 exact certificate](henon_physical_tail_galois_parity_obstruction/results/c58_certificate.json)

## HCS-P59 primitive reflection half-entropy law

P59 solves the physical reflection-counting problem left by P58. The frozen
four-state H6 survivor has the unique reversal involution
`rho=(0)(1 2)(3)`. Half-word transfer and parity-sensitive Möbius inversion
give exact all-period formulas for odd reflections and both even physical
axis types. If `C_n` counts all primitive cycles and `R_n` the reversible
cycles, then

\[
C_n\sim\frac{\varphi^n}{n},\qquad
R_n=\Theta(\varphi^{n/2}).
\]

Thus the reflection subsystem has entropy exactly `(1/2)log(phi)` and
exponentially vanishing density. This is a physical symbolic theorem; it
does not count roots or embeddings of reflection closure polynomials. The
next bridge is therefore the primitive algebraic reflection dynatomic degree
and its comparison with the symbolic half entropy.

- [P59 overview](henon_reflection_half_entropy_law/README.md)
- [P59 paper](henon_reflection_half_entropy_law/paper/paper.pdf)
- [P59 proof package](henon_reflection_half_entropy_law/PROOF_PACKAGE.md)
- [P59 exact certificate](henon_reflection_half_entropy_law/results/c59_certificate.json)

## HCS-P60 mixed-axis dynatomic entropy gap

P60 executes the algebraic reflection-dynatomic step named by P59 for every
odd period.  On the mixed fixed-axis slice, the exact closure polynomial is

\[
F_n(X)=q_{(n+1)/2}(X)-q_{(n-1)/2}(X),
\qquad \deg F_n=2^{(n+1)/2}.
\]

For odd divisors `d|n`, the recurrence proves `F_d|F_n` directly in the
quotient ring.  Möbius inversion therefore gives a formal primitive degree

\[
D_n=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2}
   =2^{(n+1)/2}+O\!\left(n2^{n/6+1/2}\right),
\]

whose entropy is `(1/2)log(2)`, strictly greater than P59's physical
reflection entropy `(1/2)log(phi)`. Exact factorization through period 15 is
squarefree and the new quotients are irreducible, with the period-nine
degree-28 quotient cross-locked to P58.

The all-period statement is deliberately formal: a birational Hénon map and
a symmetry-line slice are not automatically covered by projective
dynatomic effectivity theorems.  The next bridge is an all-period
transversality/intersection-multiplicity theorem identifying which formal
roots are reduced primitive closures and which belong to the certified
physical survivor.

- [P60 overview](henon_mixed_axis_dynatomic_entropy_gap/README.md)
- [P60 paper](henon_mixed_axis_dynatomic_entropy_gap/paper/paper.pdf)
- [P60 proof package](henon_mixed_axis_dynatomic_entropy_gap/PROOF_PACKAGE.md)
- [P60 exact certificate](henon_mixed_axis_dynatomic_entropy_gap/results/c60_certificate.json)

## HCS-P61 survivor reflection transversality

P61 closes the physical half of P60's effectivity gate.  If `n=2m+1`, pull
the second reflection axis back by `H^(m+1)` to obtain the involution

\[
K_m=H^{-(m+1)}RH^{m+1},\qquad H^n=JK_m.
\]

A tangency of the two fixed curves would give a common fixed tangent and
hence eigenvalue `+1` for `DH^n`.  Uniform hyperbolicity of the certified H6
survivor excludes that multiplier.  Thus every primitive odd physical
mixed-axis root is transverse and simple.

The symmetry-equivariant coding gives one root per primitive reversible
necklace, so

\[
P_n=\sum_{d\mid n}\mu(n/d)F_{(d+3)/2},\qquad
\frac{P_n}{D_n}=\Theta((\varphi/2)^{n/2}).
\]

Every physical root has local coefficient `+1` in the formal divisor, but
physical incidence is exponentially sparse in its degree. Exact rational
isolators through period 11 and an independent Cartesian enumeration match
the counts `1,1,2,4,6,12`. The ambient critical resultant and all-period
global effectivity remain open.

- [P61 overview](henon_survivor_reflection_transversality/README.md)
- [P61 paper](henon_survivor_reflection_transversality/paper/paper.pdf)
- [P61 proof package](henon_survivor_reflection_transversality/PROOF_PACKAGE.md)
- [P61 exact certificate](henon_survivor_reflection_transversality/results/c61_certificate.json)

## HCS-P62 full-horseshoe algebraic exhaustion

P62 closes the ambient half of the P60/P61 effectivity gate.  The scaling
`S(q,p)=(6q,6p)` conjugates `H6` to the area-preserving Hénon map at
`(a,b)=(6,-1)`.  Arai's certified hyperbolic plateau connects `a=6` to a
Devaney--Nitecki full-two-shift anchor at `a=10`.  Hence `H6^n` has exactly
`2^n` distinct real hyperbolic fixed points.  Friedland--Milnor's complex
algebraic fixed-point count is also `2^n`, so the real points exhaust the
complete complex fixed-point scheme with multiplicity one.

It follows that every odd mixed-axis closure polynomial is totally real and
squarefree.  Its Möbius primitive quotient is a reduced effective divisor of
exact least-period roots, with actual degree

\[
D_n=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2}
\]

and entropy `(1/2)log(2)`.  Exact Sturm isolation through odd period 13 gives
primitive counts `2,2,6,14,28,62,126`.  This is an all-period algebraic and
dynamical Route-A theorem, not an arithmetic promotion: rational-prime
labels, von Mangoldt amplitudes, a completed determinant, and an operator
remain open.

- [P62 overview](henon_full_horseshoe_algebraic_exhaustion/README.md)
- [P62 paper](henon_full_horseshoe_algebraic_exhaustion/paper/paper.pdf)
- [P62 proof package](henon_full_horseshoe_algebraic_exhaustion/PROOF_PACKAGE.md)
- [P62 exact certificate](henon_full_horseshoe_algebraic_exhaustion/results/c62_certificate.json)

## HCS-P63 primitive-coordinate height and flat pressure

P63 tests the all-period coordinate-height pressure proposed after P62.  In
the integral coordinate `x=6q`, every primitive root is an algebraic integer
and every conjugate is another real periodic coordinate.  The cyclic
recurrence gives the sharp all-period bound

\[
|x|\le1+\sqrt7,
\qquad h(x)\le\log(1+\sqrt7).
\]

For the degree-`D_n` scaled primitive divisor,

\[
Z_n(s)=\sum_{\widetilde\Psi_n(\alpha)=0}e^{-s h(\alpha)}
\]

satisfies `exp(-|s|C)D_n <= Z_n(s) <= exp(|s|C)D_n`.  Therefore, for every
fixed real `s`,

\[
\lim_{n\to\infty,\ n\text{ odd}}\frac1n\log Z_n(s)
=\frac12\log2.
\]

The same flatness holds after every fixed nonzero algebraic coordinate
rescaling.  Thus ordinary per-root coordinate height is not an extensive
clock and cannot create a new pressure pole.  Exact finite polynomials and
factor heights through period 11, an independent Sturm checker through
period 9, and 25 hostile mutations support the theorem ledger.

Route A remains **ROUTE_A_EXPLORATORY** and Route B is not authorized.  The
next non-micro object is an extensive packet height, beginning with
`n*D_n^(-1) log M(tilde_Psi_n)` and a reflection-root equidistribution
theorem.

- [P63 overview](henon_primitive_coordinate_height_flat_pressure/README.md)
- [P63 paper](henon_primitive_coordinate_height_flat_pressure/paper/paper.pdf)
- [P63 proof package](henon_primitive_coordinate_height_flat_pressure/PROOF_PACKAGE.md)
- [P63 exact certificate](henon_primitive_coordinate_height_flat_pressure/results/c63_certificate.json)

## HCS-P64 reflection-boundary Mahler packet pressure

P64 corrects the first equidistribution guess made after P63. Under the
reversor-equivariant full-shift coding, odd mixed-axis roots are primitive
palindromic words marked at their reflection center. Their marked empirical
measures converge to a reflected one-sided fair Bernoulli process, not to the
invariant maximal-entropy measure. Averaging the same selected cycles over
all time origins does converge to maximal entropy, with radius-`r` cylinder
error at most

\[
\frac{4r+1}{n}+\tau(n)2^{-n/3}.
\]

For `a_n=D_n^{-1} log M(tilde_Psi_n)`, one has `a_n -> kappa_J`, where
`0<kappa_J<=log(1+sqrt(7))`, and

\[
\lim_{n\to\infty,\ n\text{ odd}}\frac1n
\log\bigl(D_ne^{-sna_n}\bigr)
=\frac12\log2-s\kappa_J.
\]

This is a nonconstant extensive whole-packet pressure, not an individual
factor-height pressure. Finite diagnostics suggest the marked and
orbit-averaged slopes differ, but rigorous separation remains open. Route A
remains exploratory and Route B is not authorized.

- [P64 overview](henon_reflection_boundary_mahler_pressure/README.md)
- [P64 paper](henon_reflection_boundary_mahler_pressure/paper/paper.pdf)
- [P64 proof package](henon_reflection_boundary_mahler_pressure/PROOF_PACKAGE.md)
- [P64 exact certificate](henon_reflection_boundary_mahler_pressure/results/c64_certificate.json)

## HCS-P65 minimal symmetry-defect pressure

P65 replaces an unavailable global cylinder constant by an exact symbolic
calibration. Every finite observable supported wholly on one side of the
reflection axis has the same expectation under P64's boundary and invariant
laws. The first centered cross-axis observable
`chi=1{s[-1]=s[1]}` has expectations `1` and `1/2`, giving

\[
P_J(t)=\frac12\log2-t,
\qquad
P_{\rm orb}(t)=\frac12\log2-\frac t2.
\]

The two-parameter Mahler/symmetry pressure planes therefore have an exact
transverse derivative gap `-1/2`, even though the unperturbed Mahler slope
gap remains open. Route A remains exploratory; Route B is not authorized.

- [P65 overview](henon_minimal_symmetry_defect_pressure/README.md)
- [P65 paper](henon_minimal_symmetry_defect_pressure/paper/paper.pdf)
- [P65 proof package](henon_minimal_symmetry_defect_pressure/PROOF_PACKAGE.md)
- [P65 certificate](henon_minimal_symmetry_defect_pressure/results/c65_certificate.json)

## HCS-P66 reflection-boundary cohomology anomaly

P66 tests whether the marked pressure from P64--P65 is intrinsic under the
usual symbolic replacement `f -> f+u-u∘sigma`. It is not. Its exact boundary
anomaly is

\[
A_J(u)=\int (u-u\circ\sigma)\,d\eta_J,
\qquad
P_J(f+u-u\circ\sigma)=P_J(f)-A_J(u).
\]

The boundary law and its one-step translate are mutually singular, so the
dual total-variation norm of `A_J` is exactly `2`. Radius-`r` locally constant
witnesses realize `2(1-2^{-r})`. In contrast, every complete periodic-orbit
sum of a coboundary telescopes to zero exactly, making uniform cyclic packet
averaging gauge invariant before any limit.

This is a canonical-sampling obstruction and repair, not an arithmetic
trace. Route A remains exploratory and Route B is not authorized. The next
theorem is uniqueness of the normalized cyclic sampler that annihilates all
coboundaries.

- [P66 overview](henon_reflection_boundary_cohomology_anomaly/README.md)
- [P66 paper](henon_reflection_boundary_cohomology_anomaly/paper/paper.pdf)
- [P66 proof package](henon_reflection_boundary_cohomology_anomaly/PROOF_PACKAGE.md)
- [P66 certificate](henon_reflection_boundary_cohomology_anomaly/results/c66_certificate.json)

## HCS-P67 unique gauge-invariant orbit sampler

P67 proves that P66's orbit-averaging repair is canonical. For a normalized
real linear sampler on an `n`-cycle,

\[
L_w(Du)=\sum_j(w_j-w_{j-1})u_j.
\]

It annihilates every coboundary if and only if `w_j=1/n` for all `j`. This
uses no positivity assumption, and every nonuniform sampler is rejected by a
one-site transfer function.

Combining this uniqueness theorem with P64's orbit-averaged packet
equidistribution gives, for every continuous potential `f`,

\[
\mathcal P_f(s)=\frac12\log2-s\int f\,d\mu_B.
\]

The finite packet and limiting functional are exactly cohomology invariant
and Lipschitz in `f`. This is a canonical sparse-packet pressure, not full
topological pressure or an arithmetic trace. Route A remains exploratory and
Route B is not authorized. The next non-micro gate is a source-native
reflection-packet determinant or trace with intrinsic arithmetic semantics.

- [P67 overview](henon_unique_gauge_invariant_orbit_sampler/README.md)
- [P67 paper](henon_unique_gauge_invariant_orbit_sampler/paper/paper.pdf)
- [P67 proof package](henon_unique_gauge_invariant_orbit_sampler/PROOF_PACKAGE.md)
- [P67 certificate](henon_unique_gauge_invariant_orbit_sampler/results/c67_certificate.json)

## HCS-P68 canonical reflection-packet Euler product

P68 crosses the first determinant-interface gate without overpromoting it.
P67's unique cyclic packet mean defines

\[
\mathcal Z_f(z,s)=
\prod_{\substack{n\ge1\\n\ {\rm odd}}}
\left(1-z^n e^{-sn b_n(f)}\right)^{-D_n},
\]

and its logarithmic derivative has the exact primitive/repetition ledger

\[
[z^m]\,z\partial_z\log\mathcal Z_f
=\sum_{\substack{n\mid m\\n\ {\rm odd}}}
nD_n e^{-sm b_n(f)}.
\]

At \(s=0\) the radius is \(2^{-1/2}\), while

\[
\log\mathcal Z_0(z)
=\frac{1}{\sqrt2(1-\sqrt2z)}+G(z)
\]

near the positive boundary, with \(G\) analytic. Thus the product has an
exponential essential singularity, not a meromorphic pole. It is a canonical
packet Euler germ, but it is neither the full infinite-dihedral Lind zeta nor
an orbit-resolved Fredholm determinant. Route A earns an exact A2 prefix and
partial A3 structure; Route B remains unauthorized. The next gate is the
within-period cumulant information erased by aggregate averaging.

- [P68 overview](henon_canonical_reflection_packet_euler_product/README.md)
- [P68 paper](henon_canonical_reflection_packet_euler_product/paper/paper.pdf)
- [P68 proof package](henon_canonical_reflection_packet_euler_product/PROOF_PACKAGE.md)
- [P68 certificate](henon_canonical_reflection_packet_euler_product/results/c68_certificate.json)

## HCS-P69 orbit-resolved reflection cumulant pressure

P69 computes exactly what P68's periodwise mean suppresses. For the minimal
cross-axis observable \(\chi=\mathbf1\{s_{-1}=s_1\}\), odd decimation turns
the orbit sum into nearest-neighbor equality energy on a reflected binary
chain. Thus

\[
F_{2m+1}(q)=2q(1+q^2)^m,\qquad
E_n(q)=\sum_{k\mid n}\mu(k)F_{n/k}(q^k),
\]

where \(E_n\) is the primitive weighted polynomial. The orbit-resolved
pressure is

\[
P_{\rm orb}(s)=\frac12\log(1+e^{-2s}),
\]

and its exact gap from P68's affine mean-field pressure is
\(\frac12\log\cosh s\), strictly positive for every \(s\ne0\). This is a
global cumulant theorem, not only a variance diagnostic. Route A remains
exploratory and Route B is not authorized. P70 will feed the exact primitive
polynomials into the full orbit-resolved Euler product.

- [P69 overview](henon_orbit_resolved_reflection_cumulant_pressure/README.md)
- [P69 paper](henon_orbit_resolved_reflection_cumulant_pressure/paper/paper.pdf)
- [P69 proof package](henon_orbit_resolved_reflection_cumulant_pressure/PROOF_PACKAGE.md)
- [P69 certificate](henon_orbit_resolved_reflection_cumulant_pressure/results/c69_certificate.json)

## HCS-P70 orbit-resolved reflection Euler boundary

P70 restores one Euler factor for every primitive marked reflection word:

\[
\mathcal Z_{\rm orb}(z,q)=
\prod_{n\ {\rm odd}}\prod_{\omega\in A_n}
(1-z^nq^{S_n\chi(\omega)})^{-1}.
\]

Its logarithmic derivative has exact coefficient
\(\sum_{n\mid m}nE_n(q^{m/n})\). For every \(q>0\), the radius is

\[
R(q)=(1+q^2)^{-1/2},
\]

and the logarithm has one explicit simple-pole principal part, so the product
has an exponential essential singularity. The mean-field radius
\((2q)^{-1/2}\) is strictly too large unless \(q=1\). Route A now has a full
orbit-resolved Euler germ and partial analytic structure, but no arithmetic
trace; Route B is not authorized. P71 will test an explicit relative
counterterm against source-native flip/Lind zeta structure.

- [P70 overview](henon_orbit_resolved_reflection_euler_boundary/README.md)
- [P70 paper](henon_orbit_resolved_reflection_euler_boundary/paper/paper.pdf)
- [P70 proof package](henon_orbit_resolved_reflection_euler_boundary/PROOF_PACKAGE.md)
- [P70 certificate](henon_orbit_resolved_reflection_euler_boundary/results/c70_certificate.json)

## HCS-P71 relative Lind counterterm

P71 compares P70 with the primary-source full two-shift reverse Lind zeta.
In the boundary coordinate \(u=1-\sqrt2t\), the full Lind logarithm has
exponential coefficient \(1/\sqrt2+3/4\) and branch coefficient \(-1/2\);
the odd packet accounts for only \(1/\sqrt2\). Consequently

\[
u^{1/2}e^{-3/(4u)}
\frac{\zeta_{\rm flip}(t)}{\mathcal Z_{\rm orb}(t,1)}
\]

extends holomorphically and nonvanishingly across \(u=0\) as a local branch
germ. Among counterterms \(u^\beta e^{-c/u}\), this forces uniquely
\((c,\beta)=(3/4,1/2)\). Thus a source-native local bridge exists, but odd
packet data alone is incomplete. Global continuation, zeros, and a transfer
determinant remain open; Route B is not authorized.

- [P71 overview](henon_relative_lind_counterterm/README.md)
- [P71 paper](henon_relative_lind_counterterm/paper/paper.pdf)
- [P71 proof package](henon_relative_lind_counterterm/PROOF_PACKAGE.md)
- [P71 certificate](henon_relative_lind_counterterm/results/c71_certificate.json)

## HCS-P72 relative Lind essential-singularity ladder

P72 globalizes the exact logarithmic ledger far enough to test P71's local
counterterm. Primitive and repetition indices regroup into

\[
\log\mathcal Z_{\rm orb}(t,1)
=\sum_{m\ge1}c_m\frac{2t^m}{1-2t^{2m}},\qquad
c_m=\frac1m\prod_{\substack{p\mid m\\p\ {\rm odd}}}(1-p).
\]

No channel vanishes. The P71 counterterm removes the \(m=1\) singularity,
but for every \(m\ge2\) the relative continuation has an exponential
essential singularity at \(\rho_m=2^{-1/(2m)}\), and these points increase
to one. Thus the local bridge cannot be a meromorphic/Fredholm determinant
on the entire unit disk. A punctured-domain infinite-rank renormalization is
the surviving analytic direction. Arithmetic advance is NO and Route B is
not authorized.

- [P72 overview](henon_relative_lind_essential_ladder/README.md)
- [P72 paper](henon_relative_lind_essential_ladder/paper/paper.pdf)
- [P72 proof package](henon_relative_lind_essential_ladder/PROOF_PACKAGE.md)
- [P72 certificate](henon_relative_lind_essential_ladder/results/c72_certificate.json)
- [P68--P72 batch review](BATCH_REVIEW_P68_P72.md)

## HCS-P73 relative Lind full-ladder counterterm

P73 treats every complex pole of P72 separately.  With

\[
\alpha_{m,k}=2^{-1/(2m)}e^{\pi i k/m},\qquad
b_{m,k}=\frac{c_m(-1)^k}{\sqrt2\,m},
\]

one has the exact partial fractions

\[
c_m\Phi(t^m)=\sum_{k=0}^{2m-1}
\frac{b_{m,k}}{1-t/\alpha_{m,k}}.
\]

The raw pole family is not absolutely summable.  Subtracting the Taylor
polynomial through degree \(m-1\) makes the individual pole factors normally
and unconditionally summable on compact punctured subsets, without changing
their level sum.  After also cancelling the residual source singularity at
\(w=1+\sqrt2t=0\), the normalized full counterterm satisfies
\(K_{\rm all}C_{\rm rel}=1\) on every compatible branch.  This is exact
all-channel renormalization, but it copies the entire packet ledger and is
not an independent determinant or transfer operator.  Arithmetic advance is
NO and Route B is not authorized.

- [P73 overview](henon_relative_lind_full_ladder_counterterm/README.md)
- [P73 paper](henon_relative_lind_full_ladder_counterterm/paper/paper.pdf)
- [P73 proof package](henon_relative_lind_full_ladder_counterterm/PROOF_PACKAGE.md)
- [P73 certificate](henon_relative_lind_full_ladder_counterterm/results/c73_certificate.json)

## HCS-P74 all-channel counterterm gauge rigidity

P74 determines exactly what the singular divisor fixes.  In the channel-log
class

\[
W_{d,G}(t)=\exp\!\left(\sum_{m\ge2}d_m\Phi(t^m)+G(t)\right),
\]

removability at every channel radius forces \(d_m=c_m\) coefficientwise.
Requiring the source-cancelled object to extend holomorphically and nowhere
zero across the remaining negative source point uniquely forces the
power-exponential pair \((a,\beta)=(3/4,1/2)\).  The divisor leaves the
nowhere-zero holomorphic factor \(e^G\) completely free, however, and no
finite Taylor jet fixes that gauge.

The genus-\(m-1\) convention cancels the channel sector.  The forced source
factor then leaves \(e^{-3/2}\), and the stated final scalar normalization
\(e^{3/2}\) makes the full residual \(1\).  Under the same final scalar
normalization, the equally explicit source-preserving genus-\(m\) convention
leaves

\[
\exp\!\left(-2\sum_{m\ge2}c_mt^m\right)
=e^{2t}\prod_{\substack{d\ge1\\d\ {\rm odd}}}
(1-t^d)^{2\mu(d)}.
\]

Thus singular cancellation is rigid modulo holomorphic gauge, while no
finite basepoint jet selects a unique gauge.  Whether independent
source-native structure supplies a canonical normalization remains open.
No operator or arithmetic ownership follows; Route B is not authorized.

- [P74 overview](henon_all_channel_counterterm_gauge_rigidity/README.md)
- [P74 paper](henon_all_channel_counterterm_gauge_rigidity/paper/paper.pdf)
- [P74 proof package](henon_all_channel_counterterm_gauge_rigidity/PROOF_PACKAGE.md)
- [P74 certificate](henon_all_channel_counterterm_gauge_rigidity/results/c74_certificate.json)

## HCS-P75 weighted reflection scalar-channel divisor

P75 extends the exact regrouping to the full P70 weight family:

\[
\log\mathcal Z_{\rm orb}(z,q)
=\sum_{m\ge1}c_m
\frac{2(qz)^m}{1-(1+q^{2m})z^{2m}}.
\]

The coefficient \(c_m\) is unchanged and never vanishes.  Introduce an
independent fugacity \(w\).  On the bidisk the lifted channels are
\(2w^m/(1-z^{2m}-w^{2m})\), with polar hypersurfaces

\[
H_m:\quad z^{2m}+w^{2m}=1.
\]

They are smooth and locally finite in the bidisk, and the channel series is
normally convergent on compact subsets of their complement.  Restricting to
the physical fiber \(w=qz\) recovers the positive-\(q\) family.  On every
such fiber the \(m\)th channel has \(2m\) explicitly phased roots
and a nonzero exact principal coefficient.  P75 does not claim the dense
limiting boundary, a weighted Lind source for \(q\ne1\), an operator, or
arithmetic semantics.  Route B remains unauthorized.

- [P75 overview](henon_weighted_reflection_channel_divisor/README.md)
- [P75 paper](henon_weighted_reflection_channel_divisor/paper/paper.pdf)
- [P75 proof package](henon_weighted_reflection_channel_divisor/PROOF_PACKAGE.md)
- [P75 certificate](henon_weighted_reflection_channel_divisor/results/c75_certificate.json)

## HCS-P76 weighted reflection natural-boundary circle

P76 globalizes P75 on every fixed positive weight fiber.  Its singular radii

\[
\rho_m(q)=(1+q^{2m})^{-1/(2m)}
\]

increase strictly to \(L(q)=\min(1,q^{-1})\).  Every point

\[
\rho_m(q)e^{\pi i k/m},\qquad 0\le k<2m,
\]

is an exponential essential singularity, and the angular mesh has gap
\(\pi/m\).  The roots therefore accumulate at every point of
\(|z|=L(q)\), proving that this circle is a natural boundary for the exact
unrenormalized punctured continuation.  For \(q>1\) the limiting circle lies
strictly inside the unit disk.

The theorem is deliberately object-specific: an all-channel counterterm
changes the function.  It proves no source-native operator, arithmetic
trace, or Route-B statement.

- [P76 overview](henon_weighted_reflection_natural_boundary/README.md)
- [P76 paper](henon_weighted_reflection_natural_boundary/paper/paper.pdf)
- [P76 proof package](henon_weighted_reflection_natural_boundary/PROOF_PACKAGE.md)
- [P76 certificate](henon_weighted_reflection_natural_boundary/results/c76_certificate.json)

## HCS-P77 tautological Fredholm ownership firewall

P77 separates analytic representability from dynamical ownership.  For each
fixed \(q>0\), on P76's punctured domain
\(\Omega_q=\{|z|<\min(1,q^{-1})\}\setminus\Sigma_q\),

\[
A(z,q)=\operatorname{diag}\bigl(c_m\Psi_m(z,q)\bigr)
\]

is locally trace class, so \(K=e^A-I\) is trace class and

\[
\det_F(I+K)=e^{\operatorname{Tr}A}
=\exp\!\left(\sum_m c_m\Psi_m\right).
\]

This is an exact determinant representation, but it is post hoc and
parameter dependent.  Indeed every nonvanishing holomorphic function \(F\)
has the rank-one representation
\(\det_F(I+(F-1)P)=F\).

The source-native alternative behaves oppositely.  A weighted cyclic block
\(B_\omega\) owns the Euler denominator polynomial
\[
\det(I-zB_\omega)=1-z^nq^{S_n\chi(\omega)},
\]
whose reciprocal is the corresponding P70 Euler factor.  Its singular
values are the edge weights in \(\{1,q\}\).  Infinitely
many primitive singleton reflection words therefore give singular values
bounded below by \(\min(1,q)>0\); the full orbit-block direct sum is
noncompact, so for \(z\ne0\) the standard trace-class determinant
\(\det_F(I-zB_q)\) is not defined.  A genuine compact or
nuclear source-native transfer owner remains open.  Arithmetic advance is
NO and Route B is not authorized.

- [P77 overview](henon_tautological_fredholm_ownership_firewall/README.md)
- [P77 paper](henon_tautological_fredholm_ownership_firewall/paper/paper.pdf)
- [P77 proof package](henon_tautological_fredholm_ownership_firewall/PROOF_PACKAGE.md)
- [P77 certificate](henon_tautological_fredholm_ownership_firewall/results/c77_certificate.json)
- [P73--P77 batch plan](BATCH_PLAN_P73_P77.md)
- [P73--P77 batch review](BATCH_REVIEW_P73_P77.md)

## Route-A dynamics-variant round C104--C108

This round tests five distinct Hénon subtypes while preserving the
`NO_BAD_EULER_OR_ROOT_NUMBER` firewall.  Each entry below has a complete
research package and a compiled paper PDF; finite prefixes are reported with
their exact evidence boundary and are not promoted to Route B.

- [C104 polynomial multi-branch pilot](henon_polynomial_multibranch_route_a/README.md) · [paper PDF](henon_polynomial_multibranch_route_a/paper/main.pdf)
- [C105 kneading/pruning prefix](henon_kneading_pruning_hofbauer/README.md) · [paper PDF](henon_kneading_pruning_hofbauer/paper/main.pdf)
- [C106 variational coupled Hénon lattice](henon_variational_coupled_henon_lattice/README.md) · [paper PDF](henon_variational_coupled_henon_lattice/paper/main.pdf)
- [C107 open-hole survivor transfer](henon_open_hole_route_a/README.md) · [paper PDF](henon_open_hole_route_a/paper/main.pdf)
- [C108 complex holomorphic transfer gate](henon_holomorphic_complex_transfer/README.md) · [paper PDF](henon_holomorphic_complex_transfer/paper/main.pdf)

See the [C104--C108 batch plan](BATCH_PLAN_C104_C108.md) and
[batch review](BATCH_REVIEW_C104_C108.md) for the exact artifact ledger,
uniform audit, and current Route-A tuple.

## Route-A dynamics-variant round C109--C113

This round broadens the A-route search across five distinct Hénon subtypes:
dissipative, periodically forced Floquet, three-site variational/symplectic,
piecewise-affine border-collision, and third-order memory dynamics.  Each
entry is a complete finite paper package with exact evidence, independent
validation, hostile mutation tests, and a compiled PDF.  The finite prefixes
are reported with their evidence boundaries and are not promoted to Route B.

- [C109 dissipative Hénon](henon_dissipative_route_a/README.md) · [paper PDF](henon_dissipative_route_a/paper/main.pdf)
- [C110 non-autonomous Floquet Hénon](henon_nonautonomous_floquet_route_a/README.md) · [paper PDF](henon_nonautonomous_floquet_route_a/paper/main.pdf)
- [C111 three-site variational ring](henon_three_site_variational_lattice/README.md) · [paper PDF](henon_three_site_variational_lattice/paper/main.pdf)
- [C112 piecewise-affine border collision](henon_piecewise_affine_border_collision_route_a/README.md) · [paper PDF](henon_piecewise_affine_border_collision_route_a/paper/main.pdf)
- [C113 third-order memory Hénon](henon_third_order_memory_route_a/README.md) · [paper PDF](henon_third_order_memory_route_a/paper/main.pdf)

See the [C109--C113 batch plan](BATCH_PLAN_C109_C113.md) and
[batch review](BATCH_REVIEW_C109_C113.md) for the full hash ledger, uniform
audit, and the unchanged global Route-A tuple.

## Route-A dynamics-variant round C114--C118

This round keeps the A-route priority while widening the dynamical design
space again: a finite local Koopman jet, a rational reversible McMillan/QRT
map, a nonsmooth Lozi map, a Markov-switching H\'enon cocycle, and a damped
conformally symplectic two-site dimer.  Each paper has exact evidence,
independent validation, hostile mutation tests, a closed manifest, and a
reproducible compiled PDF.  Every local or finite prefix retains its explicit
scope boundary.

- [C114 local jet Koopman quotient](henon_local_jet_koopman_route_a/README.md) · [paper PDF](henon_local_jet_koopman_route_a/paper/main.pdf)
- [C115 rational reversible McMillan/QRT map](henon_mcmillan_rational_route_a/README.md) · [paper PDF](henon_mcmillan_rational_route_a/paper/main.pdf)
- [C116 nonsmooth Lozi itinerary pruning](henon_lozi_nonsmooth_route_a/README.md) · [paper PDF](henon_lozi_nonsmooth_route_a/paper/main.pdf)
- [C117 Markov-switching tangent moments](henon_markov_switching_moment_route_a/README.md) · [paper PDF](henon_markov_switching_moment_route_a/paper/main.pdf)
- [C118 conformally symplectic damped dimer](henon_conformally_symplectic_dimer_route_a/README.md) · [paper PDF](henon_conformally_symplectic_dimer_route_a/paper/main.pdf)

See the [C114--C118 batch plan](BATCH_PLAN_C114_C118.md) and
[batch review](BATCH_REVIEW_C114_C118.md) for the exact hash ledger, release
audit, integrity checks, and the unchanged global Route-A tuple.

## Route-A dynamics-variant round C119--C123

This round continues the A-route diversity strategy with a trace-class
bosonic-Fock contraction, a quartic variational three-cycle, a projectively
algebraically stable polynomial automorphism, a three-dimensional
adaptive-feedback automorphism, and an iid additive-noise moment system.  Each
entry is a complete paper package with exact evidence, independent validation,
hostile mutation tests, a closed manifest, and a reproducible compiled PDF.
Local, low-period, finite-word, and finite-moment boundaries remain explicit.

- [C119 trace-class bosonic-Fock contraction](henon_fock_nuclear_contraction_route_a/README.md) · [paper PDF](henon_fock_nuclear_contraction_route_a/paper/main.pdf)
- [C120 quartic variational period-three certificate](henon_quartic_variational_period3_route_a/README.md) · [paper PDF](henon_quartic_variational_period3_route_a/paper/main.pdf)
- [C121 projective algebraic stability](henon_projective_algebraic_stability_route_a/README.md) · [paper PDF](henon_projective_algebraic_stability_route_a/paper/main.pdf)
- [C122 adaptive-feedback Hénon automorphism](henon_adaptive_feedback_route_a/README.md) · [paper PDF](henon_adaptive_feedback_route_a/paper/main.pdf)
- [C123 additive-noise Hénon moments](henon_additive_noise_moment_route_a/README.md) · [paper PDF](henon_additive_noise_moment_route_a/paper/main.pdf)

See the [C119--C123 batch plan](BATCH_PLAN_C119_C123.md) and
[batch review](BATCH_REVIEW_C119_C123.md) for the exact artifact ledger,
uniform audit, integrity/failure-mode review, and the strict per-candidate
Route-A verdicts.

## Route-A structural-gate round C124--C128

This round keeps subtype diversity but raises the progress threshold: each
paper closes an all-period, parameter-uniform, natural-operator, or exact
obstruction gate.  The five systems are a graph-directed analytic Hénon IFS,
an Anosov torus automorphism, a critical Chebyshev contracting skew product,
a parameter-uniform affine horseshoe, and an exact finite metaplectic lift.
Every entry has exact evidence, independent reconstruction, hostile mutation
tests, a package-local Route-A evaluation, a closed manifest, and a
reproducible paper PDF.

- [C124 graph-directed Hardy--Fredholm bridge](henon_graph_directed_hardy_trace_route_a/README.md) · [paper PDF](henon_graph_directed_hardy_trace_route_a/paper/main.pdf)
- [C125 Anosov zeta and Koopman obstruction](henon_anosov_zeta_koopman_obstruction_route_a/README.md) · [paper PDF](henon_anosov_zeta_koopman_obstruction_route_a/paper/main.pdf)
- [C126 Chebyshev contracting skew product](henon_chebyshev_contracting_skew_route_a/README.md) · [paper PDF](henon_chebyshev_contracting_skew_route_a/paper/main.pdf)
- [C127 uniform affine Hénon horseshoe](henon_uniform_affine_horseshoe_route_a/README.md) · [paper PDF](henon_uniform_affine_horseshoe_route_a/paper/main.pdf)
- [C128 finite metaplectic Hénon quantization](henon_finite_metaplectic_quantization_route_a/README.md) · [paper PDF](henon_finite_metaplectic_quantization_route_a/paper/main.pdf)

See the [C124--C128 batch plan](BATCH_PLAN_C124_C128.md) and
[batch review](BATCH_REVIEW_C124_C128.md) for the progress gates, exact hash
ledger, uniform release audit, and conservative Route-A boundary.

## Route-A structural-gate round C129--C133

This round continues the explicit-progress rule across five further dynamical
subtypes: a phase-sensitive graph-directed affine IFS, an irrational-roof
symbolic suspension, an all-odd metaplectic family, a nonlinear
Möbius--Bergman trace owner, and a metric quantum graph.  Each entry has an
all-period or uniform structural theorem, exact controls, independent
validation, hostile mutation tests, a closed manifest, and a reproducible
paper PDF.  Phase, clock, quantization, nonlinear order, and scattering
boundaries remain separate.

- [C129 graph-directed phase holonomy](henon_graph_directed_phase_holonomy_route_a/README.md) · [paper PDF](henon_graph_directed_phase_holonomy_route_a/paper/main.pdf)
- [C130 irrational-roof suspension](henon_irrational_roof_suspension_route_a/README.md) · [paper PDF](henon_irrational_roof_suspension_route_a/paper/main.pdf)
- [C131 all-odd metaplectic family](henon_odd_level_metaplectic_family_route_a/README.md) · [paper PDF](henon_odd_level_metaplectic_family_route_a/paper/main.pdf)
- [C132 nonlinear Möbius--Bergman trace owner](henon_mobius_bergman_trace_route_a/README.md) · [paper PDF](henon_mobius_bergman_trace_route_a/paper/main.pdf)
- [C133 metric quantum-graph unitary scattering](henon_quantum_graph_unitary_scattering_route_a/README.md) · [paper PDF](henon_quantum_graph_unitary_scattering_route_a/paper/main.pdf)

See the [C129--C133 batch plan](BATCH_PLAN_C129_C133.md) and
[batch review](BATCH_REVIEW_C129_C133.md) for the exact progress claims,
artifact ledger, uniform release audit, and strict per-candidate Route-A
tuples.  The common scope is `NO_BAD_EULER_OR_ROOT_NUMBER`, every package has
`route_b_invocation_allowed=false`, and no coordinates are combined across
candidates.

## Route-A refinement round C134--C138

This round converts five boundaries from C129--C133 into new exact tests: a
faithful character torus, a directed-edge roof, CRT-compatible generalized
metaplectic characters, a uniform nonlinear Bergman family, and a magnetic
quantum graph.  Every paper records one explicit structural advance together
with the obstruction that remains.  Exact evidence, independent validation,
hostile mutation tests, closed manifests, and reproducible PDF papers are
retained package by package.

- [C134 faithful character-torus recovery](henon_faithful_character_torus_route_a/README.md) · [paper PDF](henon_faithful_character_torus_route_a/paper/main.pdf)
- [C135 directed-edge nonlattice suspension](henon_edge_roof_suspension_route_a/README.md) · [paper PDF](henon_edge_roof_suspension_route_a/paper/main.pdf)
- [C136 CRT-compatible metaplectic characters](henon_crt_metaplectic_compatibility_route_a/README.md) · [paper PDF](henon_crt_metaplectic_compatibility_route_a/paper/main.pdf)
- [C137 uniform Möbius--Bergman family](henon_uniform_mobius_bergman_family_route_a/README.md) · [paper PDF](henon_uniform_mobius_bergman_family_route_a/paper/main.pdf)
- [C138 magnetic theta-graph scattering](henon_magnetic_quantum_graph_route_a/README.md) · [paper PDF](henon_magnetic_quantum_graph_route_a/paper/main.pdf)

See the [C134--C138 batch plan](BATCH_PLAN_C134_C138.md) and
[batch review](BATCH_REVIEW_C134_C138.md) for the exact hash ledger, uniform
release audit, cross-review repairs, and conservative Route-A tuples.  The
common scope remains `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is unauthorized.

## Route-A dynamics-diversification round C139--C143

This round tests five deliberately different source mechanisms: a finite-
memory symbolic roof, a strictly sofic suspension, a nonlinear complex
inverse-branch operator, a countable renewal operator, and an inhomogeneous
coined quantum walk.  Each paper proves an all-period or analytic structural
advance and retains an exact negative control.  The packages include
independent validation, hostile mutation tests, closed manifests, and
reproducible PDF papers.

- [C139 four-block marker suspension](henon_four_block_marker_suspension_route_a/README.md) · [paper PDF](henon_four_block_marker_suspension_route_a/paper/main.pdf)
- [C140 strictly sofic mod-three suspension](henon_mod3_sofic_suspension_route_a/README.md) · [paper PDF](henon_mod3_sofic_suspension_route_a/paper/main.pdf)
- [C141 quadratic inverse-branch Ruelle ladder](henon_quadratic_inverse_branch_ruelle_route_a/README.md) · [paper PDF](henon_quadratic_inverse_branch_ruelle_route_a/paper/main.pdf)
- [C142 trace-class countable renewal operator](henon_trace_class_renewal_operator_route_a/README.md) · [paper PDF](henon_trace_class_renewal_operator_route_a/paper/main.pdf)
- [C143 inhomogeneous coined quantum walk](henon_inhomogeneous_coined_quantum_walk_route_a/README.md) · [paper PDF](henon_inhomogeneous_coined_quantum_walk_route_a/paper/main.pdf)

See the [C139--C143 batch plan](BATCH_PLAN_C139_C143.md) and
[batch review](BATCH_REVIEW_C139_C143.md) for the exact progress ledger,
content-addressed artifacts, cross-review repairs, and uniform release audit.
The five Route-A coordinates remain separate.  Their common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B remains unauthorized.

## Route-A dynamics-diversification round C144--C148

This round again changes dynamical subtype paper by paper: a minimal
substitution subshift, a two-clock cellular automaton, a nilmanifold
automorphism, an integrable billiard, and an open Walsh quantum gate.  Each
paper closes an all-period structural theorem or obstruction and includes an
exact negative control.  The packages retain producer-independent checks,
separate symbolic reconstruction, hostile mutation tests, closed manifests,
and reproducible PDF papers.

- [C144 Thue--Morse periodic-orbit vacuum](henon_thue_morse_periodic_orbit_vacuum_route_a/README.md) · [paper PDF](henon_thue_morse_periodic_orbit_vacuum_route_a/paper/main.pdf)
- [C145 Rule-90 two-clock periodic geometry](henon_rule90_two_clock_periodic_geometry_route_a/README.md) · [paper PDF](henon_rule90_two_clock_periodic_geometry_route_a/paper/main.pdf)
- [C146 Heisenberg nilmanifold clean fixed sets](henon_heisenberg_nilmanifold_clean_fixed_sets_route_a/README.md) · [paper PDF](henon_heisenberg_nilmanifold_clean_fixed_sets_route_a/paper/main.pdf)
- [C147 rectangular-billiard primitive families](henon_rectangular_billiard_orbit_family_route_a/README.md) · [paper PDF](henon_rectangular_billiard_orbit_family_route_a/paper/main.pdf)
- [C148 open Walsh quantum-baker scattering gate](henon_open_walsh_baker_scattering_route_a/README.md) · [paper PDF](henon_open_walsh_baker_scattering_route_a/paper/main.pdf)

See the [C144--C148 batch plan](BATCH_PLAN_C144_C148.md) and
[batch review](BATCH_REVIEW_C144_C148.md) for the exact progress ledger,
content-addressed artifacts, cross-review repairs, and uniform release audit.
The five Route-A coordinates are not combined.  Their common scope remains
`NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B remains unauthorized.

## Route-A dynamics-refinement round C149--C153

This round turns the five explicit C144--C148 boundaries into new exact
tests: a finite periodic attachment to an aperiodic symbolic component, a
Mersenne scaling family for Rule 90, character-resolved nilmanifold fibre
rotations, a primitive billiard-direction heat transform, and a controlled
growing-size limit for the open Walsh gate.  Each paper records a genuine
all-parameter theorem or exact classification together with the remaining
obstruction.  Producer-independent checks, separate symbolic
reconstructions, hostile mutations, closed manifests, and reproducible PDF
papers are retained package by package.

- [C149 Thue--Morse finite periodic skeleton](henon_thue_morse_finite_periodic_skeleton_route_a/README.md) · [paper PDF](henon_thue_morse_finite_periodic_skeleton_route_a/paper/main.pdf)
- [C150 Rule-90 Mersenne scaling family](henon_rule90_mersenne_scaling_route_a/README.md) · [paper PDF](henon_rule90_mersenne_scaling_route_a/paper/main.pdf)
- [C151 character-resolved Heisenberg fibres](henon_heisenberg_character_resolved_fibre_route_a/README.md) · [paper PDF](henon_heisenberg_character_resolved_fibre_route_a/paper/main.pdf)
- [C152 primitive billiard-family heat transform](henon_billiard_primitive_heat_trace_route_a/README.md) · [paper PDF](henon_billiard_primitive_heat_trace_route_a/paper/main.pdf)
- [C153 growing-`k` open Walsh escape](henon_open_walsh_growing_k_escape_route_a/README.md) · [paper PDF](henon_open_walsh_growing_k_escape_route_a/paper/main.pdf)

See the [C149--C153 batch plan](BATCH_PLAN_C149_C153.md) and
[batch review](BATCH_REVIEW_C149_C153.md) for the theorem ledger,
content-addressed artifacts, failed-conjecture record, cross-review repairs,
and uniform release audit.  The common scope remains
`NO_BAD_EULER_OR_ROOT_NUMBER`; the five Route-A coordinates are not combined,
and Route B remains unauthorized.

## Route-A dynamics-refinement round C154--C158

This round replaces five residual qualitative boundaries by exact structure
or scaling theorems: a single heteroclinic symbolic orbit closure, Rule-90
full-period concentration, a Heisenberg primary quadratic module, the
Dirichlet square-billiard Abel trace, and a full-cycle open-Walsh secular
limit.  The papers keep these dynamical subtypes separate and record the
remaining obstruction beside every positive result.

- [C154 Thue--Morse/period-three heteroclinic closure](henon_thue_morse_heteroclinic_period3_route_a/README.md) · [paper PDF](henon_thue_morse_heteroclinic_period3_route_a/paper/main.pdf)
- [C155 Mersenne Rule-90 full-period concentration](henon_rule90_mersenne_full_period_concentration_route_a/README.md) · [paper PDF](henon_rule90_mersenne_full_period_concentration_route_a/paper/main.pdf)
- [C156 Heisenberg primary quadratic module](henon_heisenberg_primary_quadratic_module_route_a/README.md) · [paper PDF](henon_heisenberg_primary_quadratic_module_route_a/paper/main.pdf)
- [C157 square-billiard Dirichlet Abel trace](henon_square_billiard_abel_wave_trace_route_a/README.md) · [paper PDF](henon_square_billiard_abel_wave_trace_route_a/paper/main.pdf)
- [C158 open-Walsh full-cycle secular scaling](henon_open_walsh_full_cycle_secular_scaling_route_a/README.md) · [paper PDF](henon_open_walsh_full_cycle_secular_scaling_route_a/paper/main.pdf)

See the [C154--C158 batch plan](BATCH_PLAN_C154_C158.md) and
[batch review](BATCH_REVIEW_C154_C158.md) for the proof ledger,
content-addressed artifacts, internal cross-review repairs, and uniform
release audit.  The common scope remains `NO_BAD_EULER_OR_ROOT_NUMBER`; the
five Route-A coordinates are not combined, and Route B remains unauthorized.

## Route-A theorem-progress round C159--C163

This round enforces a theorem-first gate: every retained paper contributes an
all-parameter identity, limit law, classification, or obstruction stronger
than its predecessor.  A clock-decorated Sturmian candidate and an incomplete
Heisenberg all-iterate evaluation were rejected; the round pivoted to a
mixing Thue--Morse S-gap shift and finite cyclic quadratic Birkhoff amplitudes.
The other three papers sharpen Rule-90 cycle sieving, square-billiard Abel
boundary coefficients, and open-Walsh phase statistics.

- [C159 mixing Thue--Morse S-gap shift and natural boundary](henon_thue_morse_s_gap_natural_boundary_route_a/README.md) · [paper PDF](henon_thue_morse_s_gap_natural_boundary_route_a/paper/main.pdf)
- [C160 exact Rule-90 maximal-subgroup period sieve](henon_rule90_maximal_subgroup_sieve_route_a/README.md) · [paper PDF](henon_rule90_maximal_subgroup_sieve_route_a/paper/main.pdf)
- [C161 finite cyclic quadratic Birkhoff amplitudes](henon_finite_cyclic_quadratic_birkhoff_route_a/README.md) · [paper PDF](henon_finite_cyclic_quadratic_birkhoff_route_a/paper/main.pdf)
- [C162 square-billiard renormalized branch amplitudes](henon_square_billiard_renormalized_branch_amplitude_route_a/README.md) · [paper PDF](henon_square_billiard_renormalized_branch_amplitude_route_a/paper/main.pdf)
- [C163 open-Walsh phase equidistribution](henon_open_walsh_phase_equidistribution_route_a/README.md) · [paper PDF](henon_open_walsh_phase_equidistribution_route_a/paper/main.pdf)

See the [C159--C163 batch plan](BATCH_PLAN_C159_C163.md) and
[batch review](BATCH_REVIEW_C159_C163.md) for the theorem ledger, rejected
candidate record, content-addressed artifacts, cross-review repairs, and
uniform release audit.  The common scope remains
`NO_BAD_EULER_OR_ROOT_NUMBER`; the five source systems remain separate and
Route B remains unauthorized.

## Route-A theorem-progress round C164--C168

This round keeps the theorem-first gate and broadens the dynamical mix: an
induced renewal Fredholm family, a reversible Margolus cellular automaton, a
high-dimensional dyadic skew tower, a continuously deformed rectangular
billiard, and a natural rank-three open Walsh gate.  Repeated or unsupported
candidate lines were explicitly pivoted before paper release.  Each retained
paper proves an all-parameter identity, classification, limit law, or
obstruction and states its remaining boundary beside the theorem.

- [C164 induced Thue--Morse first-return Fredholm owner](henon_thue_morse_induced_fredholm_owner_route_a/README.md) · [paper PDF](henon_thue_morse_induced_fredholm_owner_route_a/paper/main.pdf)
- [C165 reversible Margolus necklace period law](henon_margolus_necklace_period_law_route_a/README.md) · [paper PDF](henon_margolus_necklace_period_law_route_a/paper/main.pdf)
- [C166 dyadic Pascal skew-tower period theorem](henon_dyadic_pascal_skew_tower_route_a/README.md) · [paper PDF](henon_dyadic_pascal_skew_tower_route_a/paper/main.pdf)
- [C167 rectangular-billiard deformation branches](henon_rectangular_billiard_deformation_branch_route_a/README.md) · [paper PDF](henon_rectangular_billiard_deformation_branch_route_a/paper/main.pdf)
- [C168 natural rank-three open-Walsh phase law](henon_open_walsh_rank_three_phase_route_a/README.md) · [paper PDF](henon_open_walsh_rank_three_phase_route_a/paper/main.pdf)

See the [C164--C168 batch plan](BATCH_PLAN_C164_C168.md) and
[batch review](BATCH_REVIEW_C164_C168.md) for the exact theorem ledger,
candidate-pivot record, content-addressed artifacts, hostile cross-review,
and uniform release audit.  The five coordinates remain separate.  Their
common scope is `NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B remains
unauthorized.

## Route-A theorem-progress round C169--C173

This round applies the expanded `A0--A4` roadmap and changes dynamical subtype
in every paper: a parabolic Furstenberg skew shift, a deterministic Kac
scatterer ring, a reversible Ehrenfest chain, a primitive finite-field
multiplier, and the nonlinear integrable Lyness map.  An Anosov torus family,
a baker-map continuation, and a generic complete-graph Hashimoto factorization
were screened out as collisions with earlier repository lines.  Each retained
paper closes an all-parameter theorem or exact obstruction and exposes its
arithmetic and determinant boundary beside the result.

- [C169 irrational Furstenberg skew-shift spectrum](henon_furstenberg_skew_shift_spectral_route_a/README.md) · [paper PDF](henon_furstenberg_skew_shift_spectral_route_a/paper/main.pdf)
- [C170 all-marker Kac-ring cycle classification](henon_kac_ring_cycle_classification_route_a/README.md) · [paper PDF](henon_kac_ring_cycle_classification_route_a/paper/main.pdf)
- [C171 Ehrenfest hypercube trace and Krawtchouk lumping](henon_ehrenfest_hypercube_trace_route_a/README.md) · [paper PDF](henon_ehrenfest_hypercube_trace_route_a/paper/main.pdf)
- [C172 primitive finite-field multiplier](henon_primitive_field_multiplier_route_a/README.md) · [paper PDF](henon_primitive_field_multiplier_route_a/paper/main.pdf)
- [C173 Lyness five-cycle determinant obstruction](henon_lyness_five_cycle_obstruction_route_a/README.md) · [paper PDF](henon_lyness_five_cycle_obstruction_route_a/paper/main.pdf)

See the [C169--C173 batch plan](BATCH_PLAN_C169_C173.md) and
[batch review](BATCH_REVIEW_C169_C173.md) for the A0--A4 theorem ledger,
candidate pivots, content-addressed artifacts, two integrity gates, and uniform
release audit.  The five source systems and their verdict coordinates remain
separate.  The common scope is `NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B
remains unauthorized.

## Route-A theorem-progress round C174--C178

This round takes larger theorem steps and changes subtype in every paper: an
odd-affine 2-adic renewal, the Rule-184 traffic cellular automaton, recurrent
Abelian sandpile stabilization, smooth expanding circle endomorphisms, and a
classical/quantum harmonic-oscillator strobe.  Finite-field Frobenius,
logistic/tent, and Gauss/Farey candidates were screened out before release;
rotor-router, Lattès, and Morse--Smale alternatives remain future pivots.

- [C174 odd-affine 2-adic parity renewal and clock recovery](henon_dyadic_odd_affine_parity_renewal_route_a/README.md) · [paper PDF](henon_dyadic_odd_affine_parity_renewal_route_a/paper/main.pdf)
- [C175 cyclic Rule-184 periodic geometry](henon_rule184_traffic_periodic_geometry_route_a/README.md) · [paper PDF](henon_rule184_traffic_periodic_geometry_route_a/paper/main.pdf)
- [C176 recurrent sandpile translation spectrum](henon_sandpile_translation_spectral_route_a/README.md) · [paper PDF](henon_sandpile_translation_spectral_route_a/paper/main.pdf)
- [C177 expanding-circle Wold and sharp mixing law](henon_expanding_circle_wold_route_a/README.md) · [paper PDF](henon_expanding_circle_wold_route_a/paper/main.pdf)
- [C178 harmonic-strobe Gaussian and metaplectic spectra](henon_harmonic_strobe_quantization_route_a/README.md) · [paper PDF](henon_harmonic_strobe_quantization_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C174_C178.md),
[batch plan](BATCH_PLAN_C174_C178.md), and
[batch review](BATCH_REVIEW_C174_C178.md) for candidate pivots, all-parameter
theorems, Route-A verdicts, internal cross-audit repairs, exact release hashes,
and the uniform 472,538-checker/46,114-SymPy audit.  All five source systems
remain separate, all fail A0, and Route B remains unauthorized under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Route-A independent big-step round C179--C183

This round deliberately prevents one manuscript from being split into five.
It changes mathematical owner in every paper: arithmetic congruence returns,
holomorphic elliptic-quotient dynamics, deterministic rotor routing,
ultradiscrete soliton action--angle dynamics, and stochastic symmetric-group
convolution. Each package closes an all-parameter theorem and its sharp
Route-A boundary.

- [C179 Zsigmondy congruence first-return tower](henon_zsigmondy_congruence_return_tower_route_a/README.md) · [paper PDF](henon_zsigmondy_congruence_return_tower_route_a/paper/main.pdf)
- [C180 Lattès three-channel Lefschetz collapse](henon_lattes_three_channel_lefschetz_route_a/README.md) · [paper PDF](henon_lattes_three_channel_lefschetz_route_a/paper/main.pdf)
- [C181 all-digraph rotor-router orbit theorem](henon_rotor_router_strong_digraph_route_a/README.md) · [paper PDF](henon_rotor_router_strong_digraph_route_a/paper/main.pdf)
- [C182 periodic box--ball action--angle classification](henon_periodic_box_ball_action_angle_route_a/README.md) · [paper PDF](henon_periodic_box_ball_action_angle_route_a/paper/main.pdf)
- [C183 random-transposition full partition spectrum](henon_random_transposition_full_spectrum_route_a/README.md) · [paper PDF](henon_random_transposition_full_spectrum_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C179_C183.md),
[batch plan](BATCH_PLAN_C179_C183.md), and
[batch review](BATCH_REVIEW_C179_C183.md) for candidate pivots, exact theorem
increments, source ownership, strict Route-A verdicts, cross-audit repairs,
release hashes, and the uniform 515,765-checker / 91,035-SymPy / 238-mutation /
135-payload / 15-page audit. C179 alone reaches a
weak arithmetic relation because primitive rational-prime divisors arise as
intrinsic first-return moduli; it still lacks a unique global owner and a
logarithmic prime clock. Coordinates remain candidate-local, the common scope
is `NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B remains false.

## Route-A independent dynamical-owner round C184--C188

This round again refuses to turn one manuscript into five installments.  It
changes owner in every paper and closes five all-parameter results: finite
fractal spectral decimation, an isospectral sorting flow, a Hamiltonian
rigid-body atlas, rectangular tableau promotion, and irreducible max-plus
cyclicity.  Each paper includes its singular or degenerate boundary and its
strict stopping result.

- [C184 Sierpiński-gasket spectral decimation](henon_sierpinski_gasket_spectral_decimation_route_a/README.md) · [paper PDF](henon_sierpinski_gasket_spectral_decimation_route_a/paper/main.pdf)
- [C185 Brockett double-bracket sorting flow](henon_brockett_double_bracket_sorting_flow_route_a/README.md) · [paper PDF](henon_brockett_double_bracket_sorting_flow_route_a/paper/main.pdf)
- [C186 triaxial Euler-top elliptic action--angle atlas](henon_euler_top_elliptic_action_angle_route_a/README.md) · [paper PDF](henon_euler_top_elliptic_action_angle_route_a/paper/main.pdf)
- [C187 rectangular tableau-promotion cyclic sieving](henon_rectangular_tableau_promotion_csp_route_a/README.md) · [paper PDF](henon_rectangular_tableau_promotion_csp_route_a/paper/main.pdf)
- [C188 irreducible max-plus projective cyclicity](henon_max_plus_irreducible_cyclicity_route_a/README.md) · [paper PDF](henon_max_plus_irreducible_cyclicity_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C184_C188.md),
[batch plan](BATCH_PLAN_C184_C188.md), and
[batch review](BATCH_REVIEW_C184_C188.md) for collision pivots, source
ownership, exact theorem increments, cross-review repairs, release hashes,
and the uniform executable/PDF audit.  All five fail A0 and therefore remain
`ROUTE_A_REJECTED`; exact source mathematics is retained without manufacturing
arithmetic semantics.  The release totals are 428,425 independent-checker
assertions, 300,647 SymPy checks, 406 hostile rejections, 135 payloads, and
eleven PDF pages.  Coordinates remain separate, the common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B remains false.

## Route-A independent big-step round C189--C193

This round again makes one complete advance per paper and changes the
dynamical owner in every slot.  It closes an arbitrary-common-forcing Möbius
oscillator theorem, an all-deck noninvertible partition theorem, an
all-support-stratum matrix-scaling theorem, an all-arrangement
face-semigroup-walk theorem, and the complete positive Markoff--Vieta descent
tree.  Finite exact censuses remain regression oracles rather than substitutes
for the all-parameter proofs.

- [C189 Watanabe--Strogatz Möbius reduction](henon_watanabe_strogatz_mobius_reduction_route_a/README.md) · [paper PDF](henon_watanabe_strogatz_mobius_reduction_route_a/paper/main.pdf)
- [C190 Bulgarian-solitaire recurrent necklaces](henon_bulgarian_solitaire_recurrent_necklace_route_a/README.md) · [paper PDF](henon_bulgarian_solitaire_recurrent_necklace_route_a/paper/main.pdf)
- [C191 Sinkhorn--Knopp support-stratum dynamics](henon_sinkhorn_knopp_projective_scaling_route_a/README.md) · [paper PDF](henon_sinkhorn_knopp_projective_scaling_route_a/paper/main.pdf)
- [C192 hyperplane chamber walks](henon_hyperplane_chamber_walk_route_a/README.md) · [paper PDF](henon_hyperplane_chamber_walk_route_a/paper/main.pdf)
- [C193 positive Markoff--Vieta descent tree](henon_markoff_vieta_descent_tree_route_a/README.md) · [paper PDF](henon_markoff_vieta_descent_tree_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C189_C193.md),
[batch plan](BATCH_PLAN_C189_C193.md), and
[batch review](BATCH_REVIEW_C189_C193.md) for the model pivots, source
ownership, exact theorem increments, hostile repairs, release hashes and
uniform executable/PDF audit.  The release totals are 692,747
independent-checker assertions, 14,995 SymPy checks, 619 hostile rejections,
135 payloads and ten PDF pages.  C193 alone reaches
`A0_WEAK_ARITHMETIC_RELATION`; it still has no rational-prime primitive
carrier or logarithmic clock, so all five remain `ROUTE_A_REJECTED`.
Coordinates stay candidate-local, scope is `NO_BAD_EULER_OR_ROOT_NUMBER`, and
Route B remains false.

## Route-A independent all-parameter round C194--C198

This round takes one large, complete theorem step per paper and changes the
dynamical owner in every slot: positional-addition carries, a nonlinear
parabolic PDE, a repulsive many-body Hamiltonian, an operator-splitting
algorithm, and a monotone compartmental ODE.  Finite certificates test exact
conventions; the full-family conclusions remain proof- or source-theorem
driven.

- [C194 Holte carries base semigroup](henon_holte_carries_base_semigroup_route_a/README.md) · [paper PDF](henon_holte_carries_base_semigroup_route_a/paper/main.pdf)
- [C195 periodic viscous Burgers Cole--Hopf flow](henon_periodic_viscous_burgers_cole_hopf_route_a/README.md) · [paper PDF](henon_periodic_viscous_burgers_cole_hopf_route_a/paper/main.pdf)
- [C196 rational Calogero--Moser Hermitian pencil](henon_calogero_moser_free_hermitian_pencil_route_a/README.md) · [paper PDF](henon_calogero_moser_free_hermitian_pencil_route_a/paper/main.pdf)
- [C197 all-relaxation Douglas--Rachford geometry](henon_douglas_rachford_principal_angle_route_a/README.md) · [paper PDF](henon_douglas_rachford_principal_angle_route_a/paper/main.pdf)
- [C198 closed SIR final-size phase portrait](henon_sir_final_size_phase_portrait_route_a/README.md) · [paper PDF](henon_sir_final_size_phase_portrait_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C194_C198.md),
[batch plan](BATCH_PLAN_C194_C198.md), and
[batch review](BATCH_REVIEW_C194_C198.md) for the collision pivots,
all-parameter proof ledger, exact Route-A tuples, adversarial repairs and
content-addressed release hashes.  The uniform audit contains 29,591
independent-checker assertions, 16,256 SymPy checks, 345 hostile rejections,
135 payloads and 11 final PDF pages.  C194 alone reaches
`A0_WEAK_ARITHMETIC_RELATION`, while C196 alone reaches
`A4_NATURAL_QUANTIZATION`; the coordinates are not combined and all five
remain `ROUTE_A_REJECTED`.  Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`, and Route
B remains false.

## Route-A independent cross-subtype round C199--C203

This round again takes one complete theorem-scale step per paper and changes
the dynamical owner in every slot: a nonholonomic rigid body, a degenerate
diffusion, an inertial optimization recurrence, a reaction--diffusion wave,
and a signed-network gradient semigroup.  Each package closes the full declared
parameter family and its singular or degenerate boundaries; finite exact
ledgers remain verification oracles rather than substitutes for the proofs.

- [C199 signed-offset Chaplygin-sleigh scattering](henon_chaplygin_sleigh_complete_scattering_route_a/README.md) · [paper PDF](henon_chaplygin_sleigh_complete_scattering_route_a/paper/main.pdf)
- [C200 Jacobi--Wright--Fisher spectral atlas](henon_jacobi_diffusion_spectral_atlas_route_a/README.md) · [paper PDF](henon_jacobi_diffusion_spectral_atlas_route_a/paper/main.pdf)
- [C201 all-real Polyak heavy-ball stability](henon_polyak_heavy_ball_stability_route_a/README.md) · [paper PDF](henon_polyak_heavy_ball_stability_route_a/paper/main.pdf)
- [C202 every-speed Fisher--KPP wave atlas](henon_fisher_kpp_traveling_wave_atlas_route_a/README.md) · [paper PDF](henon_fisher_kpp_traveling_wave_atlas_route_a/paper/main.pdf)
- [C203 signed-Laplacian consensus and pseudoforests](henon_signed_laplacian_balance_consensus_route_a/README.md) · [paper PDF](henon_signed_laplacian_balance_consensus_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C199_C203.md),
[batch plan](BATCH_PLAN_C199_C203.md), and
[batch review](BATCH_REVIEW_C199_C203.md) for collision screening, exact
theorem increments, internal repairs, content-addressed hashes and the uniform
52,379-checker / 3,429-SymPy / 163-mutation / 135-payload / 15-page audit.
Four packages retain candidate-local `A4_FORMAL_HINT`; C202 has `A4_FAIL`.
None supplies A0--A3, so all five remain `ROUTE_A_REJECTED`.  Coordinates stay
separate, scope is `NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B remains false.

## Route-A independent cross-subtype round C204--C208

This round again gives every paper one complete theorem-scale advance and
changes the dynamical owner in every slot: an all-finite-field linear map, a
non-sofic context-free shift, a linear shear PDE, a nonlinear self-similar
diffusion, and a continuous-time branching process.  Finite ledgers and
symbolic identities are regression oracles; all-family conclusions remain
proof- or source-theorem driven.

- [C204 finite linear rational-canonical dynamics](henon_finite_linear_rational_canonical_dynamics_route_a/README.md) · [paper PDF](henon_finite_linear_rational_canonical_dynamics_route_a/paper/main.pdf)
- [C205 Dyck-shift algebraic zeta](henon_dyck_shift_algebraic_zeta_route_a/README.md) · [paper PDF](henon_dyck_shift_algebraic_zeta_route_a/paper/main.pdf)
- [C206 Couette shear enhanced dissipation](henon_couette_shear_enhanced_dissipation_route_a/README.md) · [paper PDF](henon_couette_shear_enhanced_dissipation_route_a/paper/main.pdf)
- [C207 full-exponent Barenblatt similarity atlas](henon_barenblatt_full_exponent_similarity_route_a/README.md) · [paper PDF](henon_barenblatt_full_exponent_similarity_route_a/paper/main.pdf)
- [C208 linear birth--death branching process](henon_linear_birth_death_branching_route_a/README.md) · [paper PDF](henon_linear_birth_death_branching_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C204_C208.md),
[batch plan](BATCH_PLAN_C204_C208.md), and completed
[batch review](BATCH_REVIEW_C204_C208.md) for collision pivots, theorem
increments, proof/evidence boundaries and the release audit.  The round closes
15,623 checker exact cells/assertions, 4,060 SymPy checks, 112/112 hostile
rejections, 135 content-addressed payloads and 15 final-paper pages.  C204 and
C205 retain genuine source primitive ledgers, and C206 retains only a
candidate-local inviscid operator hint; none clears A0 or supplies a target
bridge.  Coordinates remain separate, scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B remains false.

## Route-A independent cross-subtype round C209--C213

This round changes the dynamical owner in every slot: a finite Catalan
permutation, a retarded delay semigroup, a positive Hamiltonian flow, a hybrid
impact system, and a persistent-velocity Markov process.  Each paper closes
one complete theorem-scale advance, including its singular and boundary
regimes; no theorem is split across the five packages.

- [C209 Kreweras-complement cycle atlas](henon_kreweras_noncrossing_cycle_atlas_route_a/README.md) · [paper PDF](henon_kreweras_noncrossing_cycle_atlas_route_a/paper/main.pdf)
- [C210 scalar retarded-delay Lambert stability](henon_scalar_retarded_delay_lambert_stability_route_a/README.md) · [paper PDF](henon_scalar_retarded_delay_lambert_stability_route_a/paper/main.pdf)
- [C211 Hamiltonian Lotka--Volterra period atlas](henon_lotka_volterra_hamiltonian_period_atlas_route_a/README.md) · [paper PDF](henon_lotka_volterra_hamiltonian_period_atlas_route_a/paper/main.pdf)
- [C212 affine-impact bouncing-ball atlas](henon_affine_impact_bouncing_ball_route_a/README.md) · [paper PDF](henon_affine_impact_bouncing_ball_route_a/paper/main.pdf)
- [C213 circular telegraph Fourier/hypocoercivity atlas](henon_circle_telegraph_fourier_hypocoercivity_route_a/README.md) · [paper PDF](henon_circle_telegraph_fourier_hypocoercivity_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C209_C213.md), [batch plan](BATCH_PLAN_C209_C213.md),
and [batch review](BATCH_REVIEW_C209_C213.md) for the frozen owners,
collision decisions, proof/evidence boundaries, and release audit.  The round
closes 30,406 checker assertions, 3,445 SymPy checks, 111 hostile mutations,
135 content-addressed payloads, and 13 final-paper pages.  All five remain
`ROUTE_A_REJECTED`; no target table, arithmetic local datum, Euler factor,
root number, automorphy object, target divisor, Hilbert--Pólya operator, or
Route-B input is used.  Coordinates remain separate, scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B remains false.

## Route-A independent cross-subtype round C214--C218

This round takes one theorem-scale step per paper and deliberately changes
the dynamical subtype in every slot: Brownian resetting renewal, partition-
valued coalescent genealogy, planar Kepler collision regularization,
constant-`f` rotating shallow-water Fourier flow, and Kelvin--Voigt spectral
damping.  Each package closes its own all-parameter theorem and boundary
cases, with independent evidence and a strict Route-A stopping decision.

- [C214 Brownian resetting renewal and first-passage atlas](henon_brownian_stochastic_resetting_first_passage_route_a/README.md) · [paper PDF](henon_brownian_stochastic_resetting_first_passage_route_a/paper/main.pdf)
- [C215 Kingman coalescent genealogy and branch-length atlas](henon_kingman_coalescent_genealogy_route_a/README.md) · [paper PDF](henon_kingman_coalescent_genealogy_route_a/paper/main.pdf)
- [C216 planar Kepler conics and Levi--Civita collision boundary](henon_planar_kepler_conic_collision_regularization_route_a/README.md) · [paper PDF](henon_planar_kepler_conic_collision_regularization_route_a/paper/main.pdf)
- [C217 rotating shallow-water Fourier projector atlas](henon_rotating_shallow_water_fourier_route_a/README.md) · [paper PDF](henon_rotating_shallow_water_fourier_route_a/paper/main.pdf)
- [C218 Kelvin--Voigt essential spectral accumulation and optimal damping](henon_kelvin_voigt_wave_spectral_route_a/README.md) · [paper PDF](henon_kelvin_voigt_wave_spectral_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C214_C218.md),
[batch plan](BATCH_PLAN_C214_C218.md), and
[batch review](BATCH_REVIEW_C214_C218.md) for the frozen owners, cross-review
repairs, exact theorem/evidence ledgers, and content-addressed release hashes.
The uniform audit closes 24,208 independent-checker assertions, 549 SymPy
checks, 101 hostile rejections, 135 payloads, and 13 final-paper pages.  The
final PDF SHA-256 values are, in order C214--C218:
`135989257553d59dadf4fbe2b31a2843c06a892a56b612fc1b9494289b8cde06`,
`a2ce47e6c601a153720c29b907e27d0aae56ffc6e383e04ce54f3853fa718a5c`,
`10b9769a1ef8be2a10ba6a1f9d8f55e271b8724124a93b7167ebbd64b571cf05`,
`de12b191d81c6d12fe1c58800cfcc9c95481d69d8d47dfea636d74036177c7d1`, and
`1d92dd1acfc9fd35d5f1622d32975dab9eac8a7de118624371b5d55eba623d97`.
All five tuples remain exactly as recorded in their evaluator YAML files,
`ROUTE_A_REJECTED`, and `route_b_invocation_allowed: false`; no target primes,
zeros, local arithmetic, Euler factors, root numbers, automorphy, target
divisor, Hilbert--Pólya operator, or Route-B input is claimed.

## Route-A independent cross-subtype round C219--C223

This round takes one complete theorem-scale step per paper while switching
the dynamical owner in every slot: a singular radial fluid ODE, a stochastic
boundary-driven exclusion chain, a dispersive Hamiltonian PDE, a nonsmooth
minimum-time control system, and a quantum-optical atom--field Hamiltonian.
Each package closes its own parameter/boundary theorem, executable evidence,
three substantive manuscript revisions, and content-addressed release
manifest.  The finite ledgers are regression controls; the all-family claims
are carried by the displayed proofs and source-local theorems.

- [C219 Rayleigh spherical-cavity collapse](henon_rayleigh_spherical_cavity_collapse_route_a/README.md) · [paper PDF](henon_rayleigh_spherical_cavity_collapse_route_a/paper/main.pdf)
- [C220 open TASEP matrix-Ansatz phase atlas](henon_open_tasep_matrix_ansatz_phase_route_a/README.md) · [paper PDF](henon_open_tasep_matrix_ansatz_phase_route_a/paper/main.pdf)
- [C221 focusing cubic NLS soliton Hessian](henon_cubic_nls_soliton_hessian_route_a/README.md) · [paper PDF](henon_cubic_nls_soliton_hessian_route_a/paper/main.pdf)
- [C222 bounded double-integrator bang--bang synthesis](henon_double_integrator_bang_bang_time_optimal_route_a/README.md) · [paper PDF](henon_double_integrator_bang_bang_time_optimal_route_a/paper/main.pdf)
- [C223 Jaynes--Cummings excitation blocks](henon_jaynes_cummings_excitation_block_route_a/README.md) · [paper PDF](henon_jaynes_cummings_excitation_block_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C219_C223.md), [batch plan](BATCH_PLAN_C219_C223.md),
and [batch review](BATCH_REVIEW_C219_C223.md) for collision decisions,
theorem increments, exact audit counts, release hashes and the complete PDF
reproducibility record.  The round closes 7,981 independent-checker
assertions, 847 SymPy checks, 110 hostile rejections, 135 payloads (140
physical files), and 14 final-paper pages.  The strict tuples are recorded in
the per-paper evaluator YAML files; all five remain `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false`.  The common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic or operator bridge is
claimed.

## Route-A independent cross-subtype round C224--C228

This round makes one large, complete theorem-scale advance in each paper and
changes the dynamical owner in every slot: a nonautonomous Landau--Zener
crossing, a finite-capacity birth--death queue, a one-phase Stefan free
boundary, a dissipative Lorenz flow, and a gelating coagulation equation.
Finite receipts are independent regression oracles; the all-parameter claims
are carried by the displayed source-local theorems.  The five papers are not
installments of one theorem.

- [C224 Landau--Zener--Weber scattering](henon_landau_zener_weber_scattering_route_a/README.md) · [paper PDF](henon_landau_zener_weber_scattering_route_a/paper/main.pdf)
- [C225 finite M/M/1/K spectral--mixing atlas](henon_mm1k_queue_spectral_mixing_route_a/README.md) · [paper PDF](henon_mm1k_queue_spectral_mixing_route_a/paper/main.pdf)
- [C226 one-phase Stefan--Neumann similarity](henon_one_phase_stefan_neumann_similarity_route_a/README.md) · [paper PDF](henon_one_phase_stefan_neumann_similarity_route_a/paper/main.pdf)
- [C227 Lorenz-63 dissipativity and stability atlas](henon_lorenz63_dissipative_stability_atlas_route_a/README.md) · [paper PDF](henon_lorenz63_dissipative_stability_atlas_route_a/paper/main.pdf)
- [C228 product-kernel coagulation and postgel closure](henon_smoluchowski_product_kernel_gelation_route_a/README.md) · [paper PDF](henon_smoluchowski_product_kernel_gelation_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C224_C228.md), [batch plan](BATCH_PLAN_C224_C228.md),
and [batch review](BATCH_REVIEW_C224_C228.md) for the frozen collision
decisions, theorem increments, source/evidence boundaries, release hashes,
and uniform audit.  All five strict tuples remain `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false`; scope is
`NO_BAD_EULER_OR_ROOT_NUMBER` and no target arithmetic or operator bridge is
claimed.

## Route-A independent cross-subtype round C229--C233

This round takes one large, complete theorem step per paper and deliberately
changes the dynamical owner in every slot: a degenerate square-root diffusion,
an open integrable lattice, a gradient reaction--diffusion front, a quartic
Hamiltonian oscillator, and a countable-state immigration--death semigroup.
Each package closes its declared parameter and boundary faces, carries an
independent executable certificate, and includes a finished manuscript.  The
five papers are independent owners, not installments of one theorem.

- [C229 CIR square-root diffusion and Laguerre spectrum](henon_cir_square_root_diffusion_affine_spectral_route_a/README.md) · [paper PDF](henon_cir_square_root_diffusion_affine_spectral_route_a/paper/main.pdf)
- [C230 open Toda Lax/scattering flow](henon_open_toda_lax_scattering_route_a/README.md) · [paper PDF](henon_open_toda_lax_scattering_route_a/paper/main.pdf)
- [C231 Allen--Cahn tanh front and Pöschl--Teller edge](henon_allen_cahn_front_pochhammer_spectrum_route_a/README.md) · [paper PDF](henon_allen_cahn_front_pochhammer_spectrum_route_a/paper/main.pdf)
- [C232 Duffing energy topology and homoclinic separatrix](henon_duffing_hamiltonian_separatrix_route_a/README.md) · [paper PDF](henon_duffing_hamiltonian_separatrix_route_a/paper/main.pdf)
- [C233 M/M/infinity Poisson--Charlier semigroup](henon_mm_infinity_poisson_spectral_route_a/README.md) · [paper PDF](henon_mm_infinity_poisson_spectral_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C229_C233.md), [batch plan](BATCH_PLAN_C229_C233.md),
and [batch review](BATCH_REVIEW_C229_C233.md) for collision pivots, theorem
increments, source/evidence boundaries, release hashes and the uniform audit.
The round closes 9,192 independent-checker assertions, 91 symbolic/algebra
checks, 104 hostile rejections, 135 content-addressed payloads (140 physical
files), and 15 final-paper pages.  All five strict tuples are recorded in the
per-paper evaluator YAML files and remain `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false`.  The common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic or operator bridge is
claimed.

## Route-A independent cross-subtype round C234--C238

This round takes one large, complete theorem step per paper and changes the
dynamical owner in every slot: a dissipative spin flow on the sphere, a cyclic
population replicator, an integrable hyperbolic field equation, a hypoelliptic
phase-space diffusion, and a nonsmooth dry-friction inclusion.  Each package
closes its declared parameter/boundary atlas, executable evidence, three
substantive manuscript revisions, and content-addressed release manifest.  The
five papers are independent owners, not installments of one theorem.

- [C234 constant-field Landau--Lifshitz--Gilbert sphere flow](henon_landau_lifshitz_gilbert_constant_field_route_a/README.md) · [paper PDF](henon_landau_lifshitz_gilbert_constant_field_route_a/paper/main.pdf)
- [C235 rock--paper--scissors uniform-mutation replicator](henon_rock_paper_scissors_uniform_mutation_route_a/README.md) · [paper PDF](henon_rock_paper_scissors_uniform_mutation_route_a/paper/main.pdf)
- [C236 sine--Gordon kink and breather coherent families](henon_sine_gordon_kink_breather_route_a/README.md) · [paper PDF](henon_sine_gordon_kink_breather_route_a/paper/main.pdf)
- [C237 harmonic Kramers--Langevin Mehler flow](henon_kramers_harmonic_langevin_mehler_route_a/README.md) · [paper PDF](henon_kramers_harmonic_langevin_mehler_route_a/paper/main.pdf)
- [C238 Coulomb dry-friction Filippov oscillator](henon_coulomb_dry_friction_filippov_route_a/README.md) · [paper PDF](henon_coulomb_dry_friction_filippov_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C234_C238.md), [batch plan](BATCH_PLAN_C234_C238.md),
and [batch review](BATCH_REVIEW_C234_C238.md) for collision screening,
theorem increments, exact audit counts, release hashes and the complete PDF
reproducibility record.  The round closes 2,092 independent-checker
assertions, 92 symbolic/algebra checks, 163 hostile rejections, 135
content-addressed payloads (140 physical files), and 11 final-paper pages
with 111 embedded subset-font entries.  All five strict tuples are recorded
in their evaluator YAML files and remain `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false`.  The common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic or operator bridge is
claimed.

## Route-A independent cross-subtype round C239--C243

This round makes one large, complete theorem step in each paper while changing
the dynamical owner in every slot: a multiway permutation, a discontinuous
contracted rotation, a countable-branch interval map, an integrable Reeb flow,
and a nonlinear Bose--Josephson dimer.  The five manuscripts are independent
source-local results, not five installments of one theorem.  The initial
pair-of-pants/Schottky idea for C243 was screened out because a substantive
Schottky ledger already exists; the released dimer is the documented pivot.

- [C239 multiway perfect-shuffle cycle atlas](henon_multiway_perfect_shuffle_cycle_atlas/README.md) · [paper PDF](henon_multiway_perfect_shuffle_cycle_atlas/paper/main.pdf)
- [C240 contracted-rotation mode-locking atlas](henon_contracted_rotation_mode_locking_atlas/README.md) · [paper PDF](henon_contracted_rotation_mode_locking_atlas/paper/main.pdf)
- [C241 classical Lüroth countable-branch periodic atlas](henon_luroth_countable_branch_periodic_atlas/README.md) · [paper PDF](henon_luroth_countable_branch_periodic_atlas/paper/main.pdf)
- [C242 irrational ellipsoid Reeb orbit atlas](henon_irrational_ellipsoid_reeb_orbit_atlas/README.md) · [paper PDF](henon_irrational_ellipsoid_reeb_orbit_atlas/paper/main.pdf)
- [C243 Bose--Josephson dimer phase portrait](henon_bose_josephson_dimer_phase_portrait/README.md) · [paper PDF](henon_bose_josephson_dimer_phase_portrait/paper/main.pdf)

See the [idea report](IDEA_REPORT_C239_C243.md), [batch plan](BATCH_PLAN_C239_C243.md),
and [batch review](BATCH_REVIEW_C239_C243.md) for collision screening,
theorem increments, evidence boundaries, release hashes and the complete
reproducibility audit.  The round closes 30,925 independent-checker
assertions, 1,826 symbolic identities plus three independent elliptic
quadratures, 190 hostile rejections, 135 content-addressed payloads (140
physical files), and 11 final-paper pages with 113 embedded/subset font
entries.  The strict tuples are, in order C239--C243,
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, and
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.  All five are
`ROUTE_A_REJECTED`, `route_b_invocation_allowed: false`, and use the common
scope `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, divisor/counting
law, Euler factor, root number, automorphy object, Hilbert--Pólya operator,
or Route-B input is claimed.

## Route-A independent cross-subtype round C369--C373

This round takes five independent theorem-scale steps across a quartic
arithmetic root scheme, a quasiregular contact flow, a rational-flux magnetic
Bloch family, an inviscid free-boundary vortex patch, and a curved
classical--quantum oscillator.  The papers have different state spaces,
clocks, proof engines, and boundary phenomena; they are not one article split
into installments.

- [C369 quartic S4 Frobenius root atlas](henon_s4_frobenius_root_scheme_route_a/README.md) · [paper PDF](henon_s4_frobenius_root_scheme_route_a/paper/main.pdf)
- [C370 pairwise-coprime Brieskorn Reeb atlas](henon_brieskorn_quasiregular_reeb_route_a/README.md) · [paper PDF](henon_brieskorn_quasiregular_reeb_route_a/paper/main.pdf)
- [C371 rational-flux anisotropic Harper--Chambers atlas](henon_harper_chambers_bloch_route_a/README.md) · [paper PDF](henon_harper_chambers_bloch_route_a/paper/main.pdf)
- [C372 Kirchhoff--Love elliptic-vortex threshold ladder](henon_kirchhoff_ellipse_love_stability_route_a/README.md) · [paper PDF](henon_kirchhoff_ellipse_love_stability_route_a/paper/main.pdf)
- [C373 hemispherical Higgs oscillator and exact revivals](henon_hemispherical_higgs_oscillator_route_a/README.md) · [paper PDF](henon_hemispherical_higgs_oscillator_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C369_C373.md),
[batch plan](BATCH_PLAN_C369_C373.md), and
[batch review](BATCH_REVIEW_C369_C373.md) for collision screening, theorem
contracts, author-swapped proof/source repairs, exact hashes, and release
accounting.  C369 explicitly inherits C12A's universal finite-fibre
Frobenius zeta/determinant mechanism and owns only the quartic-specific
`S_4` atlas.  C371's all-even-denominator step is now tied to the exact
Lamoureux--Mingo normalization; C372's zero-vorticity and co-rotating-frame
conventions are closed; C373's PDF source has a hostile gate against
unescaped TeX spacing commands.

The round closes 16,659 symbolic identities, 358 hostile rejections,
15,217,220 canonical evidence bytes, 175 content-addressed payloads (180
physical files), and 18 final-paper pages with 93 embedded/subset font rows.
The strict tuples, in order C369--C373, are
`(A0_STRUCTURAL_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, and
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.  C369 is
`ROUTE_A_ARITHMETIC_CANDIDATE`, C370 is `ROUTE_A_EXPLORATORY`, and
C371--C373 are `ROUTE_A_REJECTED`.  Route B is false and the common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic local datum, target
Euler factor, target bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target-zero match,
Hilbert--Polya operator, or Route-B input is asserted.

## Route-A independent cross-subtype round C364--C368

This round takes five independent theorem-scale steps across a fixed-
discriminant arithmetic reduction permutation, a compact collective
Hamiltonian system, an engineered quantum spin chain, a reflected stochastic
fluid, and a conformal free-boundary flow.  The five papers have different
phase spaces, clocks, proof engines, and boundary phenomena; they are not one
article divided into installments.

- [C364 fixed-discriminant Gauss reduction cycles](henon_gauss_indefinite_reduction_cycles_route_a/README.md) · [paper PDF](henon_gauss_indefinite_reduction_cycles_route_a/paper/main.pdf)
- [C365 U(3) Gelfand--Tsetlin dynamics and quantization](henon_gelfand_tsetlin_u3_integrable_quantization_route_a/README.md) · [paper PDF](henon_gelfand_tsetlin_u3_integrable_quantization_route_a/paper/main.pdf)
- [C366 Krawtchouk XX mirror inversion](henon_krawtchouk_xx_mirror_inversion_route_a/README.md) · [paper PDF](henon_krawtchouk_xx_mirror_inversion_route_a/paper/main.pdf)
- [C367 two-state reflected Markov-fluid atlas](henon_two_state_reflected_markov_fluid_route_a/README.md) · [paper PDF](henon_two_state_reflected_markov_fluid_route_a/paper/main.pdf)
- [C368 quadratic Polubarinova--Galin first-cusp atlas](henon_quadratic_polubarinova_galin_route_a/README.md) · [paper PDF](henon_quadratic_polubarinova_galin_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C364_C368.md),
[batch plan](BATCH_PLAN_C364_C368.md), and
[batch review](BATCH_REVIEW_C364_C368.md) for collision screening, theorem
contracts, author-swapped repairs, exact hashes, and release accounting.  The
round closes 1,000,804 independent-checker assertions, 7,532 symbolic
identities, 440 hostile rejections, 17,874,609 canonical evidence bytes, 135
content-addressed payloads (140 physical files), and 11 final-paper pages with
80 embedded/subset font entries.  The strict tuples, in order C364--C368, are
`(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.  C364 and C365 are
`ROUTE_A_EXPLORATORY`; C366--C368 are `ROUTE_A_REJECTED`.  Route B is false
and the common scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic
local datum, Euler factor, root number, automorphy object, target
divisor/counting law or functional equation, target-zero match,
Hilbert--Polya operator, or Route-B input is asserted.

## Route-A independent cross-subtype round C359--C363

This round takes five independent theorem-scale steps and changes dynamical
owner in every paper: a fourth-order higher-derivative oscillator, a
homogeneous Ricci flow, a finite nonequilibrium jump process, a many-particle
alignment flow, and a nonlocal chemotaxis PDE.  The papers share a release
protocol, not one theorem split into installments.

- [C359 Pais--Uhlenbeck Ostrogradsky resonance and quantum atlas](henon_pais_uhlenbeck_ostrogradsky_resonance_route_a/README.md) · [paper PDF](henon_pais_uhlenbeck_ostrogradsky_resonance_route_a/paper/main.pdf)
- [C360 Berger SU(2) Ricci-flow extinction atlas](henon_berger_su2_ricci_flow_extinction_route_a/README.md) · [paper PDF](henon_berger_su2_ricci_flow_extinction_route_a/paper/main.pdf)
- [C361 finite Markov entropy-production and fluctuation symmetry](henon_finite_markov_entropy_fluctuation_route_a/README.md) · [paper PDF](henon_finite_markov_entropy_fluctuation_route_a/paper/main.pdf)
- [C362 Cucker--Smale sharp flocking threshold](henon_cucker_smale_flocking_threshold_route_a/README.md) · [paper PDF](henon_cucker_smale_flocking_threshold_route_a/paper/main.pdf)
- [C363 planar Keller--Segel critical-mass virial atlas](henon_keller_segel_critical_mass_virial_route_a/README.md) · [paper PDF](henon_keller_segel_critical_mass_virial_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C359_C363.md),
[batch plan](BATCH_PLAN_C359_C363.md), and
[batch review](BATCH_REVIEW_C359_C363.md) for collision screening, theorem
contracts, source audits, author-swapped proof repairs, exact release hashes,
and aggregate accounting.  The strict tuples, in order C359--C363, are
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.
All five are `ROUTE_A_REJECTED`; Route B is false and the common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, root number, automorphy object, target divisor/counting law or
functional equation, target-zero match, Hilbert--Pólya operator, or Route-B
input is asserted.

## Route-A independent cross-subtype round C354--C358

This round takes five independent theorem-scale steps across a symmetric
heavy-top Hamiltonian, an infinite nonamenable group walk, a topological Bloch
pump, a nonsmooth isochronous oscillator and a cyclic population flow.  Each
paper closes its own global, spectral, topological or boundary atlas; these are
five complete owners rather than installments of one theorem.

- [C354 Lagrange heavy-top elliptic reconstruction and closure](henon_lagrange_heavy_top_elliptic_closure_route_a/README.md) · [paper PDF](henon_lagrange_heavy_top_elliptic_closure_route_a/paper/main.pdf)
- [C355 free-group Kesten spectrum, returns and escape](henon_free_group_kesten_random_walk_route_a/README.md) · [paper PDF](henon_free_group_kesten_random_walk_route_a/paper/main.pdf)
- [C356 QWZ--Thouless Chern-pump phase atlas](henon_qwz_thouless_chern_pump_route_a/README.md) · [paper PDF](henon_qwz_thouless_chern_pump_route_a/paper/main.pdf)
- [C357 bilinear two-stiffness isochronous oscillator](henon_bilinear_two_stiffness_isochronous_oscillator_route_a/README.md) · [paper PDF](henon_bilinear_two_stiffness_isochronous_oscillator_route_a/paper/main.pdf)
- [C358 May--Leonard cyclic-competition trichotomy](henon_may_leonard_cyclic_competition_route_a/README.md) · [paper PDF](henon_may_leonard_cyclic_competition_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C354_C358.md),
[batch plan](BATCH_PLAN_C354_C358.md), and
[batch review](BATCH_REVIEW_C354_C358.md) for collision screening, frozen
theorem contracts, author-swapped repairs, exact release receipts and aggregate
accounting.  The strict
tuples, in order C354--C358, are
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, and
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.
All five are `ROUTE_A_REJECTED`; Route B is false and common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, root number, automorphy object, target divisor/counting law or
functional equation, target-zero match, Hilbert--Polya operator, or Route-B
input is asserted.

## Route-A independent cross-subtype round C349--C353

This round takes five separate theorem-scale steps across an integrable
constrained Hamiltonian, a reaction--diffusion instability, an open queueing
network, a supersymmetric whole-line Dirac problem and an exchangeable random
partition growth law.  These are five complete papers, not five installments
of one result.

- [C349 Neumann--Uhlenbeck integrable sphere](henon_neumann_uhlenbeck_integrable_sphere_route_a/README.md) · [paper PDF](henon_neumann_uhlenbeck_integrable_sphere_route_a/paper/main.pdf)
- [C350 Schnakenberg finite-domain Turing modes](henon_schnakenberg_neumann_turing_modes_route_a/README.md) · [paper PDF](henon_schnakenberg_neumann_turing_modes_route_a/paper/main.pdf)
- [C351 open Jackson network and quasi-reversibility](henon_open_jackson_network_quasireversibility_route_a/README.md) · [paper PDF](henon_open_jackson_network_quasireversibility_route_a/paper/main.pdf)
- [C352 integer-kink Jackiw--Rebbi Dirac spectrum](henon_jackiw_rebbi_kink_dirac_spectrum_route_a/README.md) · [paper PDF](henon_jackiw_rebbi_kink_dirac_spectrum_route_a/paper/main.pdf)
- [C353 Ewens--Chinese-restaurant partition growth](henon_ewens_chinese_restaurant_partition_growth_route_a/README.md) · [paper PDF](henon_ewens_chinese_restaurant_partition_growth_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C349_C353.md),
[batch plan](BATCH_PLAN_C349_C353.md), and
[batch review](BATCH_REVIEW_C349_C353.md) for collision screening, theorem
contracts, author-swapped proof repairs, exact release receipts and aggregate
accounting.  The strict tuples, in order C349--C353, are
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.
All five are `ROUTE_A_REJECTED`; Route B is false and common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, root number, automorphy object, target divisor/counting law or
functional equation, target-zero match, Hilbert--Polya operator, or Route-B
input is asserted.

## Route-A independent cross-subtype round C344--C348

This round takes five independent theorem-scale steps: a complex Hamiltonian
wave triad, a side-coupled lattice impurity, a nonsmooth oblique reflection
map, a noisy nonlinear mean-field PDE, and a random walk in infinite iid
spatial disorder.  These are five complete papers, not five installments of
one result.

- [C344 Hamiltonian resonant-triad elliptic dynamics](henon_hamiltonian_resonant_triad_elliptic_route_a/README.md) · [paper PDF](henon_hamiltonian_resonant_triad_elliptic_route_a/paper/main.pdf)
- [C345 Fano--Anderson side-impurity spectrum and scattering](henon_fano_anderson_side_impurity_spectral_scattering_route_a/README.md) · [paper PDF](henon_fano_anderson_side_impurity_spectral_scattering_route_a/paper/main.pdf)
- [C346 oblique Skorokhod-map M-matrix threshold](henon_oblique_skorokhod_map_mmatrix_threshold_route_a/README.md) · [paper PDF](henon_oblique_skorokhod_map_mmatrix_threshold_route_a/paper/main.pdf)
- [C347 noisy mean-field Kuramoto phase transition](henon_noisy_mean_field_kuramoto_phase_transition_route_a/README.md) · [paper PDF](henon_noisy_mean_field_kuramoto_phase_transition_route_a/paper/main.pdf)
- [C348 one-dimensional iid RWRE Solomon phase atlas](henon_one_dimensional_iid_rwre_solomon_phase_route_a/README.md) · [paper PDF](henon_one_dimensional_iid_rwre_solomon_phase_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C344_C348.md),
[batch plan](BATCH_PLAN_C344_C348.md), and
[batch review](BATCH_REVIEW_C344_C348.md) for collision screening, theorem
contracts, source ownership, author-swapped proof checks, exact release
receipts and aggregate accounting.  The five strict tuples, in order
C344--C348, are
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.
All five are `ROUTE_A_REJECTED`.  Route B is false for all five and the common
scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum,
Euler factor, root number, automorphy object, target divisor/counting law or
functional equation, target zero match, Hilbert--Polya operator, or Route-B
input is asserted.

## Route-A independent cross-subtype round C339--C343

This round takes five separate theorem-scale steps across unrelated dynamics:
a nonreversible Finsler geodesic flow, a periodic finite-gap Hamiltonian, a
finite lamplighter Markov chain, a directed reinforced walk in random
environment, and an Erlang-distributed memory flow.  These are five complete
papers, not five installments of one result.

- [C339 Katok--Zermelo two-geodesic Randers sphere](henon_katok_zermelo_randers_two_geodesic_route_a/README.md) · [paper PDF](henon_katok_zermelo_randers_two_geodesic_route_a/paper/main.pdf)
- [C340 complete one-gap Lame spectrum](henon_lame_one_gap_floquet_spectrum_route_a/README.md) · [paper PDF](henon_lame_one_gap_floquet_spectrum_route_a/paper/main.pdf)
- [C341 finite-cycle lamplighter full spectrum](henon_lamplighter_cycle_full_spectrum_route_a/README.md) · [paper PDF](henon_lamplighter_cycle_full_spectrum_route_a/paper/main.pdf)
- [C342 directed reinforcement and Dirichlet environment](henon_directed_edge_reinforced_dirichlet_environment_route_a/README.md) · [paper PDF](henon_directed_edge_reinforced_dirichlet_environment_route_a/paper/main.pdf)
- [C343 Erlang-2 distributed-delay stability atlas](henon_erlang2_distributed_delay_hopf_route_a/README.md) · [paper PDF](henon_erlang2_distributed_delay_hopf_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C339_C343.md),
[batch plan](BATCH_PLAN_C339_C343.md), and
[batch review](BATCH_REVIEW_C339_C343.md) for collision screening, theorem
contracts, source ownership, author-swapped proof checks, exact release
receipts and aggregate accounting.  The five strict tuples, in order
C339--C343, are
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.
All five are `ROUTE_A_REJECTED`.  Route B is false for all five and the common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, root number, automorphy object, target divisor/counting law or
functional equation, target zero match, Hilbert--Polya operator, or Route-B
input is asserted.

## Route-A independent cross-subtype round C334--C338

This round advances five unrelated mechanisms at theorem scale: an
integrable molecular Hamiltonian and its natural quantization, a jump-driven
affine Markov process, a finite-genome mutation--selection flow, an
integer-resonant quantum Floquet system, and an abelian random-stack dynamics.
These are five complete papers, not five installments of one theorem.

- [C334 Morse classical action and bound spectrum](henon_morse_action_bound_spectrum_route_a/README.md) · [paper PDF](henon_morse_action_bound_spectrum_route_a/paper/main.pdf)
- [C335 exponential shot-noise OU semigroup](henon_exponential_shot_noise_ou_route_a/README.md) · [paper PDF](henon_exponential_shot_noise_ou_route_a/paper/main.pdf)
- [C336 Crow--Kimura single-peak quasispecies](henon_crow_kimura_single_peak_quasispecies_route_a/README.md) · [paper PDF](henon_crow_kimura_single_peak_quasispecies_route_a/paper/main.pdf)
- [C337 integer-resonant quantum kicked rotor](henon_quantum_kicked_rotor_integer_resonance_route_a/README.md) · [paper PDF](henon_quantum_kicked_rotor_integer_resonance_route_a/paper/main.pdf)
- [C338 Wilson cycle-popping weighted UST](henon_wilson_cycle_popping_weighted_ust_route_a/README.md) · [paper PDF](henon_wilson_cycle_popping_weighted_ust_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C334_C338.md),
[batch plan](BATCH_PLAN_C334_C338.md), and
[batch review](BATCH_REVIEW_C334_C338.md) for collision screening, theorem
contracts, source ownership, author-swapped proof checks and exact release
receipts.  Across the five packages the final audit closes **275,948**
independent-checker assertions, **14,353** symbolic identities, **466/466**
hostile rejections, **2,596,399** evidence bytes, 135 manifest payloads (140
physical files), and **15** final-paper pages with **76** embedded/subset font
records.  Four evidence schemas expose **137,385** audited scalar leaves;
C336 instead records its complete row/cell ledger.  The five strict tuples,
in order C334--C338, are
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
All five are `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false` and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target zero match,
Hilbert--Polya operator, or Route-B input is asserted.

## Route-A independent cross-subtype round C329--C333

This round makes five separate theorem-scale advances while deliberately
changing the dynamical mechanism in every paper: a finite-field
nonbacktracking edge flow, a Diophantine three-branch map, a charged magnetic
flow with bundle quantization, a rate-independent sweeping process, and a
random continuous-state consensus product.  These are five complete papers,
not five installments of one result.

- [C329 Paley--Ihara nonbacktracking dynamics](henon_paley_graph_ihara_nonbacktracking_route_a/README.md) · [paper PDF](henon_paley_graph_ihara_nonbacktracking_route_a/paper/main.pdf)
- [C330 Romik Pythagorean periodic zeta](henon_romik_pythagorean_periodic_zeta_route_a/README.md) · [paper PDF](henon_romik_pythagorean_periodic_zeta_route_a/paper/main.pdf)
- [C331 Dirac-monopole magnetic flow and spectrum](henon_dirac_monopole_magnetic_flow_spectrum_route_a/README.md) · [paper PDF](henon_dirac_monopole_magnetic_flow_spectrum_route_a/paper/main.pdf)
- [C332 periodic scalar Moreau play](henon_moreau_scalar_play_periodic_sweeping_route_a/README.md) · [paper PDF](henon_moreau_scalar_play_periodic_sweeping_route_a/paper/main.pdf)
- [C333 complete-graph randomized-gossip covariance](henon_complete_graph_randomized_gossip_covariance_route_a/README.md) · [paper PDF](henon_complete_graph_randomized_gossip_covariance_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C329_C333.md),
[batch plan](BATCH_PLAN_C329_C333.md), and
[batch review](BATCH_REVIEW_C329_C333.md) for collision screening, theorem
contracts, source ownership, author-swapped proof repairs and exact release
receipts.  Across the five packages the final audit closes **310,049**
independent-checker assertions, **11,284** symbolic identities, **431/431**
hostile rejections, **205,051** audited scalar leaves, **6,302,716** evidence
bytes, 135 manifest payloads (140 physical files), and **15** final-paper pages
with **82** embedded/subset font records.  The five strict tuples, in order
C329--C333, are
`(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.  C329 and C330 are
`ROUTE_A_EXPLORATORY`; C331--C333 are `ROUTE_A_REJECTED`.  All five have
`route_b_invocation_allowed: false` under literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target zero match,
Hilbert--Polya operator, or Route-B input is asserted.

## Route-A independent cross-subtype round C324--C328

This round advances five unrelated dynamical mechanisms at theorem scale: a
nonlinear wave-breaking PDE, a randomized local-resampling algorithm, an
attractive conservative particle chain, a periodic singular quantum
Hamiltonian, and a confined active-matter PDMP.  These are five complete
papers, not five installments of one theorem.

- [C324 periodic Hunter--Saxton wave breaking](henon_hunter_saxton_periodic_wave_breaking_route_a/README.md) · [paper PDF](henon_hunter_saxton_periodic_wave_breaking_route_a/paper/main.pdf)
- [C325 Moser--Tardos witness-tree termination](henon_moser_tardos_resampling_witness_tree_route_a/README.md) · [paper PDF](henon_moser_tardos_resampling_witness_tree_route_a/paper/main.pdf)
- [C326 two-site inclusion Hahn spectrum](henon_two_site_inclusion_hahn_spectrum_route_a/README.md) · [paper PDF](henon_two_site_inclusion_hahn_spectrum_route_a/paper/main.pdf)
- [C327 Kronig--Penney band/gap atlas](henon_kronig_penney_band_gap_atlas_route_a/README.md) · [paper PDF](henon_kronig_penney_band_gap_atlas_route_a/paper/main.pdf)
- [C328 harmonic run-and-tumble beta spectrum](henon_harmonic_run_tumble_beta_spectrum_route_a/README.md) · [paper PDF](henon_harmonic_run_tumble_beta_spectrum_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C324_C328.md),
[batch plan](BATCH_PLAN_C324_C328.md), and
[batch review](BATCH_REVIEW_C324_C328.md) for collision screening, theorem
contracts, source ownership, adversarial proof repairs and exact release
receipts.  Across the five packages the final audit closes **15,366**
independent-checker assertions, **2,377** symbolic identities, **292/292**
hostile rejections, **788,600** evidence bytes, 135 manifest payloads (140
physical files), and **13** final-paper pages with **107** embedded/subset font
records.  The five strict tuples, in order C324--C328, are
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.
All five remain `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false` and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target zero match,
Hilbert--Polya operator, or Route-B input is claimed.

## Route-A independent cross-subtype round C319--C323

This round makes five independent theorem-scale advances while changing the
state space, clock, and proof mechanism in every paper: an extrinsic
geometric flow, a modular integrable polynomial flow, a growing random tree,
a continuous-state kinetic collision process, and a finite oracle
Hamiltonian.  These are five complete papers, not five installments of one
theorem.

- [C319 spherical Clifford-product mean-curvature flow](henon_clifford_product_mean_curvature_flow_route_a/README.md) · [paper PDF](henon_clifford_product_mean_curvature_flow_route_a/paper/main.pdf)
- [C320 Darboux--Halphen modular dynamics](henon_darboux_halphen_modular_dynamics_route_a/README.md) · [paper PDF](henon_darboux_halphen_modular_dynamics_route_a/paper/main.pdf)
- [C321 preferential-attachment degree martingales](henon_preferential_attachment_degree_martingale_route_a/README.md) · [paper PDF](henon_preferential_attachment_degree_martingale_route_a/paper/main.pdf)
- [C322 Kac master-equation spectral gap](henon_kac_master_equation_spectral_gap_route_a/README.md) · [paper PDF](henon_kac_master_equation_spectral_gap_route_a/paper/main.pdf)
- [C323 complete-graph quantum-search detuning](henon_complete_graph_quantum_search_detuning_route_a/README.md) · [paper PDF](henon_complete_graph_quantum_search_detuning_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C319_C323.md),
[batch plan](BATCH_PLAN_C319_C323.md), and
[batch review](BATCH_REVIEW_C319_C323.md) for collision screening, theorem
contracts, historical ownership, exact release receipts, the repaired
whole-spectrum projection argument in C322, and deterministic PDFs.  Across
the five packages the final audit closes **114,735** independent-checker
assertions, **19,543** exact symbolic identities, **228/228** hostile
rejections, **5,112,737** evidence bytes, 135 manifest payloads (140 physical
files), and **15** final-paper pages with **102** embedded/subset font
records.  The five strict tuples, in order C319--C323, are
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, and
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.
All five remain `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false` and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target zero match,
Hilbert--Polya operator, or Route-B input is claimed.

## Route-A independent cross-subtype round C314--C318

This round makes five independent theorem-scale advances while changing the
state space, clock, and proof mechanism in every paper: an ancient geometric
PDE, a velocity-coupled integrable root flow, a complete-memory stochastic
process, a nonlinear matrix inverse algorithm, and a Hermitian chiral
quantum lattice.  These are five complete papers, not five installments of
one theorem.

- [C314 Angenent-oval curve-shortening atlas](henon_angenent_oval_curve_shortening_route_a/README.md) · [paper PDF](henon_angenent_oval_curve_shortening_route_a/paper/main.pdf)
- [C315 positive-root-pencil goldfish scattering](henon_goldfish_positive_root_pencil_scattering_route_a/README.md) · [paper PDF](henon_goldfish_positive_root_pencil_scattering_route_a/paper/main.pdf)
- [C316 elephant-walk phase transition](henon_elephant_random_walk_phase_transition_route_a/README.md) · [paper PDF](henon_elephant_random_walk_phase_transition_route_a/paper/main.pdf)
- [C317 Newton--Schulz full basin and pseudoinverse](henon_newton_schulz_full_basin_pseudoinverse_route_a/README.md) · [paper PDF](henon_newton_schulz_full_basin_pseudoinverse_route_a/paper/main.pdf)
- [C318 finite SSH bulk--edge and quench atlas](henon_ssh_finite_bulk_edge_route_a/README.md) · [paper PDF](henon_ssh_finite_bulk_edge_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C314_C318.md),
[batch plan](BATCH_PLAN_C314_C318.md), and
[batch review](BATCH_REVIEW_C314_C318.md) for collision screening, theorem
contracts, historical ownership, exact release receipts, and deterministic
PDFs.  Across the five packages the final audit closes **34,432**
independent-checker assertions, **9,785** exact symbolic identities/groups,
**221/221** hostile rejections, **1,623,797** evidence bytes, 135 manifest
payloads (140 physical files), and **14** final-paper pages with **100**
embedded/subset font records.  The five strict tuples, in order C314--C318,
are
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.
All five remain `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false` and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target zero match,
Hilbert--Polya operator, or Route-B input is claimed.

## Route-A independent cross-subtype round C309--C313

This round makes five independent theorem-scale advances while changing the
state space, clock, and proof mechanism in every paper: a nonlinear symmetric
matrix ODE, a nonholonomic time-optimal car, a chemical reaction oscillator,
a discontinuous confidence-network map, and a maximally periodic geodesic
Hamiltonian flow with its native elliptic operator.  These are five complete
papers, not five installments of one theorem.

- [C309 symmetric matrix Riccati Mobius flow](henon_symmetric_matrix_riccati_mobius_flow_route_a/README.md) · [paper PDF](henon_symmetric_matrix_riccati_mobius_flow_route_a/paper/main.pdf)
- [C310 Dubins bounded-curvature global synthesis](henon_dubins_bounded_curvature_optimal_synthesis_route_a/README.md) · [paper PDF](henon_dubins_bounded_curvature_optimal_synthesis_route_a/paper/main.pdf)
- [C311 Brusselator exact Hopf normal form](henon_brusselator_hopf_normal_form_route_a/README.md) · [paper PDF](henon_brusselator_hopf_normal_form_route_a/paper/main.pdf)
- [C312 one-dimensional Hegselmann--Krause finite termination](henon_hegselmann_krause_finite_termination_route_a/README.md) · [paper PDF](henon_hegselmann_krause_finite_termination_route_a/paper/main.pdf)
- [C313 round-sphere geodesic/Laplace atlas](henon_round_sphere_geodesic_laplace_route_a/README.md) · [paper PDF](henon_round_sphere_geodesic_laplace_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C309_C313.md),
[batch plan](BATCH_PLAN_C309_C313.md), and
[batch review](BATCH_REVIEW_C309_C313.md) for collision screening, theorem
contracts, historical ownership, exact release receipts, and deterministic
PDFs.  Across the five packages the final audit closes **36,347**
independent-checker assertions, **1,366** exact symbolic identities/groups,
**142/142** hostile rejections, **1,313,011** evidence bytes, 135 manifest
payloads (140 physical files), and **11** final-paper pages with **107**
embedded/subset font records.  The five strict tuples, in order C309--C313,
are
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.
All five remain `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false` and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target zero match,
Hilbert--Polya operator, or Route-B input is claimed.

## Route-A independent cross-subtype round C304--C308

This round takes five independent theorem-scale steps and changes the phase
space, clock, and proof mechanism in every paper: a fourth-order periodic PDE
semigroup, a continuous-time navigation control problem, a killed
determinantal walker system, a monotone random graph process, and a
non-normal quantum lattice Hamiltonian.  These are five complete papers, not
five installments of one theorem.

- [C304 multidimensional linear Cahn--Hilliard spinodal semigroup](henon_linear_cahn_hilliard_spinodal_route_a/README.md) · [paper PDF](henon_linear_cahn_hilliard_spinodal_route_a/paper/main.pdf)
- [C305 constant-wind Zermelo navigation atlas](henon_constant_wind_zermelo_navigation_route_a/README.md) · [paper PDF](henon_constant_wind_zermelo_navigation_route_a/paper/main.pdf)
- [C306 killed noncolliding continuous-time walkers](henon_killed_noncolliding_walkers_route_a/README.md) · [paper PDF](henon_killed_noncolliding_walkers_route_a/paper/main.pdf)
- [C307 Erdos--Renyi connectivity first-passage process](henon_erdos_renyi_connectivity_hitting_route_a/README.md) · [paper PDF](henon_erdos_renyi_connectivity_hitting_route_a/paper/main.pdf)
- [C308 Hatano--Nelson boundary and skin-effect atlas](henon_hatano_nelson_boundary_skin_route_a/README.md) · [paper PDF](henon_hatano_nelson_boundary_skin_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C304_C308.md),
[batch plan](BATCH_PLAN_C304_C308.md), and
[batch review](BATCH_REVIEW_C304_C308.md) for collision screening, theorem
contracts, historical ownership, hostile-review repairs, exact release
receipts, and deterministic PDFs.  Across the five packages the final audit
closes **15,143** independent-checker assertions, **881** exact symbolic
identities/cells, **350/350** hostile rejections, **397,400** evidence bytes,
135 manifest payloads (140 physical files), and **15** final-paper pages with
**116** embedded/subset font records.  The five strict tuples, in order
C304--C308, are
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
All five remain `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false` and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target zero match,
Hilbert--Polya operator, or Route-B input is claimed.

## Route-A independent cross-subtype round C299--C303

This round takes five independent theorem-scale steps while changing the
dynamical owner, state space, clock and proof mechanism in every paper: a
viscous radial vorticity PDE, a strictly hyperbolic conservation law, an
absorbing partition-lattice chain, a recursive random algorithm and a
dissipative quantum channel.  These are five complete papers, not five
installments of one theorem.

- [C299 Lamb--Oseen radial self-similar vortex](henon_lamb_oseen_self_similar_vortex_route_a/README.md) · [paper PDF](henon_lamb_oseen_self_similar_vortex_route_a/paper/main.pdf)
- [C300 positive-density isothermal Euler Riemann solver](henon_isothermal_euler_riemann_solver_route_a/README.md) · [paper PDF](henon_isothermal_euler_riemann_solver_route_a/paper/main.pdf)
- [C301 parallel binary partition fragmentation](henon_parallel_binary_partition_fragmentation_route_a/README.md) · [paper PDF](henon_parallel_binary_partition_fragmentation_route_a/paper/main.pdf)
- [C302 randomized Quicksort comparison-cost contraction](henon_quicksort_comparison_contraction_route_a/README.md) · [paper PDF](henon_quicksort_comparison_contraction_route_a/paper/main.pdf)
- [C303 thermal-qubit Lindblad entanglement-breaking atlas](henon_thermal_qubit_lindblad_entanglement_breaking_route_a/README.md) · [paper PDF](henon_thermal_qubit_lindblad_entanglement_breaking_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C299_C303.md),
[batch plan](BATCH_PLAN_C299_C303.md), and
[batch review](BATCH_REVIEW_C299_C303.md) for collision screening, theorem
contracts, historical ownership, hostile-review repairs, exact release
receipts and deterministic PDFs.  Across the five packages the final audit
closes **15,070** independent-checker assertions, **20,524** symbolic checks,
**358/358** hostile rejections, **722,186** evidence bytes, 135 manifest
payloads (140 physical files), and **16** final-paper pages with **116**
embedded/subset font records.  The five strict tuples, in order C299--C303,
are
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
All five remain `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false` and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target zero match,
Hilbert--Polya operator, or Route-B input is claimed.

## Route-A independent cross-subtype round C294--C298

This round takes five independent theorem-scale steps while changing the
dynamical owner, state space, clock, and proof mechanism in every paper: an
open dispersing billiard, an integrable central-force flow, a many-body
hard-collision quotient, a non-Hermitian projective flow, and a compact
Grassmann gradient flow.  These are five complete papers, not five
installments of one theorem.  The hard-rod proposal was materially corrected
from a false full physical quotient to the exact rotation-reduced shape flow.

- [C294 equilateral three-disk no-eclipse collision coding](henon_three_disk_open_billiard_route_a/README.md) · [paper PDF](henon_three_disk_open_billiard_route_a/paper/main.pdf)
- [C295 Hénon isochrone action--frequency and closure atlas](henon_isochrone_action_frequency_route_a/README.md) · [paper PDF](henon_isochrone_action_frequency_route_a/paper/main.pdf)
- [C296 rotation-reduced circular hard-rod shape flow](henon_hard_rod_rotation_reduced_shape_route_a/README.md) · [paper PDF](henon_hard_rod_rotation_reduced_shape_route_a/paper/main.pdf)
- [C297 PT-symmetric balanced-gain/loss dimer phase atlas](henon_pt_symmetric_dimer_route_a/README.md) · [paper PDF](henon_pt_symmetric_dimer_route_a/paper/main.pdf)
- [C298 exact Schubert and Morse--Bott Grassmann projection flow](henon_grassmann_projection_flow_route_a/README.md) · [paper PDF](henon_grassmann_projection_flow_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C294_C298.md),
[batch plan](BATCH_PLAN_C294_C298.md), and
[batch review](BATCH_REVIEW_C294_C298.md) for collision screening, theorem
contracts, historical ownership, the periodic-ray multiplicity repair, the
rotation-quotient correction, type-and-polarity hostile review, deterministic
PDFs, and exact receipts.  Across the five packages the final audit closes
**115,411** independent-checker assertions, **161,630** symbolic checks,
**409/409** hostile rejections, **412,477** evidence bytes, 135 manifest
payloads (140 physical files), and **19** final-paper pages with **106**
embedded/subset font records.

The strict tuples, in order C294--C298, are
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
All five remain `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false` and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local data, Euler factor,
root number, automorphy object, target divisor/counting law or functional
equation, target zero match, Hilbert--Pólya operator, or Route-B input is
claimed.

Final PDF SHA-256 values, in order C294--C298, are
`a8d7f4c1a0aa4b2bca95435348e6305c942cf226f3201157d8a2e0f8105606d8`,
`e89f5fa8ba9d9b2148f7d15d2b1d48d6767681278ff6c123fd61f2e673b87f3b`,
`dc8890acabb563e3de21572381e479c8ac7ea2a23e6e4077aab4f8bffa6589f9`,
`a6122768fabaa99cfa3ab62ef28384a5360103c029ce4393fe94f16d4537fc82`,
and `37c2512b70f1042b18b3fc89282fa58f82d65897e9e4c6aab6f8199957477295`.

## Route-A independent cross-subtype round C289--C293

This round takes five separate theorem-scale steps while changing the owner,
state space, clock, and proof mechanism in every paper: a homogeneous magnetic
flow on the hyperbolic plane, a singular rotating celestial Hamiltonian, a
finite stochastic greedy-adsorption process, an irreversible all-event
particle coalescence flow, and a degenerate magnetic quantum operator.  The
five manuscripts are independent results, not installments of one theorem.

- [C289 hyperbolic constant-magnetic-flow orbit atlas](henon_hyperbolic_constant_magnetic_flow_route_a/README.md) · [paper PDF](henon_hyperbolic_constant_magnetic_flow_route_a/paper/main.pdf)
- [C290 five Lagrange equilibria and defective Gascheau--Routh boundary](henon_cr3bp_lagrange_stability_route_a/README.md) · [paper PDF](henon_cr3bp_lagrange_stability_route_a/paper/main.pdf)
- [C291 exact path/cycle dimer-RSA laws](henon_dimer_rsa_path_cycle_route_a/README.md) · [paper PDF](henon_dimer_rsa_path_cycle_route_a/paper/main.pdf)
- [C292 arbitrary finite all-event sticky-particle flow](henon_sticky_particle_all_event_route_a/README.md) · [paper PDF](henon_sticky_particle_all_event_route_a/paper/main.pdf)
- [C293 flux-driven magnetic Grushin spectral transition](henon_magnetic_grushin_cylinder_route_a/README.md) · [paper PDF](henon_magnetic_grushin_cylinder_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C289_C293.md),
[batch plan](BATCH_PLAN_C289_C293.md), and
[batch review](BATCH_REVIEW_C289_C293.md) for collision screening, proof
contracts, historical ownership, independent hostile reviews, the base-point
return and resonant-multiplicity repairs, strict duplicate-rejecting JSON/YAML
release gates, deterministic PDFs, and exact receipts.  Across the five
packages the final audit closes **28,356** independent-checker assertions,
**1,554** symbolic checks, **354/354** hostile rejections, **167,316** evidence
bytes, 135 manifest payloads (140 physical files), and **21** final-paper pages
with **118** embedded/subset font records.

The strict tuples, in order C289--C293, are
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,`\
`A3_PARTIAL_ANALYTIC_STRUCTURE,A4_NATURAL_QUANTIZATION)`.
All five remain `ROUTE_A_REJECTED`, with
`route_b_invocation_allowed: false` and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local data, Euler factor,
root number, automorphy object, target divisor/counting law or functional
equation, target zero match, Hilbert--Pólya operator, or Route-B input is
claimed.

Final PDF SHA-256 values, in order C289--C293, are
`c3361619fe4d967223415894bd712a772989827a0ebc2de5b0fd98872b328cd1`,
`88ce6ad9ad23e0cebea986cf9305bc6b258c5816170120e656c334b0b38aed9e`,
`b410ec70209302f891992712b4a6be16663e04d2a79cd6f7e4f1e762fef64a22`,
`b91f101d7947d4a5e5feeaf3a2dd2d405a3308ed1e0ec8bf984be2cdf262f6d8`,
and `3295011b255e5e70761bd1119af1b8b72453b0724cfbb21663614321a763935d`.

## Route-A independent cross-subtype round C284--C288

This round takes five complete theorem-scale steps while changing the owner,
state space, clock, and proof mechanism in every paper: a singular
point-vortex Hamiltonian, a nonreversible closed queueing CTMC, a
state-dependent Coxeter rewrite system, a boundary-controlled hyperbolic PDE,
and a singular self-adjoint quantum Hamiltonian.  The manuscripts are
independent results, not five installments of one calculation.

- [C284 Thomson polygon point-vortex linear-stability atlas](henon_thomson_polygon_point_vortex_stability_route_a/README.md) · [paper PDF](henon_thomson_polygon_point_vortex_stability_route_a/paper/main.pdf)
- [C285 Gordon--Newell bottleneck-condensation theorem](henon_gordon_newell_bottleneck_condensation_route_a/README.md) · [paper PDF](henon_gordon_newell_bottleneck_condensation_route_a/paper/main.pdf)
- [C286 finite Coxeter numbers-game strong-convergence theorem](henon_coxeter_numbers_game_strong_convergence_route_a/README.md) · [paper PDF](henon_coxeter_numbers_game_strong_convergence_route_a/paper/main.pdf)
- [C287 exact minimal time for one-end string observation and control](henon_wave_boundary_control_minimal_time_route_a/README.md) · [paper PDF](henon_wave_boundary_control_minimal_time_route_a/paper/main.pdf)
- [C288 delta point-interaction spectral/heat atlas](henon_delta_point_interaction_spectral_dynamics_route_a/README.md) · [paper PDF](henon_delta_point_interaction_spectral_dynamics_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C284_C288.md),
[batch plan](BATCH_PLAN_C284_C288.md), and
[batch review](BATCH_REVIEW_C284_C288.md) for the collision scan, frozen
theorem contracts, source-owner boundaries, exact evidence, hostile semantic
repairs, independent formula reconstructions, deterministic PDFs, and release
receipts.  Across the five packages the final strengthened audit closes
**100,869** independent-checker assertions,
**5,322** symbolic checks, **277/277** hostile rejections,
**2,470,926** evidence bytes, 135 manifest payloads (140 physical files), and
**19** final-paper pages with **113** embedded/subset font records.  All five are
`ROUTE_A_REJECTED`; Route B is disabled and the common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.  The heptagon conclusion is explicitly linear
only, finite executable cells do not replace the arbitrary-size/PDE/operator
proofs, and classical source ownership is named.  No target arithmetic local
data, Euler factor, root number, automorphy object, target divisor/counting law
or functional equation, Hilbert--Pólya operator, or Route-B input is claimed.

Final PDF SHA-256 values, in order C284--C288, are
`6b1501af2dba761ad34e87cc89502c8f4ba8e9c8bb04ed7771ef49f6bf009f6f`,
`088d2ca85d86d1e1fc797071bef5aa8c4a4364178f0ab61f454d77df14e6000e`,
`3a3684fe15c61d0e6fa76b46a0719a80e3e63d1a6a2a6091028f11d95a92e518`,
`e0fb034b86b6016aca38207387bcd3152eba62ce76e85b08c2239305f2e23fe7`,
and `f6d2973ac3523a6b29609820e348f45cddec81135ee36f02d6f6019ad05dae35`.

## Route-A independent cross-subtype round C279--C283

This round takes five separate theorem-scale steps in five different
dynamical categories: a nonsmooth convex coalescence flow, a projective
orientation flow, a nonlinear geometric metric flow, a killed stochastic
first-passage process, and a compact ultrametric Markov semigroup.  A drafted
dimer-RSA candidate was retired after the hostile collision scan and replaced
by the product-spheres Ricci-flow paper; the five released manuscripts are
independent results, not installments of one calculation.

- [C279 path-graph total-variation flow and all-time ROF identity](henon_path_graph_total_variation_flow_route_a/README.md) · [paper PDF](henon_path_graph_total_variation_flow_route_a/paper/main.pdf)
- [C280 Jeffery--Bretherton planar projective-orientation atlas](henon_jeffery_bretherton_planar_orientation_route_a/README.md) · [paper PDF](henon_jeffery_bretherton_planar_orientation_route_a/paper/main.pdf)
- [C281 product-spheres homogeneous Ricci-flow singularity atlas](henon_product_spheres_ricci_flow_route_a/README.md) · [paper PDF](henon_product_spheres_ricci_flow_route_a/paper/main.pdf)
- [C282 exponential Cramér--Lundberg joint ruin atlas](henon_cramer_lundberg_exponential_ruin_route_a/README.md) · [paper PDF](henon_cramer_lundberg_exponential_ruin_route_a/paper/main.pdf)
- [C283 p-adic conductor-shell heat-semigroup atlas](henon_padic_conductor_shell_heat_semigroup_route_a/README.md) · [paper PDF](henon_padic_conductor_shell_heat_semigroup_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C279_C283.md),
[batch plan](BATCH_PLAN_C279_C283.md), and
[batch review](BATCH_REVIEW_C279_C283.md) for the model replacement,
direct-owner corrections, theorem contracts, exact evidence, hostile
proof/checker repairs, deterministic PDFs and release receipts.  Across the
five packages the round closes **1,026,482** independent-checker assertions,
**3,883** symbolic checks, **178/178** hostile rejections, **1,279,791**
evidence bytes, 135 manifest payloads (140 physical files), and **16**
final-paper pages with **106** embedded/subset font records.  All five are
`ROUTE_A_REJECTED`; Route B is disabled and the common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.  C279 and C283 explicitly credit the direct
owners of their central source-side phenomena; no literature originality is
inferred from workspace packaging.  No target arithmetic local data, Euler
factor, root number, automorphy object, target divisor/counting law or
functional equation, Hilbert--Pólya operator, or Route-B input is claimed.

Final PDF SHA-256 values, in order C279--C283, are
`83b2d3b5cb296c37edf10cd6120ff430750953ed39c11a74cc467b207a1dc024`,
`768d840bfbde6ceb4632bc1d48c10faea5ec267c743e190986824dc467a81035`,
`93b6aaf8229ec317c4933cf5bf264f82501c64ec1c7121625f2b27860e6a4d8a`,
`bb934cc9ed23105dac16c3ee7dba1acd37f0826f8da7a0b5c215f97ff9e4218e`,
and `9d789d9533e54eb6228f04dece3595a10281c60ae730d53fd3ae6755a64befde`.

## Route-A independent cross-subtype round C274--C278

This round changes mathematical owner, state space, clock, and proof
technology in every paper: a six-dimensional magnetic Hamiltonian, an
integrable confocal billiard map, a random finite self-map, a
fractional-memory operator family, and a singular invariant manifold of an
integrable PDE.  Each manuscript takes one complete theorem-scale step; the
five papers are not installments of one calculation.

- [C274 ideal Penning-trap symplectic, stability and resonance atlas](henon_penning_trap_symplectic_atlas_route_a/README.md) · [paper PDF](henon_penning_trap_symplectic_atlas_route_a/paper/main.pdf)
- [C275 confocal elliptic-billiard Poncelet rigidity theorem](henon_elliptic_billiard_poncelet_route_a/README.md) · [paper PDF](henon_elliptic_billiard_poncelet_route_a/paper/main.pdf)
- [C276 uniform random-mapping functional-graph theorem](henon_uniform_random_mapping_functional_graph_route_a/README.md) · [paper PDF](henon_uniform_random_mapping_functional_graph_route_a/paper/main.pdf)
- [C277 Caputo fractional Dirichlet heat-flow theorem](henon_caputo_fractional_dirichlet_heat_route_a/README.md) · [paper PDF](henon_caputo_fractional_dirichlet_heat_route_a/paper/main.pdf)
- [C278 signed Camassa--Holm two-peakon scattering/collision atlas](henon_camassa_holm_two_peakon_route_a/README.md) · [paper PDF](henon_camassa_holm_two_peakon_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C274_C278.md),
[batch plan](BATCH_PLAN_C274_C278.md), and
[batch review](BATCH_REVIEW_C274_C278.md) for collision screening, frozen
theorem contracts, exact evidence, proof and semantic-checker repairs,
originality/citation review, and release receipts.  Across the five packages
the round closes 10,444 independent-checker assertions, 1,322 symbolic
checks, 129/129 hostile rejections, 719,457 evidence bytes, 135 manifest
payloads (140 physical files), and 15 final-paper pages with 103
embedded/subset font records.  All five are `ROUTE_A_REJECTED`; Route B is
disabled and the common scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  No target
arithmetic local data, Euler factor, root number, automorphy object, target
divisor/counting law or functional equation, Hilbert--Pólya operator, or
Route-B input is claimed.

Final PDF SHA-256 values, in order C274--C278, are
`960afb3c5ec99cbd320a033c72affbc3cde357b0fe4b4cee6c741de773df9d42`,
`77b15baa296c7107990f36208099118e7186632a2fc075a3087d74989ec948a1`,
`ff5bee778af4d778c73ffdc1e38b457d64e1babe5050bb16588b72023d035972`,
`c3efe7030d157fbbe1a7b0a45b2bda73973a8bc5070af9968facef32297fc169`,
and `3aef1600dc97bb94cb50922ba7d135950ee9db37295a40268467a474b36faa67`.

## Route-A independent cross-subtype round C269--C273

This round again changes mathematical owner in every paper and takes one
complete theorem-scale step in each: a nonlinear finite-field functional
graph, a sub-Riemannian Hamiltonian control flow, a cooperative epidemic
network, an infinite-dimensional age-transport semigroup, and a stochastic
fluctuation process.  The five papers are independent results rather than
installments of one calculation.

- [C269 finite-field Chebyshev functional graph and Koopman atlas](henon_finite_field_chebyshev_functional_graph_route_a/README.md) · [paper PDF](henon_finite_field_chebyshev_functional_graph_route_a/paper/main.pdf)
- [C270 standard Heisenberg cut, conjugate and distance atlas](henon_heisenberg_subriemannian_cut_locus_route_a/README.md) · [paper PDF](henon_heisenberg_subriemannian_cut_locus_route_a/paper/main.pdf)
- [C271 irreducible network-SIS threshold and critical Perron law](henon_network_sis_threshold_critical_route_a/README.md) · [paper PDF](henon_network_sis_threshold_critical_route_a/paper/main.pdf)
- [C272 Erlang age-transport renewal and essential-spectrum atlas](henon_erlang_age_transport_spectral_route_a/README.md) · [paper PDF](henon_erlang_age_transport_spectral_route_a/paper/main.pdf)
- [C273 Sparre--Andersen survival and two arcsine laws](henon_sparre_andersen_universal_fluctuation_route_a/README.md) · [paper PDF](henon_sparre_andersen_universal_fluctuation_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C269_C273.md),
[batch plan](BATCH_PLAN_C269_C273.md), and
[batch review](BATCH_REVIEW_C269_C273.md) for collision screening, frozen
theorem contracts, exact evidence, proof repairs, originality/citation review
and release receipts.  Across the five packages the round closes 65,525
independent-checker assertions, 823 symbolic checks, 114/114 hostile
rejections, 2,734,029 evidence bytes, 135 manifest payloads (140 physical
files), and 13 final-paper pages with 111 embedded/subset font records.  C269
is `ROUTE_A_EXPLORATORY`; C270--C273 are `ROUTE_A_REJECTED`.  Route B is
disabled and the common scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  No target
arithmetic local data, Euler factor, root number, automorphy object, target
divisor/counting law or functional equation, Hilbert--Pólya operator, or
Route-B input is claimed.

Final PDF SHA-256 values, in order C269--C273, are
`c966e31fe276300869a18ff7460952f850b7810e1cc0d4df3481d62da0fd5e0a`,
`21134aa7aa51475bb686a9ceae9ebe83414aee6ebd38f2b8277f8f14db694cfa`,
`666b0e3e62cef878a88caf0305d9cdc6e6331e1ddab42c76369f1e9973c0c03e`,
`06bb70f11ddb1e3dbcdf72a89896b88feb843c354c29a4eac5640dfc9bc350de`,
and `0f81c47565325f0a1fd296f8de0af7468638bc9981f197b9ed08d4cacda80b52`.

## Route-A independent cross-subtype round C264--C268

This round changes mathematical owner in every paper and takes one complete
theorem-scale step in each: a finite-group power map, a self-exciting point
process, a local-time interface diffusion, a quantum tight-binding lattice,
and a relativistic Lorentz flow.  Each manuscript closes its full declared
parameter and boundary atlas; the five papers are independent rather than
installments of one calculation.

- [C264 finite-abelian power-map functional graph and Koopman Jordan atlas](henon_finite_abelian_power_map_route_a/README.md) · [paper PDF](henon_finite_abelian_power_map_route_a/paper/main.pdf)
- [C265 exponential-Hawkes stationary, covariance and cluster atlas](henon_exponential_hawkes_stationary_route_a/README.md) · [paper PDF](henon_exponential_hawkes_stationary_route_a/paper/main.pdf)
- [C266 skew-Brownian interface semigroup, exit and occupation atlas](henon_skew_brownian_interface_route_a/README.md) · [paper PDF](henon_skew_brownian_interface_route_a/paper/main.pdf)
- [C267 Wannier--Stark Bloch oscillation and Schatten atlas](henon_wannier_stark_bloch_route_a/README.md) · [paper PDF](henon_wannier_stark_bloch_route_a/paper/main.pdf)
- [C268 constant electromagnetic Lorentz-flow invariant-plane atlas](henon_constant_em_lorentz_flow_route_a/README.md) · [paper PDF](henon_constant_em_lorentz_flow_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C264_C268.md),
[batch plan](BATCH_PLAN_C264_C268.md), and
[batch review](BATCH_REVIEW_C264_C268.md) for collision screening, frozen
theorem contracts, exact evidence, validation and PDF receipts.  Across the
five packages the round closes
245,718 independent-checker assertions, 2,736 symbolic checks, 121/121
hostile rejections, 135 manifest payloads (140 physical files), and 12
final-paper pages with 103 embedded/subset font records.  C265--C268 are
`ROUTE_A_REJECTED`; C264 reaches only `ROUTE_A_PARTIAL` through its weak
finite-group arithmetic and complete source-local zeta/Koopman atlas.  Route B
is disabled and the common scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  No target
arithmetic local data, Euler factor, root number, automorphy object, target
divisor/counting law or functional equation, Hilbert--Pólya operator, or
Route-B input is claimed.

Final PDF SHA-256 values, in order C264--C268, are
`d3d604ea273a27c1286463b23e07ab7bda78895fd5d998a281800343a2aefc3a`,
`3c0283170bb6cf7d807e53fbcd814b268c59670649726200e0dcc9d44a98bc24`,
`eaeabde91cd9e40e80222a85e913e0706c1a9d0a548318d09a054b515a928ca3`,
`83c5a7eb7e17e770251ed769104c287e912f5a0909d8092e0926f42f472b3862`,
and `1076dfc4469cd42aa86a2addc1bd757ebb5139d2b633d5c1a7c761bcf0db180a`.

## Route-A independent cross-subtype round C259--C263

This round changes mathematical owner in every paper: a nonlinear
heterogeneous phase network on a tree, a finite-field projective group action,
a linear dispersive PDE with rational-time revivals, a periodically switched
Hamiltonian oscillator, and an exchangeable reinforced stochastic process.
Each manuscript closes one all-parameter source theorem; the five papers are
independent rather than installments of one calculation.

- [C259 heterogeneous tree-Kuramoto locking and Morse atlas](henon_tree_kuramoto_locking_morse_route_a/README.md) · [paper PDF](henon_tree_kuramoto_locking_morse_route_a/paper/main.pdf)
- [C260 projective Möbius cycle atlas over finite fields](henon_pgl2_projective_mobius_cycle_atlas_route_a/README.md) · [paper PDF](henon_pgl2_projective_mobius_cycle_atlas_route_a/paper/main.pdf)
- [C261 periodic Airy cubic-Talbot revival atlas](henon_airy_talbot_revival_route_a/README.md) · [paper PDF](henon_airy_talbot_revival_route_a/paper/main.pdf)
- [C262 square-wave Hill Floquet and band-edge atlas](henon_square_wave_hill_floquet_route_a/README.md) · [paper PDF](henon_square_wave_hill_floquet_route_a/paper/main.pdf)
- [C263 multicolor Pólya-urn and Dirichlet-limit atlas](henon_multicolor_polya_urn_dirichlet_route_a/README.md) · [paper PDF](henon_multicolor_polya_urn_dirichlet_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C259_C263.md),
[batch plan](BATCH_PLAN_C259_C263.md), and
[batch review](BATCH_REVIEW_C259_C263.md) for collision screening, theorem
contracts, exact validation counts, PDF hashes, and content-addressed release
ledgers.  Across the five packages the round closes 6,769,495 independent-
checker assertions, 302,099 symbolic checks, 179/179 hostile rejections, 135
manifest payloads (140 physical files), and 11 final-paper pages with 122
embedded/subset font records.  C259 and C261--C263 remain
`ROUTE_A_REJECTED`; C260 reaches only `ROUTE_A_EXPLORATORY` through intrinsic
finite-field arithmetic and a complete source-local cycle atlas.  Coordinates
remain candidate-local, Route B is disabled, and the common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local data, Euler factor,
root number, automorphy object, target divisor/counting law or functional
equation, Hilbert--Pólya operator, or Route-B input is claimed.

## Route-A independent cross-subtype round C254--C258

This round again changes mathematical owner in every paper: a Monod
chemostat, an Euler--Poincare--Suslov nonholonomic rigid body, KdV cnoidal
traveling waves, quadratic Newton root-finding on the Riemann sphere, and a
mixed congruential finite-ring map.  Each paper closes one all-parameter
source theorem and its Route-A boundary; none is an installment of another.

- [C254 Monod chemostat threshold and transient atlas](henon_monod_chemostat_threshold_route_a/README.md) · [paper PDF](henon_monod_chemostat_threshold_route_a/paper/main.pdf)
- [C255 Suslov nonholonomic heteroclinic and clean-rotation atlas](henon_suslov_nonholonomic_heteroclinic_route_a/README.md) · [paper PDF](henon_suslov_nonholonomic_heteroclinic_route_a/paper/main.pdf)
- [C256 KdV cnoidal--soliton traveling-wave atlas](henon_kdv_cnoidal_traveling_wave_atlas_route_a/README.md) · [paper PDF](henon_kdv_cnoidal_traveling_wave_atlas_route_a/paper/main.pdf)
- [C257 quadratic Newton--Cayley global dynamics](henon_quadratic_newton_cayley_global_dynamics_route_a/README.md) · [paper PDF](henon_quadratic_newton_cayley_global_dynamics_route_a/paper/main.pdf)
- [C258 mixed congruential Hull--Dobell atlas](henon_mixed_lcg_hull_dobell_route_a/README.md) · [paper PDF](henon_mixed_lcg_hull_dobell_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C254_C258.md),
[batch plan](BATCH_PLAN_C254_C258.md), and
[batch review](BATCH_REVIEW_C254_C258.md) for collision pivots, theorem
contracts, exact validation counts, PDF hashes, and content-addressed release
ledgers.  C254--C257 remain `ROUTE_A_REJECTED`; C258 reaches only
`ROUTE_A_EXPLORATORY` through an intrinsic but weak prime-power/CRT relation.
Coordinates stay candidate-local, Route B is disabled, and the common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local data, Euler factor,
root number, automorphy object, divisor/counting law or functional equation,
Hilbert--Pólya operator, or Route-B input is claimed.

## Route-A independent cross-subtype round C249--C253

This round switches across five unrelated owners—a smooth Liénard oscillator,
an integrable singular Hamiltonian, a finite cellular automaton, a hysteretic
hybrid relay, and a finite stochastic population process.  Each manuscript
closes one theorem-scale source-local advance with explicit boundary faces and
replayable evidence; the papers are independent, not installments of one
calculation.

- [C249 Van der Pol/Liénard limit-cycle atlas](henon_van_der_pol_lienard_limit_cycle_route_a/README.md) · [paper PDF](henon_van_der_pol_lienard_limit_cycle_route_a/paper/main.pdf)
- [C250 Ermakov--Pinney isotonic action atlas](henon_ermakov_pinney_isotonic_action_route_a/README.md) · [paper PDF](henon_ermakov_pinney_isotonic_action_route_a/paper/main.pdf)
- [C251 cyclic majority-rule 232 wall erosion](henon_majority_rule232_domainwall_route_a/README.md) · [paper PDF](henon_majority_rule232_domainwall_route_a/paper/main.pdf)
- [C252 two-threshold hysteretic relay oscillator](henon_hysteretic_relay_oscillator_route_a/README.md) · [paper PDF](henon_hysteretic_relay_oscillator_route_a/paper/main.pdf)
- [C253 Moran fixation and Green atlas](henon_moran_fixation_green_route_a/README.md) · [paper PDF](henon_moran_fixation_green_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C249_C253.md), [batch plan](BATCH_PLAN_C249_C253.md),
and [batch review](BATCH_REVIEW_C249_C253.md) for theorem increments,
collision decisions, exact audit counts, release hashes, and the fixed-epoch
PDF reproducibility record.  All five strict tuples are
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` except C250,
which has `A4_NATURAL_QUANTIZATION`; all are `ROUTE_A_REJECTED` with Route B
disabled.  The common scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; no target prime
or zero table, arithmetic local datum, Euler factor, root number, automorphy,
target divisor/counting law, functional equation, Hilbert--Pólya operator, or
Route-B input is claimed.

## Route-A independent cross-subtype round C244--C248

This round takes one theorem-scale step in each of five independent owners and
switches subtype in every slot: a focus--focus integrable Hamiltonian, a
pulse-coupled hybrid network, a state-dependent stochastic AIMD process, a
clean-family circular billiard, and an aperiodic Rudin--Shapiro substitution.
Each package closes its source-local theorem, explicit boundary faces, and
replayable evidence chain; none is an installment of another paper.

- [C244 spherical-pendulum cubic chambers and focus--focus monodromy](henon_spherical_pendulum_monodromy_route_a/README.md) · [paper PDF](henon_spherical_pendulum_monodromy_route_a/paper/main.pdf)
- [C245 pulse-coupled integrate-and-fire event maps and synchrony](henon_pulse_coupled_integrate_fire_sync_route_a/README.md) · [paper PDF](henon_pulse_coupled_integrate_fire_sync_route_a/paper/main.pdf)
- [C246 TCP/AIMD affine perpetuity and Palm occupation law](henon_tcp_aimd_perpetuity_renewal_route_a/README.md) · [paper PDF](henon_tcp_aimd_perpetuity_renewal_route_a/paper/main.pdf)
- [C247 circular-billiard clean primitive-family atlas](henon_circular_billiard_clean_orbit_atlas_route_a/README.md) · [paper PDF](henon_circular_billiard_clean_orbit_atlas_route_a/paper/main.pdf)
- [C248 Rudin--Shapiro Hadamard cocycle and diffraction certificate](henon_rudin_shapiro_diffraction_cocycle_route_a/README.md) · [paper PDF](henon_rudin_shapiro_diffraction_cocycle_route_a/paper/main.pdf)

See the [idea report](IDEA_REPORT_C244_C248.md), [batch plan](BATCH_PLAN_C244_C248.md),
and [batch review](BATCH_REVIEW_C244_C248.md) for collision decisions,
theorem increments, exact audit counts, release hashes, and the complete
fixed-epoch PDF reproducibility record.  The round closes 7,394 independent
checker assertions, 1,066 symbolic identities, 184 hostile rejections, 135
content-addressed payloads (140 physical files), and 12 final-paper pages with
121 embedded/subset font entries.  The strict tuples, in order C244--C248, are
(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION),
(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT),
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT),
(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION), and
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT).  All five are
ROUTE_A_REJECTED, Route B is disabled, and the common scope is
NO_BAD_EULER_OR_ROOT_NUMBER.  No target prime/zero table, arithmetic local
datum, Euler factor, root number, automorphy, target divisor/counting law,
functional equation, Hilbert--Pólya operator, or Route-B input is claimed.
