# HCS-C30 test report

Test date: **2026-08-11 UTC**

## Exact replay

```text
certificate schema: hcs-c30-certificate-v3
payload SHA-256: f6b26d29490a1870911d808d8934bb7a3505c8091615debb1c2da0c0ac85d796
independent checker: 13/13 PASS
test suite: 43/43 PASS
```

The original main-thread v3 replay passed 41 tests in 60.574 seconds; a
forty-second exact regression then locked the distinction between certificate
type counts and support-size counts.  Test 43 makes manifest refresh fail
closed when any authored paper source or the accumulated Route-A record is
missing.  The final release refresh replayed all 43 tests in 61.125 seconds
with Python standard-library arithmetic only.

## Frozen implementation hashes

```text
producer: 629a47f0d0c2dbf62057a46a7a0d6868336a8afc8a87f94c9d468ca4f2de24ee
checker:  0d2c63e42972465c050a9e425a7bd998bc2fa1cd3d259edefb5dd2223fa858e3
tests:    7e9388bc910f289dc9a6a798836633da504f3d2f875a762c66f8829b5a971846
manifest: 519e886bc2a36e455ec4ad5f70fac47d9f1510dfa2ff8efcd41be06e7e4aad70
```

The temporary main-thread outputs had file hashes

```text
certificate: b3e07fe93fe9dc5eab8b5da4d024b9e414c48b342c5536574da25bd897141dd7
check report: a08d531daf7905af581558ac21b23d3e9413f7950f18d88a3a94caed52b20d12
```

## Coverage

The 43 tests cover:

- deterministic canonical serialization;
- source-lock and raw identity replay;
- all 6/6, 6/6, and 24/24 length and transfer phase censuses;
- positive raw-homology controls and the infeasible C26 raw control;
- exact representative rows, final identities, and primitive Farkas weights;
- the distinct C26 certificate-type census \(15+9\) and forward support-size
  census \(14+10\), preventing those two partitions from being conflated;
- inverse roof, normalized domain, identity trichotomy, signed
  abelianization, symmetric-clock classification, and repetition fork;
- same-space nuclearity and standard flat-trace decisions;
- stale digest, strict boolean/integer typing, unknown keys, malformed JSON,
  chronology, rows, coefficients, source path, clock, unit-path, and Route-A
  rehashed mutations;
- an AST import firewall, real uncached checker CLI pass/fail paths, unexpected
  checker error classification, and exact unimodular inverse fuzzing;
- fail-closed manifest refresh when the bibliography, any of the eleven paper
  sections, or the accumulated Route-A evaluation is missing.

## Release-chain replay

The intentional release refresh regenerated the certificate and checker
report, passed all 43 tests, and wrote a 40-entry whole-project manifest.  A
subsequent default invocation from `/tmp` passed all 43 tests in 61.019
seconds, reproduced both JSON files byte-for-byte, and verified all 40 hashes
without modifying the frozen artifacts.
