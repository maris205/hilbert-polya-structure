# Independent hostile review B - P141 Round 1 freeze

**Review date:** 2026-09-01 UTC  
**Reviewer role:** independent hostile reviewer; the reviewer did not author the manuscript  
**Scope:** frozen-contract alignment, independent theorem reconstruction, independent exact controls, canonical verifier byte replay, isolated rebuild, source/owner/collision audit, owner-thin framing audit against the frozen batch owner review, and all-page/font/metadata/anonymity audit  
**Round-A delta:** `main.pdf`, `main_round0_original.pdf`, and `main_round1.pdf` are byte-identical, so Round B is reviewing an unchanged manuscript artifact  
**Disposition:** **REPAIR** before the internal owner-summary gate  
**External status:** **HOLD_EXTERNAL**

No manuscript source, bibliography, verifier, canonical stdout, or PDF artifact
was edited during this review. The only paper-local output of Round B is this
file.

## 1. Severity-indexed findings

### Critical

**C-B-01 - owned support subtraction and weighted reverse-stick endpoint law
survive independent reattack: PASS.** The manuscript still places the support
lemma behind an explicit zero-credit boundary (`main.tex:57-66,97-112`) and
states the residual theorem only for the weighted endpoint masses
(`main.tex:121-147`). Reconstructing the process from the rightmost created
vertex again gives the stated alternatives: a terminal zero is forced, while a
terminal one either wins its prefix race with probability `w_d/W_d` or is
deleted after an earlier acceptance. An independently written script that did
not import `code/verify.py` checked 2,515 exact conditions across literal
active-set recursion, hazard inversion, marginals, nesting, simplex
realization, and clock recursions; on every creation string of size at most `6`
and several independent weight profiles it reproduced the reverse-stick law
exactly. No support/process conflation appeared.

**C-B-02 - hazard inversion, nonidentifiability, accepted-size PGF, and
vertex laws remain correct: PASS.** The inverse and realization theorem in
`main.tex:152-184`, the nonidentifiability remark in `main.tex:186-194`, and
the size/marginal formulas in `main.tex:196-245` survive hostile boundary
probes. The denominator in the inverse formula is exactly the reverse-survival
factor, so every dominant hazard is recovered from labelled endpoint masses.
The realization step correctly permits arbitrary positive zero-position weights,
which preserves the distinction between endpoint-law identifiability and
vertex-rate identifiability. The same independent script verified all dominant
hazard recoveries and all vertex marginals on the finite grid, plus the zero
nesting law `Pr(i,k in I)=Pr(i in I)` for `i<k` both zero. As an additional
repeated-size control, on the creation word `00110` with weights `(1,2,3,4,5)`
the two dominant endpoints have the same accepted size and their masses
aggregate at the same PGF coefficient exactly as stated in `main.tex:204-221`.

**C-B-03 - the firewall between `J`, `K`, `R`, and `tau` and the
state-dependent Laplace recursion survive reattack: PASS.** The manuscript does
not collapse the full scan count, accepted-update count, full-priority span, or
continuous completion time (`main.tex:247-286`). The active-set recursion
`L_A(s)` is the correct first-ring decomposition, not a substitution into the
size PGF. The independent script matched this recursion against full weighted
permutation enumeration for every creation string of size at most `5`, weights
`(1,2,...,n)`, and `s in {1,2}`. The two-vertex clique firewall values are
still exact:

```text
E[e^{-tau}] = 3/4,   E[e^{-R}] = 5/9,   E[(1/2)^K] = 1/2.
```

No counterexample to the theorem package or to the statistic-separation claims
appeared.

### Major

**M-B-01 - package-level owner-thin repair is still open: REPAIR REQUIRED.**
The frozen batch owner audit now classifies P141 as owner-thin and explicitly
requires narrower package framing
(`docs/papers137_141_sequence/phase1/FINAL_OWNER_AUDIT.md:240-263`): the
weighted endpoint law is a very short conditioning corollary of owned support
plus owned weighted-order machinery, its corollaries are algebraically
immediate, the package is plausibly folklore, and the bounded non-hit is not
novelty or ownership clearance.

