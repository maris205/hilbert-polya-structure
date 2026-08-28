# Test report

Commands run from the package root:

```text
python3 code/c211_lv_producer.py                 PASS (24 levels)
python3 code/c211_lv_checker.py                  PASS (732 assertions)
python3 code/c211_lv_sympy_crosscheck.py         PASS (12 identities)
python3 code/c211_lv_replay.py                   PASS (byte replay)
python3 code/c211_lv_mutation.py                 PASS (12/12 rejected)
```

The checker uses an independent SciPy DOP853 event integration with
`rtol=2e-11`, `atol=2e-13`, and `max_step=T_quad/200` (with a one-step lower
bound), where `T_quad` is only a safe horizon from its own quadrature.  No
producer helper is imported.  Scope flags are all false and Route B is denied.
