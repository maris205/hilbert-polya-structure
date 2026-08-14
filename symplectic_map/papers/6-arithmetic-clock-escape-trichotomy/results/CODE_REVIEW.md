# Independent Pre-execution Code Review

**Candidate:** `additive_finite_arithmetic_capacity_v2`  
**Review date:** 2026-08-14 UTC  
**Reviewer role:** independent deployment and proof-consistency attacker  
**Verdict:** `DEPLOYMENT_FAIL`

Historical Round-1 machine record (inactive): {"candidate_id":"additive_finite_arithmetic_capacity_v2","reviewed_code_sha256":"76e523fa3b76bf4110cdbceb1210be2e57c1b2ca51561e563a4739717d8c9caf","reviewer_independent":true,"source_lock_sha256":"2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc","verdict":"DEPLOYMENT_FAIL"}

## Scope and execution discipline

I reviewed the version-2 source lock, proof package, proof and scope ledgers,
all executable Python modules, wrappers, and tests.  I ran syntax compilation,
the isolated development tests, and temporary-directory negative controls only.
I did **not** invoke the registered audit command, create an official experiment
report or registry, enumerate or retrieve primes, access Riemann-zero data,
evaluate a numerical logarithm, or compute a target match.

The supplied immutable values were independently reproduced:

- source-lock SHA-256:
  `2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc`;
- independent proof/novelty review SHA-256:
  `4036f346b75e44ff1acc8402cc1b17f497f3510ee0f4aa6456288f9856fbb63b`;
- reviewed pre-execution tree SHA-256:
  `76e523fa3b76bf4110cdbceb1210be2e57c1b2ca51561e563a4739717d8c9caf`.

The safe baseline completed with `29 passed` and syntax compilation succeeded.
Those facts do not override the fail-open deployment findings below.

## Mathematical and scope audit

### Main additive theorem: PASS

The normal form

\[
\log p=v_p+\log q_p+\alpha_p
\]

is used consistently.  A rational relation among the selected outside-support
terms is cleared to integer coefficients.  Positivity validates the real-log
product law for positive and negative powers.  Substitution gives
`log(R)=beta` with positive algebraic `R` and real algebraic `beta`.
Hermite--Lindemann forces `beta=0`, hence `R=1`; squaring produces only the
certified `q_p^2` factors.  Passing the finite set of factors to one number
field preserves unit status, and a place above each distinct outside prime
isolates its relation coefficient.  This proves rational independence and the
bound

\[
|\mathcal P_{\rm hit}|\leq\dim_{\mathbb Q}V+|S_{\mathbb Q}|.
\]

The proof correctly needs no prior finiteness assumption.  It treats the hit
collection as a set, chooses one arbitrary valid certificate per distinct
prime before a relation, allows `q=1`, rational powers and negative powers,
and uses only the real logarithm on positive inputs.

### Source-class and repair audit: PASS

All ten version-2 repairs are represented consistently in the human proof,
source lock, and structured ledgers:

1. the additive statement is primary and the selector statement is a
   corollary;
2. admitted and excluded operations are explicit;
3. the unit definition is stable under finite extension;
4. `q` is positive algebraic and the certified object is `q^2`;
5. the transcendence, squaring, and valuation spine is complete;
6. class M retains cyclic multiplicity, separate homogenization degrees, the
   projective-affine dimension step, good-reduction integrality, and normal
   saturation;
7. class L uses higher-block recoding;
8. class A distinguishes algebraicity from canonical gauge invariance and
   uses the positive-dimensional symbolic control;
9. set selection and power/log edge cases are explicit; and
10. escape gates are necessary failures of this certificate only, not an
    exhaustive, exclusive, sufficient, or universal trichotomy.

The proof ledger uses structured IDs rather than prose acceptance, is bound to
the source-lock and independent-review hashes, has the exact required ID set,
and has no missing dependencies or cycles.  The proof package is itself in the
reviewed-tree digest.  Its evidence anchors correspond to real headings,
although the validator does not mechanically resolve them; this is a minor
machine-audit limitation, not the reason for the deployment failure.

## Deployment blockers

### CR-01 — Result manifest accepts unaudited or malformed artifacts (critical)

`build_result_manifest` checks only that eight fixed paths satisfy `is_file`,
then hashes their bytes.  It does not reject symbolic links, require resolved
paths to remain inside the project, parse the JSON artifacts, reject duplicate
JSON keys, validate exact schemas and key sets, cross-check the result and run
registry, require a passing classification, verify the single-run invariants,
or reject unexpected result artifacts.

A temporary negative control supplied an external symbolic link as the review,
malformed text as the experiment JSON, duplicate keys in the run registry, and
an extra untracked result file.  The manifest nevertheless returned `pass=true`
with no missing paths.  Therefore the proposed immutable manifest can bless an
invalid or externally mutable result package.

Required repair: reject every symlink and non-regular file with `lstat`, enforce
resolved containment, parse JSON with duplicate-key rejection, validate exact
schemas/types/key sets and cross-artifact hashes/counters/classification, bind
the registered report to the reviewed code and source lock, and define and
enforce the exact allowed result-file set.  Add independent negative tests for
each failure mode.

