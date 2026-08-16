# Paper 37 exact integration plan — SD-C39

## Milestones and run order

1. Freeze this plan and the integration preregistration before code or result
   artifacts are created.
2. Pin authority, bridge, prototype, and standard-library dependencies in
   machine-readable research/dependency locks.
3. Bridge the frozen prototype into physically separate `code/source/` and
   `code/evaluator/` processes; add only serialization, isolation, integrity,
   and Route-A integration around the unchanged scientific core.
4. Run a smallest sanity evaluation, then fresh A/B and cold C exact runs.
5. Test absent/null/empty/populated transport metadata and absent/present
   future-manifest metadata without changing scientific or Route bytes.
6. Independently evaluate canonical counts, formulas, exact result closure,
   and the frozen Route tuple; emit JSON/CSV evidence and the report.
7. Run standard-library tests, text/cache hygiene, research locks, and full
   integrity checks; freeze `results/SHA256SUMS.txt` with the documented
   structural exclusions.
8. Repeat the full integration and require managed-artifact idempotence.

## Source/evaluator process boundary

The source subprocess may construct only frozen fixtures. The evaluator
subprocess independently reimplements the mathematical decisions and never
imports source code. The integrator transports canonical JSON through stdin
and stdout and records the source packet hash separately from the scientific
aggregate. Route evaluation consumes only canonical evaluator output and
frozen locks.

## Exact result set

Required evidence comprises:

- canonical scientific JSON plus byte-identical A/B/C copies;
- reproducibility and cold-run certificate;
- four-state metadata-stability certificate;
- prototype-bridge and canonical-count certificates;
- raw affine, fixed, random, and paired CSV tables;
- independent Route-A evaluation JSON;
- research/dependency locks;
- standard-library test results;
- exact result-set, text/cache hygiene, and integrity certificates;
- root `EXPERIMENT_REPORT.md`;
- the preartifact Route YAML at its fixed path;
- immutable `results/SHA256SUMS.txt`, excluding itself, Route YAML, and the
  nonexistent/future root `PAPER_MANIFEST.sha256`.

No unlisted scientific experiment is added.

Path provenance note: the pre-canonical path correction was made before the
final cleared-output run; the sole canonical report is the root
`EXPERIMENT_REPORT.md`, and no experiments-directory copy is retained.

## Success and stop criteria

Sanity must pass before the full run. Every subprocess must exit cleanly,
all 131 evaluator assertions must pass, the canonical aggregate must equal
the frozen prototype hash, and A/B/C plus all metadata variants must be byte
identical. Canonical counts must be exactly `8`, `48`, `9`, `9`, `24`, `2`,
and `2` in their preregistered roles. Every affine `r>=2` witness must equal
`-4*r^4*(r-1)`.

Any authority hash mismatch, scientific mismatch, source/evaluator import
violation, incomplete or surplus exact-result artifact, noncanonical text,
cache residue, ledger failure, or non-idempotent rerun stops integration.

The scientific success criterion is not promotion: successful reproduction
confirms the frozen negative conclusion `ROUTE_A_REJECTED` and keeps Route B
locked.

## Resource bound

CPU-only, Python standard library only, no network, no floating tolerance,
no unbounded word enumeration, no GPU-hours. A/B/C and metadata variants run
sequentially to make process provenance explicit.
