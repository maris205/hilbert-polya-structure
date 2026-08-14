# Integrity report

## Artifact gates

- required `README.md`, `paper/`, `code/`, `experiments/`, `results/`,
  `notes/`: PASS;
- final PDF: PASS, 7 pages;
- PDF author metadata: Liang Wang;
- final PDF equals round-two PDF: PASS;
- producer and independent certificate: PASS;
- Route-A evaluation and Route-B refusal: PASS.

## High-impact claim verification

| Claim | Evidence | Verdict |
|---|---|---|
| uniform totient packet formula | exact Möbius/cyclotomic proof + 70 rows | VERIFIED |
| Abel constant \(3\log L/\pi^2\) | summatory-totient proof + independent rows | VERIFIED |
| Gamma\((2,1)\) profile | exact Laplace ratio + tightness proof | VERIFIED |
| no tagged norm/weak limit | coordinate and mass functionals | VERIFIED |
| all-orbit boundary remains open | theorem ledger and paper claim firewall | VERIFIED |

## Reference verification

- Flatters article: title, author, journal, pages, year, DOI and arXiv ID
  verified against arXiv `0708.2190` and DOI metadata;
- Apostol book: title, author, publisher, year and DOI verified against the
  Springer book record;
- internal P49/P51 artifacts: SHA256-locked and independently rehashed.

No external reference is used as a substitute for the P52 proofs.

## AI research failure-mode checklist

1. **Implementation bug passing self-review — CLEAR.** Separate producer and
   checker, normal/optimized runs and 12 adversarial tests agree.
2. **Hallucinated citation — CLEAR.** Both external records were checked
   against primary/official metadata.
3. **Hallucinated experimental result — CLEAR.** Every displayed finite row
   is regenerated from the committed JSON producer.
4. **Shortcut reliance — CLEAR / theoretical scope.** Wrong scaling,
   normalization, Gamma shape and vector promotion are explicit controls.
5. **Bug reframed as insight — CLEAR.** The negative vector result follows
   from a proof independent of finite convergence behaviour.
6. **Methodology fabrication — CLEAR.** The methods section, scripts,
   certificate and test report use the same cutoffs and constants.
7. **Early frame-lock — CLEAR.** The project tests the exact P51 open theorem
   and records both the positive scalar boundary and the failed tagged
   topology rather than forcing a determinant narrative.

## Claim firewall

The report certifies a fixed-period-four-orbit boundary theorem.  It does not
certify all-orbit interchange, a prime-orbit bijection, von-Mangoldt weights,
analytic continuation, a Fredholm determinant, a self-adjoint operator or the
Riemann hypothesis.