The manuscript text itself is already largely compliant. `main.tex` narrows the
note to a residual exact-law calculation (`main.tex:63-66`), states that finite
controls provide no novelty evidence (`main.tex:314-317`), marks the support,
process, weighted orders, and exponential races as fully owned
(`main.tex:319-323`), and explicitly says the proof may be unpublished folklore
(`main.tex:322-324`). `NARRATIVE_REPORT.md:41-46` and
`PAPER_PLAN.md:7-9,35-47` carry the same guardrails.

The paper-local summary ledger, however, is not synchronized to that owner
audit. `README.md:3-23` still presents an unconditional `ROUND-A PASS /
GO_INTERNAL` package summary; `IMPROVEMENT_LOG.md:5-27` says the review
disposition was `PASS / GO_INTERNAL / HOLD_EXTERNAL` and that no repair was
made; `CLAIMS_EVIDENCE.md:3-12,22-27` records a clean pass without marking the
reverse-stick package as owner-thin/folklore-risky; and `FINAL_QA.md:3-15,44-45`
states that no paper-source repair was warranted. Those summaries make the
package look owner-cleaner than the frozen owner audit allows.

**Required repair scope:** documentation/status sync only.

- In `README.md`, `IMPROVEMENT_LOG.md`, `CLAIMS_EVIDENCE.md`, and `FINAL_QA.md`,
  replace the unconditional Round-A PASS framing with an owner-thin internal
  status that matches the batch audit.
- State explicitly in those package summaries that this is a specialized
  exact-law note on a fully owned support/process and that Theorem 3.1 and its
  corollaries are owner-thin and folklore-risky.
- State explicitly that the bounded non-hit is not novelty, priority, or owner
  clearance.
- No theorem rewrite is required by this finding unless the authors want every
  file to use identical phrasing; the current manuscript body is already narrow
  enough.

**M-B-02 - manuscript-level owner subtraction and collision firewall: PASS.**
Once the stale package summaries above are set aside, the source manuscript
itself respects the owner boundary. It gives zero credit to Klivans's support,
generic RSA/random-greedy MIS, and Plackett ordering
(`main.tex:59-66,319-323`), and the batch owner audit records no local
collision with the nearest internal graph-system neighbor P106
(`docs/papers137_141_sequence/phase1/FINAL_OWNER_AUDIT.md:252-256`). I found
no additional source-ownership broadening in the current manuscript body.

**M-B-03 - canonical verifier replay, isolated build, and frozen-byte identity:
PASS.** A fresh replay of `PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py`
compared byte for byte with `code/verification_output.txt` (`cmp=0`) and again
reported `exact_assertions=750181` with `status=PASS`. A fresh four-stage
isolated build from only `main.tex` and `references.bib` exited zero on all
stages and reproduced the current PDF byte for byte. The current artifact
hashes are:

| artifact | SHA-256 |
|---|---|
| `main.tex` | `b312ca8becfcc405de8276195058b9876c8631ae0119b882a5bf4973db2d7f6e` |
| `references.bib` | `7a9bad554745322727fac587e773a862622e7f35d5e486bbf3e6f216376f1286` |
| `code/verify.py` | `25c3a0ba8d9f8134aeee42dd98176faedc84c5d7de8852afa527df8ae3b2b5e6` |
| `code/verification_output.txt` | `bcb2e2f68121a3c13e79e0987fcd1ee5e985b225f4a948357424ed70ee695502` |
| `main.pdf` | `e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6` |
| `main_round0_original.pdf` | `e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6` |
| `main_round1.pdf` | `e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6` |

### Minor

**N-B-01 - page, font, metadata, and anonymity audit: PASS.** `pdfinfo` on
`main_round1.pdf` reports four A4 pages, PDF 1.5, no encryption, no forms, and
no JavaScript. `Title`, `Author`, `Subject`, and `Keywords` metadata are
blank. `pdffonts` lists 20 rows, all embedded and subsetted. A raw `strings`
scan found no local path, workspace name, hostname, or machine identifier. All
four pages were rasterized at 150 dpi and visually inspected; formulas,
references, and the table are legible, the only visible author string is
`Anonymous`, and no clipping, overlap, or anonymity leak appeared.

## 2. Final gate

There are **zero critical REPAIR items, one major REPAIR item, and zero minor
REPAIR items**. The core theorem package and artifact mechanics pass this
independent hostile reattack, but the paper-local owner framing is not yet
synchronized to the frozen owner audit. The correct current disposition is
**REPAIR / HOLD_EXTERNAL**.
