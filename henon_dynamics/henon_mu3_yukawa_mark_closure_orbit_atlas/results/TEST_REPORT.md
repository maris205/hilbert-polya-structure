# C76 test report

The following checks are required for the prefreeze package:

```text
producer: PREFREEZE_G3_PASS
independent checker: PASS
GAP cross-check: GAP_CROSSCHECK_PASS
clean replay: REPLAY_PASS
hostile mutations: MUTATION_TEST_PASS (16/16 rejected)
```

The producer and checker validate the C75 authority bytes, canonical C76
JSON, the 20 subgroup closures, the effective group order and element-order
distribution, the complete 65536-support partition, and both minimality
filters.  The GAP check is restricted to the faithful 16-label action and
must not reintroduce the C75 ambient C6 kernel.  Replay and mutation tests
exercise the same evidence in a fresh process and under semantic corruption.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

The canonical evidence SHA-256 is
`42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94`.
The GAP check reports `|H|=1920`, structure `C2 x S5 x D8`, 3024 support
orbits, and the complete cardinality and orbit-size spectra.  The replay
preserves the evidence hash byte-for-byte.
