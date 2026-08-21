# Adaptive batch plan: HCS-C94 through HCS-C98

Status: **round complete; five packages prefreeze-verified and release-ready**

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round keeps the frozen C88 first-passage atlas and the exact C89-C93
extensions.  Every result is finite, source-bound, and reproducible; no
arithmetic/local-data, Euler-factor, root-number, automorphy, full
Burnside/table-of-marks, or Hilbert--Polya claim is allowed.

## Research sequence

1. **C94 - first-passage hazard and residual life.**  Derive every target's
   exact discrete hazard, cumulative hazard product, mean residual life, and
   conditional residual moments directly from C88.
2. **C95 - comparable-target passage delay.**  For all 102 comparable
   ordered target pairs, including reflexive pairs, certify the exact delay
   law, conditional delay moments, and zero-delay probabilities from C90.
3. **C96 - target coverage order statistics.**  For each random label order,
   study the number of targets reached by time `k` and certify exact coverage,
   quantile, and order-statistic laws across all twenty C88 targets.
4. **C97 - ordered-pair orbit quotient.**  Lift the C93 faithful order-1920
   target action to all 400 ordered target pairs; certify complete C90-law
   transport, orbit--stabilizer, Burnside, relation-type, and transpose data.
5. **C98 - conditional first-passage kernels.**  Convert all 400 C90 joint
   laws into exact forward and reverse conditional kernels, with explicit
   null rows, Bayes balance, and total expectation/variance identities.

## Authority and dependency boundary

C94 reads frozen C88.  C95 reads frozen C88/C90.  C96 independently
reconstructs its coverage process from C88.  C97 reads frozen
C75/C76/C88/C90/C93 and reconstructs the faithful label action.  C98 reads
frozen C88/C90 and independently rebuilds synchronous cells from C88 packed
supports.  Any effective label action uses the faithful order-1920 image;
C75's ambient lifted order 11520 remains a distinct datum.

## Release gate

Each package must provide a research question, source audit, theorem package,
producer, independent checker, symbolic or exact finite cross-check, clean
replay, hostile mutation audit, deterministic two-pass LaTeX build, evidence
hash, manifest hash, PDF hash, and explicit scope nonclaims.  The round is
released after all five packages pass the uniform final audit and this batch
is committed and pushed.

## Gate and artifact ledger

| paper | gate result | hostile mutations | evidence SHA-256 | manifest SHA-256 | PDF SHA-256 |
|---|---|---:|---|---|---|
| C94 | producer/checker/SymPy/replay PASS | 13/13 | `e185462629459a7d6602e3d1e3f49977a82d3fdee86007c3f906b224f028d1b` | `c2eafa0f604aeb817a010afcf9f4e1841f4c02ca7b91ce303b31e9ad04930912` | `c9678e7a39c3ae4aeaff56ce20f809cd2bd894bae4ca98cf5164cd18c2dddf54` |
| C95 | producer/checker/SymPy/replay PASS | 17/17 | `53e5c9a1dbda2fa7e01af34ce6fc161ac102a312b003e1c86402ae7ec7373a3c` | `ba03e5e86ec6a9f3d7a31d9e6b57533c4af5e65db0e4f9fa3dfeddba15d47176` | `60caec178a32d3d33d459cd0103c922fb5e967d25e06830fcd4011705ac3698c` |
| C96 | producer/checker/SymPy/replay PASS | 15/15 | `75a93c80b5e44f6aca1885073cf12e943de02751ad4e99aa37e83bf211b6ca23` | `bfd172a456330ea7d5c0c821e4a3ef93f0a39db9e49a9159b16ecbea3932bb4a` | `9222c35bd7d0d8c097ffadf47eeb086e735adbfccd98bff142143087c4626e18` |
| C97 | producer/checker/SymPy/replay PASS | 14/14 | `099d8f32794d6967b3f2653f92dcaa0b096c711b67ed070330d7763a146bc696` | `94f4b3c8e15977e0882194bc6c0165291694902169d01f9ff278a542e74ed516` | `7c52b3081c1941b8c18aec7cfce89e2a95f4f85581e6135505061af0260422b1` |
| C98 | producer/checker/SymPy/replay PASS | 16/16 | `49179ea34f6f10b7e20c68914cdd7aa5bb5df775cefade69f1a40163f2e933cb` | `feeeaa4af1959b804e21923f47bf24df161fb78d69b624ead768473cb652f4d1` | `774fa65062106e611c3d597b56aa4865a341f880263b1431bc4a6661f5820cfb` |

## Round-wide release checklist

- [x] All five evidence receipts pass independent reconstruction and replay.
- [x] All manifest file ledgers match the complete non-excluded file sets.
- [x] C75 ambient order 11520 and effective order 1920 remain distinct.
- [x] Scope firewall and arithmetic/operator nonclaims remain explicit.
- [x] Uniform final audit passes with `git diff --check`.
