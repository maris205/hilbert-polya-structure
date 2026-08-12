# Test report

The frozen release is required to satisfy all of the following:

- producer replay is byte-identical across two runs;
- the independent checker passes 9/9 gates;
- the unit suite passes 6/6 test methods;
- 27 rehashed or stale-hash semantic mutations are rejected;
- float/bool substitutions cannot impersonate integers/booleans;
- checker `FAIL` is distinguished from unexpected `ERROR`;
- the release manifest covers every required code, result, documentation,
  evaluation, and paper source.

The exact counts and hashes are refreshed only by the explicit release mode
of `run_c34.sh`; the default runner is read-only.
