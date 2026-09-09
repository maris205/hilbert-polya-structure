# C428 manuscript source, bibliography and evidence audit

2026-09-09 UTC. This is a bounded source/metadata and evidence-migration
audit for the first manuscript. It does not replace the frozen author
audit or independent IH6 review, both of which retain their original
historical status wording. Coordinator admission is a separate record.

## Actual bibliography and source ownership

| Key | Primary or actual local source and accessed scope | Claim supported and limit |
| --- | --- | --- |
| Pezda2002 | T. Pezda, *On cycles and orbits of polynomial mappings Z²→Z²*, Acta Mathematica et Informatica Universitatis Ostraviensis 10(1) (2002), 95–102. Complete DML-CZ metadata record reopened at https://dmlcz-proxy.ics.muni.cz/handle/10338.dmlcz/120574?show=full. At proof stage the author read selected original PDF text including definitions and Theorem 2.1; the independent source reviewer read the whole stream-extracted text, not all page images. | General planar period union `{1,2,3,4,6,8,9,12,16,18,24}` and integer-coefficient hypothesis. Not used to truncate our enumeration. Its local five-item `(*)`-cycle result is not a global positive-Jacobian Hénon theorem. No DOI verified; no invented DOI or expanded first name. |
| KimEtAl2025 | Hyeonggeun Kim, Holly Krieger, Mara-Ioana Postolache, Vivian Szeto, arXiv:2412.01668v2. Version page reopened: v1 2024-12-02, v2 2025-07-08. Primary v2 HTML reopened at Section 4.1, including explicit leading coefficient `1/d!`; displayed Section 5 Theorem 5.1 also read. Earlier proof/source checks read the introduction, Theorems A–B, Section 2.2 and Lemma 2.1, and the relevant long-cycle text. | Long integer cycles for a rational integer-valued family. Odd degree ≥3 gives a nonintegral leading coefficient, so this family is not in Z[t]. We cite the exact preprint version, not an unverified journal publication; HTML redraw date is not the version date. |
| deHenon2024 | Julia Xénelkis de Hénon, *Hénon maps: A list of open problems*, Arnold Mathematical Journal 10 (2024), 585–620, DOI 10.1007/s40598-024-00252-x. The official journal HTML's Section 11, attributed to P. Ingram, was reread through Conjectures 2–5 and Question 47. Springer publisher metadata independently reopened and verified title, credited author, volume, pages, publication date 2024-08-13 and DOI route. | Section 11 Conjecture 3 concerns `(y,y²+c+x)` over Q with rational periodic points. Its negative list is conjectural in that scope; this manuscript does not settle it. Whole-volume credited name is reproduced from the publication; Ingram's section ownership is explicit. |
| C412Working | Actual unpublished manuscript `../../../continuation_c409_c413_round2/papers/C412_integer_henon/main.tex`; title and introduction/classification statement checked, with prior complete input read and the independent source report. | Monic integral conservative quadratic rational classification, periods 1,2,3,4. No invented human author/journal/DOI, no re-audit of all old proof sections or old certificate execution. |
| C417Working | Actual unpublished manuscript `../../../continuation_c414_c418_round2/papers/C417_integral_cubic/main.tex`; actual title checked. Its `cubic_arithmetic/PROOF_PACKAGE.md` beginning and relevant source ownership reread; full old proof was independently read by the IH6 source reviewer and main reviewer. | Owns the positive spectrum and witnesses, secant/endpoint/affine/symbolic graph framework, plus a finer cubic point atlas and eleven-point bound not claimed here. Our unbounded-degree `h∈Z[t]` congruence reduction is the extension, not a new endpoint method. |
| IH6Working | Full six-file immutable author package in `../../continuation_round6/arithmetic/` read; scripts read as text, not executed during writing. | Origin and two exact computational dependencies. Historical author status is not silently rewritten as a new review; no external publication or DOI asserted. |
| IH6Review | Full review, CHECK_CONTRACT.md, independent_check.py, RUN_RECEIPT.md, 611-line RUN_OUTPUT.txt and SOURCE_SPOTCHECK.md previously read in full; code and receipts reread for manuscript migration. | One actual independently implemented reconstruction, with different algorithms and broader unpruned symbolic scope. AI-assisted current-team nonauthor review, nonblind, not human peer review or a formal proof assistant certificate. |

