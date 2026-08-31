# Paper 27 — Stage 4.5 Round 2 originality and failure-mode audit

Audit date: **2026-08-31**  
Operating mode: **Mode 2 — final-check**

Fresh successful body search coverage: **39/78 (50.0%)**; every major section represented; changed paragraphs successful: **20/20**.

The recorded 8–12-word quoted queries, accessible engine, HTTP state, and reviewed top-result titles/URLs/snippets are in `stage4_5_round2_originality_failure_mode_audit.json`. Access failures are excluded from the numerator. Paragraph 71 is explicitly retained as a failed search because its quoted track returned HTTP 202 with no result cards; paragraph 75 is the fresh replacement sample and has two HTTP-200, non-empty top-result tracks. No exact external or Liang Wang self-repetition match requiring attribution was detected in the successful recorded top results.

The comparison is limited to publicly searchable material. It is not Turnitin, iThenticate, Crossref Similarity Check, or another licensed professional corpus; it cannot establish global originality, detect all translated reuse, or cover inaccessible full text. The Liang Wang check is likewise a bounded searchable-subset comparison, not a self-plagiarism certificate.

| ARS failure mode | status | recorded evidence |
|---|---|---|
| Implementation bug passing AI self-review | CLEAR | 61-test fresh replay; hash-locked manifests; fail-closed tests |
| Hallucinated citation | CLEAR | 5/5 bibliography resolution; 5/5 citation contexts; fresh authoritative source snapshot |
| Hallucinated experimental result | CLEAR | 14/14 Phase-C provenance alignment; 61 unit and 12 verify/support tests; existing receipts and canonical-result hashes |
| Shortcut reliance | CLEAR | full claim-registry coverage; exact protected-surface replay; separate proof/provenance/citation/originality checks |
| Implementation bug reframed as novel insight | CLEAR | adversarial/fail-closed tests; bounded contribution and limitation language; full-bundle E6 review |
| Methodology fabrication | CLEAR | recorded code/config/test commands; hash-bound provenance and receipts; exact C4 disclosure boundary |
| Frame-lock at early pipeline stage | CLEAR | Stage-1 through Stage-4-prime chain; reviewer roadmaps and author adjudications; Route re-evaluation without promotion |

Modes 1/3/5/6 are supported by actual logs, configurations, tests, provenance, and receipts. Any `SUSPECTED` result, or insufficient evidence in Modes 1/3/5/6, would block rather than be reported as CLEAR.
