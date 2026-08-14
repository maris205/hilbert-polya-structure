# Reproduction

Run the complete deterministic package from the Paper 7 directory:

```bash
./experiments/reproduce.sh
```

The script runs the unit tests, regenerates the checked-in result tables,
verifies every table and the current implementation files against
`packet_trace_manifest.json`, generates two independent copies in fresh
temporary directories, and compares all ten generated files byte for byte
across all three locations. It makes no network request and deletes only its
own `mktemp` directory on exit.

The command is a regression check, not a proof runner. In particular, its
finite prime cutoffs and positive-real values of `sigma` do not establish an
infinite trace ideal, analytic continuation, source ownership, or a Route
verdict. The determinant convention checked here is
`log_Z=-tau_Log_D` and `Z=D**(-1)`.
