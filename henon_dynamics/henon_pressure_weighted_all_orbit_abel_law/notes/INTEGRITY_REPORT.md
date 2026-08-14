# Final integrity report

Date: 2026-08-14

Mode: final verification

Verdict: **PASS**

## Artifact and reproducibility gates

- required `README.md`, `paper/`, `code/`, `experiments/`, `results/` and
  `notes/`: PASS;
- final LaTeX PDF: PASS, 9 pages, author metadata `Liang Wang`;
- final PDF equals the round-two manuscript: PASS;
- exact producer, separate checker and 11 unit tests: PASS;
- dependency locks: 7/7; finite packet rows: 280; adversarial mutations: 9/9;
- Route-A evaluation: PASS with claim ceiling
  `(A1_WEAK, A2_FAIL, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)`;
- Route B: correctly refused because no operator, domain or determinant exists.

## High-impact claim verification

| Claim | Evidence | Verdict |
|---|---|---|
| orbitwise Mahler-height packet law | reciprocal embedding identity, Yamada unit-circle branch and exact norms | VERIFIED |
| coefficient is full Mahler height, not physical multiplier | exact period-one counter-sentinel and independent root calculation | VERIFIED |
| pressure-weighted all-orbit exchange | orbitwise limit plus P51 positive normal majorant | VERIFIED |
| joint orbit--index law is \(\pi_\sigma\otimes\Gamma(2,1)\) | Laplace transform, tightness and all-orbit exchange | VERIFIED |
| no norm or weak tagged boundary | coordinate functionals versus positive mass functional | VERIFIED |
| determinant/operator/critical continuation remain open | theorem ledger, hostile review and Route-A firewall | VERIFIED |

## Reference and citation audit

All six bibliography entries are cited and every citation key resolves.  No
orphan references or dangling citations remain.

| Reference | Authoritative check | Result |
|---|---|---|
| H\'enon (1976) | DOI `10.1007/BF01608556`; Crossref-backed journal record confirms author, title, volume 50(1), pages 69--77 and year | VERIFIED |
| Yamada (2025) | IMPAN journal record and arXiv `1906.00419v5` confirm author, title, Acta Arithmetica 221, pages 153--163 and DOI `10.4064/aa241112-2-6` | VERIFIED |
| Apostol (1976) | Springer book record confirms author, title, UTM series, publisher, year and DOI `10.1007/978-1-4757-5579-4` | VERIFIED |
| Wang P49/P51/P52 | committed local source packages and seven recomputed dependency hashes | VERIFIED |

The Yamada citation is used only for the argument lower bound for a fixed
algebraic unit-circle conjugate.  It is not cited for the H6 orbit theorem,
the pressure exchange, a determinant or an operator.  The Apostol citation
is background; the exact Abel consequence used by P53 is proved internally.

## Data and internal-consistency audit

- every displayed finite number is recoverable from
  `results/c53_certificate.json` and checked independently in
  `results/c53_independent_check.json`;
- the producer and checker agree on four sentinels, including the explicitly
  non-H6 Salem stress polynomial;
- the paper, README, proof package, results report and Route-A record use the
  same safe-half-plane threshold, Gamma shape, packet normalization and claim
  ceiling;
- the finite sentinels are labelled regression evidence only; no finite-orbit
  extrapolation is used to prove the all-orbit theorem;
- PDF text extraction, metadata and rasterized pages 1, 5 and 9 were checked;
  there are no undefined references, box warnings, clipped objects or blank
  pages.

## Originality screen

Twenty-five characteristic 8--12-word fragments, covering more than half of
the prose paragraphs and every major section, were searched verbatim on
2026-08-14.  No exact or close manuscript match was found.  Internal P49,
P51 and P52 results are cited where reused.  This is a public-web heuristic,
not a substitute for Turnitin or iThenticate.

## AI research failure-mode checklist

1. **Implementation bug passing self-review -- CLEAR.** Exact resultants,
   90-digit embedding checks, a separate verifier, 11 tests and nine hostile
   mutations agree.
2. **Hallucinated citation -- CLEAR.** All external records were checked
   against publisher/DOI metadata and every internal source is hash-locked.
3. **Hallucinated experimental result -- CLEAR.** Every reported finite row
   is regenerated from committed code and preserved JSON output.
4. **Shortcut reliance -- CLEAR / theoretical scope.** Physical-only height,
   doubled normalization, wrong Gamma shape and H6/non-H6 type confusion are
   explicit controls.
5. **Bug reframed as insight -- CLEAR.** The tagged-space obstruction and
   pressure theorem have independent proofs; neither is inferred from a
   surprising finite curve.
6. **Methodology fabrication -- CLEAR.** Code, experiment plan, test report,
   manuscript and stored cutoffs agree exactly.
7. **Early frame-lock -- CLEAR.** The project pursued P52's stated all-orbit
   gap, retained the stronger Mahler-height coefficient when it differed from
   the physical multiplier, and records the failed determinant/operator route
   instead of promoting it.

## Claim firewall

P53 proves a pressure-safe scalar Abel boundary, a Mahler-height orbit law and
a joint orbit--index Gamma limit.  It does **not** prove pressure-critical
continuation, a rational-prime or von-Mangoldt trace, a Fredholm determinant,
a self-adjoint operator, the Riemann hypothesis or a Hilbert--P\'olya
realization.
