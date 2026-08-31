# Test report

## Commands

```bash
python3 -B code/c265_hawkes_producer.py
python3 -B code/c265_hawkes_checker.py
python3 -B code/c265_hawkes_sympy_crosscheck.py
python3 -B code/c265_hawkes_replay.py
python3 -B code/c265_hawkes_mutation.py
```

## Settled results

- producer: PASS;
- independent checker: PASS, 27,893 assertions;
- SymPy: PASS, 1,304 checks;
- byte replay: PASS;
- mutation suite: PASS, 28/28.

The checker imports no producer module.  All stored rational cells are
reconstructed, not merely sampled.  The symbolic suite avoids assuming the
critical face inside the subcritical stationary formulas.