### CR-02 — Review authority accepts mutable symlinks and ambiguous JSON (critical)

`validate_review_authority` follows `results/CODE_REVIEW.md` when it is a
symbolic link.  A temporary external review file carrying an otherwise valid
record was accepted.  Because the authority file is intentionally outside the
reviewed-tree hash, an external symlink makes deployment authority mutable
after review.

In addition, the authority parser uses ordinary `json.loads`; duplicate object
keys are silently resolved by the last value.  A record containing two
`candidate_id` keys, the first wrong and the second correct, passed.  Exact key
*sets* do not detect duplicate occurrences.

Required repair: require a regular, nonsymlink file whose resolved path is the
canonical in-project review path, and parse with an object-pairs hook that
rejects duplicate keys at every object level.  Preserve the exact five-field
schema and the one-column-one-record rule, and add both attacks to the test
suite.

### CR-03 — Upstream finality is self-attested (critical)

`validate_upstream_bindings` compares each proof package with a digest supplied
in the same newly created binding file and accepts the literal status
`FINAL_LOCAL`.  It has no independently locked expected final digest, no
upstream candidate/source-lock identity, and no authenticated final-integrity
record.  A temporary pair of files containing only `unfinished placeholder`,
with their freshly computed hashes and self-declared final statuses, passed the
gate.

This does not establish the required Paper-3/Paper-4 **final** theorem/hash
consistency.  Required repair: bind independently known final proof-package
digests (preferably through strict final-integrity records that themselves bind
candidate ID, final source, review verdict and PDF/result manifest) into a
frozen Paper-5 input or runtime constants.  Reject symlinks, duplicate JSON
keys, extra/missing fields, noncanonical paths, and any upstream status that is
not cryptographically tied to those final artifacts.

### CR-04 — Isolation scanner's claimed prohibitions are bypassable (major)

The scanner correctly covers its own module and both wrappers and reports zero
findings on the present executable tree.  Manual inspection also found no
current network client, numerical logarithm, target array, or candidate solver.
However, the scanner does not enforce the stronger property stated by the
source lock and plan.  Temporary executable modules passed with each of:

- `import_module` imported under an alias and used to load a network module;
- direct use of the builtin dynamic importer;
- a numerical logarithm reached through `getattr` and a dynamic import; and
- a target-named variable assigned indirectly from a numeric collection.

String-encoded numeric target collections and numeric values embedded in
formal labels are likewise outside its current AST checks.  Tree-hash binding
prevents an unnoticed post-review source change, but it does not make the
scanner's recorded isolation claim true or protect a later reviewed revision
unless the reviewer manually rediscovers every bypass.

Required repair: move to a restrictive allowlist for executable imports and
I/O/call sites, reject dynamic import/reflection primitives and their aliases,
track simple aliases and assignments (or forbid suspicious target/prime/zero
identifiers regardless of literal construction), scan relevant string
constants, and add the demonstrated bypasses as negative controls.

### CR-05 — Tests encode only the pre-review filesystem phase (major)

The deployment tests require the review and upstream files to be missing and
the manifest to be incomplete.  Consequently, creating this review file,
later adding valid upstream bindings, and finally producing official artifacts
make those tests fail by design.  The final package therefore cannot retain a
green reproducibility suite, and the registered command does not run or bind a
post-review test result.

Required repair: test closed and open states in isolated temporary fixtures,
not by asserting the live project is permanently incomplete.  Add a
post-authority/pre-run test phase and a post-run integrity phase.  The
single-run write should also use an exclusive/atomic creation mechanism rather
than a check-then-overwrite sequence.

## Other gates checked

- The source-lock validator reproduces the locked SHA-256, historical review
  provenance, ten repair IDs, clean pre-execution counters, and closed formal
  permissions.
- Canonical-readout records reject non-`Fraction` multiplier coefficients and
  undeclared support; exact controls remain symbolic except for the frozen
  rational boundary constant.
- Escape/output classifiers reject the enumerated broad claims and preserve
  the scoped necessary-failure semantics.
- No formal registered output, run registry, result manifest, target table,
  prime/zero data, or numerical candidate result was produced by this review.

## Final decision

The mathematical theorem and its ten repaired scope conditions pass the
independent audit, but the deployment authority, upstream-finality, isolation,
and result-integrity mechanisms are not fail closed.  The registered audit must
remain blocked.  After CR-01 through CR-05 are repaired, the entire reviewed
tree hash will change and a new independent pre-execution code review is
required before any official run.

## Author repair record — not independent deployment authority

**Repair role:** implementation author; `NOT INDEPENDENT`  
**Repair status:** `READY_FOR_INDEPENDENT_ROUND2_REVIEW`  
**Formal registered audit:** not run; remains blocked

The five failed-review items were repaired without changing the scientific
source lock:

1. The post-run manifest now enforces a flat exact result-file allowlist,
   rejects nested/extra/symlink/out-of-root artifacts, loads JSON with duplicate
   key rejection, checks exact result and registry schemas, binds source-lock
   and reviewed-tree hashes, cross-checks timestamps/result digest/counters,
   requires every registered gate to pass, and uses exclusive creation.
