# Stage 2 Research Protocol — Packet Trace and Flow Zeta

Protocol status: **Phase-1 design passed adversarial review; awaiting checkpoint confirmation**  
Date: 2026-08-13  
Proposal layer: Route A / A1--A3  
External cutoff: primary sources verified through 2026-08-13; later evidence requires a versioned amendment.

## Research Question Brief

### Topic area

Natural dynamical traces, Ruelle/Fredholm determinants, and resonance structures for a continuous arithmetic flow whose rational primes index compact packets rather than isolated periodic orbits.

### Candidate questions considered

| ID | Candidate question | F | I | N | E | R | Average | Decision |
|---|---|---:|---:|---:|---:|---:|---:|---|
| A | Can the source-defined geometry and symmetries of Deninger's periodic packets determine a functorial transverse trace whose repetition terms and determinant are derived from the flow? | 3 | 5 | 5 | 5 | 5 | **4.6** | Selected as the unresolved arithmetic-survivor question |
| B | Under explicit flow-equivariance, packet-automorphism invariance, locality, and admissibility-compatibility axioms, is a packet trace unique, non-unique, or impossible? | 4 | 4 | 5 | 5 | 5 | 4.6 | Becomes sub-question 1 |
| C | Can one trace axiomatics cover both compact packets and isolated hyperbolic closed orbits while agreeing at coefficient level with the modular Ruelle quotient benchmark? | 5 | 4 | 4 | 5 | 4 | 4.4 | Calibration sub-question; too broad as the primary RQ |
| D | Does the modular Ruelle quotient meet rational-prime A2--A3 obligations once its stability denominator is removed? | 5 | 4 | 3 | 5 | 4 | 4.2 | Exact negative benchmark; much of its obstruction is already fixed by Stage 1 |
| E | Assuming a packet Euler product, can its divisor be continued to the critical strip? | 2 | 5 | 4 | 4 | 4 | 3.8 | Rejected: assumes the missing trace and risks importing `zeta` by definition |

`F/I/N/E/R` mean Feasible, Interesting, Novel, evidence-safe/Ethical, and Relevant, each on a 1--5 scale.  Candidate A is less immediately feasible than the modular benchmark because the source may not define the needed category or trace domain.  It is nevertheless selected because it addresses the only unresolved arithmetic survivor and admits a useful `NOT_TESTABLE` or obstruction outcome; D remains a theorem-level normalization and falsification control.

### Primary research question

> For the frozen Deninger system `(X_0,E_fin, phi^t)`, does the intrinsic structure of each compact periodic packet determine a functorial transverse trace—uniquely or up to a completely classified ambiguity—from which the primitive/repetition coefficients and a right-half-plane dynamical determinant follow without declaring each packet to count once?

Here `E_fin` is a local name for the explicitly allowed finite-kernel admissibility condition frozen in Stage 1, not a claim that the source assigns that canonical notation.

### FINER assessment

| Criterion | Score | Justification |
|---|---:|---|
| Feasible | 3/5 | The first go/no-go test is whether the published packet fibration supplies enough category, action, and topology to formulate the trace.  A rigorous `NOT_TESTABLE` diagnosis or no-go theorem is sufficient; full continuation is not required. |
| Interesting | 5/5 | It isolates the precise interface between the only A0-strong flow and a genuine dynamical determinant. |
| Novel | 5/5 | The source proves packet periodicity but does not supply the project-specific trace-normalization classification or comparison with isolated-orbit Ruelle weights. |
| Ethical / evidence-safe | 5/5 | No human subjects or sensitive data are involved; the design explicitly blocks target fitting and circular Euler-product definitions. |
| Relevant | 5/5 | The answer determines whether the arithmetic flow can advance from A1 weak toward A2, or whether packet multiplicity becomes a proved obstruction. |
| **Average** | **4.6/5** | Above the 3.0 threshold; no item is below 2. |

### Sub-questions and inherited bindings

