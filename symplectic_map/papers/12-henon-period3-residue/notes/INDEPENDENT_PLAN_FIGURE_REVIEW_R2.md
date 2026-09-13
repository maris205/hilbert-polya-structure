# Independent Paper-Plan and Figure-Asset Review, Round 2

- Review date: 2026-08-16 UTC
- Review mode: fresh independent Round-2 review of the bounded proof-only
  Paper-12 asset repair
- Reviewer relation: I authored none of the repair, frozen plan, proof,
  handoff, manuscript, bibliography, citation contract, figure sources,
  media, or publication records under review
- Canonical path base: `papers/12-henon-period3-residue`
- Candidate/lifecycle: `henon_period3_residue_proof_note_v1`
- Immutable predecessor review:
  `notes/INDEPENDENT_PLAN_FIGURE_REVIEW.md`
- Sole package write:
  `notes/INDEPENDENT_PLAN_FIGURE_REVIEW_R2.md`
- Manuscript action: read-only citation-domain and targeted scope inspection;
  no edit, citation migration, figure integration, compilation,
  finalization, or submission was performed
- Report SHA-256: self-excluded from this file and reported after the final
  write

CANONICAL_MARKER=PAPER12_PLAN_FIGURE_R2__R1_d6bc5c624d371752__LOCK_2c7f056b7f9566f7__CONTRACT_997ca84ee7d868f3__TREE_a5006ef63be3bcc5__VERDICT_ASSET_PASS

## Canonical verdict

`ASSET_PASS`

The sole Round-1 blocker is closed exactly. An independent citation parser
enumerated every uncommented manuscript `\cite...{}` command, split
comma-separated calls, and found ten unique lowerCamel citation keys. That
set equals the exact domain of `frozen_draft_placeholder_map`:
`missing=[]` and `extra=[]`. The ten targets are unique and equal exactly to
the eleven canonical bibliography keys minus optional `BianchiHe2026`.

The repair is bounded and nonregressive. The immutable R1 report, proof
lock, proof-only handoff, plan, manuscript, bibliography, trace,
determinism audit, figure sources linked by the trace, and all nine media
outputs retain their required hashes. The changed content is confined to
the citation contract, fail-closed citation validator, R1-repair
documentation, derived manifest, and derived tree. The rebuilt trace is
byte-identical to R1. Two fresh publication-only asset copies independently
regenerated and rebuilt the package byte-for-byte, with no forbidden root in
either copy.

All prior science, nonclaim, provenance, caption/label, placement,
mechanical, visual, and forbidden-language gates remain satisfied under
targeted regression. This `ASSET_PASS` discharges only the independent
plan/figure asset gate. It does not itself perform or authorize manuscript
editing, citation migration, figure integration, compilation,
finalization, submission, or any use of the failed registered audit as
scientific evidence.

## 1. Exact bindings

Every supplied Round-2 binding was recomputed before review.

