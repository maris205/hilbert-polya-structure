# Paper 22 — Independent Publication Lock Review

Date: 2026-08-24 UTC  
Project root: `papers/22-hamiltonian-cubic-spectral-collapse`  
Reviewer role: fresh independent publication-lock auditor  
Write authority used: this file only

## Scope and result

I performed the bounded publication-lock integrity review required by
`experiments/publication_lock.json` and wrote no path other than this review.
Every conjunctive structural, provenance, semantic, and permission check passed.

The audited lock is:

- path: `experiments/publication_lock.json`
- SHA-256: `3d7eb3c7ef143a17c1ccdb82ece985a05c916b78c1ebe0591bca8af3c05ce6cd`
- bytes: `34222`
- LF count: `1`

## 1. Strict canonical JSON audit

I validated the lock with two independent strict parsers/runtimes:

1. Python strict parse:
   - UTF-8 decode with `errors="strict"`;
   - duplicate-key rejection via `object_pairs_hook`;
   - nonfinite rejection via `parse_constant`;
   - recursive object-key order audit against Unicode code-point sort order;
   - byte-exact canonical reserialization with compact separators and one final
     LF.
2. Node.js independent parse:
   - fatal UTF-8 decoding via `TextDecoder("utf-8", { fatal: true })`;
   - custom recursive-descent JSON parser rejecting duplicate keys, malformed
     escapes, malformed surrogates, and nonfinite numbers;
   - recursive key-order audit;
   - canonical reserialization check against the original bytes.

Both routes agreed on the same object and the same external identity above.
Both confirmed:

- no BOM;
- no CR;
- no NUL;
- exactly one physical JSON line;
- exactly one terminal LF;
- compact canonical UTF-8 JSON round-trips byte-exactly;
- `self_identity_exclusion.path == "experiments/publication_lock.json"`;
- `self_identity_exclusion.bytes == null`;
- `self_identity_exclusion.sha256 == null`;
- `post_lock_universe.self_structural_record.bytes == null`;
- `post_lock_universe.self_structural_record.sha256 == null`.

The lock therefore satisfies the declared `canonical_json_contract`.

## 2. Independent recomputation of the 17-file pre-lock universe

I recomputed every listed pre-lock project file and matched the lock’s stored
per-file hygiene and identity fields:

| Path | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 5812 | 146 | `914542c082f3bc65c47db822c6d7d3bceca8b55041117548b10b1cef96cc2873` |
| `experiments/EXPERIMENT_TRACKER.md` | 3318 | 63 | `07c147aaa323bb7d445d3fb669a9c75b896a006f53aed1d8f11e3e0637d35f4c` |
| `experiments/source_lock.json` | 32258 | 1 | `6f79231121f78e1c6b55da148c5710c2005e0ae36f92b0771740d127a253ad88` |
| `notes/CITATION_VERIFICATION.md` | 4916 | 65 | `d2b89b3313d54e612c3aa6e1e0a454c034d312268fd431217638417d90afa2bc` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 6915 | 94 | `b1184e0dffd4ccd633e9ced15c227e5bad3e9074627fd7442bd78896c1f48416` |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | 10683 | 248 | `20c7e7b49a2f698b509026bd025e5dd3ebf000ff6d3fa343466867e755d3951c` |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | 16536 | 388 | `65bfe3d7e24c6f9f4ec6a826f2d29a387c0105e208f4990226a4d22242f24512` |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 12590 | 390 | `a8dd5800afbf1b950453bd8fef7538b8c4a97e8a971d4db5e0c4705aa9917e56` |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | 16605 | 521 | `1fa152bdf1cf83a852b7e585e1e3aac402d06534c447a881e7506f082594846f` |
| `notes/NOVELTY_ASSESSMENT.md` | 7486 | 140 | `dbd33f68af27f0ba57982e5bb6f2dde8d01099188e2d240e0319199ee52b2699` |
| `notes/PROOF_PACKAGE.md` | 23639 | 951 | `2d290cbc316b42be8c978a527d9fa24751c992f532747067aeaf64d79eef6846` |
| `notes/PUBLICATION_STAGE_SCOPE.md` | 21397 | 561 | `49b17a22be1a774f5befbce67f54d1770d8277bd179a4a7ec728e4f55a59eeeb` |
| `notes/RESEARCH_QUESTION.md` | 5266 | 138 | `fc2269c6abe58b077b1c0b33bf07f93661f59a2ca72733330b9d67c38cb63175` |
| `paper/PAPER_PLAN.md` | 34692 | 952 | `2fdfc4eab1bd60e361b144eb8c3c9d0d7c71d37c63ce54145e7e6cca3888e224` |
| `refine-logs/FINAL_PROPOSAL.md` | 5764 | 162 | `f58efbf336df21ab32296fc3c022be2200d4a0c7679e935652a405600c182679` |
| `refine-logs/INITIAL_PROPOSAL.md` | 4052 | 124 | `1d23119b72630a34446a0a331e1f3be5bf8e8362385c88b63c7f568aa411097d` |
| `refine-logs/REVIEW_SUMMARY.md` | 3234 | 80 | `96ee47f7cfa3f5324521335ebba6b6a21e009631fd0d668a3de7061dcf8a934d` |

