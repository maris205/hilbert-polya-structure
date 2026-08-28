# Stage 2 report — Papers 92–96

Status: **five theorem-bearing manuscripts and PDFs generated**.  
External release: **HOLD**.

## Artifact census

| Paper | Current pages | Concrete landed advance | Deterministic control |
|---:|---:|---|---|
| P92 | 6 | weighted Singer compression to two characteristic factors, all periodic data, mixing/MME boundary, and first-anomaly recovery of `(q,r)` | 258 exact full-matrix/finite-field assertions in five lanes including `F_4` |
| P93 | 7 | pathwise image/fibre normal form, exact quenched rates and synchronization, and a three-regime annealed law with thresholds `1/(b+1)` and `1/2` | 265,861 exact integer/rational assertions; 5 floating diagnostics excluded |
| P94 | 7 | marker recognizability, minimal aperiodicity, affine two-tower measure bijection, bias interval, and `n`/`n^2` products | 90,509 exact marker/incidence/inverse-limit assertions; 1 floating diagnostic excluded |
| P95 | 4 | exact initial period ledger, least-period parameter recovery, and iid color-return renewal on the cited Cayley presentation | 5,031 exact graph/period/return assertions plus 99,058 literal cyclic words |
| P96 | 8 | exact-cardinality fixed subsets, parity collapse, alternating zeta, temporal census, `k=1` boundary, entropy control, and rigidity | 7,000 exact coefficient/zeta/temporal assertions plus 189,245 literal subsets |

The packet contains **32 pages** and **368,659 exact assertions**. Final byte
counts and digests, which were deferred at the Stage-2 checkpoint, are now
recorded in `FINAL_QA_REPORT.md` and `CANONICAL_PDF_MANIFEST.sha256`.

## Paper packages

- [`papers/92-primitive-recurrence-avoidance-shifts/`](../../papers/92-primitive-recurrence-avoidance-shifts/)
- [`papers/93-random-push-pop-stack-cocycles/`](../../papers/93-random-push-pop-stack-cocycles/)
- [`papers/94-marked-symmetric-s-adic-shifts/`](../../papers/94-marked-symmetric-s-adic-shifts/)
- [`papers/95-minimal-slack-no-repeat-shifts/`](../../papers/95-minimal-slack-no-repeat-shifts/)
- [`papers/96-finite-subset-circle-expansion/`](../../papers/96-finite-subset-circle-expansion/)

Each package contains an anonymous `amsart` manuscript, a cited-only
bibliography, canonical PDF, runnable exact control, build instructions, and a
claim/evidence map. Each frozen package now also contains its hostile-review,
final-QA, and checksum files. No target venue is named.

## Claim discipline

- P92 credits primitive-polynomial/Singer/LFSR and generic SFT machinery; its
  residual theorem concerns the nonzero-discrepancy relation and delayed
  spectral anomaly.
- P93 credits bicyclic-monoid and reflected-walk theory; its residual theorem
  is the exact coupling to symbolic images/fibres and the full annealed
  trichotomy.
- P94 explicitly does not claim the reciprocal-sum transition mechanism; it
  solves one marked symbolic realization completely.
- P95 removes the Ruskey--Williams Cayley graph from its contribution and
  retains the no-repeat period and color-renewal package.
- P96 treats orbit-union and finite-to-one entropy mechanisms as general
  inputs and retains the circle-specific rational collapse, parity zeta,
  temporal census, and rigidity.

Writing-level source details are in
[`phase2/SOURCE_VERIFICATION_REPORT.md`](phase2/SOURCE_VERIFICATION_REPORT.md).
