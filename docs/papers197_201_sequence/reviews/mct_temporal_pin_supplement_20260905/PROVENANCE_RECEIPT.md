# Historical author-input pin drift: append-only receipt

2026-09-05 UTC. **ONE_HISTORICAL_INPUT_PIN_CURRENTLY_FAILS /
TEMPORAL_ARTIFACTS_UNCHANGED / STAGE1_ADJUDICATION_PENDING.**

This receipt neither modifies nor replaces any frozen file in
`reviews/mct_temporal_pressure_20260905/` or the candidate author package.
The old `PINNED_INPUTS.sha256` remains exactly as frozen, including the
now-failing author-code entry. The failure is retained in the actual
`OLD_INPUT_PIN_CHECK.txt` output; that command exited 1.

## Exact version distinction

The changing working path is
`docs/papers197_201_sequence/scouting/monochromatic_triangle_20260905/probe.py`.

- Historical temporal input pin:
  `7672dea68f66714f1415fec3a507ea06b1ca1beb18c03ac65fc51753f3fea1f7`.
- Current author-frozen code:
  `1e40d08722268ab476a8687d1f0204a5dd3f5b2dc6c7046eb0d887c63d36b937`.
- Current author nonself manifest:
  `90918cef587de27f99968afbbf951b56d57f27af404a2f2b4754808f47fc97a8`.

The historical pin identifies an intermediate author-code observation,
not the later final author freeze. The original `SOURCE_OWNER_BOUNDARY.md`
already says that the author's file was a working input, but the bytes of
that working input should also have been physically preserved. Pinning its
mutable pathname without a snapshot created the present provenance defect.

The old input-pin command now gives exactly **3 PASS / 1 FAIL**. This
supplement does not describe it as four current passing pins. The old
10-entry package manifest itself still passes completely, since it pins
the historical pin-list file rather than guaranteeing that external working
paths will never change.

## Timeline and evidence strength

Tool execution order and currently observed filesystem mtimes support the
following sequence. Mtimes are ordinary filesystem metadata, not a signed
clock or standalone cryptographic proof of execution times.

| Event | Recorded UTC mtime |
|---|---|
| Original temporal RUN1 completed | 07:21:32.689454 |
| Original temporal RUN2 completed | 07:21:48.365397 |
| Temporal nonself manifest written | 07:24:02.889081 |
| Current author probe last modified | 07:24:32.449048 |
| Final author nonself manifest written | 07:27:47.325098 |

At the temporal freeze, the actual four-input checksum command returned
four OK lines in tool receipt `083f93`. The subsequent current author code
contains the additional target-only D/C local-inverse parser and the local
recurrent iff checks (current lines 120--139). Their presence was read
directly for this supplement. The current final author `REPLAY_LOG.md`
identifies its final code hash and two completed 374,812-assertion runs.
Those are author-recorded runs; this supplement does not rerun or certify
their mathematical coverage.

## Historical bytes: unavailable in the inspected archive

No authentic saved file with the historical code digest was found in the
bounded search. The complete candidate directory, current-batch files
whose basenames contain `probe`, and reachable Git history for both known
mirror layouts were inspected. `BOUNDED_OLD_BYTE_SEARCH.txt` preserves the
scope and result. This was not a search of every filesystem location or
unreachable Git object. The candidate author was separately asked whether
a real pre-change copy survives; no old bytes have been supplied to this
supplement at freeze time.

**The exact intermediate author-code bytes are missing from this supplied
archive.** Consequently this supplement cannot independently rerun that
version, verify its exact contents from the digest alone, or present a
byte-for-byte old/new diff. Chat/tool excerpts and remembered patches are
not substituted for a saved original file. No historical file is reconstructed
or relabelled as an authentic snapshot. The old pin is preserved as evidence
of which unavailable version was inspected, not upgraded into availability.

## Actual dependency and authorship boundary

The temporal contributor received the literal map and finite signal from
the parent/candidate scout, read an early author probe, and ran an early
author diagnostic before constructing its own representation. This was not
a blind research review, and no claim of never seeing author code is made.
The currently pinned intermediate author probe was also read as an input
observation after the original temporal verifier's two fresh runs.

The all-size argument in `PROOF_PACKAGE.md` is a standalone mathematical
argument from the literal map: shared-edge obstructions, stable minimum,
colour-parity no-return, the separate initially retired vertex case, and
the uniform graph construction. It invokes no author program as a lemma.
The candidate scout's checks and common discovery of the witness are
disclosed mathematical collaboration, not an independent acceptance.

The frozen `verify_mct_temporal.py` extends this contributor's own earlier
tuple-edge probe. Full source reading and the supplementary AST check find
only `collections` and `itertools` imports. There is no author import,
file-read operation, dynamic import, or execution of external code. The
script reconstructs the literal map internally and uses indegree peeling
to check every strict selector trace. Therefore the missing intermediate
author probe is not a runtime dependency of this verifier. The static check
is not portrayed as a sandbox/security attestation.

Unchanged frozen identities were checked explicitly:

| Artifact | SHA-256 |
|---|---|
| Temporal proof | `25ba4d29400ee7047fac588c3e8ba64cd55bf3782368a96bf4fb88dcbd5b85f8` |
| Temporal verifier | `8cce1feebbe5857ae3ce258856b26b0a04141d4bb8943fa6925405f00adf3295` |
| Original canonical | `8ef4b48a22d04127e71224d0f5edd43be7d4f6347621332d5b1ded2e1cb99395` |
| Original temporal manifest | `7566a9edb7e200b2a67f29fb1e609c825d89522242b0f73306c196fc57a64c1f` |
| Original input-pin list | `c987e124c592ff63f2eba5d121b1e105e1d1d71f5a27f3aeb74dfc1700900189` |

## Two new physical replays

Two separate completed Python processes ran the exact frozen verifier,
without changing its source, scope, expected output, or proof:

```sh
python docs/papers197_201_sequence/reviews/mct_temporal_pressure_20260905/verify_mct_temporal.py > docs/papers197_201_sequence/reviews/mct_temporal_pin_supplement_20260905/RUN1.txt
python docs/papers197_201_sequence/reviews/mct_temporal_pressure_20260905/verify_mct_temporal.py > docs/papers197_201_sequence/reviews/mct_temporal_pin_supplement_20260905/RUN2.txt
```

The first exited zero in tool receipt `b3ea44`, the second in `9c7595`.
Their saved output mtimes are 07:33:44.478024 and 07:34:29.226191 UTC.
Each reports 225,506 assertions and PASS. A direct byte comparison confirms
RUN1 = RUN2 = the original frozen canonical; output SHA-256 is
`8ef4b48a22d04127e71224d0f5edd43be7d4f6347621332d5b1ded2e1cb99395`.
`REPLAY_COMPARISON.txt` preserves the actual comparison results.

These runs provide fresh reproducibility evidence for the unchanged temporal
work despite the changed external author path. They do **not** recover the
missing historical bytes, erase the old input-pin failure, certify the
candidate author's expanded inverse code, or supply an independent paper
review. The independent Stage1 reviewer decides whether the provenance
defect is bounded by the preserved proof/code and current version-specific
evidence. No acceptance or new paper number is granted by this supplement.

The new `PINNED_INPUTS.sha256` records current exact versions under explicit
paths, including the unchanged old manifest/pin list and the final author
code/manifest/replay receipt. Its successful check is a **new** input check,
never a repair of the original failing one.
