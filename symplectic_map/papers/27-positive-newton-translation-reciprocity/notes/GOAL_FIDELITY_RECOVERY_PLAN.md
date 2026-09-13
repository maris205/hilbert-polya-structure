# Paper 27 goal-fidelity successor recovery plan

author_disposition: AUTHOR_STOP_FOR_FRESH_INDEPENDENT_REVIEW
controlling_event: B07-E0230-GOAL-FIDELITY-SUCCESSOR-RECOVERY-AUTHORIZATION
candidate_id: positive_newton_translation_reciprocity_v5
project: papers/27-positive-newton-translation-reciprocity
recovery_kind: append-only successor lifecycle; never a retroactive retry or conversion of an old FAIL
bounded_plan_correction: 1/1, authorized by B07-E0232 after an immutable zero-write review FAIL
external_effect: none

## 1. Purpose and immutable history

The original Paper 27 theorem, proof package, source locks, manuscript, build
profiles, build evidence, failed build-revision review, and terminal R3 review
remain immutable.  They establish useful local mathematics and two technically
matching 17-page outputs, but they do not establish a release-grade paper:

- the locked target was 24--28 anonymous proof-content pages;
- the 17-page output places references on pages 15--17 and therefore contains
  at most 14 content pages;
- the build-revision review froze `Blocker=1`, `Major=1`, `Minor=1`;
- the source-revision allowance was exhausted; and
- lifecycle stages 11--14 never opened.

The user's explicit goal-fidelity authorization opens a new successor regime.
No old result is relabeled.  Every new theorem, source byte, lock, build,
receipt, review, local candidate copy, and terminal decision must be created
and consumed prospectively under a separate ledger gate.

## 2. Frozen recovery-opening inputs

The following exact regular mode-0644, link-one files are the inherited
scientific and governance inputs.  Build-tree files are deliberately absent
from this plan's read boundary.

| Path | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `PAPER_PLAN.md` | 18,412 | 249 | `61be9c2849d37ba6def1e3dc43a96fcd895d0d9b36500166ff08bfe164d79ca4` |
| `notes/BUILD_PROFILE.md` | 6,124 | 117 | `8fba2cbb84a02078094fbced92cf2b6286e86b6be4360bdbc0a893bd55b32c6e` |
| `notes/BUILD_PROFILE_REVISION.md` | 5,238 | 109 | `1c01ec583391c3f60996018debd85f860c4b9709f3913da49c7e6c686e032f63` |
| `notes/INDEPENDENT_BUILD_REVISION_REVIEW.md` | 11,434 | 181 | `549082029f4a1b0ed8b153d86fea858ef7e16173fae981db070a957080bd7781` |
| `notes/INDEPENDENT_TERMINAL_BLOCKER_REVIEW_R3.md` | 3,940 | 76 | `20a81ab28c51c1acef5e563ef1beafdb37ac7c1bc4328c804cb910ce2c1679b0` |
| `notes/PROOF_PACKAGE.md` | 19,921 | 527 | `c583d2cedcd97bef8410172bed967dfe99bcaf9caa69595c305bbf36ccd51fd1` |
| `notes/PUBLICATION_LOCK.md` | 7,996 | 148 | `7eb6ad779a00c4f56f4b5bea5fc56f22ebe55ee9b80af9924d18c70d4ff834aa` |
| `notes/SOURCE_LOCK.md` | 9,328 | 177 | `ab63ffebbc62149daa0db70f4378cd59604c4c24c201b70036e96f831b9560c6` |
| `notes/SOURCE_LOCK_REVISION.md` | 3,387 | 68 | `8afd2516173ab949a65bfab7e232c1040c10b897bcce9681e7418c04d0d93445` |
| `paper/main.tex` | 33,811 | 829 | `ba9879a7084821b18c3e76166706d90d99bc4cb8e0bb1cb09d04a23f3a007f18` |
| `paper/math_commands.tex` | 601 | 17 | `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` |
| `paper/references.bib` | 6,610 | 217 | `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` |

The recovery-opening status identity after E0230 is 843,435 bytes, 13,055 LF,
SHA-256
`8d4e38333605ceeb60f2e7bdfe5a9bfd5f0a03d1fefc1cfacd989b0abc05e4a3`.
The 77-row source-and-control aggregate remains
`d8c9b2dadcaeb72a92884e94f6353cd083af59036a1c8fe2dd3cc32975fb4596`.

## 3. Frozen theorem boundary

The successor retains the existing headline and may strengthen exposition and
proved boundary statements only inside this exact scope:

1. characteristic-zero polynomial Hamiltonian shears with `r >= 3` and
   finite collected positive supports;
