# Papers 44–48 sequence-selection provenance

Status: **PRE-PUSH CLEAN / TERMINAL PENDING**.

This directory makes the two frozen selection packets for Papers 44–48
Git-reachable.  It preserves the research-gate chronology; it does not create
novelty, priority, Route, or publication credit.

## Sealed packets

| Packet | Manifest SHA-256 | Replay |
|---|---|---|
| [Phase 1](phase1/) | `e048907c8fdd02101aeeedbf7a6bd51960ac15a78c5fdae4759d2dad83701a78` | 4/4 children verified |
| [Phase 2](phase2/) | `d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181` | 10/10 children verified |

Replay from this directory:

```sh
printf '%s  %s\n' \
  e048907c8fdd02101aeeedbf7a6bd51960ac15a78c5fdae4759d2dad83701a78 \
  phase1/SHA256SUMS.txt | sha256sum -c -
(cd phase1 && sha256sum -c SHA256SUMS.txt)

printf '%s  %s\n' \
  d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181 \
  phase2/SHA256SUMS.txt | sha256sum -c -
(cd phase2 && sha256sum -c SHA256SUMS.txt)
```

## Chronology and source-universe boundary

The Papers 1–43 selection baseline is commit
`6e5658649d2eab0fce077cbcdcc00070dd54095f`.  Paper 43 commissioned the
working set `{SD-C02, SD-C03, SD-C05}` and retrospectively selected `SD-C02`.
The residual `{SD-C03, SD-C05}` is a historical workflow remainder, not a
mutable registry, ranking, or successor authorization.

[Phase 1](phase1/CANDIDATE_UNIVERSE_AND_SEQUENCE_GATE.md) separates historical
registry membership, a commissioned remainder, and a newly proposed source
universe.  A different object is therefore `NEW_SOURCE_UNIVERSE` and inherits
no C03/C05/P43 A0, factor, novelty, priority, or Route credit.  Phase 1 also
allowed `STOP_AT_k`; it did not pre-authorize five papers.

[Phase 2](phase2/REPLACEMENT_CANDIDATES.md) preserves the withdrawn/merged
finite-prime-square and perfect-power-product proposals.  Its
[final gate](phase2/FINAL_SEQUENCE_GATE.md),
[collision matrix](phase2/CLAIM_COLLISION_MATRIX.md), and
[hostile review](phase2/DEVILS_ADVOCATE_CHECKPOINT_2.md) freeze five distinct
central theorem positions only after shared Schur, summability, pinching,
Schatten, Euler, and determinant techniques are subtracted.  The bounded
literature disposition remains `PRIMARY_METADATA_VERIFIED /
EXACT_ABSENCE_NOT_PROVED`; no bounded search is promoted to global priority.

## Final paper identities and evidence

