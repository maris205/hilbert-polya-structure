# Independent Paper-Plan and Figure-Asset Review

- Review date: 2026-08-16 UTC
- Review mode: fresh independent, read-only review of the frozen proof-only
  Paper-12 publication assets
- Reviewer relation: I authored none of the frozen plan, proof, handoff,
  bibliography, citation contract, figure source, media output, or asset
  record under review
- Canonical path base: `papers/12-henon-period3-residue`
- Candidate/lifecycle: `henon_period3_residue_proof_note_v1`
- Sole package write:
  `notes/INDEPENDENT_PLAN_FIGURE_REVIEW.md`
- Manuscript action: inspection for citation-key domain, forbidden language,
  and prospective figure-placement compatibility only; no compilation,
  integration, or edit was performed
- Report SHA-256: self-excluded from this file and reported after the final
  write

CANONICAL_MARKER=PAPER12_PLAN_FIGURE_R1__LOCK_2c7f056b7f9566f__HANDOFF_407cec5bf295c293__PLAN_e4876a50d172ccfb__TREE_77c7bdc856d6a8c__VERDICT_REPAIR_REQUIRED

## Canonical verdict

`REPAIR_REQUIRED`

One blocking defect prevents `ASSET_PASS`: the ten-key frozen manuscript
citation migration has the correct cardinality but the wrong exact domain.
The manuscript uses ten lowerCamel placeholders with descriptive suffixes,
while `paper/CITATION_KEY_CONTRACT.json` maps ten shorter, absent keys.
Consequently, the contract's promised bounded mechanical replacement cannot
resolve the frozen manuscript citations to the eleven-key PascalCase
bibliography.

All other required checks pass: bound hashes and closed proof-only inputs;
the plan's C1--C18 and PC1--PC2 claim scope; all mandatory nonclaims; the
formal period spectra and quartic constants; Figure 1's explicit
`S_m(a,1)` specialization; Figure 2's four supports, two proof eliminations,
two-term law, and open nonvanishing boundary; Figure 3's full Step-9 chain;
exact captions and labels; prospective placements; primary-source metadata
and bounded claim roles; forbidden-language controls; all nine media outputs;
mechanical publication properties; native-resolution color and grayscale
readability; deterministic regeneration; and manifest/trace/tree closure.

This verdict does not authorize citation migration, figure integration,
manuscript compilation, finalization, or submission.

## 1. Exact review bindings

Every supplied binding was recomputed before content review.

| Artifact | Required and recomputed SHA-256 | Result |
|---|---|---|
| `experiments/proof_only_manuscript_lock.json` | `2c7f056b7f9566f754a06c30417105c0b1cefb2d0081f4bca8bb3a00adbf8eeb` | PASS |
| `notes/INDEPENDENT_PROOF_ONLY_HANDOFF_REVIEW.md` | `407cec5bf295c29330c24ae461dca86ad1bf54d77f44d477d83a821bf7e41711` | PASS |
| `PAPER_PLAN.md` | `e4876a50d172ccfb857b3c6667a0be85d12105f4d7da63da393531a36cef9d31` | PASS |
| `notes/CITATION_VERIFICATION.md` | `eb99e7ab59e5d2947b6d5dab0d23dd471c05d090280f7915f010210b021e39ee` | PASS |
| `paper/CITATION_KEY_CONTRACT.json` | `e73c0c75310cdb60706bed900ac90308cd27320a9d9ce6d53b2fc7e73ce82f92` | PASS as a bound file; content blocker in Section 8 |
| `paper/references.bib` | `f1b6fe0807e33debf87c8be19e1b81b2a4a10f886fd9f4ae1d20bf264e978adc` | PASS |
| `paper/figures/DETERMINISM_AUDIT.json` | `c9442c6f75ca6bcc1bb8294faf75f2ff0a89866e6a9c6e8758fbeea54eb324b3` | PASS |
| `paper/figures/FIGURE_MANIFEST.json` | `f81921a54b704380d98710cda8aecd4d9e89b85ae8a99be6eee901b07419301b` | PASS |
| `paper/figures/FIGURE_TRACE.json` | `7ffb609fd2e7a1f4cd1598d750e754787d72b0efec03188b4789e3e95003185d` | PASS |
| `paper/figures/ASSET_TREE.json` | `77c7bdc856d6a8c284cd67d86cb201e43a4423eb6647b80b8bfd9b2932a6265e` | PASS |

