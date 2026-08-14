# Test report

Command:

```bash
bash code/run_c55.sh
```

Results:

- producer: PASS;
- independent checker: PASS;
- unit tests: 14/14 PASS;
- hostile mutations: 17/17 rejected;
- producer and checker use distinct cycle-enumeration paths;
- exact trace root counts: 6/6 isolated;
- physical coordinate/trace branch: one coordinate root, zero derivative
  roots, certified sign word and strictly decreasing trace;
- no prime/zero data consumed;
- no Python cache required (`-B` and `PYTHONDONTWRITEBYTECODE=1`).

The test suite checks the finite-memory theorem and its scope firewall.  It
does not constitute an empirical test of all-period Hölder realizability.