| Paper | Authority identity | Distinct residual theorem | Source / selection | Current Route evidence |
|---|---|---|---|---|
| P44 | `SD-C46` | exact q-adic increment/remainder/accumulation image; golden-control Cantor dimension and natural boundary | [lock](../../papers/44-q-adic-finite-size-boundary-spectra/preauthority/SOURCE_LOCK.md) / [selection](../../papers/44-q-adic-finite-size-boundary-spectra/preauthority/SELECTION_AND_PROVENANCE.md) | [canonical v0.2 card](../../papers/44-q-adic-finite-size-boundary-spectra/evaluations/route_a/SD-C46/2026-08-19.yaml), [primary](../../papers/44-q-adic-finite-size-boundary-spectra/evidence/route_v0_2/PRIMARY_AUDIT.json), [independent](../../papers/44-q-adic-finite-size-boundary-spectra/evidence/route_v0_2/INDEPENDENT_AUDIT.json) |
| P45 | `P45-ALLH-RETRACTIONS` | all-h paired arithmetic retractions with common spectrum but exact similarity, Weyl, primorial, and commutator separations | [lock](../../papers/45-isospectral-arithmetic-fiber-retractions/inputs/preauthority/SOURCE_LOCK.md) / [selection](../../papers/45-isospectral-arithmetic-fiber-retractions/inputs/preauthority/SELECTION_AND_PROVENANCE.md) | [canonical v0.2 card](../../papers/45-isospectral-arithmetic-fiber-retractions/evaluations/route_a/P45-ALLH-RETRACTIONS/2026-08-19.yaml), [validation receipt](../../papers/45-isospectral-arithmetic-fiber-retractions/evaluations/route_a/P45-ALLH-RETRACTIONS/VALIDATION_RECEIPT.json), [State-B route](../../papers/45-isospectral-arithmetic-fiber-retractions/.paper45-publication-state/ROUTE.json) |
| P46 | `SD-C48` | dyadic-sum Hankel sharp ideal walls, 2-adic block product, and complete fixed-label cycle solver | [lock](../../papers/46-dyadic-sum-hankel-cycle-calculus/preauthority/SOURCE_LOCK.md) / [selection](../../papers/46-dyadic-sum-hankel-cycle-calculus/preauthority/SELECTION_AND_PROVENANCE.md) | [primary](../../papers/46-dyadic-sum-hankel-cycle-calculus/outputs/audits/route_primary.json) / [independent](../../papers/46-dyadic-sum-hankel-cycle-calculus/outputs/audits/route_independent.json) |
| P47 | `SD-C49` | harmonic-quotient graph ideal walls and zeta–Mordell–Tornheim trace identity with mixed-cycle sign witness | [lock](../../papers/47-harmonic-egyptian-mordell-tornheim/preauthority/SOURCE_LOCK.md) / [selection](../../papers/47-harmonic-egyptian-mordell-tornheim/preauthority/SELECTION_AND_PROVENANCE.md) | [primary](../../papers/47-harmonic-egyptian-mordell-tornheim/outputs/audits/route_primary.json) / [independent](../../papers/47-harmonic-egyptian-mordell-tornheim/outputs/audits/route_independent.json) |
| P48 | `SD-C50` | all-radix carry-free Schatten surface and binary full-bad-range endpoint pinching | [lock](../../papers/48-all-radix-carry-free-schatten/preauthority/SOURCE_LOCK.md) / [selection](../../papers/48-all-radix-carry-free-schatten/preauthority/SELECTION_AND_PROVENANCE.md) | [main](../../papers/48-all-radix-carry-free-schatten/outputs/evaluations/main_evaluation.json) / [independent](../../papers/48-all-radix-carry-free-schatten/outputs/evaluations/independent_evaluation.json) |

P45 deliberately has no invented `SD-C47` alias.  The sealed contract ID
`P45-ALLH-RETRACTIONS` is the only authority identity for its actual record.

## Two-stage Git provenance

| Paper | Stage-1 content/static commit | Stage-2 derived/seal commit |
|---|---|---|
| P44 science | `b0e41ac3d6bd30618421d1b76122c3e9e04d070b` | `bd6eddb937c6b5cd68014843e4b849164fdb0a8a` |
| P44 Route-v0.2 reclosure | `56c29ac5738069e45c0d8392bac7d0beb732efcb` | `e3f468a3894731629972283e0086a98d77b7049b` |
| P45 science | `68369da38e651604cbee65df498846b863572448` | `a02828183fb144eb893694f8ed9ea2aaa6808609` |
| P45 Route-v0.2 reclosure | `a0f840c67f5f771e9089fc538c190bf384e6f022` | `ea94d2c32113a8fdc576ae54f6625c84486125bd` |
| P46 | `47739ed48774cad00b79c27dc66e1ab6a4e36969` | `e0da119ba5b90d9854e34dceab83d93250e24bd3` |
| P47 | `c596c7b0113a06fd38658e03984b775bba7cf17f` | `c5dccdca6cd5d3a25272e6c4be076d6add3dc569` |
| P48 | `7443ec58dc14331e5931b786d721fde3a99e7a43` | `431c9e5069bc6a18e85b9c676b498d6a8786a4d1` |

The P45 preauthority expectation and its historical validators remain frozen
chronology only.  The authoritative actual stack is the v0.2 card and
validation receipt above, the two `code/route_actual_*` validators,
`.paper45-publication-state/ROUTE.json`, and its 137-entry full-root manifest.
That stack intentionally queries the Git object graph to prove science-H1 to
renderer-H1 ancestry and exact committed blobs.  Git ancestry is direct
two-stage provenance; this project does not replace it with, or claim, an
archive-only ancestry proof.

Finite computations are diagnostics and falsifiers.  The frozen proof
packages own universal, endpoint, and infinite-domain statements.  See the
[completion audit](COMPLETION_AUDIT.md) for exact current counts, hashes, and
the remaining push/mirror terminal gates.
