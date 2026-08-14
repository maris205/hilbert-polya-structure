# Stage 3 Research Protocol — The Same-Object Trace Bridge

Protocol status: **Phase 1 source lock and research design complete**  
Date: 2026-08-13  
Proposal layer: Route A / A3--A4  
Manuscript status: not started  
Route-B status: not invoked; `MOD-GEO` is used only as an exact calibration object

## 1. Inherited result and reason for this stage

Stage 2 closed the most immediate determinant route for the frozen arithmetic
flow `DEN-WITT-Z-FIN`:

- Deninger's source proves an arithmetic packet decomposition and the period
  law \(T_p=\log p\), but one prime labels an uncountable packet of primitive
  orbits rather than a single isolated orbit;
- the conventional product over individual primitive orbits is therefore not
  length-locally finite and diverges already inside one packet;
- normalized Haar probability on an abstract packet base, even when granted,
  does not determine a lift/disintegration (`N2`), cross-packet masses (`N3`),
  or an operator/flat/Lefschetz trace (`O-gate`);
- a packetwise determinant is consequently `NOT_TESTABLE` for the frozen
  object, rather than an unproved copy of the Riemann Euler product.

The strongest exact comparator remains `MOD-GEO`.  Its unit-speed geodesic
flow has isolated primitive/repeated closed orbits, a natural Laplace operator,
and an exact Selberg trace formula, but Stage 1 proved that its repeated length
support is disjoint from rational-prime-power logarithms.  Stage 3 therefore
does **not** try to combine Deninger's arithmetic coordinate with the modular
surface's trace/operator coordinates.  It asks what a trace bridge certifies
when every coordinate belongs to one frozen object.

## 2. Research question brief

### Primary research question

> For one frozen continuous-time flow candidate, what source-defined data are
> sufficient to promote a certified periodic-orbit contribution to a global
> trace distribution attached to a specified spectral, resonant, or
> cohomological object, and which of those gates are actually satisfied by
> `DEN-WITT-Z-FIN` and `MOD-GEO` without transferring structure between them?

The question is deliberately about a **certification boundary**, not a
universal classification of all possible quantizations.

### Sub-questions

1. What exactly is certified by each of the following theorem families:
   Duistermaat--Guillemin wave trace, Selberg trace, foliated Lefschetz trace,
   Ruelle flat trace/Pollicott--Ruelle resonances, and Gutzwiller
   semiclassics?
2. Which statements are local germs or asymptotic coefficients, which are
   global distributional identities, and which have a fixed self-adjoint
   spectral side?
3. What data must remain identical across the classical and analytic ledgers:
   candidate, clock, primitive/repetition convention, operator, domain, test
   class, trace regularization, normalization, and non-orbit terms?
4. Can the inherited modular norm theorem rule out a clock-preserving atomic
   fusion of the Deninger prime-power ledger with the modular Selberg ledger?
5. What is the smallest missing theorem for each frozen candidate after the
   comparison, without claiming that all future quantum enrichments are
   impossible?

### FINER-style assessment

| Criterion | Score | Justification |
|---|---:|---|
| Feasible | 5/5 | The target is a theorem-hypothesis audit plus two elementary non-composability statements; it does not require constructing a new operator. |
| Interesting | 5/5 | It addresses the exact point at which a local orbit resemblance is repeatedly promoted too far in Hilbert--Polya proposals. |
| Novel | 4/5 | Each trace theorem is classical or recent, but their typed applicability to the two frozen ledgers and the same-object gate are project-specific. |
| Evidence-safe | 5/5 | Every positive assertion is tied to a theorem family; missing hypotheses remain `NOT_TESTABLE`, and no zero data are used. |
| Relevant | 5/5 | The result determines whether A3--A4 can advance and prevents Route B from being opened by coordinatewise patching. |
| **Average** | **4.8/5** | The design is narrow enough to finish and strong enough to change the candidate decision. |

## 3. Scope and claim boundary

### In scope

