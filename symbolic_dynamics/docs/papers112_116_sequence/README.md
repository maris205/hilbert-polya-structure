# P112--P116 Route-A sequence

Status: **FINAL QA PASS / INTERNAL FREEZE / EXTERNAL HOLD**.

This batch continues the breadth-first Route-A search for distinct dynamical
systems with early exact signals.  Forty-eight candidate maps were screened;
five different phase/update types survived to theorem-bearing short papers.
Every final claim boundary below is post-review and owner-subtracted.

| paper | phase space and action | concrete post-review advance |
|---:|---|---|
| [P112](../../papers/112-tournament-score-upset-reversal/README.md) | labelled tournaments; synchronously correct score upsets | exact score-energy increment, permanent score-block factorization, recursive pointwise depth with `tau<=n-1`, and fixed ordered sums of regular tournaments |
| [P113](../../papers/113-principal-hook-partition-dynamics/README.md) | partitions of `n`; replace the diagram by its principal-hook partition | exact first-gap increment, pointwise depth bound, and sharp global depth `floor(n/2)` attained by balanced two-row states |
| [P114](../../papers/114-rooted-forest-leaf-peeling/README.md) | rooted forests on subsets; delete all nonroot leaves in parallel | after extensive classical subtraction, an endpoint-indexed finite-map assembly and an elementary target-local `(m,s)` predecessor formula |
| [P115](../../papers/115-bounded-cartier-operator-dynamics/README.md) | bounded finite-field polynomials; Cartier coefficient selection with inverse Frobenius | explicit index-chain product conjugacy, full weak components and attached trees, exact temporal/fibre laws, lattice depth limit, and parameter recovery |
| [P116](../../papers/116-max-plus-switching-induced-growth/README.md) | iid products of two explicit max-plus matrices; maximum-entry observable | five-gap/three-state reward law, exact reset classification, rational drift/variance, cubic pressure, exact support/extremes, and temperature constants |

## Final internal freeze

| paper | pages | PDF bytes | exact assertions | hostile audit | final gate |
|---:|---:|---:|---:|---|---|
| P112 | 8 | 332,780 | 1,677,508 | [A](../../papers/112-tournament-score-upset-reversal/HOSTILE_REVIEW_A.md), [B](../../papers/112-tournament-score-upset-reversal/HOSTILE_REVIEW_B.md), [decision](../../papers/112-tournament-score-upset-reversal/HOSTILE_REVIEW.md) | [PASS](../../papers/112-tournament-score-upset-reversal/FINAL_QA.md) |
| P113 | 4 | 325,001 | 10,110,035 | [A](../../papers/113-principal-hook-partition-dynamics/HOSTILE_REVIEW_A.md), [B](../../papers/113-principal-hook-partition-dynamics/HOSTILE_REVIEW_B.md), [decision](../../papers/113-principal-hook-partition-dynamics/HOSTILE_REVIEW.md) | [PASS](../../papers/113-principal-hook-partition-dynamics/FINAL_QA.md) |
| P114 | 3 | 318,137 | 400,105 | [A](../../papers/114-rooted-forest-leaf-peeling/HOSTILE_REVIEW_A.md), [B](../../papers/114-rooted-forest-leaf-peeling/HOSTILE_REVIEW_B.md), [decision](../../papers/114-rooted-forest-leaf-peeling/HOSTILE_REVIEW.md) | [PASS](../../papers/114-rooted-forest-leaf-peeling/FINAL_QA.md) |
| P115 | 7 | 397,625 | 2,259,162 | [A](../../papers/115-bounded-cartier-operator-dynamics/HOSTILE_REVIEW_A.md), [B](../../papers/115-bounded-cartier-operator-dynamics/HOSTILE_REVIEW_B.md), [decision](../../papers/115-bounded-cartier-operator-dynamics/HOSTILE_REVIEW.md) | [PASS](../../papers/115-bounded-cartier-operator-dynamics/FINAL_QA.md) |
| P116 | 10 | 419,711 | 1,183,356 | [A](../../papers/116-max-plus-switching-induced-growth/HOSTILE_REVIEW_A.md), [B](../../papers/116-max-plus-switching-induced-growth/HOSTILE_REVIEW_B.md), [decision](../../papers/116-max-plus-switching-induced-growth/HOSTILE_REVIEW.md) | [PASS](../../papers/116-max-plus-switching-induced-growth/FINAL_QA.md) |
| **total** | **32** | **1,793,254** | **15,630,166** | **10 independent nonauthor reviews** | **5/5 PASS** |

The assertion total is the sum of heterogeneous deterministic checks, not a
proof count or paper ranking.  Consistent `pdftotext -layout` extraction gives
135,614 bytes in 1,838 lines.  The five PDFs contain 126/126 embedded,
subsetted, Unicode-mapped font records; all 51 paper-local bibliography
entries are cited and resolved.  Paper-local manifests cover 84/84 frozen
files.

