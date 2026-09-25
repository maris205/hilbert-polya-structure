# Evidence boundary

- [OEIS A100478](https://oeis.org/A100478), consulted 2026-09-14: definition of the five-step `PrimePi` recurrence, its listed initial values, and the fixed value `66` from index 54 onward.  The entry links a 2026 Lean proof note for its stated general eventual-periodicity extension; this screen does not rely on that extension.
- The exact fixed-state check is finite: `5*66=330` and `pi(330)=66`, so `(66,66,66,66,66)` maps to itself.

Method: definition and elementary fixed-point audit only.  No prime tables beyond the cited definition were imported; no parameter tuning, orbit enumeration, roof, zeta/determinant, lift, or Route evaluation was performed.
