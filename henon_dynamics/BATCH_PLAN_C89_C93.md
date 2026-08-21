# Adaptive batch plan: HCS-C89 through HCS-C93

Status: **round complete; five packages prefreeze-verified and release-ready**

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round keeps the frozen named-label model from C75 and the exact
first-passage atlas from C88.  Every result is finite, source-bound, and
reproducible; no arithmetic/local-data, Euler-factor, root-number,
automorphy, full Burnside/table-of-marks, or Hilbert--Polya claim is allowed.

## Research sequence

1. **C89 - first-passage moments and cumulants.** Derive exact raw,
   factorial, central, and tail moments for all twenty target variables from
   the C88 laws, with independent survival-sum and probability-generating
   function checks.
2. **C90 - pairwise first-passage coupling.** Count the exact joint survival
   array for every ordered target pair by nested prefix supports; certify
   mixed moments, covariance, and the 400 marginal consistency identities.
3. **C91 - incomparable-target race atlas.** For all unordered incomparable
   subgroup pairs, compute exact first-hit race, tie, minimum-time, and
   completion-time laws using pivotal prefix edges and joint survival counts.
4. **C92 - label sensitivity of first passage.** Quantify each label's exact
   random-order pivotal probability, pivotal-rank moment, and Shapley-style
   first-passage contribution for each target; prove the efficiency identities.
5. **C93 - effective-orbit quotient of first-passage laws.** Induce the
   faithful order-1920 label action on the twenty subgroup targets and certify
   orbit representatives, equivariance of C88/C89 laws, and transport of C92
   label sensitivities.

## Dependency boundary

All five packages read only frozen C75/C76/C83/C85/C88 evidence and their
prefreeze manifests.  C89, C91, and C92 are independently regenerated from
their source receipts.  C90 additionally reads the completed C89 receipt as
an explicitly hash-bound marginal/mixed-moment check.  C93 may read the
completed C92 receipt only as a downstream sensitivity-transport check; its
core target-orbit and law checks are independently regenerated from
C75/C76/C88.

## Release gate

Each package must provide a research question, source audit, theorem package,
producer, independent checker, symbolic or finite cross-check, clean replay,
hostile mutation audit, deterministic two-pass LaTeX build, evidence hash,
manifest hash, PDF hash, and explicit scope nonclaims.  All five package gates
pass; repository release closure is recorded by the clean commit and push of
this batch.

## Gate and artifact ledger

| paper | gate result | hostile mutations | evidence SHA-256 | manifest SHA-256 | PDF SHA-256 |
|---|---|---:|---|---|---|
| C89 | producer/checker/SymPy/replay PASS | 13/13 | `86a589505280721590674235626ddc21e37d57c891c726c7e6fbba98b2bd3af9` | `81daf852ce48765f5804b675133e77cb086ae2ee94f3973237ec3ce6d5c3b16e` | `5f7d98c1a62a8bb1ebe2ffaf88cb9331ea1f53d2fe89dc816ca3463f9e9c797b` |
| C90 | producer/checker/SymPy/replay PASS | 13/13 | `c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978` | `4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737` | `d1dcd62d535729aa36c6c173421c7e5ff9789d6520c464da6be3dfc23ae55af3` |
| C91 | producer/checker/SymPy/replay PASS | 16/16 | `36b0fffda585ea483ba5603101c83c361b85ca4ba9a49c878f1e366d3c13ff0f` | `542de9625733b94e9aaec3f430d048d8878f6fe1b556e2f0493b5c7a50a31495` | `468d2f66b2296bd96a05760cc6d70e25e850d94b89c9bafa17fc0040a162b26b` |
| C92 | producer/checker/SymPy/replay PASS | 12/12 | `902d6b2fd688abc525d2fab187559bfc9904c7f3c97dc51af62050586d145812` | `ca0c6435c6a69c845ae663f25ff3fcc002c2b6ea119c14b8205da2c529594642` | `960f7c5869ed49a40f21cf22dd5eb2c1a14b652b982ce0ee69407454406b4a95` |
| C93 | producer/checker/SymPy/replay PASS | 10/10 | `4104f181b88d83666c9fcff814a7029a148c498e6393ad181c60fe5133adb9fe` | `a60e0855482e205b0174281c4a20b8f86d2eb9531a3f980cb76d92fcfb77c608` | `956588842f57ec297299fd12c4de52bd37d2d3d9b6a4eaeec9e10f81790bcc20` |

## Round-wide release checklist

- [x] C89-C93 evidence receipts pass independent reconstruction and replay.
- [x] C90's C89 dependency and C93's C92 transport dependency are hash-bound.
- [x] C75 ambient order 11520 and C76/C93 effective order 1920 remain distinct.
- [x] All package manifests list their complete non-excluded file sets.
- [x] Scope firewall and all arithmetic/operator nonclaims remain explicit.
- [x] Repository index and batch plan are updated for the five-paper round.
