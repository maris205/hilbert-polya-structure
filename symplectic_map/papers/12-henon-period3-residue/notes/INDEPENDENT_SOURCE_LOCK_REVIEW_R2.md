# Independent Source-Lock Review — R2

- Candidate: `henon_period3_residue_v1`
- Review date: 2026-08-16 UTC
- Reviewer relation: fresh independent R2 reviewer; I did not author any
  bound source file or the preserved R1 review
- Canonical path base: `papers/12-henon-period3-residue`
- Bound lock: `experiments/source_lock.json`
- Required and recomputed v2 lock SHA-256:
  `2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2`
- Preserved R1 review SHA-256:
  `e514ec05235be640dc4a8d02df3147d8018df40b445e92a4c6d1d0ffed0aff1f`
- Sole R2 write: `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md`

## Canonical verdict

`SOURCE_LOCK_PASS`

All mechanical, R1-repair, mathematical-regression, protocol-isolation,
source-role, novelty, and scope checks required by the v2 lock pass. No
blocking or advisory defect remains in the frozen v2 source package.

This verdict discharges only the source-lock review gate. It is not a
`DEPLOYMENT_PASS`, registered result, figure authorization, manuscript
authorization, or proof of universal nonvanishing. The registered exact audit
remains prohibited until the separately frozen implementation and deployment
gates pass.

## 1. Mechanical lock and inventory audit

Strict JSON parsing with duplicate-key rejection passed. The lock has no
self-hash, excludes itself from the bound-document count, declares exactly 14
source-design bindings plus one preserved R1 review, and resolves every bound
path relative to the explicit canonical path base above. All 15 paths are
distinct.

| Binding | Recomputed SHA-256 | Result |
|---|---|---|
| `notes/RESEARCH_QUESTION.md` | `6feb5c525caecf81fd6e9de98116b9ff0ffc143749e0a586d0dbc131a10e75d8` | PASS |
| `notes/NOVELTY_ASSESSMENT.md` | `c497dc4e2c404fbbfc3c89450991964d1049f06288a051bc647a15005a66146a` | PASS |
| `notes/PROOF_PACKAGE.md` | `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9` | PASS |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `5630610bb637e155fa631eb2d9c4b36c6ea334ae976a6ef39a53dd733b8c62de` | PASS |
| `notes/CITATION_VERIFICATION.md` | `eb99e7ab59e5d2947b6d5dab0d23dd471c05d090280f7915f010210b021e39ee` | PASS |
| `experiments/EXPERIMENT_PLAN.md` | `5f93cd0b156f096abab7f366d2bbc209677fb913b0fdfcea14895a1ab3d1eec6` | PASS |
| `experiments/EXPERIMENT_TRACKER.md` | `531d42a7c00847115accb6a54f5c147e3cb0eed2da64c19bc21a0038da001c39` | PASS |
| `refine-logs/FINAL_PROPOSAL.md` | `ff20ef84c3a55900881a5ad4d380ccf840da7b1fd9794c4d26d23e5b78df315f` | PASS |
| `refine-logs/REFINEMENT_REPORT.md` | `0a2d3020c9715bdba6c855dcc1156f49029ff959ed853636572106fea7c014ac` | PASS |
| `refine-logs/REVIEW_SUMMARY.md` | `5a6e67c0bba046ae8540c585cf2ffa116a471ca0b1a66e5ae4b5977b3e26ec6c` | PASS |
| `refine-logs/INITIAL_PROPOSAL.md` | `46984d6028e52842602f5a1d5a4f41b13aa9a840528c21328af3f4eb5ea5c8d6` | PASS |
| `refine-logs/round-1-review.md` | `757279f1b7274f20f619db78f4ae38214927d8ce04161c63d5da89b919ae86ba` | PASS |
| `refine-logs/round-2-review.md` | `7a35bd1feb2283e6934032a489c648e116e712ccbb14d5377c5d9575a7620277` | PASS |
| `refine-logs/score-history.md` | `edd13b5ce88132f6ec08f571885ecb6b6501b2eafacb57c9d4f9df561dd04b28` | PASS |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `e514ec05235be640dc4a8d02df3147d8018df40b445e92a4c6d1d0ffed0aff1f` | PASS |

Before this permitted R2 report was added, the Paper-12 tree contained exactly
the 14 design documents, the self-excluded lock, and the preserved R1 review.
It contained no candidate code, registered run, scientific result, figure, or
manuscript artifact. No degree diagnostic or scientific calculation was run
during this review.