| Artifact | Required and recomputed SHA-256 | Result |
|---|---|---|
| `notes/INDEPENDENT_PLAN_FIGURE_REVIEW.md` | `d6bc5c624d371752f06ff1d8a8ae27367a7b4c2370b4ab2f19b52cbe24d95ed6` | PASS; immutable R1 history |
| `experiments/proof_only_manuscript_lock.json` | `2c7f056b7f9566f754a06c30417105c0b1cefb2d0081f4bca8bb3a00adbf8eeb` | PASS |
| `notes/INDEPENDENT_PROOF_ONLY_HANDOFF_REVIEW.md` | `407cec5bf295c29330c24ae461dca86ad1bf54d77f44d477d83a821bf7e41711` | PASS |
| `PAPER_PLAN.md` | `e4876a50d172ccfb857b3c6667a0be85d12105f4d7da63da393531a36cef9d31` | PASS |
| `paper/manuscript.tex` | `f3c535739046e61378ec8896b70e6d30652a7654213894e1556d221e511d3022` | PASS |
| `paper/references.bib` | `f1b6fe0807e33debf87c8be19e1b81b2a4a10f886fd9f4ae1d20bf264e978adc` | PASS |
| `paper/CITATION_KEY_CONTRACT.json` | `997ca84ee7d868f34cacc783993f10d1b82b86c71fbdc1c9b80f38bcf5199bfd` | PASS |
| `paper/figures/build_records.py` | `53128eb51cfc9ff8d2454fba2ac3f85423e098f501a55d0cba12b3f41e826431` | PASS |
| `paper/figures/PROVENANCE.md` | `989f284f5b27ed0a4cf3b1c0c8dafd3ac6cf8a48406b3712a92d4cf556aa36c9` | PASS |
| `paper/figures/FIGURE_QA.md` | `b3abfcde6aba53576d8474ef3f763c829e1e5c41206855d8b16cfec4eb6af16e` | PASS |
| `paper/figures/FIGURE_MANIFEST.json` | `3adc970996ea7a6e1dc043a554c88b8007f4fe203aa30a522b0a4663dcb31096` | PASS |
| `paper/figures/FIGURE_TRACE.json` | `7ffb609fd2e7a1f4cd1598d750e754787d72b0efec03188b4789e3e95003185d` | PASS; unchanged from R1 |
| `paper/figures/DETERMINISM_AUDIT.json` | `c9442c6f75ca6bcc1bb8294faf75f2ff0a89866e6a9c6e8758fbeea54eb324b3` | PASS; unchanged from R1 |
| `paper/figures/ASSET_TREE.json` | `a5006ef63be3bcc585567276f05f063fd6786c6170081e0eea8ec0ca128598ee` | PASS |

The transitive proof-only authorities in the lock also retain all eight
recorded hashes. The lock remains a closed eight-file allowlist with
`allowlist_is_closed=true`,
`transitive_input_expansion_allowed=false`,
`registered_evidence_used=false`, and
`finalization_authorized=false`.

## 2. Exact Round-1 blocker closure

### 2.1 Independent manuscript enumeration

The independent parser did not reuse `build_records.py`. It removed
unescaped LaTeX comments, located every `\cite...` command, consumed up to
two optional arguments with balanced delimiters, consumed the required
balanced brace group, split that group on commas, trimmed whitespace, and
failed on an empty or structurally unparsed call.

It found ten citation calls. Two calls contain two comma-separated keys:

- `hutz2010DynatomicCycles,hutz2020MultipliersInvariants`; and
- `guillotRamirez2019Multipliers,ueda2004FixedPoints`.

The exact unique manuscript set and repaired map domain are both:

```text
cantatDujardin2026MultiplierRigidity
cattaniDickensteinSturmfels1996Residues
cvitanovicHansenRolfVattay1998Beyond
dullinMeiss2000GeneralizedHenon
friedlandMilnor1989DynamicalProperties
guillotRamirez2019Multipliers
huguin2024ModuliMultipliers
hutz2010DynatomicCycles
hutz2020MultipliersInvariants
ueda2004FixedPoints
```

Exact set result:

```text
missing=[]
extra=[]
```

This is set equality, not a cardinality proxy.

### 2.2 Target and bibliography closure

The bibliography contains exactly eleven distinct keys and no duplicate
aliases. The ten placeholder-map targets are distinct and equal exactly to:

```text
canonical Bib keys - {BianchiHe2026}
```

Thus every manuscript placeholder has one canonical target, every mandatory
canonical target has one placeholder, and optional `BianchiHe2026` is the
only canonical key without a frozen-draft placeholder. The canonical
bibliography and its primary-source role ledger are unchanged, so no source
role, publication status, metadata, or novelty boundary moved in this
repair.

### 2.3 Positive and negative validator regression

The normal record build accepts the frozen manuscript and records the exact
manuscript set, map domain, and empty differences. Three destructive-test
copies were then mutated outside the package:

1. adding `unmappedRegressionKey` to a comma-separated manuscript citation
   failed with
   `missing_from_map=['unmappedRegressionKey'], extra_in_map=[]`; and
2. replacing one correct map-domain key with
   `staleEqualCountRegressionKey` while keeping the map cardinality at ten
   failed with the displaced manuscript key in `missing_from_map` and the
   stale key in `extra_in_map`; and
3. making a citation command structurally unparseable failed with
   `unparsed manuscript citation command; citation-domain validation fails closed`.