For all 17 files I also independently matched the lock’s regular-file status,
non-symlink status, UTF-8 validity, no-BOM/no-CR/no-NUL hygiene, mode `0644`,
and terminal-LF requirement.

I recomputed the framed aggregate exactly as specified:

- path base: `papers/22-hamiltonian-cubic-spectral-collapse`
- order: byte-sorted UTF-8 relative POSIX names
- framing: `uint64_be(name_byte_length) || name_utf8 || uint64_be(content_byte_length) || content_bytes`
- file count: `17`
- total bytes: `215163`
- total LF: `5024`
- framed bytes: `215965`
- aggregate SHA-256:
  `bedd0f0ced78d7540e5276675752aba6db52abf93d08ec1a9cd2458de25768da`

This exactly matches `pre_lock_universe.aggregate`.

## 3. Author-stop inventories and absence checks

Immediately before this review write, I verified the current project universe is
exactly:

- `18` regular files;
- `4` child directories: `experiments`, `notes`, `paper`, `refine-logs`;
- `0` symlinks.

The pre-write regular-file universe includes `experiments/publication_lock.json`
and excludes this review file, matching `post_lock_universe.regular_file_paths`
exactly.

I also verified all declared forbidden/currently absent paths remain absent:

- directories or trees:
  `assets`, `build`, `code`, `data`, `figures`, `manuscript`, `publication`,
  `release`, `results`, `submission`, `transport`;
- future source candidates:
  `paper/main.tex`, `paper/math_commands.tex`, `paper/references.bib`;
- premature review path:
  `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md` before this write.

Post-review inventory after this sole authorized write is therefore:

- `19` regular files;
- `4` child directories;
- `0` symlinks.

## 4. Bound upstream artifacts and root provenance

### 4.1 Upstream project artifacts bound by the lock

I verified each bound upstream artifact exists, matches the lock exactly, and
has the required terminal PASS/STOP line when one is declared:

