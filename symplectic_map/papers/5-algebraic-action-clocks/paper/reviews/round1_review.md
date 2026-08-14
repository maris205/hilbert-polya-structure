# Independent manuscript review — Round 1

**Paper:** *Normalized Algebraic Periodic Actions versus Prime Logarithms:
A Hénon Design Certificate*  
**Review date:** 2026-08-14  
**Review mode:** independent mathematical/manuscript review; no source,
result, figure, or manuscript file was edited  
**Verdict:** `MINOR_REVISION`  
**Overall score:** **7.4/10**  
**Confidence:** **0.96**

The mathematical certificate is correct under its stated hypotheses, and the
manuscript is unusually disciplined about normalization, branches, endpoint
terms, domain failures, and the distinction between proof and static
implementation audit. I found no counterexample to the stated theorems. The
current pre-review snapshot should nevertheless not be promoted to a final
paper unchanged: Figure 2 contains one false categorical cell for
`log|A|`, and its supposedly source-driven matrix is actually hard-coded in
the generator. This is a localized repair rather than a failure of the core
theorem.

For the present research sequence, the paper is a strong, useful design
certificate after the required repair. As a standalone mathematical article,
the main obstacle is not correctness but depth: the central implication is an
elementary finite-evaluation lemma followed by classical
Hermite--Lindemann. The manuscript's own `MERGE_IF_STANDALONE_DEPTH_IS_REQUIRED`
disposition is therefore appropriate.

## 1. What I checked

I read and cross-checked:

- `paper/manuscript.tex` and the complete 12-page
  `paper/paper_pre_review.pdf`;
- the proof, derivation, counterexample, independent counterexample, novelty,
  and citation-audit notes;
- source lock v3, experiment plan/tracker, all seven official result JSON
  records, the final result manifest, validation/result reports, and the
  complete pre-run code-review history;
- `CLAIM_MANIFEST.json`, `EXPERIMENT_PASSPORT.json`,
  `FIGURE_PACKAGE.json`, `PIPELINE_STATE.json`, paper configuration, and
  pre-review integrity report;
- all three figure masters and the figure-loader/generator source.

I independently performed only safe checks:

- final result manifest: **35/35 files hash correctly**;
- safe unit suite: **82 passed in 0.92 s**;
- deterministic paper build: **PASS**;
- rebuilt `manuscript.pdf` and frozen `paper_pre_review.pdf`: identical
  SHA-256
  `2e8f2cef866f06e219fb0d582aec8ad4a1403b26e61cf8f44549dbc4f8399742`;
- PDF: **12 pages**, letter size, no LaTeX warning/error/box-warning match in
  the final log, and all pages visually legible;
- no candidate parameter, candidate periodic point, candidate action, prime
  table, or Riemann-zero data was accessed.