2. Review authority must now be a canonical regular in-project file. Its
   single JSON object is parsed with duplicate-key rejection and the exact
   five-field schema, source-lock hash, current reviewed-tree hash,
   independence flag, and passing verdict remain mandatory.
3. Upstream binding version 2 no longer accepts self-reported digests. Runtime
   constants independently freeze the Paper-3/Paper-4 candidate identities,
   source locks, proof-package hashes, and final-result-manifest hashes, then
   validate the internal final-manifest semantics. Because no binding file has
   yet been authored in this package, the live gate correctly remains
   `UPSTREAM_NOT_FINAL`; no upstream finality was fabricated.
4. The executable scanner now uses an import allowlist, resolves import/from
   aliases and direct callable aliases, forbids dynamic import and reflection
   primitives, and propagates simple numeric-collection taint into suspicious
   target/prime/zero assignments. Regression attacks cover aliased
   `import_module`, the builtin importer, reflected numerical log access, and
   indirect target arrays.
5. Lifecycle tests now use temporary fixtures for review-pass/upstream-pending,
   self-attested upstream rejection, and
   symlink/malformed/duplicate/extra/nested manifest rejection, while the live
   project correctly represents the failed Round-1 review and pre-run state.

Safe verification after repair: syntax compilation **PASS**; isolated suite
**37 passed in 0.14 s**; current executable scan **PASS** with zero findings.
The repaired reviewed-tree SHA-256 is
`44c5bb3b1d7c009e4409d5e91691f894161352237f530c16dcebe8715dee0370`;
the review report itself is deliberately outside that tree hash. The existing
independent `DEPLOYMENT_FAIL` authority remains the only machine authority and
correctly fails both verdict and stale-tree checks. A fresh independent
Round-2 review must bind the repaired current tree before any formal run.

No registered CLI, official result/registry/manifest, prime or Riemann-zero
data, numerical logarithm, target match, or network operation was used during
these repairs.

## Independent Round-2 pre-run code review

**Review date:** 2026-08-14 UTC  
**Reviewer role:** independent deployment, lifecycle, and proof-regression
reviewer; not the implementation author  
**Reviewed repaired tree:**
`44c5bb3b1d7c009e4409d5e91691f894161352237f530c16dcebe8715dee0370`  
**Source lock:**
`2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc`  
**Code verdict:** `DEPLOYMENT_FAIL`  
**Formal run:** closed

Historical Round-2 machine record (inactive): {"candidate_id":"additive_finite_arithmetic_capacity_v2","reviewed_code_sha256":"44c5bb3b1d7c009e4409d5e91691f894161352237f530c16dcebe8715dee0370","reviewer_independent":true,"source_lock_sha256":"2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc","verdict":"DEPLOYMENT_FAIL"}

### Review boundary

This review read the complete repaired implementation tree, the source lock,
proof and scope ledgers, proof package, prior review and repair record, and the
tests. It ran Python syntax compilation, isolated safe tests, direct parser and
scanner attacks, and temporary-directory lifecycle attacks. It did not invoke
the registered CLI, write an experiment result, registry, or result manifest,
enumerate or retrieve primes, access Riemann-zero data, evaluate a numerical
logarithm, or compute a target match. The only project write is this independent
review section and its machine authority; the review file is deliberately
outside the reviewed-tree digest.

### Reproduced immutable baseline

- `reviewed_code_tree_sha256(project_root)` exactly equals the repaired digest
  above.
- The source-lock digest exactly equals the frozen version-2 digest above, and
  `validate_source_lock` passes its history, ten-repair, zero-execution, and
  closed-permission checks.
- `python -m compileall -q -f code` succeeds.
- `PYTHONPATH=code pytest -q -p no:cacheprovider` reports **37 passed** in the
  current failed-authority/pre-run state.
- The current executable scan covers 12 Python files, including itself and both
  wrappers, and returns zero findings.

### Mathematical and ten-repair regression audit — PASS

The additive theorem remains correct. After selecting one certificate for each
distinct outside-support prime, a rational dependence of the corresponding
`V`-terms clears to an integer relation. Exact substitution gives
`log(R)=beta` with positive algebraic `R` and real algebraic `beta`.
Hermite--Lindemann forces `beta=0`, hence `R=1`; squaring leaves only the
certified `q_p^2` unit factors, and a place over each distinct outside prime
forces its relation coefficient to vanish. This proves the outside-prime
vectors rationally independent and gives the stated rank-plus-support bound
without a prior finiteness assumption.

All ten version-2 repairs remain represented in the proof package, source lock,
and structured ledgers: additive primacy; exact admitted/excluded operations;
extension-stable unit definition; positive algebraic `q` with certified square;
the complete transcendence/squaring/valuation spine; the repaired Class-M
projective, good-reduction, monodromy, normal-extension and saturation steps;
Class-L higher-block recoding; the Class-A algebraicity/gauge distinction and
positive-dimensional control; set, power, `q=1`, and real-log edge cases; and
necessary-only nonexhaustive escape semantics. No theorem or scope regression
was found.