1. **Existence and canonicity.** Does the source first define enough topology, morphisms, and automorphism actions to state a transverse-measure/trace problem; if so, which objects satisfy source-derived equivariance, locality/disjoint-union compatibility, and admissibility compatibility, and are they unique, classifiable, or nonexistent?  
   Binding: frozen `DEN-WITT-Z-FIN`; unchanged clock and admissibility; no target weights.  Deviation: none.
2. **Repetition and determinant.** If an admissible trace exists, what coefficients does it assign to the `r`-fold return, what abscissa follows from those coefficients, and do period-cutoff determinants converge locally uniformly there without an imposed packet-mass rule?  
   Binding: the same trace from sub-question 1; cutoff by intrinsic period; no analytic continuation claim without an operator theorem.  Deviation: none.
3. **Exact comparison and controls.** Does the derived rule agree at coefficient level with the isolated-orbit modular Ruelle logarithmic derivative under the fixed convention, and does it reject generic equal-period bundles, copied packets, rescaled transverse measures, and shuffled/composite labels?  
   Binding: `MOD-GEO` only as A1--A3 calibration; its A0 verdict remains refuted.  Deviation: none.

## Scope boundaries

### In scope

- the published topology, flow, packet fibration, orbit space, and intrinsic automorphism actions of `Gamma_p`;
- flow-specific transverse measures, periodic-equivalence/groupoid traces, or Lefschetz-type traces only to the extent forced by that geometry;
- existence, uniqueness, ambiguity, and normalization theorems;
- primitive/repetition coefficients and convergence in the absolute half-plane;
- a finite packet-index/repetition ledger used only after the trace rule is frozen, never an enumeration of all individual orbits inside a packet;
- the modular Selberg/Ruelle quotient as an exact isolated-orbit benchmark;
- generic hyperbolic flows and artificial equal-period bundles as proves-too-much controls;
- exact, conditional, numerical, heuristic, and modeling claims kept in separate evidence classes.

### Out of scope

- Riemann-zero data, zero fitting, scale fitting, unfolding, or root matching;
- defining the trace by requiring the Riemann Euler product as its output;
- arbitrary selection of one orbit from each packet;
- arbitrary probability normalization described as canonical;
- critical-line, RH, Hilbert--Polya, self-adjoint-spectrum, or Route-B claims;
- Stage-3 wave-trace or quantum-trace work;
- a general von Neumann-algebra or noncommutative-geometry programme as the main branch;
- rescuing `MOD-GEO` by changing its clock, norm, or near-prime label;
- meromorphic continuation inferred from finite cutoff stability.

### Key assumptions to test rather than adopt

1. The packet fibration has enough intrinsic symmetry to select a transverse measure.
2. A source-derived compact homogeneous base may have a canonical Haar probability, but this does **not** automatically supply a canonical lift, a global trace across all packets, or a unit contribution to a fixed-point formula.
3. A measured packet trace can be defined without making the flow operator trace class by fiat and without importing a general operator-algebra programme.
4. The `r`-fold return coefficient is determined by the same trace and not independently inserted.
5. The isolated-orbit coefficient can calibrate signs and repetitions, but is not a categorical specialization of a clean packet family unless that relationship is proved.

## Methodology Blueprint

### Research paradigm

**Selected:** theorem-led critical realism with a comparative falsification design.

The packet, flow, and symmetry statements are mathematical facts under their hypotheses, while the proposed trace interpretation is open.  The study therefore treats existence, uniqueness, and no-go theorems as primary evidence and computation only as reproducibility support.

### Method

**Type:** theoretical/computational mathematical case study with an exact benchmark.

**Specific methods:**

