# Results

The evidence payload is `results/c291_dimer_rsa_evidence.json`.

- Canonical payload SHA-256:
  `1e9911ffb46b20b1c50e0a22566eb5048860d50ff0fb3be787fb9e64d6092af4`
- Evidence-file SHA-256:
  `65fdb2333d3fbb6c3177eaa7da5d303ab0b42f2ff99b8d55ecd97e1863008a0f`
- Evidence size: 23,778 bytes.
- Exact path distributions: `P_0,...,P_10`.
- Exact simple-cycle distributions: `C_3,...,C_9`.
- Stored factorial moments: orders `0,...,5` for `P_0,...,P_20`.
- Exact first/second moment recurrence controls: through `n=200`.
- Asymptotic cells: `n=20,50,100,200`.
- Independent checker: PASS, 19,371 assertions, including strict Route-A YAML
  schema/type/value and semantic-hash validation.
- SymPy cross-check: PASS, 132 symbolic checks.
- Fresh-path replay: PASS, two unrelated temporary roots and exact bytes.
- Hostile audit: PASS, 105/105 mutations rejected, including recursive
  duplicate-YAML and repaired YAML semantic attacks.

The direct bitmask DP aggregates all 818,225 labeled edge orders in its declared
path/cycle window.  Its distributions reproduce the first-edge PGFs, exact
means and variances, contiguous support intervals, `G_n=zF_{n-2}`, and
`Var(K_n)=Var(M_{n-2})`.

The finite data are an executable regression oracle.  The all-size recurrence,
all-order factorial hierarchy, pole extraction, support, and cycle theorem are
proved in `THEOREM_PACKAGE.md` and `paper/main.tex`.