## 2. Disposition of all four R1 blockers

| R1 blocker | V2 evidence | Result |
|---|---|---|
| Incorrect rationale for $T_{\mathrm{reg}}=(8,9)$ | The normative plan now states the exact arithmetic: one even and one odd index, the same value $\lfloor m/2\rfloor=4$, and adjacent values $\lceil m/2\rceil=4,5$. The lock repeats the corrected guarded-range role and explicitly records the v1 disposition. The inaccurate sentence remains only in immutable historical review material. | PASS |
| Aggregate/atomic claim-ID collision | The paper-level claims are uniformly `PC1` and `PC2`. The plan explicitly maps `PC1` principally to atomic C1--C7 and C14--C18, with C8--C13 as the independent uniform cross-check, and maps `PC2` to C1--C14. The tracker and lock use the `PC` namespace; the matrix alone owns atomic C1--C18. Their union covers all atomic claims without reusing `C1` or `C2` as aggregate IDs. | PASS |
| Research-decision enum drift | The only current normative enum is `GO_BORDERLINE_STANDALONE_SPECIALIST_NOTE`, identically recorded in the lock, novelty assessment, and claims matrix. The obsolete alternative occurs only inside the immutable R1 description of the defect. | PASS |
| Stale lifecycle wording | Every current normative stage statement says that source-lock v2 is frozen after the bounded R1 repair and that fresh v2 review is pending. It also says no code, result, figure, or manuscript is yet authorized. The lock has `source_design_frozen=true`, all downstream authorization flags false, and `SOURCE_LOCK_PASS` as the required next verdict. | PASS |

## 3. Advisory consistency checks

- No adjacent duplicate-word defect was found in the Paper-12 Markdown
  package.
- No Unicode replacement character or common mojibake sequence was found.
- Current theorem, scope, decision, and reporting statements use the precise
  phrase “formal fixed-point trace multiset $0^4$.” Residual
  “fixed-trace-zero” shorthand is confined to immutable historical records,
  one literature-search query, and section labels in the unchanged proof,
  where the formal multiplication-spectrum meaning is immediately defined;
  it does not create a broader claim.
- The lock explicitly declares
  `canonical_path_base = papers/12-henon-period3-residue`, and every bound path
  is relative to that base.

All four advisory checks pass.

## 4. Mathematical regression audit

The 1,639-line proof package is byte-identical to the proof that passed R1:

`36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`.

The R2 regression therefore focused on the four fragile claims and their
current plan bindings.

### C10 — local degeneration closure

PASS. Step 7 separately treats all-distinct, exactly-two-equal, and all-equal
root triples, giving lower valuations $3/2$, $7/4$, and $3$ for
$t_\varepsilon$. Their $m$-th powers have order strictly greater than
$m$. Step 10 handles the exact diagonal branch rather than hiding it in the
valuation argument: on the fixed algebra,
$t_\varepsilon=q^3+3\varepsilon^2q$, $q^2=0$, and hence
$t_\varepsilon^m=0$ for every $m\ge2$. This closes the exclusion of the
$a^{2(2m-1)}\varepsilon^m$ term.

### C13 and P7 — exact coefficient certificate

PASS. Step 9 still contains the complete terminating four-branch recurrence
and base cases, the order-independent Laurent interpretation, the finite
admissible-tuple sum, and the signed local fiber identity

\[
\sum_{\ell+A+2B=\alpha}(-1)^{\ell+B}2^A\binom N\ell
\frac{(n+A+B)!}{n!A!B!}
=(-1)^\alpha\binom{N-2n-2}{\alpha}.
\]

Coefficient extraction from
$(1-z)^N(1-2z+z^2)^{-n-1}$ proves this identity with the required
generalized-binomial convention. The congruence then forces the unique
distinguished coordinate for $j\ge1$; the incoming-transfer equations give
the $(k,u,v)$ bijection, guarded ranges, sign $(-1)^{r+k}$, and exact local
factors. The separate $j=0$ analysis retains both incoming patterns and
kills the exceptional $(0,0,2m)$-type contribution. The resulting
$H/A/D/E$ formulas and P7 wording are unchanged and complete.

### C16 — independent quartic slope and constant

PASS. Step 12 does not rely only on the general-$m$ collapse. Its independent
tensor-Laurent calculation gives