| Binding | Path | Bytes | LF | SHA-256 | Terminal line |
|---|---|---:|---:|---|---|
| source lock | `experiments/source_lock.json` | 32258 | 1 | `6f79231121f78e1c6b55da148c5710c2005e0ae36f92b0771740d127a253ad88` | self-null only |
| source lock review | `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | 16605 | 521 | `1fa152bdf1cf83a852b7e585e1e3aac402d06534c447a881e7506f082594846f` | `SOURCE_LOCK_PASS` |
| paper plan | `paper/PAPER_PLAN.md` | 34692 | 952 | `2fdfc4eab1bd60e361b144eb8c3c9d0d7c71d37c63ce54145e7e6cca3888e224` | `PAPER PLAN PERMISSION REPAIR AUTHOR STOP R2` |
| paper plan review | `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | 10683 | 248 | `20c7e7b49a2f698b509026bd025e5dd3ebf000ff6d3fa343466867e755d3951c` | `PAPER_PLAN_PASS` |
| publication stage scope | `notes/PUBLICATION_STAGE_SCOPE.md` | 21397 | 561 | `49b17a22be1a774f5befbce67f54d1770d8277bd179a4a7ec728e4f55a59eeeb` | `PUBLICATION SCOPE AUTHOR STOP` |
| publication stage review | `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | 16536 | 388 | `65bfe3d7e24c6f9f4ec6a826f2d29a387c0105e208f4990226a4d22242f24512` | `PUBLICATION_STAGE_PASS` |
| source design review | `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 12590 | 390 | `a8dd5800afbf1b950453bd8fef7538b8c4a97e8a971d4db5e0c4705aa9917e56` | `SOURCE_DESIGN_PASS` |
| proof package | `notes/PROOF_PACKAGE.md` | 23639 | 951 | `2d290cbc316b42be8c978a527d9fa24751c992f532747067aeaf64d79eef6846` | none declared |

The source-design author stop is also still present at
`refine-logs/REVIEW_SUMMARY.md` with SHA-256
`96ee47f7cfa3f5324521335ebba6b6a21e009631fd0d668a3de7061dcf8a934d`,
3234 bytes, 80 LF, and terminal line `SOURCE DESIGN AUTHOR STOP`.

### 4.2 Root provenance records

I verified all six root provenance records exactly as locked, and all remain
excluded from the 17-file project aggregate:

| Path | Bytes | LF | SHA-256 | Terminal line / note |
|---|---:|---:|---|---|
| `BATCH_06_STATUS.md` | 19626 | 324 | `40db532b5823471fcc3b180b16a84a95d748f21f4e90be90acacd1d14fbff813` | no terminal token bound |
| `BATCH_06_IDEA_REPORT.md` | 23971 | 534 | `b4157a8d0c757fe3afe8986ce9487c0fc8be4b87bdcd77db79fcb51647272eb3` | no terminal token bound |
| `BATCH_06_PAPER22_CANDIDATE_REVIEW_R1.md` | 22934 | 570 | `8d6cb168b303563cfc3719e176ca9b677b060c91a2527d48f4b49488d827e268` | `PAPER22_CANDIDATE_GATE_PASS_R1` |
| `BATCH_06_PAPER22_CANDIDATE_REVIEW_R2.md` | 18787 | 669 | `de7a20a707c5b8926802cb2b5f0db1fd355970a808e908884fa30bbe948b1349` | `PAPER22_CANDIDATE_GATE_PASS_R2` |
| `BATCH_06_PAPER22_PAPER_PLAN_FAILED_R0.md` | 32169 | 795 | `7758ce22918de8ee2511611884f861a58d36b37873e114ebbe5534a83a9301f2` | deliberate CR-bearing immutable history |
| `BATCH_06_PAPER22_PAPER_PLAN_BLOCKED_R1.md` | 34008 | 939 | `6a5ae037c6351291132ff1ea22ade36d851b1f861e5d1e88e4501a8fb498f785` | `PAPER PLAN REPAIR AUTHOR STOP R1` |

The current root lifecycle text remains aligned with the lock-stage state:
`BATCH_06_STATUS.md` still records
`PUBLICATION_STAGE_PASS_PUBLICATION_LOCK_ONLY` and the closure of source,
manuscript, build, PDF, release, Paper 23, and external effects.

## 5. Frozen public identity, theorem boundaries, article contract, citations, and anti-claims

### 5.1 Public identity and firewall

`notes/PUBLICATION_STAGE_SCOPE.md` lines 48-76 and
`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` lines 147-170 still bind and
reaffirm:

- exact title:
  `Cubic Spectral Collapse for Endpoint-Spiked Hamiltonian Product Shears: Sharp Selector Thresholds in Arbitrary Mode Number`;
