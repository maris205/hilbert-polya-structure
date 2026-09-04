# Route-A idea report: C364--C368

## Round objective and frozen baseline

The user authorized exactly five independent papers and asked that every paper
take a theorem-scale step in a different dynamical subtype.  The collision scan
covered the C1--C363 candidate and obstruction registries, the first-level
project inventory, recent batch reports, and mechanism-level neighbours.  The
five retained owners are an arithmetic reduction permutation, a collective
integrable Hamiltonian system, an engineered quantum spin chain, a reflected
piecewise-deterministic queue, and a free-boundary conformal-map evolution.
Their phase spaces, clocks, proof engines, and boundary phenomena are disjoint;
none is a parameter slice or deferred section of another paper.

The frozen collision baseline is
`323ea43f6970544467f8a89f0ed9be0c7c39f896`, the date is `2026-09-04`, and
the build epoch is `1788480000`.  Every candidate uses
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  `NEW` below is only a
workspace ownership statement, never a literature-priority claim.

## Ranked and frozen candidates

### C364 -- fixed-discriminant Gauss reduction cycles

**Owner.** Primitive indefinite integral binary quadratic forms of one fixed
positive nonsquare discriminant, acted on by a fully specified Gauss reduction
map and its finite reduced-state permutation.

**Large step.** Prove finiteness of the primitive reduced set, invertibility of
the reduced successor, decomposition into pure finite cycles, and reconstruction
of the positive projective stabilizer from the period product, with the
determinant-one generator equal to \(M\) or \(M^2\) according to parity.
Identify reversal of cycles, primitive-cycle lengths, and the exact finite
permutation zeta.  Square and invalid discriminants, odd norm sign, and
imprimitive forms are kept separate instead of being absorbed into a numerical
continued-fraction experiment; no proper/narrow class bijection is assumed.

**Nearest collisions.** Earlier packages use symbolic codings, finite group
actions, and orbit determinants, but none owns the classical fixed-discriminant
reduction permutation or its form stabilizers.

**Strict tuple.**
`(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`;
the result remains exploratory because no target arithmetic ownership or
analytic target bridge is proved, and Route B remains locked.

**Verified lineage/context sources.** Gauss reduction lineage is documented through
Uspensky, DOI `10.1090/S0002-9904-1930-05043-0`; Buell,
DOI `10.1007/978-1-4612-4542-1_3`; and Zagier,
DOI `10.1007/978-3-642-61829-1`.

### C365 -- the `U(3)` Gelfand--Tsetlin integrable system

**Owner.** The regular Hermitian coadjoint orbit of `U(3)`, equipped with the
Gelfand--Tsetlin map formed from spectra of leading principal minors and the
physical Hamiltonian time of a linear collective Hamiltonian.

**Large step.** Derive the full interlacing polytope, its regular Thimm torus,
and the exact linear flow and rational-frequency closure criterion.  Quantize
integral orbits and prove the lattice-point/branching multiplicity identity.
Delimit repeated-eigenvalue faces, polytope facets, collapsed circle actions,
and nonintegral prequantization
boundaries without treating the regular chart as global.

**Nearest collisions.** C349 owns the Neumann--Uhlenbeck system on a sphere and
several earlier candidates own toric or representation-theoretic finite
receipts.  None owns principal-minor spectral dynamics on a `U(3)` orbit or its
Gelfand--Tsetlin quantization.