All three negative tests returned nonzero. The repaired validator therefore
closes the R1 defect and fails closed rather than silently accepting an
equal-count, stale-domain, or unparsed-citation condition.

## 3. Bounded-change and immutable-history regression

R1 remains byte-identical at its supplied digest and retains its canonical
`REPAIR_REQUIRED` marker. Its old contract, manifest, and tree bindings are
preserved in that immutable report:

| Record | R1 SHA-256 | R2 SHA-256 | Disposition |
|---|---|---|---|
| `CITATION_KEY_CONTRACT.json` | `e73c0c75310cdb60706bed900ac90308cd27320a9d9ce6d53b2fc7e73ce82f92` | `997ca84ee7d868f34cacc783993f10d1b82b86c71fbdc1c9b80f38bcf5199bfd` | intended map-domain repair |
| `FIGURE_MANIFEST.json` | `f81921a54b704380d98710cda8aecd4d9e89b85ae8a99be6eee901b07419301b` | `3adc970996ea7a6e1dc043a554c88b8007f4fe203aa30a522b0a4663dcb31096` | derived link/citation record rebuild |
| `ASSET_TREE.json` | `77c7bdc856d6a8c284cd67d86cb201e43a4423eb6647b80b8bfd9b2932a6265e` | `a5006ef63be3bcc585567276f05f063fd6786c6170081e0eea8ec0ca128598ee` | derived inventory rebuild |

The exact repair/rebuild write allowlist after the R1 report is:

```text
paper/CITATION_KEY_CONTRACT.json
paper/figures/build_records.py
paper/figures/FIGURE_QA.md
paper/figures/PROVENANCE.md
paper/figures/FIGURE_TRACE.json
paper/figures/FIGURE_MANIFEST.json
paper/figures/ASSET_TREE.json
```

`FIGURE_TRACE.json` was re-emitted but remains byte-identical at the R1
hash. Consequently the content-delta set is the other six paths. The
contract changes only the ten map-domain keys; targets and all other
contract semantics are unchanged. The validator adds independent
manuscript-domain extraction and exact-set/target checks. QA and provenance
bind the unchanged R1 report and explain the bounded repair. Manifest and
tree are the required derived records.

All user-designated immutable scientific and integration-sensitive files
retain their R1/supplied hashes:

| Immutable file | SHA-256 |
|---|---|
| `PAPER_PLAN.md` | `e4876a50d172ccfb857b3c6667a0be85d12105f4d7da63da393531a36cef9d31` |
| `paper/manuscript.tex` | `f3c535739046e61378ec8896b70e6d30652a7654213894e1556d221e511d3022` |
| `paper/references.bib` | `f1b6fe0807e33debf87c8be19e1b81b2a4a10f886fd9f4ae1d20bf264e978adc` |
| `paper/figures/FIGURE_TRACE.json` | `7ffb609fd2e7a1f4cd1598d750e754787d72b0efec03188b4789e3e95003185d` |
| `paper/figures/DETERMINISM_AUDIT.json` | `c9442c6f75ca6bcc1bb8294faf75f2ff0a89866e6a9c6e8758fbeea54eb324b3` |

The unchanged trace binds the same three figure contracts, generators,
captions, labels, input authorities, output hashes, transformations,
supported claims, and nonclaims as R1. The rebuilt manifest closes those
links against the current ordinary nonsymlink files.

## 4. Media immutability and independent regeneration

All nine frozen media hashes equal the R1 hashes:

