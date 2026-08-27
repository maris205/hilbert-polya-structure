# Deterministic control results

Command:

```bash
python3 code/verify_digit_weight.py
```

Status: **PASS**.

- phased centered-window checks: `1,080`;
- lowering-composition checks: `3,846`;
- bounded-difference divisibility checks: `261,120`;
- finite return-scale separations: `21`.

Total reported checks: **266,067**.  These are finite exact regressions over
the stated parameter boxes; they support but do not replace the general
proofs.
