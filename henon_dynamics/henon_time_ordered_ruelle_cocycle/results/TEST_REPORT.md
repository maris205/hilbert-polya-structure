# HCS-C22 T1--T4 and orbitwise scalar-T5 test report

**Run date:** 2026-08-09 UTC
**Platform:** Linux, Python 3.12.3
**Locked packages:** SymPy 1.14.0, pytest 9.0.3

## Clean command

From the project root:

```bash
python -m pip install -r requirements.txt
./code/run_c22.sh
./code/run_c22_t4.sh
sha256sum -c results/ARTIFACT_HASHES.sha256
```

The first wrapper below is the frozen T1--T3 chain; the second is the
T4/orbitwise-scalar-T5 chain.

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
Regression suite: 11 passed
```

The T4/orbitwise-scalar-T5 command is

```bash
./code/run_c22_t4.sh
```

with expanded commands

```bash
python code/c22_t4_producer.py
python code/c22_t4_independent_check.py
pytest -q code/test_c22_t4.py
```

Its outcome is

```text
T4 instability repetition/log-trace/convergence: PASS
T5 common two-letter base pinning domain: PASS
T5 common projective slope and holomorphic Log domain: PASS
T5 orbitwise base/projective scalar denominator cancellation: NO-GO (expected theorem gate)
Independent checker: PASS
Regression and fail-closed mutation suite: 15 passed
```

The combined regression command

```bash
pytest -q code/test_c22.py code/test_c22_t4.py
```

passes all 26 tests.

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
| `code/c22_independent_check.py` | `52348f8cb7cf1d2f905adc1d13052789eac156cb78653d6ebb1d3897c01e0643` |
| `code/test_c22.py` | `c6914c8e5098d915f31ed494135e352705c619fd62b5365d4011c39b206555eb` |
| `code/run_c22.sh` | `d48ff13bec7e815de2d10001fd843d464682395f28b3cb401b9f575f71d856c4` |
| `requirements.txt` | `c9f828d169aee548b4c4d5fb0eca5b3b851c4a1561e6af961a27cdbd9534b529` |
| `results/c22_certificate.json` | `8def07eda4e10f6358a58bf27fa281dd113534213099e659db6280411237a987` |
| `results/c22_independent_check.json` | `68a80bf1d915d766cb0533deb24058f9b24bc82b101683f71cb522b014dbf26c` |
| `code/c22_t4_producer.py` | `6053e203ec8a3cd3d1af1fd0e0b47ffbffd95d70bf0525dd537aacdbe0da7dcd` |
| `code/c22_t4_independent_check.py` | `54a6ac99988ff8ed19bfc4717cf45d7075d4ce8dbae34a2e563f32d53556da54` |
| `code/test_c22_t4.py` | `238c20e93fdc5fde39b8d651e2455bd314cde8ccc9022fe9697ea6029fa04098` |
| `code/run_c22_t4.sh` | `2cc9cffacd7654871ddfc97a7de9d1c4254f608c50cf8d3f23286826826ef4e0` |
| `results/c22_t4_certificate.json` | `b352888d7ac9585d8edc0026909b6a94a15e6cab0d1771df83431f3e0aec1a5f` |
| `results/c22_t4_independent_check.json` | `6fd1601164cdd1cf69a41d7c105a05109cc0fd8c859c11d1831ad35e15ea1a75` |
| `T4_T5_DERIVATION.md` | `4688fc25c0fda115ccd40b0394ca8693cbeeaecbb8227d9aca947f0586f850ff` |
| `GRADED_PIVOT_ROADMAP.md` | `f85ac00451be0599fe23ee1031f5656e46c88b85541983350354048951d14d28` |
| `results/T4_T5_RESULTS.md` | `c22f6ef4529827caa0846fa502fb854d4be9044f2fc2b67555a0942d5ed9c054` |

The independent-check artifact embeds and verifies the producer artifact's
hash.  All pass/fail gates use exact rational, symbolic, or rational-interval
arithmetic; no claim depends on binary floating-point agreement.

A copy under a different absolute checkout path produced byte-identical
`c22_independent_check.json` output, confirming that the released checker no
longer serializes a machine-specific path.