| Output | SHA-256 |
|---|---|
| `fig1_theorem_architecture.pdf` | `1fbed2c5d27025763b68f660a87f695d4c7fe3a96e7786ef98b0bdccf0a53b79` |
| `fig1_theorem_architecture.png` | `469eb67789e64f8dadf2350c241828081fe0ae0f2b5a8dfbde838b31b7a78d25` |
| `fig1_theorem_architecture.svg` | `6d8f21b62b08cc019a992a37861e00d38577323117590d6909e12b30a5b5a43a` |
| `fig2_weighted_two_term_law.pdf` | `744853231c1c2700bb29f0ca4d8cf0d4059691966d91a0316c7674c526054835` |
| `fig2_weighted_two_term_law.png` | `cb04e39943746491ba61bb4de8b66a5047f1bc9ba15447f546004fdc8c09a7d1` |
| `fig2_weighted_two_term_law.svg` | `8b2c68d86f7aec84893c668fe354b432324f6413d390e6a6b85cd0d930c0dd11` |
| `fig3_step9_certificate_pipeline.pdf` | `e120cb0c8d05cf884862c3e0d23a8db7b45115e5691fda65620d9bcf203c5f6a` |
| `fig3_step9_certificate_pipeline.png` | `86914b64a13c6abcc4ebcbb2f80a78caf617d3ac5a6ab91e336134623621ca22` |
| `fig3_step9_certificate_pipeline.svg` | `03b6b1a5b94b1fb71b9b4dd7f1c6186c4cdf40309134743e67aa1e42381a9ca6` |

Two new isolated asset copies were made with only `PAPER_PLAN.md`, the
citation ledger, the citation contract, manuscript, bibliography, and the
publication figure directory. Neither copy contained `code/`,
`preexecution/`, `results/`, or `runtime/`. In each copy I ran:

```text
python3 -B paper/figures/generate_all.py
python3 -B paper/figures/build_records.py
```

Each `generate_all.py` invocation additionally used its own two internal
isolated generation trees. In both outer copies:

- all nine regenerated media files were byte-identical to each other and to
  the frozen package;
- `DETERMINISM_AUDIT.json` was byte-identical at `c9442c6f...`;
- `FIGURE_TRACE.json` was byte-identical at `7ffb609f...`;
- `FIGURE_MANIFEST.json` was byte-identical at `3adc9709...`; and
- `ASSET_TREE.json` was byte-identical at `a5006ef6...`.

Thus 13 regenerated/rebuilt artifacts per outer copy match the freeze, with
zero forbidden-root directories in both copies.

## 5. Record, path, and hash-link closure

Strict duplicate-key-rejecting parsing passed for the proof lock, citation
contract, figure contract, determinism record, manifest, trace, and asset
tree. Independent link traversal established:

- the lock's eight allowed inputs are ordinary nonsymlink files and match
  their recorded hashes;
- figure-contract, trace, and manifest input bindings equal exactly those
  eight inputs plus the proof lock and proof-only handoff;
- every manifest generator/documentation/output/trace/determinism hash link
  resolves to the named current file;
- every trace generator and output hash resolves;
- every determinism run-one hash equals run two and the frozen output;
- every citation record path and digest resolves to the unchanged
  manuscript, bibliography, contract, and primary-source ledger; and
- `ASSET_TREE.json` enumerates exactly 27 ordinary nonsymlink publication
  files, with no omission, extra path, byte-count mismatch, or digest
  mismatch.

The manifest and tree still say
`FROZEN_PENDING_INDEPENDENT_ASSET_REVIEW` and
`independent_asset_pass=false`. Those are correctly frozen author-side
pre-review states, not self-issued independent outcomes. This external R2
report is the independent verdict and does not rewrite author records.

## 6. Mechanical and visual regression

The rebuilt manifest's mechanical facts were independently rechecked.

| Figure | PDF | SVG | PNG | Result |
|---|---|---|---|---|
| Fig. 1 | one page, 518.4 x 363.6 pt, vector-only, embedded fonts, no Type 3 | valid XML, selectable text, no raster image node | 2160 x 1515 RGBA, 299.9994 dpi | PASS |
| Fig. 2 | one page, 518.4 x 360 pt, vector-only, embedded fonts, no Type 3 | valid XML, selectable text, no raster image node | 2160 x 1500 RGBA, 299.9994 dpi | PASS |
| Fig. 3 | one page, 518.4 x 399.6 pt, vector-only, embedded fonts, no Type 3 | valid XML, selectable text, no raster image node | 2160 x 1665 RGBA, 299.9994 dpi | PASS |

