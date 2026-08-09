# HCS-C22 T1--T3 test report

**Run date:** 2026-08-09 UTC
**Platform:** Linux, Python 3.12.3
**Locked packages:** SymPy 1.14.0, pytest 9.0.3

## Clean command

From the project root:

```bash
python -m pip install -r requirements.txt
./code/run_c22.sh
```

Equivalent expanded commands:

```bash
python code/c22_producer.py
python code/c22_independent_check.py
pytest -q code/test_c22.py
```

## Outcome

```text
T1 common survivor: PASS
T2 complete local chronology aggregate: PASS
T3 unit-numerator global residue collapse controls: PASS
Independent checker: PASS (zero branch failures)
Regression suite: 10 passed
```

The producer uses exact `Fraction` arithmetic for every decision and
90-decimal integer-square-root enclosures for irrational quantities.  The
checker imports neither producer code nor earlier Hénon code.  It recomputes
the exact geometry windows and margins, joint combinatorics, minimal matched
protocol pairs, all 78 matched branch comparisons (156 local orbit
enclosures), four aggregate differences per pair, finite-field control,
exact cyclic/reversal interval maps, and Hill identities.

## Released hashes

| Artifact | SHA-256 |
|---|---|
| `code/c22_producer.py` | `e890fdeaddeb113a1ef23ba0e4c75d270f3057c4b58570e205a9e3005f3711c3` |
| `code/c22_independent_check.py` | `1a1c9894891a6551c8dd6f1f726f81c4da238dc7b749919874346609847f0aed` |
| `code/test_c22.py` | `c24382173474cc6993d249c9fab71d4a33f544deb60d28e4d82c153e8306cad9` |
| `code/run_c22.sh` | `d48ff13bec7e815de2d10001fd843d464682395f28b3cb401b9f575f71d856c4` |
| `requirements.txt` | `c9f828d169aee548b4c4d5fb0eca5b3b851c4a1561e6af961a27cdbd9534b529` |
| `results/c22_certificate.json` | `8def07eda4e10f6358a58bf27fa281dd113534213099e659db6280411237a987` |
| `results/c22_independent_check.json` | `f740fb6f5e5733bd1b069b1a182bc171ad6980943eb877cb18ba15d8cd0654ae` |

The independent-check artifact embeds and verifies the producer artifact's
hash.  All pass/fail gates use exact rational, symbolic, or rational-interval
arithmetic; no claim depends on binary floating-point agreement.

A copy under a different absolute checkout path produced byte-identical
`c22_independent_check.json` output, confirming that the released checker no
longer serializes a machine-specific path.
