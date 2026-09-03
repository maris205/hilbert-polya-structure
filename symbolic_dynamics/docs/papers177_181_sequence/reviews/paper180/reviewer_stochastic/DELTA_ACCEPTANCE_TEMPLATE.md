# P180 stochastic-review delta acceptance template

- [x] The abstract distinguishes tail dependence on the 3-primary exponent
  from period dependence on the coprime residual order.
- [x] `(3^t-1)/2` and `2s` are typed as integer exponent/modulus
  notation, including in characteristic two.
- [x] Rechecked `A=0`, `GF(64)` (`A=2`), and `GF(109)` (`A=3`).
- [x] `verify_reviewer_stochastic.py` reproduces `CANONICAL.txt` in two fresh
  processes.
- [x] No repair changes `ord_(2s)(3)` to the scalar-value period
  `ord_s(3)`.
- [x] `OWNER_AMBER / HOLD_EXTERNAL` remains visible.
- [x] The rebuilt Round-2 PDF is recorded under a new round without overwriting the
  immutable Round-0 PDF.

**Current disposition:** repaired delta accepted; no open finding at the
reviewed Round-1 hashes.
