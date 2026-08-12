# C36 code

This directory contains a producer/checker pair for the certified Mellin
parity obstruction associated with the Hénon phase

\[
P_6(u)=2u^3-u.
\]

The producer reconstructs the two signed Mellin symbols through a rigorous
hypergeometric continuation using `python-flint==0.9.0`. The independent
checker does not import producer code. It separately checks:

1. strict recursive schema, canonical payload hash, source locks, and runtime;
2. the fixed symbolic Mellin/scattering ledger;
3. the registered off-critical disc and all numerical thresholds;
4. independent Arb enclosures for the even and odd parity symbols;
5. an elementary rotated-contour bound `sup_D |A''| < 1200`;
6. the strict quantitative Rouché inequality proving one simple zero in `D`;
7. nonvanishing of all companion factors needed to prevent cancellation;
8. direct nonvanishing of the completed Riemann \(\xi\) function on the
   registered disc, without consulting a zero table;
9. the conservative Route-A and claim-scope firewall.

Run a complete frozen replay from the project directory:

```bash
./code/run_c36.sh
```

Only intentional release preparation may overwrite results and the manifest:

```bash
./code/run_c36.sh --refresh-manifest
```

The mutation suite is also available directly:

```bash
python3 -I -B -m unittest discover -s code -p 'test_c36.py' -v
```

The certificate proves a local obstruction for the unrenormalized parity
symbol. It does not turn the pointwise multiplier into a Fredholm operator,
does not supply a global strip census, and does not prove RH.
