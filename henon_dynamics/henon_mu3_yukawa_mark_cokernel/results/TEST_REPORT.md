# C66 test report

```text
producer: PREFREEZE_G3_PASS
structural checker: PASS
SNF library cross-check: SNF_CROSSCHECK_PASS
source replay checker: REPLAY_PASS
hostile mutation test: PASS, 10/10 mutations rejected
```

The producer and structural checker use separate explicit integer Smith
implementations.  The library check uses SymPy's integer Smith form.  All
checks bind the C64/C65 source hashes and preserve the scope firewall.
