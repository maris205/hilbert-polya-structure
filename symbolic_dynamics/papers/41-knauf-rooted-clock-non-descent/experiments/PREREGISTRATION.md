# SD-C43 authority-integration preregistration

status: `FROZEN_BEFORE_AUTHORITY_CODE_AND_RESULTS`

date: `2026-08-17`

candidate: `SD-C43`

## 1. Timing and chronology

This is a retrospective authority-integration protocol. It is not an
untouched scientific preregistration. The six Session-4 cards, all card
outcomes, the Boolean selection rule, every small-word witness, the corrected
preauthority package, and the independent devil's-advocate verdict were known
before this file was written. Only the final corrected research inputs were
frozen before independent review.

The authority integration will reproduce already known exact claims. Its
code, vendored runtime dependencies, canonical Route card, and result bytes do
not exist when this document and `EXPERIMENT_PLAN.md` are frozen. This timing
earns no novelty, priority, prospective-validation, or outcome-independence
credit.

## 2. Frozen research and review inputs

The authority run accepts exactly these immutable release anchors:

| Input | SHA-256 |
|---|---|
| `preauthority/SHA256SUMS.txt` | `55214e6af4457ba22ea41d406524d6e94f7fe99c7274c08644822fe7505d41bb` |
| `preauthority/RESEARCH_LOCK.json` | `010b1633369fd0a0e622bdf22224145b860d139ec70cc3f5f30fe2fe5a01025a` |
| `preauthority/SOURCE_HASHES.sha256` | `773671adbfed36050f837d73378baa07237a338c21cf118915dc10cd0d123129` |
| `preauthority/ROUTE_EXPECTATION.yaml` | `54e0ad184799de8c12a93e64e7fcba09b0938725afec5362b621f2b9be88ff51` |
| `independent_da/paper41_DA_REPORT_v2.md` | `47644ea76e1f9b355052fa32ffcc02938ba1fbe18ee9fed96afa822043b7b8c1` |
| `independent_da/paper41_DA_REPORT_v2.sha256` | `209e2dca06b6bf339b1ad9f133d770a2fc6e1cd0dea8a318f8d7d68a5844678a` |

The package manifest must verify 15 of 15 entries, its self-excluding research
lock must verify 14 of 14 immutable mappings, and the typed source resolver
must verify 22 of 22 sorted unique portable IDs. The two dependency IDs are
resolved only through locally vendored, hash-checked bytes. No staging path or
external authority tree may be needed at runtime.

## 3. Ownership and write boundary

The integrator owns only:

- these two files under `experiments/`;
- `code/**`;
- integration-specific `docs/**`;
- `evaluations/route_a/SD-C43/**`;
- `results/**`;
- `EXPERIMENT_REPORT.md`.

The integrator must not modify `preauthority/**`, `independent_da/**`, the
mutable writer files at paper root, manuscript sources, bibliography,
figures, compilation products, or any future writer rendering. It also must
not create or change `PAPER_MANIFEST.sha256`, the symbolic-dynamics root
README, a candidate registry, Git state, or a mirror. Exact-set audits ignore
writer-owned paths but require the integration-owned sets to match their
contracts exactly.

## 4. Frozen mathematical targets

All calculations use

```text
L = [[1,1],[0,1]]
R = [[1,0],[1,1]]
M_w = M_w1 ... M_wk
h(w) = [1,1] M_w [1,0]^T
```

The exact witness ledger is:

```text
h(epsilon)=1, h(0)=1, h(1)=2,
h(01)=3, h(10)=2, h(11)=3,
h(001)=4, h(010)=3.
```

The source and both evaluators must independently establish:

1. the recurrence convention through all prefixes of length at most three;
2. append-one non-descent from `epsilon ~ 0` and `h(1) != h(01)`;
3. cyclic-clock failure from `h(01) != h(10)`;
4. power failure from `h(11) != h(1)^2`;
5. Liouville cyclic and power failures from the frozen length-three and
   repetition witnesses;
6. the one-letter-character contradiction;
7. the trace and matrix-power changed-clock positive controls;
8. the typed diagonal inventory identity, marker separation, trace-class
   domain, local trace-log domain, and eigenvalue-one factor, without
   conferring primitive-return ownership.

The experiment may check exact finite truncations of the diagonal inventory,
but it may not present such truncations as a proof of the inherited infinite
multiplicity theorem.

## 5. Retrospective selection resolver