1. reconstruct the source-defined packet object and every action used by the proposed trace;
2. impose a go/no-go gate: define a minimal, target-free axiom list only if the source supplies the required domain, relations, and actions;
3. prove existence/uniqueness, classify ambiguity, or prove incompatibility;
4. derive repetitions and any determinant only after the trace is fixed;
5. compare any derived rule with isolated modular-orbit coefficients while refusing to call this a categorical specialization unless proved;
6. run finite deterministic sanity checks and adversarial controls without Riemann-zero data.

### Candidate and convention freeze

| ID | Frozen object | Clock | Candidate trace/determinant status | Role |
|---|---|---|---|---|
| `DEN-WITT-Z-FIN` | Deninger's rational-Witt topological `R`-flow for `Spec Z`, restricted by the Stage-1 finite-kernel condition locally named `E_fin` | additive `t` in `phi^t[P,u]=[P,exp(t)u]` | **not yet defined**; the packet-indexed Euler product is diagnostic only | primary case |
| `MOD-RUELLE` | unit-speed geodesic flow on `T1(PSL(2,Z) backslash H)` | hyperbolic arc length | direct-product `R_Gamma(s)=Z_Gamma(s)/Z_Gamma(s+1)` under the Stage-1 orientation convention | exact isolated-orbit benchmark |
| `EQUAL-PERIOD-BUNDLE` | a product/bundle of equal-period circles over an arbitrary compact base | translation along circle fibres | any trace recipe inherited from the primary case | proves-too-much control |
| `COPIED-PACKET` | disjoint union of two isomorphic copies of one packet | inherited flow time | tests additivity and multiplicity | normalization control |

No candidate determinant for `DEN-WITT-Z-FIN` is source-locked until its domain, algebra/kernel, trace, sign, repetition convention, and normalization are all explicit.  Failure to specify any of these yields `NOT_TESTABLE`, not a favorable numerical verdict.

### Minimal trace obligations to be investigated

These are research tests, not facts assumed true:

1. **Intrinsic domain:** the observable/kernel algebra is constructed from the frozen flow and packet relation, not from primes or target zeros.
2. **Flow compatibility:** time translation acts naturally on the domain and the trace respects the required invariance/covariance.
3. **Packet-automorphism invariance:** no orbit representative or coordinate chart is privileged.
4. **Disjoint-union additivity:** copied components expose whether the rule counts geometry or labels.
5. **Transverse locality:** restriction and gluing are compatible wherever the packet fibration supplies them.
6. **Finite-kernel compatibility:** the trace is well defined under the frozen admissibility relation and does not silently change `E_fin`.
7. **Two-level normalization provenance:** a transverse probability on one packet and a global trace on the disjoint union of all packets are separate obligations.  The masses of the central packet components must be derived jointly; `tau(Gamma_p)=1` for every `p` cannot be imposed because it yields Euler factors.
8. **Repetition covariance:** the `r`-fold return coefficient is derived from the same primitive object.
9. **Isolated-orbit comparison:** the fixed modular Ruelle coefficient calibrates sign, primitive length, and repetitions.  Agreement is necessary but does not prove that isolated and clean-family traces belong to one category.
10. **Analytic legitimacy:** a determinant claim states its convergence domain and the operator/nuclearity or trace-expansion theorem that supports it.

### Data and source strategy

**Primary evidence:** original/peer-reviewed sources defining Deninger's rational-Witt system and packets; primary sources on transverse/groupoid or Lefschetz traces selected only after the exact packet geometry is reconstructed; original Selberg/Ruelle/Fried/Mayer sources for the modular benchmark.

**Generated evidence:** symbolic representations of finite packet and repetition terms, exact algebraic identities, deterministic cutoff tables, and source-free control bundles.  A list of closed points of `Spec Z` is intrinsic arithmetic data, but it may not be used to choose a trace rule.

**Forbidden evidence:** Riemann zeros; fitted target scales; an Euler product used as proof of its own dynamical origin; unverified secondary summaries for theorem-level claims.

### Ordered analysis

#### Phase A — Object reconstruction

