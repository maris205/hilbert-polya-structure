# Paper 27 Stage 4-prime revision log — implementation round 1

Date: **2026-08-30**

Revision-chain round: **2**

| Item | Stage-3-prime residual | Author triage | Authorized operations | Landed result |
|---|---|---|---|---|
| `REV-03` | `must_fix` | `will_address` | `B0040/replace_block`; `B0041/replace_block`; `B0042/replace_block` | Original registered paragraphs retained byte-for-byte; fresh boundary/provenance blocks `B0108`, `B0109`, and `B0110` added; item `RESOLVED` |

## Authority receipt

- Batch request SHA-256:
  `d2e94cd10b1ca12204c8747b5bc0895f6c642e3a3ff7c08194016ed62fd461ec`.
- Unified raw author-event SHA-256:
  `fc4de4ab870bcb6ff3f1c0c9fc6eb9f389edbfbb2d6b01a79a063d21f80365dd`.
- Author choices SHA-256:
  `cf71b46158714d0c30190fc25473ea8c353668f49f253cb0a4ffeb85ce9eac72`.
- Validated adjudication SHA-256:
  `cf6168fc4e0e0f6759236667497631ee86f8bfbe5d873896ff7cf242b5f0bed1`;
  decision digest
  `7b743532aee12799873348ab7ea9a14f45572ddeba8cbeedf503dda094388f51`.
- Claim-strength replacements: `0`; collateral operations: `0`.

## Mechanical application

- Base anchored draft SHA-256:
  `b445b5c8350439e97f6be415c2ea99c948114cb241c3ccb084e5f8263e61be8f`.
- Patch SHA-256:
  `d192894bca6de7655383edf59ed4712c6b42a511be7a0e216db58f87af7907ba`.
- Revised anchored draft SHA-256:
  `803d9e7d69c233363d912b4fee25f5915b7f07d48937b794ee11c807ca182ef7`.
- Apply-report SHA-256:
  `a9a127bec6e2436bdeea73a347ae456ebdd6ed210727f1c89375f1f2a928ab58`.
- Three authorized operations applied; structural flags `false`; section-count
  delta `0`; 104/107 original blocks remain byte-identical.
- Marker-stripped word count: 5,698 to 5,829 (`+131`); bibliography-key set
  and heading sequence unchanged.
- Token conservation: `PASS`, with no number, citation, or protected-term
  delta and no advisory row. Receipt SHA-256:
  `3c38674612a52c7891ea76d581f9f8e30d24d0e9809ffa0db1599c6ced7d8f65`.
- All 10/10 registered ClaimIntent surfaces replay byte-exact and exact-once.
  P27 contributes 10 surfaces to the frozen 51-surface batch population.

## Support and preview validation

- Existing support was replayed read-only: 8/8 tests passed (5 legacy and 3
  direct), and the canonical verifier passed 24 order cross-checks and 21
  bonding transitions over 24 rows. Support receipt SHA-256:
  `ee3d3bc1635c6d4258c420732e22dbe875dc437bca788a5d9095d993dd9f00de`.
- The revision now states the exact assurance boundary: the high-level order
  searches are separately implemented, but they share the scalar-sign and
  matrix-multiplication kernel. The pre-existing `-I` fixture is branch
  coverage only and adds no owner or canonical row.
- The revision-stage E6 audit reviewed every fresh paragraph and passed with
  an explicit completeness boundary. It is not the mandatory Stage-4.5
  integrity pass.
- The isolated marker-stripped preview passes on 13 A4 pages with zero
  undefined citations/references, missing glyphs, fatal errors, or overfull
  boxes. Preview PDF SHA-256:
  `55613905b6041a3a47377630c0ab92004739d754614015b947397e4d87b9b93a`.

## Evidence and frozen-state boundary

- Continuous two-round revision-evidence bundle SHA-256:
  `c2fb508efd2f9daa2f8ac6df90fcd2cea247d6175f0265e0071284e143236484`;
  official bundle replay `PASS`.
- Stage-4-prime evidence package SHA-256:
  `76f4c131152734a8d54bd956cd2c121a353862b14888c624650130b7a8660bab`;
  every bound local path/digest replays.
- Canonical `paper/manuscript.tex` remains
  `c2809011a722b81732952d889f194549adea58875b605dbafe58ada93de9b4b9`;
  canonical `paper/paper.pdf` remains
  `540403e2cfb3c893822f3bcb80fb56e33bff00970f340df3dc9e6e8d2810d65a`;
  the canonical Round-2 result tree remains
  `04d212196398835e0a07cf699fb2b30f06164827697af8270c0c4b8475c07413`.
- The frozen coordinatewise geodesic flow, `Gamma(3 n!)` tower, common
  arclength clock, both rejected Route-A tuples, and Route-B prohibition are
  unchanged. The unchanged Route crosswalk SHA-256 is
  `3e9c51110ee310de3fb43bf8fa76b6591129262404919193431f7413a22c53b3`.

Stage 4-prime is complete within its exact authority. Stage 4.5 has not been
invoked and remains the next mandatory scholar-confirmation checkpoint.
