# Deterministic reproduction and control ledger

## Frozen candidate integrity

The candidate was first read only after the builder's explicit STOP/frozen
message.  Its manifest SHA-256 was

```text
c070bd76d8a28e1b918fa040d9346db32776f238e7081d8c3504648b137a583e
```

Independent parsing found 13 unique sorted entries and rehashed every entry.
The candidate's own verifier independently returned `PASS` with 13 files,
and a final `sha256sum -c` returned `OK` for every entry.  Including the
self-excluding manifest itself, the frozen tree contains 14 regular files.

The auditor snapshot is content-, size-, type-, and mode-sensitive.  Its
canonical tree digest was identical before and after the audit:

```text
before = ee3d52804910954ad62e2f3caed6295a5b9246c95fe92998a617535793105c70
after  = ee3d52804910954ad62e2f3caed6295a5b9246c95fe92998a617535793105c70
```

The complete `candidate_before.json` and `candidate_after.json` bytes are
identical, each with SHA-256
`b664daee14f263e304775571d7ff311c6d17beeb7fd3904902f4ecd465746f1e`.
Both report empty cache, symlink, and nonregular-path lists.

## Candidate-run reproduction

With bytecode writing disabled, the frozen driver was run twice using the
immutable Stage-1 input `/tmp/p49_53_phase1` and distinct auditor-owned
outputs `reproduction_1` and `reproduction_2`.  No output path was inside the
candidate.  The three evidence files from both runs are byte-identical to
one another and to the frozen candidate evidence:

```text
canonical_evidence.json  b6e7f69ca360680c21bf3d772d79ceeb543f1cb8a82d236a647206df8781c74b
input_hashes.json        620c53d713d91c74ac1519d7bce259b0728c043d383e5b13adff8cc44dd14bc0
test_results.json        99ee0fb200903772944ec05897af21ae4126bedd1df08fab6cae4bdf46772963
```

Each run returned nine assertion groups with status `PASS`.  The candidate
counts include:

- 68,288 formula-versus-hole-fill point comparisons;
- 28,764 skeleton residue classes and 1,920 high-center identities;
- 3,918 rejected prime smaller-period candidates;
- 998,025 composite direct comparisons and 99,519 nested-fill comparisons;
- 44 directives, 477 partition checks, 112 admissible partitions, and 308
  chromatic evaluations;
- 972 local-rule source/target/radius/base cases, with 132 consistent cases,
  exactly 132 quotient cases, and zero false positives or false negatives;
- all four typed negative controls accepted for their intended rejection
  reason.

The two candidate engines do not import one another; this was checked by an
auditor-owned AST pass, not by trusting module comments.

## Auditor-owned independent implementation

`independent_checks.py` imports no candidate implementation.  It separately
implements the affine exponent evaluator, iterative nested-hole evaluator,
restricted-growth directive and partition enumeration, graph coloring,
refinement, manifest parsing, and type-sensitive tree snapshot.  Its seven
sections all returned `PASS`.  Exact counts are:

```text
formula/nested point comparisons                 24,024
skeleton residue checks                           1,519
nonhole progression equalities                    1,501
essential-hole translation checks                 1,501
universal upper-bound coordinates                 3,448
prime lower-bound congruence witnesses           19,766
prime smaller-period rejections                  19,766
composite counterperiod coordinates               4,739
composite progression equalities                 80,563
high-center identities                            7,200
high-window normal forms                          1,120
directives independently enumerated                 135
partition tests                                   1,632
admissible quotients                                315
refinement-pair tests                               871
chromatic identities                                945
```

These finite checks are falsification evidence.  The unbounded theorem is
supported by `INDEPENDENT_PROOF.md`, not inferred from enumeration.

## Mutation and scope controls

The independent checker rejects:

1. an identity-letter proposal between bases `3` and `4` after finding a
   basepoint mismatch;
2. a shift map as nonpointed after finding a distinguished-point mismatch;
3. the partition `(0,0,1)` of directive `(0,1,2)` because it merges an
   adjacent pair;
4. the false all-integer-base constructive statement using the strict
   composite counterperiod `q=8<4^2` at `p=4,N=1`.

The candidate's own typed suite additionally rejects a nonsurjective letter
map.  No negative control is used to broaden the theorem beyond its frozen
same-base pointed scope.

## Evidence anchors

- `evidence/independent_checks.json`: canonical independent results.
- `evidence/candidate_before.json` and `candidate_after.json`: immutable-tree
  receipts.
- `evidence/candidate_sha256sum_check.txt`: final per-entry manifest replay.
- `evidence/candidate_verify_manifest_final.json`: final candidate-verifier
  result.
- `reproduction_1/evidence` and `reproduction_2/evidence`: two byte-stable
  reruns.

