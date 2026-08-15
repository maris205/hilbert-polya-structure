# Test report

`bash code/run_c68.sh` completed successfully.

- Main certificate: PASS.
- Independent recurrence/log-derivative checker: PASS.
- Unit tests: 8/8 normal Python, 8/8 optimized Python.
- Main normal/optimized JSON: byte-identical.
- Main normal/optimized stdout: byte-identical, SHA-256
  `6f89ed04352f7260feff6e21d6ae13090774014e30d2dbb00a65e4050641632b`.
- Dependency locks: 5/5.
- Mutation audit: 25/25 rejected.

All theorem-bearing identities use integer arithmetic. Floating boundary rows
are diagnostics and are not used to certify the singularity theorem.