\[
\mathcal C_{2,0}=-6,\qquad
\mathcal C_{2,1}=\mathcal C_{2,2}=0,
\qquad D_2=4^9(-6)=-1572864.
\]

The separate exact normal-form ledger then gives $C_2=-1296000$, hence
$S_2^{(3)}(L)=-1296000-1572864L^3$. The $m=2$ specialization of the
all-degree formula remains only a cross-check.

### C17 and P8 — moment versus multiplicity

PASS. P8 continues to split the obligations explicitly. Step 10 proves zero
fixed **moment**. Step 13 independently proves the fixed **local
multiplicity**: the transverse $(u,v)$-Jacobian is invertible and formal
elimination leaves
$3p(\alpha+\delta)+O(\delta^{2r-1})$, of exact order $r$. Thus the
fixed-scheme length is subtracted without reducing the scheme, giving
$64-4=60$; only afterward is the pointwise moment divided by three for the
cyclewise display.

No theorem-level regression was found. The proof status remains
`PROVABLE AS STATED` under its explicit formal multiplication-spectrum and
normalized-conjugacy interpretations.

## 5. Exact-audit protocol and nonclaim regression

- **Q/R separation — PASS.** Track Q is frozen to the pre-collapse recurrence
  and Laurent/admissible-tuple routes (9.9) and (9.13), assembled through
  (9.8). Track R is frozen to the collapsed guarded formulas (9.27)--(9.28).
  The plan forbids either route from resolving the other's scientific
  objects and forbids shared arithmetic, generalized-binomial, $H/A$,
  reduction, tuple, or scientific-intermediate code.
- **Input and adjudication isolation — PASS.** Engines may share only a
  definitions-only schema and types-only envelope. Neither may read source
  documents or the private acceptance ledger, and no expected
  $D_8,D_9,E_8,E_9$ value is stored.
- **Registered tuple — PASS.** The sole tuple is $(8,9)$, used only as two
  isolated implementation-falsification indices. No neighbor expansion,
  range scan, high-degree quotient/residue run, trend inference, parity
  proof, or nonvanishing inference is permitted.
- **Development disclosure — PASS.** The incidental pre-lock recurrence
  recheck at $m=2,\ldots,7$ is consistently disclosed as unregistered,
  non-evidentiary, value-free, and outside the tracker. Both future engines
  must retain `historical_m2_m7_result_access_count = 0`.
- **Nonclaims — PASS.** Universal $D_m\ne0$, all-$m$ period-three
  separation, all-quartic separation, global $P(4)=3$, discovery of the
  exceptional family or low-period blindness, novelty of residue/dynatomic
  machinery, and historical priority from a bounded no-hit search remain
  explicitly excluded.

These are design-contract findings only; no implementation exists to review
at this gate.

## 6. Primary-source and novelty continuity

The citation-verification file is byte-identical to the R1-passed file:

`eb99e7ab59e5d2947b6d5dab0d23dd471c05d090280f7915f010210b021e39ee`.

The novelty assessment is likewise byte-identical:

`c497dc4e2c404fbbfc3c89450991964d1049f06288a051bc647a15005a66146a`.

Therefore there is no citation, source-role, search-bound, or novelty wording
drift to invalidate R1's primary-source audit. Its PASS is carried forward
without expanding the search: Cantat--Dujardin owns the direct exceptional
family and period-one/two blindness; Friedland--Milnor supplies normalized
Hénon structure; Cattani--Dickenstein--Sturmfels supplies mature global
residue machinery; the remaining sources retain only their bounded adjacent
or background roles.

The 2026-08-16 bounded no-hit statement remains explicitly non-priority and
non-universal. The frozen post-proof novelty score `6.2/10`, standalone-size
score `5.8/10`, and decision
`GO_BORDERLINE_STANDALONE_SPECIALIST_NOTE` remain above the required threshold
only for a transparent specialist note. If the coefficient proof were made
opaque, the recorded `4.8/10` stop boundary would still apply.

## 7. Final gate decision

There are zero blocking findings and zero unresolved advisories. All required
v2 bindings, all four R1 repairs, the unchanged proof's fragile dependencies,
the P7/P8 contracts, Q/R isolation, source roles, novelty bounds, and
mandatory nonclaims pass.

**Final verdict: `SOURCE_LOCK_PASS`.**
