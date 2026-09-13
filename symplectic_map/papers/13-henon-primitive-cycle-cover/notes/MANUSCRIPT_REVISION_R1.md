# Manuscript Revision Receipt — Round 1

## 1. Revision status and authority

- Revision status: `R1_BOUNDED_REVISION_COMPLETE`
- Revision rounds used: **one**
- Authoring authority: sole authorized Round-1 revision author
- Frozen review:
  `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md`
- Frozen review SHA-256:
  `aaa77a37a8d8a8fccedd18073f346312b1ea0245447bbf1b0f5c60095809848c`
- Frozen review size: 22,525 bytes; 353 lines
- Frozen disposition: `BOUNDED_REVISION_REQUIRED`

This revision implements exactly R1-P1--R1-P3, R1-C1--R1-C2,
R1-E1--R1-E3, and R1-B1.  It does not implement either nonblocking note,
does not change a theorem statement, and does not authorize finalization.

## 2. Source bindings before and after the revision

| Source | State | SHA-256 | Bytes | Lines |
|---|---|---|---:|---:|
| `paper/main.tex` | before | `5547882d589f9a8920880994acc812248d0e134516937b43f89b30ea008ede0c` | 79,207 | 1,859 |
| `paper/main.tex` | after | `f62f72ad129bc371d0e76d1daf48b0a2df82cf60d0d1e750d6c0f049047539ce` | 80,689 | 1,895 |
| `paper/references.bib` | before | `c792a29b55ad6016460fd42cca7d85554fc8d08836e08670afa4731b5fcd041c` | 7,851 | 244 |
| `paper/references.bib` | after | `005edd30410ffd8b9b9851e9008636aed9bcddba3195af550bd6daed0529a19b` | 8,175 | 256 |

The architecture source was not edited:

| Unchanged source | SHA-256 | Bytes |
|---|---|---:|
| `paper/figures/architecture.tex` | `eabb9c99296c39a3744a57aaa7484522d20175e42dc7577a6e658dc732fed9b9` | 3,185 |

## 3. Required-repair ledger

| Repair | Count | Revised source location | Implemented repair |
|---|---:|---|---|
| R1-P1 | 2 | `paper/main.tex:465-476`, `1178-1204` | The main proof now cites the explicit Henselian idempotent-extension argument.  The appendix shows that the lifted scalar factor is a direct subfactor of the generic actual-period block and that both sides have dimension `nu`, forcing equality. |
| R1-P2 | 1 | `paper/main.tex:594-602` | The dynatomic relation is stated after tensoring with `Q(c)`; finite flatness makes `S/aS` flat and torsion-free over `Q[c]`; injectivity of localization descends the relation before the map from `D_n` is defined. |
| R1-P3 | 1 | `paper/main.tex:936-940` | The arithmetic image is stated to contain the geometric `S_r` and to lie in the ambient `S_r`, hence to equal `S_r`. |
| R1-C1 | 2 | `paper/main.tex:155-158`, `1067-1074` | Both Cantat--Dujardin descriptions now carry the fixed-degree qualification. |
| R1-C2 | 1 | `paper/main.tex:1079-1084` | The Endler--Gallas carrier attribution is explicitly restricted to the quadratic Hénon map. |
| R1-E1 | 1 | `paper/main.tex:381` | The type-mismatched map statement was replaced by “`B_n` is finite flat over `A`.” |
| R1-E2 | 1 | `paper/main.tex:531-533` | `\etaleness{} for` restores the interword space. |
| R1-E3 | 1 | `paper/main.tex:550-555` | The undefined `Q(Y_1(n))` notation was removed; the residue field is stated as `Frac(D_n)`. |
| R1-B1 | 12/12 | `paper/references.bib:162-256` | Every existing Stacks entry now has protected title `{{The Stacks Project}}` and `year={n.d.}`; all twelve keys, tag URLs, and access notes are unchanged. |

No definition of `tau` or `rho`, PC hierarchy, mandatory bounded-audit
paragraph, architecture caption, citation key, figure byte, or theorem
statement was changed.

## 4. Exact-diff and consistency checks

- A read-only in-memory reversal of exactly the ten intended text
  replacements in the revised `paper/main.tex` reproduced the before hash
  `5547882d589f9a8920880994acc812248d0e134516937b43f89b30ea008ede0c`.
- A read-only in-memory reversal of exactly the twelve Stacks title/year
  mutations reproduced the before bibliography hash
  `c792a29b55ad6016460fd42cca7d85554fc8d08836e08670afa4731b5fcd041c`.
- Stacks mutation audit: 12 entries, 12 protected titles, 12 `n.d.` years,
  12 unchanged authors, 12 exact tag/URL/access-note matches; result 12/12.
- Citations: 50 citation commands, 26 unique cited keys, and 26 unique
  bibliography keys; no missing or uncited key.
- Cross-references: 64 unique labels, no duplicate label, and no unresolved
  `ref` or `eqref` target.
- Syntax checks: main-source brace balance zero, bibliography brace balance
  zero, and LaTeX environment stack empty with no mismatch.
- Contract counts: mandatory bounded-audit opening 1, `RESULT_PASS` 1,
  architecture figure 1, architecture input 1, exact caption 1, tables 0,
  and each of `thm:A`, `thm:B`, and `prop:C` 1.
- Priority, internal-workflow, placeholder, and `[VERIFY]` ban scan: zero
  matches.

## 5. Unchanged Round-0 build bindings

No build output or Round-0 receipt was edited.

| Unchanged Round-0 file | SHA-256 | Bytes |
|---|---|---:|
| `paper/main.aux` | `176afa439699fd0fe5ee4ac3e5ec0c7a888825acf53c29b5a1df7fcacb1b6337` | 16,708 |
| `paper/main.bbl` | `83aaef938617f4c1f6b7b4ed9bf6b6a49653b11a4ef6692943da6f0eb7797b66` | 7,917 |
| `paper/main.blg` | `f0120fd2bfd5eb0bdaadd6154df485d7ed3f84549a8a538251cca2f67af4e139` | 1,364 |
| `paper/main.log` | `4f17382ee5a41a291e2209d7e3b1f25316383651b06bf519501e8dde7f9d9232` | 38,628 |
| `paper/main.out` | `838757a680eeb5ef6b3115a65e94801212acb9659c8ae2465e3184db40920af0` | 12,541 |
| `paper/main.pdf` | `f9bb3e4c08215e91d0baf3e278ee1802b88a1d77c8e08515b61b51fb5850118d` | 517,616 |
| `paper/main_round0.pdf` | `f9bb3e4c08215e91d0baf3e278ee1802b88a1d77c8e08515b61b51fb5850118d` | 517,616 |
| `paper/BUILD_RECEIPT_R0.json` | `1e05beda50a07fc120c40d4568aa54f9bf51b4c212682b3248a30efb78c38548` | 4,942 |

## 6. Write and execution inventory

Authorized writes in this revision:

1. `paper/main.tex`
2. `paper/references.bib`
3. `notes/MANUSCRIPT_REVISION_R1.md`

All writes used `apply_patch`.  No figure, build output, governance file, or
other source was written.  No LaTeX, BibTeX, PDF, or build command was run.
No scientific program, symbolic experiment, registered route, runtime
adjudicator, network retrieval, or evidence recomputation was invoked.

The receipt's final SHA-256 is intentionally reported externally after this
single write; a file cannot contain a stable binding to its own final hash.