- visible/source author: `Anonymous`;
- PDF author metadata: exactly empty;
- source date: exactly empty via `\date{}`;
- prohibition on real names, pseudonymous identifiers, affiliations, addresses,
  email, ORCID, acknowledgments, funding, grant numbers, reviewer/agent/model
  identity, local paths, hashes, byte counts, PASS tokens, dashboards,
  governance history, submission venue, and private provenance in public source,
  rendering, comments, bibliography comments, or PDF metadata.

### 5.2 Exact theorem and boundary audit

I checked the lock against `notes/PUBLICATION_STAGE_SCOPE.md`,
`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`, `notes/PROOF_PACKAGE.md`, and
`paper/PAPER_PLAN.md`. The frozen mathematics remain consistent and explicitly
bounded:

- field/parameter boundary: characteristic-zero field, `r>=4`, `g>=2r+1`
  (`PUBLICATION_STAGE_SCOPE.md` lines 80-82; `PROOF_PACKAGE.md` opening and
  lines 118-137);
- map order and geometry: `F=T∘S`, with the specific `S`, `T`, and inverse
  formulas (`INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` lines 188-195);
- selector convention: `sigma=sum_{i=2}^r x_i`, excluding `x_1`
  (`PUBLICATION_STAGE_SCOPE.md` lines 141-147;
  `INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` lines 195-200;
  `PROOF_PACKAGE.md` lines 926-933);
- exact cone language: always “explicit sufficient invariant selector cone,”
  never maximal/necessary/unique/classified
  (`PUBLICATION_STAGE_SCOPE.md` lines 146-167, 419-423;
  `PROOF_PACKAGE.md` lines 50-53, 932-933);
- carry and leading-form requirements: both selector margins, all cone walls,
  `A*1>1`, `C-I>0`, and polynomial-domain leading-form survival remain
  theorem-critical (`PUBLICATION_STAGE_SCOPE.md` lines 155-167;
  `INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` lines 201-205;
  `PROOF_PACKAGE.md` lines 54-62);
- visibility boundary: strict last-coordinate visibility only for `n>=1`,
  while the exact degree identity includes the tied initial case `n=0`
  (`INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` lines 206-211;
  `PROOF_PACKAGE.md` lines 63-70, 645-654, 930-931;
  `PAPER_PLAN.md` lines 223-227);
- spectral-collapse boundary: exact `U`/`E` split, quotient matrix `Q`,
  factorization `chi_C(t)=(t-1)^(r-3)P_{m,h}(t)`, `P_{m,h}(1)`, and exact unit
  multiplicity (`INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` lines 212-215;
  `PROOF_PACKAGE.md` lines 788-800);
- sharp-threshold boundary: `g=2r` gives only the seed/selected-face tie and
  open-cone boundary, not a global failure or global optimality theorem
  (`PUBLICATION_STAGE_SCOPE.md` lines 293-299, 405-406;
  `PROOF_PACKAGE.md` lines 857-866;
  `PAPER_PLAN.md` lines 226-227);
- low-mode boundary: formal `r=3`, `m=1` is predecessor consistency only, not a
  new theorem or correction (`PUBLICATION_STAGE_SCOPE.md` lines 296-298;
  `PROOF_PACKAGE.md` lines 868-887);
- coefficient-corollary boundary: only the four fixed-support nonzero
  coefficients
  `alpha,beta,gamma,delta in K^times`, with no added monomial, altered support,
  vanished coefficient, or positive-characteristic extension
  (`PUBLICATION_STAGE_SCOPE.md` lines 300-307;
  `PROOF_PACKAGE.md` lines 126-136 and 889-916).

### 5.3 Article structure, page, table, and zero-generated-science contract

`notes/PUBLICATION_STAGE_SCOPE.md` lines 318-346,
`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` lines 368-380, and
`paper/PAPER_PLAN.md` lines 204-229 and 780-810 still agree on:

