# Paper 45 pre-output smoke report

Status: `PREOUTPUT_HOLD_FOR_INDEPENDENT_STATIC_AUDIT`.

Every executable check below ran in a fresh disposable `/tmp` clone bearing
the exact disposable-root marker.  The candidate itself has no marker, no
`results`, no stage, and no Python cache, so its production driver refuses to
run.

## Frozen intake and science

- Frozen input tree: 17 files; all 16 self-excluding members verified.
- Frozen input seal:
  `4053f398c8318d09a821907ce421cb34a2adbe88efa2ac4dbfdc059e54d1e849`.
- A: 21 finite records, zero infinite records.
- B: the independently reconstructed same 21 finite records plus exactly 15
  C-sorted analytic records; theorem-set hash
  `6401b141f7b46b0f7275ec124ec571542655b9874cfa9aa5c7123108577e8a84`.
- Every B analytic record contains a canonical serializable theorem AST,
  frozen endpoint/witness provenance, and typed indexed local-factor families
  with 768-bit certified partial-product enclosures. The exact Proposition-4
  power-S/power-M factors, both commutator Euler products and their certified
  difference, Tauberian F=zeta*G/inversion data, C/D/eigen constants,
  primorial three regimes, and a full free-UFD negative-control clone are
  explicit. The free-UFD formulas record an independent atom namespace and
  `rational_prime_semantics=false`.
- P independently rebuilt all 15 obligations from the frozen proof/source
  corpus, bound the main/relevant section bytes and normalized
  formula/operator/quantifier ASTs, and independently parsed typed all-`h`,
  operator, strict inequality, endpoint, witness, and conclusion nodes. Each
  domain/witness/conclusion triple is rendered from the selected typed claim,
  with no imported B metadata table. P also evaluated every local factor and
  partial product at 320 decimal digits. Result: 15/15 PASS with exact B/P
  owner and payload/proof/analytic hash closure; overall PASS iff every case PASS.
- An independent 1400-bit `arb` truth sweep checked every sampled prime in
  the exact power-S/power-M, commutator A/B, Weyl D/eigen, and all four
  sigma-one crossover families; every check passed 5/5.
- T and X independently expanded every `DIRICHLET_POWER` AST at at least 245
  and 250 decimal digits, respectively, and proved containment in the required
  eigenvalue intervals.
- X finite-only result: exact mismatches 0, interval mismatches 0, PASS.
- Cold A projection seal:
  `ba3f374f1e65e3598c7d4e769144514e911f5be268ae36afc90000df5a5154da`.
- Cold B projection seal:
  `ac8226e8d9a726ebf78e753d66b19e200ba382a5ecdc926ff79a262c7c81a675`.

## Semantic mutations and hostile audit

- No consumer accepts a mutation ID, expected code, or consumer set, and no
  consumer reads the mutation registry.  The harness alone reads the frozen
  registry, physically mutates a case/output/Route/filesystem artifact, calls
  the ordinary validator, and compares its derived fixed code.
- Internal semantic suite: all 75 rows killed; all 168 exact designated calls
  returned exit 2 and the exact row code.  Mutation-bundle SHA-256:
  `8042263d0ddd43b3b2c8c27737c10a053b422e1dfbf9667f292a4b5bba4f147b`.
- M048 invoked the real production `FINAL --force-late-failure` path after a
  complete eight-file stage passed schema, semantic, manifest, and report
  reconstruction checks.
- Independent external harness: 75/75 rows killed in 168 physical calls;
  8/8 strict schema attacks killed (Boolean/integer, float/integer,
  string/Boolean, unknown/missing key, output/common-case order, duplicate
  case ID).
- Thirty-two additional physical audit reproductions were killed. They
  include all 15 proof-source mutations, eight reclosed analytic AST/output
  mutations, and the original nine transaction/integrity reproductions:
  `tau999999+remanifest`, X Boolean count with dishonest PASS, missing required
  eigen interval, analytic endpoint drift, per-case HOLD rerendered as PASS,
  false integrity Boolean with PASS, forged registry plus remanifest, Route
  zero source hash plus nested extra key, and hostile TMPDIR sentinel.
- The analytic negatives reclosed the payload, analytic-derivation, and
  certificate hashes after changing `sigma>0` to `sigma<=0`, fabricating both
  witness copies, reversing the conclusion, or making the trace endpoint
  non-strict. Normal P still rendered HOLD from its typed proof semantics.

Both evaluators independently ran the 13-case raw serialization grid.
Duplicate JSON members were rejected by token-pairs hooks before object
construction; unique-key reorderings canonicalized; numeric/Boolean integer
confusions failed; stored RFC8785 JCS text and SHA-256 were recomputed.

## Transaction and reproducibility

- `PRE_CERT` passed with zero outputs.
- First cold `FINAL` installed exactly eight mode-`0444` files by one sibling
  directory rename.  Result-manifest seal:
  `2fae66ff866b63e7119fce7b86c928f589570572728cae942d758f4e599ad734`.
- Integrity-ledger SHA-256:
  `fef14966637e160367f545e7c6ee9f53399c6f3de3f6a01b74614ac3bff94c9b`.
- Every installed file and the directory used deterministic canonical mtime
  `1787011200000000000` ns, enabling an exact fresh rebuild comparison.
- The explicit second `FINAL` did not trust the target manifest: it rebuilt
  all eight files from frozen inputs/code in a fresh sibling and compared
  bytes plus recursive `(path,file_type,sha256,size_bytes,mode,mtime_ns)`.
  Result: identical, zero replacements.
- A real forced-late run against an already installed target returned exit 2
  `FORCED_LATE_PREINSTALL_FAILURE`; the target manifest seal and recursive
  metadata remained unchanged.
- The supplied preexisting-target tamper sweep changed and remanifested each
  of seven target artifacts. Every run returned `TARGET_EXISTS_DIFFERENT`,
  removed its fresh sibling stage, and preserved the attacked target's exact
  recursive metadata.
- All temporary-directory calls use explicit `/tmp`; a hostile
  `TMPDIR`/`TMP`/`TEMP` sentinel remained byte- and metadata-identical.

These are pre-output experiment checks only.  They do not authorize or claim
an authority, paper, root README, mirror, registry, or Git write.  The sole
next step is independent review of the new static pre-output seal.
