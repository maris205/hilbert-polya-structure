# P32 -- ARS Stage 2 manuscript audit

Status: **Stage 2 WRITE complete; Stage 2.5 awaiting explicit user confirmation.**
This audit claims neither scientific execution, passage-level verification,
peer-review acceptance, nor Route-A/Route-B promotion.

## Deliverables and integrity

| File | SHA-256 |
|---|---|
| `manuscript.tex` | `246545c14b5d7c3e43f7aad8b421b254ded52bf82efc1182b4c4bfe3ef6232c9` |
| `references.bib` | `e699c96196377892d3aa1f280e6a5117001c3cec37a511a3d1c08fdc52127de9` |
| `paper.pdf` | `aa951b643bc0080ca1473449b0574693701266c6b84a110f5b8a04ec9929c183` |
| `notes/stage2_claim_intent_manifest.json` | `9b410195e7423304ba7bbb0c45342729dea1a79eb0a1fb5a6c53131d41b0db3a` |
| `notes/stage2_bib_key_map.json` | `6a6d2ca1e3536b65d008800e63d2aaa99671e1693594a2a29828142fcb9748c4` |
| `notes/stage2_build_receipt.json` | `3993b773153d2cc6fc9a16cedb8e62a82f4207e842a3f760c0b02c9f29c49ee4` |
| `notes/stage2_independent_recheck.md` | `87b5e8ae5db67af5ec20436321f2fdae67759f9d550d5dcdec1707d1b1d54365` |

- PDF: **13 pages**, 252668 bytes.
- Isolated build: LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX; receipt verdict `PASS`.
- Bibliography: natbib with plainnat numeric output.
- Build log: no fatal error, undefined citation/reference, missing glyph, or overfull box.

## Length, structure, and citation closure

| Check | Result |
|---|---:|
| English body | **4442 words** |
| English abstract | **229 words** |
| Traditional-Chinese abstract | **350 Han characters** |
| Keywords | **6 English; 6 Traditional Chinese** |
| Stage-2 ClaimIntents | **8/8** |
| Bibliography | **26/26 entries; 26 unique cited; 0 missing; 0 orphan** |
| Citation commands / key occurrences | **8 / 26** |
| Adjacent anchor-none markers | **8** |

The manuscript contains the author block, independent English and
Traditional-Chinese abstracts, introduction and research question, frozen
object and owner conventions, related literature, executed closed-corpus
methodology, certificate/proof-method architecture, synthesis findings,
reproducibility interface, discussion, dedicated limitations, future work,
conclusion, and all publication declarations.

## Article-level result and boundary

The article makes higher-content and zero-content factors the first falsification targets under the exact 1/N time and 1/N^3 logarithmic normalizations. Content one is contingent and secondary; formal objects, panels, tails, and limits remain unresolved.

P32-S13 remains PLAUSIBLE/background-only; P32-S06 remains a presentation-unmapped preprint; P32-S17 remains correction-limited.

The independent hash-bound recheck covers all eight ClaimIntents and reports
no unresolved Blocker or Major finding. Every source-dependent statement stays
inside the frozen corpus; every citation remains `anchor:none`, and
claim-to-passage faithfulness remains `INCONCLUSIVE`. No direct source
quotation or invented locator is used.

## Route and scientific state

Generic Route-A A1--A2 preparation; A0 unavailable; formal tuple UNASSIGNED; Route B closed.

`SCIENTIFIC_EXECUTION=NOT_RUN`; `NEW_RETRIEVAL=NO`;
`CANONICAL_RESULT_REFRESH=NO`; `FORMAL_ROUTE_A_TUPLE=UNASSIGNED`;
`ROUTE_B_INVOCATION=false`; `STAGE2_5_INTEGRITY=NOT_STARTED`.

**Audit conclusion:** the complete Stage-2 article package is internally
reproducible and ready for the separate Stage-2.5 confirmation gate.