### Round-1 blocker replay

#### R2-CR01 — Manifest hardening remains type-fail-open (critical)

Several Round-1 attacks are now rejected: strict JSON loading catches duplicate
keys; result/registry timestamp and digest mismatches fail; and the flat result
allowlist rejects extra, nested, symlinked, and externally resolved artifacts.
The post-run validator also checks the top-level key sets, frozen source-lock
and tree digests, classification, counters, registry digest, review gate, and
upstream gate.

The claimed strict schema is nevertheless incomplete. In a temporary otherwise
valid post-run fixture, I replaced both timestamps by the JSON number `7`,
encoded zero counters as JSON booleans, and encoded `registered_run_count` as
`true`. Because the validator does not type-check the timestamp and Python
equates `False == 0` and `True == 1`, `build_result_manifest` returned
`pass=true`. Gate records containing only `{"pass":true}` also satisfy the
current inner-gate check. Thus a package not conforming to the registered
report/registry types or gate-record schemas can still be blessed.

Required repair: validate every field's exact JSON type (explicitly exclude
`bool` from integer counters), parse a canonical UTC timestamp string, and
validate exact per-gate record schemas or recompute the registered gates from
the frozen inputs. Add separate positive and negative post-run fixtures so each
semantic path is actually executed.

#### R2-CR02 — Review authority repair — PASS

The authority gate now requires the canonical regular in-root review file,
rejects a symlink and symlinked parent path, parses with duplicate-key
rejection, requires exactly one column-one object and exact five-field schema,
and binds candidate ID, source-lock hash, independence, verdict, and the current
reviewed-tree digest. Duplicate, indented, quoted, extra-key, stale-tree, and
duplicate-JSON attacks all fail. The Round-2 authority above intentionally
binds the current tree and carries a failing verdict because of the unresolved
findings in this report.

#### R2-CR03 — Upstream finality can still be asserted before finalization (critical)

The arbitrary-placeholder self-attestation attack is fixed: hashes supplied
only by a binding file cannot replace the independently frozen runtime hashes,
and malformed, duplicate, unsafe, or nonexact bindings fail. The live missing
binding correctly returns `UPSTREAM_NOT_FINAL`.

However, finality itself is still not authenticated. Paper 3 currently reports
`ROUND1_REPAIRS_COMPLETE` with independent Round 2 and final integrity pending;
Paper 4 reports `PRE_REVIEW_COMPLETE`. I created only a temporary Paper-5
binding containing the runtime-frozen constants and the status literal required
by `upstream.py`. Against the already existing Paper-3/Paper-4 experiment
result manifests, `validate_upstream_bindings` returned top-level `pass=true`
for both records even though neither upstream is `FINAL_LOCAL`. The frozen
digests authenticate pre-final experiment packages, not completed manuscript
review/final-integrity state; the binding's status remains the only finality
assertion.

There is also a return-type defect in `_paper3_manifest_valid`: its final
`and` operand is a SHA-256 string, so the audit record serializes that string,
not a Boolean, for `manifest_semantics_pass` and the record-level `pass`.

Required repair: keep this gate unconditionally `UPSTREAM_NOT_FINAL` until each
upstream has a real, independently produced `FINAL_LOCAL` integrity record.
Then freeze and verify that record's digest and exact semantics, including the
candidate/source-lock/proof hashes, accepted independent review state, final
manuscript/PDF, and result manifest. A Paper-5 binding must reference those
external final records rather than create their status. Return strict Booleans
from every semantic predicate and add the current pre-final-packages attack as
a negative test.

#### R2-CR04 — Isolation scanner repair — PASS for the registered attack set

The restrictive import allowlist and alias resolution reject the Round-1
bypasses: aliased `import_module`, direct or aliased `__import__`, reflected
access through `getattr`, and numeric collections propagated through an
intermediate assignment into a target/prime/zero-named variable. The live
executable tree has no finding, numeric logarithm, network/process route,
floating literal, unreviewed I/O site, or candidate target array.

#### R2-CR05 — Lifecycle tests remain phase-dependent and incomplete (major)

The temporary review-pass/upstream-pending and arbitrary-placeholder upstream
fixtures are useful additions. The suite still contains
`test_live_failed_review_gate_remains_closed`, which requires the live authority
to fail specifically with `VERDICT_NOT_DEPLOYMENT_PASS`. Replacing this report's
authority by a passing Round-2 verdict would therefore make the final
post-review suite fail. This reproduces the original phase-transition defect.

The combined manifest attack test also does not exercise all behavior named in
its title. Its extra/nested/symlink findings cause the result-tree gate to stop
before post-run JSON parsing, so its malformed result and duplicate registry
are never passed to the strict semantic loader. There is no fully valid
post-run lifecycle test, no exact-type attack, and no isolated cross-artifact
semantic test.

