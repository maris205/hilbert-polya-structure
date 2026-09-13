# Paper plan: Vertical critical ideals and cyclotomic first jets of q-Painlevé I

Date: 2026-09-09. Status: `COMPLETE_SCOPE_OUTLINE_BEFORE_DRAFT`.
This is the writing plan for the admitted V1–V3 problem, not a manuscript, a new theorem,
an independent score, a page measurement, or a PDF acceptance.
The [source scope lock](notes/SOURCE_SCOPE_LOCK_20260909.md) and
[publication lock](notes/PUBLICATION_LOCK_20260909.md) bind the scientific and artifact requirements.
The authoritative statement and dependency details remain the frozen
[brief](../../docs/research-batch07/PAPER30_QPI_VERTICAL_ALPHA_CANDIDATE_BRIEF_V1_20260909.md)
and [proof map](../../docs/research-batch07/PAPER30_QPI_VERTICAL_ALPHA_CURRENT_PROOF_MAP_V1_20260909.md).

## 1. Narrative and statement contract

The mod-p formula for the divided differential detects ordinary levels but vanishes on
supersingular levels. The paper computes what that formula does not determine:
the complete first-layer coefficient ideal, its actual obstruction class, and the full
first jets at all higher cyclotomic levels. All three branches form one problem.

The abstract states the first-layer full ideal, the odd-prime truncated ideal, the distinct
characteristic-two mixed ideal, and the scope boundary. It does not claim a general new
Cartier/Bockstein method, global priority, higher full thickness, or an RH application.
No results-only short version, experimental section, numerical evidence, or appendix is planned.

The introduction distinguishes:

- first-layer perfect residue fields from the finite residue fields used by the higher geometric claims;
- identities of complete forms on the full open surface from ideal conclusions near complete smooth finite fibers;
- actual full ideals at height one from ideals after adding the square of the uniformizer at higher height;
- canonical actual obstruction arrows from one-dimensional vector-space comparisons;
- exact state orders from lower bounds and a transverse truncated length from a full critical length.

All three main results are stated with their hypotheses after the common objects are defined.
The root multiplicity is retained, and the four terminal affine lines are expressly included.
The original matrix and parameter normalization appear once and are used throughout.

## 2. Complete body organization and file ownership interface

The source root will be `paper/v1/`, with `main.tex`, `macros.tex`, `references.bib`, and
the eight section files below. The root editor owns assembly, macros, bibliography, abstract,
and all cross-section interfaces. Any delegation must give exclusive section-file ownership;
authors may report needed macro/interface changes but must not concurrently edit root-owned files.

| Section / source file | Required mathematical content | Frozen proof suppliers | Stable label prefix |
|---|---|---|---|
| 1. Introduction and main results / `sections/01-introduction.tex` | Exact original matrix, cyclotomic setup, full V1–V3 statements, state-order summary, novelty boundaries and related work | brief; verified citation records; source differences | `intro:`, `main:` |
| 2. The original surface and primitive pencil / `sections/02-surface-pencil.tex` | Eight centers/four terminal charts, polar divisor, boundary units, genuine constants, normal bundle order, complete primitive pencil, Stein non-compositeness, geometric connectedness and generic smoothness including characteristics two and three | P, Nbd, Gfield, Ucoh Steps 1–2, Gint model | `geom:` |
| 3. The actual spectral Jacobian / `sections/03-spectral-jacobian.tex` | Pure W0 geometry and finite critical algebra, two spectral charts/four endpoints, actual spectral module, rational inverse to original states, inseparable-degree exclusion, fixed Picard difference, no kernel, torsor action descent over the original field | Bbad pure W0 portions, Wreuse V2, Jspec | `spec:` |
| 4. Complete smooth fibers and the Hasse polynomial / `sections/04-closed-hasse.tex` | Geometric integrality of each already smooth complete fiber, same-energy henselian section, minimality on both sides, extension of the specified generic isomorphism and its inverse, complete spectral differential and Cartier calculation, descent of its zero property | SH, Hloc L(a), Ddiff Cartier | `hasse:` |
| 5. Integral trace calculus and global divided forms / `sections/05-integral-trace.tex` | Original cyclic insertion identity, integer trace recurrence and divisibility before reduction, arbitrary unit time, all-chart regularity, mod-p Hasse multiplier, nonreduced chart restriction lemma | Ddiff integral portions, Gint G3a/b, generic Matrix identities where appropriate | `trace:` |
| 6. The complete first-layer critical ideal / `sections/06-first-layer.tex` | Actual boundary Bockstein with constant frames, restriction via the original section 1, prime trace p-pi congruence, integer Taylor and characteristic four, actual obstruction–Cartier class, full two-direction ideal at every smooth complete-fiber point, root multiplicities and first-layer state orders | DB, prime, TH, OC; established geometry and Hasse | `first:` |
| 7. Odd-prime first jets at all higher levels / `sections/07-odd-jets.tex` | Generic weighted commutators, complete tame-block internal/external first-order terms, all-m degree support and unique digit selection, common dual-number rings and full time jets, lift-power gluing and all-chart identity, exact truncated ideals with multiple roots | Matrix generic Steps 1–3, TB all Steps 1–6, GFI common-ring and gluing interfaces, V1 | `odd:` |
| 8. Characteristic-two jets and mixed critical ideals / `sections/08-two-jets.tex` | All seven P2 steps, four-block base and genuine ambient chi, characteristic-four first-layer comparison, local difference quotient and two Cartier-parameter divisions at every point, mixed ideals and base-parameter action, all higher powers, exact versus lower-bound state orders, limitations | P2, PI, prime/TH/OC interfaces, V1 | `two:` |

