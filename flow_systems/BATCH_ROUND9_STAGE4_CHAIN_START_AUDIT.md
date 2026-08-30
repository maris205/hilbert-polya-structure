# Round 9 Stage 4 chain-start audit

Date: 2026-08-30 (UTC)

Verdict: **PASS for all five exact chain starts**

Each Stage-2.5 report records the gate verdict `PASS`, binds the unanchored
manuscript bytes, and carries no open blocking integrity issue. Paper 28 also
carries the nonblocking replay-order distortion into the Stage-3 roadmap; the
Stage-4 authorization addresses it and this receipt does not treat it as
already corrected.

The official ARS anchorizer was replayed on a temporary byte-copy of each
Stage-2.5 manuscript. Both the anchored draft and generated manifest were
byte-identical to the frozen Stage-3 chain-start artifacts. Deleting only the
`<!--block:BNNNN-->` marker lines from each anchored draft reproduced its
Stage-2.5 manuscript byte-for-byte.

| Paper | Stage-2.5 manuscript SHA-256 | Anchored draft SHA-256 | Manifest SHA-256 | Blocks |
|---|---|---|---|---:|
| 24 | `e43ba0f77332b79df4d84346dcb6e3041c20f4bdded5a91f42caac348ea9fd11` | `b59bc70c51960f6c89167619df21923c035b4311d9df4e40c034a1fe036cf60e` | `c0a86683ac4137831c80b11dd06b2369c7fb8b96cbd01b2f7b8b5e723f6dc2e0` | 106 |
| 25 | `283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb` | `4c3af70463340eab57c7ed9db6b88c2a6d64f88b2f03b058b3527573da375f70` | `4f386b130e29c032ecbef86fd06e21fcfde36c7737b8f79801c3bbcb1e307f30` | 110 |
| 26 | `00a21246f496b12f98389522d762ad6c4e10683e0eb21163b881d7b035f9c2fe` | `af61f7b9a80b95bbc15c937ff0af3eed1ecc327965679324c51c376ad9dbb836` | `29f3d9fecdc8c11273a15298310ff58b27641d58d592d0f7d49d773a65e932a4` | 100 |
| 27 | `c2809011a722b81732952d889f194549adea58875b605dbafe58ada93de9b4b9` | `e74f592f6ee907fb25712de0eb2b09359af09848d6cee458bd0a565d7a58f20e` | `276a946006d54e59f27b3abd3224f116885655c8bb9dc0df237770c8abcdd531` | 102 |
| 28 | `864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7` | `743a047cbe5f6227fbfaa5fef3169029b339af5790218df4ddf8f7cac2987f59` | `e70d9d74f0e1396938b75e7908e2f86008a5934cb635f8393bc7f5595c9774c0` | 124 |

The five `integrity-pass-receipt/1.0` files bind the anchored hashes above and
start only the continuous revision-evidence chains. They grant no edit scope;
all Stage-4 writes remain governed by the immutable roadmap, exact author
adjudication, claim-surface manifest, patch, and apply report.