A targeted independent literature search recovered the adjacent action-spectrum
and arithmetic-Hénon literature already represented in the bibliography but
no direct collision with the complete certificate. That negative result is
recall-limited and does not justify a priority claim. The current arXiv record
for *Hénon maps with many rational periodic points* remains a preprint and is
available as [arXiv:2412.01668](https://arxiv.org/abs/2412.01668); its current
record is v2, last revised 2025-07-08.

## 2. Mathematical assessment

| Component | Verdict | Independent check |
|---|---|---|
| Finite algebraic evaluation | PASS | A pole-free value of a `Qbar`-rational function at a `Qbar` point is algebraic, and a finite sum remains algebraic. Exactness is needed for the action interpretation, not for this closure step. |
| Hermite--Lindemann branch exclusion | PASS | If algebraic `A != 0` satisfied `exp(A)=beta` with algebraic nonzero `beta`, Hermite--Lindemann gives a contradiction. The `beta=0` no-log case and the unique algebraic `beta=1, A=0` case are correctly retained. |
| Algebraic post-conventions | PASS | Algebraic scale, average, repetition, real part, imaginary part, and modulus remain algebraic. The manuscript correctly does **not** infer anything about `log|A|` or `arg A`. |
| Autonomous gauge ledger | PASS | For `theta'=theta+dchi`, the representative is `G'=G+chi o F-chi+C`, and a closed period-`n` sum changes by `nC`. |
| Stepwise gauge ledger | PASS | Direct summation gives exactly `chi_n(P_n)-chi_0(P_0)+sum_j C_j`. Endpoint compatibility removes only the endpoint term; a defined algebraic mismatch preserves algebraicity. |
| Identity-map control | PASS | `F=id`, `theta=p dq`, and constant `G=log 2` give `dG=0` and one-step action `log 2`; this decisively refutes any map-only algebraicity claim once transcendental normalization is admitted. |
| Hénon exact potential and type-1 sign | PASS | Direct differentiation gives `H_a^*theta-theta=d(2q^3/3-pq)`, while `L_a=q^3/3-aq-qQ` satisfies the graph relations and `L_a=-G` on the graph. |
| Hénon periodic-coordinate algebraicity | PASS | The cyclic system has homogeneous leading equations `Q_j^2=0` at `Z=0`, hence no point at infinity. A positive-dimensional projective component cannot lie entirely in the affine chart, so the projective scheme is zero-dimensional and its affine coordinates are algebraic over `Q(a)`. The repeated-neighbor cases `n=1,2` are handled correctly. |
| `S`-integral refinement | PASS | At `v` outside extended `S`, a maximum `R>1` would give simultaneously `|q_j^2-a|_v=R^2` and `|q_{j+1}+q_{j-1}|_v<=R`. Thus coordinates are `S`-integral and only `3A_G` is uniformly certified. |
| Sharp denominator control | PASS | At `a=-1`, `(1,1)` is fixed and `A_G=-1/3`; the manuscript therefore correctly avoids claiming `A_G` itself is integral above 3. |
| Static audit versus theorem | PASS | The prose consistently assigns the all-period result to deduction and uses R020--R023 only to audit formula/indexing/implementation ledgers. No finite-period output is promoted to a proof. |

The core scope is also correct. The paper does not close `log|A|`, multiplier,
return-time, multivalued, closed-nonexact, transcendental-normalization,
infinite-place, adelic, or approximate clocks, and it does not make a
prime-orbit, trace-formula, zeta, determinant, quantization, or historical-first
claim.

## 3. Required repair before Round 2

### R1 — Correct the false `log|A|` cell in Figure 2

**Severity:** mandatory scientific correction; localized, so it supports
`MINOR_REVISION` rather than rejection.

In `paper/figures/gen_fig2_gauge_scope_matrix.py`, the row

```python
("$\\log|\\mathcal{A}|$", control["log_abs_nonclaim"], [1, 2, 0])
```

renders `CERTIFIED` under the column **algebraicity retained**. Read literally,
this says that `log|A|` is certified algebraic. That is false: when nonzero
algebraic `|A| != 1`, any logarithm is transcendental by the very theorem used
in the paper. It also directly conflicts with Remark 3.4, Figure 2's caption,
the source lock, and the limitations section, all of which place `log|A|`
outside the certificate.

At minimum, change the row so that the algebraicity cell is `STOP/OUT` (or
possibly `EDGE` if the column is redefined with unambiguous semantics). The
cleanest current-column repair is `[1, 0, 0]`. Also consider renaming the last
column from `prime-log conclusion` to `target-log conclusion`, because the
`beta=0` and `beta=1` rows are target-domain edge cases rather than prime
cases.

### R2 — Make Figure 2's status provenance real, not declarative

**Severity:** mandatory integrity repair tied to R1.

The manuscript and integrity package say that categorical figure statuses are
read from the frozen JSON package. Figure 2 does load the records, but all 27
cell codes are manually embedded in the generator. Its `expected` dictionary
checks only one selected field per row and does not derive or verify the three
displayed statuses. The incorrect `log|A|` cell is exactly the failure mode
this provenance claim is meant to prevent.

Either:

1. add explicit three-column categorical fields to a frozen/audited result
   record and derive the matrix from them; or
2. add a strict, semantically named mapping plus tests that assert every cell,
   and weaken the manuscript/package wording from “read from” to “generated
   from an audited mapping over” the frozen records.

After the repair, regenerate all Figure 2 formats, rebuild the manuscript,
update `FIGURE_PACKAGE.json` and all affected paper hashes/manifests, and rerun
the deterministic build and visual checks.

## 4. Minor repairs and clarifications

### M1 — Align the claim manifest's primary evidence with the paper's own proof policy

`CLAIM_MANIFEST.json` assigns `results/control_audit.json` as primary evidence
for C4 and `results/henon_static_audit.json` as primary evidence for C8. Yet the
paper repeatedly and correctly states that static JSON does not prove the
mathematics. For C4 and especially the all-period C8 valuation conclusion,
`notes/PROOF_PACKAGE.md` or the manuscript proof should be primary evidence;
the static JSON should be supporting implementation evidence. C6 can be
treated the same way for maximal consistency.

### M2 — Make the projective-dimension sentence maximally explicit

Theorem 5.1 is correct, but “a positive-dimensional projective component must
meet a hyperplane” should say “must meet the hyperplane `Z=0`” (or cite the
projective dimension theorem / proper-and-affine argument). The appendix gives
the intended statement more clearly. This is a presentation clarification,
not a proof gap.

### M3 — Preserve the arXiv identifier in the compiled bibliography

The BibTeX record contains `2412.01668`, but the `plainnat` output prints only
“Preprint,” so the identifier disappears from the PDF. Add an explicit
`howpublished` or note field that survives the chosen bibliography style,
preferably `arXiv:2412.01668 [math.DS], v2`. The paper's description of the
source as a preprint remains accurate.

### M4 — Reduce one small visual-density issue in Figure 1

The orange classification text above the normalization boxes is long and very
small in the compiled PDF. Wrap it into two lines or replace the machine-style
classification with a shorter human label. The rest of the 12-page PDF and
all three figures are visually clean.

### M5 — Keep the novelty disposition exactly as conservative as it is now

The novelty audit's standalone estimate of 3/10 is credible. The paper should
continue to describe its contribution as a normalization-aware provenance
certificate and Hénon case study, not a new transcendence theorem or historical
first. If submitted standalone, the likely objection is insufficient depth;
merging it into the broader obstruction synthesis is the strongest route.

## 5. Scores

| Criterion | Score | Comment |
|---|---:|---|
| Mathematical correctness | 9.0/10 | Core theorem, gauge ledger, Hénon proof, and denominator control pass independent attack. |
| Scope and claim discipline | 9.0/10 | Negative boundaries are unusually explicit and mostly consistent across prose and packages. |
| Reproducibility / provenance | 8.0/10 | Excellent source lock, tests, manifests, and deterministic build; reduced by the hard-coded false Figure 2 cell. |
| Clarity and presentation | 8.2/10 | Concise, readable, and visually clean apart from the noted matrix/label issues. |
| Standalone novelty | 3.0/10 | Correct but elementary mechanism; strongest as a design certificate in a synthesis. |
| Overall | **7.4/10** | Strong research-sequence artifact; minor revision required before final integrity. |

## 6. Round-2 acceptance gate

Round 2 can return `PASS` if and only if:

1. Figure 2 no longer certifies algebraicity of `log|A|`;
2. the figure-status provenance claim is made literally true or accurately
   weakened and tested;
3. affected figure/package/manuscript hashes are refreshed and close;
4. the claim manifest distinguishes deductive primary evidence from static
   implementation support;
5. the paper rebuilds cleanly and the full safe test suite still passes.

No new candidate orbit/action computation, prime data, zero data, or numerical
experiment is needed. The required work is a bounded manuscript/provenance
repair.
