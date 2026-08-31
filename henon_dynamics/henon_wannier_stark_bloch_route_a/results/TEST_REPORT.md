# Test report

Expected command sentinels:

- `C267_PRODUCER_PASS rows=210 kernel=1050 shell=5250 eigen=1890`
- `C267 independent checker: PASS (12335 assertions; ...)`
- `C267_SYMPY_PASS (142 symbolic identities; ...)`
- `C267 byte replay: PASS`
- `C267 hostile repaired-hash mutations: PASS 20/20`
- `C267_MANIFEST_PASS`

The checker independently differentiates the proposed kernel and verifies the Schrödinger equation, preventing
an incorrect Bessel index, hopping sign, phase sign, or field sign from surviving.
