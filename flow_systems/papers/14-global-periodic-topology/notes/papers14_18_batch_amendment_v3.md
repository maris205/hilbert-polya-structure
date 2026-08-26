# Papers 14--18 batch amendment v3 — five-slot fail-fast re-lock

Status: **ACTIVE / EXACT-BYTE BATCH RE-LOCK**  
Version: `P14-18-BATCH-AMENDMENT-v3.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Tracked slots: **exactly five (`14,15,16,17,18`)**  
Standalone manuscript candidates currently supported: **Paper 15 only**  
Technical Note candidates currently supported: **Paper 17 only**

This is a coordination and authorization record. It does not create a sixth
project merely because historical directories remain on disk. It authorizes
no control implementation or execution, Route A/B evaluation, composition,
manuscript, figure, release, archive, Git, or public synchronization.

## 1. Exact authority and precedence

This amendment binds the following stable records:

```text
Papers 14--18 batch design lock
  sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
batch amendment v1
  sha256:afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802
batch amendment v2
  sha256:3aa08c2cc2e38b02c83316d188f418d157abd43cf881e447cc28bf083ed3684b

replacement-P14 coordinate-transition precheck
  sha256:037dd140f53dcc8384a0d4b71bd7f3f3358b55ab6dff284fa81d63940cf5d6df
slot-14 rank-two common-quotient precheck
  sha256:63dcace23ac620b7cc5d41ac78f4c6adbdafecd77f3cec11d0a6f66401634332

replacement-P15 Phase-2 proof ledger
  sha256:7804e73863e271402b4c1331843a0cf9a1f4a06e6944b4cbb35257c0aa7d8355
replacement-P15 independent proof review
  sha256:2b889ba09b95b3d97be62780f026e4a9e3de58379eb9abb8c720c8b6cd792cc7
replacement-P15 control-design gate
  sha256:0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3

Paper-16 owner-sensitive salvage/replacement precheck
  sha256:9f50124a7c89b5164fdbf63fcea6f14f28187fb4cb559e975039a4cbab0a1bda

Paper-17 symbolic proof
  sha256:f6c7475b854b3d00b37d3e7f2edca8e8f2f15d92d67ae8bbcdcd71be127b3bb1
Paper-17 independent proof review
  sha256:9ad4817e32c6da461d7e15eee1bd53d24368b7c55751738c86c8b033caeb796e
Paper-17 control-design gate
  sha256:093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647
Paper-17 base control design
  sha256:abdc4239077b9c9a82d22ccd86e560bb6fd0850dfcfbb261cf500120555a03aa
Paper-17 control-design amendment v1
  sha256:83c8effb2dc4e79f90ef4c72cf5b8f4b20974dc21af8a02e074e19a231b0970d
Paper-17 final append-only control-design review
  sha256:42d1389171a7c23ed40657ff979a2500a8b3daade2561af54755c0c1c4339326

Paper-18 historical broad protocol
  sha256:d3fa7c262727ebb7501d09692315b1dc53dc5c3409f4fd37000cef9f22bd572e
Paper-18 historical candidate lock
  sha256:98fb74d3dd27e854af22ee31a94753b8d26d1f22e3260cec5ca977f854d6ed17
```

This amendment supersedes batch-amendment-v2's provisional positive
replacement-P14 branch. All earlier mathematical receipts remain historical
evidence, but the publication and authorization decisions below are current.

## 2. Slot 14 is stopped, not recycled into a weak paper

The coordinate-transition precheck proves that every source-permitted
fixed-prime transition is an affine translation on the compact chart
coordinate and the identity on time. All such translations are realized,
and normalized Haar is preserved. This is mathematically correct but reduces
to compact-group translation invariance after the source formulas are
unpacked.

The final rank-two attack also succeeds mathematically: the source-induced
common quotient has a complete Kummer--Ulm/Smith description. After exact
subtraction of the replacement-P15 theorem, however, its remaining content is
the formal common quotient, a finite-rank incidence matrix, a minimum of two
already-owned `kappa` tails, and finite Smith minors. The independent
standalone verdict is therefore binding:

```text
SLOT14_MATHEMATICS=PASS
SLOT14_FINDINGS=C0_M1_m0
SLOT14_FULL_PAPER=NO
SLOT14_DISPOSITION=MERGE_P15R_AND_STOP_SLOT14
```

No new slot-14 protocol, proof ledger, controls, Route record, manuscript, or
technical note may be created. The useful two-prime and finite-set formulas
may later appear only as an explicitly credited corollary or appendix to
Paper 15 after that paper's own downstream gates permit composition.

## 3. Slot 15 is the validated Full-Paper branch

The replacement-P15 proof and independent exact-byte review establish the
complete Wieferich--Ulm signature theorem at `C0/M0/m0`. The review records

```text
STANDALONE_PASS=PASS
FULL_PAPER_PLAUSIBLE=YES
MERGE_OR_STOP=false
```

The universal statement that the signature always recovers the prime remains
open and must remain open. Paper 15 advances only through its separate
post-proof control-design gate. This batch amendment neither predicts the
design bytes nor authorizes implementation or a reproduction run.

## 4. Slot 16 receives one final shared-choice fail-fast

The current minimal-ideal/Arveson-spectrum package is a correct generic
`c_0`-sum-of-circles lemma and is not a standalone rational-Witt theorem. The
old Paper-16 candidate therefore remains `NO_GO / MERGE_OR_REPLACE`.

One final source-level precheck is authorized at exactly:

```text
papers/16-arveson-prime-recovery/notes/
  phase1_shared_iota_factorization_precheck.md