The bibliography lists only these actually cited references. All central
new arguments are in the article; the companion links identify frozen
proof/evidence bytes and do not substitute for the typeset analytic
reduction or pseudocode.

## Exact proof inputs rehashed during drafting

| File in `continuation_round6/arithmetic/` | SHA-256 |
| --- | --- |
| FROZEN_CONTRACTS.md | 8ad60e11f388bb8c1f21ba6a0e7a38113e10b818379552c618f51cf3b81750ce |
| PROOF_PACKAGE.md | 93f96bd6a49821111b0bcc04a3db8f34b2e030653597ae525d39940d1dbcf4a9 |
| check_integer_periods.py | 58fae6478013c34dcbca9a2b28bcacf675dfbcc28a84ac813197ecc7f1a5f2ef |
| check_large_diameter.py | d28a7f77e02b5d336ef790d6eeedfd809da4e139fb0d80eca53373911c2c69d4 |
| RUN_LOG.md | 2d2751b041c5a80539e985b2070c5e2acadd41bd6741f57a0b3c80fd8949043e |
| SOURCE_AUDIT.md | a1580e24d2978c3115b197e994b6a4b74fbfc0d202bc020f6954f812c3cb7e86 |

All six matched the actual independent execution's frozen CHECK_CONTRACT.
Independent checker SHA-256:
`babc84a2424ca6e45453e794a7bb9d7670c0c739c477c90f0b292d71ed40a5ba`.
Independent full-output SHA-256:
`9a3767996763dbff0ef049384af06f33bca14c271e71902a4311fc0be419f85a`.
Hashing checks input identity, not mathematics, and adds no mathematical
execution. No old file was changed.

## Exact-table provenance

- `tables/small_diameter.tex`: all ten D=0,...,9 rows from the independent
  RUN_RECEIPT and full output, cumulative values/spectra matched to author
  PROOF_PACKAGE Section 5. Per-sign exact-D restriction counts are not
  one-map point counts.
- `tables/large_author.tex`: all six rows of author PROOF_PACKAGE Section 6
  and its actual RUN_LOG. Generic period `{4}` means a period set, not a
  count of four cycles. No exception survives that output pruning.
- `tables/large_independent.tex`: all six unpruned rows of RUN_RECEIPT,
  totaling 9020 identity graphs and 512 exceptional graphs. The four
  generic cycles all have period four. Roots 10,11,12 were outputs of
  exact linear-equation solving, not preselected cutoffs.
- `tables/witnesses.tex`: all eleven original proof-package rows,
  independently checked with every native step and pairwise-distinct
  ordered states. The eight-cycle uses the sign -1, not a squared clock.

Tables are exact transcriptions of frozen records with their original
semantics, not newly simulated or fitted data. Pseudocode describes the
accepted algorithms; it was not run as a replacement certificate.

## Failures, limited checks and disclosure

The DOI redirect for the open-problems paper returned a safe-open error;
the direct Springer publisher URL succeeded, as did the official journal
HTML. A first local C417 locator guessed a nonexistent directory name;
`rg --files` resolved the actual `C417_integral_cubic` source. These are
source-location failures, not failed mathematical or LaTeX executions.
Some combined tool output was truncated; exact metadata and selected
sections were then requested separately. Earlier source-stage failures
remain recorded in the immutable author/reviewer audits.

No paid database, external model upload, model switch, GPU work,
external submission or new mathematical execution occurred. No claim
of exhaustive global priority search is made. Retraction databases,
venue reputation, competing interests, ORCID and commercial DOI
registry reconciliation were not specifically checked. The Kim et al.
version and local working manuscripts have no claimed journal DOI;
Pezda's DOI is unverified. AI preparation and current-team internal
review are disclosed without invented human authors or funding.

The two future manuscript-review rounds and coordinator's final fresh
deterministic build pair are not counted by this source audit.
