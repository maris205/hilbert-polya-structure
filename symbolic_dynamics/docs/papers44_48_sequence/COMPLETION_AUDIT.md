# Papers 44--48 completion audit

Status: **PRE-PUSH CLEAN / TERMINAL PENDING**.

Audit date: 2026-08-19 UTC.  This record indexes the current scientific,
manuscript, Route, and local Git evidence for Papers 44--48.  The terminal
disposition is deliberately pending until the final documentation commit is
reachable from GitHub `main`, the plain mirror is synchronized, and an
independent terminal audit passes against both trees.

## Scope and interpretation

The [Phase-1 packet](phase1/) is sealed by
`e048907c8fdd02101aeeedbf7a6bd51960ac15a78c5fdae4759d2dad83701a78`
and replays 4/4 children.  The [Phase-2 packet](phase2/) is sealed by
`d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181`
and replays 10/10 children.

These packets distinguish three things that must not be conflated:

1. Paper 43's historical commissioned remainder `{SD-C03, SD-C05}`;
2. the newly opened source universe for Papers 44--48; and
3. the five objects selected only after source verification, theorem audit,
   hostile review, and the Phase-2 collision matrix.

The five papers therefore inherit no P43/C03/C05 credit.  Their selection
records establish bounded, source-controlled nonduplication, not global
priority.  Paper 45 intentionally uses the sealed identity
`P45-ALLH-RETRACTIONS`; no `SD-C47` alias was invented.

## Exact paper closure

| Paper | Current Git subtree | PDF SHA-256 | Route-A v0.2 / Route-B | Exact finite evidence | Disposition |
|---|---|---|---|---|---|
| P44 | `a8de55de93905428f3d5b898134d65d88e803923` | `3ee4b7662f9d5f8fdd6a410461c7c8094cb5c2782fbbb486603f56b9841cb66d` | `(A0_FAIL, A1_FAIL, A2_FAIL, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`; rejected; B false | primary 9/9; independent 8/8; mutations 25 cases / 54 invocations / 0 survivors | exact q-adic accumulation image, golden-control dimension and natural boundary |
| P45 | `16860356e0b232e88c65c58a562f8425a73a77fd` | `072bfb9de07b46f7705118ce8342b3f56a90fef45240ee24be33c9931b908783` | `(A0_FAIL, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`; rejected; B false | main 48 checks; independent 43; 12 hostile attacks / 24 validator calls / 0 survivors; 3 topology attacks / 9 outcomes / 0 survivors | all-h isospectral arithmetic retractions with exact nonsimilarity, Weyl, primorial, and commutator laws |
| P46 | `642f21ac8a8fa5a1073919380a01ba9aba419d18` | `8772e8c9649bea045bace7b369d446ff51f5c9a7eb95c7e1bc957a9ff2f02d6e` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`; rejected; B false | 4 cutoffs; 335,922 ordered tuples; 36 exact traces; 25 mutation families / 62 instances / 162 invocations / 0 survivors | sharp dyadic Hankel ideal walls, 2-adic product, labeled-cycle solver |
| P47 | `3dcda0f648d2f56185cafc8a5f4fddc7d08a55f2` | `b6c4d6aa27fe23f74b4c9e63628cd9b34b83d1d4d0908b040cc923af4c0ae12d` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`; rejected; B false | two implementations; 4 cutoffs; 20 trace cases/lane; 10 walk cases/lane; mutation instances 39+35+15 / 0 survivors | harmonic-quotient ideal walls and zeta--Mordell--Tornheim trace identity |
| P48 | `bf3751aeada3a424053d755c6b984d75ae6c282c` | `5bb755f9b2b0eaf56c79b8de5e94253bc9e7ed4b8d6ef9fd4c815f832cf54573` | `(A0_FAIL, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`; rejected; B false | 1,965 rows/lane; 8,010 intervals; 420 envelopes; 39 mutations / 390 invocations / 68 designated rejects / 0 survivors | all-radix Schatten surface and binary full-bad-range endpoint pinching |

The finite columns are exact replay evidence and falsifiers.  They are not the
proofs of universal, endpoint, or infinite-domain statements; those claims are
owned by each paper's frozen theorem/proof package.

## Route repairs and supersession