1. Freeze the exact source theorem and admissibility condition.
2. Reconstruct `Gamma_p`, its orbit fibration, base, fibres, automorphisms, and topology from primary sources.
3. Determine whether individual periodic orbits are isolated, countable, locally finite by length, or occur in continuous families.
4. Record every missing structural datum as `OPEN` or `NOT_TESTABLE`.
5. **Go/no-go gate:** if the source does not determine the relation/groupoid, morphisms, or relevant action, stop the construction and state the smallest missing definition; do not invent them from the target formula.

#### Phase B — Conventional-product obstruction

1. Test whether the ordinary isolated-orbit Ruelle product is even set-theoretically/local-finitely defined.
2. If continuous orbit families occur, prove the precise divergence/non-definition statement rather than saying only that there are “too many” orbits.
3. Separate orbit-counting failure from the possible existence of a measured or clean-family trace.

#### Phase C — Canonicity classification

1. Derive the actual symmetry group/action from the source.
2. Classify invariant transverse probability measures under the frozen obligations before discussing an operator trace.
3. Test lifting/disintegration through the packet fibration, then separately test whether a single global trace assigns packet-component masses functorially.
4. Run rescaling, copied-packet, arbitrary-base, and broken-functoriality controls.
5. Accept Haar probability only if the relevant compact homogeneous action and unique invariant probability are proved.  Even then, record only `canonical packet-base probability` until a canonical lift and a global trace normalization are separately proved.

#### Phase D — Repetition and determinant

1. Derive the trace of each `r`-fold return with its primitive length, repetition factor, sign, phase, and any transverse determinant.
2. State the trace expansion before exponentiating it.
3. Define `D_dyn` or `Z_dyn` only from that expansion.
4. Derive the abscissa from the trace masses and periods, then prove absolute/local-uniform convergence in the resulting half-plane or report failure.  Compare the result with `Re(s)>1` only afterward.
5. Treat continuation, functional equation, and divisor counting as unavailable unless derived from the same operator.

#### Phase E — Exact calibration and computation

1. Verify coefficient-level agreement with the source-verified modular Ruelle convention; do not call it an isolated-base specialization without a proved common category.
2. Compare independent direct-sum/repetition and logarithmic-derivative implementations.
3. Freeze all cutoffs and precision before generating arithmetic packet tables.
4. Report cutoff and precision drift; preserve signed/complex cancellations.
5. Do not search for, plot, or compare Riemann zeros.

### Pre-registered falsification tests

1. **Rescaling test:** if `tau` is admissible, determine whether `c tau` is also admissible.  If yes for arbitrary `c>0`, normalization is not canonical under the current axioms.
2. **Copied-packet test:** compare one packet with two disjoint isomorphic copies.  Additivity must expose multiplicity rather than silently renormalize both to one.
3. **Arbitrary-base test:** replace the arithmetic packet base by a generic compact space with equal-period fibres.  If the same proof produces the target coefficient without using arithmetic structure, flag `PROVES_TOO_MUCH`.
4. **Isolated-orbit comparison:** independently recover the exact modular Ruelle repetition convention and test coefficient agreement; this is a calibration, not evidence that packet and isolated traces have the same fixed-point theorem.
5. **Admissibility sensitivity:** only after the primary frozen evaluation, inspect whether the structural argument would change for another source-allowed condition.  This creates a new version and cannot alter the primary result retroactively.
6. **Composite/shuffle test:** shuffled packet labels and composite labels must fail the closed-point/Frobenius functoriality even if a formal product can still be written.
7. **Determinant-direction test:** distinguish `Z`, `1/Z`, `Z'/Z`, and `det(I-L_s)`; a sign or reciprocal switch is a failed convention check.
8. **Finite-stability test:** no finite convergence plot can upgrade an unproved trace or continuation theorem.

### Validity criteria