- exact hypotheses and outputs of the five trace frameworks named above;
- the distinction between a local singular/asymptotic orbit contribution and
  a full global trace identity;
- fixed-operator, resonance-generator, cohomological, and semiclassical data
  types, kept separate;
- the two frozen candidates and compact hyperbolic controls;
- an elementary smooth-ambiguity lemma for distributions;
- a clock-support non-composability theorem for the two frozen candidates;
- A3--A4 consequence statements using the enumerations in
  `skills/route-a-evaluator.md`.

### Out of scope

- constructing a new smooth, symplectic, groupoid, or cohomological
  enrichment of Deninger's space;
- claiming that Deninger's flow admits no possible future quantization;
- claiming that every local trace theorem can never be globalized;
- a general von Neumann-algebra programme;
- a full Route-B audit, self-adjoint Hilbert--Polya operator, or completed-xi
  determinant;
- Riemann-zero lookup, fitting, unfolding, or numerical spectral matching;
- replacing the standard clocks or omitting modular continuous/scattering,
  parabolic, elliptic, identity, or zero-time contributions;
- calling Pollicott--Ruelle resonances eigenvalues of a self-adjoint quantum
  Hamiltonian.

## 4. Frozen objects and ledgers

### 4.1 `DEN-WITT-Z-FIN`

```yaml
candidate_id: DEN-WITT-Z-FIN
object: Deninger rational-Witt topological R-flow for Spec Z
admissibility: Stage-1 finite-kernel condition, locally named E_fin
dynamics: phi^t[P,u] = [P,exp(t)u]
clock: additive flow time t
primitive_ledger: compact packets Gamma_p; every orbit in Gamma_p has least period log p
repetition_ledger: k log p, k >= 1
analytic_object: absent in the frozen source
trace_functional: absent in the frozen source
quantum_operator: absent in the frozen source
forbidden_completion: importing a trace, density, operator, or packet mass from another candidate
```

The packet theorem is `PROVED`; a smooth return map, Maslov phase,
fixed-point density, trace domain, and quantum/cohomological operator are
`NOT_TESTABLE` for the frozen source.  This is an applicability statement, not
an ontology claim about every possible enrichment.

### 4.2 `MOD-GEO`

```yaml
candidate_id: MOD-GEO
base: M = PSL(2,Z) backslash H, including its cusp and elliptic orbifold structure
classical_system: unit-speed geodesic flow on T^1 M
clock: hyperbolic arc length
primitive_ledger: primitive hyperbolic conjugacy classes / primitive closed geodesics
repetition_ledger: r ell_gamma, r >= 1
operator: the standard self-adjoint Laplace-Beltrami realization on L^2(M,dmu)
spectral_parameter: lambda = 1/4 + r^2
trace_convention: complete cofinite Selberg framework; one local test-function convention was preregistered for acquisition
mandatory_terms: identity, elliptic, parabolic/cusp, discrete spectrum, continuous spectrum/scattering, hyperbolic terms
arithmetic_target_status: rational-prime support refuted under the standard clock
```

The protocol preregistered verbatim acquisition of an exact test class and
Fourier normalization before any coefficient table.  The execution amendment
in Section 9 records that this acquisition did not complete: the manuscript
therefore prints no full coefficient table and uses only a typed schematic
framework plus a separately proved convention-independent support theorem.
Compact-surface formulae may be used as controls, never as a silent replacement
for the cofinite modular formula.

### 4.3 Controls

| ID | Frozen role | What it tests |
|---|---|---|
| `COMPACT-HYP-TRACE` | one closed hyperbolic surface with its geodesic flow and Laplacian | exact same-object Selberg/wave bridge can exist without rational-prime arithmetic; proves-too-much control for A0 |
| `LOCAL-GERM-SMOOTH-SHIFT` | a trace distribution \(\Theta\) and \(\Theta+\psi\), with \(\psi\in C_c^\infty\) supported away from the audited period | identical local orbit germ does not determine a global trace distribution |
| `HBAR-FAMILY` | \(\widehat H_\hbar=\operatorname{Op}_\hbar(H)\), \(\hbar\downarrow0\) | detects replacement of a fixed operator by a varying semiclassical family |
| `MOD-OMITTED-CONTINUUM` | the modular spectral sum with scattering/continuous terms deleted | verifies that a convenient hyperbolic-only formula is not the exact cofinite trace identity |
| `CLOCK-RESCALE` | either frozen ledger after a post-hoc time rescaling | detects a false bridge produced by changing the source-locked clock |

