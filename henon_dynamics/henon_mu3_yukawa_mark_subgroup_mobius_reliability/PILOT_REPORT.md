# C77 pilot report

The C77 pilot is **exact and source-bound**.  It reads the sixteen C76
coordinates and twenty ordered subgroup rows, computes the subgroup-poset
Möbius function, and compares inversion against a complete 16-bit support
enumeration.

The label-containment counts are

```text
n_H = [5, 6, 7, 6, 7, 6, 8, 7, 8, 7, 11, 7, 7, 8, 12, 8, 8, 9, 15, 16].
```

The direct support totals by subgroup index are

```text
[32, 32, 96, 32, 96, 32, 96, 32, 96, 32,
 1760, 64, 64, 192, 1760, 64, 64, 192, 30400, 30400].
```

All 65536 supports are accounted for.  Every subgroup's direct Bernoulli
polynomial agrees with its Möbius-inverted cumulative polynomial.  The full
core row is

```text
1 - q - q^4 + q^5 - q^7 - q^8 + 5q^9 - 3q^10
= (1-q)(1-q^4-q^7-2q^8+3q^9).
```

The producer status is `PREFREEZE_G3_PASS`; the independent checker reports
`PASS`, the SymPy cross-check reports `SYMPY_CROSSCHECK_PASS`, clean replay
reports `REPLAY_PASS`, and the hostile audit rejects 25 semantic mutations
(`MUTATION_TEST_PASS`).  The canonical evidence hash is
`f7e2db84698ec61bf6283175368d2749d7f17ac77baeda37fd0a5cb8caf1c634`.
The deterministic paper double-build is the remaining release gate.  Scope
firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