Required repair: replace live-phase assertions with temporary closed- and
open-authority fixtures; add a passing post-authority/pre-run fixture and a
complete passing post-run fixture; then mutate one property per negative test,
including malformed JSON, duplicate keys, wrong types, cross-artifact
timestamp/hash/counter disagreements, extra/nested/symlink/outside paths, and
exclusive manifest creation. The whole suite must remain green after a future
passing authority and after legitimate upstream bindings appear.

### Final code decision

`DEPLOYMENT_FAIL`. The additive theorem, ten-repair closure, review-authority
parser, and registered scanner attacks pass, but R2-CR01, R2-CR03, and R2-CR05
remain deployment blockers. The registered audit must stay closed. Independently
of those code defects, the formal run also requires genuinely final Paper-3 and
Paper-4 integrity records; neither upstream is final at this review point.
Fixing the blockers changes the reviewed tree and therefore requires a fresh
independent code review and new authority before any formal run.

## Author repair record after independent Round 2 — not deployment authority

**Role:** `AUTHOR_REPAIR_NOT_INDEPENDENT`  
**Repair date:** 2026-08-14 UTC  
**Independent Round-2 verdict being repaired:** `DEPLOYMENT_FAIL`  
**Repair status:** `READY_FOR_FRESH_INDEPENDENT_REVIEW`  
**Formal registered audit:** not run; remains closed

This section records implementation work only. It does not alter the sole
machine authority above, does not claim `DEPLOYMENT_PASS`, and cannot authorize
the registered run.

### R2-CR01: exact post-run semantics

The manifest validator now enforces exact JSON types before semantic equality:
timestamps must be canonical timezone-aware UTC ISO strings; counters must be
actual JSON integers with Python booleans explicitly excluded; flags and
top-level `pass` must be actual booleans. The post-run validator recomputes all
nine safe gate records from the current source lock, reviewed tree, review,
ledgers, controls, scanner, upstream closure, escape semantics, and output
scope, then compares the submitted gate object by canonical JSON. A minimal
`{"pass":true}` record, an extra/missing key, wrong enum, stale path/hash, or a
Boolean substituted for an integer therefore cannot pass.

Separate tests now reach strict parsing with an otherwise exact flat result
tree and reject malformed JSON and duplicate keys. Further one-property tests
reject wrong result/registry types, inner-gate truncation, timestamp mismatch,
and each flat-tree attack (extra, nested, and symlink/out-of-root result).

### R2-CR03: authenticated upstream finality

An upstream binding now names and hashes the actual source lock, proof package,
final result manifest, `paper/PIPELINE_STATE.json`, `paper/FINAL_INTEGRITY.md`,
`paper/paper_final.pdf`, and independent Round-2 review. Every path must be the
canonical regular in-paper path, every digest must equal an independently
frozen runtime constant, and the pipeline must have `stage=COMPLETE_LOCAL`, one
completed final-integrity stage, an accepted independent Round-2 stage, and a
completed final PDF whose review/PDF hashes and page count agree with the
evidence indexes. The binding's status string is no longer evidence by itself.

All manifest and pipeline predicates now return strict Booleans. Paper 3's
current terminal package passes the actual-artifact closure at its independently
frozen hashes. Paper 4 intentionally has no frozen terminal hashes while its
pipeline remains `PRE_REVIEW_COMPLETE`, so a binding cannot promote it: the
combined upstream gate remains `UPSTREAM_NOT_FINAL:PAPER4_ALGEBRAIC_ACTION_CLOCKS`.
After Paper 4 genuinely completes, its independently reviewed terminal hashes
must be frozen in code; that code change will itself require a fresh tree-bound
review before a formal run.

### R2-CR05: phase-independent lifecycle tests

The live failed-authority and live missing-output assertions were removed.
Authority fail/pass, upstream missing/final, and post-run complete states now
use isolated parameterized fixtures. The suite contains a fully valid post-run
fixture, then mutates one property per negative test. Consequently it remains
green when the live authority later changes from fail to pass and when a valid
binding/result package is legitimately installed. The malformed/duplicate JSON
tests explicitly assert that the flat result-tree gate passed before strict
semantic rejection, so those branches are no longer masked by an earlier
allowlist failure.

### Safe repair verification

- Repaired reviewed-tree SHA-256:
  `464dacc999e940b483f568d0b5a5398a2a2a1ed9e58abe6cb9f7a4fe1ec1220e`.
- Source-lock SHA-256 remains:
  `2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc`.
- `python -m compileall -q -f code`: PASS.
- `PYTHONPATH=code pytest -q -p no:cacheprovider`: **49 passed**.
- Executable isolation: PASS, 12 files scanned, zero findings.
- Actual terminal-artifact replay: Paper 3 PASS; Paper 4
  `UPSTREAM_NOT_FINAL`; combined gate closed.
- Registered CLI, official result/registry/manifest creation, prime/zero data,
  numerical logarithms, and target matching: not used.

The next permitted step is a fresh independent code review bound to the new
tree digest. This author record is not that review.

## Independent Round-3 pre-run code review