## 5. Trace data types

The paper will not arrange the five frameworks on one vague ladder.  It will
record the following independent fields.

| Field | Allowed values | Meaning |
|---|---|---|
| analytic ledger | self-adjoint spectrum / resonances / reduced cohomology / regularized density of states | What is being traced or paired |
| trace functional | ordinary trace / distributional wave trace / flat trace / supertrace / b-trace / asymptotic regularized trace | The actual functional, not the word "trace" |
| theorem range | local near one period / global on a test space / meromorphic continuation / semiclassical window | Where the assertion holds |
| operator regime | one fixed operator / one fixed generator on anisotropic spaces / cohomological action / family indexed by \(\hbar\) | Prevents fixed/semiclassical conflation |
| orbit geometry | isolated nondegenerate / clean family / simple foliated orbit / relative fixed set | Determines the legitimate coefficient |
| equality strength | exact / exact after named regularization / asymptotic with remainder / singular-support inclusion | Prevents a local asymptotic from becoming an exact identity |

### Certification labels used in this paper

```text
LOCAL_ORBIT_GERM_CERTIFIED
GLOBAL_TRACE_DISTRIBUTION_CERTIFIED
FIXED_OPERATOR_SPECTRAL_SIDE_CERTIFIED
RESONANCE_TRACE_CERTIFIED
COHOMOLOGICAL_LEFSCHETZ_CERTIFIED
SEMICLASSICAL_ASYMPTOTIC_CERTIFIED
ARITHMETIC_SAME_OBJECT_BRIDGE_CERTIFIED
NOT_APPLICABLE_HYPOTHESES_FAIL
NOT_TESTABLE_OBJECT_MISSING
```

These labels are descriptive outputs internal to the paper.  Route-A verdicts
remain the exact enumerations required by `route-a-evaluator.md`.

## 6. The same-object trace certificate

A candidate may be credited with a classical-to-analytic trace bridge only if
one record supplies every required field below.

```yaml
candidate_id:
source_lock:
classical_phase_object:
flow:
clock:
primitive_and_repetition_ledger:
analytic_object:
hilbert_or_cohomology_space:
operator_or_action:
domain_or_topology:
trace_or_regularization:
test_function_class:
spectral_or_resonance_ledger:
global_identity_or_local_statement:
orbit_coefficients:
non_orbit_terms:
error_or_distributional_convergence:
normalization:
arithmetic_map:
```

### Gates

| Gate | Required question | Failure mode |
|---|---|---|
| `T0 Object identity` | Do all fields carry the same candidate/source-lock ID? | coordinatewise patching of unrelated objects |
| `T1 Classical ledger` | Are primitive orbits, repetitions, periods, orientations, phases, stability/clean data, and multiplicities intrinsic? | a period label or amplitude is attached afterward |
| `T2 Trace definition` | Is a trace, flat trace, b-trace, supertrace, or regularized trace defined on an explicit test class? | an orbit sum is called a trace without an analytic functional |
| `T3 Analytic ledger` | Is the spectrum, resonance set, or cohomological action tied to an explicit operator/action and domain/topology? | a formal generator or unrelated spectrum |
| `T4 Theorem extent` | Is the output local/global and exact/asymptotic, with all remainder or distributional qualifications? | one local coefficient promoted to a global identity |
| `T5 Coefficient provenance` | Do period, primitive factor, normal determinant/density, phase, sign, and multiplicity follow from that theorem? | Selberg, DG, or Gutzwiller weights copied into another geometry |
| `T6 Clock and normalization` | Are the same time variable, Fourier convention, trace normalization, and cutoff used on both sides? | post-hoc clock rescaling or missing continuous/smooth terms |
| `T7 Arithmetic promotion` | Does the same certificate derive rational-prime/prime-power support and weights? | generic exact trace formula mistaken for Riemann arithmetic |

