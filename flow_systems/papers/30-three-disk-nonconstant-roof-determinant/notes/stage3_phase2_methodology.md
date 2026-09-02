criteria_binding_unavailable

contract_role: methodology
## Dimension Scores

### D1: methodology_rigor
score: warn
trigger: "The validation strategy would remain viable, but one or more uncertainty dependencies, norm conversions, conditioning assumptions, stopping rules, or replay obligations would be incompletely specified."

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: pass

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

The manuscript offers a careful prospective design for deciding whether a classical determinant belongs to the frozen physical three-disk flow. It correctly treats the geometry-to-roof map, operator eligibility, coefficient correspondence, error propagation, physical controls, and directional nontransfer as dependent gates rather than interchangeable checks. It also distinguishes four numerical approximation channels from geometry/roof-input uncertainty and refuses to add heterogeneous tolerances without a common norm, stability map, dependency treatment, and determinant-conditioning argument. These are genuine methodological strengths. The scientific roof, operator, coefficients, determinant, enclosure, controls, and nontransfer witness were not executed, and the report does not claim otherwise. D1 warns because the central error and control contracts remain prose-level obligations without the exact norms, domains, transformations, constants, schemas, or replay fixtures needed for application. D3 passes because internal calibration is never promoted to physical identity, finite agreement is not promoted to global equivalence, and no unexecuted gate is reported as a result.

### S1: Three levels of agreement are kept distinct
The separation of formal, analytic, and finite numerical agreement prevents algebraic consistency or a visually stable computation from being treated as evidence for the physical roof.
**Evidence Anchor**: text: §1, Typed claim graph and falsifiability — "Each level can reveal an implementation inconsistency, but none by itself identifies the roof as the Euclidean-flight roof of the frozen geometry."

### S2: Heterogeneous errors are not summed by default
The paper correctly recognizes that roof input, orbit tails, projection, evaluation, and roundoff enter at different stages and require explicit transport into a common quantity before an enclosure is meaningful.
**Evidence Anchor**: text: §4, Gate 4 — "These bounds cannot simply be summed."

### S3: Gate ordering prevents retrospective repair
The dependency graph makes each artifact consume the exact upstream artifact and disallows a successful later calculation from validating an earlier type or applicability failure.
**Evidence Anchor**: text: §4, Gate dependencies, artifacts, and independent replay — "A later gate cannot retroactively validate an earlier one."

### W1: The five-channel error contract lacks an executable inequality
**Problem**: The manuscript enumerates required channels and connecting maps but does not select the roof, operator, coefficient, or output norms; state a composed inequality; identify a complex domain; or define the determinant quantity and its conditioning metric.
**Evidence Anchor**: text: §4, Prospective composition of the five error channels — "No such domain, output tolerance, or conditioning constant is reported here"
**Why it matters**: Without these fields, a future implementation cannot determine whether two bounds share units, whether dependencies are covered, or whether the propagated error encloses the claimed determinant output. This is central to the manuscript's methodological contribution.
**Suggestion**: Add a typed error theorem template with the exact spaces, norms, domains, maps, constants, dependency ledger, output functional, condition number, and fail conditions; include a worked symbolic composition showing which raw bounds are consumed at each edge without inventing numerical values.
**Severity**: Major
**Confidence**: 5 — core expertise: validated numerics and perturbation contracts

### W2: The proposed physical-control family is not operationally defined
**Problem**: Unit, pointwise-shuffled, and neighboring-geometry roofs are required on a common coding interface, but the manuscript does not define the shuffle operation, its regularity and admissibility constraints, the neighboring-geometry matching rule, or predeclared comparison metrics and tolerances.
**Evidence Anchor**: text: §4, Gate 5 — "Unit-roof, pointwise-shuffled-roof, and neighboring-geometry controls must be constructed as actual roofs on the same coding interface."
**Why it matters**: An arbitrary shuffle can cease to be a lawful roof, alter regularity, or create a control whose difference from the physical object is uninterpretable. Outcome-dependent selection of a neighboring geometry would also defeat the stated firewall.
**Suggestion**: Define every control as a deterministic transformation of a frozen roof object, state preserved and deliberately broken properties, pre-register geometry parameters and comparison functionals, and require the same operator/error pipeline and replay checks for all controls.
**Severity**: Major
**Confidence**: 4 — core expertise: control design for validated computation

### W3: The only executed method lacks a reproducible search and passage package
**Problem**: The manuscript provides aggregate search counts and a closed bibliography, but not the exact queries, row-level screening ledger, or source passages and theorem-hypothesis maps underlying its 26 source-role assignments.
**Evidence Anchor**: absence: Executed Methodology and Acknowledged Limitations — expected exact search strings, a screening-decision ledger, and claim-level passage locators; checked §§3, 8, and references.bib
**Why it matters**: Readers cannot independently recreate the admitted corpus or verify that the proposed operator, determinant, numerical, and cohomological components have the narrow roles attributed to them. Correction-aware metadata closure alone does not resolve this.
**Suggestion**: Publish a hash-bound retrieval and screening supplement plus exact passage locators, hypothesis records, correction applicability, and prohibited-transfer fields for every decision-bearing source claim.
**Severity**: Major
**Confidence**: 4 — adjacent expertise: reproducible evidence synthesis

## Arithmetic Receipts
no_recomputable_statistics: Checked the reported workflow tallies of 68 manifestations, 16 duplicates, 52 unique screened records, 26 admitted records, 24 peer-reviewed records, 26 verified identifiers, six thematic groups, six compatibility tensions, three correction-companion omissions, and 144 batch citation pairs; these are inventory or design counts, and no reported t, z, F, chi-square, discrete mean/SD, or test-specific df/N claim is covered by p_from_test_statistic, grim, grimmer, or n_from_df.
