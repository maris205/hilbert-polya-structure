# Deterministic control results

Command:

```bash
python3 code/verify_sandpile_translation.py
```

Status: **PASS**.

- two-site reduced-Laplacian checks: `7,938`;
- arbitrary-profile reduced-Laplacian checks: `1,176`;
- literal recurrent-addition orbit checks: `23,346`;
- additional determinant identities executed by the script: `49`.

The three printed counters total **32,460**, with all checks passing.  Literal
enumeration covers all `K_{m,n}` with `2 <= m,n <= 4`, including the `n=2`
three-denominator branch.  This finite regression is not a proof or novelty
claim.
