# Experiment Tracker

## Run C38-0 — Discovery Pilot

- Status: `COMPLETED / NONRELEASE`
- Method: floating-point sector spectra for split primes through 61.
- Observation: sectors one and two coincide; sectors zero and one show no
  numerical common eigenvalue.
- Use: discovery only.  No theorem or released result depends on this run.

## Run C38-1 — Exact Modular Pilot

- Status: `COMPLETED / PRECERTIFICATE`
- Method: FLINT characteristic polynomials over the smallest
  \(\mathbb F_\ell\) with \(\ell\equiv1\pmod{3p}\).
- Primes: \(7,13,19,31,37,43,61,67,73\).
- Observation: \(\chi_{p,1}=\chi_{p,2}\) and
  \(\gcd(\chi_{p,0},\chi_{p,1})=1\) in every case.
- Next action: replace the pilot with a frozen producer/checker and retain only
  the declared nine-prime release ledger.

## Run C38-2 — Release Certificate

- Status: `PASS / PRE-COMMIT FREEZE`.
- Exact ledger: every split prime through 73.
- Checker: 12/12 gates PASS.
- Tests: 29/29 PASS.
- Paper: 7 pages, clean final LaTeX log.
- Remaining: commit hash backfill and provenance freeze.