`T0` is not clerical metadata.  It is the condition that the maps appearing in
the purported bridge have common source and target objects.  Coordinatewise
maxima across two certificates do not form a new certificate.

## 7. Pre-registered theorem candidates

### Theorem candidate A — smooth ambiguity of local trace data

Let \(U\subset\mathbb R\) be a neighborhood of a period \(T\), and suppose the
germ \(\Theta|_U\) of a distributional trace has been determined, including all
singular coefficients associated with the closed orbit(s) at \(T\).  For any
nonzero \(\psi\in C_c^\infty(\mathbb R\setminus U)\),

\[
\widetilde\Theta=\Theta+\psi
\]

has exactly the same germ at \(T\), but is a different global distribution.
Under a prior containing every possible nonzero singular location, equality
of all nonzero singular germs determines the difference only up to a
distribution smooth on \(\mathbb R\setminus\{0\}\).  If the zero germ is also
fixed, the remaining difference is globally smooth.  Without the support
prior, an unlisted delta singularity can be added.

**Planned status:** `PROVED` by the displayed construction.  
**Claim boundary:** this does not deny that a fixed operator already defines a
global wave trace.  It says that local periodic-orbit data alone cannot be used
to *construct or identify* the full trace, its zero-time/Weyl term, continuous
part, or an arithmetic explicit formula.

**Execution note (2026-08-13):** the original phrase “modulo a smooth term”
was too short until the zero germ is fixed.  The preceding punctured-line
statement supersedes that preliminary wording and matches the proved theorem.

### Theorem candidate B — clock-support non-composability

For a hyperbolic \(\gamma\in\mathrm{PSL}_2(\mathbb Z)\), write

\[
\lambda=\frac{|\operatorname{tr}\gamma|+
\sqrt{\operatorname{tr}(\gamma)^2-4}}{2}>1,
\qquad
N_\gamma=\lambda^2=e^{\ell_\gamma}.
\]

The nontrivial Galois conjugate of \(N_\gamma\) is \(N_\gamma^{-1}\).
If \(N_\gamma^r\in\mathbb Q\) for some \(r\ge1\), conjugation would give
\(N_\gamma^r=N_\gamma^{-r}\), impossible because \(N_\gamma>1\).  Hence for
every rational prime \(p\) and integers \(r,k\ge1\),

\[
r\ell_\gamma\ne k\log p.
\]

**Planned status:** `PROVED`; this rechecks the Stage-1 proof.  
**Consequence:** no atom-by-atom correspondence preserving the two standard
clocks can transfer modular Selberg coefficients to Deninger's rational-prime
packets.  
**Claim boundary:** this is not a no-go theorem for every arithmetic flow, every
time change, or every future quantization.  A time change would be a new
candidate and must restart A0--A4.

### Audit lemma C — coordinatewise promotion is invalid

Define a trace certificate as the typed record in Section 6.  A Route-A A3--A4
claim is a predicate of one record.  If record \(C_D\) supplies an arithmetic
period ledger but no analytic/trace fields, and record \(C_M\) supplies a trace
and operator but fails the rational-prime arithmetic field, selecting satisfied
fields from \(C_D\) and \(C_M\) does not instantiate the predicate because `T0`
fails.  A source-defined bridge morphism preserving clock and normalization
would be additional mathematical data, not logical inheritance.

**Planned status:** `PROVED` as a type/certificate lemma; theorem candidate B
gives the stronger candidate-specific obstruction to a period-preserving
bridge.

## 8. Framework-specific questions

### Wave trace

1. Is the operator positive self-adjoint elliptic on a closed smooth manifold?
2. Is its bicharacteristic flow the proposed classical flow?
3. Is the fixed locus clean, and what canonical density/Maslov data enter?
4. Is the theorem only a local expansion near one length, a singular-support
   inclusion, or a global equality after testing?