**Strict tuple.**
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`;
the source-local quantization is not a target spectral realization, so the
overall result is exploratory and Route B remains locked.

**Verified lineage/context sources.** Guillemin and Sternberg, *Journal of
Functional Analysis* 52 (1983), DOI `10.1016/0022-1236(83)90092-7`, and
*Inventiones Mathematicae* 67 (1982), DOI `10.1007/BF01398934`.

### C366 -- Krawtchouk XX mirror inversion

**Owner.** The engineered open number-conserving XX chain whose one-excitation
Hamiltonian is the spin-`N/2` representation of `Omega J_x`, together with its
fermionic exterior-power lift.

**Large step.** Prove the complete Krawtchouk spectrum and propagator for every
chain length, the exact binomial endpoint law and perfect mirror time, and then
lift the mirror to every excitation sector with the wedge-reordering phase
included.  Derive the complete subset-energy multiplicity generating function
and distinguish sectorwise revival from a global Fock-space identity.  Close
one-site, zero/negative coupling, uniform-field, and revival-parity faces.

**Nearest collisions.** Earlier quantum packages own Bloch bands, Dirac
scattering, and other source Hamiltonians; none owns engineered perfect state
transfer or its all-sector fermionic phase.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; natural source
quantization does not repair the missing arithmetic owner, so Route A is
rejected and Route B remains locked.

**Verified lineage/context sources.** Christandl, Datta, Ekert, and Landahl,
DOI `10.1103/PhysRevLett.92.187902`; Albanese, Christandl, Datta, and
Ekert, DOI `10.1103/PhysRevLett.93.230502`.

### C367 -- two-state reflected Markov-fluid queue

**Owner.** A two-state continuous-time Markov additive fluid with slopes
`-d,c`, reflected at zero by the Skorokhod regulator.

**Large step.** Prove the sharp positive/null/transient recurrence trichotomy
from the stationary mean drift.  In the stable chamber reconstruct the unique
boundary atom and both interior densities, all integer workload moments, the
environment marginals, and the regulator rate.  Classify all zero switching-
and fluid-rate faces by closed environmental classes, retaining every
nonuniqueness and escape case.

**Nearest collisions.** C351 owns open Jackson quasi-reversibility and C346 a
deterministic oblique Skorokhod map.  Neither owns a Markov-additive reflected
PDMP, its critical Lindley recurrence, or the complete stationary atom/density
normalization.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A is rejected and Route B
remains locked.

**Verified lineage/context sources.** Anick, Mitra, and Sondhi,
DOI `10.1002/j.1538-7305.1982.tb03089.x`; Asmussen,
DOI `10.1080/15326349508807330`.

### C368 -- quadratic Polubarinova--Galin growth

**Owner.** The normalized quadratic conformal-map ansatz
`f(zeta,t)=a(t)zeta+b(t)zeta^2`, with `a>0` and complex `b`, for zero-surface-tension radial
Polubarinova--Galin evolution at constant signed source strength.

**Large step.** Derive the conserved complex coefficient `a^2 b`, the exact
linear area law, and the one-variable implicit solution.  Prove global forward
univalence and circularization under injection, stationarity at zero source,
and the exact first loss time under suction.  At the loss time identify the
boundary critical point and prove it is an ordinary semicubical cusp.  Separate
the circle family, initially critical maps, initially nonunivalent maps, and
unsupported higher-degree conformal-map extensions.

**Nearest collisions.** Earlier packages include geometric and curvature
flows, but none owns a moving free boundary governed by the
Polubarinova--Galin equation or a finite-time univalence wall.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; the conformal-map invariant is
source-local and supplies no Route-A arithmetic or analytic bridge.  Route A is
rejected and Route B remains locked.

**Verified lineage/context sources.** Richardson,
DOI `10.1017/S0022112072002551`; Gustafsson,
DOI `10.1007/s13324-018-0239-3`; Gustafsson and Lin,
DOI `10.5186/aasfm.2013.3802`.

## Round decision

All five candidates are retained because each supports a complete analytic
theorem and a hostilely checked finite receipt, not because it passes Route A.
C364 and C365 retain only carefully delimited weak/formal arithmetic interest;
C366--C368 are explicit negative controls.  No result in this batch introduces
target local data, Euler factors, root numbers, automorphy, a target
divisor/counting law or functional equation, a target-zero match, a
Hilbert--Polya operator, or any Route-B input.