2. actual strict-edge survival of the selected leading blocks;
3. the all-ones translation of the certified weight state;
4. at most `d_V+d_W-2` selector changes along an infinite certified branch;
5. a stationary affine tail with the global origin retained;
6. reflected inverse reciprocity for finite typed words, together with the
   exact theorem that every nonempty strict homogeneous positive cell has
   full observable spans and therefore admits only literal global reflected
   selector identities in the frozen framework; and
7. a local, one-edge, one-step lower-ideal robustness statement.

The successor may add exact equality criteria, definitions, quantitative
margins, typed transition lemmas, complete proofs, and strict boundary
examples that are logical consequences of the frozen proof spine.  It may not
claim a universal sharpness-realization theorem, a multi-edge perturbation
theorem, a global lower-ideal invariant, a broader support classification, a
characteristic-positive theorem, or a new candidate axis without returning to
a fresh novelty gate.

## 4. Required substantive modules

The manuscript needs about eleven genuine new body pages.  The target below
is 9.5--13 mathematical pages; a source edit is acceptable only if a fresh
reviewer confirms that the material is theorem/proof/example content rather
than padding.

### M1. Typed edge and cell formalism (1.5--2 pages)

Replace opaque predicates such as `PairGaps_e(u,w)>0` and prose references to
“all listed checks” by four finite displayed inequality families:

1. source selector and source carry;
2. target selector and target carry;
3. reflected selector and reflected carry; and
4. transformed-pair membership.

For every typed edge `e -> f`, define the positive cell `C_e^+`, the selected
labels `(alpha,beta)`, and the exact transition

`Phi_e(u,w) = (B_beta A_alpha u, A_alpha u)`.

Whenever target certification is used, state and prove the literal inclusion
`Phi_e(C_e^+) subset C_f^+`; do not infer it from a source-only margin.
Construct algebraically independent leading blocks that realize every
positive integer pair seed used in the fixture.  State explicitly which
conditions are hypotheses and which are derived.

### M2. Face-Hessian and leading-form survival (1.5--2 pages)

Split the compressed survival argument into separate formal lemmas:

1. grouped determinant and uniqueness of the secondary-lowest monomial;
2. characteristic-zero Jacobian algebraic independence;
3. injectivity of the selected substitution into the associated graded ring;
4. separation of fresh and old leading blocks; and
5. induction through forward and inverse half-steps.

Give three different failure mechanisms, not one blended warning:

- zero-coordinate Hessian failure;
- unit-coordinate selector/carry failure; and
- positive-characteristic derivative cancellation.

The successor must acknowledge that the Jacobian/Hessian ingredient itself is
classical and that the contribution is its typed use in the certified branch.

### M3. Envelope theorem and equality cases (1.5--2 pages)

For every total degree `s`, freeze a single within-total representative.  For
the W-side use

`N_s = - min_{|beta|=s} beta dot u_0`,

so the envelope is `max_s (s g + N_s)`.  Let `S_V` and `S_W` be the
actually available total classes, let `q_V=|S_V|` and `q_W=|S_W|`, and define
the strict activity interval of a class to be the set on which its affine
line is the unique upper-envelope maximizer.  A class that only touches at a
tie has an empty strict activity interval and is not counted as visited.

At the discrete branch samples `g_n`, define the ordered-pair change count by

`N_pair = #{n >= 0 : (s_V(n+1),s_W(n+1)) != (s_V(n),s_W(n))}`.

A simultaneous V- and W-component switch therefore counts once, not twice.
Prove:

1. active slopes are strictly ordered;
2. equal-total representatives cannot switch on a strict certified branch;
3. discrete sampling may skip a wall but cannot repeat a wall;
4. `N_pair <= (q_V-1)+(q_W-1) <= d_V+d_W-2` without generic-time
   assumptions; and
5. equality in the final `d_V+d_W-2` bound holds exactly when
   `q_V=d_V`, `q_W=d_W`, every class on each side owns a nonempty strict
   activity interval hit by at least one branch sample, and no update index
   contains simultaneous V- and W-component switches.

Write the closed stationary-tail solution with the global origin unchanged.
No claim of realizing every possible equality pattern is permitted.

### M4. Word-level reciprocity (1.5--2 pages)

Rewrite reciprocity at the level of a finite typed word.  For literal reflected
labels `R alpha, R beta`, distinguish the global algebraic matrix identities
from the substantive support-selection/certification statement.  Preserve
the observable-span notation, but prove rather than assume its size: if
`C_e^+` is a nonempty strict homogeneous cell containing an integer seed,
then scaling that seed and applying sufficiently small coordinate
perturbations gives every coordinate direction in `U_e`; hence
`U_e=R^r`.  Since

