# Paper 45: all-`h` arithmetic fiber retractions

This directory contains the published Paper 45 science package for the
all-`h` saturated/modulo retraction experiment.  Its frozen mathematical input
is the read-only 17-file tree at `inputs/preauthority`; the unique input seal is
`4053f398c8318d09a821907ce421cb34a2adbe88efa2ac4dbfdc059e54d1e849`.
The science source remains commit
`68369da38e651604cbee65df498846b863572448`; the Route repair does not alter
the paper, proof, experiment contract, evaluator outputs, or PDF.

## Lanes

- A (`code/evaluator_a`) independently enumerates the two maps, builds actual
  finite rank-one matrices, and emits 21 finite records and zero INF records.
- B (`code/evaluator_b`) independently uses exponent states, closed fibers,
  prime-set optimization, and Euler/analytic derivations.  It emits the same
  21 finite records plus the exact ordered 15 INF certificates, each with a
  theorem AST, endpoint witness, indexed `(h,k,q,sigma,p)` Euler-factor
  enclosures, and certified 768-bit partial products. Separate typed families
  cover power-S/power-M, both commutator products and their difference,
  Tauberian inversion, Weyl C/D/eigen constants, primorial regimes, and the
  free-UFD clone.
- P (`code/proof_auditor`) reconstructs all proof and analytic anchors from
  the frozen proof/source corpus, parses and binds section bytes plus
  normalized formula/operator/quantifier ASTs, and independently parses typed
  all-`h`, operator-form, strict-domain, witness, and conclusion nodes. It
  derives each certificate's domain/witness/conclusion triple from those
  nodes, rebuilds every analytic family, recomputes its witnesses at 320
  decimal digits, and enforces B-to-P owner and three-hash closure case by case.
- X receives only finite-only sealed views.  It never receives an infinite
  certificate.
- T/S/I/G enforce recursive schemas, source ownership, physical independence,
  and path/transaction integrity.  The historical validators in
  `code/route_main` and `code/route_independent` validate only the frozen
  preauthority expectation.  The actual-record validators in
  `code/route_actual_main` and `code/route_actual_independent` independently
  enforce the canonical Route-A v0.2 record and its two-commit provenance.

Both A and B contain their own raw JSON token-pair duplicate hook, strict
canonical-integer grammar, 13-row serialization-grid executor, RFC8785 JCS
construction for the string-only AST domain, and SHA-256 recomputation.
Neither imports a shared production module.

## Safe execution

Never execute the sealed candidate itself.  First make a disposable copy:

```bash
clone=$(mktemp -d /tmp/paper45-audit-XXXXXX)/candidate
cp -a /tmp/paper45_integration_candidate "$clone"
printf '%s\n' '{"purpose":"paper45-disposable-clone-v1"}' \
  > "$clone/.paper45-disposable-root.json"
chmod 0444 "$clone/.paper45-disposable-root.json"
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  "$clone/code/integration/run_integration.py" \
  --root "$clone" --phase PRE_CERT
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  "$clone/code/integration/run_integration.py" \
  --root "$clone" --phase FINAL
```

`PRE_CERT` performs no output write.  `FINAL` constructs exactly eight
read-only result files in a sibling stage, validates schemas, semantics,
mechanical report reconstruction, and the self-excluding manifest, then
installs with one same-filesystem directory rename.  Repeating `FINAL` on an
identical target performs zero physical replacements.  The registered late
failure can be tested only on a fresh disposable copy:

```bash
python3 -B "$clone/code/integration/run_integration.py" \
  --root "$clone" --phase FINAL --force-late-failure
```

It must exit 2 with `FORCED_LATE_PREINSTALL_FAILURE` and leave no `results`
or stage while preserving the full frozen metadata tuple.  The external
auditor is likewise run only against a disposable or output-free candidate:

```bash
python3 -B "$clone/code/external_auditor/frozen_mutation_auditor.py" \
  --root "$clone"
```

It independently applies all 75 rows to fresh physical clones and then runs
eight recursive schema attacks plus 32 physical audit reproductions: the
original nine, 15 proof-source edits, and eight reclosed analytic AST/output
edits. None of those extra attacks is counted as a frozen registry row. Consumers are
never passed a mutation ID or expected code and never read the registry; only
the harness performs the immutable registry comparison.

## Actual Route-A v0.2 disposition

`GO_EVALUATED` in `results/evaluation_report.json` is the external scientific
disposition; it is not a Route terminal.  The actual record is
`evaluations/route_a/P45-ALLH-RETRACTIONS/2026-08-19.yaml`, under the sealed
scientific contract ID `P45-ALLH-RETRACTIONS`.  No authority evidence assigns
Paper 45 the guessed label `SD-C47`, so this repair does not invent one.

The actual tuple is
`(A0_FAIL,A1_FAIL,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)`, the overall
verdict is `ROUTE_A_REJECTED`, and Route B remains locked (`false`).  The
record follows canonical Route-A v0.2 section 8 exactly: it has 19 top-level
keys, its nine-key `source_lock` has no provenance extension, and its sole
`source_commit` is the unchanged science H1.  Renderer provenance does not
belong to the Route record schema.  Instead, the H2 validation receipt and
`.paper45-publication-state/ROUTE.json` bind the later remediation H1 and its
six committed renderer/template/validator/test blobs.  Renderer, main
validator, independent validator, and hostile harness use the pinned regular
`/usr/bin/git` binary with `--no-replace-objects`, a minimal non-inherited Git
environment, and an exact six-row `100644 blob` tree/byte replay.  Each
consumer executes a fail-closed ancestry check from the frozen science H1 to
that remediation H1.  Three fixed topology controls are mandatory rejects:
an ordinary identical-blobs orphan, the same orphan under a hostile `PATH`
fake Git, and the same orphan behind a replace ref that points to a
science-descended surrogate.  The record and receipt are generated only after
that H1 exists and are closed as derived H2 artifacts; this avoids
self-reference and avoids attributing new code to the old science H1.