P44 retains its historical v0.3 record unchanged, but adds the append-only
canonical v0.2 card
[`2026-08-19.yaml`](../../papers/44-q-adic-finite-size-boundary-spectra/evaluations/route_a/SD-C46/2026-08-19.yaml).
The current primary and independent receipts report 9/9 and 8/8, and the fixed
hostile suite reports 25 cases, 54 invocations, and zero survivors.  The card
keeps science `source_commit=b0e41ac3d6bd30618421d1b76122c3e9e04d070b`;
its receipts separately bind the Route-code H1.  Publication Stage-1 remains
the historical science H1.

P45's preauthority expectation and its historical validators remain immutable
chronology.  They are explicitly superseded by the canonical v0.2 actual card,
the validation receipt, the two `code/route_actual_*` validators, the State-B
route record, and the 137-entry full-root manifest.  The actual card SHA-256 is
`e8b32b573940e1074bed01128f16b9f4689c56dd07e7341203316511b069879c`;
the validation receipt SHA-256 is
`94f44fa40e3ef60a9bfc3f693ba8cf0721f26af27881b594192ceefe875fa958`.
The validators intentionally query the trusted Git object graph to prove
science-H1 ancestry and exact committed Route-code blobs.  This is the direct
two-stage provenance proof; an extracted archive is neither represented nor
required to reproduce Git ancestry.

## Two-stage reachability

| Package | Stage 1 | Stage 2 |
|---|---|---|
| P44 science | `b0e41ac3d6bd30618421d1b76122c3e9e04d070b` | `bd6eddb937c6b5cd68014843e4b849164fdb0a8a` |
| P44 canonical Route reclosure | `56c29ac5738069e45c0d8392bac7d0beb732efcb` | `e3f468a3894731629972283e0086a98d77b7049b` |
| P45 science | `68369da38e651604cbee65df498846b863572448` | `a02828183fb144eb893694f8ed9ea2aaa6808609` |
| P45 canonical Route reclosure | `a0f840c67f5f771e9089fc538c190bf384e6f022` | `ea94d2c32113a8fdc576ae54f6625c84486125bd` |
| P46 | `47739ed48774cad00b79c27dc66e1ab6a4e36969` | `e0da119ba5b90d9854e34dceab83d93250e24bd3` |
| P47 | `c596c7b0113a06fd38658e03984b775bba7cf17f` | `c5dccdca6cd5d3a25272e6c4be076d6add3dc569` |
| P48 | `7443ec58dc14331e5931b786d721fde3a99e7a43` | `431c9e5069bc6a18e85b9c676b498d6a8786a4d1` |

The raw Phase-1/Phase-2 archive commit is
`4e99bc3bc319d801d93993f7eff9d116cd7f056d`.  The local completion chain is
linear through the four P45/P44 Route-reclosure commits shown above.  No
rebase or synthetic test OID is part of the authority history.

## Local publication and manuscript gates

- All five current PDFs reproduce byte-for-byte under fixed-epoch clean
  builds; all are A4, have embedded fonts, resolved citations/references, and
  clean strict log scans.
- Paper-specific downstream State-B audits pass on the current authority trees
  in normal and hostile environments.  P44's authenticated publication auditor
  names its success state `PUBLISHED_STATE_B_EXACT`; P45 replays its repaired
  actual Route/State-B record, while P46--P48 retain their paper-specific
  State-B integration stacks.
- Independent science replays, dual implementations, mutation suites,
  source/selection locks, proof packages, and paper-specific claim firewalls
  are closed.  The downstream documentation-closure audit also rechecked P47's
  repaired Figure 2 and P48's corrected Unicode extraction, one-sided shift
  convention, and Lucas metadata on the current PDF bytes; it does not rewrite
  the immutable upstream writer-handoff `HOLD` chronology.
- The repository worktree and index were clean immediately before this
  documentation-only closure.  P44--P48 content subtrees are unchanged by this
  documentation step.

## Terminal gates

The following items are intentionally not pre-claimed in this pre-push record:

- [ ] final GitHub `main` compare-and-swap check and push;
- [ ] verification that every Stage-1/Stage-2 commit above is reachable from
      the pushed remote head;
- [ ] exact path/kind/mode/byte synchronization to the plain mirror;
- [ ] authority and mirror publication audits in normal and hostile
      environments;
- [ ] final independent cross-paper terminal verdict.

The status may be promoted to `COMPLETE` only after all five checks are
recorded against the final remote head.  Until then, the scientifically closed
packages are **PRE-PUSH CLEAN**, while the sequence as a distributed artifact
remains **TERMINAL PENDING**.
