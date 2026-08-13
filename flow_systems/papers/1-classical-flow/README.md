# 1-classical-flow

Stage 1 studies which continuous-time flow families simultaneously possess intrinsic arithmetic content and a reproducible primitive closed-orbit structure. The study establishes a **two-halves obstruction**:

- arithmetic-scheme flows supply intrinsic prime packets with period `log p`, but not yet the smooth hyperbolic orbit/trace/quantization package;
- hyperbolic geodesic flows supply the exact closed-orbit, stability, Selberg/Ruelle and Laplace-spectral package, but their orbit norms are not rational primes.

The two statements were not assumed: the first is calibrated against Deninger's packet theorem and its disclosed limitations; the second follows from an exact Galois-conjugation obstruction and a zero-free orbit audit.

## Status

- Stage: Route A / A0--A1 baseline — **complete; awaiting checkpoint confirmation**
- Target evidence: theorem-level structural comparison plus a zero-free numerical orbit ledger
- Forbidden inputs: Riemann-zero tables, prime-fitted parameters, manually assigned `log p` roof functions, manually inserted von Mangoldt weights
- Primary isolated-orbit candidate: modular geodesic flow on `PSL(2,Z)\H` — rejected as a rational-prime Hilbert--Pólya candidate, retained as an exact benchmark
- Arithmetic comparator: Deninger's rational-Witt flow for `Spec Z`
- Proves-too-much controls: generic compact hyperbolic geodesic flow and generic contact Anosov flow
- Route-B status: not invocable; no candidate simultaneously reaches strict A0 and pass-level A1

## Main artifacts

- [Chinese Stage-1 summary](notes/stage1_summary_zh.md)
- [Paper](paper/paper.pdf) and [LaTeX source](paper/manuscript.tex)
- [Mathematical results](notes/mathematical_results.md) and [candidate evaluation](notes/candidate_evaluation.md)
- [Prior-work audit](notes/prior_work_audit.md) and [source verification](notes/source_verification.md)
- [Reproduction command](experiments/reproduce.sh) and [result summary](results/arithmetic_audit_summary.json)
- Route-A evaluations: [`DEN-WITT-Z-FIN`](../../evaluations/route_a/DEN-WITT-Z-FIN/2026-08-13-stage1.yaml) and [`MOD-GEO`](../../evaluations/route_a/MOD-GEO/2026-08-13-stage1.yaml)

## Reproduction

Run `bash experiments/reproduce.sh` from this directory. The script executes the unit tests, rebuilds the zero-free orbit ledger, checks the local phase-boundary hashes, and regenerates all declared numerical controls. Commands, caveats, checksums, figures, and tables are recorded under `experiments/` and `results/`.
