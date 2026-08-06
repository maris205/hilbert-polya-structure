# Exact test report

Date: 2026-08-06

## Frozen commands

```bash
python code/solenoid_zeta.py --max-period 20 --parity-period 12 --tower-level 8
python code/independent_check.py --max-period 12
python code/test_solenoid_zeta.py -v
```

## Outcome

- Producer: passed; all deterministic artifacts regenerated.
- Direct word range: periods 1--20, totaling 2,097,150 based words.
- Independent direct implementation: passed through period 12.
- Witness repetition audit: passed for repetitions 1--20.
- Unit tests: 10/10 passed.
- Python bytecode compilation: passed for all three code files.

The independent checker is deliberately separate from the producer.  Version
2 also performs the following cross-artifact checks:

- all 20 Möbius/Dold exact-period and primitive-orbit rows;
- all 20 exact zeta-coefficient recurrences;
- all 20 valuation-distribution reconstructions;
- all 96 congruence-tower rows;
- certificate-to-periodic-CSV identity;
- certificate-to-witness-JSON identity;
- SHA-256 hashes of all six producer artifacts before writing its own report.

All checks passed.  A separate clean rebuild in a temporary directory during
the adversarial audit produced byte-identical copies of all seven generated
data artifacts.

## Scope

The Berlekamp--Massey screen in `recurrence_screen.json` is a finite-prefix
diagnostic only.  It is not used to claim rationality, nonrationality, or a
natural boundary.  The all-period results in the manuscript are proved from
the fixed-index formula, the mod-2 language theorem, and uniform
archimedean bounds.