5. What smooth ambiguity and possible cancellation remain?

### Selberg exact trace

1. Is the classical flow the geodesic flow of the same quotient whose
   Laplacian appears spectrally?
2. Is the quotient compact or cofinite, and are cusp/scattering, elliptic,
   parabolic, identity, and hyperbolic terms all retained?
3. Is the test-function/Fourier convention frozen?
4. Are primitive/repetition and orientation/multiplicity conventions exact?
5. Does exactness concern rational primes or only hyperbolic conjugacy classes?

### Foliated Lefschetz

1. Is there a closed smooth manifold with a transversely oriented codimension-1
   foliation and smooth foliated flow?
2. Are closed orbits simple and preserved leaves transversely simple?
3. Which conormal/dual-conormal reduced cohomologies are acted on?
4. Which b-trace and renormalization choices define the distribution?
5. Are positive-dimensional terms preserved leaves, rather than families of
   periodic orbits?

### Ruelle flat trace / Pollicott--Ruelle resonances

1. Is the flow a compact smooth Anosov flow satisfying the normal-return and
   wavefront conditions?
2. Is the flat trace well defined as a pullback of the propagator kernel to the
   diagonal?
3. Are the spectral objects resonances of a generally non-self-adjoint
   generator on anisotropic spaces?
4. Which orbit distribution is exact, and which resonance expansion has a
   remainder or support restriction?
5. Is a self-adjoint quantum conclusion being imported without a theorem?

### Gutzwiller semiclassics

1. What is the family \(\widehat H_\hbar\) and the classical Hamiltonian?
2. Is \(\hbar\to0\) explicit, and is the energy window/test support fixed?
3. Are periodic orbits isolated/nondegenerate or clean, and is the time window
   finite?
4. What is the remainder (for example \(O(\hbar^\infty)\) after smoothing)?
5. Does the statement say anything exact about a single operator at
   \(\hbar=1\) and global \(E\to\infty\)?

## 9. Ordered method

### Phase A — source and convention lock

1. Verify source versions, DOI/arXiv metadata, local hashes, and theorem
   locators in `source_matrix.md`.
2. Transcribe one exact statement per framework with its hypotheses and test
   class; do not harmonize notation before the transcription is frozen.
3. Freeze the cofinite modular Selberg convention and all non-hyperbolic terms.
4. Freeze evidence labels (`PROVED`, `CONDITIONAL_THEOREM`, `OPEN`,
   `NOT_TESTABLE`, `NOT_APPLICABLE_HYPOTHESES_FAIL`).

**Phase-A execution amendment (2026-08-13).**  Items 1 and the framework-level
parts of 2 and 4 were completed.  Item 3 was not completed because neither a
full Selberg article nor the relevant Hejhal convention was locally acquired.
Rather than treat metadata as formula evidence, the manuscript uses only a
typed schematic cofinite identity.  Convention-dependent T2 and T6 fields are
therefore `NOT_TESTABLE` in this stage.  The modular clock-support theorem and
all candidate verdicts used here are independent of the missing constants.

### Phase B — applicability matrix

1. Evaluate every framework against every field in the trace certificate.
2. Mark a hypothesis failure separately from a missing object.
3. Record the strongest certified statement and the exact non-implication for
   each framework.
4. Run a second pass specifically for fixed-operator versus
   \(\hbar\)-dependent or resonance/cohomology ledgers.

### Phase C — proofs and controls

1. Prove the smooth-ambiguity lemma.
2. Reprove the modular/Deninger support-disjointness theorem.
3. Run the coordinatewise-certificate audit.
4. Remove the modular continuous/scattering terms as an explicit failed
   identity control.
5. Check that a compact hyperbolic surface passes trace gates without passing
   rational-prime A0.

### Phase D — candidate decisions