`det A_alpha = (-1)^r (1-|alpha|) != 0`,

also `V_e=A_alpha U_e=R^r`.  Consequently the restricted identities are
global identities.  Use the frozen label-to-matrix injectivity to show that
they force the literal reflected labels; no proper-span or nonliteral
example is claimed or permitted.

Prove phase-by-phase necessity and sufficiency by finite-word induction.  Add
one explicit full-span cell calculation and one `n=1` missing-reflection
mismatch.  The full-span conclusion is part of the theorem boundary, not a
promotion of restricted agreement by fiat.

### M5. Quantitative one-step lower-ideal robustness (1.5--2 pages)

Perturb only the normalized source pair state
`z=(u,w) in R^(2r)` while the supports, exponent rows, selected labels,
permitted lower/new row sets, and all four projection domains remain fixed.
Use the `l_infinity` norm.  Write every required source, target, reflected,
and transformed-pair certification inequality, after composing with the
relevant one-step linear map, in the form

`ell_j(z) = a_j dot z > 0`.

For the forward and reflected families separately define

`m_+ = min_j ell_j(z)`,  `L_+ = max_j ||a_j||_1`,

`m_- = min_j ell_j(z)`,  `L_- = max_j ||a_j||_1`,

where the coefficient rows `a_j` already include the exact projection and
transition matrices.  Freeze the explicit combined radius

`rho_e(z) = min{m_+,m_-} / (2 max{1,L_+,L_-})`.

Prove directly from `|a_j dot delta| <= ||a_j||_1 ||delta||_infinity` that
every admissible perturbation `||delta||_infinity < rho_e(z)` retains at
least half of every listed margin.  Prove forward and reflected clauses
separately and give an explicit fixture counterexample obtained by deleting
one indispensable inequality.

The conclusion must remain one edge and one step.  No target-core inclusion,
support or exponent-row perturbation, multi-edge invariant, or global
perturbation result is allowed.

### M6. Complete fixture and boundary dossier (2--3 pages)

Print six full integer pair seeds `(u,w)`, not six isolated `u` vectors.  For
each seed give score, source-carry, target-carry, reflected-score, and
reflected-carry tables.  Verify the typed path `C_1 -> C_2 -> C_2` literally.
Record the two seed determinants `1` and `-1` separately from
`det A_1=11` and `det A_2=12`.

Expand the cancellation computation and include strict examples for:

- characteristic-positive failure;
- a selector tie;
- a failed carry;
- the strict-cell full-observable-span calculation;
- missing reflection; and
- an omitted lower-ideal margin.

Treat `r=2` only as an excluded predecessor/portfolio boundary unless an
actual failure theorem is independently proved.

## 5. Page-mass and typesetting acceptance

The successor source must insert a forced page boundary immediately before
the bibliography and emit an exact log sentinel
`BATCH07_REFERENCE_START_PAGE=<integer>`.  The measured anonymous proof-content
count is the first bibliography page minus one.  Acceptance requires:

- proof-content pages in `[24,28]`;
- all six substantive modules present and reviewed;
- references excluded from the count;
- no governance text, file paths, hashes, discovery logs, or review narrative
  in the manuscript;
- no font shrinking, spacing manipulation, oversized tables, gratuitous
  display breaks, or bibliography inflation; and
- zero overfull boxes, including removal of the former 471-point overflow.

Underfull warnings must either be removed or individually dispositioned as
typographically harmless by the fresh source and build reviewers.  Warning
repairs never count as mathematical page mass.

## 6. Planned successor source-and-control artifacts

Every path below is prospective and confers no write authority until a later
ledger event names it exactly.  No absence test is permitted before that
event.

1. `notes/PROOF_PACKAGE_SUCCESSOR.md`
2. `notes/CLAIMS_EVIDENCE_MATRIX_SUCCESSOR.md`
3. `PAPER_PLAN_SUCCESSOR.md`
4. `notes/SOURCE_LOCK_SUCCESSOR.md`
5. `notes/PUBLICATION_SCOPE_SUCCESSOR.md`
6. `notes/PUBLICATION_LOCK_SUCCESSOR.md`
7. `notes/BUILD_PROFILE_SUCCESSOR.md`
8. distinct independent review artifacts for the proof package, source lock,
   paper plan, publication scope, publication lock, source, build profile,
   build R1, build R2, finalization, and terminal integrity.