**Review date:** 2026-08-14 UTC  
**Reviewer role:** fresh independent deployment, lifecycle, proof-regression,
and adversarial-fixture reviewer; not the implementation author  
**Reviewed repaired tree:**
`464dacc999e940b483f568d0b5a5398a2a2a1ed9e58abe6cb9f7a4fe1ec1220e`  
**Source lock:**
`2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc`  
**Code verdict:** `DEPLOYMENT_PASS`  
**Formal run:** still closed by nonfinal Paper 4 upstream state

Historical Round-3 machine record (inactive): {"candidate_id":"additive_finite_arithmetic_capacity_v2","reviewed_code_sha256":"464dacc999e940b483f568d0b5a5398a2a2a1ed9e58abe6cb9f7a4fe1ec1220e","reviewer_independent":true,"source_lock_sha256":"2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc","verdict":"DEPLOYMENT_PASS"}

### Review boundary and immutable baseline

I read the full version-2 source lock, research question, proof sketch, proof
package, independent proof/novelty report, proof and scope ledgers, all twelve
executable Python files, both wrappers, and all tests. I performed syntax
compilation, isolated unit and lifecycle tests, parser/scanner attacks, strict
post-run manifest fixtures, and temporary-directory upstream-binding attacks.
I did **not** invoke either registered wrapper, create an official report,
registry, result manifest, or upstream binding in the project, enumerate or
retrieve primes, access Riemann-zero data, evaluate a numerical logarithm, or
compute a target match. This review section and the replacement of the stale
Round-2 marker by its explicitly inactive historical record are the only
project edits; the review file is deliberately excluded from the reviewed-tree
digest.

The source-lock and reviewed-tree hashes independently reproduce the values
above. The independent proof/novelty report reproduces
`4036f346b75e44ff1acc8402cc1b17f497f3510ee0f4aa6456288f9856fbb63b`.
Forced syntax compilation succeeds, and the complete isolated suite reports
**49 passed in 0.23 s**. The live executable scan covers twelve files,
including the scanner and both wrappers, and reports zero findings. The
project contains only this review under `results/`; the registered result,
run registry, result manifest, and Paper-5 upstream binding remain absent.

### Additive theorem and ten-repair regression — PASS

The main proof remains sound. Choose one certificate for each distinct
outside-support prime before considering a relation. Clearing rational
denominators and substituting the selected certificates yields
`log(R)=beta`, with positive algebraic `R` and real algebraic `beta` even in
the presence of negative powers. Hermite--Lindemann forces `beta=0` and
`R=1`; squaring leaves only the certified squared-unit factors. After passing
the finitely many factors to one number field, extension invariance preserves
their zero valuations outside the fixed support, and a place above each
distinct outside prime forces the corresponding integer coefficient to be
zero. Thus the selected `V` terms are rationally independent and the
rank-plus-support bound follows without assuming the hit set finite.

All ten mandated version-2 repairs remain closed: additive primacy and selector
demotion; exact admitted/excluded operations; extension-stable unit semantics;
positive algebraic `q` with `q^2` certified; the full transcendence, squaring,
and valuation spine; Class-M cyclic multiplicities, separate homogenization
degrees, projective-affine dimension step, good-reduction integrality,
determinant-one monodromy, normal extension, and support saturation; Class-L
higher-block recoding; Class-A algebraicity versus gauge invariance and the
positive-dimensional symbolic injection control; set/selection, rational and
negative-power, `q=1`, and real-log edge cases; and necessary-only,
nonexclusive, nonexhaustive, nonsufficient escape semantics. The source-lock
gate reports ten repairs and clean zero-execution provenance; the 20-ID proof
ledger has no missing dependency or cycle; the scope ledger has exactly ten
admitted and nine excluded operations; and all six exact controls pass with
zero computed matches.

### Round-2 manifest blocker replay — PASS

An otherwise exact temporary post-run package passes. One-property attacks
then fail in the intended semantic branch while the flat result-tree gate
continues to pass:

- numeric or noncanonical timestamps are rejected;
- JSON booleans substituted for zero counters or the one-run count are
  rejected as wrong exact types;
- a truncated inner gate or an extra inner-gate field is rejected because the
  submitted nine-gate object differs from the recomputed canonical records;
- a cross-artifact timestamp mismatch is rejected; and
- malformed result JSON, duplicate result keys, and duplicate registry keys
  all reach strict parsing and fail with the corresponding decode or
  duplicate-key error.

This closes the prior `bool == int`, timestamp, counter, masked-branch, and
minimal-inner-record attacks. The result and registry schemas, classifications,
source/tree hashes, counters, timestamps, result digest, all nine gate records,
and exact flat result allowlist are now mutually bound.

### Round-2 upstream-finality blocker replay — PASS, gate correctly pending

I copied the currently available upstream artifacts to an isolated directory
and supplied exact bindings. Paper 3 passes manifest semantics, terminal
pipeline semantics, all frozen cross-hashes, and the record-level strict
Boolean gate. Paper 4 fails terminal closure, so the combined result is exactly
`UPSTREAM_NOT_FINAL:PAPER4_ALGEBRAIC_ACTION_CLOCKS`. Its live pipeline is not
terminal and the required final integrity, final PDF, and independent Round-2
review are absent at review time.