1. Give separate gate vectors for `DEN-WITT-Z-FIN` and `MOD-GEO`.
2. Do not average or take coordinatewise maxima.
3. Map only same-object results to A3 and A4 verdicts.
4. Identify the next smallest missing theorem for each object.

## 10. Decision rules

| Finding | Evidence required | Consequence |
|---|---|---|
| Local orbit contribution only | source theorem fixes a germ/asymptotic coefficient near one period | retain `LOCAL_ORBIT_GERM_CERTIFIED`; no global A3 promotion |
| Global classical/resonance trace | explicit flat trace/test class and full distribution identity for the same flow | A3 structural evidence only; no self-adjoint inference |
| Global fixed-operator trace | fixed operator/domain, spectral trace, same principal/geodesic flow, complete geometric side | potential A3/A4 evidence for that candidate |
| Semiclassical bridge | \(\hbar\)-family, energy/time localization, explicit asymptotic/remainder | `SEMICLASSICAL_ASYMPTOTIC_CERTIFIED`; not a fixed-operator identity |
| Exact trace but wrong arithmetic support | same-object trace passes while T7 fails analytically | calibration benchmark; no rational-prime Route-A promotion |
| Arithmetic periods but no trace/operator | T1 arithmetic packet ledger passes while T2--T5 cannot be stated | A3/A4 fail or remain `NOT_TESTABLE`; no borrowing from benchmark |
| Full same-object arithmetic bridge | one record passes T0--T7 | reevaluate A3--A4; still no automatic Route-B or RH claim |

## 11. Validity and falsification safeguards

| Risk | Safeguard |
|---|---|
| Equivocation on “trace” | State the trace functional, test space, and analytic ledger in every row. |
| Local-to-global overreach | Apply theorem candidate A and list all smooth/non-orbit terms. |
| Fixed/semiclassical conflation | Record the varying parameter and whether the operator changes. |
| Exactness by omission | Keep every cofinite Selberg spectral/geometric term. |
| Candidate patching | Enforce immutable `candidate_id`, clock, and normalization through T0/T6. |
| Generic geometry mistaken for arithmetic | Use a compact hyperbolic exact-trace control and re-run A0. |
| Absolute impossibility claim | Phrase failures as theorem-hypothesis inapplicability or frozen-object missing data. |
| Citation drift | Use primary originals and exact locators; any unresolved locator remains flagged. |
| Target leakage | No Riemann-zero data, fitted clock, or inserted von Mangoldt weight. |

## 12. Anticipated candidate boundary, not a result

The design expects `MOD-GEO` to be the strongest same-object classical/quantum
trace benchmark: its geodesic flow and Laplacian belong to one geometry and the
Selberg identity is exact.  It also expects T7 to fail by the inherited support
theorem.  Conversely, `DEN-WITT-Z-FIN` is expected to retain the strongest
rational-prime period ledger while failing before a trace functional or analytic
ledger can be stated.  These are pre-registered expectations, not Phase-3
findings; the applicability audit may weaken them but may not silently strengthen
them.

## 13. Ethics, reproducibility, and disclosure

- No human subjects, personal data, or IRB review are involved.
- Theoretical source checking and symbolic proofs are reproducible from the
  recorded locators and local hashes.
- Any later computation will use deterministic code and no zero tables.
- The eventual manuscript must disclose AI-assisted literature organization,
  proof checking, and drafting; mathematical responsibility remains with the
  author.
- This theoretical study does not require preregistration, but this protocol is
  frozen prospectively to prevent changing the trace definition after seeing a
  favorable comparison.

## 14. Phase-1 completion gate

Phase 1 is complete when:

- the two candidates and all clocks are frozen;
- the five trace data types are non-equivocal;
- the same-object certificate and T0--T7 gates are explicit;
- theorem candidates A--C have exact claim boundaries;
- the source matrix contains primary-source locators, evidence states,
  retrieval dates, and limitations;
- no manuscript prose, Route-B promotion, or cross-candidate hybrid has been
  created.

All six conditions are satisfied by this protocol and `source_matrix.md`.
