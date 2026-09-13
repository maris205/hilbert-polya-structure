# Paper 12 Figure Provenance

## Disposition

- Candidate/lifecycle: `henon_period3_residue_proof_note_v1`
- Asset class: proof-navigation diagrams only
- Registered evidence used: `false`
- Scientific runtime, result file, or registered diagnostic used: `false`
- Asset-author review: complete
- Independent `ASSET_PASS`: **not issued by this author; required next**
- Finalization authorized: `false`

These figures visualize the organization and boundaries of an immutable
proof. They are not experimental plots, numerical-result plots, runtime
screenshots, or computer-assisted theorem certificates.

## Closed input authorities

The publication package used only the closed proof-only allowlist and the
independent handoff:

| Path | SHA-256 | Role in assets |
|---|---|---|
| `experiments/proof_only_manuscript_lock.json` | `2c7f056b7f9566f754a06c30417105c0b1cefb2d0081f4bca8bb3a00adbf8eeb` | closed input and forbidden-root policy |
| `experiments/source_lock.json` | `2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2` | frozen source binding |
| `notes/CITATION_VERIFICATION.md` | `eb99e7ab59e5d2947b6d5dab0d23dd471c05d090280f7915f010210b021e39ee` | source roles and bounded novelty language |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `5630610bb637e155fa631eb2d9c4b36c6ea334ae976a6ef39a53dd733b8c62de` | atomic claim and nonclaim boundary |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` | `5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11` | independent source verdict |
| `notes/NOVELTY_ASSESSMENT.md` | `c497dc4e2c404fbbfc3c89450991964d1049f06288a051bc647a15005a66146a` | narrow positioning and paper-size gate |
| `notes/PROOF_ONLY_MANUSCRIPT_SCOPE.md` | `d0dc07976e9631e5d30ffe6d20f1e4d7d76aea4c04d1d42598e3b594d0fc23b9` | presentation and provenance contract |
| `notes/PROOF_PACKAGE.md` | `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9` | sole scientific theorem authority |
| `notes/REGISTERED_AUDIT_POSTMORTEM.md` | `6648a0c3642d24eac1e22f3cc7349a805209d3293b556d6d5d5cbd873d0f831b` | failure disclosure only, never scientific evidence |
| `notes/INDEPENDENT_PROOF_ONLY_HANDOFF_REVIEW.md` | `407cec5bf295c29330c24ae461dca86ad1bf54d77f44d477d83a821bf7e41711` | proof-only drafting authorization |

No transitive expansion through the source lock was used. The recursively
forbidden Paper-12 roots `code/`, `preexecution/`, `results/`, and `runtime/`
were not read or used as manuscript evidence or figure input.

The record builder additionally reads `paper/manuscript.tex` solely to
extract citation commands and enforce exact equality between their key set
and the frozen migration-map domain. This mechanical integration check is
not a scientific authority or figure input.

## Figure transformations

### Figure 1

The source proof's period-one, formal exact-period-two, period-three, and
quartic statements are arranged as a theorem dependency diagram. The
period-three box uses the explicit specialization

\[
S_m(a,1)=C_m+D_ma^{2m-1},
\]

so it cannot be confused with Figure 2's full two-parameter law. A horizontal
firewall separates the source proof and independent reviews from a hatched,
dashed audit-provenance box. The latter has no arrow into a theorem and states
terminal failure, absence of raw/result pass authority, and lack of
finalization authority.

### Figure 2

The four solutions of the source proof's weight equation are rendered as two
surviving and two crossed-out supports. Each elimination is attached to its
proof reason. The diagram then shows the exact two-term law, odd-$m$ parity,
quartic specialization, and a dashed/hatched `OPEN` box for universal
$D_m\neq0$.

### Figure 3

The mandatory Step-9 order is rendered as seven numbered stages: recurrence
and base cases; Laurent/order independence; admissible tuples; local identity
(9.14); distinguished-coordinate and incoming-transfer classification;
separate $j\geq1$ and $j=0$ flows; and the $H/A/D$ certificate. The
$j=0$ stage has a distinct hatch. The final `OPEN` box explicitly rejects
finite diagnostic evidence for universal nonvanishing.

## Bibliography provenance

The locked primary-source ledger remains byte-identical at its allowlisted
hash. Bibliographic metadata in `paper/references.bib` was rechecked on
2026-08-16 UTC against arXiv's primary Atom records for the three preprints,
DOI/publisher registration records for published works, and the New York
Journal of Mathematics primary record for Hutz (2010). The canonical 11-key
set and the bounded ten-key frozen-draft migration are recorded in
`paper/CITATION_KEY_CONTRACT.json`; duplicate alias entries are forbidden.

## R1 bounded-repair history

The independent R1 report is preserved unchanged at
`notes/INDEPENDENT_PLAN_FIGURE_REVIEW.md`, SHA-256
`d6bc5c624d371752f06ff1d8a8ae27367a7b4c2370b4ab2f19b52cbe24d95ed6`,
with verdict `REPAIR_REQUIRED`. Its single blocker was a disjoint exact
domain between the ten manuscript citation placeholders and the ten keys in
the migration map. No existing publication-record schema provides a review-
history field, so this provenance section and `FIGURE_QA.md` bind the R1
report for the requested R2 history.

The bounded repair changed the citation contract from
`e73c0c75310cdb60706bed900ac90308cd27320a9d9ce6d53b2fc7e73ce82f92`
to `997ca84ee7d868f34cacc783993f10d1b82b86c71fbdc1c9b80f38bcf5199bfd`.
Only the ten map-domain keys changed; all PascalCase targets, the canonical
bibliography, manuscript, plan, captions, figure sources, and media remained
unchanged. `build_records.py` now extracts citation keys from the manuscript,
requires exact set equality rather than cardinality, records both sets and
their empty difference, and fails closed on an unparsed citation command.

## Reproduction

From the Paper-12 root, run:

```text
python3 -B paper/figures/generate_all.py
python3 -B paper/figures/build_records.py
```

`generate_all.py` creates two isolated temporary trees, invokes one standalone
script per figure, compares all nine output hashes, and copies outputs only
after byte identity passes. Fixed `SOURCE_DATE_EPOCH`, `PYTHONHASHSEED`, PDF
dates, SVG hash salt, and metadata make each format deterministic. The
generation scripts read only `figure_contract.json`; they do not open any
scientific runtime or result tree.

## Copyright and authorship

All diagram composition and wording were authored for this Paper-12 package.
No third-party figure, screenshot, photograph, or quoted passage is embedded.
Prior sources are credited bibliographically rather than visually copied.
