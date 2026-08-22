# C104 test report

Commands run from the package directory:

```text
python3 code/c104_multibranch_producer.py       PASS
python3 code/c104_multibranch_checker.py        PASS
python3 code/c104_sympy_crosscheck.py           PASS
python3 code/c104_replay_checker.py             PASS
python3 code/c104_mutation_test.py              PASS (9/9 rejected)
```

The checker independently reproduces all 196 rows, the six trace identities,
and the determinant coefficients. SymPy independently verifies six powers,
the determinant, and six Newton identities. Replay confirms canonical JSON
bytes and the scope firewall. Mutation tests reject changes to schema, scope,
word data, monodromy, traces, primitive decomposition, determinant,
Route-A assessment, and a forbidden Fredholm claim.

No test establishes geometric Hénon coding or a Fredholm operator; those are
the explicit next-stage obligations.

Frozen hashes: evidence
`392b356265b1f4caaec9dd0b9f9ff1d5466acef3e25374c443d3e55c9e199205`; PDF
`b9d3a478e211cfe4856485c96e0045de0c95240354e3163768ddf09f57761efb`.