The previous self-attestation route is closed. The binding already used the
required final-status literal; adding temporary fake Paper-4 terminal files did
not promote it. Mutating Paper 3's bound final-PDF hash demoted Paper 3, and a
duplicate-key binding failed strict loading. Both manifest-semantic and
record-level `pass` outputs are actual Booleans. Paper 4's terminal hashes are
intentionally unavailable in the frozen runtime constants, so no Paper-5
binding can declare it final.

When Paper 4 genuinely reaches `COMPLETE_LOCAL`, its independently reviewed
terminal hashes must be frozen into `upstream.py`. That necessary code change
will alter the reviewed-tree digest and automatically stale this Round-3
authority; a fresh tree-bound review is therefore required before the formal
run. The present code review passes, but it does not waive or pre-approve that
future upstream update.

### Lifecycle, authority, and isolation regression — PASS

The isolated lifecycle suite explicitly passes failed and passing review
authority phases, missing and terminal upstream phases, a complete post-run
phase, and malformed/duplicate post-run semantic attacks. No live-state test
depends on the authority remaining failed, so installing this passing marker
does not make the suite phase-inconsistent.

Authority replay rejects duplicate occurrences, indented markers, duplicate
JSON keys, and stale code hashes while accepting one exact column-one marker.
The scanner replay rejects a direct network import, an aliased dynamic import,
the builtin dynamic importer, reflected numerical-log access, and an indirect
numeric target array. Manual review of the fixed bound tree found no alternate
network, subprocess, numerical-log, tolerance, target-table, or unreviewed I/O
route. The scanner remains a defense for this fixed reviewed tree rather than
a semantic theorem about arbitrary future obfuscated Python; the tree digest
and mandatory fresh review protect future revisions.

### Final Round-3 decision

`DEPLOYMENT_PASS` for the code tree bound above. The three Round-2 blockers are
closed, the Round-1 authority and scanner attacks remain closed, and no
mathematical or ten-repair regression was found. This authority opens only the
independent-code-review gate. The registered audit remains fail-closed because
Paper 4 is not final and no Paper-5 upstream binding exists. No registered or
official command is authorized until the genuine Paper-4 terminal package is
frozen, the resulting changed Paper-5 tree receives a fresh independent pass,
and the upstream gate itself validates both final packages.

## Author terminal-upstream binding record — not independent authority

**Role:** `AUTHOR_BINDING_NOT_INDEPENDENT`  
**Binding date:** 2026-08-14 UTC  
**Scientific source lock/theorem:** unchanged  
**Registered/official audit:** not run  
**Fresh independent review required:** yes

Paper 4 subsequently reached genuine `COMPLETE_LOCAL` status after its
independent Round-2 manuscript review. Acting only as a mechanical binding
implementer, I rehashed the actual Paper-3 and Paper-4 source locks, proof
packages, final result manifests, terminal pipeline states, final integrity
records, final PDFs, and Round-2 reviews. I froze those exact values in
`capacity_audit/upstream.py` and wrote the strict corresponding records to
`experiments/upstream_bindings.json`.

The Paper-4 terminal values are:

- source lock:
  `d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7`;
- proof package:
  `c579e2da093a8ab588a5818bab0df59a47804792fcdfa338777f48e1bd1a1214`;
- final result manifest:
  `6b3dbfed68dbd058056c35139756d5ccbb4e9f3b9a263ccaddef64bb183326e7`;
- terminal pipeline:
  `2e49c5025360648c8eedd2c1110a21c835b970194f3d96fb6fdfb35377f1904e`;
- final integrity:
  `6239c69703d555f9607db6409817870d438a934089491295c0df24b2d0038d1e`;
- approved final PDF:
  `871197f5a385f68accf6d3ba7876e5df830e9eef43b4bf9e9ae52a3edb7bc996`;
- independent Round-2 review:
  `ca3d789bdcc3b4040be0338238a6f67cde5c76ea59a4f7b7f90d74484c060d71`.

Terminal validation now requires the package-specific Paper-3 or Paper-4
pipeline schema, exact candidate/paper identity, `COMPLETE_LOCAL` and terminal
final status, an independently accepted Round-2 stage with exact integer zero
remaining issues, unchanged science, forbidden-data false flags, matching
review/PDF evidence indexes, and every external file digest. A regression test
shows that setting Paper 4's author-self-check flag as if it were independent
fails even while its status strings remain terminal; replacing the zero issue
count by JSON `false` also fails.

Safe author verification after binding:

- syntax compilation: PASS;
- isolated suite: **51 passed in 0.25 s**;
- executable scan: PASS, twelve files, zero findings;
- actual Paper-3 upstream record: PASS;
- actual Paper-4 upstream record: PASS;
- combined upstream gate: PASS;
- reviewed tree after binding:
  `10fd57b1f99616799f05c3b6a4ce11a9e8ea747d33bb50299aac618948482fb7`.