| Criterion | Protection |
|---|---|
| Construct validity | Keep packet-index product, measured trace, conventional Ruelle zeta, Fredholm determinant, and arithmetic Euler product distinct. |
| Internal validity | Derive normalization before viewing its arithmetic consequence; version every axiom and source lock. |
| External validity | Equal-period bundles, copied packets, and modular isolated orbits test both proves-too-much and coefficient-comparison behavior. |
| Mathematical validity | Theorem statements list topology, action, domain, convergence region, and all conditional hypotheses. |
| Computational validity | Deterministic code, two independent formulas where possible, fixed cutoffs, precision drift, checksums, and no best-seed reporting. |
| Citation validity | Every non-elementary structural claim is tied to a verified primary source with a locator. |

### Decision matrix

| Outcome | Required evidence | Route-A consequence |
|---|---|---|
| Canonical trace and determinant | existence plus uniqueness/classified ambiguity; a single global packet-mass rule; derived repetition coefficients and abscissa; controls pass | reevaluate Deninger A1/A2; no automatic A3 or Route B |
| Canonical packet-base probability only | unique invariant probability, but no canonical lift, global component masses, or legitimate trace/determinant | positive structural prior; A1 remains weak and A2 remains open/fail |
| Classified normalization ambiguity | nontrivial family of admissible rescalings/measures survives all source-derived axioms | new packet-normalization obstruction; A2 fails under current object |
| Conventional product undefined but measured route open | continuous/non-locally-finite orbit family blocks isolated product | proved A2 obstruction for conventional Ruelle; measured trace stays `ROUND2_CLUE` if it leaves flow scope |
| Formal Euler product only | target factor appears only after `packet mass = 1` is stipulated | `A2_FAIL`; no candidate promotion |
| Source geometry insufficient | domain/action needed for the trace is absent from the frozen object | `NOT_TESTABLE`; state the smallest missing theorem |

### A2/A3 reporting fields

If no root-matching experiment is mathematically legitimate, the evaluator's `zero_error_train`, `zero_error_validation`, `zero_error_test`, `extra_zero_count`, `missing_zero_count`, and `root_count_discrepancy` fields will be recorded as `not_applicable_no_candidate_determinant`, never as zero.  Cutoff/precision drift are reported only for an explicitly defined object.  A3 claims require continuation, divisor, functional-equation, and prefactor results for that same object.

### Limitations by design

- The primary source may not furnish enough smooth or groupoid structure to define the desired trace.
- A canonical probability measure does not by itself determine the relative masses of all packet components or make a Koopman/transfer operator trace class.
- Clean families of periodic orbits require different trace theory from isolated hyperbolic orbits; the modular benchmark cannot be transferred by analogy alone.
- Right-half-plane convergence is weaker than meromorphic continuation and says nothing about a critical line.
- This protocol cannot rule out all future enrichments of Deninger's construction; it evaluates only the frozen object.

### Ethics, reporting, preregistration, and model boundary

- Human subjects/IRB: not applicable.
- Reporting standard: theorem, algorithm, and reproducibility conventions for mathematical research; no EQUATOR checklist applies.
- Preregistration: this file is a local design freeze, not an immutable third-party registration.  Any amendment after seeing results must be appended and versioned.
- AI disclosure: literature triage, code, and adversarial audit assistance will be disclosed; all claims remain the author's responsibility.
- Cross-model review: not enabled; no unpublished material is uploaded to an external model.

## Phase-1 acceptance conditions

Phase 1 passes only if an independent Devil's Advocate audit finds no critical flaw and the user confirms the following design choices:

1. Deninger packet trace is the primary question; modular Ruelle is a benchmark, not a co-primary rescue candidate.
2. A rigorous non-existence/non-uniqueness theorem counts as a successful Stage-2 result.
3. No continuation or divisor calculation begins before a candidate trace/determinant is legitimately defined.
4. A general von Neumann-algebra construction is recorded as a clue rather than becoming the main paper.
5. A canonical Haar probability on each packet base, if found, is not by itself accepted as the global packet trace or as a proof that every packet contributes one.
