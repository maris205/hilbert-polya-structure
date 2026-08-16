# Paper 38 Stage-1 integrity protocol

Candidate: `SD-C40`

1. Managed roots are root `EXPERIMENT_REPORT.md`, `code/`, `results/`,
   `experiments/`, `docs/`, and `evaluations/route_a/SD-C40/`. Writer-owned
   manuscript files and the five in-flight LaTeX auxiliaries are outside the
   integrator managed set.
2. Stage 1 requires the root `PAPER_MANIFEST.sha256` to be absent and never
   creates it. Stage 2 is reserved for the root authority.
3. `results/SHA256SUMS.txt` is immutable after freeze and excludes itself,
   `evaluations/route_a/SD-C40/2026-08-15.yaml`, and the future root manifest.
   The Route card receives a separately reported SHA-256.
4. Every managed text file must decode as UTF-8, contain no BOM or carriage
   return, have no trailing horizontal whitespace, and end in exactly one LF.
5. Python cache directories, bytecode, pytest caches, retained cold-run
   directories, and temporary outputs are forbidden.
6. The independent audit checks the complete expected result path set,
   source/evaluator import and directory separation, stable five-file research
   lock, experiment-plan hashes, exact science and Route hashes, fixed PENDING
   provenance triple, ledger coverage, text hygiene, and manifest state.
7. Runs A and B are fresh subprocess executions. Run C uses an isolated copy
   of only the integrated source and evaluator directories; its temporary
   directory is removed before materialization.
8. External `/tmp/paper38_*` files are provenance witnesses only. If present,
   their hashes are checked. If absent, scientific execution and the integrity
   verdict remain byte-identical.
9. A second complete integration run must leave all managed bytes unchanged.