The three frozen PNG originals were inspected at native resolution. Fresh
300-dpi grayscale renderings from the PDFs were then inspected separately.
No edge clipping, cut-off glyph, panel-marker collision, or new overlap was
found. All claim-bearing distinctions remain readable without color:
survive/remove cross-outs, proof firewall, dashed no-theorem branch,
separate hatched `j=0`, and crosshatched `OPEN` boundaries. The epsilon-one
specialization, spectra, four supports, two eliminations, quartic constants,
length 60, identity (9.14), incoming transfer, and finite certificate remain
legible. There is no internal decorative title; A/B/C are panel markers.

Visual and mechanical regression result: PASS.

## 7. Targeted science, plan, caption, and nonclaim regression

The plan, manuscript, trace, determinism record, and all media are
byte-identical to the R1-reviewed versions. This immutability carries forward
R1's full C1--C18 and PC1--PC2 audit. A fresh targeted regression also
checked the most fragile boundaries:

- Figure 1 says `S_m(a,1)=C_m+D_m a^{2m-1}`, retains `q^2=0` with `q`
  possibly nonzero, retains `2+q(x)q(y)` before diagonal subtraction,
  restricts the quartic theorem to the complete normalized `0^4` fiber,
  gives the exact pointwise moment and length 60, and has no audit-to-theorem
  arrow.
- Figure 2 has exactly four weighted supports, the two exact survivors, both
  crossed-out eliminations with their proof reasons, the two-term law,
  odd-`m` parity, the exact quartic formula in both forms, and an explicit
  `OPEN` no-all-degree-separator boundary.
- Figure 3 retains the seven-stage recurrence-to-certificate order, local
  identity (9.14), incoming-transfer bijection, separate `j>=1` and `j=0`
  branches, the exceptional vanishing, the `H/A/D` formula, and the explicit
  statement that no finite diagnostic proves universal nonvanishing.
- The plan remains one theorem-first story with PC1 front-loaded, PC2 as its
  mechanism, a complete Step-9 allocation, separate Step-10 moment and
  Step-13 multiplicity obligations, honest limitations, and exact
  claim--evidence mapping.
- All three captions and labels remain whitespace-normalized identical in
  the plan, figure contract, trace, and `latex_includes.tex`. Their
  prospective locations remain unchanged, and no figure was inserted into
  the manuscript.
- The primary-source ledger and bibliography are unchanged. Cantat--Dujardin
  remains the direct-family/low-period precedent; residue, trace,
  formal-period, and low-period Hénon methods remain prior art; adjacent
  works are not promoted to support PC1 or PC2; and the bounded no-hit search
  is not converted into historical-priority proof.

## 8. Forbidden-root, registered-evidence, and diagnostic regression

The generation scripts continue to read only `figure_contract.json` and
their publication helpers. `generate_all.py` invokes only the three
standalone figure scripts. The record builder reads the publication layer
and now reads `paper/manuscript.tex` solely for mechanical citation-domain
validation. It does not admit the manuscript as scientific authority.

No generator imports or reads `code/`, `preexecution/`, `results/`, or
`runtime/`. Both fresh outer copies omitted those roots completely and still
regenerated every asset and record.

Targeted text scans found no statement or implication that Track Q, Track R,
or adjudication passed; that Q and R agreed; that a registered coefficient
matched; that any theorem is computationally, experimentally, or
empirically certified; that a raw result or result pass exists; or that a
rerun or retained traceback confirmed the failure. The only audit wording is
the allowed terminal-failure, no-rerun, no-raw-result, no-result-pass,
provenance-only disclosure.

No numerical value of `D8`, `D9`, `E8`, `E9`, `D_8`, `D_9`, `E_8`, or
`E_9` appears. Universal `D_m != 0`, all-degree period-three separation, a
theorem for all quartic Hénon maps, global `P(4)=3`, global conjugacy
classification, and global multiplier rigidity remain explicit nonclaims.

Result: PASS.

## 9. Gate disposition

Blocking findings: 0.

Unresolved advisories: 0.

The Round-1 exact-domain defect is repaired without changing the manuscript,
bibliography, plan, proof inputs, figure semantics, media, trace, or
determinism record. Exact citation migration is now mechanically defined on
every frozen manuscript citation key and only on those keys. The independent
plan/figure asset gate is therefore discharged.

**Final verdict: `ASSET_PASS`.**