```

It must bind the final coordinate-transition precheck, the slot-14 rank-two
report, the replacement-P15 proof/review, and the existing Paper-16 salvage
report. It must answer this binary question:

> After the independently realizable changes of the two lifts `x_p,x_q` are
> included together with the one global roots-of-unity choice `iota`, is the
> full paired transition image still a proper subdirect subgroupoid of the
> two fixed-prime transition groupoids, and does it carry an intrinsic
> invariant invisible on both projections?

The precheck must derive the complete arrows, identities, inverses,
composition and flow covariance. It must distinguish the compact-chart owner
from the actual packet topology and from the source-induced common quotient.
It must attack the possibility that independently realized translations make
the full image a product and erase the embedding-only compatibility.

Pass is possible only if both conditions hold:

1. the full transition image, including lift changes, is proved proper; and
2. a factor-invisible invariant survives and is not the generic P15
   common-quotient/Smith signature.

Otherwise the mandatory result is `STOP_SLOT16 / MERGE_FOUNDATION`. No new
protocol, candidate lock, proof, controls, or Technical Note is authorized by
this precheck.

## 5. Slot 17 remains the sole Technical-Note branch

The symbolic topos/quantale theorem and its proof review remain exact
`C0/M0/m0`. The control-design review's historical M1 is closed by amendment
v1: the effective design `base + amendment` now has an independent
`PASS C0/M0/m0` receipt. The exact lock-path/concurrency ordering is:

```text
recursive guard
  -> root/environment validation
  -> exact pre-existing-lock check
  -> all-other-residue scan
  -> atomic mkdir
  -> owned-lock state.
```

This amendment authorizes creation of one separate exact-byte
control-implementation gate binding the final design tuple. It does not itself
authorize implementation or execution. Paper 17 remains the sole
`TECHNICAL_NOTE_CANDIDATE`; `STANDALONE_PASS` is not manufactured.

## 6. Slot 18 receives one operator-coupling fail-fast

The positive transition result now permits a sharply narrower question, but
not the broad historical P18 protocol. A chart-enhanced measured record based
on compact `B_p` with normalized Haar is a distinct owner from the actual
indiscrete packet. If time acts only on the circle/time factor, tensoring with
`B_p` risks reducing every normalized trace to the already-owned one-orbit
formula because `integral_{B_p} 1 dmu=1`.

One final source/domain/nonredundancy precheck is authorized at exactly:

```text
papers/18-packet-haar-trace/notes/
  phase1_measured_operator_coupling_precheck.md
```

It must test whether the source supplies a canonical map, correspondence, or
operator that genuinely couples the transverse compact coordinate to literal
time evolution. It must explicitly compare the Deninger packet formulas and
the rational-Witt Frobenius/Verschiebung correspondence record with the
Paper-8 one-orbit trace and Papers 11--13 time/diagonal ceilings.

The precheck passes only if it identifies all of the following on one owner:

1. a source-induced, choice-independent measured enhancement;
2. a represented algebra and exact same map into its von Neumann owner;
3. a non-product operator or correspondence mixing transverse and time data;
4. a trace/weight calculation that fails for an arbitrary probability base
   and does not collapse after normalized Haar integration; and
5. a claim delta not already owned by the standard-circle, time-only, or
   generic-diagonal results.

If no such coupling exists in the bounded source corpus, the report must say
`NO_SOURCE_INDUCED_COUPLING / STOP_SLOT18`; it may not replace the missing map
with target Euler weights, an arbitrary chart, an arbitrary kernel, or a
generic tensor product. No versioned P18 protocol or proof is authorized
before this pass.

## 7. Exact five-slot register

| Slot | Current disposition | Next authorized gate | Publication ceiling |
|---|---|---|---|
| 14 | stopped; theorem fragments merge into P15 | none | no paper / no Note |
| 15 | proof + peer PASS | design-only controls under separate gate | Full Paper plausible |
| 16 | old candidate NO_GO | one shared-`iota` fail-fast | HOLD; stop unless strict pass |
| 17 | proof + peer + control-design PASS | one implementation-gate record | sole Technical Note candidate |
| 18 | broad protocol superseded | one operator-coupling fail-fast | HOLD; stop unless strict pass |

There are exactly five tracked slots. A stopped slot remains visible so the
batch does not silently relabel a failed idea or manufacture a replacement
without evidence; it is not counted as an active manuscript candidate.

## 8. Authorization matrix

```text
BATCH_AMENDMENT_V3_ACTIVE=true
TRACKED_SLOT_COUNT=5

SLOT14_STOPPED=true
SLOT14_MERGE_TARGET=P15R
SLOT14_PROTOCOL_AUTHORIZED=false

P15_STANDALONE_PASS=true
P15_FULL_PAPER_PLAUSIBLE=true
P15_CONTROL_DESIGN_SEPARATELY_GATED=true

P16_SHARED_IOTA_FAILFAST_AUTHORIZED=true
P16_PROTOCOL_AUTHORIZED=false
P16_PROOF_AUTHORIZED=false

P17_TECHNICAL_NOTE_CANDIDATE=true
P17_EFFECTIVE_CONTROL_DESIGN_PASS=true
P17_CONTROL_IMPLEMENTATION_GATE_CREATION_AUTHORIZED=true
P17_CONTROL_IMPLEMENTATION_AUTHORIZED=false
P17_CONTROL_EXECUTION_AUTHORIZED=false

P18_OPERATOR_COUPLING_FAILFAST_AUTHORIZED=true
P18_PROTOCOL_AUTHORIZED=false
P18_PROOF_AUTHORIZED=false

CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

## 9. Provenance DAG

This amendment is an acyclic downstream receipt:

```text
batch lock -> amendments v1/v2 -> final proof/review/precheck receipts
           -> this amendment v3
           -> P16/P18 fail-fast reports or a P17 implementation gate
           -> later independent reviews/gates, if any.
```

It does not embed its own digest. Later records must bind its final SHA-256.