This record does not issue or modify machine authority. The Round-3 authority
binds `464dacc...1220e`, so it correctly fails the changed tree with
`REVIEWED_CODE_SHA256_MISMATCH`. The registered audit therefore remains
closed until a fresh independent reviewer inspects and authorizes the current
tree. No result, run registry, result manifest, candidate match, prime/zero
dataset, numerical logarithm, or official output was created.

## Independent final tree-bound pre-run review

**Review date:** 2026-08-14 UTC  
**Reviewer role:** fresh independent final deployment, upstream-provenance,
lifecycle, and adversarial-fixture reviewer; not the implementation or binding
author  
**Reviewed current tree:**
`10fd57b1f99616799f05c3b6a4ce11a9e8ea747d33bb50299aac618948482fb7`  
**Source lock:**
`2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc`  
**Upstream binding:**
`654dcd13336e0dea7d4ae49a165601cae31f83db418316a5c356f1b108c40d2e`  
**Verdict:** `DEPLOYMENT_PASS`  
**Formal run:** authorized by the pre-run gates, but not executed in this
review

CAPACITY_AUDIT_CODE_REVIEW_V1 {"candidate_id":"additive_finite_arithmetic_capacity_v2","reviewed_code_sha256":"10fd57b1f99616799f05c3b6a4ce11a9e8ea747d33bb50299aac618948482fb7","reviewer_independent":true,"source_lock_sha256":"2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc","verdict":"DEPLOYMENT_PASS"}

### Review boundary and reproducible baseline

I reviewed the terminal-binding delta against the independently passed Round-3
tree, the strict upstream validator and frozen constants, the exact binding,
deployment/lifecycle tests, source/proof/scope ledgers, manifest semantics,
scanner, wrappers, and prior review chronology. I ran forced Python syntax
compilation and the isolated noncandidate suite: **51 passed in 0.23 s**. The
current executable scan remains clean over all twelve Python files. I did not
invoke either registered or official wrapper, write a result, registry, or
result manifest, enumerate or retrieve primes, access Riemann-zero data,
evaluate a numerical logarithm, use the network, or compute a target match.

The current tree, source lock, and binding independently reproduce the three
hashes above. Before installing this authority, the Round-3 marker failed
closed with exactly `REVIEWED_CODE_SHA256_MISMATCH`, establishing that the
terminal-binding edit was not silently covered by the old review.

### Actual upstream terminal replay — G110 PASS

The validator re-read and rehashed all seven terminal artifacts for each
upstream package rather than trusting binding status text. Paper 3 reproduced
source lock `3ae16233...d269`, proof package `2c536656...afdd`, final result
manifest `e47c93cc...863`, terminal pipeline `61ec1ff8...592f`, final integrity
`29d271c5...b43`, final PDF `f7368ecf...3156`, and independent Round-2 review
`9cd87c61...f8e9`. Paper 4 reproduced source lock `d15f5084...49d7`, proof
package `c579e2da...214`, final result manifest `6b3dbfed...26e7`, terminal
pipeline `2e49c502...904e`, final integrity `6239c697...8d1e`, final PDF
`871197f5...996`, and independent Round-2 review `ca3d789b...0d71`.

For both records, frozen-constant equality, final-result-manifest semantics,
package-specific terminal pipeline semantics, independent-review/PDF
cross-hashes, exact candidate identity, strict JSON types, zero remaining
issues, unchanged-science flags, and forbidden-data false flags all pass.
`G110` returns two record-level strict Boolean passes, no errors, and a strict
Boolean combined pass.

### Adversarial and regression replay — PASS

The isolated lifecycle/adversarial fixtures retain the Round-3 additive,
20-ID proof-ledger, ten-repair, scope, six-control, result-manifest, authority,
scanner, and phase-independent lifecycle gates. In particular:

- the stale Round-3 authority fails on the changed tree;
- placeholder/fake terminal artifacts and digest self-attestation cannot
  promote an upstream record;
- mutation of a bound artifact or a manifest/pipeline/review/PDF cross-hash
  fails the relevant record and the combined gate;
- duplicate keys, extra/missing fields, noncanonical paths, symlinks, wrong
  candidate identity, and Boolean-for-integer terminal fields fail closed;
- a terminal-looking Paper-4 record with an author self-check substituted for
  independent review fails; and
- malformed, stale, wrong-type, cross-artifact, extra/nested/symlink, dynamic
  import, reflected numerical-log, and indirect target-array attacks remain
  rejected.

No regression was found in the additive theorem or its scope: one certificate
is selected per distinct prime, rational denominators and negative powers are
handled before Hermite--Lindemann and valuation isolation, and escape labels
remain necessary failures of this certificate only. No formal output label is
reachable through self-report or prose acceptance.

### Final decision

`DEPLOYMENT_PASS` for the exact current tree bound above. The terminal-binding
delta is authentic, both actual upstream packages close under strict terminal
semantics, `G110` is fully green, and all 51 safe tests pass without weakening
the Round-1--Round-3 repair gates. This is the sole active machine authority;
the prior Round-3 record is explicitly historical. The formal registered
exact/static audit may now run once under its single-run and immutable-result
protocol. This review itself created no registered or official artifact and
used no prime or Riemann-zero data.
