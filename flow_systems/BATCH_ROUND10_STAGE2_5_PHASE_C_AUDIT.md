# Round 10 Stage 2.5 Phase C Data and Experiment-Provenance Audit

Audit time: **2026-09-02T16:41:02Z**  
Scope: **Papers 29--33; ARS Phase C1--C4 and declaration-anchored D7 only**  
Canonical mutation: **none**  
Scientific execution: **none**

## Disposition

**Phase C verdict: PASS.**

All **244/244** Claim Registry rows tagged `quantitative`, `statistical`, or
`data` were enumerated against the exact pre-repair manuscript bytes. None is
a reported project-owned statistical or experimental outcome. The rows divide
into frozen scientific-design/formal surfaces, internal literature-workflow
accounting, bibliographic/contextual numeric tokens, structural false-positive
tags, and five P33 table-spanning registry rows. No Phase-C numerical
inconsistency, unreported own-experiment result, or table-to-prose overclaim was
found.

This is a coverage-bounded Phase-C result. It does not establish semantic Claim
Registry completeness, mathematical truth, successful scientific execution,
or an overall Stage-2.5 verdict.

## Frozen inputs

| Artifact | SHA-256 |
|---|---|
| Scholar experiment-declaration receipt | `4d38cbe820e8832604b1cbb9a8443f8da1b6d27f57c4c6143da54fabbc0fdae2` |
| Experiment-intake request at confirmation | `48374f70e9e4780897a95ed519a54ed4259a7209f833dee0128103d53fe21397` |
| Current request after receipt-preserving closure addendum | `5325bb7abda07d3694feec1c32ea8375042da6a64cc10eb884e1c206de6d5227` |
| Stage-2.5 route crosswalk | `8eeff02ed29dddc62f801e727b208848a479db5f85304c0a194e98bac532131f` |
| Stage-2 replay receipt | `14d826b03b94850990d8fa77f59a9c9265668601b6214573528b5ca18ee0c32c` |

The declaration receipt deliberately retains the confirmation-time request
digest. The request file's current digest differs because a closure addendum
was appended after confirmation; the scholar event remains bound to the
preserved confirmation-time digest, not retroactively to the amended bytes.

## Registered population and classification

The machine denominator is every registry row whose `claim_kinds` contains
`quantitative`, `statistical`, or `data`. Exact sorted-ID-set digest for the
five-paper union is
`001310a3dbe08875f2bb824f36c3a9a889d0f0b5b7ed23aa3b44e200217714d8`
under the rule `SHA256(sorted IDs joined by LF with a final LF)`.

| Paper | Registry claims | Phase-C rows | Literature/context numeric metadata | Workflow accounting/disclosure | Frozen design/formal/status | Structural nondata | Prospective table spans | Reported statistical or own-experiment outcomes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| P29 | 83 | 45 | 22 | 11 | 12 | 0 | 0 | 0 |
| P30 | 95 | 53 | 26 | 14 | 13 | 0 | 0 | 0 |
| P31 | 78 | 45 | 7 | 9 | 19 | 10 | 0 | 0 |
| P32 | 98 | 58 | 10 | 9 | 24 | 15 | 0 | 0 |
| P33 | 126 | 43 | 16 | 4 | 16 | 2 | 5 | 0 |
| **Batch** | **480** | **244** | **81** | **47** | **84** | **27** | **5** | **0** |

The table-spanning rows are counted separately from the 84 prose-level design
rows, so the classification is disjoint and sums exactly to 244. The
`quantitative` tag is intentionally conservative: source IDs such as `P32-S13`,
numbered headings, years, DOI digits, and LaTeX table spans can trigger the
registry even when the row is not a statistical assertion.

## C1 statistical-data cross-reference

No manuscript reports a project p-value, confidence interval, effect size,
sample mean, variance, accuracy, ablation, seed count, observed improvement,
scientific coefficient table, or experimental comparison. Consequently the C1
population of reported statistical figures is **0**, rather than an untraced
positive denominator.

The quantitative surfaces that do exist were traced as follows:

- **81 literature/context rows:** numeric tokens belong to reference identity,
  source context, page/year/DOI information, or a cited method. They are not
  reclassified as project measurements. Bibliographic and semantic source
  correctness remains governed by Phases A, B, and E.
- **47 workflow rows:** values are checked against source inventories,
  verification TSVs, review records, build receipts, citation markers, and
  hash-bound manifests. These are document/provenance facts, not scientific
  experiments.
