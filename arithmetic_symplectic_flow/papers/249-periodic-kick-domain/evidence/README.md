## Material Passport

- Origin Skill: experiment-agent (ARS-Codex)
- Origin Mode: run
- Origin Date: 2026-09-19 (supplied research date)
- Verification Status: UNVERIFIED (formal ARS rerun not invoked; analytic proof separate)
- Version Label: ds06_result_v1

## Experiment Result

- ID: `ASFS-DISCOVERY-20260919-DS06`
- Type/status: single-kick vector FFT controls / COMPLETED
- Process PID: 44077; exit code 0
- Internal duration before final JSON: 0.06558480486 seconds
- Tool-observed wall duration: 0.084492747 seconds
- Initial/peak max RSS: 31336 / 35632 KiB
- Actual UTC: start 2026-09-18T17:32:29.621240; completion
  2026-09-18T17:32:29.686558; separate from supplied research date.
- No stderr, failure, retry, timeout, GPU, installation, full matrix forward,
  eigensolve, target-zero loading or optimization.

cwd = arithmetic_symplectic_flow root:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 120s python -u papers/249-periodic-kick-domain/one_kick.py
```

Hard timeout armed; start/PID and normal completion observed in one tool call,
before the first 30-second monitoring interval. No periodic process snapshot
or precise kernel-only timing is claimed.

[Manifest](run-1/manifest.json) records environment, unchanged source hash,
pre-audit card hash and script hash.
Script SHA256: `cd040d81c6b9ca0a2c51d448612d26e253bdcd3c58c1cf2364d750ddbd9e1265`.
Card SHA256: `f8a0a03ba77dc724f8dff268008a33185c129d92a7b40cb81947e0a3fc493670`.
Source SHA256: `dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb`.

[Result](run-1/result.json) contains both a values, every preselected N and
both potentials; [NPZ](run-1/mode-weights.npz) stores momentum and all weights.
There are 12 (a,N) blocks and 24 norm/kinetic observations, no adverse-case
selection. The cutoff-energy slope field is the analytic *exact Fourier
projection* formula, not a fit or the sampled FFT slope.

Analytic evidence: [independent review](independent-math-review.md) and
[paper](../paper.md); independent same-family agent, not external peer review.
Primary background checked: Strang §4.1, printed p318 (PDF page index1),
[Fourier Series for Periodic Functions](https://math.mit.edu/~gs/cse/websections/cse41.pdf),
the 1/k jump-decay discussion. No local PDF generated or source archive changed.