The final paragraphs of Section 8 close the paper; no separate repetitive conclusion section is needed.
Two compact tables are justified by exact mappings: the eight centers/four final charts and the
state-order branches. Their role is clarity, not extra page material. No raster illustration is needed.

## 3. Claims, proof consumers, and closure checks

| Output | Body statement | Required proof closure | Explicit non-claim |
|---|---|---|---|
| Original full model and pencil | Section 2 | Actual Laurent leading term and polar divisor; integral boundary frames; all allowed small characteristics; complete fibers and four terminal lines | No use of a merely isospectral replacement surface |
| Actual closed-fiber Hasse identification | Sections 3–4 | W0 finite critical algebra before generic smoothness; actual spectral line-bundle family and original-state inverse; no inseparable hidden degree; original-field torsor; same closed energy and bidirectional minimal-model extension; Cartier on complete curve | No unknown-kernel isogeny or global rational point assumption |
| Regular divided form | Section 5 | Integer division before reduction and full-chart regularity with arbitrary unit time | No torus-only differential promoted by pointwise density |
| V1a–c | Main first-layer theorem; Section 6 | DB and restriction preserve the actual J class; p-pi trace congruence includes p=2; OC hypotheses individually supplied; image-sheaf Frobenius; nowhere-vanishing regular tangent form; both coefficients | No arbitrary scalar replacement for the actual arrows; no simple-root hypothesis |
| V2a–b | Main odd-prime theorem; Section 7 | Full internal nonresonant deformation and external terms, actual support bound, digit selection, common-ring and time matching, nonreduced gluing, V1 ideal | No natural cyclotomic embedding; no full higher-thickness ideal or exact higher supersingular order |
| V3a–d | Main characteristic-two theorem; Section 8 | All-m four-block calculation, precise chi definition, characteristic-four comparison before reducing 2, two local divisions at all endpoints, local two-coefficient elimination, original base-parameter action | No global ambient chi regularity or global lift of the block coefficient; five is only transverse truncated length; T is not a new formal modulus |
| State orders | Main summary; deductions after Sections 6–8 | Evaluation of the proved local ideals along the allowed unramified states, then add the valuation of p^a | No statement about extra ramified states, singular levels, or a global pi-squared factor on the surface |

The core dependency order is Sections 2–4 for geometric identity, Section 5 for the integral form,
then Section 6, followed independently by the odd and characteristic-two higher blocks.
Section 3 must use only the pure W0 portions of Bbad/Wreuse at its entry; it cannot invoke their
later transported strong critical or dynamics results as an earlier premise.
Section 4 uses smoothness as a hypothesis on the selected closed fiber, not an unproved classification
of all finite fibers. The abstract may summarize results proved later without reversing proof dependence.

## 4. Exact reuse and source exclusions

Each of the twenty author suppliers in the proof map has a current consumer:
P/Nbd/Gfield/Ucoh in Section 2; Bbad/Wreuse/Jspec in Section 3;
SH/Hloc and Ddiff Cartier in Section 4; Ddiff/Gint in Section 5;
DB/prime/TH/OC in Section 6; Matrix/TB/GFI in Section 7; P2/PI in Section 8.
Gint's same original model and restriction injectivity are also used wherever charts are glued.
The shared rank-two insertion, trace recurrence, chart-injectivity lemma and parameter conventions
are each proved once, with an explicit cross-reference at later consumers.

DB replaces only its approved first-layer universal-cohomology/splitting consumer; it retains
the actual constants and node frames. SH replaces only the geometric-integrality premise for
the selected already smooth complete closed fiber. Neither substitution removes the original
primitive pencil, actual generic Jacobian, pure W0 finite algebra, or complete closed Hasse calculation.
The old general splitting, all singular-fiber classification, strong critical Artin tables,
period/return-point/finite-field orbit counts and unused pairing guesses are not body obligations.
These are exclusions already fixed in the admitted consumer map, not deletions to meet a page target.

## 5. Scholarly source and drafting checks

Use actual primary-source metadata and theorem locators from the forthcoming
`notes/CITATION_RECORDS_20260909.md`; do not generate a bibliography from memory.
The records must distinguish the JR published identity from author-v2 conjecture numbering,
general Halphen/spectral/minimal-model tools from the calculations proved here, and standard
Hasse/formal-group/obstruction mechanisms from the actual original-object identification.
Any discovered erratum requires a bounded scope/consumer check before using the affected assertion.
No unsupported venue, citation quota, literature priority, author identity, or AI-reproducibility claim is added.

Draft as a single complete English proof paper. Section prose should explain each map before using it
and preserve genuine hypotheses; displayed equations should carry the calculation, not conceal missing steps.
The current outline makes no physical page estimate and no word-count quota. Natural length will be
measured only after the complete source is frozen under the publication lock.
The existing capacity votes remain forecasts with genuine risk above 30 pages.

Before that first build, perform a bounded non-author coverage review of the actual new outline/locks,
and a static complete-draft transcription/interface check when the manuscript exists.
These checks do not reopen unchanged formal candidate voting, change novelty scores, or grant PDF acceptance.
Any real missing proof is addressed before source freezing; if its repair changes the scientific contract,
record the issue and obtain the necessary decision rather than silently narrowing a theorem.

## 6. Remaining execution

1. Finish verified citations and bounded outline/lock consistency checking.
2. Draft all eight sections and assemble the exact common notation, statements, and bibliography.
3. Check the complete new source against the admitted proof consumers and record source-byte identity.
4. Run the first natural complete build, measure the actual body, and follow the fixed failure boundaries.
5. If the window passes, complete same-source second-root determinism, full actual PDF review,
   scoped repairs if needed, independent final integrity review, and local acceptance.

Nothing in this plan counts Paper30 as complete. The batch remains 3/5 until actual acceptance;
Paper31 and the final cross-paper audit remain downstream work.