## Evidence map

| paper | manuscript | exact control | evidence and seal |
|---:|---|---|---|
| P112 | [source](../../papers/112-tournament-score-upset-reversal/main.tex), [PDF](../../papers/112-tournament-score-upset-reversal/main.pdf) | [verifier](../../papers/112-tournament-score-upset-reversal/code/verify.py), [stdout](../../papers/112-tournament-score-upset-reversal/code/verification_output.txt) | [claims](../../papers/112-tournament-score-upset-reversal/CLAIMS_EVIDENCE.md), [reviews](../../papers/112-tournament-score-upset-reversal/HOSTILE_REVIEW.md), [QA](../../papers/112-tournament-score-upset-reversal/FINAL_QA.md), [seal](../../papers/112-tournament-score-upset-reversal/SHA256SUMS) |
| P113 | [source](../../papers/113-principal-hook-partition-dynamics/main.tex), [PDF](../../papers/113-principal-hook-partition-dynamics/main.pdf) | [verifier](../../papers/113-principal-hook-partition-dynamics/code/verify.py), [stdout](../../papers/113-principal-hook-partition-dynamics/code/verification_output.txt) | [claims](../../papers/113-principal-hook-partition-dynamics/CLAIMS_EVIDENCE.md), [reviews](../../papers/113-principal-hook-partition-dynamics/HOSTILE_REVIEW.md), [QA](../../papers/113-principal-hook-partition-dynamics/FINAL_QA.md), [seal](../../papers/113-principal-hook-partition-dynamics/SHA256SUMS) |
| P114 | [source](../../papers/114-rooted-forest-leaf-peeling/main.tex), [PDF](../../papers/114-rooted-forest-leaf-peeling/main.pdf) | [verifier](../../papers/114-rooted-forest-leaf-peeling/code/verify.py), [stdout](../../papers/114-rooted-forest-leaf-peeling/code/verification_output.txt) | [claims](../../papers/114-rooted-forest-leaf-peeling/CLAIMS_EVIDENCE.md), [reviews](../../papers/114-rooted-forest-leaf-peeling/HOSTILE_REVIEW.md), [QA](../../papers/114-rooted-forest-leaf-peeling/FINAL_QA.md), [seal](../../papers/114-rooted-forest-leaf-peeling/SHA256SUMS) |
| P115 | [source](../../papers/115-bounded-cartier-operator-dynamics/main.tex), [PDF](../../papers/115-bounded-cartier-operator-dynamics/main.pdf) | [verifier](../../papers/115-bounded-cartier-operator-dynamics/code/verify.py), [stdout](../../papers/115-bounded-cartier-operator-dynamics/code/verification_output.txt) | [claims](../../papers/115-bounded-cartier-operator-dynamics/CLAIMS_EVIDENCE.md), [reviews](../../papers/115-bounded-cartier-operator-dynamics/HOSTILE_REVIEW.md), [QA](../../papers/115-bounded-cartier-operator-dynamics/FINAL_QA.md), [seal](../../papers/115-bounded-cartier-operator-dynamics/SHA256SUMS) |
| P116 | [source](../../papers/116-max-plus-switching-induced-growth/main.tex), [PDF](../../papers/116-max-plus-switching-induced-growth/main.pdf) | [verifier](../../papers/116-max-plus-switching-induced-growth/code/verify.py), [stdout](../../papers/116-max-plus-switching-induced-growth/code/verify.out) | [claims](../../papers/116-max-plus-switching-induced-growth/CLAIMS_EVIDENCE.md), [reviews](../../papers/116-max-plus-switching-induced-growth/HOSTILE_REVIEW.md), [QA](../../papers/116-max-plus-switching-induced-growth/FINAL_QA.md), [seal](../../papers/116-max-plus-switching-induced-growth/SHA256SUMS) |

## Selection and release boundary

Stage 1 tested 48 concrete dynamics with 4,456,612 scouting assertions.  That
historical total is separate from the canonical paper total above.  False or
overwide signals were retained in the kill ledger: tournament idempotence,
naive principal-hook deepest-shell rules, a reset-free interpretation of
P116, and numerous direct-owner or same-engine candidates did not survive.

The [Stage-1 report](STAGE1_REPORT.md), [contracts](phase1/THEOREM_CONTRACTS.md),
[kill ledger](phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md), [source report](phase2/SOURCE_VERIFICATION_REPORT.md),
[Stage-2 report](STAGE2_REPORT.md), [hostile-audit report](STAGE2_5_REPORT.md),
[final QA report](FINAL_QA_REPORT.md), [Material Passport](MATERIAL_PASSPORT.md),
and [canonical PDF manifest](CANONICAL_PDF_MANIFEST.sha256) retain the batch
provenance.

Every paper remains anonymous and internal.  Public posting, submission,
specialist contact, venue selection, and novelty or priority statements remain
**HOLD**.