The successor manuscript may modify only `paper/main.tex` unless a separately
reviewed proof or citation need justifies an exact additional modification to
`math_commands.tex` or `references.bib`.  Existing source bytes remain the
parent of the successor lock and may never be overwritten without an event
that binds their preimage.

## 7. Serial successor lifecycle

### Stage S1: proof and scope recovery

1. create this plan and obtain a wholly fresh all-zero plan review;
2. create the successor proof package, claim matrix, and paper plan;
3. independently rederive every new lemma, equality criterion, full-span
   reciprocity reduction, margin radius, and fixture value;
4. repeat bounded primary-source positioning only if a claim grows beyond the
   existing publication scope; and
5. consume a fresh all-zero proof/scope review.

### Stage S2: locks and manuscript

1. create and review `SOURCE_LOCK_SUCCESSOR.md`;
2. create and review successor publication scope and publication lock;
3. edit only the exact source paths authorized by those locks;
4. perform a fresh static source review, including citation closure, all
   theorem/anti-claim mappings, page-mass plausibility, and the reference-page
   sentinel; and
5. allow at most one bounded successor source correction, followed by a new
   reviewer.

### Stage S3: deterministic build (recovery lifecycle stages 9--10)

1. create a successor build profile with exact binaries, dependencies,
   environment, commands, output universe, validators, stage order, and two
   fresh roots;
2. obtain an all-zero independent profile review before touching a root;
3. build root 0 completely and seal it before root 1 is checked or created;
4. build root 1 from the live source trio rather than copying root 0;
5. compare source copies, PDFs, logs, bibliography outputs, dependency
   receipts, page sentinel, page count, and normalized root-dependent fields;
6. require byte-identical PDFs and zero undispositioned warnings; and
7. consume fresh all-zero build R1 and build R2 reviews.  An R3 review of an
   old blocker cannot substitute.

### Stage S4: finalization and local release evidence (stages 11--12)

1. create a finalization-scope author stop and immutable finalization lock;
2. validate the complete lifecycle DAG and roles;
3. obtain a fresh independent finalization PASS;
4. create one exclusive raw-byte local candidate copy;
5. bind it with a release manifest and receipt; and
6. keep the effect strictly `LOCAL_ANONYMOUS_RELEASE_ONLY`.

No upload, submission, host, repository push, message, or identity disclosure
is part of “release” here.

### Stage S5: terminal rebuild and integrity (stages 13--14)

1. perform two further fresh terminal rebuilds in separately authorized roots;
2. compare their source/PDF/receipt evidence with the finalized candidate;
3. obtain one sole terminal-integrity review from a role distinct from every
   source, build, finalization, release, and earlier terminal-blocker role;
4. consume an all-zero terminal-integrity PASS; and
5. perform cleanup only after a separately authorized exact cleanup plan and
   cleanup review.

Only this sequence may replace Paper27's active recovery gate with a fresh
release-grade terminal PASS.  Historical terminal states remain visible.

## 8. Review census and correction budgets

Every independent review uses the conjunctive rule

`Blocker=0; Major=0; Minor=0; Ambiguity=0`.

Any finding requires `FAIL_WRITE_NOTHING` unless the review artifact itself is
the authorized output recording a negative gate.  No reviewer may reuse an
earlier Paper27 or Batch07 role.  No author score substitutes for a review.

The successor regime permits at most one bounded correction at each of these
major stages: proof/scope package, source package, build profile, and final
integrity metadata.  A correction may not change the candidate axis, enlarge
the frozen theorem boundary, add padding, or erase a failure.  An intrinsic
novelty, proof, deterministic-build, or page-mass failure returns to the user
authority gate rather than spawning an implicit retry.

## 9. Completion conditions

Paper27 successor recovery is complete only when all of the following are
simultaneously proved by current artifacts:

- the six modules pass a fresh mathematical review;
- successor source and publication locks pass;
- static source review passes;
- measured proof-content pages lie in `[24,28]`;
- two ordinary build roots pass deterministic comparison;
- finalization scope, lock, and lifecycle DAG pass;
- the exclusive local candidate copy and release manifest agree;
- two terminal rebuilds agree with the finalized candidate;
- the sole terminal-integrity census is all zero;
- cleanup, if any, is independently authorized and verified;
- external effect remains none; and
- the final effect is local anonymous evidence only.

This author plan creates no theorem, source, lock, build, PDF, release,
terminal PASS, or downstream Paper28 authority.  A wholly fresh reviewer must
now decide whether the plan is complete, non-padding, serial, exact-path
compatible, and faithful to the user's five-paper objective.

BATCH07_P27_GOAL_FIDELITY_RECOVERY_PLAN_AUTHOR_STOP