- `§0` Abstract plus exactly eight numbered main sections `§1`–`§8`;
- substantive target `26.5` pages;
- preferred band `24--28`;
- hard band `22--30`;
- all theorem-critical proofs required in `§§2`–`§8`, never repaired in an
  appendix;
- exactly zero generated figures, plots, diagrams, images, assets, empirical
  tables, experiments, datasets, numerical spectra, parameter scans, and CAS or
  symbolic certificates;
- at most three public mathematical tables, and only for the three locked roles
  (gradient support-row ledger; selector/cone proof ledger; three-dimensional
  invariant ledger).

### 5.4 Citation pool and predecessor boundary

`notes/PUBLICATION_STAGE_SCOPE.md` lines 354-390 and
`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` lines 261-282 still bind the
exact six context-only public records and no seventh:

1. `S01` / `BlancVanSanten2021`
2. `S02` / `ShaoSun2025`
3. `S03` / `Deserti2016`
4. `S04` / `DangFavre2021`
5. `S05` / `Rangarajan2002`
6. `S06` / `FujiokaKogawaLiShudo2023`

I verified:

- `citation_lock.exact_source_count == 6`;
- `citation_lock.context_only == true`;
- `citation_lock.no_seventh_source == true`;
- `citation_lock.local_predecessor_citation_authorized == false`;
- `citation_lock.proof_transfer_authorized == false`;
- `citation_lock.priority_or_firstness_authorized == false`.

The public article therefore still may not cite or invent a stable public
identifier for the local low-mode predecessor.

### 5.5 Anti-claims and required public language

I verified the full anti-claim boundary remains intact:

- `11` forbidden-claim entries in `anti_claim_lock.claims_forbidden`;
- `6` mandatory public-language phrases in
  `anti_claim_lock.mandatory_public_language`;
- `8` stop rules in `anti_claim_lock.stop_rules`.

`notes/PUBLICATION_STAGE_SCOPE.md` lines 399-423 and
`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` lines 309-312 still enforce the
required public language:

- explicit sufficient invariant selector cone;
- strict visibility for `n>=1`;
- tied initial case at `n=0`;
- seed/selected-face boundary;
- formal low-mode consistency;
- cubic annihilator.

## 6. Permission audit and source-trio closure

I verified that the lock’s permissions remain internally consistent:

- `authorized_write_paths == ["notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md"]`;
- `publication_lock_review_authorized == true`;
- `publication_lock_authoring_consumed == true`;
- `historical_author_write_path == "experiments/publication_lock.json"`;
- every other boolean permission flag in `permissions` is `false`.

In particular, the publication lock does **not** authorize:

- manuscript prose;
- `paper/main.tex`, `paper/math_commands.tex`, or `paper/references.bib`;
- TeX/BibTeX authoring generally;
- figures, assets, code, data, experiments, CAS, builds, PDFs, release,
  transport, submission, upload, repository push, messaging, or identity
  disclosure;
- Paper 23;
- any external effect.

I also verified `source_candidate_eligibility_contract` remains exact:

- `current_authorization == false`;
- exact future candidate paths are only
  `paper/main.tex`, `paper/math_commands.tex`, `paper/references.bib`;
- no fourth source path is authorized;
- all three candidate paths are absent now;
- a valid review at this gate creates only candidate eligibility, and only after
  a separate parent lifecycle transition.

## 7. Final review ledger

All required publication-lock checks passed simultaneously.

Recorded lock identity:

- SHA-256: `3d7eb3c7ef143a17c1ccdb82ece985a05c916b78c1ebe0591bca8af3c05ce6cd`
- bytes: `34222`
- LF: `1`

Recorded inventories:

- pre-write: `18` regular files / `4` child directories / `0` symlinks;
- post-review: `19` regular files / `4` child directories / `0` symlinks.

This file is the sole authorized write for the current review gate.

PUBLICATION_LOCK_PASS
