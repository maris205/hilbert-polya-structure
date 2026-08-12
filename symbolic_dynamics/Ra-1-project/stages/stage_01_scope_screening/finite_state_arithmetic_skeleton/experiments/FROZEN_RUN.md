# Frozen SD-C01/02/03 run

Single command:

Run from the Git repository root:

```bash
cd symbolic_dynamics/Ra-1-project/stages/stage_01_scope_screening
python finite_state_arithmetic_skeleton/experiments/run_session4_core.py
```

The command runs the three unit-test suites before executing any full run.  It
uses only the preregistered seeds `20260812`--`20260816`, uses no Riemann-zero
data, and writes deterministic JSON/CSV artifacts to each candidate's
`results/` directory.  Exact arithmetic and numerical observations are stored
in separate result sections.