- **84 design/formal/status rows:** values are immutable inputs, exact finite
  arithmetic, candidate formulas, quantifiers, prospective gates, or negative
  execution states. Candidate formulas remain explicitly unproved and were not
  promoted to results.
- **27 structural rows:** numbered headings or small registry fragments carry
  numeric tokens but no data assertion.
- **5 P33 table rows:** both tables are prospective design specifications and
  contain no measured cell.

## C2 internal-consistency replay

### P29

- `48 - 12 = 36` record manifestations after duplicate removal.
- Source inventory: 22 rows; 17 rows marked peer reviewed; verification ledger:
  22 `VERIFIED` rows.
- Manuscript citation provenance: 22 source-ID pairs and 22 unique IDs.
- Level-(3), the literal one-ideal codomain, Gate M/Gate Q, and all five
  prospective interfaces remain definitions or obligations. No owner,
  quotient, collision statistic, or Route output is reported.

### P30

- `68 - 16 = 52` unique screened records; 26 retained.
- Source inventory: 26 rows; 24 peer-reviewed rows; verification ledger:
  26 `VERIFIED` rows.
- Bibliography-year replay: 24 of 26 records predate 2021, matching the
  manuscript limitation.
- The error ledger has five channels: four numerical components plus separately
  propagated geometry/roof-input uncertainty. This is a prospective typing
  identity, not a computed bound.
- All six gates remain open. No physical roof, eligible operator, determinant,
  enclosure, fidelity result, or nontransfer result is reported.

### P31

- `44 - 9 = 35` unique screened records and `35 - 13 = 22` retained sources.
- Source inventory: 22 rows; 19 peer-reviewed rows; verification ledger:
  22 `VERIFIED` rows.
- The inherited instance split satisfies `2 + 2 + 134 = 138`.
- The proposed all-pairs audit satisfies
  `binom(138,2) = 138*137/2 = 9,453`.
- The conditional incidence relation has one row per frozen input, hence
  `|I|=138`; `G`, `I`, and `C` remain unmaterialized scientific objects.
- No canonicalizer, pair result, owner partition, owner count, or cell quotient
  is reported.

### P32

- `51 - 12 = 39` unique screened records and `39 - 13 = 26` retained sources.
- Source inventory: 26 rows; 22 peer-reviewed rows. The historical Stage-2
  verification split is `25 VERIFIED + 1 PLAUSIBLE = 26`.
- For fixed positive `d`, the prospective factorial schedule has
  `gcd(k!,d)=d` once `d` divides `k!`; this checks the displayed design
  arithmetic, not the cover-factor theorem.
- The candidate zero-content bookkeeping `N^4` components under `1/N^3`
  logarithmic scaling yields the displayed candidate exponent `N`. The
  manuscript correctly says every underlying field still requires proof.
- The prefix `k=1,...,8` and panel sizes `{8,16,32,64,128}` are explicitly
  unexecuted and assigned no convergence force.
- No factor derivation, coefficient comparison, panel result, limit, or
  scientific computation is reported.

### P33

- `26 - 6 = 20` retained sources.
- Source inventory: 20 rows; 18 peer-reviewed rows; verification split:
  `9 S2_VERIFIED + 10 VERIFIED + 1 PLAUSIBLE = 20`.
- Manuscript citation provenance: 48 source-ID pairs and 20 unique IDs.
- The first longtable contains eight prospective record families. The second
  table's package rows cover the union of obligations 1 through 7.
- `P33-RC-1` is consistently `0/7` in the table, surrounding prose,
  limitations, and conclusion.
- Neither the fixed `b=1/2` subtype nor `Lambda=21/10` is presented as a new
  measured outcome. No producer, schema bytes, adapter, validator, fixture,
  census, arithmetic comparison, magnetic result, determinant result, or Route
  result is reported.

Across all papers, the manuscript ARS-CITE source-ID pair counts are
`22 + 26 + 22 + 26 + 48 = 144`, matching the batch-wide locator statement.

## C3 figure/table fidelity

P29--P32 contain no `figure`, `table`, `longtable`, `tabular`, or
`includegraphics` surface. P33 contains no figure and exactly two source-native
text longtables. Both are fully traced in the P33 JSON sidecar.