A locally vendored normalized packet contains all decision-relevant fields
and original byte hashes for `SD-C01` through `SD-C06`. Both evaluators must
derive the literal rule independently. The exact result is the singleton
`[SD-C06]`. Candidate number, paper order, a hidden nontriviality predicate,
Paper 39 ranking, Paper 40 authorization, and witness outcomes are forbidden
selection inputs.

The emitted result must label the rule `RETROSPECTIVE_RESULTS_AND_WITNESSES_KNOWN`
and must set prospective, outcome-independent, preregistered, novelty-credit,
and priority-credit fields to false.

## 6. Strict Route-A v0.2 contract

The exact live `route-a-evaluator` v0.2.0 bytes, SHA-256
`29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a`,
must be vendored locally and decoded before use. The Route renderer must
validate the exact schema, evidence labels, layer verdict labels, artifact
paths, source-lock obligations, controls, and Route-B lock.

The canonical tuple is

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_FAIL,
 A2_FAIL,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FAIL)
```

with `overall_verdict: ROUTE_A_REJECTED` and
`route_b_invocation_allowed: false`. A valid diagonal determinant does not
earn A2, and the parameter-dependent diagonal inventory does not earn A4.
No target roots, zero fitting, or prime-table input is permitted.

## 7. Source/evaluator separation

The source generator emits canonical JSON from primitive fields and local
vendored inputs. It imports neither evaluator. The main evaluator consumes
only packet bytes and uses exact matrix multiplication. The independent
evaluator is a physically distinct module, imports neither source nor main
evaluator, and recomputes `h` primarily from the frozen recurrence with its
own integer and Liouville routines. No evaluator trusts aggregate PASS flags,
precomputed witness labels, the research Route expectation, or another
evaluator's projection.

Static inspection must enforce these import and dependency boundaries.

## 8. Mutation registry

Every declared mutation is executed against both evaluators. The registry
must cover at least:

- every matrix, word-order, recurrence, direct-limit, cyclic, power, and
  Liouville witness field class;
- the full type, marker, operator, determinant, domain, and terminal-code
  ledgers;
- all six selection-card records, hashes, predicate clauses, chronology
  flags, and hidden-predicate attempts;
- portable source-ID syntax, sorting, uniqueness, containment, dependency
  mapping, and hash substitution;
- the Route tuple, every layer verdict/status, mandatory metrics, controls,
  artifact paths, overall verdict, Route-B fields, and provenance triple;
- exact managed-result, managed-text, and immutable-ledger path sets;
- source/evaluator import and declared-dependency violations.

Acceptance requires zero mutation survivors in both implementations.

## 9. Reproduction, exact sets, and paired states

Fresh runs A and B must be byte-identical for the source packet, both science
evaluations, strict Route evaluation, and all deterministic projections. A
cold run C starts from a copied paper tree with every integration output,
cache, ledger, Route artifact, report, and paper manifest absent. It must run
from a non-project working directory and reproduce the same deterministic
bytes without reading any external historical tree.

The result ledger is sorted, unique, exact-set, self-excluding, and validates
every declared hash. Exact result and integration-text path inventories are
machine checked. Writer files are explicitly excluded from those inventories
and may not be rewritten.

The read-only integrity auditor accepts exactly two paired states:

- State A: `PAPER_MANIFEST.sha256` absent and the three Route provenance
  fields all equal `PENDING_FIRST_ARTIFACT_COMMIT` with the exact Stage-1
  note;
- State B: a hypothetical sorted self-excluding paper manifest is present,
  the three Route fields contain one identical lowercase nonzero 40-hex
  commit, and the exact metadata-only Stage-2 note is present.

The actual authority is left in State A. State B is tested only in an
isolated copy. Mixed, malformed, unsafe, stale-note, mismatched, duplicate,
unsorted, self-including, missing-path, extra-path, or bad-hash states fail.
The auditor itself writes nothing.

A final full rerun must report `changed_paths=0`. UTF-8/LF, one final LF,
zero trailing whitespace, zero control characters, no cache, no auxiliary
files, and no symlinks are mandatory.

## 10. Stop rules

Stop without publishing canonical results if any frozen input changes, a
portable ID does not resolve, evaluator projections differ, a mutation is
accepted, a type boundary is crossed, a Route obligation is omitted, a
deterministic byte differs across A/B/C, the paired-state audit depends on
the current state, an exact-set or ledger check fails, or an owned-path write
touches writer or immutable research material.