The principal transitive proof-only authorities also remained at their
locked hashes:

| Authority | SHA-256 | Role |
|---|---|---|
| `experiments/source_lock.json` | `2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2` | frozen source binding |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `5630610bb637e155fa631eb2d9c4b36c6ea334ae976a6ef39a53dd733b8c62de` | atomic claim and nonclaim boundary |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` | `5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11` | independent `SOURCE_LOCK_PASS` |
| `notes/NOVELTY_ASSESSMENT.md` | `c497dc4e2c404fbbfc3c89450991964d1049f06288a051bc647a15005a66146a` | bounded novelty and size boundary |
| `notes/PROOF_ONLY_MANUSCRIPT_SCOPE.md` | `d0dc07976e9631e5d30ffe6d20f1e4d7d76aea4c04d1d42598e3b594d0fc23b9` | presentation, provenance, and nonclaim boundary |
| `notes/PROOF_PACKAGE.md` | `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9` | sole scientific theorem authority |
| `notes/REGISTERED_AUDIT_POSTMORTEM.md` | `6648a0c3642d24eac1e22f3cc7349a805209d3293b556d6d5d5cbd873d0f831b` | failure disclosure only, never theorem evidence |

## 2. Closed proof-only input boundary

The proof-only lock has a closed eight-file manuscript allowlist,
`allowlist_is_closed=true`, and
`transitive_input_expansion_allowed=false`. The figure contract contains
exactly those eight paths plus the proof-only lock itself and the independent
handoff, for ten bound figure inputs. Every path is an ordinary nonsymlink
file below the canonical base and matches its recorded digest.

The recursively forbidden roots are:

- `code/`;
- `preexecution/`;
- `results/`; and
- `runtime/`.

No figure generator reads any of these roots. The three standalone figure
scripts read only `figure_contract.json`; `generate_all.py` invokes only the
three standalone generators; and `build_records.py` reads the publication
layer needed for captions, citations, media QA, trace, manifest, and tree
records. The two independent regeneration trees described in Section 10
contained zero forbidden-root directories. No candidate module was imported
or executed, and no scientific coefficient was computed from candidate,
preexecution, result, staging, or runtime material.

## 3. Plan and exact claim-scope audit

The plan tells one theorem-first story, leads with PC1, uses PC2 as the
supporting mechanism, allocates the complete Step-9 derivation rather than an
opaque computation, and preserves the separation between Step-10 moment and
Step-13 multiplicity.

| ID | Required proof-only scope | Plan/asset disposition |
|---|---|---|
| C1 | characteristic-zero normalized monic-centered Jacobian-minus-one Hénon category | PASS |
| C2 | length-`2m` fixed scheme, `q^2=0`, formal spectrum `0^{x 2m}`, without claiming `q=0` | PASS |
| C3 | retain `2+q(x)q(y)` before diagonal subtraction; exact-period-two spectrum `2^{x((2m)^2-2m)}` | PASS |
| C4 | normalized conjugacy iff `a^{2m-1}=b^{2m-1}`, with both directions and centering scope | PASS |
| C5 | cyclic equations encode `Fix(f^3)` at `epsilon=1`; stated Jacobian/trace element | PASS |
| C6 | monic free cyclic quotient of rank `(2m)^3` | PASS |
| C7 | complete-intersection trace/residue specialization labeled prior method | PASS |
| C8 | exactly four weighted supports | PASS |
| C9 | separated-algebra removal of `a^{3(2m-1)}` | PASS |
| C10 | removal of `a^{2(2m-1)} epsilon^m` using all three nonfixed branches plus the exact diagonal branch | PASS |
| C11 | exact surviving two-term law | PASS |
| C12 | cyclic reversal and `C_m=0` for odd `m` | PASS |
| C13 | full symbolic finite certificate, including (9.14), transfer flow, and separate `j=0` | PASS |
| C14 | zero fixed moment from `q^2=0`, not a length shortcut | PASS |
| C15 | complete normalized quartic `0^4` fiber is `p=(x^2-L)^2` | PASS |
| C16 | pointwise quartic moment `-1296000-1572864L^3` from source-level derivations | PASS |
| C17 | local multiplicity first, then length `64-4=60`, then cyclewise moment `-432000-524288L^3` | PASS |
| C18 | minimality only on the complete normalized quartic `0^4` fiber | PASS |
| PC1 | scoped quartic aggregate, with exact moment, affine `L^3` coordinate, and first separator on that fiber | PASS |
| PC2 | all-symbolic-`m` two-term law and certificate; universal nonvanishing excluded | PASS |

The plan's Claims--Evidence Matrix is internally aligned: theorem claims map
to the bound proof, figures are navigation rather than evidence, the
registered failure is provenance only, and evidence gaps are explicitly
open rather than promoted.

## 4. Mandatory nonclaims and provenance

The plan, figure contract, trace, captions, generators, and inspected
manuscript preserve the required boundaries:

- universal `D_m != 0` remains open;
- PC2 does not imply period-three separation in every degree;
- the quartic theorem does not cover all quartic Hénon maps;
- no global `P(4)=3`, global conjugacy classification, or global
  multiplier-rigidity theorem is claimed;
- the quartic family and period-one/two blindness are credited to
  Cantat--Dujardin;
- global residues, quotient traces, formal/dynatomic cycles, and low-period
  Hénon algebra remain prior methods;
- bounded search is not a historical-priority proof;
- no unstable/saddle multiplier, arithmetic height/finiteness, prime/zero,
  transfer/Fredholm, or Euler-product conclusion is claimed; and
- no finite diagnostic, development check, or failed runtime supports an
  all-`m` theorem.

The three required provenance ideas are present: the proof and independent
source review are the only theorem authorities; the one registered audit
terminally failed with no rerun, raw result, or result pass; and the direct
family/method precedents are credited while novelty remains narrowly bounded.

## 5. Figure 1 semantic audit

Figure 1 passes the requested semantic repair and theorem-boundary checks.

- The period-three box explicitly states
  `S_m(a,1)=C_m+D_m a^{2m-1}`. It does not ambiguously present the
  two-parameter law as the epsilon-one theorem.
- The formal period-one box says `q^2=0` and that `q` may be nonzero.
- The exact-period-two box retains `2+q(x)q(y)` before subtraction.
- The quartic box states the complete normalized `0^4` fiber,
  `p=(x^2-L)^2`, normalized conjugacy through `L^3`, pointwise moment
  `-384(3375+4096L^3)`, exact length `60`, and first separation only on
  this fiber.
- The proof and two independent proof reviews feed the theorem layer.
- The consumed audit is a dashed, hatched provenance-only branch labeled
  terminal fail/no rerun/no raw result/no result pass, with an explicit
  `no theorem arrow` label and `finalization not authorized`.

## 6. Figure 2 semantic audit

Figure 2 passes all requested mathematical and scope checks.

- It displays the weight equation and says there are exactly four
  nonnegative parameter supports.
- It shows the two survivors
  `C_m epsilon^{3m}` and
  `D_m a^{2m-1} epsilon^{2m}`.
- It visibly crosses out `a^{2(2m-1)} epsilon^m` and attaches the three
  nonfixed valuations plus exact diagonal branch as the proof reason.
- It visibly crosses out `a^{3(2m-1)}` and attaches the separated-algebra
  `epsilon=0`, `q_i^2=0` argument.
- It states the two-term law, the odd-`m` parity consequence, and the exact
  quartic specialization in both integer forms.
- Its dashed, hatched `OPEN` box states that universal `D_m != 0` is open
  and that no all-degree separator is claimed.

## 7. Figure 3 and complete Step-9 audit

Figure 3 retains the mandatory seven-stage order and agrees with the full
source proof.

1. recurrence (R), state (9.1), bases (9.2), all four signed branches (9.3),
   and strict total-degree decrease;
2. Laurent form (9.4), reciprocal expansion (9.5), unique normal form,
   order independence, and no branch-interleaving double count;
3. assembly (9.6)--(9.9), admissible tuples (9.10)--(9.13), and preservation
   of signs and multiplicities;
4. the full local identity (9.14), explicitly labeled and paired with its
   coefficient-extraction proof;
5. integrality (9.17), sum rule (9.18), the unique distinguished coordinate
   (9.19), the incoming-transfer bijection (9.20), guarded factors, and the
   orientation sign (9.21)--(9.22);
6. a `j>=1` branch for (9.23)--(9.24) and a visually separate, hatched
   `j=0` branch with the two flow types (9.25) and exceptional vanishing
   (9.26); and
7. the finite `H/A/D` certificate, followed by an explicit `OPEN` box for
   universal nonvanishing and rejection of finite-diagnostic proof evidence.

The figure is a reader map, not a substitute for the manuscript proof.

## 8. Citation and primary-source audit

### 8.1 Bibliography and source roles

`paper/references.bib` contains exactly eleven distinct PascalCase keys, no
aliases, and matches its locked digest. Metadata and claim roles agree with
the locked primary-source ledger:

| Key/source | Locked role | Result |
|---|---|---|
| `CantatDujardin2026` | direct quartic family and period-one/two obstruction; preprint | PASS |
| `FriedlandMilnor1989` | normalized Hénon structure and conjugacy background | PASS |
| `CattaniDickensteinSturmfels1996` | global-residue and quotient-trace prior method | PASS |
| `CvitanovicHansenRolfVattay1998` | exact Hénon periodic-orbit sum-rule precedent, with a different observable | PASS |
| `DullinMeiss2000` | generalized-Hénon low-period background | PASS |
| `Huguin2024` | adjacent one-dimensional small-cycle multiplier moduli; preprint | PASS |
| `Hutz2010` | formal-period/dynatomic-cycle background | PASS |
| `Hutz2020` | adjacent projective multiplier invariants | PASS |
| `GuillotRamirez2019` | fixed-point multiplier/index relations in a different projective setting | PASS |
| `Ueda2004` | fixed-point background for polynomial automorphisms | PASS |
| `BianchiHe2026` | optional current thermodynamic context; preprint and not direct support | PASS |

No role is promoted to direct support for PC1 or PC2 beyond the locked
ledger. The bounded no-hit statement remains a bounded absence inference,
not priority proof.

### 8.2 Blocking exact-domain defect in the ten-key manuscript map

The contract correctly records eleven canonical PascalCase bibliography
keys, a ten-entry placeholder map, and optional unmapped
`BianchiHe2026`. Cardinality alone is insufficient. Exact enumeration of the
frozen manuscript gives the following mismatch:

| Actual manuscript placeholder | Contract-domain key | Intended PascalCase target | Result |
|---|---|---|---|
| `cantatDujardin2026MultiplierRigidity` | `cantatDujardin2026` | `CantatDujardin2026` | FAIL |
| `cattaniDickensteinSturmfels1996Residues` | `cattaniDickensteinSturmfels1996` | `CattaniDickensteinSturmfels1996` | FAIL |
| `cvitanovicHansenRolfVattay1998Beyond` | `cvitanovicHansenRolfVattay1998` | `CvitanovicHansenRolfVattay1998` | FAIL |
| `dullinMeiss2000GeneralizedHenon` | `dullinMeiss2000` | `DullinMeiss2000` | FAIL |
| `friedlandMilnor1989DynamicalProperties` | `friedlandMilnor1989` | `FriedlandMilnor1989` | FAIL |
| `guillotRamirez2019Multipliers` | `guillotRamirez2019` | `GuillotRamirez2019` | FAIL |
| `huguin2024ModuliMultipliers` | `huguin2024` | `Huguin2024` | FAIL |
| `hutz2010DynatomicCycles` | `hutz2010` | `Hutz2010` | FAIL |
| `hutz2020MultipliersInvariants` | `hutz2020` | `Hutz2020` | FAIL |
| `ueda2004FixedPoints` | `ueda2004` | `Ueda2004` | FAIL |

The two ten-element sets are disjoint. Every actual manuscript key is
missing from the map domain, and every existing map-domain key is absent from
the manuscript. This is a blocking integration defect, not a stylistic
advisory.

The current `build_records.py` validates the bibliography against the
contract and records `frozen_placeholder_map_count=10`, but it does not
extract the manuscript citation set or compare it with the map domain. The
manuscript is intentionally excluded from `ASSET_TREE.json`, so manifest and
tree closure cannot detect this defect.

## 9. Caption, label, and prospective-placement contract

The three exact captions in `PAPER_PLAN.md`, `figure_contract.json`,
`FIGURE_TRACE.json`, and `latex_includes.tex` are whitespace-normalized
identical. Labels are exactly:

| Figure | Stem | Label | Prospective location | Result |
|---|---|---|---|---|
| 1 | `fig1_theorem_architecture` | `fig:theorem-architecture` | after the Introduction contribution bullets, before detailed proof | PASS |
| 2 | `fig2_weighted_two_term_law` | `fig:weighted-two-term-law` | Section 4, after enumeration/reduction of the four weighted supports | PASS |
| 3 | `fig3_step9_certificate_pipeline` | `fig:step9-certificate-pipeline` | near the start of the coefficient-certificate section, before the full Step-9 derivation | PASS |

All three snippets use full-width vector PDFs and `[t]` placement. The
figures have not been inserted into `paper/manuscript.tex`, which is
consistent with the explicit prohibition on integration before independent
`ASSET_PASS`. Therefore this review audits the frozen prospective placement
contract, not compiled float placement.

## 10. Independent regeneration and record closure

I regenerated the assets in two fresh, isolated copied asset trees. Each
tree contained only the publication-layer figure sources and records plus
`PAPER_PLAN.md`, `notes/CITATION_VERIFICATION.md`,
`paper/CITATION_KEY_CONTRACT.json`, and `paper/references.bib`. Neither copy
contained a `code/`, `preexecution/`, `results/`, or `runtime/` directory.

All nine regenerated media outputs were byte-identical across run 1, run 2,
and the frozen package:

| Output | SHA-256 | Result |
|---|---|---|
| `fig1_theorem_architecture.pdf` | `1fbed2c5d27025763b68f660a87f695d4c7fe3a96e7786ef98b0bdccf0a53b79` | PASS |
| `fig1_theorem_architecture.png` | `469eb67789e64f8dadf2350c241828081fe0ae0f2b5a8dfbde838b31b7a78d25` | PASS |
| `fig1_theorem_architecture.svg` | `6d8f21b62b08cc019a992a37861e00d38577323117590d6909e12b30a5b5a43a` | PASS |
| `fig2_weighted_two_term_law.pdf` | `744853231c1c2700bb29f0ca4d8cf0d4059691966d91a0316c7674c526054835` | PASS |
| `fig2_weighted_two_term_law.png` | `cb04e39943746491ba61bb4de8b66a5047f1bc9ba15447f546004fdc8c09a7d1` | PASS |
| `fig2_weighted_two_term_law.svg` | `8b2c68d86f7aec84893c668fe354b432324f6413d390e6a6b85cd0d930c0dd11` | PASS |
| `fig3_step9_certificate_pipeline.pdf` | `e120cb0c8d05cf884862c3e0d23a8db7b45115e5691fda65620d9bcf203c5f6a` | PASS |
| `fig3_step9_certificate_pipeline.png` | `86914b64a13c6abcc4ebcbb2f80a78caf617d3ac5a6ab91e336134623621ca22` | PASS |
| `fig3_step9_certificate_pipeline.svg` | `03b6b1a5b94b1fb71b9b4dd7f1c6186c4cdf40309134743e67aa1e42381a9ca6` | PASS |

The independently rebuilt records were likewise byte-identical in both
copies and the frozen package:

| Record | SHA-256 | Result |
|---|---|---|
| `DETERMINISM_AUDIT.json` | `c9442c6f75ca6bcc1bb8294faf75f2ff0a89866e6a9c6e8758fbeea54eb324b3` | PASS |
| `FIGURE_TRACE.json` | `7ffb609fd2e7a1f4cd1598d750e754787d72b0efec03188b4789e3e95003185d` | PASS |
| `FIGURE_MANIFEST.json` | `f81921a54b704380d98710cda8aecd4d9e89b85ae8a99be6eee901b07419301b` | PASS |
| `ASSET_TREE.json` | `77c7bdc856d6a8c284cd67d86cb201e43a4423eb6647b80b8bfd9b2932a6265e` | PASS |

Strict duplicate-key-rejecting JSON parsing passed for the lock, citation
contract, figure contract, determinism record, manifest, trace, and asset
tree. `ASSET_TREE.json` lists exactly 27 nonsymlink ordinary files; every
listed byte count and digest matches, and its computed publication-layer
inventory has neither omissions nor extras. Manifest generator,
documentation, trace, determinism, media, bibliography, and citation-contract
hash links all close exactly.

## 11. Independent mechanical and visual QA

### 11.1 PDF, SVG, and PNG mechanics

| Figure | PDF | SVG | PNG | Result |
|---|---|---|---|---|
| Fig. 1 | one page, 518.4 x 363.6 pt, vector-only, 3 embedded fonts, no Type 3 | valid XML, 30 selectable text nodes, 25 paths, no image node | 2160 x 1515 RGBA, 299.9994 dpi | PASS |
| Fig. 2 | one page, 518.4 x 360 pt, vector-only, 3 embedded fonts, no Type 3 | valid XML, 28 selectable text nodes, 40 paths, no image node | 2160 x 1500 RGBA, 299.9994 dpi | PASS |
| Fig. 3 | one page, 518.4 x 399.6 pt, vector-only, 7 embedded fonts, no Type 3 | valid XML, 44 selectable text nodes, 32 paths, no image node | 2160 x 1665 RGBA, 299.9994 dpi | PASS |

All PDFs contain zero raster image objects. All SVGs contain selectable text
and zero raster-image nodes. PNG DPI falls within the declared 300-dpi
tolerance.

### 11.2 Native-resolution color and grayscale inspection

All three frozen PNGs were viewed at original resolution. Native-size
grayscale conversions were then generated in an automatically cleaned
temporary directory and viewed independently.

- No edge clipping, cut-off glyph, panel-marker collision, box/text overlap,
  or arrow/text overlap was found.
- The period spectra, epsilon-one specialization, quartic formulas, length
  `60`, four supports, two removals, identity (9.14), `j>=1`, separate `j=0`,
  and open-boundary wording remain readable.
- In grayscale, the source/review/audit and survive/remove/open distinctions
  remain recoverable through text, border style, cross-outs, dashes, and
  hatches rather than hue alone.
- No figure has an internal decorative title; A/B/C are panel markers.
- Line weights and minimum text remain readable for the intended full-width
  placement.

Visual QA result: PASS.

## 12. Forbidden registered and diagnostic language

No figure, caption, trace transformation, plan theorem claim, or inspected
manuscript theorem statement says or implies that Track Q, Track R, an
adjudicator, or the registered audit passed; that two runtime engines agreed;
that a registered coefficient matched; that any theorem is computationally,
experimentally, or empirically certified; that a raw result, result manifest,
or result-pass artifact exists; or that a retained traceback or rerun
confirmed the failure cause.

No numerical value of `D8`, `D9`, `E8`, `E9`, `D_8`, `D_9`, `E_8`, or
`E_9` appears in the publication assets or manuscript. The allowed failure
disclosure is expressly non-evidentiary, and `no scientific mismatch` is
paired with the statement that absence is not evidence of agreement.

Result: PASS.

## 13. Minimum repair and required refreeze

The minimum acceptable repair is:

1. replace the exact domain of
   `frozen_draft_placeholder_map` in
   `paper/CITATION_KEY_CONTRACT.json` with the ten actual manuscript keys
   enumerated in Section 8.2, mapped to the existing ten PascalCase targets;
2. keep the canonical eleven-key bibliography unchanged and do not add
   duplicate BibTeX aliases;
3. add or run a validation that extracts the manuscript citation-key set and
   requires exact equality with the placeholder-map domain, not merely equal
   counts;
4. rebuild `FIGURE_MANIFEST.json` and `ASSET_TREE.json` because the citation
   contract digest changes; rebuild the trace/record set through the normal
   record builder so all links are rechecked; and
5. obtain a fresh independent asset review over the new exact hashes before
   any citation migration, figure integration, compilation, finalization, or
   submission.

An alternative repair that renames all ten frozen manuscript placeholders to
the current shorter map domain would also require a new manuscript binding
and review. Updating the contract to the already present manuscript keys is
the smaller, clearer repair.

## 14. Gate disposition

Blocking findings: 1.

Unresolved advisories: 0.

Passing a cardinality-only ten-key check is insufficient because the
authorized migration function is undefined on every citation key actually
used by the manuscript. Until the exact-domain repair is frozen and reviewed,
the independent asset gate is not discharged.

**Final verdict: `REPAIR_REQUIRED`.**
