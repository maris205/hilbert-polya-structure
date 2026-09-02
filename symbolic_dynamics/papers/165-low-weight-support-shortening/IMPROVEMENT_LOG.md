# P165 improvement log

External status remains `HOLD_EXTERNAL` throughout.

## Round 0

- Frozen PDF: `main_round0_original.pdf`
- SHA-256:
  `f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a`
- Hostile Review A verdict:
  `ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 minor`

## Independent Review-A controls

- The reviewer rederived strict descent, distance doubling, the sharp
  height, the every-time image equivalence, both universal source lower
  bounds, and the simultaneous-equality classification and count.
- The zero target, time zero, empty ambient space, full-support targets,
  post-cap times, and the strict `<2d` selector boundary were audited
  separately.
- An independent verifier checked 1,574,098 assertions over 32,805 code
  states and 43,357 equality sources.  Two fresh transcripts were
  byte-identical at SHA-256
  `66de01f2399047e6a32d9b22d508be9eab56fd14b62b3e766991d0b28d5b25e7`.
- The one-step low-weight hitting-set shortening owner was fully subtracted;
  the reviewer found no direct owner for the residual iterated targetwise
  contract and no P1--P164 proof-engine transfer.

## Round 1 freeze

No theorem, proof, source, bibliography, or PDF repair was requested.
Consequently `main.pdf`, `main_round0_original.pdf`, and
`main_round1.pdf` are byte-identical, four-page artifacts at SHA-256
`f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a`.
Both review cold builds matched that PDF; warning, font, metadata,
anonymity, and all-page visual QA passed.  Round 1 is ready for a different
Hostile Review B.

## Independent Review-B controls

- A different reviewer independently rederived the full theorem package,
  including every edge case and the simultaneous-equality inverse atlas.
- Its separate implementation checked 1,220,460 assertions over true
  `F_2`, `F_3`, `F_4`, and `F_5`, 37,193 labelled codes, and 215,030
  target--time interfaces.
- Two fresh transcripts were byte-identical at SHA-256
  `3a593364f3a30a18bf76fe1611dad2a8330a57772cd466afd8d672cda238da04`;
  the verifier SHA-256 is
  `987e913be21a91d7f612bf158f14d84c0b597950e215a870c4d0405280685b54`.
- The one-step owner was again fully subtracted, with no direct owner for
  the autonomous all-time target contract and no internal literal or
  proof-engine collision.

## Round 2 freeze

Review B returned `ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 minor` and
requested no source repair.  `main.pdf`, `main_round0_original.pdf`,
`main_round1.pdf`, and `main_round2.pdf` are byte-identical four-page
artifacts at SHA-256
`f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a`.
Both additional source-only cold builds and all mathematical, warning,
font, metadata, anonymity, all-page visual, and `HOLD_EXTERNAL` checks
passed.  The internal Round-2 artifact is frozen.
