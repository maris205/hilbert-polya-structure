# Independent hostile review A — P141 Round 0

**Review date:** 2026-09-01 UTC  
**Reviewer role:** independent; the reviewer did not author the manuscript  
**Scope:** frozen-contract hostile reconstruction, edge-case attack,
canonical verifier replay, isolated rebuild, primary-source/owner subtraction,
current-vs-original PDF audit, and anonymity/metadata/font/page checks  
**Disposition:** **PASS** at the internal theorem/artifact gate  
**External status:** **HOLD_EXTERNAL**

No manuscript source, bibliography, verifier, canonical transcript, or PDF was
changed during this review. The only paper-local output of the review is this
file.

## 1. Severity-indexed findings

### Critical

**C-A-01 — owned support subtraction and weighted reverse-stick endpoint law:
PASS.** The support statement in `main.tex:91-112` is correctly treated as
owned and is used only as a labelled carrier. Reconstructing the greedy
process from the rightmost created vertex gives the stated endpoint masses in
`main.tex:121-147`:

```text
p_d = h_d product_(j in D, j>d) (1-h_j),
p_Z = product_(j in D) (1-h_j),
```

with `h_d=w_d/W_d`. The rightmost-zero and rightmost-dominant cases are the
only possibilities, and the prefix law survives by Plackett-Luce conditioning
plus memorylessness. An independently written full-permutation enumerator over
all creation strings with `n<=6` and all weight vectors in `{1,2}^n`
reproduced the reverse-stick law exactly.

**C-A-02 — inverse map, open-simplex realization, and nonidentifiability:
PASS.** The inverse formula in `main.tex:152-184`

```text
h_d = p_d / (p_Z + sum_(e in D, e<=d) p_e)
```

is the correct reverse-survival ratio. Reverse-stick telescoping yields the
denominator `product_(j in D, j>d)(1-h_j)`, so the inversion is exact and
label-sensitive. The realization step

```text
w_d = h_d W_(d-1)/(1-h_d)
```

correctly produces any positive hazard vector once the zero-position weights
are chosen.

The manuscript also distinguishes endpoint-law identifiability from full-rate
identifiability correctly. Independent hostile checks covered:

- `D=empty`: then `p_Z=1`, the simplex collapses to the singleton endpoint,
  and the formulas remain valid vacuously.
- zero vertices after the last dominant: their positive weights do not enter
  any hazard and therefore do not affect the endpoint law.
- arbitrary zero-position weights before or between dominants: these can be
  changed while adjusting later dominant weights to preserve the same hazards.

No hidden identifiability claim was found.

**C-A-03 — accepted-size PGF, repeated sizes, marginals, and nested zero
events: PASS.** The PGF statement in `main.tex:196-245` is exactly the support
mixture for `K=|I|`, not a new dynamic recursion. Distinct dominant vertices
can indeed produce the same endpoint size `k_d`, and the manuscript explicitly
states that those masses aggregate at the same coefficient. A direct repeated-
size hostile example is the creation word `0110`, where both dominant
positions produce size `2`; the coefficient aggregation is correct.

Independent permutation-based replay reproduced:

- the complete size PGF on all creation strings with `n<=6`,
- every dominant marginal `Pr(d in I)=p_d`,
- every zero marginal
  `Pr(i in I)=product_(j in D, j>i)(1-h_j)`,
- the nesting law `Pr(i,k in I)=Pr(i in I)` for `i<k` both zero.

No missing case was found.

**C-A-04 — separation of `J`, `K`, `R`, and `tau`, and the active-set Laplace
recursion: PASS.** The paper does not conflate the deterministic full scan
count `J=n`, the accepted-update count `K=|I|`, the full-priority span `R`,
or the continuous completion time `tau` (`main.tex:247-286`). The one-shot
priority coupling and the active-clock recursion are also kept distinct.

The recursion

```text
L_A(s) = [sum_(v in A) w_v L_(A\\N_A[v])(s)] / [s + sum_(v in A) w_v]
```

is the correct residual-state Laplace relation. An independently written
comparison between this recursion and full weighted-permutation enumeration on
all creation strings with `n<=5`, weights `(1,2,...,n)`, and `s in {1,2}`
matched exactly. The two-vertex clique firewall example is also numerically
correct:

```text
E[e^{-tau}] = 3/4,   E[e^{-R}] = 5/9,   E[(1/2)^K] = 1/2.
```

### Major

**M-A-01 — owner subtraction and folklore-risk framing: PASS.** The primary
owner boundary is internally coherent:

- Klivans owns the endpoint support on threshold graphs.
- Pippenger and later random-greedy MIS work own the process family.
- Plackett owns the weighted permutation law.

The manuscript does not attempt to reclaim those parts. The actual residual is
the threshold-specific weighted endpoint law, its hazard inversion/open-simplex
parametrization, and the PGF/marginal consequences. I found no direct source
inside the cited owner set that already prints this exact package, but the
proof is short enough that folklore risk remains substantial. Keeping
`HOLD_EXTERNAL` is therefore the correct status.

**M-A-02 — artifact stability and current-vs-original equivalence: PASS.**

- Fresh canonical replay: `cmp=0` against
  `code/verification_output.txt`; the replay again ended in `status=PASS` with
  `exact_assertions=750181`.
- Fresh isolated four-stage build from only `main.tex` and `references.bib`:
  all stages exited zero; the isolated PDF was byte-identical to both the
  working `main.pdf` and `main_round0_original.pdf`.
- Frozen artifact hashes audited during this review:
  - `main.tex`: `b312ca8becfcc405de8276195058b9876c8631ae0119b882a5bf4973db2d7f6e`
  - `references.bib`: `7a9bad554745322727fac587e773a862622e7f35d5e486bbf3e6f216376f1286`
  - `code/verify.py`: `25c3a0ba8d9f8134aeee42dd98176faedc84c5d7de8852afa527df8ae3b2b5e6`
  - `code/verification_output.txt`: `bcb2e2f68121a3c13e79e0987fcd1ee5e985b225f4a948357424ed70ee695502`
  - `main.pdf`: `e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6`
  - `main_round0_original.pdf`: `e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6`

### Minor

**N-A-01 — PDF/anonymity/page audit: PASS.**

- `pdfinfo`/`pdffonts` audit: four A4 pages, PDF 1.5, unencrypted, no forms,
  JavaScript, custom metadata, or metadata stream; title/author/subject/
  keywords metadata are blank; all 20 font rows are embedded, subsetted, and
  Unicode-mapped.
- `pdftotext` succeeded (`346` lines, `1875` words, `10965` bytes).
- All four pages were rasterized and inspected at 150 dpi. Endpoint formulas,
  inverse theorem, PGF, clock recursion, and references are legible; no
  clipping, overlap, or anonymization leak was found.
- Current and frozen round-0 PDFs are byte-identical, so this review found no
  silent artifact drift.

## 2. Final gate

There are **zero critical REPAIR items, zero major REPAIR items, and zero
minor REPAIR items**. The Round-0 manuscript passes this independent hostile
theorem/artifact review. This verdict does not clear novelty, priority,
authorship, posting, submission, owner contact, or public release. The
mandatory external status remains **HOLD_EXTERNAL**.
