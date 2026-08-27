# P24 experiment status — Round 2

The exact word-ball enumeration and target-free holonomy shuffle completed.
The core output is reproduced byte for byte under the hash recorded in
`round2_receipt.json`; exact checks and claim boundaries are in
`round2_validation.md`.

Executed control:

- keep every sampled complex-length real part and observed repetition field;
- permute holonomy angles by a fixed SHA-256 ordering derived only from row IDs;
- record orientation reversal separately;
- never inspect prime ideals, rational primes, or Riemann zeros.

Observed phase/length score:

```text
original = 0.003173818350680037
shuffle  = 0.02247064819754699
```

This is `[NUMERICAL_OBSERVATION]`; it does not favor the observed angles over
the shuffle and does not create an arithmetic owner.  The matched
non-arithmetic Kleinian ledger and scalar/chiral trace comparison remain
`[OPEN]`.  Arithmetic label controls remain prohibited until a canonical
orbit owner exists.