| Artifact | Manuscript locator | Classification | Source/transform trace | Caption-claim support | Forward/reverse linkage | Limitations visible | Verdict |
|---|---|---|---|---|---|---|---|
| `P33-TBL-SEMANTIC-RECORD-FAMILIES` | `manuscript.tex:L252-L320` | prospective design table | Phase-6 revision log + recheck + Stage-2 blueprint; precise manual row transcription | PASS | 8 linked claim surfaces; PASS | 2/2 surfaced | PASS |
| `P33-TBL-RC1-THREE-PACKAGE-MAPPING` | `manuscript.tex:L340-L381` | prospective design table | Phase-4 report + Phase-6 revision log + recheck; manual 1--7 set-union mapping | PASS | 13 linked claim surfaces; PASS | 2/2 surfaced | PASS |

Both tables use the subsection heading and lead sentence as their semantic
caption surface rather than a separate `\caption{}` command. They are LaTeX
text tables, so raster/VLM verification is not applicable. The trace does not
claim that either table is a dataset or an executed schema.

## C4/D7 experiment declaration and anti-skip

The scholar-confirmed receipt records, for all five papers:

- `status = no_experiments_declared`;
- `declared_by = scholar`;
- `declared_at = 2026-09-02T16:05:50Z`;
- `experiment_provenance = []`;
- no scientific-execution, canonical-scientific-content, Route, or Stage-3
  authorization.

The exact mandatory boundary is preserved in the receipt and every per-paper
sidecar:

> This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

D7 replay results:

| Check | Result |
|---|---|
| Declaration present for a treated-as-post-#260 passport projection | PASS |
| `no_experiments_declared` with nonempty provenance | 0 contradictions |
| Stage-2 ClaimIntent manifests | 40 claims total; 0 `planned_experiment_ids` pointers |
| Empirical-intent manifest claims | 2 workflow/source-ledger claims, both with 0 experiment pointers |
| Results-section first-person own metric/ablation/run statements | 0 |
| Non-`.gitkeep` files in the five papers' `code/`, `experiments/`, and `results/` directories | 0 |
| Manuscript/declaration contradiction | 0 |
| Experiment-backed claims requiring `experiment_alignment_results[]` | 0 |

The five Material Passports have not yet been emitted. Their C4 blocks must
copy this declaration and boundary exactly; this audit marks that projection
ready but does not fabricate a passport or infer additional scholar authority.

## Mismatches, overclaims, and scope separation

No **Phase-C** mismatch or overclaim was found.

Three findings already tracked by other integrity phases remain visible and
are not silently cleared here:

- P29's omitted volume editors are a Phase-A bibliographic correction.
- P31-E1-056 is a nonquantitative Phase-E reconstructability overclaim.
- P32-S13's live current-state wording is a Phase-A source-status correction;
  the historical Stage-2 `25/1` accounting remains accurate.

They are listed in
`BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_REQUEST.md`, current SHA-256
`778c5ef44b3ef3790f0e34098923735edbd9a2af681c79d4f0fc8f83a69a7e16`.
This Phase-C PASS neither authorizes nor substitutes for those repairs.

## Sidecars and exact hashes

| Paper | Sidecar | SHA-256 | Coverage |
|---|---|---|---:|
| P29 | `papers/29-bianchi-ideal-owner-refinement/notes/stage2_5_phase_c_data_trace.json` | `9adc4befcbda9519a80227bb7fee5c42326c3ad40bf4dc57eb3e47c01d30ca11` | 45/45 |
| P30 | `papers/30-three-disk-nonconstant-roof-determinant/notes/stage2_5_phase_c_data_trace.json` | `63a54c9e348b5ca5352ed7068b244139684dd9fb044400df9effdf21cfb22b36` | 53/53 |
| P31 | `papers/31-level11-conjugacy-owner-ledger/notes/stage2_5_phase_c_data_trace.json` | `e5d80d7832470d27c5b1a00db49532cfe8f91ce6962af2682df2c3389214624d` | 45/45 |
| P32 | `papers/32-homology-cover-renormalization-uniformity/notes/stage2_5_phase_c_data_trace.json` | `9ad199fa5e1eab5eb9b43c113601cc0695dbc052371abc669f0621c997b210be` | 58/58 |
| P33 | `papers/33-bolza-control-matched-census/notes/stage2_5_phase_c_data_trace.json` | `0e115edf6a2ec1d701b44e75c8e7ac96b64cc0a0fb3c8b0c1b771d09af9fa3bf` | 43/43; 2/2 tables |

Deterministic readback validated all five JSON documents, every declared input
hash, exact population coverage with no duplicate/missing/extra claim ID, the
verbatim C4 boundary, and both P33 table traces' required keys and source
hashes.

No manuscript, bibliography, PDF, README, pipeline state, Route artifact,
canonical result, or scientific output was modified by this Phase-C audit.
